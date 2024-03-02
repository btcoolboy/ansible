### persistent_paths

This role provides a generic mechanism to declare which
files/directories are required to be persistent. How this information is
used can then be defined in this role.

On [Qubes OS](https://en.wikipedia.org/wiki/Qubes_OS), all work gets
done in AppVMs which are typically based on TemplateVMs. Only a few
paths in such TemplateBasedVM will persist a reboot, mainly `/home` and
`/rw`. Package installation and the like is supposed to happen in
TemplateVMs only but configuration can happen in either VM type as
desired. If changes should be made in a TemplateBasedVM however it needs
to be made sure that they are persistent.

Since Qubes OS R3.2 the [bind-dirs]() script and related configuration
can be used to easily make additional paths persistent by bind mounting
them from `/rw/bind-dirs/` to the desired path.

`debops.persistent_paths` allows other Ansible roles to interact with
[bind-dirs]() by using this role as a dependency role. An example which
does this is `debops.cryptsetup`.

The role can also be used by the system administrator to manage
[bind-dirs]() using the Ansible inventory.

Read the [persistent_paths role documentation](https://docs.debops.org/en/HEAD/ansible/roles/persistent_paths/) for more details.
