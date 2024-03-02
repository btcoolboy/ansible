### journald

The Journal, part of the
[systemd](https://www.freedesktop.org/wiki/Software/systemd/) project,
is a syslog replacement. On systems that use `systemd` as the init
daemon, the `systemd-journald` service takes care of receiving, storing
and routing the log messages received via the `/dev/log` device, the
`logger(1)` command or from services managed by the `systemd` init
daemon.

The `debops.journald` Ansible role can be used to manage the Journal
configuration, enable or disable persistent log storage and configure
Forward Secure Sealing on the managed hosts.

Read the [journald role documentation](https://docs.debops.org/en/HEAD/ansible/roles/journald/) for more details.
