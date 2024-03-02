### minio

[MinIO](https://min.io/) is an Open Source Amazon Simple Storage Service
(S3) compatible object storage service.

The `debops.minio` Ansible role can be used to deploy and configure
MinIO in various scenarios, either as a single node, single tenant
service, or a multi node and/or multi tenant distributed storage
service. The role relies on other DebOps roles to install MinIO binary
from upstream URL or build it from source code, configure firewall
access, provide TLS support and configure web server access to the
service. See the Getting Started page for more details about the
deployment stack.

The [MinIO Client](https://docs.min.io/docs/minio-client-complete-guide)
application is used to interface with MinIO and perform various
administrative tasks, including extended configuration of the service.
It can be installed on a host using the `debops.mcli` Ansible role.

Read the [minio role documentation](https://docs.debops.org/en/HEAD/ansible/roles/minio/) for more details.
