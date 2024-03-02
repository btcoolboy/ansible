### tgt

This Ansible role will allow you to configure iSCSI Targets on specified
hosts using [tgt](http://stgt.sourceforge.net/) package. You can create
and remove specific iSCSI Targets without disrupting the connections of
other targets. Only targets that are unused will be modified during
normal operation. `debops.ferm` role will be used to manage `iptables`
firewall to allow access from all or specific hosts or networks.

Read the [tgt role documentation](https://docs.debops.org/en/HEAD/ansible/roles/tgt/) for more details.
