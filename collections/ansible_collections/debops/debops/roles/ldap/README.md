### ldap

[Lightweight Directory Access
Protocol](https://en.wikipedia.org/wiki/Lightweight_Directory_Access_Protocol)
is a popular and standardized protocol that permits applications to
access structured data. It can be used to build and manage clustered
environments with central authentication and access control based on
directory services that allow efficient searching and retrieval of data.

The `debops.ldap` Ansible role can set up system-wide LDAP configuration
on a Debian/Ubuntu host, and provide LDAP-based applications, as well as
other Ansible roles, information necessary to connect them to a LDAP
directory service. In addition to that, `debops.ldap` role can be used
via Ansible inventory, or as a dependent role by other Ansible roles, to
perform tasks in the LDAP directory itself, on behalf of the Ansible
user.

If you are looking for a LDAP server management solution, check out the
`debops.slapd` Ansible role that can manage OpenLDAP servers.

Read the [ldap role documentation](https://docs.debops.org/en/stable-3.0/ansible/roles/ldap/) for more details.
