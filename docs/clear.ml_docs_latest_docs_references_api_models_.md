---
url: "https://clear.ml/docs/latest/docs/references/api/models/"
title: "models | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/api/models/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

### POST /models.add\_or\_update\_metadata [​](https://clear.ml/docs/latest/docs/references/api/models/\#post-modelsadd_or_update_metadata "Direct link to POST /models.add_or_update_metadata")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/models/\#description "Direct link to Description")

Add or update model metadata

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/models/\#parameters "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/models/#models-add_or_update_metadata-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **metadata**<br>_required_ | Metadata items to add or update | < [models.metadata\_item](https://clear.ml/docs/latest/docs/references/api/definitions#modelsmetadata_item) \> array |
| **model**<br>_required_ | ID of the model | string |
| **replace\_metadata**<br>_optional_ | If set then the all the metadata items will be replaced with the provided ones. <br>Otherwise only the provided metadata items will be updated or added <br>**Default** : `false` | boolean |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/models/\#responses "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/models/#models-add_or_update_metadata-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **updated**<br>_optional_ | Number of models updated (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/models/\#security "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /models.archive\_many [​](https://clear.ml/docs/latest/docs/references/api/models/\#post-modelsarchive_many "Direct link to POST /models.archive_many")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/models/\#description-1 "Direct link to Description")

Archive models

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/models/\#parameters-1 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/models/#models-archive_many-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **ids**<br>_required_ | IDs of the models to archive | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/models/\#responses-1 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/models/#models-archive_many-response-200) |

**Response 200**

