### filebeat

[Filebeat](https://www.elastic.co/beats/filebeat), from
[Elastic](https://www.elastic.co/) is part of the Elastic Stack.
Filebeat can be used to parse and "ingest" logs from files, syslog, and
various other sources, parse them and send them off to Elasticsearch,
Logstash or other destinations.

The `filebeat` Ansible role configures Filebeat on Debian/Ubuntu hosts.
The software itself will be installed using the `debops.elastic_co`
Ansible role.

Read the [filebeat role documentation](https://docs.debops.org/en/HEAD/ansible/roles/filebeat/) for more details.
