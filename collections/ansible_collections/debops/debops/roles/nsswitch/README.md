### nsswitch

The `debops.nsswitch` Ansible role can be used to configure the Name
Service Switch using the `/etc/nsswitch.conf` configuration file. The
role can be used as a dependency of another Ansible role to allow
management of NSS services after they have been configured. System
administrators can use this role to enable or disable NSS services
conditionally or change the preferred order of the NSS services.

Read the [nsswitch role documentation](https://docs.debops.org/en/HEAD/ansible/roles/nsswitch/) for more details.
