### mcli

[MinIO](https://min.io/) is an Open Source Amazon Simple Storage Service
(S3) compatible object storage service. The [MinIO
Client](https://docs.min.io/docs/minio-client-complete-guide)
application is used to interface with MinIO and perform various
administrative tasks, including extended configuration of the service.

The `debops.mcli` Ansible role installs MinIO Client binary on a Debian
or Ubuntu host either by downloading and verifying it from the upstream
repository directly, or cloning the source code and building it locally.

The MinIO Client binary will be installed as the `mcli` binary instead
of the `mc` binary preferred by upstream to avoid clashing with the `mc`
Debian package which provides Midnight Commander. This solution [is
suggested by
upstream](https://github.com/minio/mc/blob/master/CONFLICT.md) as well.

You can use the `debops.minio` Ansible role to install and configure the
MinIO service itself.

Read the [mcli role documentation](https://docs.debops.org/en/HEAD/ansible/roles/mcli/) for more details.
