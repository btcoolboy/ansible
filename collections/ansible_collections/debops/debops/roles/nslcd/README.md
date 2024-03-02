### nslcd

The `nslcd` daemon, part of the
[nss-pam-ldapd](https://arthurdejong.org/nss-pam-ldapd/) software
package, is used to look up user, group or other information stored in
LDAP that is related to UNIX accounts or groups. It is needed if you
want to use the `posixAccount` and `posixGroup` LDAP objects to
authenticate to the UNIX-like hosts.

The `debops.nslcd` Ansible role can be used to configure the `nslcd`
service on a host and, via `debops.ldap` role, create a bind account in
the LDAP directory used by `nslcd` to perform LDAP lookups.

Read the [nslcd role documentation](https://docs.debops.org/en/HEAD/ansible/roles/nslcd/) for more details.
