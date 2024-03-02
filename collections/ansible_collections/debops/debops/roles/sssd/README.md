### sssd

The `sssd` daemon, maintained by the [SSSD Project](https://sssd.io/),
is a spinoff from the [FreeIPA Project](https://www.freeipa.org/) and
provides a modern take on venerable daemons such as `debops.nslcd`,
`debops.nscd` and `unscd(1)`. It is used to look up user, group or other
information stored in a number of different databases, such as LDAP,
Kerberos, FreeIPA, Active Directory, etc. It is needed if you want to
use the `posixAccount` and `posixGroup` LDAP objects to authenticate to
UNIX-like hosts.

The `debops.sssd` Ansible role can be used to configure the `sssd`
service on a host and, via `debops.ldap` role, create a bind account in
the LDAP directory used by `sssd` to perform LDAP lookups.

Read the [sssd role documentation](https://docs.debops.org/en/HEAD/ansible/roles/sssd/) for more details.
