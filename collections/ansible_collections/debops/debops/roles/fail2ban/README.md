### fail2ban

[fail2ban](https://www.fail2ban.org/) is a service which parses
specified log files and can perform configured actions when a given
[regexp](https://en.wikipedia.org/wiki/Regular_expression) is found.
It's usually used to ban offending IP addresses using `iptables` rules
(only IPv4 connections are supported at the moment).

Read the [fail2ban role documentation](https://docs.debops.org/en/HEAD/ansible/roles/fail2ban/) for more details.
