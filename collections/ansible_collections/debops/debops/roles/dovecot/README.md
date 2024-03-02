### dovecot

The `dovecot` daemon, maintained by the [Dovecot
Project](https://www.dovecot.org/), is a modern IMAP and POP3 email
server for Linux/UNIX-like systems, written with security primarily in
mind. Dovecot is an excellent choice for both small and large
installations. It’s fast, simple to set up, requires no special
administration and it uses very little memory.

The `debops.dovecot` Ansible role can be used to configure the `dovecot`
service on a host and to automatically setup various auxiliary roles,
such as `debops.pki` for SSL/TLS encryption.

Read the [dovecot role documentation](https://docs.debops.org/en/HEAD/ansible/roles/dovecot/) for more details.
