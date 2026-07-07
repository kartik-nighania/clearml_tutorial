---
url: "https://clear.ml/docs/latest/docs/references/enterprise/models/"
title: "models | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/enterprise/models/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

### POST /models.add\_or\_update\_metadata [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#post-modelsadd_or_update_metadata "Direct link to POST /models.add_or_update_metadata")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#description "Direct link to Description")

Add or update model metadata

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#parameters "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-add_or_update_metadata-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **metadata**<br>_required_ | Metadata items to add or update | < [models.metadata\_item](https://clear.ml/docs/latest/docs/references/enterprise/definitions#modelsmetadata_item) \> array |
| **model**<br>_required_ | ID of the model | string |
| **replace\_metadata**<br>_optional_ | If set then the all the metadata items will be replaced with the provided ones. <br>Otherwise only the provided metadata items will be updated or added <br>**Default** : `false` | boolean |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#responses "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-add_or_update_metadata-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **updated**<br>_optional_ | Number of models updated (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#security "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /models.archive\_many [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#post-modelsarchive_many "Direct link to POST /models.archive_many")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#description-1 "Direct link to Description")

Archive models

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#parameters-1 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-archive_many-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **ids**<br>_required_ | IDs of the models to archive | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#responses-1 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-archive_many-response-200) |

**Response 200**

| Name | Schema |
| --- | --- |
| **failed**<br>_optional_ | < [failed](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-archive_many-post-failed) \> array |
| **succeeded**<br>_optional_ | < [succeeded](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-archive_many-post-succeeded) \> array |

**failed**

| Name | Description | Schema |
| --- | --- | --- |
| **error**<br>_optional_ | Error info | [error](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-archive_many-post-failed-error) |
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

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#security-1 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /models.create [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#post-modelscreate "Direct link to POST /models.create")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#description-2 "Direct link to Description")

