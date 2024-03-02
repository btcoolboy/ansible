### mount

The `debops.mount` Ansible role can be used to manage local filesystem
mounts as well as bind mounts in the `/etc/fstab` database. Custom
directories can also be created by this role, with support for normal as
well as ACL attributes.

This role is meant to be used to configure local filesystems, for remote
filesystems, you can use the `debops.nfs` role instead, which will
configure the NFS client service.

Read the [mount role documentation](https://docs.debops.org/en/HEAD/ansible/roles/mount/) for more details.
