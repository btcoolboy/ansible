### rsnapshot

The [rsnapshot](https://rsnapshot.org/) script is a wrapper around the
[rsync](https://rsync.samba.org/) command that allows creation and
management of snapshotted backups of local or remote filesystems.
Periodic snapshots are created using `cron` jobs and use [hard
links](https://en.wikipedia.org/wiki/Hard_link) to perform
deduplication.

The `debops.rsnapshot` Ansible role acts as another "layer" above
`rsnapshot`. The role can configure snapshotted backups of the local
host to internal or removable storage, as well as create snapshotted
backups of remote hosts over SSH.

Read the [rsnapshot role documentation](https://docs.debops.org/en/HEAD/ansible/roles/rsnapshot/) for more details.
