### cryptsetup

`debops.cryptsetup` allows you to configure encrypted filesystems on top
of any given block device using
[dm-crypt](https://en.wikipedia.org/wiki/Dm-crypt)/[cryptsetup](https://gitlab.com/cryptsetup/cryptsetup)
and [LUKS](https://en.wikipedia.org/wiki/Linux_Unified_Key_Setup). A
random keyfile generated on the Ansible controller will be used for the
encryption by default. It is your responsibility that the keyfile is
kept secure for this to make sense. For example by storing the keyfile
on an already encrypted filesystem (both on the Ansible controller and
the remote system).

**Features:**

-   Create a random keyfile or use an already existing keyfile.
-   Manage `/etc/crypttab` and `/etc/fstab` and mount point directories.
-   Create a LUKS header backup and store it on the Ansible controller.
-   Decrypt and mount an encrypted filesystem and never store any key
    material on persistent storage on the remote system. You might need
    to take care of your Swap space yourself for this!
-   Setup an encrypted swap space (with random key or with persistent
    key).
-   Setup filesystems using a random key on boot.
-   `cryptsetup` plain, LUKS, TrueCrypt and VeraCrypt mode.
-   Multiple ciphers and corresponding keys chained to encrypt one
    filesystem.

Read the [cryptsetup role documentation](https://docs.debops.org/en/HEAD/ansible/roles/cryptsetup/) for more details.
