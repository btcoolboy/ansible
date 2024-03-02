### dhcp_probe

The [dhcp\_probe](https://www.net.princeton.edu/software/dhcp_probe/)
tool can be used to passively detect rogue DHCP servers on IPv4
networks. Upon detection, the service can execute custom commands to,
for example, block the culprit via RADIUS or notify the system
administrator.

The `debops.dhcp_probe` role can be used to install and configure
`dhcp_probe` on a Debian/Ubuntu host. It will utilize `systemd` instance
templates to run DHCP Probe instances on multiple network interfaces at
once. By default, an e-mail message will be sent to the system
administrator with notification on newly detected rogue DHCP servers.

Read the [dhcp_probe role documentation](https://docs.debops.org/en/HEAD/ansible/roles/dhcp_probe/) for more details.
