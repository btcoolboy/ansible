### hashicorp

The `debops.hashicorp` Ansible role can be used to securely install
[HashiCorp](https://en.wikipedia.org/wiki/HashiCorp) applications, such
as [Consul](https://consul.io/), [Terraform](https://terraform.io/),
[Vault](https://vaultproject.io/) and others.

The selected applications are downloaded from the HashiCorp release
repository, authenticated using the HashiCorp OpenPGP key and installed
on the system. After that, other Ansible roles can be used to configure
them as needed.

Read the [hashicorp role documentation](https://docs.debops.org/en/HEAD/ansible/roles/hashicorp/) for more details.
