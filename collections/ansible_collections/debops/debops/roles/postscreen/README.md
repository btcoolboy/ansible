### postscreen

The [Postscreen](http://www.postfix.org/POSTSCREEN_README.html) Postfix
service can be enabled to filter out undesired SMTP clients on initial
connection to the mail server. Postscreen uses certain criteria (static
white/blacklist, DNS Block List queries, communication analysis) to
allow or deny connections for a given SMTP client.

This role can be used to enable and configure Postscreen in a Postfix
installation managed by the `debops.postfix` Ansible role. It does not
configure Postfix directly on its own.

Read the [postscreen role documentation](https://docs.debops.org/en/HEAD/ansible/roles/postscreen/) for more details.
