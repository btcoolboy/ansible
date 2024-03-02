### ipxe

The [iPXE](https://ipxe.org/) project provides an open source network
boot firmware. It can be used to boot computers over the network using
DHCP, PXE and TFTP protocols, and hand off the boot process to other
operating systems provided over HTTP, NFS or iSCSI protocols.

The `debops.ipxe` Ansible role installs the `ipxe` APT package and
prepares a simple boot menu which can be used to either launch the
Debian Installer over the network, or switch to another publicly
available network boot menu.

Read the [ipxe role documentation](https://docs.debops.org/en/HEAD/ansible/roles/ipxe/) for more details.
