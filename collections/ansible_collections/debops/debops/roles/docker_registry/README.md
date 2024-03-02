### docker_registry

The `debops.docker_registry` Ansible role can be used to install and
manage a Docker Registry instance. A [Docker
Registry](https://docs.docker.com/registry/) is a service which allows
you to publish and distribute Docker container images. It can be used to
create a private, local alternative to a Docker Hub.

By default the role installs the Registry using an OS package on
supported OS releases; on older OS releases without the Registry
packaged in the repositories the role can download the official upstream
release from GitHub and build a Go `docker-registry` binary
automatically.

The role integrates with the `debops.gitlab` and `debops.redis_server`
Ansible roles to provide backend support for the [GitLab Container
Registry](https://gitlab.com/help/user/project/container_registry)
service. Docker Registry can be installed as standalone service, in
which case it will be secured using HTTP Basic Authentication provided
by the `debops.nginx` role.

Read the [docker_registry role documentation](https://docs.debops.org/en/HEAD/ansible/roles/docker_registry/) for more details.
