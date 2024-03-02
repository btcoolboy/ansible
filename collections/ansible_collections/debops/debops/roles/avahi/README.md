### avahi

[Avahi](https://www.avahi.org/) is a Linux daemon which can be used to
publish information about local or remote services using [Multicast
DNS](https://en.wikipedia.org/wiki/Multicast_DNS) protocol (mDNS, also
used by Bonjour or ZeroConf). This protocol can then be queried by other
applications such as DNS clients or those that support [DNS Service
Discovery](https://en.wikipedia.org/wiki/Zero-configuration_networking#Service_discovery)
to find out and access services on the local network.

The `debops.avahi` Ansible role can be used to configure the Avahi
service on Debian or Ubuntu hosts. You can create custom services,
publish static host entries that point to other hosts on the local
network, or even define and publish CNAME records pointing to the host
itself via a custom script.

Read the [avahi role documentation](https://docs.debops.org/en/HEAD/ansible/roles/avahi/) for more details.
