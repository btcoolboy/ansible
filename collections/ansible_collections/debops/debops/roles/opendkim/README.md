### opendkim

[DomainKeys Identified
Mail](https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail) (DKIM)
standard can be used by organizations to automatically sign and verify
e-mail messages sent by their SMTP server(s). Other organizations can
verify signed messages using public keys retrieved from the DNS
database; the signature validity can then be used to classify e-mail
messages as wanted or not.

The [OpenDKIM](http://opendkim.org/) library implements DKIM in the form
of a Sendmail milter service, which can be used by SMTP servers. You can
use the `debops.opendkim` Ansible role to configure the OpenDKIM service
on one or multiple hosts. If `debops.postfix` role is used together with
this one, Postfix can be automatically configured to sign and verify
e-mail messages.

Read the [opendkim role documentation](https://docs.debops.org/en/HEAD/ansible/roles/opendkim/) for more details.
