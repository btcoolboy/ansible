### resolved

The `systemd-resolved(8)` service is a part of the
[systemd](https://www.freedesktop.org/wiki/Software/systemd/) project.
The service is a local DNS resolver that can manage the
`/etc/resolv.conf` configuration file and provide name resolution,
Multicast DNS and LLDP capabilities, among other things.

The `debops.resolved` Ansible role manages the `systemd-resolved`
configuration. Other parts of the `systemd` ecosystem are managed by
separate Ansible roles.

Read the [resolved role documentation](https://docs.debops.org/en/HEAD/ansible/roles/resolved/) for more details.
