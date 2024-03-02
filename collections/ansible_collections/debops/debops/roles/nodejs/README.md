### nodejs

[Node.js](https://nodejs.org/) is a JavaScript runtime environment which
can be used to execute JS code outside of the browser. It is commonly
used for server-side applications written in JavaScript.

There are two popular package managers in the Node.js ecosystem:
[NPM](https://npmjs.org/) which is bundled with Node.js, and
[Yarn](https://yarnpkg.org/), a third-party package manager that is
compatible with NPM.

The `debops.nodejs` Ansible role can be used to manage a Node.js
environment on a host. By default, it will install Node.js, NPM and Yarn
packages included in a given OS release (if possible), but it can also
automatically install or upgrade an existing installation to their
upstream versions.

Read the [nodejs role documentation](https://docs.debops.org/en/HEAD/ansible/roles/nodejs/) for more details.
