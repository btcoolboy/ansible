### sysfs

[sysfs](https://en.wikipedia.org/wiki/Sysfs) is a Linux kernel virtual
filesystem, usually mounted at `/sys`. It provides a file-based
interface to the kernel data structures related to hardware and host
configuration. The filesystem entries can be manipulated by the
`sysfsutils` package provided by Debian/Ubuntu.

The `debops.sysfs` Ansible role can be used to configure `sysfs`
attributes in supported environments. It can be used as a standalone
role, or a dependent role to configure `sysfs` on behalf of another
Ansible role.

Read the [sysfs role documentation](https://docs.debops.org/en/HEAD/ansible/roles/sysfs/) for more details.
