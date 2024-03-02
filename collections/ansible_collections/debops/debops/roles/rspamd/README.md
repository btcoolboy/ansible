### rspamd

The `rspamd` daemon, maintained by the [Rspamd
Project](https://rspamd.com/), is a modern spam filtering daemon which
can be integrated with any MTA which supports `milters`. It provides an
advanced spam filtering system that allows evaluation of messages by a
number of rules including regular expressions, statistical analysis and
custom services such as URL black lists. A web-based user interface is
also provided.

The `debops.rspamd` Ansible role can be used to configure the `rspamd`
service on a host and automatically setup the `debops.postfix` role to
use it for spam filtering.

Read the [rspamd role documentation](https://docs.debops.org/en/HEAD/ansible/roles/rspamd/) for more details.
