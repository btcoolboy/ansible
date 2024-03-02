### lxc

[Linux Containers](https://en.wikipedia.org/wiki/LXC) or LXC provide a
way to partition existing Linux hosts into separate environments using
Linux cgroups, namespace isolation, POSIX capabilities and chrooted
filesystems.

The `debops.lxc` Ansible role can be used to configure LXC support on a
Debian/Ubuntu host. It can manage configuration files in `/etc/lxc/`
directory and provide custom scripts that allow, for example, initial
bootstrapping of the user's SSH public keys inside of the container so
that it can be managed remotely with Ansible.

Read the [lxc role documentation](https://docs.debops.org/en/HEAD/ansible/roles/lxc/) for more details.
