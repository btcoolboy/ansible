### apparmor

[AppArmor](https://apparmor.net/) is a Linux kernel Security Module
(<span class="title-ref">LSM</span>) which provides [mandatory access
control](https://en.wikipedia.org/wiki/Mandatory_access_control).

Programs are restricted on the basis of <span
class="title-ref">profiles</span>, which are traditionally stored under
`/etc/apparmor.d/`, using filenames which correspond to the path to the
binary being protected by the profile (`/usr/bin/foobar` →
`/etc/apparmor.d/usr.bin.foobar`).

Profiles can be configured in different modes: `enforce`, `disabled`, or
`complain` (log, but don't enforce).

This role is primarily geared towards allowing other roles to perform
customizations of existing profiles, and allowing administrators to
selectively enable/disable profiles.

Read the [apparmor role documentation](https://docs.debops.org/en/stable-3.2/ansible/roles/apparmor/) for more details.
