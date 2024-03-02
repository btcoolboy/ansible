### etckeeper

The `debops.etckeeper` Ansible role will install
[etckeeper](https://etckeeper.branchable.com/), which puts the `/etc`
directory under version control. To do this, `etckeeper` hooks into the
package management and from now on automatically will commit changes to
a local git repository under `/etc/.git/` directory. This makes it easy
to see which changes are applied on a specific host and quickly revert
them, if something breaks.

The role will install a special Ansible local fact which will commit any
changes in the `/etc` directory as well, usually at the moment the
Ansible facts are gathered.

Read the [etckeeper role documentation](https://docs.debops.org/en/HEAD/ansible/roles/etckeeper/) for more details.
