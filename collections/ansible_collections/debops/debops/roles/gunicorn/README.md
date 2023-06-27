### gunicorn

The [Green Unicorn](http://gunicorn.org/) is a Python WSGI HTTP Server
for UNIX. It uses a pre-fork worker model ported from Ruby's Unicorn
project. The Gunicorn server is broadly compatible with various web
frameworks, simply implemented, light on server resources, and fairly
speedy.

The `debops.gunicorn` Ansible role uses the [Debian package
configuration
structure](https://chris-lamb.co.uk/posts/sysadmin-friendly-deployment-gunicorn-debian)
on older Debian and Ubuntu releases to manage multiple `gunicorn`
applications as a single service. This can be used to deploy
applications that use either a system Python installation, or a
`virtualenv` Python environment.

From Debian Stretch upwards, the role configures a custom set of
`systemd` units to support Green Unicorn service instances.

Read the [gunicorn role documentation](https://docs.debops.org/en/stable-3.0/ansible/roles/gunicorn/) for more details.
