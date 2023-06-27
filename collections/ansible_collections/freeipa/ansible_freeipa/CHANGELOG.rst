Changes for 1.11.0 since 1.10.0
-------------------------------

  - Multiple service management (#1101)
  - Don't allow the FQDN to match the domain on server installs (#1099)
  - upstream CI: Disable ansible-lint var-naming check (#1097)
  - Upstream CI: Disable execution of pytest tests (#1094)
  - tests/azure/templates/build_container.yml: Quote requests with version (#1092)
  - Pin requests to < 2.29 temporarily (#1089)
  - Fix new ansible lint disallowes ignores (#1088)
  - tests/azure: Install molecule-plguins to get docker driver (#1083)
  - pwpolicy test: Fix maxsequence test (#1082)
  - Fix typo in ipapwpolicy.py (#1081)
  - Create action group in collection for use with module_defaults (#1080)
  - ipapwpolicy: simplified and faster attribute verification (#1078)
  - Make Git ignore temporary and output files. (#1077)
  - Fixes and enhancements for utils/new_module and templates (#1035)
  - ipacert module (#687)

Detailed changelog for 1.11.0 since 1.10.0 by author
----------------------------------------------------
  5 authors, 30 commits

Denis Karpelevich (1)

  - Allow multiple services creation

Jacob Cutright (1)

  - Fix typo in ipapwpolicy.py

Rafael Guterres Jeffman (6)

  - Don't allow the FQDN to match the domain on server installs
  - upstream CI: Disable ansible-lint var-naming check
  - Upstream CI: Disable execution of pytest tests.
  - Make Git ignore temporary and output files.
  - utils/new_module: Ensure correct number of parameters for new_module
  - ipapwpolicy: simplified and faster attribute verification

Sam Morris (1)

  - New certificate management module.

Thomas Woerner (21)

  - pwpolicy test: Fix maxsequence test
  - ipaservice: Updated and new tests for certificates and multi service handling
  - ipaservice: Add Denis Karpelevich to the authors header
  - ipaservice: Properly Handle certs with leading or trailing white space
  - tests/azure/templates/build_container.yml: Quote requests with version
  - ansible_freeipa_module.py: Calm down ansible-test on print and sys.exit
  - ipaserver_test.py: Add missing default for random_serial_numbers
  - ansible-test: Do not use automatic field numbering specification
  - Use "#!/usr/bin/env python" for python shebang
  - Add -eu to all bash shebangs
  - Remove old or empty sanity ignore files
  - Pin requests to < 2.29 temporarily
  - tests/azure: Install molecule-plguins to get docker driver
  - utils/templates/test_module*.yml.in: Use generic module_defaults
  - utils/templates/test_module*.yml.in: Better docs for become and gather_facts
  - utils/templates/{README*.md.in,test_module*.yml.in}: Use true and false
  - utils/build-galaxy-release.sh: Create module action group
  - utils/galaxyfy.py: Handle module_defaults, match roles and modules
  - New utils/facts.py: Provide facts about the repo like role and module lists
  - utils/templates/ipamodule.py.in: Add missing bracket
  - utils/new_module: Fix github_user test

