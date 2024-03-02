### authorized_keys

The `debops.authorized_keys` role can be used to manage SSH keys
centrally in the `/etc/ssh/authorized_keys/` directory. The role only
manages the keys themselves, you should configure the `sshd` service to
use them separately, for example by using the `debops.sshd` Ansible
role.

Read the [authorized_keys role documentation](https://docs.debops.org/en/HEAD/ansible/roles/authorized_keys/) for more details.
