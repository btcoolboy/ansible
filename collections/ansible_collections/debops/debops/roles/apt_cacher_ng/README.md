### apt_cacher_ng

Ansible role to install and manage Apt-Cacher NG. Apt-Cacher NG is a
caching HTTP proxy for downloading software packages. This role sets up
the Apt-Cacher NG server in your network and allows clients to use the
proxy. Only the proxy server is setup by this role.

The following options are available to get clients to use the Apt-Cacher
NG server:

-   Advanced Package Tool: `debops.apt_proxy`

Read the [apt_cacher_ng role documentation](https://docs.debops.org/en/stable-3.0/ansible/roles/apt_cacher_ng/) for more details.
