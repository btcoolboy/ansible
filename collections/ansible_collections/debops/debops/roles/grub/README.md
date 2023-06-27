### grub

This Ansible role manages GRUB configuration. It detects kernel
parameters which are currently set (probably during installation).
Autodetected parameters can be merged or overwritten by Ansible
variables. It can also enable both Linux kernel and GRUB serial console.

Parameter autodetection with values that contain spaces is not
supported.

Additionally, this role allows you to configure password protection for
GRUB.

Read the [grub role documentation](https://docs.debops.org/en/stable-3.0/ansible/roles/grub/) for more details.
