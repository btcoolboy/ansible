### dhcrelay

The `debops.dhcrelay` role can be used to configure dhcrelay, the
Internet Systems Consortium DHCP Relay Agent. dhcrelay can be used to
relay DHCPv4 messages between hosts on one network, and a DHCPv4 server
on another network.

This role does not support DHCPv6, as DHCPv6 is currently not supported
by the init script provided by the isc-dhcp-relay package in Debian
Stable. A workaround for this can be implemented if there is demand for
it.

Read the [dhcrelay role documentation](https://docs.debops.org/en/stable-3.0/ansible/roles/dhcrelay/) for more details.
