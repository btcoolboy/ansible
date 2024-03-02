### libuser

The [libuser](https://pagure.io/libuser/) library and its corresponding
package provides a set of commands and an API which can be used by tools
like Ansible to manage UNIX account and group configuration in different
NSS databases (local `/etc/passwd` and `/etc/group` databases, LDAP,
NIS, etc.). This allows to abstract away user and group management and
make it independent from the underlying database.

The `debops.libuser` role installs and configures the `libuser` package
on Debian or Ubuntu hosts. The library is used by some other DebOps
roles like `debops.users`, `debops.system_users` to manage local UNIX
accounts and groups when the hosts are joined to an LDAP environment.
The default configuration set up by the role ensures that Ansible `user`
and `group` modules, when instructed, can correctly create local account
and group entries in the `passwd` and `group` databases.

Read the [libuser role documentation](https://docs.debops.org/en/HEAD/ansible/roles/libuser/) for more details.
