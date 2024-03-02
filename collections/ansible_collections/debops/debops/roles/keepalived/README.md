### keepalived

The [keepalived](https://keepalived.org/) service can be used to provide
simple load balancing and high availability services in a Linux cluster.
The service uses the [Virtual Router Redundancy
Protocol](https://en.wikipedia.org/wiki/Virtual_Router_Redundancy_Protocol)
for communication between the nodes in a cluster and can perform
specified actions on the nodes - create or remove IP addresses, start or
stop services, and more.

The `debops.keepalived` Ansible role can be used to install and
configure the `keepalived` service on Debian and Ubuntu hosts. The role
allows Jinja expressions to be used in the `keepalived.conf(5)`
configuration file to augment generated configuration files as needed.

Read the [keepalived role documentation](https://docs.debops.org/en/HEAD/ansible/roles/keepalived/) for more details.
