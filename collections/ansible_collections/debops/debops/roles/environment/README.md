### environment

The `debops.environment` role can be used to manage system-wide
environment variables, by default located in `/etc/environment` file.
Variables are gathered from multiple sources and combined to allow
global/group/host tiered environment modeled after Ansible inventory.

This role can also be used by other Ansible roles as a dependency to
create global environment variables in a safe way, that preserves
idempotency.

Read the [environment role documentation](https://docs.debops.org/en/stable-3.2/ansible/roles/environment/) for more details.
