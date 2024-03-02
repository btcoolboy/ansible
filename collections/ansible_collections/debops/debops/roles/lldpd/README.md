### lldpd

Link-Layer Discovery Protocol is an industry standard protocol which
enables network devices to exchange information about themselves with
their neighbors connected over network links. This in turn can be used
to locate other devices connected to a particular device and port.

The [lldpd](https://packages.debian.org/stable/lldpd) Debian package
provides a lightweight `lldpd` daemon which implements this protocol and
can be installed on Debian/Ubuntu based hosts to advertise the LLDP
notifications to other devices. This might be useful in more complex
environments with multiple layers of infrastructure comprised of
physical hosts, virtual machines and containers.

The `debops.lldpd` role can be used to install and manage the `lldpd`
service and by default will try to distinguish virtualized hosts (VMs,
containers) from physical ones to make their management easier by
changing their "ChassisID" attribute to reflect their virtualized
status.

Read the [lldpd role documentation](https://docs.debops.org/en/HEAD/ansible/roles/lldpd/) for more details.