Create a new model not associated with a task

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#parameters-2 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-create-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **comment**<br>_optional_ | Model comment | string |
| **design**<br>_optional_ | Json\[d\] object representing the model design. Should be identical to the <br>network design of the task which created the model | object |
| **framework**<br>_optional_ | Framework on which the model is based. Case insensitive. Should be identical to <br>the framework of the task which created the model. | string |
| **labels**<br>_optional_ | Json object | < string, integer > map |
| **metadata**<br>_optional_ | Model metadata | < string, [models.metadata\_item](https://clear.ml/docs/latest/docs/references/enterprise/definitions#modelsmetadata_item) \> map |
| **name**<br>_required_ | Model name Unique within the company. | string |
| **parent**<br>_optional_ | Parent model | string |
| **project**<br>_optional_ | Project to which to model belongs | string |
| **public**<br>_optional_ | Create a public model Default is false. <br>**Default** : `false` | boolean |
| **ready**<br>_optional_ | Indication if the model is final and can be used by other tasks. Default is <br>false. <br>**Default** : `false` | boolean |
| **system\_tags**<br>_optional_ | System tags list. This field is reserved for system use, please don't use it. | < string > array |
| **tags**<br>_optional_ | User-defined tags list | < string > array |
| **task**<br>_optional_ | Associated task ID | string |
| **uri**<br>_required_ | URI for the model | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#responses-2 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-create-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **created**<br>_optional_ | Was the model created | boolean |
| **id**<br>_optional_ | ID of the model | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#security-2 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /models.delete [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#post-modelsdelete "Direct link to POST /models.delete")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#description-3 "Direct link to Description")

Delete a model.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#parameters-3 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-delete-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **force**<br>_optional_ | Force. Required if there are tasks that use the model as an execution model, or <br>if the model's creating task is published. | boolean |
| **model**<br>_required_ | Model ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#responses-3 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-delete-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **deleted**<br>_optional_ | Indicates whether the model was deleted | boolean |
| **url**<br>_optional_ | The url of the model file | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#security-3 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /models.delete\_many [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#post-modelsdelete_many "Direct link to POST /models.delete_many")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#description-4 "Direct link to Description")

Delete models

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#parameters-4 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-delete_many-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **force**<br>_optional_ | Force. Required if there are tasks that use the model as an execution model, or <br>if the model's creating task is published. | boolean |
| **ids**<br>_required_ | IDs of the models to delete | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#responses-4 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-delete_many-response-200) |

**Response 200**

| Name | Schema |
| --- | --- |
| **failed**<br>_optional_ | < [failed](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-delete_many-post-failed) \> array |
| **succeeded**<br>_optional_ | < [succeeded](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-delete_many-post-succeeded) \> array |

**failed**

| Name | Description | Schema |
| --- | --- | --- |
| **error**<br>_optional_ | Error info | [error](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-delete_many-post-failed-error) |
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

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#security-4 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /models.delete\_metadata [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#post-modelsdelete_metadata "Direct link to POST /models.delete_metadata")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#description-5 "Direct link to Description")

Delete metadata from model

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#parameters-5 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-delete_metadata-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **keys**<br>_required_ | The list of metadata keys to delete | < string > array |
| **model**<br>_required_ | ID of the model | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#responses-5 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-delete_metadata-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **updated**<br>_optional_ | Number of models updated (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#security-5 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /models.edit [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#post-modelsedit "Direct link to POST /models.edit")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#description-6 "Direct link to Description")

Edit an existing model

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#parameters-6 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-edit-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **comment**<br>_optional_ | Model comment | string |
| **design**<br>_optional_ | Json\[d\] object representing the model design. Should be identical to the <br>network design of the task which created the model | object |
| **framework**<br>_optional_ | Framework on which the model is based. Case insensitive. Should be identical to <br>the framework of the task which created the model. | string |
| **iteration**<br>_optional_ | Iteration (used to update task statistics) | integer |
| **labels**<br>_optional_ | Json object | < string, integer > map |
| **metadata**<br>_optional_ | Model metadata | < string, [models.metadata\_item](https://clear.ml/docs/latest/docs/references/enterprise/definitions#modelsmetadata_item) \> map |
| **model**<br>_required_ | Model ID | string |
| **name**<br>_optional_ | Model name Unique within the company. | string |
| **parent**<br>_optional_ | Parent model | string |
| **project**<br>_optional_ | Project to which to model belongs | string |
| **ready**<br>_optional_ | Indication if the model is final and can be used by other tasks | boolean |
| **system\_tags**<br>_optional_ | System tags list. This field is reserved for system use, please don't use it. | < string > array |
| **tags**<br>_optional_ | User-defined tags list | < string > array |
| **task**<br>_optional_ | Associated task ID | string |
| **uri**<br>_optional_ | URI for the model | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#responses-6 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-edit-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **fields**<br>_optional_ | Updated fields names and values | object |
| **updated**<br>_optional_ | Number of models updated (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#security-6 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /models.get\_all [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#post-modelsget_all "Direct link to POST /models.get_all")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#description-7 "Direct link to Description")

Get all models

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#parameters-7 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-get_all-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **_all_**<br>_optional_ | Multi-field pattern condition (all fields match pattern) | [models.multi\_field\_pattern\_data](https://clear.ml/docs/latest/docs/references/enterprise/definitions#modelsmulti_field_pattern_data) |
| **_any_**<br>_optional_ | Multi-field pattern condition (any field matches pattern) | [models.multi\_field\_pattern\_data](https://clear.ml/docs/latest/docs/references/enterprise/definitions#modelsmulti_field_pattern_data) |
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

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#responses-7 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-get_all-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **models**<br>_optional_ | Models list | < [models.model](https://clear.ml/docs/latest/docs/references/enterprise/definitions#modelsmodel) \> array |
| **scroll\_id**<br>_optional_ | Scroll ID that can be used with the next calls to get\_all to retrieve more data | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#security-7 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /models.get\_all\_ex [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#post-modelsget_all_ex "Direct link to POST /models.get_all_ex")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#description-8 "Direct link to Description")

Internal. Get all models

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#parameters-8 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-get_all_ex-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **_all_**<br>_optional_ | Multi-field pattern condition (all fields match pattern) | [models.multi\_field\_pattern\_data](https://clear.ml/docs/latest/docs/references/enterprise/definitions#modelsmulti_field_pattern_data) |
| **_any_**<br>_optional_ | Multi-field pattern condition (any field matches pattern) | [models.multi\_field\_pattern\_data](https://clear.ml/docs/latest/docs/references/enterprise/definitions#modelsmulti_field_pattern_data) |
| **allow\_public**<br>_optional_ | Allow public models to be returned in the results <br>**Default** : `true` | boolean |
| **filters**<br>_optional_ | List of FilterRule ('OR' connection) | < string, [filters](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-get_all_ex-post-filters) \> map |
| **framework**<br>_optional_ | List of frameworks | < string > array |
| **id**<br>_optional_ | List of model IDs | < string > array |
| **include\_stats**<br>_optional_ | If true, include models statistic in response <br>**Default** : `false` | boolean |
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
| **scroll\_id**<br>_optional_ | Scroll ID returned from the previos calls to get\_all\_ex | string |
| **search\_text**<br>_optional_ | Free text search query | string |
| **size**<br>_optional_ | The number of models to retrieve <br>**Minimum value** : `1` | integer |
| **system\_tags**<br>_optional_ | System tags list used to filter results. Prepend '-' to system tag name to <br>indicate exclusion | < string > array |
| **tags**<br>_optional_ | User-defined tags list used to filter results. Prepend '-' to tag name to <br>indicate exclusion | < string > array |
| **task**<br>_optional_ | List of associated task IDs | < string > array |
| **uri**<br>_optional_ | List of model URIs | < string > array |
| **user**<br>_optional_ | List of user IDs used to filter results by the model's creating user | < string > array |

**filters**

| Name | Description | Schema |
| --- | --- | --- |
| **all**<br>_optional_ | All the terms in 'all' condition are combined with 'and' operation | [all](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-get_all_ex-post-filters-all) |
| **any**<br>_optional_ | All the terms in 'any' condition are combined with 'or' operation | [any](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-get_all_ex-post-filters-any) |
| **op**<br>_optional_ | The operation between 'any' and 'all' parts of the filter if both are provided <br>**Default** : `"and"` | enum (and, or) |

**all**

| Name | Schema |
| --- | --- |
| **exclude**<br>_optional_ | < string > array |
| **include**<br>_optional_ | < string > array |

**any**

| Name | Schema |
| --- | --- |
| **exclude**<br>_optional_ | < string > array |
| **include**<br>_optional_ | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#responses-8 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-get_all_ex-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **models**<br>_optional_ | Models list | < [models.model](https://clear.ml/docs/latest/docs/references/enterprise/definitions#modelsmodel) \> array |
| **scroll\_id**<br>_optional_ | Scroll ID that can be used with the next calls to get\_all\_ex to retrieve more <br>data | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#security-8 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /models.get\_by\_id [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#post-modelsget_by_id "Direct link to POST /models.get_by_id")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#description-9 "Direct link to Description")

Gets model information

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#parameters-9 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-get_by_id-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **model**<br>_required_ | Model id | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#responses-9 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-get_by_id-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **model**<br>_optional_ | Model info | [models.model](https://clear.ml/docs/latest/docs/references/enterprise/definitions#modelsmodel) |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#security-9 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /models.get\_by\_id\_ex [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#post-modelsget_by_id_ex "Direct link to POST /models.get_by_id_ex")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#description-10 "Direct link to Description")

Internal. Get all models

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#parameters-10 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-get_by_id_ex-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **_all_**<br>_optional_ | Multi-field pattern condition (all fields match pattern) | [models.multi\_field\_pattern\_data](https://clear.ml/docs/latest/docs/references/enterprise/definitions#modelsmulti_field_pattern_data) |
| **_any_**<br>_optional_ | Multi-field pattern condition (any field matches pattern) | [models.multi\_field\_pattern\_data](https://clear.ml/docs/latest/docs/references/enterprise/definitions#modelsmulti_field_pattern_data) |
| **framework**<br>_optional_ | List of frameworks | < string > array |
| **id**<br>_optional_ | List of model IDs | < string > array |
| **last\_update**<br>_optional_ | List of last\_update constraint strings (utcformat, epoch) with an optional <br>prefix modifier (>, >=, <, <=) | < string > array |
| **name**<br>_optional_ | Get only models whose name matches this pattern (python regular expression <br>syntax) | string |
| **only\_fields**<br>_optional_ | List of model field names (if applicable, nesting is supported using '.'). If <br>provided, this list defines the query's projection (only these fields will be <br>returned for each result entry) | < string > array |
| **order\_by**<br>_optional_ | List of field names to order by. When search\_text is used, '@text\_score' can be <br>used as a field representing the text score of returned documents. Use '-' <br>prefix to specify descending order. Optional, recommended when using page | < string > array |
| **page**<br>_optional_ | Page number, returns a specific page out of the resulting list of models <br>**Minimum value** : `0` | integer |
| **page\_size**<br>_optional_ | Page size, specifies the number of results returned in each page (last page may <br>contain fewer results) <br>**Minimum value** : `1` | integer |
| **project**<br>_optional_ | List of associated project IDs | < string > array |
| **ready**<br>_optional_ | Indication whether to retrieve only models that are marked ready If not <br>supplied returns both ready and not-ready projects. | boolean |
| **search\_text**<br>_optional_ | Free text search query | string |
| **system\_tags**<br>_optional_ | System tags list used to filter results. Prepend '-' to system tag name to <br>indicate exclusion | < string > array |
| **tags**<br>_optional_ | User-defined tags list used to filter results. Prepend '-' to tag name to <br>indicate exclusion | < string > array |
| **task**<br>_optional_ | List of associated task IDs | < string > array |
| **uri**<br>_optional_ | List of model URIs | < string > array |
| **user**<br>_optional_ | List of user IDs used to filter results by the model's creating user | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#responses-10 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-get_by_id_ex-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **models**<br>_optional_ | Models list | < [models.model](https://clear.ml/docs/latest/docs/references/enterprise/definitions#modelsmodel) \> array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#security-10 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /models.get\_by\_task\_id [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#post-modelsget_by_task_id "Direct link to POST /models.get_by_task_id")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#description-11 "Direct link to Description")

Gets model information

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#parameters-11 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-get_by_task_id-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **task**<br>_optional_ | Task id | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#responses-11 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-get_by_task_id-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **model**<br>_optional_ | Model info | [models.model](https://clear.ml/docs/latest/docs/references/enterprise/definitions#modelsmodel) |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#security-11 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /models.get\_frameworks [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#post-modelsget_frameworks "Direct link to POST /models.get_frameworks")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#description-12 "Direct link to Description")

Get the list of frameworks used in the company models

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#parameters-12 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-get_frameworks-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **projects**<br>_optional_ | The list of projects which models will be analyzed. If not passed or empty then <br>all the company and public models will be analyzed | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#responses-12 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-get_frameworks-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **frameworks**<br>_optional_ | Unique list of the frameworks used in the company models | < string > array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#security-12 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /models.move [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#post-modelsmove "Direct link to POST /models.move")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#description-13 "Direct link to Description")

Move models to a project

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#parameters-13 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-move-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **ids**<br>_required_ | Models to move | < string > array |
| **project**<br>_optional_ | Target project ID. If not provided, `project_name` must be provided. Use null <br>for the root project | string |
| **project\_name**<br>_optional_ | Target project name. If provided and a project with this name does not exist, a <br>new project will be created. If not provided, `project` must be provided. | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#responses-13 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#security-13 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /models.publish\_many [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#post-modelspublish_many "Direct link to POST /models.publish_many")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#description-14 "Direct link to Description")

Publish models

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#parameters-14 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-publish_many-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **force\_publish\_task**<br>_optional_ | Publish the associated tasks (if exist) even if they are not in the 'stopped' <br>state. Optional, the default value is False. | boolean |
| **ids**<br>_required_ | IDs of the models to publish | < string > array |
| **publish\_tasks**<br>_optional_ | Indicates that the associated tasks (if exist) should be published. Optional, <br>the default value is True. | boolean |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#responses-14 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-publish_many-response-200) |

**Response 200**

| Name | Schema |
| --- | --- |
| **failed**<br>_optional_ | < [failed](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-publish_many-post-failed) \> array |
| **succeeded**<br>_optional_ | < [succeeded](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-publish_many-post-succeeded) \> array |

**failed**

| Name | Description | Schema |
| --- | --- | --- |
| **error**<br>_optional_ | Error info | [error](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-publish_many-post-failed-error) |
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
| **published\_task**<br>_optional_ | Result of publishing of the model's associated task (if exists). Returned only <br>if the task was published successfully as part of the model publishing. | [published\_task](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-publish_many-post-succeeded-published_task) |
| **updated**<br>_optional_ | Indicates whether the model was updated | boolean |

**published\_task**

| Name | Description | Schema |
| --- | --- | --- |
| **data**<br>_optional_ | Data returned from the task publishing operation. | [data](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-publish_many-post-succeeded-published_task-data) |
| **id**<br>_optional_ | Task id | string |

**data**

| Name | Description | Schema |
| --- | --- | --- |
| **committed\_versions\_results**<br>_optional_ | Committed versions results | < object > array |
| **fields**<br>_optional_ | Updated fields names and values | object |
| **updated**<br>_optional_ | Number of tasks updated (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#security-14 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /models.set\_ready [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#post-modelsset_ready "Direct link to POST /models.set_ready")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#description-15 "Direct link to Description")

Set the model ready flag to True. If the model is an output model of a task

then try to publish the task.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#parameters-15 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-set_ready-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **force\_publish\_task**<br>_optional_ | Publish the associated task (if exists) even if it is not in the 'stopped' <br>state. Optional, the default value is False. | boolean |
| **model**<br>_required_ | Model id | string |
| **publish\_task**<br>_optional_ | Indicates that the associated task (if exists) should be published. Optional, <br>the default value is True. | boolean |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#responses-15 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-set_ready-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **published\_task**<br>_optional_ | Result of publishing of the model's associated task (if exists). Returned only <br>if the task was published successfully as part of the model publishing. | [published\_task](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-set_ready-post-published_task) |
| **updated**<br>_optional_ | Number of models updated (0 or 1) | integer |

**published\_task**

| Name | Description | Schema |
| --- | --- | --- |
| **data**<br>_optional_ | Data returned from the task publishing operation. | [data](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-set_ready-post-published_task-data) |
| **id**<br>_optional_ | Task id | string |

**data**

| Name | Description | Schema |
| --- | --- | --- |
| **committed\_versions\_results**<br>_optional_ | Committed versions results | < object > array |
| **fields**<br>_optional_ | Updated fields names and values | object |
| **updated**<br>_optional_ | Number of tasks updated (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#security-15 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /models.unarchive\_many [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#post-modelsunarchive_many "Direct link to POST /models.unarchive_many")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#description-16 "Direct link to Description")

Unarchive models

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#parameters-16 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-unarchive_many-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **ids**<br>_required_ | IDs of the models to unarchive | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#responses-16 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-unarchive_many-response-200) |

**Response 200**

| Name | Schema |
| --- | --- |
| **failed**<br>_optional_ | < [failed](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-unarchive_many-post-failed) \> array |
| **succeeded**<br>_optional_ | < [succeeded](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-unarchive_many-post-succeeded) \> array |

**failed**

| Name | Description | Schema |
| --- | --- | --- |
| **error**<br>_optional_ | Error info | [error](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-unarchive_many-post-failed-error) |
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

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#security-16 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /models.update [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#post-modelsupdate "Direct link to POST /models.update")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#description-17 "Direct link to Description")

Update a model

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#parameters-17 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-update-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **comment**<br>_optional_ | Model comment | string |
| **created**<br>_optional_ | Model creation time (UTC) | string (date-time) |
| **iteration**<br>_optional_ | Iteration (used to update task statistics if an associated task is reported) | integer |
| **metadata**<br>_optional_ | Model metadata | < string, [models.metadata\_item](https://clear.ml/docs/latest/docs/references/enterprise/definitions#modelsmetadata_item) \> map |
| **model**<br>_required_ | Model id | string |
| **name**<br>_optional_ | Model name Unique within the company. | string |
| **project**<br>_optional_ | Project to which to model belongs | string |
| **ready**<br>_optional_ | Indication if the model is final and can be used by other tasks Default is <br>false. <br>**Default** : `false` | boolean |
| **system\_tags**<br>_optional_ | System tags list. This field is reserved for system use, please don't use it. | < string > array |
| **tags**<br>_optional_ | User-defined tags list | < string > array |
| **task**<br>_optional_ | Associated task ID | string |
| **ui\_cache**<br>_optional_ | UI cache for this model | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#responses-17 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-update-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **fields**<br>_optional_ | Updated fields names and values | object |
| **updated**<br>_optional_ | Number of models updated (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#security-17 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /models.update\_for\_task [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#post-modelsupdate_for_task "Direct link to POST /models.update_for_task")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#description-18 "Direct link to Description")

Create or update a new model for a task

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#parameters-18 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-update_for_task-request) |

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

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#responses-18 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-update_for_task-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **created**<br>_optional_ | Was the model created | boolean |
| **fields**<br>_optional_ | Updated fields names and values | object |
| **id**<br>_optional_ | ID of the model | string |
| **updated**<br>_optional_ | Number of models updated (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#security-18 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /models.update\_tags [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#post-modelsupdate_tags "Direct link to POST /models.update_tags")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#description-19 "Direct link to Description")

Add or remove tags from multiple models

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#parameters-19 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-update_tags-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **add\_tags**<br>_optional_ | User tags to add | < string > array |
| **ids**<br>_optional_ | IDs of the models to update | < string > array |
| **remove\_tags**<br>_optional_ | User tags to remove | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#responses-19 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/models/#models-update_tags-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **updated**<br>_optional_ | The number of updated models | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/models/\#security-19 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

- [POST /models.add\_or\_update\_metadata](https://clear.ml/docs/latest/docs/references/enterprise/models/#post-modelsadd_or_update_metadata)
- [POST /models.archive\_many](https://clear.ml/docs/latest/docs/references/enterprise/models/#post-modelsarchive_many)
- [POST /models.create](https://clear.ml/docs/latest/docs/references/enterprise/models/#post-modelscreate)
- [POST /models.delete](https://clear.ml/docs/latest/docs/references/enterprise/models/#post-modelsdelete)
- [POST /models.delete\_many](https://clear.ml/docs/latest/docs/references/enterprise/models/#post-modelsdelete_many)
- [POST /models.delete\_metadata](https://clear.ml/docs/latest/docs/references/enterprise/models/#post-modelsdelete_metadata)
- [POST /models.edit](https://clear.ml/docs/latest/docs/references/enterprise/models/#post-modelsedit)
- [POST /models.get\_all](https://clear.ml/docs/latest/docs/references/enterprise/models/#post-modelsget_all)
- [POST /models.get\_all\_ex](https://clear.ml/docs/latest/docs/references/enterprise/models/#post-modelsget_all_ex)
- [POST /models.get\_by\_id](https://clear.ml/docs/latest/docs/references/enterprise/models/#post-modelsget_by_id)
- [POST /models.get\_by\_id\_ex](https://clear.ml/docs/latest/docs/references/enterprise/models/#post-modelsget_by_id_ex)
- [POST /models.get\_by\_task\_id](https://clear.ml/docs/latest/docs/references/enterprise/models/#post-modelsget_by_task_id)
- [POST /models.get\_frameworks](https://clear.ml/docs/latest/docs/references/enterprise/models/#post-modelsget_frameworks)
- [POST /models.move](https://clear.ml/docs/latest/docs/references/enterprise/models/#post-modelsmove)
- [POST /models.publish\_many](https://clear.ml/docs/latest/docs/references/enterprise/models/#post-modelspublish_many)
- [POST /models.set\_ready](https://clear.ml/docs/latest/docs/references/enterprise/models/#post-modelsset_ready)
- [POST /models.unarchive\_many](https://clear.ml/docs/latest/docs/references/enterprise/models/#post-modelsunarchive_many)
- [POST /models.update](https://clear.ml/docs/latest/docs/references/enterprise/models/#post-modelsupdate)
- [POST /models.update\_for\_task](https://clear.ml/docs/latest/docs/references/enterprise/models/#post-modelsupdate_for_task)
- [POST /models.update\_tags](https://clear.ml/docs/latest/docs/references/enterprise/models/#post-modelsupdate_tags)