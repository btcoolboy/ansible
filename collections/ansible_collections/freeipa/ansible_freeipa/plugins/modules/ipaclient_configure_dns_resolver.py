# -*- coding: utf-8 -*-

# Authors:
#   Thomas Woerner <twoerner@redhat.com>
#
# Based on ipaplatform/redhat/tasks.py code from Christian Heimes
#
# Copyright (C) 2022 Red Hat
# see file 'COPYING' for use and warranty information
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.0',
    'supported_by': 'community',
    'status': ['preview'],
}

DOCUMENTATION = """
---
module: ipaclient_configure_dns_resolver
short_description: Configure DNS resolver for IPA client
description:
  Configure DNS resolver for IPA client, register files for installer
options:
  nameservers:
    description: The nameservers, required with state:present.
    type: list
    elements: str
    required: false
  searchdomains:
    description: The searchdomains, required with state:present.
    type: list
    elements: str
    required: false
  state:
    description: The state to ensure.
    type: str
    choices: ["present", "absent"]
    default: present
    required: false
author:
  - Thomas Woerner (@t-woerner)
"""

EXAMPLES = """
# Ensure DNS nameservers and domain are configured
- freeipa.ansible_freeipa.ipaclient_configure_dns_resolver:
    nameservers: groups.ipaservers
    searchdomains: "{{ ipaserver_domain | default(ipaclient_domain) }}"
# Ensure DNS nameservers and domain are not configured
- freeipa.ansible_freeipa.ipaclient_configure_dns_resolver:
    state: absent
"""

RETURN = """
"""

import os
import os.path

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.freeipa.ansible_freeipa.plugins.module_utils.ansible_ipa_client import (
    check_imports, services, tasks, paths, sysrestore, CheckedIPAddress
)
try:
    from ipalib.installdnsforwarders import detect_resolve1_resolv_conf
except ImportError:
    def detect_resolve1_resolv_conf():
        """
        Detect if /etc/resolv.conf is managed by systemd-resolved.

        See man(5) NetworkManager.conf
        """
        systemd_resolv_conf_files = {
            "/run/systemd/resolve/stub-resolv.conf",
            "/run/systemd/resolve/resolv.conf",
            "/lib/systemd/resolv.conf",
            "/usr/lib/systemd/resolv.conf",
        }

        try:
            dest = os.readlink(paths.RESOLV_CONF)
        except OSError:
            # not a link
            return False
        # convert path relative to /etc/resolv.conf to abs path
        dest = os.path.normpath(
            os.path.join(os.path.dirname(paths.RESOLV_CONF), dest)
        )
        return dest in systemd_resolv_conf_files


if hasattr(paths, "SYSTEMD_RESOLVED_IPA_CONF"):
    SYSTEMD_RESOLVED_IPA_CONF = paths.SYSTEMD_RESOLVED_IPA_CONF
else:
    SYSTEMD_RESOLVED_IPA_CONF = "/etc/systemd/resolved.conf.d/zzz-ipa.conf"


if hasattr(paths, "NETWORK_MANAGER_IPA_CONF"):
    NETWORK_MANAGER_IPA_CONF = paths.NETWORK_MANAGER_IPA_CONF
else:
    NETWORK_MANAGER_IPA_CONF = "/etc/NetworkManager/conf.d/zzz-ipa.conf"


NM_IPA_CONF = """
# auto-generated by IPA client installer
[main]
dns={dnsprocessing}
[global-dns]
searches={searches}
[global-dns-domain-*]
servers={servers}
"""


RESOLVE1_IPA_CONF = """
# auto-generated by IPA client installer
[Resolve]
# use DNS servers
DNS={servers}
# make default DNS server, add search suffixes
Domains=~. {searchdomains}
"""


