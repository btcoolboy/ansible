### radvd

The [radvd](https://en.wikipedia.org/wiki/Radvd), Router Advertisement
Daemon, is used to publish IPv6 subnets, routes, DNS configuration to
other hosts on the local network. It's required for the hosts to use
SLAAC autoconfiguration.

The `debops.radvd` Ansible role can be used to install and configure the
`radvd` service. It will detect and automatically configure any network
bridges with IPv6 networking enabled.

Read the [radvd role documentation](https://docs.debops.org/en/HEAD/ansible/roles/radvd/) for more details.
