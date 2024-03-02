### systemd

The [systemd](https://www.freedesktop.org/wiki/Software/systemd/)
project is a system and service manager, a replacement for the
traditional `/bin/init` daemon started by the kernel after the boot
process is complete. `systemd` focuses on the intermediate layer between
the "kernel space" and "userspace", so called "system" layer. The
project itself is composed from multiple separate services which can be
enabled or disabled as needed.

The `debops.systemd` Ansible role focuses on management of the `systemd`
service itself; other Ansible roles included in the DebOps project can
be used to manage disparate components like `journald` via the
`debops.journald` role. This role manages the "system" instance of
`systemd`, as well as the global configuration of the `systemd --user`
instances and the configuration of the `systemd-logind` login manager.

Read the [systemd role documentation](https://docs.debops.org/en/HEAD/ansible/roles/systemd/) for more details.
