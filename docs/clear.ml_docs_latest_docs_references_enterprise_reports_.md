---
url: "https://clear.ml/docs/latest/docs/references/enterprise/reports/"
title: "reports | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/enterprise/reports/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

### POST /reports.archive [​](https://clear.ml/docs/latest/docs/references/enterprise/reports/\#post-reportsarchive "Direct link to POST /reports.archive")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/reports/\#description "Direct link to Description")

Archive report

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/reports/\#parameters "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/reports/#reports-archive-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **comment**<br>_optional_ | The client message | string |
| **task**<br>_required_ | The ID of the report task to archive | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/reports/\#responses "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/reports/#reports-archive-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **archived**<br>_optional_ | Number of reports archived (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/reports/\#security "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /reports.create [​](https://clear.ml/docs/latest/docs/references/enterprise/reports/\#post-reportscreate "Direct link to POST /reports.create")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/reports/\#description-1 "Direct link to Description")

Create a new report

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/reports/\#parameters-1 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/reports/#reports-create-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **comment**<br>_optional_ | Free text comment | string |
| **name**<br>_required_ | Report name. Unique within the company. | string |
| **project**<br>_optional_ | Project ID of the project to which this report is assigned Must exist\[ab\] | string |
| **report**<br>_optional_ | Report template | string |
| **report\_assets**<br>_optional_ | List of the external report assets | < string > array |
| **tags**<br>_optional_ | User-defined tags list | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/reports/\#responses-1 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/reports/#reports-create-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_optional_ | ID of the report | string |
| **project\_id**<br>_optional_ | ID of the project that the report belongs to | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/reports/\#security-1 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /reports.delete [​](https://clear.ml/docs/latest/docs/references/enterprise/reports/\#post-reportsdelete "Direct link to POST /reports.delete")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/reports/\#description-2 "Direct link to Description")

Delete report

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/reports/\#parameters-2 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/reports/#reports-delete-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **force**<br>_optional_ | If not set then published or unarchived reports cannot be deleted <br>**Default** : `false` | boolean |
| **task**<br>_required_ | The ID of the report task to delete | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/reports/\#responses-2 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/reports/#reports-delete-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **deleted**<br>_optional_ | Number of deleted reports (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/reports/\#security-2 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /reports.get\_all\_ex [​](https://clear.ml/docs/latest/docs/references/enterprise/reports/\#post-reportsget_all_ex "Direct link to POST /reports.get_all_ex")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/reports/\#description-3 "Direct link to Description")

