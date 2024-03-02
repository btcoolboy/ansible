### gitlab

[GitLab](https://about.gitlab.com/) is a complete suite of tools and
services needed for application development, testing and deployment,
including a software forge based on `git`, issue tracking, Continuous
Integration and support for Kubernetes and other popular services.
GitLab is developed using an "open core" model, with essential parts of
the project licensed under Open Source licenses and ability to upgrade
the service with commercial licenses.

The project can be deployed in several different ways, one of which is
an "omnibus" installation which consists of all of the needed services
(web server, database, various other tools) bundled together in a
package and managed as a whole using Chef. The `debops.gitlab` Ansible
role provides an integration layer between various services managed by
DebOps (firewall, PKI infrastructure, LDAP environment) and GitLab
Omnibus, and allows the system administrator to deploy and manage GitLab
Omnibus using Ansible.

Read the [gitlab role documentation](https://docs.debops.org/en/HEAD/ansible/roles/gitlab/) for more details.
