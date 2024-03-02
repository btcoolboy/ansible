### docker_gen

[docker-gen](https://github.com/jwilder/docker-gen) generates
configuration files for host services to make the Dockerized services
accessible to them. For example this role can create the required
configuration for publishing a Dockerized web-service via the host's
web-server. The configuration is based on available Docker container
metadata.

This role creates a service and configuration to generate `nginx`
upstream service definitions, which can be used by `debops.nginx` role
to configure Dockerized services, either local or remote, behind an
`nginx` reverse proxy. Other services and templates might be provided in
the future.

Read the [docker_gen role documentation](https://docs.debops.org/en/HEAD/ansible/roles/docker_gen/) for more details.
