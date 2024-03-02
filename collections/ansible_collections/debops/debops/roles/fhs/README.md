### fhs

By default various DebOps application roles install their data in
directories designated by the [Filesystem Hierarchy
Standard](https://en.wikipedia.org/wiki/Filesystem_Hierarchy_Standard)
for locally-installed software - for example `/usr/local/bin/` for
binaries, `/usr/local/src/` for source code, and so on. To allow system
administrators to easily change the preferred location of various
resources without the need to modify multiple roles separately, the
`debops.fhs` role is a central place which defines base directories for
other roles to use.

The base directories are created by the role, and a special
`/etc/ansible/facts.d/fhs.fact` script is generated on the host. It
serves dual purpose - the facts are used to ensure that any changes in
the directory paths don't affect existing installations, and can be used
by other Ansible roles to define various resource paths in their
variables.

Read the [fhs role documentation](https://docs.debops.org/en/HEAD/ansible/roles/fhs/) for more details.
