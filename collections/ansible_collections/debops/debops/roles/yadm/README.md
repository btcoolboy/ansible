### yadm

[Yet Another Dotfiles Manager](https://yadm.io/) (`yadm`) is a wrapper
script around the `git` command that manages
[dotfiles](https://en.wikipedia.org/wiki/Hidden_file_and_hidden_directory)
located in the `$HOME` directory using a `git` repository. yadm supports
encrypted storage for sensitive files, alternative file selection based
on host class/OS/hostname/user account, bootstrap script and Jinja
templating.

The `debops.yadm` Ansible role will install the `yadm` script, either
from an APT repository, or using the upstream `git` repository. The role
will also install a `zsh` shell and a few essential CLI applications.

Optionally, `debops.yadm` role can clone selected dotfiles `git`
repositories to the host creating mirrors, that can be used by users or
other Ansible roles to deploy dotfiles locally.

Read the [yadm role documentation](https://docs.debops.org/en/HEAD/ansible/roles/yadm/) for more details.
