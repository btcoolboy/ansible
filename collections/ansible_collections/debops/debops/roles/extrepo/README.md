### extrepo

The [extrepo](https://packages.debian.org/sid/extrepo) Debian package
provides an easy way to manage APT sources external to the Debian main
archives. The [list of supported APT
sources](https://salsa.debian.org/extrepo-team/extrepo-data) is curated
outside of the normal Debian release cycle and contains details about
popular third-party APT repositories maintained by software vendors.

The `debops.extrepo` Ansible role can be used to manage third-party APT
repositories via Ansible using the `extrepo` package. The role is
written as complimentary to the `debops.keyring` role which provides a
similar functionality.

Read the [extrepo role documentation](https://docs.debops.org/en/HEAD/ansible/roles/extrepo/) for more details.
