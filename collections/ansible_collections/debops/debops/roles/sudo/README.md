### sudo

The `debops.sudo` role can be used to ensure that `sudo` is supported on
a host. The role will automatically install `sudo-ldap` APT package if
LDAP support is detected on a host, otherwise a normal `sudo` APT
package will be installed.

Read the [sudo role documentation](https://docs.debops.org/en/HEAD/ansible/roles/sudo/) for more details.
