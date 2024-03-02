### core

The `debops.core` Ansible role takes care of variables that are shared
among different roles and are useful to keep in a central location. This
is done by leveraging functionality of [Ansible local
facts](https://docs.ansible.com/ansible/latest/user_guide/playbooks_vars_facts.html#facts-d-or-local-facts)
stored on remote hosts to ensure that the variables are always evaluated
by Ansible, even when playbook is run with or without different sets of
role tags.

Read the [core role documentation](https://docs.debops.org/en/HEAD/ansible/roles/core/) for more details.
