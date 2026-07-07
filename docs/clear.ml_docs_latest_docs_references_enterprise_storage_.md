---
url: "https://clear.ml/docs/latest/docs/references/enterprise/storage/"
title: "storage | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/enterprise/storage/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

### POST /storage.get\_settings [​](https://clear.ml/docs/latest/docs/references/enterprise/storage/\#post-storageget_settings "Direct link to POST /storage.get_settings")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/storage/\#description "Direct link to Description")

Internal. Get storage settings

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/storage/\#parameters "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/storage/\#responses "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/storage/#storage-get_settings-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **aws**<br>_optional_ |  | [storage.aws](https://clear.ml/docs/latest/docs/references/enterprise/definitions#storageaws) |
| **azure**<br>_optional_ |  | [storage.azure](https://clear.ml/docs/latest/docs/references/enterprise/definitions#storageazure) |
| **google**<br>_optional_ |  | [storage.google](https://clear.ml/docs/latest/docs/references/enterprise/definitions#storagegoogle) |
| **last\_update**<br>_optional_ | Settings last update time (UTC) | string (date-time) |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/storage/\#security "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /storage.get\_user\_settings [​](https://clear.ml/docs/latest/docs/references/enterprise/storage/\#post-storageget_user_settings "Direct link to POST /storage.get_user_settings")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/storage/\#description-1 "Direct link to Description")

Get the calling user's personal storage credentials

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/storage/\#parameters-1 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/storage/\#responses-1 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/storage/#storage-get_user_settings-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **aws**<br>_optional_ |  | [storage.aws](https://clear.ml/docs/latest/docs/references/enterprise/definitions#storageaws) |
| **azure**<br>_optional_ |  | [storage.azure](https://clear.ml/docs/latest/docs/references/enterprise/definitions#storageazure) |
| **google**<br>_optional_ |  | [storage.google](https://clear.ml/docs/latest/docs/references/enterprise/definitions#storagegoogle) |
| **last\_update**<br>_optional_ | Settings last update time (UTC) | string (date-time) |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/storage/\#security-1 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /storage.reset\_settings [​](https://clear.ml/docs/latest/docs/references/enterprise/storage/\#post-storagereset_settings "Direct link to POST /storage.reset_settings")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/storage/\#description-2 "Direct link to Description")

Internal. Reset selected storage settings

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/storage/\#parameters-2 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/storage/#storage-reset_settings-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **keys**<br>_optional_ | The names of the settings to delete | < enum (azure, aws, google) > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/storage/\#responses-2 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/storage/#storage-reset_settings-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **updated**<br>_optional_ | Number of settings documents updated (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/storage/\#security-2 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /storage.reset\_user\_settings [​](https://clear.ml/docs/latest/docs/references/enterprise/storage/\#post-storagereset_user_settings "Direct link to POST /storage.reset_user_settings")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/storage/\#description-3 "Direct link to Description")

Reset selected personal storage credentials for the calling user

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/storage/\#parameters-3 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/storage/#storage-reset_user_settings-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **keys**<br>_optional_ | The names of the settings to delete | < enum (azure, aws, google) > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/storage/\#responses-3 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/storage/#storage-reset_user_settings-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **updated**<br>_optional_ | Number of settings documents updated (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/storage/\#security-3 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /storage.set\_settings [​](https://clear.ml/docs/latest/docs/references/enterprise/storage/\#post-storageset_settings "Direct link to POST /storage.set_settings")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/storage/\#description-4 "Direct link to Description")

Internal. Set Storage settings

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/storage/\#parameters-4 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/storage/#storage-set_settings-request) |

**request**

| Name | Schema |
| --- | --- |
| **aws**<br>_optional_ | [storage.aws](https://clear.ml/docs/latest/docs/references/enterprise/definitions#storageaws) |
| **azure**<br>_optional_ | [storage.azure](https://clear.ml/docs/latest/docs/references/enterprise/definitions#storageazure) |
| **google**<br>_optional_ | [storage.google](https://clear.ml/docs/latest/docs/references/enterprise/definitions#storagegoogle) |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/storage/\#responses-4 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/storage/#storage-set_settings-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **updated**<br>_optional_ | Number of settings documents updated (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/storage/\#security-4 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /storage.set\_user\_settings [​](https://clear.ml/docs/latest/docs/references/enterprise/storage/\#post-storageset_user_settings "Direct link to POST /storage.set_user_settings")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/storage/\#description-5 "Direct link to Description")

Set the calling user's personal storage credentials

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/storage/\#parameters-5 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/storage/#storage-set_user_settings-request) |

**request**

| Name | Schema |
| --- | --- |
| **aws**<br>_optional_ | [storage.aws](https://clear.ml/docs/latest/docs/references/enterprise/definitions#storageaws) |
| **azure**<br>_optional_ | [storage.azure](https://clear.ml/docs/latest/docs/references/enterprise/definitions#storageazure) |
| **google**<br>_optional_ | [storage.google](https://clear.ml/docs/latest/docs/references/enterprise/definitions#storagegoogle) |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/storage/\#responses-5 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/storage/#storage-set_user_settings-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **updated**<br>_optional_ | Number of settings documents updated (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/storage/\#security-5 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

- [POST /storage.get\_settings](https://clear.ml/docs/latest/docs/references/enterprise/storage/#post-storageget_settings)
- [POST /storage.get\_user\_settings](https://clear.ml/docs/latest/docs/references/enterprise/storage/#post-storageget_user_settings)
- [POST /storage.reset\_settings](https://clear.ml/docs/latest/docs/references/enterprise/storage/#post-storagereset_settings)
- [POST /storage.reset\_user\_settings](https://clear.ml/docs/latest/docs/references/enterprise/storage/#post-storagereset_user_settings)
- [POST /storage.set\_settings](https://clear.ml/docs/latest/docs/references/enterprise/storage/#post-storageset_settings)
- [POST /storage.set\_user\_settings](https://clear.ml/docs/latest/docs/references/enterprise/storage/#post-storageset_user_settings)