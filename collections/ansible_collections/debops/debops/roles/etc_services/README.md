### etc_services

The `debops.etc_services` role can be used to "reserve" or "register" a
service port in the `/etc/services` file. Service ports configured this
way can appear as named entries in many command outputs, such as
`iptables --list` or `netstat --listening --program`. You can also have
convenient database of reserved and free ports on a particular host, and
reference ports by their names in firewall configuration files.

Read the [etc_services role documentation](https://docs.debops.org/en/HEAD/ansible/roles/etc_services/) for more details.
