### networkd

The `systemd-networkd(8)` service is a part of the
[systemd](https://www.freedesktop.org/wiki/Software/systemd/) project.
The service manages the runtime and on-disk configuration of the network
connections, physical and virtual network devices and their state in the
`systemd-udevd(8)` subsystem.

The `debops.networkd` Ansible role can be used to generate and update
configuration of the `systemd-networkd` service. Other parts of the
`systemd` ecosystem are managed by separate Ansible roles.

Read the [networkd role documentation](https://docs.debops.org/en/HEAD/ansible/roles/networkd/) for more details.
