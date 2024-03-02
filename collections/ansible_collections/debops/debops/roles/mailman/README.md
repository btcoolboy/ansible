### mailman

The `debops.mailman` Ansible role can be used to create and manage
mailing lists using [GNU Mailman](https://list.org/) service. The role
is designed to install and configure Mailman 3 using Debian packages,
and will automatically integrate with PostgreSQL or MariaDB database for
configuration storage and Postfix for SMTP services.

By default the role provides configuration for `debops.postfix` role to
configure the SMTP server integration, as well as `debops.nginx` role to
configure access to the web control panel.

Read the [mailman role documentation](https://docs.debops.org/en/HEAD/ansible/roles/mailman/) for more details.
