Changes for 1.13.2 since 1.13.1
-------------------------------

  - Documentation fixes for issues found by ansible-test part of ansible-core 2.17.1 (#1264)
  - tests/sanity/sanity.sh: Install setuptools with pip (#1263)
  - user: Fix idp_user_id aliases (#1262)
  - plugins/inventory/freeipa: Try imports for requests and urllib3 (#1261)
  - permission: Fix idempotency issues for DN parameters (#1259)
  - README-service.md: Add multi service handling (#1255)
  - Convert input certificates (#1250)
  - ansible_freeipa_module: Fix errors in batch mode (#1248)
  - Fixes for FreeIPA 4.12 (#1246)
  - Bump minimum supported Ansible version (#1130)

Detailed changelog for 1.13.2 since 1.13.1 by author
----------------------------------------------------
  2 authors, 35 commits

Rafael Guterres Jeffman (9)

  - ansible-freeipa.spec: Bump minimum supported Ansible version to 2.15
  - utils/templates: Bump minimum supported Ansible version to 2.15
  - ipasmartcard_*: Bump minimum supported Ansible version to 2.15
  - ipabackup: Bump minimum supported Ansible version to 2.15
  - ipaserver: Bump minimum supported Ansible version to 2.15
  - ipareplica: Bump minimum supported Ansible version to 2.15
  - ipaclient: Bump minimum supported Ansible version to 2.15
  - README-*: Bump minimum Ansible supported version to 2.15
  - Set collection ansible-core minimum version to 2.15

Thomas Woerner (26)

  - Role modules: Docs: Fix default value for string list parameters
  - tests/utils.py: Fix missing whitespace around arithmetic operator (E226)
  - ipareplica_prepare: Documentation: Fixed name of ipa_client_installed
  - ipaclient_setup_nss: Documentation: Add default for selinux_works
  - service: Docs: Fix required for name, add delete_continue to services
  - idp: Drop no_log from docs section, allow to log token_uri and keys_uri
  - idoverrideuser: Docs: Fix sshpubkey element type, nomembers type
  - cert: Fix short_description tag, add chain option, remove authors
  - inventory/freeipa: Documentation: Fix version_added and drop plugin_type
  - ipamodule_base_docs: Documentation: Fix default for delete_continue
  - tests/sanity/sanity.sh: Install setuptools with pip
  - user: Fix idp_user_id aliases
  - service: Add multi service examples to EXAMPLES
  - README-service.md: Add multi service handling
  - plugins/inventory/freeipa: Try imports for requests and urllib3
  - permission: Fix idempotency issues for DN parameters
  - ansible_freeipa_module: Fix errors in batch mode
  - ipauser: Use new convert_input_certificates
  - ipaidoverrideusere: Use new convert_input_certificates
  - ipahost: Use new convert_input_certificates
  - ipaservice: Use new convert_input_certificates
  - ansible_freeipa_module: New function convert_input_certificates
  - ipareplica: After an HSM replica install ensure all certs are visible
  - ipareplica: Refactor CA file handling
  - ipareplica_install_ca_certs: Do not return unchanged config attributes
  - ipaserver: Set hsm attributes to None for now

