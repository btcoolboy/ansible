### apt_mirror

The [apt-mirror](https://apt-mirror.github.io/) script can be used to
create full or partial mirrors of APT repositories. It uses syntax
similar to the `sources.list(5)` configuration file, supports
authenticated APT repositories, access over HTTPS and more.

The `debops.apt_mirror` role can be used to install and configure the
`apt-mirror` script to periodically pull different APT repositories and
publish them using `nginx` for other hosts to use. The role supports
configuration of multiple mirror "instances", which can be configured
with different mirror frequency as needed.

Read the [apt_mirror role documentation](https://docs.debops.org/en/HEAD/ansible/roles/apt_mirror/) for more details.