Get all the company's and public report tasks

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/reports/\#parameters-3 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/reports/#reports-get_all_ex-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **_all_**<br>_optional_ | Multi-field pattern condition (all fields match pattern) | [reports.multi\_field\_pattern\_data](https://clear.ml/docs/latest/docs/references/enterprise/definitions#reportsmulti_field_pattern_data) |
| **_any_**<br>_optional_ | Multi-field pattern condition (any field matches pattern) | [reports.multi\_field\_pattern\_data](https://clear.ml/docs/latest/docs/references/enterprise/definitions#reportsmulti_field_pattern_data) |
| **allow\_public**<br>_optional_ | Allow public reports to be returned in the results <br>**Default** : `true` | boolean |
| **filters**<br>_optional_ | List of FilterRule ('OR' connection) | < string, [filters](https://clear.ml/docs/latest/docs/references/enterprise/reports/#reports-get_all_ex-post-filters) \> map |
| **id**<br>_optional_ | List of IDs to filter by | < string > array |
| **include\_subprojects**<br>_optional_ | If set to 'true' and project field is set then reports from the subprojects are <br>searched too <br>**Default** : `false` | boolean |
| **name**<br>_optional_ | Get only reports whose name matches this pattern (python regular expression <br>syntax) | string |
| **only\_fields**<br>_optional_ | List of report field names (nesting is supported using '.'). If provided, this <br>list defines the query's projection (only these fields will be returned for <br>each result entry) | < string > array |
| **order\_by**<br>_optional_ | List of field names to order by. When search\_text is used, '@text\_score' can be <br>used as a field representing the text score of returned documents. Use '-' <br>prefix to specify descending order. Optional, recommended when using page | < string > array |
| **page**<br>_optional_ | Page number, returns a specific page out of the resulting list of reports <br>**Minimum value** : `0` | integer |
| **page\_size**<br>_optional_ | Page size, specifies the number of results returned in each page (last page may <br>contain fewer results) <br>**Minimum value** : `1` | integer |
| **project**<br>_optional_ | List of project IDs | < string > array |
| **refresh\_scroll**<br>_optional_ | If set then all the data received with this scroll will be requeried | boolean |
| **scroll\_id**<br>_optional_ | Scroll ID returned from the previos calls to get\_all | string |
| **search\_text**<br>_optional_ | Free text search query | string |
| **size**<br>_optional_ | The number of tasks to retrieve <br>**Minimum value** : `1` | integer |
| **status**<br>_optional_ | List of report status. | < [reports.report\_status\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions#reportsreport_status_enum) \> array |
| **status\_changed**<br>_optional_ | List of status changed constraint strings (utcformat, epoch) with an optional <br>prefix modifier (>, >=, <, <=) | < string > array |
| **system\_tags**<br>_optional_ | List of report system tags. Use '-' prefix to exclude system tags | < string > array |
| **tags**<br>_optional_ | List of report user-defined tags. Use '-' prefix to exclude tags | < string > array |
| **user**<br>_optional_ | List of user IDs used to filter results by the reports's creating user | < string > array |

**filters**

| Name | Description | Schema |
| --- | --- | --- |
| **all**<br>_optional_ | All the terms in 'all' condition are combined with 'and' operation | [all](https://clear.ml/docs/latest/docs/references/enterprise/reports/#reports-get_all_ex-post-filters-all) |
| **any**<br>_optional_ | All the terms in 'any' condition are combined with 'or' operation | [any](https://clear.ml/docs/latest/docs/references/enterprise/reports/#reports-get_all_ex-post-filters-any) |
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

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/reports/\#responses-3 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/reports/#reports-get_all_ex-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **scroll\_id**<br>_optional_ | Scroll ID that can be used with the next calls to get\_all to retrieve more data | string |
| **tasks**<br>_optional_ | List of report tasks | < [reports.report](https://clear.ml/docs/latest/docs/references/enterprise/definitions#reportsreport) \> array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/reports/\#security-3 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /reports.get\_tags [​](https://clear.ml/docs/latest/docs/references/enterprise/reports/\#post-reportsget_tags "Direct link to POST /reports.get_tags")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/reports/\#description-4 "Direct link to Description")

Get all the user tags used for the company reports

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/reports/\#parameters-4 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/reports/\#responses-4 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/reports/#reports-get_tags-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **tags**<br>_optional_ | The list of unique tag values | < string > array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/reports/\#security-4 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /reports.get\_task\_data [​](https://clear.ml/docs/latest/docs/references/enterprise/reports/\#post-reportsget_task_data "Direct link to POST /reports.get_task_data")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/reports/\#description-5 "Direct link to Description")

Get the tasks data according the passed search criteria + requested events

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/reports/\#parameters-5 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/reports/#reports-get_task_data-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **_all_**<br>_optional_ | Multi-field pattern condition (all fields match pattern) | [reports.multi\_field\_pattern\_data](https://clear.ml/docs/latest/docs/references/enterprise/definitions#reportsmulti_field_pattern_data) |
| **_any_**<br>_optional_ | Multi-field pattern condition (any field matches pattern) | [reports.multi\_field\_pattern\_data](https://clear.ml/docs/latest/docs/references/enterprise/definitions#reportsmulti_field_pattern_data) |
| **allow\_public**<br>_optional_ | Allow public tasks to be returned in the results <br>**Default** : `true` | boolean |
| **debug\_images**<br>_optional_ | debug\_images | [debug\_images](https://clear.ml/docs/latest/docs/references/enterprise/reports/#reports-get_task_data-post-debug_images) |
| **id**<br>_optional_ | List of IDs to filter by | < string > array |
| **include\_subprojects**<br>_optional_ | If set to 'true' and project field is set then tasks from the subprojects are <br>searched too <br>**Default** : `false` | boolean |
| **input.view.entries.dataset**<br>_optional_ | List of input dataset IDs | < string > array |
| **input.view.entries.version**<br>_optional_ | List of input dataset version IDs | < string > array |
| **model\_events**<br>_optional_ | If set then the retrieving model events. Otherwise task events <br>**Default** : `false` | boolean |
| **name**<br>_optional_ | Get only tasks whose name matches this pattern (python regular expression <br>syntax) | string |
| **only\_fields**<br>_optional_ | List of task field names (nesting is supported using '.', e.g. <br>execution.model\_labels). If provided, this list defines the query's projection <br>(only these fields will be returned for each result entry) | < string > array |
| **order\_by**<br>_optional_ | List of field names to order by. When search\_text is used, '@text\_score' can be <br>used as a field representing the text score of returned documents. Use '-' <br>prefix to specify descending order. Optional, recommended when using page | < string > array |
| **parent**<br>_optional_ | Parent ID | string |
| **plots**<br>_optional_ | Description of saved plots to return | [plots](https://clear.ml/docs/latest/docs/references/enterprise/reports/#reports-get_task_data-post-plots) |
| **project**<br>_optional_ | List of project IDs | < string > array |
| **scalar\_metrics\_iter\_histogram**<br>_optional_ | scalar\_metrics\_iter\_histogram | [scalar\_metrics\_iter\_histogram](https://clear.ml/docs/latest/docs/references/enterprise/reports/#reports-get_task_data-post-scalar_metrics_iter_histogram) |
| **search\_hidden**<br>_optional_ | If set to 'true' then hidden tasks are included in the search results <br>**Default** : `false` | boolean |
| **search\_text**<br>_optional_ | Free text search query | string |
| **single\_value\_metrics**<br>_optional_ | If passed then task single value metrics are returned | object |
| **size**<br>_optional_ | The number of tasks to retrieve <br>**Minimum value** : `1` | integer |
| **status**<br>_optional_ | List of task status. | < [reports.task\_status\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions#reportstask_status_enum) \> array |
| **status\_changed**<br>_optional_ | List of status changed constraint strings (utcformat, epoch) with an optional <br>prefix modifier (>, >=, <, <=) | < string > array |
| **system\_tags**<br>_optional_ | List of task system tags. Use '-' prefix to exclude system tags | < string > array |
| **tags**<br>_optional_ | List of task user-defined tags. Use '-' prefix to exclude tags | < string > array |
| **type**<br>_optional_ | List of task types. One or more of: 'import', 'annotation', 'training' or <br>'testing' (case insensitive) | < string > array |
| **user**<br>_optional_ | List of user IDs used to filter results by the task's creating user | < string > array |

**debug\_images**

| Name | Description | Schema |
| --- | --- | --- |
| **iters**<br>_optional_ | Max number of latest iterations for which to return debug images | integer |
| **metrics**<br>_optional_ | List of metrics and variants | < [reports.metric\_variants](https://clear.ml/docs/latest/docs/references/enterprise/definitions#reportsmetric_variants) \> array |

**plots**

| Name | Description | Schema |
| --- | --- | --- |
| **iters**<br>_optional_ | Max number of latest iterations for which to return plots | integer |
| **last\_iters\_per\_task\_metric**<br>_optional_ | If set to 'true' and iters passed then last iterations for each task metrics <br>are retrieved. Otherwise last iterations for the whole task are retrieved <br>**Default** : `true` | boolean |
| **metrics**<br>_optional_ |  | < [reports.metric\_variants](https://clear.ml/docs/latest/docs/references/enterprise/definitions#reportsmetric_variants) \> array |

**scalar\_metrics\_iter\_histogram**

| Name | Description | Schema |
| --- | --- | --- |
| **key**<br>_optional_ | Histogram x axis to use: iter - iteration number iso\_time - event time as ISO <br>formatted string timestamp - event timestamp as milliseconds since epoch | [reports.scalar\_key\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions#reportsscalar_key_enum) |
| **metrics**<br>_optional_ | List of metrics and variants | < [reports.metric\_variants](https://clear.ml/docs/latest/docs/references/enterprise/definitions#reportsmetric_variants) \> array |
| **samples**<br>_optional_ | The amount of histogram points to return (0 to return all the points). <br>Optional, the default value is 6000. | integer |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/reports/\#responses-5 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/reports/#reports-get_task_data-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **debug\_images**<br>_optional_ | Debug image events grouped by tasks and iterations | < [reports.debug\_images\_response\_task\_metrics](https://clear.ml/docs/latest/docs/references/enterprise/definitions#reportsdebug_images_response_task_metrics) \> array |
| **plots**<br>_optional_ | Plots mapped by metric, variant, task and iteration | object |
| **scalar\_metrics\_iter\_histogram**<br>_optional_ |  | object |
| **single\_value\_metrics**<br>_optional_ | Single value metrics grouped by task | < [reports.single\_value\_task\_metrics](https://clear.ml/docs/latest/docs/references/enterprise/definitions#reportssingle_value_task_metrics) \> array |
| **tasks**<br>_optional_ | List of tasks | < [reports.task](https://clear.ml/docs/latest/docs/references/enterprise/definitions#reportstask) \> array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/reports/\#security-5 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /reports.move [​](https://clear.ml/docs/latest/docs/references/enterprise/reports/\#post-reportsmove "Direct link to POST /reports.move")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/reports/\#description-6 "Direct link to Description")

Move reports to a project

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/reports/\#parameters-6 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/reports/#reports-move-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **project**<br>_optional_ | Target project ID. If not provided, `project_name` must be provided. Use null <br>for the root project | string |
| **project\_name**<br>_optional_ | Target project name. If provided and a project with this name does not exist, a <br>new project will be created. If not provided, `project` must be provided. | string |
| **task**<br>_required_ | ID of the report to move | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/reports/\#responses-6 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/reports/#reports-move-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **project\_id**<br>_optional_ | The ID of the target project | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/reports/\#security-6 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /reports.publish [​](https://clear.ml/docs/latest/docs/references/enterprise/reports/\#post-reportspublish "Direct link to POST /reports.publish")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/reports/\#description-7 "Direct link to Description")

Publish report

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/reports/\#parameters-7 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/reports/#reports-publish-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **comment**<br>_optional_ | The client message | string |
| **task**<br>_required_ | The ID of the report task to publish | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/reports/\#responses-7 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/reports/#reports-publish-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **fields**<br>_optional_ | Updated fields names and values | object |
| **updated**<br>_optional_ | Number of reports updated (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/reports/\#security-7 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /reports.unarchive [​](https://clear.ml/docs/latest/docs/references/enterprise/reports/\#post-reportsunarchive "Direct link to POST /reports.unarchive")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/reports/\#description-8 "Direct link to Description")

Unarchive report

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/reports/\#parameters-8 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/reports/#reports-unarchive-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **comment**<br>_optional_ | The client message | string |
| **task**<br>_required_ | The ID of the report task to unarchive | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/reports/\#responses-8 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/reports/#reports-unarchive-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **unarchived**<br>_optional_ | Number of reports unarchived (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/reports/\#security-8 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /reports.update [​](https://clear.ml/docs/latest/docs/references/enterprise/reports/\#post-reportsupdate "Direct link to POST /reports.update")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/reports/\#description-9 "Direct link to Description")

Create a new report

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/reports/\#parameters-9 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/reports/#reports-update-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **comment**<br>_optional_ | Free text comment | string |
| **name**<br>_optional_ | Report name. Unique within the company. | string |
| **report**<br>_optional_ | Report template | string |
| **report\_assets**<br>_optional_ | List of the external report assets | < string > array |
| **tags**<br>_optional_ | User-defined tags list | < string > array |
| **task**<br>_required_ | The ID of the report task to update | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/reports/\#responses-9 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/reports/#reports-update-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **fields**<br>_optional_ | Updated fields names and values | object |
| **updated**<br>_optional_ | Number of reports updated (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/reports/\#security-9 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

- [POST /reports.archive](https://clear.ml/docs/latest/docs/references/enterprise/reports/#post-reportsarchive)
- [POST /reports.create](https://clear.ml/docs/latest/docs/references/enterprise/reports/#post-reportscreate)
- [POST /reports.delete](https://clear.ml/docs/latest/docs/references/enterprise/reports/#post-reportsdelete)
- [POST /reports.get\_all\_ex](https://clear.ml/docs/latest/docs/references/enterprise/reports/#post-reportsget_all_ex)
- [POST /reports.get\_tags](https://clear.ml/docs/latest/docs/references/enterprise/reports/#post-reportsget_tags)
- [POST /reports.get\_task\_data](https://clear.ml/docs/latest/docs/references/enterprise/reports/#post-reportsget_task_data)
- [POST /reports.move](https://clear.ml/docs/latest/docs/references/enterprise/reports/#post-reportsmove)
- [POST /reports.publish](https://clear.ml/docs/latest/docs/references/enterprise/reports/#post-reportspublish)
- [POST /reports.unarchive](https://clear.ml/docs/latest/docs/references/enterprise/reports/#post-reportsunarchive)
- [POST /reports.update](https://clear.ml/docs/latest/docs/references/enterprise/reports/#post-reportsupdate)