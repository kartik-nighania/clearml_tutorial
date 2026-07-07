---
url: "https://clear.ml/docs/latest/docs/references/enterprise/datasets/"
title: "datasets | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

info

This page covers the **Hyper-Dataset** API, ClearML's advanced queryable dataset management solution.

### POST /datasets.commit\_version [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#post-datasetscommit_version "Direct link to POST /datasets.commit_version")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#description "Direct link to Description")

Commit changes to a draft version.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#parameters "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-commit_version-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **calculate\_stats**<br>_optional_ | If set to false then the version statistics will not be calculated on commit <br>(only when version publish not requested). The default is true <br>**Default** : `true` | boolean |
| **force**<br>_optional_ | If publish=true, ignore ongoing annotation tasks with this version as input <br>**Default** : `false` | boolean |
| **override\_stats**<br>_optional_ | Override version statistics (when provided, these will be used instead of <br>computed statistics) | [datasets.statistics](https://clear.ml/docs/latest/docs/references/enterprise/definitions#datasetsstatistics) |
| **publish**<br>_optional_ | If set to true, version will also be published. <br>**Default** : `false` | boolean |
| **publishing\_task**<br>_optional_ | ID of an in-progress annotation task calling this endpoint. Versions which are <br>used as input of in-progress annotation tasks can only be published if there is <br>only one such task and its ID is sent in this field. This is required if one <br>exists. | string |
| **version**<br>_required_ | Draft version ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#responses "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-commit_version-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **dataset**<br>_optional_ | Dataset ID | string |
| **deleted**<br>_optional_ | Number of deleted frames | integer |
| **errors**<br>_optional_ | Failure details | < object > array |
| **failed**<br>_optional_ | Number of failures | integer |
| **merged**<br>_optional_ | Number of merged frames | integer |
| **parent**<br>_optional_ | Committed version parent version ID | string |
| **saved\_and\_updated**<br>_optional_ | Number of saved and updated frames | integer |
| **total**<br>_optional_ | Total number of processed frames | integer |
| **version**<br>_optional_ | Committed version ID | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#security "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /datasets.create [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#post-datasetscreate "Direct link to POST /datasets.create")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#description-1 "Direct link to Description")

Creates a new dataset with an initial (empty) version

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#parameters-1 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-create-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **comment**<br>_optional_ | Dataset comment | string |
| **field\_mappings**<br>_optional_ | field mappings | < string, object > map |
| **metadata**<br>_optional_ | User-specified metadata object. Keys must not include '$' and '.'. | object |
| **name**<br>_required_ | Dataset name. Unique within the company. | string |
| **project**<br>_optional_ | Project to which to dataset belongs | string |
| **public**<br>_optional_ | Create a public dataset Limited to 'root' users. | boolean |
| **system\_tags**<br>_optional_ | System tags list. This field is reserved for system use, please don't use it. | < string > array |
| **tags**<br>_optional_ | User-defined tags list | < string > array |
| **terms\_of\_use**<br>_optional_ | Terms of use string | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#responses-1 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-create-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_optional_ | ID of the dataset | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#security-1 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /datasets.create\_version [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#post-datasetscreate_version "Direct link to POST /datasets.create_version")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#description-2 "Direct link to Description")

Creates a new dataset version

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#parameters-2 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-create_version-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **comment**<br>_optional_ | Version comment | string |
| **dataset**<br>_required_ | Dataset ID | string |
| **metadata**<br>_optional_ | User-specified metadata object. Keys must not include '$' and '.'. | object |
| **name**<br>_required_ | Version name Unique | string |
| **parent**<br>_optional_ | Version parent ID | string |
| **stats**<br>_optional_ | Version statistics | [datasets.statistics](https://clear.ml/docs/latest/docs/references/enterprise/definitions#datasetsstatistics) |
| **system\_tags**<br>_optional_ | System tags list. This field is reserved for system use, please don't use it. | < string > array |
| **tags**<br>_optional_ | User-defined tags list | < string > array |
| **task**<br>_optional_ | ID of the task creating the version | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#responses-2 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-create_version-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_optional_ | ID of the version | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#security-2 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /datasets.delete [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#post-datasetsdelete "Direct link to POST /datasets.delete")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#description-3 "Direct link to Description")

Delete a dataset

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#parameters-3 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-delete-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **dataset**<br>_required_ | Dataset ID | string |
| **delete\_all\_versions**<br>_optional_ |  | boolean |
| **force**<br>_optional_ |  | boolean |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#responses-3 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-delete-response-200) |

**Response 200**

| Name | Schema |
| --- | --- |
| **deleted**<br>_optional_ | boolean |
| **deleted\_versions**<br>_optional_ | < string > array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#security-3 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /datasets.delete\_frames [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#post-datasetsdelete_frames "Direct link to POST /datasets.delete_frames")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#description-4 "Direct link to Description")

Delete frames in a draft version.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#parameters-4 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-delete_frames-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **force**<br>_optional_ | Ignore ongoing annotation tasks with this version as input <br>**Default** : `false` | boolean |
| **frames**<br>_required_ | Frame IDs to delete | < string > array |
| **version**<br>_required_ | Draft version ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#responses-4 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-delete_frames-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **deleted**<br>_optional_ | Number of frames deleted | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#security-4 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /datasets.delete\_version [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#post-datasetsdelete_version "Direct link to POST /datasets.delete_version")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#description-5 "Direct link to Description")

Delete a version of a dataset

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#parameters-5 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-delete_version-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **delete\_children**<br>_optional_ | If set to 'true' then deleting the version will delete all its children <br>**Default** : `false` | boolean |
| **force**<br>_optional_ | If set to 'true' then dataset version can be deleted even if it is published or <br>referenced from tasks <br>**Default** : `false` | boolean |
| **version**<br>_required_ | Dataset version ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#responses-5 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-delete_version-response-200) |

**Response 200**

| Name | Schema |
| --- | --- |
| **deleted**<br>_optional_ | boolean |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#security-5 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /datasets.get\_all [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#post-datasetsget_all "Direct link to POST /datasets.get_all")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#description-6 "Direct link to Description")

Gets a list of datasets information matching a query

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#parameters-6 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-get_all-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **_all_**<br>_optional_ | Multi-field pattern condition (all fields match pattern) | [datasets.multi\_field\_pattern\_data](https://clear.ml/docs/latest/docs/references/enterprise/definitions#datasetsmulti_field_pattern_data) |
| **_any_**<br>_optional_ | Multi-field pattern condition (any field matches pattern) | [datasets.multi\_field\_pattern\_data](https://clear.ml/docs/latest/docs/references/enterprise/definitions#datasetsmulti_field_pattern_data) |
| **allow\_public**<br>_optional_ | Allow public datasets to be returned in the results <br>**Default** : `true` | boolean |
| **id**<br>_optional_ | List of IDs to filter by | < string > array |
| **include\_subprojects**<br>_optional_ | If set to 'true' and project field is set then datasets from the subprojects <br>are searched too <br>**Default** : `false` | boolean |
| **name**<br>_optional_ | Get only datasets whose name matches this pattern (python regular expression <br>syntax) | string |
| **only\_fields**<br>_optional_ | List of document's field names (nesting is supported using '.', e.g. <br>execution.model\_labels). If provided, this list defines the query's projection <br>(only these fields will be returned for each result entry) | < string > array |
| **order\_by**<br>_optional_ | List of field names to order by. When search\_text is used, '@text\_score' can be <br>used as a field representing the text score of returned documents. Use '-' <br>prefix to specify descending order. Optional, recommended when using page | < string > array |
| **page**<br>_optional_ | Page number, returns a specific page out of the result list of datasets. <br>**Minimum value** : `0` | integer |
| **page\_size**<br>_optional_ | Page size, specifies the number of results returned in each page (last page may <br>contain fewer results) <br>**Minimum value** : `1` | integer |
| **refresh\_scroll**<br>_optional_ | If set then all the data received with this scroll will be requeried | boolean |
| **resolve\_head**<br>_optional_ | If set then dataset paradigm and head version are calculated and returned. <br>Note: do not use it with queries that are supposed to return multiple datasets. <br>**Default** : `false` | boolean |
| **scroll\_id**<br>_optional_ | Scroll ID returned from the previos calls to get\_all | string |
| **search\_text**<br>_optional_ | Free text search query | string |
| **size**<br>_optional_ | The number of datasets to retrieve <br>**Minimum value** : `1` | integer |
| **system\_tags**<br>_optional_ | System tags filter. Use '-' for exclusion (e.g. \['-archived'\] for all non- <br>hidden datasets) | < string > array |
| **tags**<br>_optional_ | User-defined tags filter. Use '-' for exclusion | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#responses-6 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-get_all-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **datasets**<br>_optional_ | List of datasets | < [datasets.dataset](https://clear.ml/docs/latest/docs/references/enterprise/definitions#datasetsdataset) \> array |
| **scroll\_id**<br>_optional_ | Scroll ID that can be used with the next calls to get\_all to retrieve more data | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#security-6 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /datasets.get\_all\_ex [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#post-datasetsget_all_ex "Direct link to POST /datasets.get_all_ex")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#description-7 "Direct link to Description")

Internal. Gets a list of datasets information matching a query

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#parameters-7 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-get_all_ex-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **_all_**<br>_optional_ | Multi-field pattern condition (all fields match pattern) | [datasets.multi\_field\_pattern\_data](https://clear.ml/docs/latest/docs/references/enterprise/definitions#datasetsmulti_field_pattern_data) |
| **_any_**<br>_optional_ | Multi-field pattern condition (any field matches pattern) | [datasets.multi\_field\_pattern\_data](https://clear.ml/docs/latest/docs/references/enterprise/definitions#datasetsmulti_field_pattern_data) |
| **allow\_public**<br>_optional_ | Allow public datasets to be returned in the results <br>**Default** : `true` | boolean |
| **filters**<br>_optional_ | List of FilterRule ('OR' connection) | < string, [filters](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-get_all_ex-post-filters) \> map |
| **id**<br>_optional_ | List of IDs to filter by | < string > array |
| **include\_subprojects**<br>_optional_ | If set to 'true' and project field is set then datasets from the subprojects <br>are searched too <br>**Default** : `false` | boolean |
| **name**<br>_optional_ | Get only datasets whose name matches this pattern (python regular expression <br>syntax) | string |
| **only\_fields**<br>_optional_ | List of document's field names (nesting is supported using '.', e.g. <br>execution.model\_labels). If provided, this list defines the query's projection <br>(only these fields will be returned for each result entry) | < string > array |
| **order\_by**<br>_optional_ | List of field names to order by. When search\_text is used, '@text\_score' can be <br>used as a field representing the text score of returned documents. Use '-' <br>prefix to specify descending order. Optional, recommended when using page | < string > array |
| **page**<br>_optional_ | Page number, returns a specific page out of the result list of datasets. <br>**Minimum value** : `0` | integer |
| **page\_size**<br>_optional_ | Page size, specifies the number of results returned in each page (last page may <br>contain fewer results) <br>**Minimum value** : `1` | integer |
| **refresh\_scroll**<br>_optional_ | If set then all the data received with this scroll will be requeried | boolean |
| **resolve\_head**<br>_optional_ | If set then dataset paradigm and head version are calculated and returned. <br>Note: do not use it with queries that are supposed to return multiple datasets. <br>**Default** : `false` | boolean |
| **scroll\_id**<br>_optional_ | Scroll ID returned from the previos calls to get\_all\_ex | string |
| **search\_text**<br>_optional_ | Free text search query | string |
| **size**<br>_optional_ | The number of datasets to retrieve <br>**Minimum value** : `1` | integer |
| **system\_tags**<br>_optional_ | System tags filter. Use '-' for exclusion (e.g. \['-archived'\] for all non- <br>hidden datasets) | < string > array |
| **tags**<br>_optional_ | User-defined tags filter. Use '-' for exclusion | < string > array |

**filters**

| Name | Description | Schema |
| --- | --- | --- |
| **all**<br>_optional_ | All the terms in 'all' condition are combined with 'and' operation | [all](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-get_all_ex-post-filters-all) |
| **any**<br>_optional_ | All the terms in 'any' condition are combined with 'or' operation | [any](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-get_all_ex-post-filters-any) |
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

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#responses-7 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-get_all_ex-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **datasets**<br>_optional_ | List of datasets | < [datasets.dataset](https://clear.ml/docs/latest/docs/references/enterprise/definitions#datasetsdataset) \> array |
| **scroll\_id**<br>_optional_ | Scroll ID that can be used with the next calls to get\_all\_ex to retrieve more <br>data | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#security-7 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /datasets.get\_by\_id [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#post-datasetsget_by_id "Direct link to POST /datasets.get_by_id")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#description-8 "Direct link to Description")

Gets dataset information

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#parameters-8 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-get_by_id-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **dataset**<br>_required_ | Dataset ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#responses-8 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-get_by_id-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **dataset**<br>_optional_ | Dataset info | [datasets.dataset](https://clear.ml/docs/latest/docs/references/enterprise/definitions#datasetsdataset) |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#security-8 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /datasets.get\_by\_name [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#post-datasetsget_by_name "Direct link to POST /datasets.get_by_name")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#description-9 "Direct link to Description")

Gets dataset information by dataset name

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#parameters-9 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-get_by_name-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **dataset**<br>_required_ | Dataset name | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#responses-9 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-get_by_name-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **dataset**<br>_optional_ | Dataset info | [datasets.dataset](https://clear.ml/docs/latest/docs/references/enterprise/definitions#datasetsdataset) |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#security-9 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /datasets.get\_label\_keywords\_for\_running\_task [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#post-datasetsget_label_keywords_for_running_task "Direct link to POST /datasets.get_label_keywords_for_running_task")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#description-10 "Direct link to Description")

Get the joined list of labels for all the datasets' versions in a task. Note

that the latest committed labels are returned even if task was not completed.

Fails if the task status is Not Started.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#parameters-10 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-get_label_keywords_for_running_task-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **task**<br>_required_ | Task ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#responses-10 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-get_label_keywords_for_running_task-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **labels**<br>_optional_ | List of objects with properties: name - string - label name count - integer - <br>number of occurences | < [labels](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-get_label_keywords_for_running_task-post-labels) \> array |

**labels**

| Name | Schema |
| --- | --- |
| **count**<br>_optional_ | integer |
| **name**<br>_optional_ | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#security-10 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /datasets.get\_schema [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#post-datasetsget_schema "Direct link to POST /datasets.get_schema")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#description-11 "Direct link to Description")

Get the aggregated fields schema for the provided set of dataset versions. The

returned schema represents the various fields that can be used to query these

versions in a Lucene query. In case of conflicting schema types between

versions, conflicting items will not be returned.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#parameters-11 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-get_schema-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **dataset**<br>_optional_ | The ID of the dataset. Either dataset or versions should be specified | string |
| **schema\_type**<br>_optional_ | Type of the schema to return (defaults to frame). <br>\- "frame" - all the fields for query at frame level will be returned <br>\- "roi" - all the fields for query at frame.rois level will be returned <br>\- "sources" - all the fields for query at frame.sources level will be returned | [datasets.schema\_type\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions#datasetsschema_type_enum) |
| **versions**<br>_required_ | Dataset version ids. The resulting schema is a merge of the common fields from <br>all the specified versions. | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#responses-11 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-get_schema-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **schema**<br>_optional_ | Fields schema dictionary. Contains all the fields (and their types) for <br>particular schema type that can be used to query the supplied versions in a <br>Lucene query. | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#security-11 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /datasets.get\_schema\_keys [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#post-datasetsget_schema_keys "Direct link to POST /datasets.get_schema_keys")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#description-12 "Direct link to Description")

Get the field names that can be used in lucene query for the given dataset

versions

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#parameters-12 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-get_schema_keys-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **dataset**<br>_optional_ | The ID of the dataset. Either dataset or versions should be specified | string |
| **excluded\_types**<br>_optional_ | If passed then the keys that store data of corresponding Elastic types are not <br>returned. By default keys of 'dense\_vector' fields are not returned | < string > array |
| **versions**<br>_required_ | The IDs of the versions. Either dataset or versions should be specified | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#responses-12 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-get_schema_keys-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **frame\_keys**<br>_optional_ | Frame level fields | < string > array |
| **roi\_keys**<br>_optional_ | ROI level fields | < string > array |
| **source\_keys**<br>_optional_ | Source level fields | < string > array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#security-12 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /datasets.get\_snippets [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#post-datasetsget_snippets "Direct link to POST /datasets.get_snippets")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#description-13 "Direct link to Description")

Return first frame of for unique URIs in the dataset

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#parameters-13 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-get_snippets-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **dataset**<br>_required_ | Dataset ID | string |
| **max\_count**<br>_optional_ | Number of sources to return. default=100, Optional | integer |
| **version**<br>_optional_ | Dataset version ID. If not provided, returns sources used by all versions. | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#responses-13 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-get_snippets-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **snippets**<br>_optional_ | list of snippets | < [datasets.frame](https://clear.ml/docs/latest/docs/references/enterprise/definitions#datasetsframe) \> array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#security-13 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /datasets.get\_source\_ids [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#post-datasetsget_source_ids "Direct link to POST /datasets.get_source_ids")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#description-14 "Direct link to Description")

Get unique source ids from the given dataset version

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#parameters-14 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-get_source_ids-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **dataset**<br>_required_ | Dataset ID | string |
| **max\_count**<br>_optional_ | Number of sources to return. default=100, Optional | integer |
| **version**<br>_optional_ | Dataset version ID. If not provided, returns sources used by all versions. | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#responses-14 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-get_source_ids-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **source\_ids**<br>_optional_ | Unique source ids for the dataset version | < string > array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#security-14 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /datasets.get\_sources [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#post-datasetsget_sources "Direct link to POST /datasets.get_sources")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#description-15 "Direct link to Description")

Get all sources used by frames in the given dataset version

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#parameters-15 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-get_sources-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **dataset**<br>_required_ | Dataset ID | string |
| **max\_count**<br>_optional_ | Number of sources to return. default=100, Optional | integer |
| **version**<br>_optional_ | Dataset version ID. If not provided, returns sources used by all versions. | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#responses-15 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-get_sources-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **sources**<br>_optional_ | Mapping of source URL to first frame\_id of the source | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#security-15 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /datasets.get\_stats [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#post-datasetsget_stats "Direct link to POST /datasets.get_stats")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#description-16 "Direct link to Description")

Get labels' stats for a dataset version

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#parameters-16 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-get_stats-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **version**<br>_required_ | Dataset version ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#responses-16 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-get_stats-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **content\_types**<br>_optional_ | List of statistics for each content type | < [datasets.stat\_count](https://clear.ml/docs/latest/docs/references/enterprise/definitions#datasetsstat_count) \> array |
| **frames**<br>_optional_ | List of statistics for each frame (annotated/unannotated) | < [datasets.stat\_count](https://clear.ml/docs/latest/docs/references/enterprise/definitions#datasetsstat_count) \> array |
| **labels**<br>_optional_ | List of statistics for each label | < [datasets.stat\_count](https://clear.ml/docs/latest/docs/references/enterprise/definitions#datasetsstat_count) \> array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#security-16 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /datasets.get\_tags [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#post-datasetsget_tags "Direct link to POST /datasets.get_tags")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#description-17 "Direct link to Description")

Get user and system tags used for the specified datasets

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#parameters-17 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-get_tags-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **datasets**<br>_optional_ | The list of datasets for which the tags are collected. If not passed or empty <br>then tags from all the datasets collected | < string > array |
| **include\_system**<br>_optional_ | If set to 'true' then the list of the system tags is also returned. The default <br>value is 'false' <br>**Default** : `false` | boolean |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#responses-17 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-get_tags-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **system\_tags**<br>_optional_ | The list of unique system tag values. Returned only if 'include\_system' is set <br>to 'true' in the request | < string > array |
| **tags**<br>_optional_ | The list of unique tag values | < string > array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#security-17 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /datasets.get\_vector\_fields [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#post-datasetsget_vector_fields "Direct link to POST /datasets.get_vector_fields")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#description-18 "Direct link to Description")

Get vector fields definitions for the provided set of dataset versions

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#parameters-18 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-get_vector_fields-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **dataset**<br>_optional_ | The ID of the dataset. Either dataset or versions should be specified | string |
| **versions**<br>_optional_ | The IDs of the versions. Either dataset or versions should be specified | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#responses-18 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-get_vector_fields-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **fields**<br>_optional_ | Vector fields with their properties. | < [fields](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-get_vector_fields-post-fields) \> array |

**fields**

| Name | Description | Schema |
| --- | --- | --- |
| **key**<br>_optional_ | Field key | string |
| **properties**<br>_optional_ |  | [properties](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-get_vector_fields-post-fields-properties) |

**properties**

| Name | Description | Schema |
| --- | --- | --- |
| **dims**<br>_optional_ | The vector length | integer |
| **element\_type**<br>_optional_ | The type of the vector element <br>**Default** : `"float"` | enum (float, byte, bit) |
| **index**<br>_optional_ | Whether the field has a predefined index | boolean |
| **similarity**<br>_optional_ | Vector similarity metric | enum (l2\_norm, dot\_product, cosine) |
| **supported\_functions**<br>_optional_ | Supported similarity functions for this field | < enum (l2\_norm, dot\_product, cosine) > array |
| **type**<br>_optional_ | Field type | enum (dense\_vector) |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#security-18 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /datasets.get\_versions [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#post-datasetsget_versions "Direct link to POST /datasets.get_versions")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#description-19 "Direct link to Description")

Gets the version tree of a dataset.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#parameters-19 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-get_versions-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **dataset**<br>_required_ | Get versions starting from this time | string |
| **only\_fields**<br>_optional_ | List of version fields to fetch | < string > array |
| **only\_published**<br>_optional_ | Return only published version. <br>**Default** : `true` | boolean |
| **order\_by**<br>_optional_ | List of field names to order by. When search\_text is used, '@text\_score' can be <br>used as a field representing the text score of returned documents. Use '-' <br>prefix to specify descending order. Optional, recommended when using page. <br>Defaults to \[created\]. | < string > array |
| **page**<br>_optional_ | Page number, returns a specific page out of the result list of datasets. <br>**Minimum value** : `0` | integer |
| **page\_size**<br>_optional_ | Page size, specifies the number of results returned in each page (last page may <br>contain fewer results) <br>**Minimum value** : `1` | integer |
| **search\_text**<br>_optional_ | Free text search query | string |
| **start\_from**<br>_optional_ | Dataset ID | string |
| **system\_tags**<br>_optional_ | System tags filter. Use '-' for exclusion | < string > array |
| **tags**<br>_optional_ | User-defined tags filter. Use '-' for exclusion | < string > array |
| **versions**<br>_optional_ | List of version IDs to fetch | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#responses-19 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-get_versions-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **versions**<br>_optional_ | List of versions | < [datasets.version](https://clear.ml/docs/latest/docs/references/enterprise/definitions#datasetsversion) \> array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#security-19 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /datasets.get\_versions\_ex [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#post-datasetsget_versions_ex "Direct link to POST /datasets.get_versions_ex")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#description-20 "Direct link to Description")

Internal. Gets the version tree of a dataset.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#parameters-20 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-get_versions_ex-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **dataset**<br>_required_ | Get versions starting from this time | string |
| **filters**<br>_optional_ | List of FilterRule ('OR' connection) | < string, [filters](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-get_versions_ex-post-filters) \> map |
| **only\_fields**<br>_optional_ | List of version fields to fetch | < string > array |
| **only\_published**<br>_optional_ | Return only published version. <br>**Default** : `true` | boolean |
| **order\_by**<br>_optional_ | List of field names to order by. When search\_text is used, '@text\_score' can be <br>used as a field representing the text score of returned documents. Use '-' <br>prefix to specify descending order. Optional, recommended when using page. <br>Defaults to \[created\]. | < string > array |
| **page**<br>_optional_ | Page number, returns a specific page out of the result list of datasets. <br>**Minimum value** : `0` | integer |
| **page\_size**<br>_optional_ | Page size, specifies the number of results returned in each page (last page may <br>contain fewer results) <br>**Minimum value** : `1` | integer |
| **search\_text**<br>_optional_ | Free text search query | string |
| **start\_from**<br>_optional_ | Dataset ID | string |
| **system\_tags**<br>_optional_ | System tags filter. Use '-' for exclusion | < string > array |
| **tags**<br>_optional_ | User-defined tags filter. Use '-' for exclusion | < string > array |
| **versions**<br>_optional_ | List of version IDs to fetch | < string > array |

**filters**

| Name | Description | Schema |
| --- | --- | --- |
| **all**<br>_optional_ | All the terms in 'all' condition are combined with 'and' operation | [all](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-get_versions_ex-post-filters-all) |
| **any**<br>_optional_ | All the terms in 'any' condition are combined with 'or' operation | [any](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-get_versions_ex-post-filters-any) |
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

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#responses-20 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-get_versions_ex-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **versions**<br>_optional_ | List of versions | < [datasets.version](https://clear.ml/docs/latest/docs/references/enterprise/definitions#datasetsversion) \> array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#security-20 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /datasets.move [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#post-datasetsmove "Direct link to POST /datasets.move")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#description-21 "Direct link to Description")

Move datasets to a project

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#parameters-21 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-move-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **ids**<br>_required_ | Datasets to move | < string > array |
| **project**<br>_optional_ | Target project ID. If not provided, `project_name` must be provided. Use null <br>for the root project | string |
| **project\_name**<br>_optional_ | Target project name. If provided and a project with this name does not exist, a <br>new project will be created. If not provided, `project` must be provided. | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#responses-21 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#security-21 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /datasets.publish\_and\_create\_child\_version [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#post-datasetspublish_and_create_child_version "Direct link to POST /datasets.publish_and_create_child_version")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#description-22 "Direct link to Description")

Publishes the specified version and creates a draft child version for it

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#parameters-22 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-publish_and_create_child_version-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **child\_comment**<br>_optional_ | Comment for the child version | string |
| **child\_metadata**<br>_optional_ | User-specified metadata object for the child version. Keys must not include '$' <br>and '.'. | object |
| **child\_name**<br>_optional_ | Name for the child version. If not provided then the name of the parent version <br>is taken | string |
| **child\_system\_tags**<br>_optional_ | The new system tags for the child version. If not passed then the parent <br>version system tags are used | < string > array |
| **child\_tags**<br>_optional_ | The new user tags for the child version. If not passed then the parent version <br>tags are used | < string > array |
| **dataset**<br>_required_ | Dataset ID | string |
| **publish\_comment**<br>_optional_ | New comment for the published version. The default value is 'published at <br> by ' | string |
| **publish\_metadata**<br>_optional_ | User-specified metadata object for the published version. Keys must not include <br>'$' and '.'. | object |
| **publish\_name**<br>_optional_ | New name for the published version. The default value is 'snapshot ' | string |
| **publish\_system\_tags**<br>_optional_ | The new system tags for the published version. If not passed then the parent <br>version system tags are used | < string > array |
| **publish\_tags**<br>_optional_ | The new user-defined tags for the published version. If not passed then the <br>parent version tags are used | < string > array |
| **version**<br>_required_ | Draft version ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#responses-22 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-publish_and_create_child_version-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_optional_ | ID of the child version | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#security-22 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /datasets.publish\_version [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#post-datasetspublish_version "Direct link to POST /datasets.publish_version")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#description-23 "Direct link to Description")

Publish a draft version.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#parameters-23 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-publish_version-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **force**<br>_optional_ | Ignore ongoing annotation tasks with this version as input <br>**Default** : `false` | boolean |
| **publishing\_task**<br>_optional_ | ID of an in-progress annotation task calling this endpoint. Versions which are <br>used as input of in-progress annotation tasks can only be published if there is <br>only one such task and its ID is sent in this field. This is required if one <br>exists. | string |
| **version**<br>_required_ | Draft version ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#responses-23 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#security-23 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /datasets.save\_frames [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#post-datasetssave_frames "Direct link to POST /datasets.save_frames")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#description-24 "Direct link to Description")

Save frames into a draft version. Frame IDs, if sent, will be ignored, and

every frame will be assigned a new ID.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#parameters-24 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-save_frames-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **frames**<br>_required_ | Frames to save | < [datasets.frame](https://clear.ml/docs/latest/docs/references/enterprise/definitions#datasetsframe) \> array |
| **version**<br>_required_ | Draft version ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#responses-24 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-save_frames-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **errors**<br>_optional_ | Failure details | < object > array |
| **failed**<br>_optional_ | Number of frames we failed to save | integer |
| **ids**<br>_optional_ | Saved frame IDs | < string > array |
| **saved**<br>_optional_ | Number of frames saved | integer |
| **total\_rois**<br>_optional_ | Total number of ROIs saved | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#security-24 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /datasets.update [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#post-datasetsupdate "Direct link to POST /datasets.update")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#description-25 "Direct link to Description")

Updates an existing dataset object

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#parameters-25 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-update-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **comment**<br>_optional_ | Dataset comment | string |
| **dataset**<br>_required_ | Dataset ID | string |
| **metadata**<br>_optional_ | User-specified metadata object. Keys must not include '$' and '.'. | object |
| **name**<br>_optional_ | Dataset name Unique within the company. | string |
| **project**<br>_optional_ | Project to which to dataset belongs | string |
| **system\_tags**<br>_optional_ | System tags list. This field is reserved for system use, please don't use it. | < string > array |
| **tags**<br>_optional_ | User-defined tags list | < string > array |
| **terms\_of\_use**<br>_optional_ | Terms of use string | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#responses-25 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-update-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **fields**<br>_optional_ | Updated fields names names and values | object |
| **updated**<br>_optional_ | Number of datasets updated (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#security-25 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /datasets.update\_frames [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#post-datasetsupdate_frames "Direct link to POST /datasets.update_frames")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#description-26 "Direct link to Description")

Update frames in a draft version. Each frame must contain an ID.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#parameters-26 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-update_frames-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **frames**<br>_required_ | Frames to update | < [datasets.frame](https://clear.ml/docs/latest/docs/references/enterprise/definitions#datasetsframe) \> array |
| **version**<br>_required_ | Draft version ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#responses-26 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-update_frames-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **errors**<br>_optional_ | Failure details | < object > array |
| **failed**<br>_optional_ | Number of frames we failed to update | integer |
| **ids**<br>_optional_ | Updated frame IDs | < string > array |
| **merged**<br>_optional_ | Number of frames merged | integer |
| **total\_rois**<br>_optional_ | Total number of ROIs updated | integer |
| **updated**<br>_optional_ | Number of frames updated | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#security-26 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /datasets.update\_stats\_for\_all\_versions [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#post-datasetsupdate_stats_for_all_versions "Direct link to POST /datasets.update_stats_for_all_versions")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#description-27 "Direct link to Description")

Internal. Update statistics for all versions in (all) datasets

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#parameters-27 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-update_stats_for_all_versions-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **datasets**<br>_optional_ | List of dataset IDs | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#responses-27 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-update_stats_for_all_versions-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **updated**<br>_optional_ | List of updated datasets (IDs) | < string > array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#security-27 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /datasets.update\_version [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#post-datasetsupdate_version "Direct link to POST /datasets.update_version")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#description-28 "Direct link to Description")

Updates version information

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#parameters-28 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-update_version-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **comment**<br>_optional_ | New comment for the version | string |
| **metadata**<br>_optional_ | User-specified metadata object. Keys must not include '$' and '.'. | object |
| **name**<br>_optional_ | New name for the version | string |
| **system\_tags**<br>_optional_ | System tags list. This field is reserved for system use, please don't use it. | < string > array |
| **tags**<br>_optional_ | User-defined tags list | < string > array |
| **version**<br>_required_ | Version ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#responses-28 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#datasets-update_version-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **updated**<br>_optional_ | Number of updated versions | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/datasets/\#security-28 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

- [POST /datasets.commit\_version](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#post-datasetscommit_version)
- [POST /datasets.create](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#post-datasetscreate)
- [POST /datasets.create\_version](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#post-datasetscreate_version)
- [POST /datasets.delete](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#post-datasetsdelete)
- [POST /datasets.delete\_frames](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#post-datasetsdelete_frames)
- [POST /datasets.delete\_version](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#post-datasetsdelete_version)
- [POST /datasets.get\_all](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#post-datasetsget_all)
- [POST /datasets.get\_all\_ex](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#post-datasetsget_all_ex)
- [POST /datasets.get\_by\_id](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#post-datasetsget_by_id)
- [POST /datasets.get\_by\_name](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#post-datasetsget_by_name)
- [POST /datasets.get\_label\_keywords\_for\_running\_task](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#post-datasetsget_label_keywords_for_running_task)
- [POST /datasets.get\_schema](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#post-datasetsget_schema)
- [POST /datasets.get\_schema\_keys](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#post-datasetsget_schema_keys)
- [POST /datasets.get\_snippets](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#post-datasetsget_snippets)
- [POST /datasets.get\_source\_ids](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#post-datasetsget_source_ids)
- [POST /datasets.get\_sources](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#post-datasetsget_sources)
- [POST /datasets.get\_stats](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#post-datasetsget_stats)
- [POST /datasets.get\_tags](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#post-datasetsget_tags)
- [POST /datasets.get\_vector\_fields](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#post-datasetsget_vector_fields)
- [POST /datasets.get\_versions](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#post-datasetsget_versions)
- [POST /datasets.get\_versions\_ex](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#post-datasetsget_versions_ex)
- [POST /datasets.move](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#post-datasetsmove)
- [POST /datasets.publish\_and\_create\_child\_version](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#post-datasetspublish_and_create_child_version)
- [POST /datasets.publish\_version](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#post-datasetspublish_version)
- [POST /datasets.save\_frames](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#post-datasetssave_frames)
- [POST /datasets.update](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#post-datasetsupdate)
- [POST /datasets.update\_frames](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#post-datasetsupdate_frames)
- [POST /datasets.update\_stats\_for\_all\_versions](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#post-datasetsupdate_stats_for_all_versions)
- [POST /datasets.update\_version](https://clear.ml/docs/latest/docs/references/enterprise/datasets/#post-datasetsupdate_version)