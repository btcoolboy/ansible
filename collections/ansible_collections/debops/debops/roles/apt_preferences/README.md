### apt_preferences

[APT preferences](https://wiki.debian.org/AptPreferences) can be used to
influence package selection performed by APT during installation or
upgrades. You can for example tell APT that you prefer packages from
certain repositories or want to hold a package on a particular version
no matter what (among other things).

By default, if you don't specify a version or provide a custom pin
configuration, `debops.apt_preferences` role will configure the
specified packages to be installed from the backports repository of the
current OS release.

Read the [apt_preferences role documentation](https://docs.debops.org/en/HEAD/ansible/roles/apt_preferences/) for more details.
