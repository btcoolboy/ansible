### lxd

[Linux Containers](https://en.wikipedia.org/wiki/LXC) or LXC provide a
way to partition existing Linux hosts into separate environments using
Linux cgroups, namespace isolation, POSIX capabilities and chrooted
filesystems.

[LXD](https://linuxcontainers.org/lxd/introduction/), or a Linux
Container Daemon, is a service written in Go which provides a REST API
and CLI interface for Linux Container management.

The `debops.lxd` Ansible role can be used to install and configure the
LXD service on a Debian or Ubuntu hosts. The role will use the
`debops.golang` role to install the `lxd` and `lxc` binaries from
upstream on Debian hosts.

Read the [lxd role documentation](https://docs.debops.org/en/HEAD/ansible/roles/lxd/) for more details.
