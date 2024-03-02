### reprepro

The `reprepro` Debian package is an [APT repository
manager](https://wiki.debian.org/DebianRepository/SetupWithReprepro). It
can be used to create and maintain APT repositories for Debian or Ubuntu
operating systems and their derivatives. The repositories managed by
`reprepro` can be used to distribute third-party software packages or
create local mirrors of official Debian or Ubuntu repositories.

The `debops.reprepro` role uses the `reprepro` package to maintain
multiple sets of APT repositories, with optional authentication and
access restrictions.

Read the [reprepro role documentation](https://docs.debops.org/en/HEAD/ansible/roles/reprepro/) for more details.
