### nscd

The Name Service Cache Daemon is a local service which caches NSS
database information from remote sources like LDAP, Active Directory or
NIS. The service is useful in combination with the `nslcd` (managed by
the `debops.nslcd` role) to lower the number of queries to the remote
databases and make system operations faster.

The `debops.nscd` Ansible role supports two flavors of the caching
service, the original `nscd` implemented by GNU `libc` library, as well
as its drop-in replacement, `unscd`, created by the BusyBox project. The
`unscd` version is installed by default.

Read the [nscd role documentation](https://docs.debops.org/en/HEAD/ansible/roles/nscd/) for more details.
