---
url: "https://clear.ml/docs/latest/docs/references/enterprise/server/"
title: "server | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/enterprise/server/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

### POST /server.config [​](https://clear.ml/docs/latest/docs/references/enterprise/server/\#post-serverconfig "Direct link to POST /server.config")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/server/\#description "Direct link to Description")

Internal. Get server config values

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/server/\#parameters "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/server/#server-config-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **path**<br>_optional_ | Path of config value. Defaults to root | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/server/\#responses "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/server/\#security "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | root,system |

### POST /server.db\_version [​](https://clear.ml/docs/latest/docs/references/enterprise/server/\#post-serverdb_version "Direct link to POST /server.db_version")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/server/\#description-1 "Direct link to Description")

Internal. Get database version

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/server/\#parameters-1 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/server/#server-db_version-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **history**<br>_optional_ | Whether to return previous versions | boolean |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/server/\#responses-1 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/server/\#security-1 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | root,system |

### POST /server.endpoints [​](https://clear.ml/docs/latest/docs/references/enterprise/server/\#post-serverendpoints "Direct link to POST /server.endpoints")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/server/\#description-2 "Direct link to Description")

Internal. Show available endpoints

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/server/\#parameters-2 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/server/\#responses-2 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/server/\#security-2 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | root,system |

### POST /server.health\_check [​](https://clear.ml/docs/latest/docs/references/enterprise/server/\#post-serverhealth_check "Direct link to POST /server.health_check")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/server/\#description-3 "Direct link to Description")

Internal. Perform a server health check (fails if errors were encountered)

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/server/\#parameters-3 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/server/\#responses-3 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/server/#server-health_check-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **errors**<br>_optional_ | Errors detected | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/server/\#security-3 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /server.health\_status [​](https://clear.ml/docs/latest/docs/references/enterprise/server/\#post-serverhealth_status "Direct link to POST /server.health_status")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/server/\#description-4 "Direct link to Description")

Internal. Get server health status

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/server/\#parameters-4 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/server/\#responses-4 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/server/#server-health_status-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **dbs**<br>_optional_ | Health status for various database infrastructure | object |
| **failed**<br>_optional_ | true if any errors were encountered, false otherwise | boolean |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/server/\#security-4 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | root,system |

### POST /server.info [​](https://clear.ml/docs/latest/docs/references/enterprise/server/\#post-serverinfo "Direct link to POST /server.info")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/server/\#description-5 "Direct link to Description")

Internal. Get server information, including version and build number

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/server/\#parameters-5 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/server/\#responses-5 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/server/#server-info-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **api\_version**<br>_optional_ | Max API version supported | string |
| **build**<br>_optional_ | Build number | string |
| **commit**<br>_optional_ | VCS commit number | string |
| **version**<br>_optional_ | Version string | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/server/\#security-5 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /server.report\_stats\_option [​](https://clear.ml/docs/latest/docs/references/enterprise/server/\#post-serverreport_stats_option "Direct link to POST /server.report_stats_option")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/server/\#description-6 "Direct link to Description")

Internal. Get or set the report statistics option per-company. Not supported.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/server/\#parameters-6 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/server/\#responses-6 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/server/#server-report_stats_option-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **enabled**<br>_optional_ | Returns the current report stats option value | boolean |
| **supported**<br>_optional_ | Is this feature supported by the server | boolean |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/server/\#security-6 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

- [POST /server.config](https://clear.ml/docs/latest/docs/references/enterprise/server/#post-serverconfig)
- [POST /server.db\_version](https://clear.ml/docs/latest/docs/references/enterprise/server/#post-serverdb_version)
- [POST /server.endpoints](https://clear.ml/docs/latest/docs/references/enterprise/server/#post-serverendpoints)
- [POST /server.health\_check](https://clear.ml/docs/latest/docs/references/enterprise/server/#post-serverhealth_check)
- [POST /server.health\_status](https://clear.ml/docs/latest/docs/references/enterprise/server/#post-serverhealth_status)
- [POST /server.info](https://clear.ml/docs/latest/docs/references/enterprise/server/#post-serverinfo)
- [POST /server.report\_stats\_option](https://clear.ml/docs/latest/docs/references/enterprise/server/#post-serverreport_stats_option)