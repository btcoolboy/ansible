### metricbeat

[Metricbeat](https://www.elastic.co/beats/metricbeat), from
[Elastic](https://www.elastic.co/) is part of the Elastic Stack.
Metricbeat can be used to gather various metrics (CPU usage, disk I/O,
application status, etc.) from host and services and send them to
Elasticsearch database for processing.

The `metricbeat` Ansible role configures Metricbeat on Debian/Ubuntu
hosts. The software itself will be installed using the `debops.extrepo`
Ansible role.

Read the [metricbeat role documentation](https://docs.debops.org/en/HEAD/ansible/roles/metricbeat/) for more details.
