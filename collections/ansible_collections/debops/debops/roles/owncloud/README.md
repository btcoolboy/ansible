### owncloud

This role installs a [NextCloud](https://nextcloud.com/) or
[ownCloud](https://en.wikipedia.org/wiki/OwnCloud) instance on a
specified host, either with SQLite, MySQL, MariaDB or PostgreSQL
database as a backend and an Nginx or Apache webserver as a frontend.

Nextcloud will be installed using the upstream tarballs. ownCloud will
be installed as package coming directly from upstream.

Note that Nginx is [not officially supported by ownCloud nor
NextCloud](https://github.com/debops/ansible-owncloud/issues/49) but it
is community supported and should work without problems. Apache is
supported by the role but not yet used by default and not very well
tested.

**Features:**

-   Support for LDAP using the `debops.ldap` Ansible role.
-   In memory caching using Redis for file locking and APCu.
-   Theming support (only tested with ownCloud 10).
-   Extensive configuration options via Ansible’s inventory.

Read the [owncloud role documentation](https://docs.debops.org/en/HEAD/ansible/roles/owncloud/) for more details.
