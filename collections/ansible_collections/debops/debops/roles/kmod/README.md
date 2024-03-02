### kmod

The `debops.kmod` Ansible role can be used to manage configuration of
the Linux kernel modules, located in the `/etc/modprobe.d/` directory,
and specify what kernel modules should be loaded at boot time using
configuration in `/etc/modules-load.d/` directory.

Kernel module configuration can be specified using Ansible inventory, or
other Ansible roles can use the `debops.kmod` role to configure kernel
module options on their behalf.

Read the [kmod role documentation](https://docs.debops.org/en/HEAD/ansible/roles/kmod/) for more details.