def configure_dns_resolver(nameservers, searchdomains, fstore=None):
    """
    Configure global DNS resolver (e.g. /etc/resolv.conf).

    :param nameservers: list of IP addresses
    :param searchdomains: list of search domaons
    :param fstore: optional file store for resolv.conf backup
    """
    if not nameservers or not isinstance(nameservers, list):
        raise AssertionError("nameservers must be of type list")
    if not searchdomains or not isinstance(searchdomains, list):
        raise AssertionError("searchdomains must be of type list")

    changed = False
    if fstore is not None and not fstore.has_file(paths.RESOLV_CONF):
        fstore.backup_file(paths.RESOLV_CONF)
        changed = True

    resolve1_enabled = detect_resolve1_resolv_conf()
    if "NetworkManager" not in services.knownservices:
        # NetworkManager is not in wellknownservices for old IPA releases
        # Therefore create own service for it.
        nm_service = services.service("NetworkManager.service")
    else:
        nm_service = services.knownservices['NetworkManager']

    # At first configure systemd-resolved
    if resolve1_enabled:
        if not os.path.exists(SYSTEMD_RESOLVED_IPA_CONF):
            confd = os.path.dirname(SYSTEMD_RESOLVED_IPA_CONF)
            if not os.path.isdir(confd):
                os.mkdir(confd)
                # owned by root, readable by systemd-resolve user
                os.chmod(confd, 0o755)
                tasks.restore_context(confd, force=True)

            # Additionally to IPA server code also set servers
            cfg = RESOLVE1_IPA_CONF.format(
                servers=' '.join(nameservers),
                searchdomains=" ".join(searchdomains)
            )
            with open(SYSTEMD_RESOLVED_IPA_CONF, "w") as outf:
                os.fchmod(outf.fileno(), 0o644)
                outf.write(cfg)

            tasks.restore_context(
                SYSTEMD_RESOLVED_IPA_CONF, force=True
            )

            if "systemd-resolved" in services.knownservices:
                sdrd_service = services.knownservices["systemd-resolved"]
            else:
                sdrd_service = services.service("systemd-resolved.service")
            if sdrd_service.is_enabled():
                sdrd_service.reload_or_restart()
            changed = True

    # Then configure NetworkManager or resolve.conf
    if nm_service.is_enabled():
        if not os.path.exists(NETWORK_MANAGER_IPA_CONF):
            # write DNS override and reload network manager to have it create
            # a new resolv.conf. The file is prefixed with ``zzz`` to
            # make it the last file. Global dns options do not stack and last
            # man standing wins.
            if resolve1_enabled:
                # push DNS configuration to systemd-resolved
                dnsprocessing = "systemd-resolved"
            else:
                # update /etc/resolv.conf
                dnsprocessing = "default"

            cfg = NM_IPA_CONF.format(
                dnsprocessing=dnsprocessing,
                servers=','.join(nameservers),
                searches=','.join(searchdomains)
            )
            with open(NETWORK_MANAGER_IPA_CONF, 'w') as outf:
                os.fchmod(outf.fileno(), 0o644)
                outf.write(cfg)
            # reload NetworkManager
            nm_service.reload_or_restart()
            changed = True

    # Configure resolv.conf if NetworkManager and systemd-resoled are not
    # enabled
    elif not resolve1_enabled:
        # no NM running, no systemd-resolved detected
        # fall back to /etc/resolv.conf
        cfg = [
            "# auto-generated by IPA installer",
            "search %s" % ' '.join(searchdomains),
        ]
        for nameserver in nameservers:
            cfg.append("nameserver %s" % nameserver)
        with open(paths.RESOLV_CONF, 'w') as outf:
            outf.write('\n'.join(cfg))
        changed = True

    return changed


def unconfigure_dns_resolver(fstore=None):
    """
    Unconfigure global DNS resolver (e.g. /etc/resolv.conf).

    :param fstore: optional file store for resolv.conf restore
    """
    changed = False

    if fstore is not None and fstore.has_file(paths.RESOLV_CONF):
        fstore.restore_file(paths.RESOLV_CONF)
        changed = True

    if os.path.isfile(NETWORK_MANAGER_IPA_CONF):
        os.unlink(NETWORK_MANAGER_IPA_CONF)
        if "NetworkManager" not in services.knownservices:
            # NetworkManager is not in wellknownservices for old IPA releases
            # Therefore create own service for it.
            nm_service = services.service("NetworkManager.service")
        else:
            nm_service = services.knownservices['NetworkManager']
        if nm_service.is_enabled():
            nm_service.reload_or_restart()
        changed = True

    if os.path.isfile(SYSTEMD_RESOLVED_IPA_CONF):
        os.unlink(SYSTEMD_RESOLVED_IPA_CONF)
        if "systemd-resolved" in services.knownservices:
            sdrd_service = services.knownservices["systemd-resolved"]
        else:
            sdrd_service = services.service("systemd-resolved.service")
        if sdrd_service.is_enabled():
            sdrd_service.reload_or_restart()
        changed = True

    return changed


def main():
    module = AnsibleModule(
        argument_spec=dict(
            nameservers=dict(type="list", elements="str", required=False),
            searchdomains=dict(type="list", elements="str", required=False),
            state=dict(type="str", default="present",
                       choices=["present", "absent"]),
        ),
        supports_check_mode=False,
    )

    check_imports(module)

    nameservers = module.params.get('nameservers')
    searchdomains = module.params.get('searchdomains')

    state = module.params.get("state")

    if state == "present":
        required = ["nameservers", "searchdomains"]
        for param in required:
            value = module.params.get(param)
            if value is None or len(value) < 1:
                module.fail_json(
                    msg="Argument '%s' is required for state:present" % param)
    else:
        invalid = ["nameservers", "searchdomains"]
        for param in invalid:
            if module.params.get(param) is not None:
                module.fail_json(
                    msg="Argument '%s' can not be used with state:present" %
                    param)

    # Check nameservers to contain valid IP addresses
    if nameservers is not None:
        for value in nameservers:
            try:
                CheckedIPAddress(value)
            except Exception as e:
                module.fail_json(
                    msg="Invalid IP address %s: %s" % (value, str(e)))

    fstore = sysrestore.FileStore(paths.IPA_CLIENT_SYSRESTORE)

    if state == "present":
        changed = configure_dns_resolver(nameservers,
                                         searchdomains, fstore)
    else:
        changed = unconfigure_dns_resolver(fstore)

    module.exit_json(changed=changed)


if __name__ == '__main__':
    main()
