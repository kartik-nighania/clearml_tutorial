---
url: "https://clear.ml/docs/latest/docs/references/enterprise/debug/"
title: "debug | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/enterprise/debug/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

### POST /debug.apiex [​](https://clear.ml/docs/latest/docs/references/enterprise/debug/\#post-debugapiex "Direct link to POST /debug.apiex")

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/debug/\#parameters "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/debug/\#responses "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

### POST /debug.echo [​](https://clear.ml/docs/latest/docs/references/enterprise/debug/\#post-debugecho "Direct link to POST /debug.echo")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/debug/\#description "Direct link to Description")

Return request data

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/debug/\#parameters-1 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/debug/\#responses-1 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

### POST /debug.ex [​](https://clear.ml/docs/latest/docs/references/enterprise/debug/\#post-debugex "Direct link to POST /debug.ex")

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/debug/\#parameters-2 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/debug/\#responses-2 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

### POST /debug.ping [​](https://clear.ml/docs/latest/docs/references/enterprise/debug/\#post-debugping "Direct link to POST /debug.ping")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/debug/\#description-1 "Direct link to Description")

Return a message. Does not require authorization.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/debug/\#parameters-3 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/debug/\#responses-3 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/debug/#debug-ping-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **msg**<br>_optional_ | A friendly message | string |

### POST /debug.ping\_auth [​](https://clear.ml/docs/latest/docs/references/enterprise/debug/\#post-debugping_auth "Direct link to POST /debug.ping_auth")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/debug/\#description-2 "Direct link to Description")

Return a message. Requires authorization.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/debug/\#parameters-4 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/debug/\#responses-4 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/debug/#debug-ping_auth-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **msg**<br>_optional_ | A friendly message | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/debug/\#security "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

- [POST /debug.apiex](https://clear.ml/docs/latest/docs/references/enterprise/debug/#post-debugapiex)
- [POST /debug.echo](https://clear.ml/docs/latest/docs/references/enterprise/debug/#post-debugecho)
- [POST /debug.ex](https://clear.ml/docs/latest/docs/references/enterprise/debug/#post-debugex)
- [POST /debug.ping](https://clear.ml/docs/latest/docs/references/enterprise/debug/#post-debugping)
- [POST /debug.ping\_auth](https://clear.ml/docs/latest/docs/references/enterprise/debug/#post-debugping_auth)