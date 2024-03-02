### preseed

[Preseeding](https://wiki.debian.org/DebianInstaller/Preseed) is a way
to configure the Debian Installer non-interactively. During
installation, a special text file can be downloaded over HTTP, this file
can provide answers to the installer questions.

After installation, a custom shell script will be downloaded and run in
the target environment to prepare host for remote use (an admin account
will be created, SSH keys will be configured, optionally a Salt Minion
will be installed and will start on the next boot).

Read the [preseed role documentation](https://docs.debops.org/en/HEAD/ansible/roles/preseed/) for more details.
