### libvirtd

`debops.libvirtd` Ansible role manages the
[libvirtd](https://libvirt.org/) daemon on a virtualization host (server
side). It will automatically install QEMU KVM support on any host that
is not a KVM guest, to allow for easy deployment of KVM virtual
machines.

Configuration of `libvirtd` instance (local or remote) can be performed
using `debops.libvirt` role, which uses the `libvirt` API to manage the
server.

Read the [libvirtd role documentation](https://docs.debops.org/en/HEAD/ansible/roles/libvirtd/) for more details.
