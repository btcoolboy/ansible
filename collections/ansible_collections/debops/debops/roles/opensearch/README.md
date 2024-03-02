### opensearch

[OpenSearch](https://www.opensearch.org/) is a fork of the popular
distributed search engine and storage system Elasticsearch (see
`debops.elasticsearch`). Some software vendors, for example Graylog,
have switched to OpenSearch because of legal concerns regarding the
Server Side Public License under which Elasticsearch is nowadays
released.

The `debops.opensearch` role only implements a subsection of the
features supported by `debops.elasticsearch`. The role is currently only
suitable for setting up a local OpenSearch instance without TLS support.

Read the [opensearch role documentation](https://docs.debops.org/en/HEAD/ansible/roles/opensearch/) for more details.
