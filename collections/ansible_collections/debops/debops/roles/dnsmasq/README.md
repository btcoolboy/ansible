### dnsmasq

[dnsmasq](http://www.thekelleys.org.uk/dnsmasq/doc.html) is an
application that provides DNS, DHCP, TFTP and Router Advertisement
services in a compact package, suitable for small, internal networks.
it's commonly used as a DNS cache and forwarder on desktop workstations
or servers.

The `debops.dnsmasq` Ansible role can be used to configure `dnsmasq` on
a given host. By default the DNS cache will be configured, but the role
checks for presence of different services like `lxc-net` configured by
the `debops.lxc`, `consul` and specific network interfaces defined by
the `debops.ifupdown`, and adjusts the configuration automatically.

Read the [dnsmasq role documentation](https://docs.debops.org/en/HEAD/ansible/roles/dnsmasq/) for more details.
