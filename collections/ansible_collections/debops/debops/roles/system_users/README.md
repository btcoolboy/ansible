### system_users

The `debops.system_users` Ansible role can be used to manage local user
accounts and groups. The role allows for certain operations inside of
the home directories, like configuration of the mail forwarding, SSH
public keys or automatic deployment of user configuration files
(dotfiles).

This role is designed to manage the local system administrator accounts,
and its behaviour will change if the support for LDAP is configured on a
host. You can also use the `debops.users` role which provides similar
functionality, but is designed to manage regular user accounts and
application accounts, without special modifications related to LDAP
support.

Read the [system_users role documentation](https://docs.debops.org/en/HEAD/ansible/roles/system_users/) for more details.
