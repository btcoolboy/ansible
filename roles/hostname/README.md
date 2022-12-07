## hostname

[![CI](https://github.com/Oefenweb/ansible-hostname/workflows/CI/badge.svg)](https://github.com/Oefenweb/ansible-hostname/actions?query=workflow%3ACI)
[![Ansible Galaxy](http://img.shields.io/badge/ansible--galaxy-hostname-blue.svg)](https://galaxy.ansible.com/Oefenweb/hostname)

Set or update the hostname in Debian-like systems.

#### Requirements

None

#### Variables

This role depends on your ansible hosts inventory.

Add the hosts to your inventory with their `FQDN` (e.g. `foo.bar.com`), and the role will take care of setting your hostname accordingly (`hostname`: `foo`, `FQDN`: `foo.bar.com`).

If you just name it with the hostname in the inventory, it will similarly work (`hostname` set, but no `FQDN` attached to it).

* `hostname_hostname`: [default: `"{{ inventory_hostname }}"`]: FQDN
* `hostname_hostname_short`: [default: `"{{ inventory_hostname_short }}"`]: Hostname
* `hostname_hostname_use_full`: [default: `false`]: If set to `true` `hostname` equal `FQDN`
* `hostname_hostname_ip_address`: [default: `127.0.1.1`]: `FQDN` and `shortname` resolve to this
* `hostname_additional_hosts`: [default: `[]`]: Hosts declaration
* `hostname_additional_hosts.{n}.ip_address`: [required]: IP address
* `hostname_additional_hosts.{n}.hostname`: [required]: FQDN
* `hostname_additional_hosts.{n}.hostname_short`: [required]: Hostname

* `hostname_use_strategy`: [optional]: Which strategy to use to update the hostname (Ansible `>= 2.9`)

## Dependencies

None

#### Example

Your **inventory** file should look like this:

```ini
foo.bar.com ansible_ssh_host=1.2.3.4
baz.bar.com ansible_ssh_host=5.6.7.8
```

And the structure of the files in your **host_vars** folders should match accordingly:

```bash
# ls host_vars/ -l
total 4
-rw-rw-r-- 1 foo bar  0 aug 14 11:51 foo.bar.com.yml
-rw-rw-r-- 1 foo bar 29 aug 14 21:01 baz.bar.com.yml
```

**foo.bar.com.yml** could look like this:
```yaml
hostname_additional_hosts:
  - ip_address: 1.2.3.4
    hostname: a.example.com
  - ip_address: 5.6.7.8
    hostname: b.example.com
    hostname_short: b
```

This will create the following **/etc/hosts** file:
```bash
# cat /etc/hosts
127.0.0.1 localhost
127.0.1.1 foo.bar.com foo

# The following lines are desirable for IPv6 capable hosts
::1 ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
ff02::3 ip6-allhosts

1.2.3.4 a.example.com
5.6.7.8 b.example.com b
```

#### License

MIT

#### Author Information

Mischa ter Smitten (based on work of [ANXS](https://github.com/ANXS))

#### Feedback, bug-reports, requests, ...

Are [welcome](https://github.com/Oefenweb/ansible-hostname/issues)!
