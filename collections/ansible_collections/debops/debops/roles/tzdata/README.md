### tzdata

The `debops.tzdata` Ansible role helps manage the time zone on
Debian/Ubuntu hosts. The role will make sure that services affected by
time zone changes (`cron`, `rsyslog`) will be restarted if needed.

The role also provides the `ansible_local.tzdata.timezone` Ansible local
fact with the host time zone specified in the `Area/Zone` format
required in some configuration files.

Read the [tzdata role documentation](https://docs.debops.org/en/HEAD/ansible/roles/tzdata/) for more details.
