---
url: "https://clear.ml/docs/latest/docs/references/api/"
title: "ClearML REST API Reference | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/api/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The ClearML Server exposes a comprehensive REST API.

The API reference pages are split into two main sections:

- [Object definitions](https://clear.ml/docs/latest/docs/references/api/#object-definitions) \- Detailed specification of available objects
- [Service definitions](https://clear.ml/docs/latest/docs/references/api/#service-definitions) \- Specification of the available REST services

## Object Definitions [​](https://clear.ml/docs/latest/docs/references/api/\#object-definitions "Direct link to Object Definitions")

See the Rest API object definitions reference page to view descriptions of the objects used in API requests:

- [Open Source Server](https://clear.ml/docs/latest/docs/references/api/definitions)
- [Enterprise Server](https://clear.ml/docs/latest/docs/references/enterprise/definitions)

## Service Definitions [​](https://clear.ml/docs/latest/docs/references/api/\#service-definitions "Direct link to Service Definitions")

The ClearML [Open Source](https://clear.ml/docs/latest/docs/references/api/#open-source-server-api-services) and [Enterprise](https://clear.ml/docs/latest/docs/references/api/#enterprise-server-api-services) offerings each support their own API sets.

### Open Source Server API Services [​](https://clear.ml/docs/latest/docs/references/api/\#open-source-server-api-services "Direct link to Open Source Server API Services")

- [debug](https://clear.ml/docs/latest/docs/references/api/debug) \- Debugging utilities.
- [events](https://clear.ml/docs/latest/docs/references/api/events) \- Event reporting and retrieval (e.g., metrics, debug samples)
- [login](https://clear.ml/docs/latest/docs/references/api/login) \- Authentication management, authorization and administration for the entire system.
- [models](https://clear.ml/docs/latest/docs/references/api/models) \- Model management: create, edit, update metadata and tags, move, publish, archive, set visibility, and retrieve models.
- [pipelines](https://clear.ml/docs/latest/docs/references/api/pipelines) – Pipeline management: create, update, execute, monitor, and query pipelines.
- [projects](https://clear.ml/docs/latest/docs/references/api/projects) \- Project management for creating, updating, retrieving, and controlling access
- [queues](https://clear.ml/docs/latest/docs/references/api/queues) \- [Queue](https://clear.ml/docs/latest/docs/fundamentals/agents_and_queues#what-is-a-queue) management (see [Workers](https://clear.ml/docs/latest/docs/references/api/workers) Service).
- [reports](https://clear.ml/docs/latest/docs/references/api/reports) – Report management: create, update, publish, archive, move, and query Reports.
- [serving](https://clear.ml/docs/latest/docs/references/api/serving) – Model serving configuration and endpoint management.
- [tasks](https://clear.ml/docs/latest/docs/references/api/tasks) \- [Task](https://clear.ml/docs/latest/docs/fundamentals/task) Management API.
- [workers](https://clear.ml/docs/latest/docs/references/api/workers) \- Worker registration, status reporting, and task execution

### Enterprise Server API Services [​](https://clear.ml/docs/latest/docs/references/api/\#enterprise-server-api-services "Direct link to Enterprise Server API Services")

- [apps](https://clear.ml/docs/latest/docs/references/enterprise/apps) – ClearML UI Application templates and instance management.
- [auth](https://clear.ml/docs/latest/docs/references/enterprise/auth) – User authentication, credential management, and token generation.
- [datasets](https://clear.ml/docs/latest/docs/references/enterprise/datasets) – HyperDataset management API
- [debug](https://clear.ml/docs/latest/docs/references/enterprise/debug) – Debugging utilities
- [events](https://clear.ml/docs/latest/docs/references/enterprise/events) – Event reporting and retrieval (e.g., metrics, debug samples)
- [frames](https://clear.ml/docs/latest/docs/references/enterprise/frames) – HyperDataset frame (entry) retrieval
- [login](https://clear.ml/docs/latest/docs/references/enterprise/login) – Authentication management, authorization and administration for the entire system.
- [models](https://clear.ml/docs/latest/docs/references/enterprise/models) – Model management: create, edit, update metadata and tags, move, publish, archive, set visibility, and retrieve models.
- [organization](https://clear.ml/docs/latest/docs/references/enterprise/organization) – Manage organizations, users, invites, and company metadata.
- [permissions](https://clear.ml/docs/latest/docs/references/enterprise/permissions) – Manage user groups, access rules, and entity-level permissions.
- [pipelines](https://clear.ml/docs/latest/docs/references/enterprise/pipelines) – Pipeline management: create, update, execute, monitor, and query pipelines.
- [projects](https://clear.ml/docs/latest/docs/references/enterprise/projects) – Project management API for creating, updating, organizing, querying, and controlling access to Projects
- [queues](https://clear.ml/docs/latest/docs/references/enterprise/queues) – Queue management API (see Workers Service).
- [reports](https://clear.ml/docs/latest/docs/references/enterprise/reports) – Report management API for creating, editing, publishing, archiving, moving, and querying ClearML Reports.
- [resources](https://clear.ml/docs/latest/docs/references/enterprise/resources) – Resource policies, configurations, and allocation management.
- [routers](https://clear.ml/docs/latest/docs/references/enterprise/routers) – Request routing rules and task router configuration.
- [server](https://clear.ml/docs/latest/docs/references/enterprise/server) – Server configuration, health, status, and version information retrieval.
- [serving](https://clear.ml/docs/latest/docs/references/enterprise/serving) – Model serving configuration and endpoint management.
- [sso](https://clear.ml/docs/latest/docs/references/enterprise/sso) – Single sign-on (SSO) provider management and authentication testing.
- [storage](https://clear.ml/docs/latest/docs/references/enterprise/storage) – Storage settings and configuration management.
- [system](https://clear.ml/docs/latest/docs/references/enterprise/system) – Companies, datasets, and system-wide configuration.
- [tasks](https://clear.ml/docs/latest/docs/references/enterprise/tasks) – Task management API.
- [tenants](https://clear.ml/docs/latest/docs/references/enterprise/tenants) –Tenant information retrieval
- [users](https://clear.ml/docs/latest/docs/references/enterprise/users) – User accounts, preferences, service users, and access-related information.
- [variables](https://clear.ml/docs/latest/docs/references/enterprise/variables) – Global variables and counters management.
- [workers](https://clear.ml/docs/latest/docs/references/enterprise/workers) – Worker registration, status reporting, and task execution

## Request Format [​](https://clear.ml/docs/latest/docs/references/api/\#request-format "Direct link to Request Format")

An API request is formatted in the following way:

```console
base_url/endpoint
```

Where the `base_url` is the `api_server` configured in your `clearml.conf` file (e.g. `https://api.clear.ml`) and the
endpoint is as specified for the available services. The content-type is `application/json`.

Requests need to be authenticated with a bearer token that identifies the workspace that you want to work with.
An initial request of `GET /auth.login`, using the basic authorization scheme generates this token to be used with all
subsequent API requests. The authorization header contains `Basic <credentials>` where `credentials`
is `base64("<key>:<secret>")` using ClearML credentials (access key and secret key).

```console
curl -u "<access_key>:<secret_key>" -X GET https://<base_url>/auth.login
```

This call will return the token. By default, the token expires in 30 days. Generate a token with a shorter expiration
time by specifying the `expiration_sec` field (as a query parameter or as a JSON payload).

- [Object Definitions](https://clear.ml/docs/latest/docs/references/api/#object-definitions)
- [Service Definitions](https://clear.ml/docs/latest/docs/references/api/#service-definitions)
  - [Open Source Server API Services](https://clear.ml/docs/latest/docs/references/api/#open-source-server-api-services)
  - [Enterprise Server API Services](https://clear.ml/docs/latest/docs/references/api/#enterprise-server-api-services)
- [Request Format](https://clear.ml/docs/latest/docs/references/api/#request-format)