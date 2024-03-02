### global_handlers

The `debops.global_handlers` role is a central place to define [Ansible
handlers](https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html#handlers-running-operations-on-change)
used by different Ansible roles. Keeping the handlers centralized allows
them to be used in different Ansible roles without the need to add
dependent roles to the playbook, making execution faster and the
codebase easier to modify and maintain.

Read the [global_handlers role documentation](https://docs.debops.org/en/HEAD/ansible/roles/global_handlers/) for more details.
