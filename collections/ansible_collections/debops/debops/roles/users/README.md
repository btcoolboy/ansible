### users

The `debops.users` Ansible role can be used to manage local user
accounts and groups. The role allows for certain operations inside of
the home directories, like configuration of the mail forwarding, SSH
public keys or automatic deployment of user configuration files
(dotfiles).

This role is designed to manage regular user accounts and application
accounts. In a LDAP-enabled environment, it might be better to configure
these using LDAP directory, and manage local system administrator
accounts using the `debops.system_users` Ansible role.

Read the [users role documentation](https://docs.debops.org/en/stable-3.0/ansible/roles/users/) for more details.
