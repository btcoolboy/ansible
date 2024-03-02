### apt_mark

The `debops.apt_mark` Ansible role can be used to set the desired state
of APT packages using `apt-mark(8)` command. It might be useful if a new
Debian/Ubuntu install results in many packages which should be installed
are marked for autoremoval, or if you want to hold certain APT packages
in their current state. The role operates only on packages that are
already installed.

Read the [apt_mark role documentation](https://docs.debops.org/en/HEAD/ansible/roles/apt_mark/) for more details.