| Name | Schema |
| --- | --- |
| **failed**<br>_optional_ | < [failed](https://clear.ml/docs/latest/docs/references/api/models/#models-archive_many-post-failed) \> array |
| **succeeded**<br>_optional_ | < [succeeded](https://clear.ml/docs/latest/docs/references/api/models/#models-archive_many-post-succeeded) \> array |

**failed**

| Name | Description | Schema |
| --- | --- | --- |
| **error**<br>_optional_ | Error info | [error](https://clear.ml/docs/latest/docs/references/api/models/#models-archive_many-post-failed-error) |
| **id**<br>_optional_ | ID of the failed entity | string |

**error**

| Name | Schema |
| --- | --- |
| **codes**<br>_optional_ | < integer > array |
| **data**<br>_optional_ | object |
| **msg**<br>_optional_ | string |

**succeeded**

| Name | Description | Schema |
| --- | --- | --- |
| **archived**<br>_optional_ | Indicates whether the model was archived | boolean |
| **id**<br>_optional_ | ID of the succeeded entity | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/models/\#security-1 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /models.create [​](https://clear.ml/docs/latest/docs/references/api/models/\#post-modelscreate "Direct link to POST /models.create")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/models/\#description-2 "Direct link to Description")

Create a new model not associated with a task

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/models/\#parameters-2 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/models/#models-create-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **comment**<br>_optional_ | Model comment | string |
| **design**<br>_optional_ | Json\[d\] object representing the model design. Should be identical to the <br>network design of the task which created the model | object |
| **framework**<br>_optional_ | Framework on which the model is based. Case insensitive. Should be identical to <br>the framework of the task which created the model. | string |
| **labels**<br>_optional_ | Json object | < string, integer > map |
| **metadata**<br>_optional_ | Model metadata | < string, [models.metadata\_item](https://clear.ml/docs/latest/docs/references/api/definitions#modelsmetadata_item) \> map |
| **name**<br>_required_ | Model name Unique within the company. | string |
| **parent**<br>_optional_ | Parent model | string |
| **project**<br>_optional_ | Project to which to model belongs | string |
| **public**<br>_optional_ | Create a public model Default is false. <br>**Default** : `false` | boolean |
| **ready**<br>_optional_ | Indication if the model is final and can be used by other tasks. Default is <br>false. <br>**Default** : `false` | boolean |
| **system\_tags**<br>_optional_ | System tags list. This field is reserved for system use, please don't use it. | < string > array |
| **tags**<br>_optional_ | User-defined tags list | < string > array |
| **task**<br>_optional_ | Associated task ID | string |
| **uri**<br>_required_ | URI for the model | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/models/\#responses-2 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/models/#models-create-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **created**<br>_optional_ | Was the model created | boolean |
| **id**<br>_optional_ | ID of the model | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/models/\#security-2 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /models.delete [​](https://clear.ml/docs/latest/docs/references/api/models/\#post-modelsdelete "Direct link to POST /models.delete")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/models/\#description-3 "Direct link to Description")

Delete a model.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/models/\#parameters-3 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/models/#models-delete-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **force**<br>_optional_ | Force. Required if there are tasks that use the model as an execution model, or <br>if the model's creating task is published. | boolean |
| **model**<br>_required_ | Model ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/models/\#responses-3 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/models/#models-delete-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **deleted**<br>_optional_ | Indicates whether the model was deleted | boolean |
| **url**<br>_optional_ | The url of the model file | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/models/\#security-3 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /models.delete\_many [​](https://clear.ml/docs/latest/docs/references/api/models/\#post-modelsdelete_many "Direct link to POST /models.delete_many")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/models/\#description-4 "Direct link to Description")

Delete models

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/models/\#parameters-4 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/models/#models-delete_many-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **force**<br>_optional_ | Force. Required if there are tasks that use the model as an execution model, or <br>if the model's creating task is published. | boolean |
| **ids**<br>_required_ | IDs of the models to delete | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/models/\#responses-4 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/models/#models-delete_many-response-200) |

**Response 200**

| Name | Schema |
| --- | --- |
| **failed**<br>_optional_ | < [failed](https://clear.ml/docs/latest/docs/references/api/models/#models-delete_many-post-failed) \> array |
| **succeeded**<br>_optional_ | < [succeeded](https://clear.ml/docs/latest/docs/references/api/models/#models-delete_many-post-succeeded) \> array |

**failed**

| Name | Description | Schema |
| --- | --- | --- |
| **error**<br>_optional_ | Error info | [error](https://clear.ml/docs/latest/docs/references/api/models/#models-delete_many-post-failed-error) |
| **id**<br>_optional_ | ID of the failed entity | string |

**error**

| Name | Schema |
| --- | --- |
| **codes**<br>_optional_ | < integer > array |
| **data**<br>_optional_ | object |
| **msg**<br>_optional_ | string |

**succeeded**

| Name | Description | Schema |
| --- | --- | --- |
| **deleted**<br>_optional_ | Indicates whether the model was deleted | boolean |
| **id**<br>_optional_ | ID of the succeeded entity | string |
| **url**<br>_optional_ | The url of the model file | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/models/\#security-4 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /models.delete\_metadata [​](https://clear.ml/docs/latest/docs/references/api/models/\#post-modelsdelete_metadata "Direct link to POST /models.delete_metadata")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/models/\#description-5 "Direct link to Description")

Delete metadata from model

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/models/\#parameters-5 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/models/#models-delete_metadata-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **keys**<br>_required_ | The list of metadata keys to delete | < string > array |
| **model**<br>_required_ | ID of the model | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/models/\#responses-5 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/models/#models-delete_metadata-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **updated**<br>_optional_ | Number of models updated (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/models/\#security-5 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /models.edit [​](https://clear.ml/docs/latest/docs/references/api/models/\#post-modelsedit "Direct link to POST /models.edit")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/models/\#description-6 "Direct link to Description")

Edit an existing model

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/models/\#parameters-6 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/models/#models-edit-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **comment**<br>_optional_ | Model comment | string |
| **design**<br>_optional_ | Json\[d\] object representing the model design. Should be identical to the <br>network design of the task which created the model | object |
| **framework**<br>_optional_ | Framework on which the model is based. Case insensitive. Should be identical to <br>the framework of the task which created the model. | string |
| **iteration**<br>_optional_ | Iteration (used to update task statistics) | integer |
| **labels**<br>_optional_ | Json object | < string, integer > map |
| **metadata**<br>_optional_ | Model metadata | < string, [models.metadata\_item](https://clear.ml/docs/latest/docs/references/api/definitions#modelsmetadata_item) \> map |
| **model**<br>_required_ | Model ID | string |
| **name**<br>_optional_ | Model name Unique within the company. | string |
| **parent**<br>_optional_ | Parent model | string |
| **project**<br>_optional_ | Project to which to model belongs | string |
| **ready**<br>_optional_ | Indication if the model is final and can be used by other tasks | boolean |
| **system\_tags**<br>_optional_ | System tags list. This field is reserved for system use, please don't use it. | < string > array |
| **tags**<br>_optional_ | User-defined tags list | < string > array |
| **task**<br>_optional_ | Associated task ID | string |
| **uri**<br>_optional_ | URI for the model | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/models/\#responses-6 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/models/#models-edit-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **fields**<br>_optional_ | Updated fields names and values | object |
| **updated**<br>_optional_ | Number of models updated (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/models/\#security-6 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /models.get\_all [​](https://clear.ml/docs/latest/docs/references/api/models/\#post-modelsget_all "Direct link to POST /models.get_all")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/models/\#description-7 "Direct link to Description")

Get all models

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/models/\#parameters-7 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/models/#models-get_all-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **_all_**<br>_optional_ | Multi-field pattern condition (all fields match pattern) | [models.multi\_field\_pattern\_data](https://clear.ml/docs/latest/docs/references/api/definitions#modelsmulti_field_pattern_data) |
| **_any_**<br>_optional_ | Multi-field pattern condition (any field matches pattern) | [models.multi\_field\_pattern\_data](https://clear.ml/docs/latest/docs/references/api/definitions#modelsmulti_field_pattern_data) |
| **framework**<br>_optional_ | List of frameworks | < string > array |
| **id**<br>_optional_ | List of model IDs | < string > array |
| **include\_subprojects**<br>_optional_ | If set to 'true' and project field is set then models from the subprojects are <br>searched too <br>**Default** : `false` | boolean |
| **last\_update**<br>_optional_ | List of last\_update constraint strings (utcformat, epoch) with an optional <br>prefix modifier (>, >=, <, <=) | < string > array |
| **name**<br>_optional_ | Get only models whose name matches this pattern (python regular expression <br>syntax) | string |
| **only\_fields**<br>_optional_ | List of model field names (if applicable, nesting is supported using '.'). If <br>provided, this list defines the query's projection (only these fields will be <br>returned for each result entry) | < string > array |
| **order\_by**<br>_optional_ | List of field names to order by. When search\_text is used, '@text\_score' can be <br>used as a field representing the text score of returned documents. Use '-' <br>prefix to specify descending order. Optional, recommended when using page | < string > array |
| **page**<br>_optional_ | Page number, returns a specific page out of the resulting list of models <br>**Minimum value** : `0` | integer |
| **page\_size**<br>_optional_ | Page size, specifies the number of results returned in each page (last page may <br>contain fewer results) <br>**Minimum value** : `1` | integer |
| **project**<br>_optional_ | List of associated project IDs | < string > array |
| **ready**<br>_optional_ | Indication whether to retrieve only models that are marked ready If not <br>supplied returns both ready and not-ready projects. | boolean |
| **refresh\_scroll**<br>_optional_ | If set then all the data received with this scroll will be requeried | boolean |
| **scroll\_id**<br>_optional_ | Scroll ID returned from the previos calls to get\_all | string |
| **search\_text**<br>_optional_ | Free text search query | string |
| **size**<br>_optional_ | The number of models to retrieve <br>**Minimum value** : `1` | integer |
| **system\_tags**<br>_optional_ | System tags list used to filter results. Prepend '-' to system tag name to <br>indicate exclusion | < string > array |
| **tags**<br>_optional_ | User-defined tags list used to filter results. Prepend '-' to tag name to <br>indicate exclusion | < string > array |
| **task**<br>_optional_ | List of associated task IDs | < string > array |
| **uri**<br>_optional_ | List of model URIs | < string > array |
| **user**<br>_optional_ | List of user IDs used to filter results by the model's creating user | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/models/\#responses-7 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/models/#models-get_all-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **models**<br>_optional_ | Models list | < [models.model](https://clear.ml/docs/latest/docs/references/api/definitions#modelsmodel) \> array |
| **scroll\_id**<br>_optional_ | Scroll ID that can be used with the next calls to get\_all to retrieve more data | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/models/\#security-7 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /models.get\_by\_id [​](https://clear.ml/docs/latest/docs/references/api/models/\#post-modelsget_by_id "Direct link to POST /models.get_by_id")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/models/\#description-8 "Direct link to Description")

Gets model information

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/models/\#parameters-8 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/models/#models-get_by_id-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **model**<br>_required_ | Model id | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/models/\#responses-8 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/models/#models-get_by_id-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **model**<br>_optional_ | Model info | [models.model](https://clear.ml/docs/latest/docs/references/api/definitions#modelsmodel) |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/models/\#security-8 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /models.get\_by\_task\_id [​](https://clear.ml/docs/latest/docs/references/api/models/\#post-modelsget_by_task_id "Direct link to POST /models.get_by_task_id")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/models/\#description-9 "Direct link to Description")

Gets model information

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/models/\#parameters-9 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/models/#models-get_by_task_id-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **task**<br>_optional_ | Task id | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/models/\#responses-9 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/models/#models-get_by_task_id-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **model**<br>_optional_ | Model info | [models.model](https://clear.ml/docs/latest/docs/references/api/definitions#modelsmodel) |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/models/\#security-9 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /models.get\_frameworks [​](https://clear.ml/docs/latest/docs/references/api/models/\#post-modelsget_frameworks "Direct link to POST /models.get_frameworks")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/models/\#description-10 "Direct link to Description")

Get the list of frameworks used in the company models

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/models/\#parameters-10 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/models/#models-get_frameworks-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **projects**<br>_optional_ | The list of projects which models will be analyzed. If not passed or empty then <br>all the company and public models will be analyzed | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/models/\#responses-10 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/models/#models-get_frameworks-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **frameworks**<br>_optional_ | Unique list of the frameworks used in the company models | < string > array |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/models/\#security-10 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /models.make\_private [​](https://clear.ml/docs/latest/docs/references/api/models/\#post-modelsmake_private "Direct link to POST /models.make_private")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/models/\#description-11 "Direct link to Description")

Convert public models to private

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/models/\#parameters-11 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/models/#models-make_private-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **ids**<br>_optional_ | Ids of the models to convert. Only the models originated by the company can be <br>converted | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/models/\#responses-11 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/models/#models-make_private-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **updated**<br>_optional_ | Number of models updated | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/models/\#security-11 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /models.make\_public [​](https://clear.ml/docs/latest/docs/references/api/models/\#post-modelsmake_public "Direct link to POST /models.make_public")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/models/\#description-12 "Direct link to Description")

Convert company models to public

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/models/\#parameters-12 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/models/#models-make_public-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **ids**<br>_optional_ | Ids of the models to convert | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/models/\#responses-12 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/models/#models-make_public-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **updated**<br>_optional_ | Number of models updated | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/models/\#security-12 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /models.move [​](https://clear.ml/docs/latest/docs/references/api/models/\#post-modelsmove "Direct link to POST /models.move")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/models/\#description-13 "Direct link to Description")

Move models to a project

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/models/\#parameters-13 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/models/#models-move-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **ids**<br>_required_ | Models to move | < string > array |
| **project**<br>_optional_ | Target project ID. If not provided, `project_name` must be provided. Use null <br>for the root project | string |
| **project\_name**<br>_optional_ | Target project name. If provided and a project with this name does not exist, a <br>new project will be created. If not provided, `project` must be provided. | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/models/\#responses-13 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/models/\#security-13 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /models.publish\_many [​](https://clear.ml/docs/latest/docs/references/api/models/\#post-modelspublish_many "Direct link to POST /models.publish_many")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/models/\#description-14 "Direct link to Description")

Publish models

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/models/\#parameters-14 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/models/#models-publish_many-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **force\_publish\_task**<br>_optional_ | Publish the associated tasks (if exist) even if they are not in the 'stopped' <br>state. Optional, the default value is False. | boolean |
| **ids**<br>_required_ | IDs of the models to publish | < string > array |
| **publish\_tasks**<br>_optional_ | Indicates that the associated tasks (if exist) should be published. Optional, <br>the default value is True. | boolean |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/models/\#responses-14 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/models/#models-publish_many-response-200) |

**Response 200**

| Name | Schema |
| --- | --- |
| **failed**<br>_optional_ | < [failed](https://clear.ml/docs/latest/docs/references/api/models/#models-publish_many-post-failed) \> array |
| **succeeded**<br>_optional_ | < [succeeded](https://clear.ml/docs/latest/docs/references/api/models/#models-publish_many-post-succeeded) \> array |

**failed**

| Name | Description | Schema |
| --- | --- | --- |
| **error**<br>_optional_ | Error info | [error](https://clear.ml/docs/latest/docs/references/api/models/#models-publish_many-post-failed-error) |
| **id**<br>_optional_ | ID of the failed entity | string |

**error**

| Name | Schema |
| --- | --- |
| **codes**<br>_optional_ | < integer > array |
| **data**<br>_optional_ | object |
| **msg**<br>_optional_ | string |

**succeeded**

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_optional_ | ID of the succeeded entity | string |
| **published\_task**<br>_optional_ | Result of publishing of the model's associated task (if exists). Returned only <br>if the task was published successfully as part of the model publishing. | [published\_task](https://clear.ml/docs/latest/docs/references/api/models/#models-publish_many-post-succeeded-published_task) |
| **updated**<br>_optional_ | Indicates whether the model was updated | boolean |

**published\_task**

| Name | Description | Schema |
| --- | --- | --- |
| **data**<br>_optional_ | Data returned from the task publishing operation. | [data](https://clear.ml/docs/latest/docs/references/api/models/#models-publish_many-post-succeeded-published_task-data) |
| **id**<br>_optional_ | Task id | string |

**data**

| Name | Description | Schema |
| --- | --- | --- |
| **fields**<br>_optional_ | Updated fields names and values | object |
| **updated**<br>_optional_ | Number of tasks updated (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/models/\#security-14 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /models.set\_ready [​](https://clear.ml/docs/latest/docs/references/api/models/\#post-modelsset_ready "Direct link to POST /models.set_ready")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/models/\#description-15 "Direct link to Description")

Set the model ready flag to True. If the model is an output model of a task

then try to publish the task.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/models/\#parameters-15 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/models/#models-set_ready-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **force\_publish\_task**<br>_optional_ | Publish the associated task (if exists) even if it is not in the 'stopped' <br>state. Optional, the default value is False. | boolean |
| **model**<br>_required_ | Model id | string |
| **publish\_task**<br>_optional_ | Indicates that the associated task (if exists) should be published. Optional, <br>the default value is True. | boolean |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/models/\#responses-15 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/models/#models-set_ready-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **published\_task**<br>_optional_ | Result of publishing of the model's associated task (if exists). Returned only <br>if the task was published successfully as part of the model publishing. | [published\_task](https://clear.ml/docs/latest/docs/references/api/models/#models-set_ready-post-published_task) |
| **updated**<br>_optional_ | Number of models updated (0 or 1) | integer |

**published\_task**

| Name | Description | Schema |
| --- | --- | --- |
| **data**<br>_optional_ | Data returned from the task publishing operation. | [data](https://clear.ml/docs/latest/docs/references/api/models/#models-set_ready-post-published_task-data) |
| **id**<br>_optional_ | Task id | string |

**data**

| Name | Description | Schema |
| --- | --- | --- |
| **fields**<br>_optional_ | Updated fields names and values | object |
| **updated**<br>_optional_ | Number of tasks updated (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/models/\#security-15 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /models.unarchive\_many [​](https://clear.ml/docs/latest/docs/references/api/models/\#post-modelsunarchive_many "Direct link to POST /models.unarchive_many")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/models/\#description-16 "Direct link to Description")

Unarchive models

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/models/\#parameters-16 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/models/#models-unarchive_many-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **ids**<br>_required_ | IDs of the models to unarchive | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/models/\#responses-16 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/models/#models-unarchive_many-response-200) |

**Response 200**

| Name | Schema |
| --- | --- |
| **failed**<br>_optional_ | < [failed](https://clear.ml/docs/latest/docs/references/api/models/#models-unarchive_many-post-failed) \> array |
| **succeeded**<br>_optional_ | < [succeeded](https://clear.ml/docs/latest/docs/references/api/models/#models-unarchive_many-post-succeeded) \> array |

**failed**

| Name | Description | Schema |
| --- | --- | --- |
| **error**<br>_optional_ | Error info | [error](https://clear.ml/docs/latest/docs/references/api/models/#models-unarchive_many-post-failed-error) |
| **id**<br>_optional_ | ID of the failed entity | string |

**error**

| Name | Schema |
| --- | --- |
| **codes**<br>_optional_ | < integer > array |
| **data**<br>_optional_ | object |
| **msg**<br>_optional_ | string |

**succeeded**

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_optional_ | ID of the succeeded entity | string |
| **unarchived**<br>_optional_ | Indicates whether the model was unarchived | boolean |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/models/\#security-16 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /models.update [​](https://clear.ml/docs/latest/docs/references/api/models/\#post-modelsupdate "Direct link to POST /models.update")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/models/\#description-17 "Direct link to Description")

Update a model

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/models/\#parameters-17 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/models/#models-update-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **comment**<br>_optional_ | Model comment | string |
| **created**<br>_optional_ | Model creation time (UTC) | string (date-time) |
| **iteration**<br>_optional_ | Iteration (used to update task statistics if an associated task is reported) | integer |
| **metadata**<br>_optional_ | Model metadata | < string, [models.metadata\_item](https://clear.ml/docs/latest/docs/references/api/definitions#modelsmetadata_item) \> map |
| **model**<br>_required_ | Model id | string |
| **name**<br>_optional_ | Model name Unique within the company. | string |
| **project**<br>_optional_ | Project to which to model belongs | string |
| **ready**<br>_optional_ | Indication if the model is final and can be used by other tasks Default is <br>false. <br>**Default** : `false` | boolean |
| **system\_tags**<br>_optional_ | System tags list. This field is reserved for system use, please don't use it. | < string > array |
| **tags**<br>_optional_ | User-defined tags list | < string > array |
| **task**<br>_optional_ | Associated task ID | string |
| **ui\_cache**<br>_optional_ | UI cache for this model | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/models/\#responses-17 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/models/#models-update-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **fields**<br>_optional_ | Updated fields names and values | object |
| **updated**<br>_optional_ | Number of models updated (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/models/\#security-17 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /models.update\_for\_task [​](https://clear.ml/docs/latest/docs/references/api/models/\#post-modelsupdate_for_task "Direct link to POST /models.update_for_task")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/models/\#description-18 "Direct link to Description")

Create or update a new model for a task

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/models/\#parameters-18 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/models/#models-update_for_task-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **comment**<br>_optional_ | Model comment | string |
| **iteration**<br>_optional_ | Iteration (used to update task statistics) | integer |
| **name**<br>_optional_ | Model name Unique within the company. | string |
| **override\_model\_id**<br>_optional_ | Override model ID. If provided, this model is updated in the task. Exactly one <br>of override\_model\_id or uri is required. | string |
| **system\_tags**<br>_optional_ | System tags list. This field is reserved for system use, please don't use it. | < string > array |
| **tags**<br>_optional_ | User-defined tags list | < string > array |
| **task**<br>_required_ | Task id | string |
| **uri**<br>_optional_ | URI for the model. Exactly one of uri or override\_model\_id is a required. | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/models/\#responses-18 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/models/#models-update_for_task-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **created**<br>_optional_ | Was the model created | boolean |
| **fields**<br>_optional_ | Updated fields names and values | object |
| **id**<br>_optional_ | ID of the model | string |
| **updated**<br>_optional_ | Number of models updated (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/models/\#security-18 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /models.update\_tags [​](https://clear.ml/docs/latest/docs/references/api/models/\#post-modelsupdate_tags "Direct link to POST /models.update_tags")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/models/\#description-19 "Direct link to Description")

Add or remove tags from multiple models

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/models/\#parameters-19 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/models/#models-update_tags-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **add\_tags**<br>_optional_ | User tags to add | < string > array |
| **ids**<br>_optional_ | IDs of the models to update | < string > array |
| **remove\_tags**<br>_optional_ | User tags to remove | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/models/\#responses-19 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/models/#models-update_tags-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **updated**<br>_optional_ | The number of updated models | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/models/\#security-19 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

- [POST /models.add\_or\_update\_metadata](https://clear.ml/docs/latest/docs/references/api/models/#post-modelsadd_or_update_metadata)
- [POST /models.archive\_many](https://clear.ml/docs/latest/docs/references/api/models/#post-modelsarchive_many)
- [POST /models.create](https://clear.ml/docs/latest/docs/references/api/models/#post-modelscreate)
- [POST /models.delete](https://clear.ml/docs/latest/docs/references/api/models/#post-modelsdelete)
- [POST /models.delete\_many](https://clear.ml/docs/latest/docs/references/api/models/#post-modelsdelete_many)
- [POST /models.delete\_metadata](https://clear.ml/docs/latest/docs/references/api/models/#post-modelsdelete_metadata)
- [POST /models.edit](https://clear.ml/docs/latest/docs/references/api/models/#post-modelsedit)
- [POST /models.get\_all](https://clear.ml/docs/latest/docs/references/api/models/#post-modelsget_all)
- [POST /models.get\_by\_id](https://clear.ml/docs/latest/docs/references/api/models/#post-modelsget_by_id)
- [POST /models.get\_by\_task\_id](https://clear.ml/docs/latest/docs/references/api/models/#post-modelsget_by_task_id)
- [POST /models.get\_frameworks](https://clear.ml/docs/latest/docs/references/api/models/#post-modelsget_frameworks)
- [POST /models.make\_private](https://clear.ml/docs/latest/docs/references/api/models/#post-modelsmake_private)
- [POST /models.make\_public](https://clear.ml/docs/latest/docs/references/api/models/#post-modelsmake_public)
- [POST /models.move](https://clear.ml/docs/latest/docs/references/api/models/#post-modelsmove)
- [POST /models.publish\_many](https://clear.ml/docs/latest/docs/references/api/models/#post-modelspublish_many)
- [POST /models.set\_ready](https://clear.ml/docs/latest/docs/references/api/models/#post-modelsset_ready)
- [POST /models.unarchive\_many](https://clear.ml/docs/latest/docs/references/api/models/#post-modelsunarchive_many)
- [POST /models.update](https://clear.ml/docs/latest/docs/references/api/models/#post-modelsupdate)
- [POST /models.update\_for\_task](https://clear.ml/docs/latest/docs/references/api/models/#post-modelsupdate_for_task)
- [POST /models.update\_tags](https://clear.ml/docs/latest/docs/references/api/models/#post-modelsupdate_tags)