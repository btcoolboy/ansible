### influxdb

[InfluxDB](https://en.wikipedia.org/wiki/InfluxDB) is an open-source
time series database (TSDB) developed by InfluxData. It is written in Go
and optimized for fast, high-availability storage and retrieval of time
series data in fields such as operations monitoring, application
metrics, Internet of Things sensor data, and real-time analytics.
Ansible roles `debops.influxdb` and `debops.influxdb_server` allow you
to manage a InfluxDB server and / or access it remotely from other
hosts.

The `debops.influxdb` role is the "client" part - it uses Ansible
delegation to configure users and databases in local or remote InfluxDB
servers. You can use `debops.influxdb_server` role to manage the
InfluxDB server itself.

Read the [influxdb role documentation](https://docs.debops.org/en/HEAD/ansible/roles/influxdb/) for more details.
