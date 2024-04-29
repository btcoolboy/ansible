Changes for 1.12.1 since 1.12.0
-------------------------------

  - Disable config tests for pac type without ms pac (#1211)
  - ipaclient_setup_automount with new install states (#1208)
  - ipaclient: Enable SELinux for SSSD (#1207)
  - ipaserver: Fix deployment after Bronze-bit fix (#1206)
  - ipahbacrule: Fix handling of hbacsvcgroup in members (#1203)
  - ipahostgroup: Fix idempotence issues due to capitalization (#1202)
  - ipagroup: Fix idempotence issues due to capitalization (#1201)
  - Fixes for ansible-lint 6.22.1 (#1195)
  - Revert "[TEMP] Enable only idp, service and user module tests" (#1189)
  - Bump minimum ansible-lint version to 6.22 (#1188)
  - ipaclient: Fix OTP error reporting (#1187)
  - test_host_random: No jinja2 templating in conditional statements (#1186)
  - upstream ci: Increase timeout for PR tests (#1184)
  - ipaidp: Fix validation and reset of parameters (#1183)
  - test_pwpolicy: minlength parameter can be reset with empty string now (#1180)
  - ipagroup: Add support for renaming groups (#1178)
  - ipauser: Add support for renaming users (#1174)
  - ipaclient: Properly name automount_location var and add documentation (#1169)
  - ipareplica: Support inventory groups.ipaserver (#1151)
  - ipauser: Do not try to modify user when not changing password (#1149)
  - ipadnszone: Add support for per-zone privilege delegation (#1147)
  - Handle data type or empty string in module_utils (#1143)
  - ipasudorule: Allow setting groups for runasuser. (#899)
  - ipadelegation: Fix idempotence issues due to capitalization. (#760)

Detailed changelog for 1.12.1 since 1.12.0 by author
----------------------------------------------------
  2 authors, 31 commits

Rafael Guterres Jeffman (20)

  - ipadelegation: Fix idempotence issues due to capitalization.
  - ipagroup: Fix idempotence issues due to capitalization
  - ipahostgroup: Fix idempotence issues due to capitalization
  - ipaserver: Fix deployment after Bronze-bit fix
  - ipahbacrule: Fix handling of hbacsvcgroup in members
  - ipasudorule: Allow setting groups for runasuser.
  - ipagroup: Add support for renaming groups
  - tests/group: Use module_defaults on tests_group
  - ipauser: Add support for renaming users
  - ipadnszone: Add support for per-zone privilege delegation
  - idoveridegroup: Use module.params_get_type
  - idoverideuser: Use module.params_get_type
  - ipapwpolicy: Use modules.params_get_type
  - ansible_freeipa_module: Ensure data type when retrieving parameter
  - Rename parameter 'allow_empty_string' to 'allow_empty_list_item'
  - upstream ci: Increase timeout for PR tests
  - Bump minimum ansible-lint version to 6.22
  - ipaclient: Fix OTP error reporting
  - ipauser: Do not try to modify user when not changing password
  - ipareplica: Support inventory groups.ipaserver

Thomas Woerner (11)

  - config: Disable config tests due to pac type requirement MS-PAC
  - ipaclient_setup_automount: Only return changed if there was a change
  - ipaclient_setup_automount with new install states
  - ipaclient: Enable SELinux for SSSD
  - Fixes for ansible-lint 6.22.1
  - Revert "[TEMP] Enable only idp, service and user module tests"
  - test_host_random: No jinja2 templating in conditional statements
  - [TEMP] Enable only idp, service and user module tests
  - ipaidp: Fix validation and reset of parameters
  - test_pwpolicy: minlength parameter can be reset with empty string now
  - ipaclient: Properly name automount_location var and add documentation

