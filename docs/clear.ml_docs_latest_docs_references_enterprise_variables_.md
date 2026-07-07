---
url: "https://clear.ml/docs/latest/docs/references/enterprise/variables/"
title: "variables | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/enterprise/variables/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

### POST /variables.delete\_global\_vars [​](https://clear.ml/docs/latest/docs/references/enterprise/variables/\#post-variablesdelete_global_vars "Direct link to POST /variables.delete_global_vars")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/variables/\#description "Direct link to Description")

Delete global vars

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/variables/\#parameters "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/variables/#variables-delete_global_vars-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **keys**<br>_required_ | The keys of the variables to delete | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/variables/\#responses "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/variables/#variables-delete_global_vars-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **deleted**<br>_optional_ | The number of the deleted vars | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/variables/\#security "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /variables.get\_global\_vars [​](https://clear.ml/docs/latest/docs/references/enterprise/variables/\#post-variablesget_global_vars "Direct link to POST /variables.get_global_vars")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/variables/\#description-1 "Direct link to Description")

Get global vars

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/variables/\#parameters-1 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/variables/#variables-get_global_vars-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **keys**<br>_required_ | The keys of the variables to retrieve | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/variables/\#responses-1 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/variables/#variables-get_global_vars-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **vars**<br>_optional_ | Retrieved variables | < [vars](https://clear.ml/docs/latest/docs/references/enterprise/variables/#variables-get_global_vars-post-vars) \> array |

**vars**

| Name | Description | Schema |
| --- | --- | --- |
| **key**<br>_optional_ | Vauriable key | string |
| **value**<br>_optional_ | Variable value | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/variables/\#security-1 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /variables.increment\_global\_vars [​](https://clear.ml/docs/latest/docs/references/enterprise/variables/\#post-variablesincrement_global_vars "Direct link to POST /variables.increment_global_vars")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/variables/\#description-2 "Direct link to Description")

Increment global vars

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/variables/\#parameters-2 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/variables/#variables-increment_global_vars-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **commands**<br>_required_ | commands | < [variables.increment\_command](https://clear.ml/docs/latest/docs/references/enterprise/definitions#variablesincrement_command) \> array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/variables/\#responses-2 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/variables/#variables-increment_global_vars-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **vars**<br>_optional_ | Updated variables | < [vars](https://clear.ml/docs/latest/docs/references/enterprise/variables/#variables-increment_global_vars-post-vars) \> array |

**vars**

| Name | Description | Schema |
| --- | --- | --- |
| **increment**<br>_optional_ | The value by which the variable was incremented. 0 if no increment was done | integer |
| **key**<br>_optional_ | Vauriable key | string |
| **value**<br>_optional_ | The new variable value after the increment | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/variables/\#security-2 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /variables.set\_global\_vars [​](https://clear.ml/docs/latest/docs/references/enterprise/variables/\#post-variablesset_global_vars "Direct link to POST /variables.set_global_vars")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/variables/\#description-3 "Direct link to Description")

Set global vars

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/variables/\#parameters-3 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/variables/#variables-set_global_vars-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **vars**<br>_required_ | vars | < [variables.variable](https://clear.ml/docs/latest/docs/references/enterprise/definitions#variablesvariable) \> array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/variables/\#responses-3 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/variables/#variables-set_global_vars-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **updated**<br>_optional_ | The number of variables set | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/variables/\#security-3 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

- [POST /variables.delete\_global\_vars](https://clear.ml/docs/latest/docs/references/enterprise/variables/#post-variablesdelete_global_vars)
- [POST /variables.get\_global\_vars](https://clear.ml/docs/latest/docs/references/enterprise/variables/#post-variablesget_global_vars)
- [POST /variables.increment\_global\_vars](https://clear.ml/docs/latest/docs/references/enterprise/variables/#post-variablesincrement_global_vars)
- [POST /variables.set\_global\_vars](https://clear.ml/docs/latest/docs/references/enterprise/variables/#post-variablesset_global_vars)