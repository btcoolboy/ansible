### wpcli

[WP-CLI](https://wp-cli.org/) framework is a PHP script which can be
used to manage [WordPress](https://wordpress.org/) installations via the
Linux shell. It provides a command line interface to WP Admin dashboard,
provides an interface for `cron` task execution for a given WordPress
website, create backups, and lots of other things.

The `debops.wpcli` Ansible role can be used to install WP-CLI on a host
managed by DebOps, which in turn enables management of per-user
WordPress websites. The role is designed with shared hosting environment
in mind; users need to utilize other DebOps/Ansible roles to manage the
`webserver
<debops.nginx>`, `database engine <debops.mariadb_server>`, `PHP
environment <debops.php>` and `UNIX accounts <debops.users>`, etc.

Read the [wpcli role documentation](https://docs.debops.org/en/HEAD/ansible/roles/wpcli/) for more details.
