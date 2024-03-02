### rabbitmq_management

[RabbitMQ](https://www.rabbitmq.com/) is an Open Source message broker
which supports
[AMQP](https://en.wikipedia.org/wiki/Advanced_Message_Queuing_Protocol),
[STOMP](https://en.wikipedia.org/wiki/Streaming_Text_Oriented_Messaging_Protocol)
and [MQTT](https://en.wikipedia.org/wiki/MQTT) protocols.

This ansible role can be used to enable and configure the [RabbitMQ
Management Console](https://www.rabbitmq.com/management.html). The role
can configure the plugin in a locally installed RabbitMQ service, or
configure a reverse proxy to a remote instance of RabbitMQ.

See the `debops.rabbitmq_server` Ansible role for general RabbitMQ
service deployment and configuration.

Read the [rabbitmq_management role documentation](https://docs.debops.org/en/HEAD/ansible/roles/rabbitmq_management/) for more details.
