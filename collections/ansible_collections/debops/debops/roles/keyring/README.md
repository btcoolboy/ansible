### keyring

The `debops.keyring` Ansible role is designed as a helper for other
Ansible roles that manages the APT keyring as well as the GPG keyrings
on unprivileged UNIX accounts. Other Ansible roles can tell the
`debops.keyring` role which GPG keys should be present or absent in the
selected keyrings; the role then retrieves the GPG keys either from:

-   local key store in the `debops.keyring` role, or located in a
    directory on the Ansible Controller, or
-   specified URL, or
-   specified <span class="title-ref">Keybase</span>\_\_ profile via the
    <span class="title-ref">Keybase API</span>\_\_, or
-   a default GPG keyserver, if defined

Warning

The role is not meant to be used via Ansible inventory to manage the APT
or GPG keys; users can use the `debops.apt` role to manage the APT
keyring via the inventory.

At the moment there is no solution for unprivileged UNIX account
keyrings manageable via the inventory. This functionality will be
implemented later via other DebOps roles that manage UNIX accounts.

Read the [keyring role documentation](https://docs.debops.org/en/HEAD/ansible/roles/keyring/) for more details.
