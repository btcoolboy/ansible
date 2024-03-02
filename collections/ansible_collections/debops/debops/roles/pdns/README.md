### pdns

The `debops.pdns` role can be used to configure [PowerDNS Authoritative
Server](https://www.powerdns.com/auth.html), whose service is called
'pdns' in Debian. pdns supports multiple backends like major relational
databases, LDAP servers and plain text files. Backends that support
native replication can be used in place of traditional zone transfers.
Furthermore, pdns can be used for geographical load balancing and has
excellent DNSSEC support, currently supporting the vast majority of
DNSSEC-enabled domains in Europe. pdns is extensible using a wide
variety of scripting languages.

Read the [pdns role documentation](https://docs.debops.org/en/HEAD/ansible/roles/pdns/) for more details.
