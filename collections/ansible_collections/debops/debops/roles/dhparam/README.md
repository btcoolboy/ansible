### dhparam

[Diffie-Hellman Key
Exchange](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange)
is a way to securely share encryption keys publicly between two parties.
It's used in TLS and SSL connections to provide [Perfect Forward
Secrecy](https://en.wikipedia.org/wiki/Forward_secrecy). Unfortunately,
the default DH parameters distributed with applications are susceptible
to a [downgrade attack](https://weakdh.org/).

The `debops.dhparam` Ansible role will generate a set of strong
Diffie-Hellman parameters on the Ansible Controller, which will be
preseeded on remote hosts, and will be ready to use by other
applications. A separate script can then be used on remote hosts in the
background to generate new random DH parameters, either once or in
regular intervals.

Read the [dhparam role documentation](https://docs.debops.org/en/HEAD/ansible/roles/dhparam/) for more details.
