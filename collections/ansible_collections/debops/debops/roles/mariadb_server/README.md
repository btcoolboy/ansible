### mariadb_server

[MariaDB](https://en.wikipedia.org/wiki/Mariadb) is a popular relational
SQL database that was forked from MySQL server. Ansible roles
`debops.mariadb` and `debops.mariadb_server` allow you to manage a
MariaDB server and / or access it remotely from other hosts.

`debops.mariadb_server` role is the "server" part - it installs
`mariadb-server` Debian package, and configures access to the database
from local `root` account. After that, you can use `debops.mariadb` role
to manage databases and user accounts on the server.

Read the [mariadb_server role documentation](https://docs.debops.org/en/stable-3.0/ansible/roles/mariadb_server/) for more details.
