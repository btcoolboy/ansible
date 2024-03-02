### timesyncd

THe `systemd-timesyncd(8)` service is a lightweight SNTP and NTP
(Network Time Protocol) client developed as a part of the
[systemd](https://www.freedesktop.org/wiki/Software/systemd/) project.
It provides time synchronization with NTP server network on hardware and
virtualized hosts.

The `debops.timesyncd` Ansible role can be used to configure the
`systemd-timesyncd` service. It will detect presence of alternative NTP
clients/servers installed on the host and back off when they are
detected, so that users can easily switch to a different service
provider if they wish.

Read the [timesyncd role documentation](https://docs.debops.org/en/HEAD/ansible/roles/timesyncd/) for more details.
