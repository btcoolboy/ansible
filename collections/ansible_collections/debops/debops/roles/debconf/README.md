### debconf

The [debconf](https://wiki.debian.org/debconf) database is a Debian
configuration management system meant to ease configuration of
applications packaged using the `.deb` file format. Debconf allows
system administrators to pre-seed the answers to the questions asked by
a given package during installation, allowing for automated and
non-interactive configuration of said package.

The `debops.debconf` role is built around using `debconf` to
pre-configure applications installed using `.deb` packages. The role is
executed late in the configuration order defined in the `site.yml`
Ansible playbook, so that other services required by a given application
can be prepared before its installation.

Read the [debconf role documentation](https://docs.debops.org/en/stable-3.2/ansible/roles/debconf/) for more details.
