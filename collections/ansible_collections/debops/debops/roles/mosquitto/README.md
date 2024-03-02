### mosquitto

[Mosquitto](https://mosquitto.org/) is an open source [Message Queue
Telemetry Transport (MQTT)](https://en.wikipedia.org/wiki/MQTT) broker
used in the [Internet of
Things](https://en.wikipedia.org/wiki/Internet_of_things) paradigm.

The `debops.mosquitto` Ansible role can be used to install and configure
Mosquitto on Debian/Ubuntu hosts. The role can use other DebOps roles to
manage firewall access to Mosquitto, publish Avahi services and
configure an nginx frontend for the Mosquitto WebSockets API.

Read the [mosquitto role documentation](https://docs.debops.org/en/HEAD/ansible/roles/mosquitto/) for more details.
