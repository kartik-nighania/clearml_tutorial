---
url: "https://clear.ml/docs/latest/docs/references/enterprise/projects/"
title: "projects | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/enterprise/projects/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

### POST /projects.create [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#post-projectscreate "Direct link to POST /projects.create")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#description "Direct link to Description")

Create a new project

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#parameters "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-create-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **default\_output\_destination**<br>_optional_ | The default output destination URL for new tasks under this project | string |
| **description**<br>_optional_ | Project description. | string |
| **name**<br>_required_ | Project name Unique within the company. | string |
| **system\_tags**<br>_optional_ | System tags. This field is reserved for system use, please don't use it. | < string > array |
| **tags**<br>_optional_ | User-defined tags | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#responses "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-create-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_optional_ | Project id | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#security "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /projects.delete [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#post-projectsdelete "Direct link to POST /projects.delete")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#description-1 "Direct link to Description")

Deletes a project

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#parameters-1 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-delete-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **delete\_contents**<br>_optional_ | If set to 'true' then the project tasks, models and dataviews will be deleted. <br>Otherwise their project property will be unassigned. Default value is 'false' | boolean |
| **delete\_external\_artifacts**<br>_optional_ | If set to 'true' then BE will try to delete the extenal artifacts associated <br>with the project tasks and models from the fileserver (if configured to do so) <br>**Default** : `true` | boolean |
| **force**<br>_optional_ | If not true, fails if project has tasks. If true, and project has tasks, they <br>will be unassigned <br>**Default** : `false` | boolean |
| **project**<br>_required_ | Project ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#responses-1 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-delete-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **deleted**<br>_optional_ | Number of projects deleted (0 or 1) | integer |
| **deleted\_datasets**<br>_optional_ | Number of datasets deleted | integer |
| **deleted\_dataviews**<br>_optional_ | Number of dataviews deleted | integer |
| **deleted\_models**<br>_optional_ | Number of models deleted | integer |
| **deleted\_tasks**<br>_optional_ | Number of tasks deleted | integer |
| **disassociated\_datasets**<br>_optional_ | Number of datasets disassociated from the deleted project | integer |
| **disassociated\_tasks**<br>_optional_ | Number of tasks disassociated from the deleted project | integer |
| **urls**<br>_optional_ | The urls of the files that were uploaded by the project tasks and models. <br>Returned if the 'delete\_contents' was set to 'true' | [projects.urls](https://clear.ml/docs/latest/docs/references/enterprise/definitions#projectsurls) |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#security-1 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /projects.get\_all [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#post-projectsget_all "Direct link to POST /projects.get_all")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#description-2 "Direct link to Description")

Get all the company's projects and all public projects

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#parameters-2 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-get_all-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **_all_**<br>_optional_ | Multi-field pattern condition (all fields match pattern) | [projects.multi\_field\_pattern\_data](https://clear.ml/docs/latest/docs/references/enterprise/definitions#projectsmulti_field_pattern_data) |
| **_any_**<br>_optional_ | Multi-field pattern condition (any field matches pattern) | [projects.multi\_field\_pattern\_data](https://clear.ml/docs/latest/docs/references/enterprise/definitions#projectsmulti_field_pattern_data) |
| **basename**<br>_optional_ | Project base name | string |
| **description**<br>_optional_ | Get only projects whose description matches this pattern (python regular <br>expression syntax) | string |
| **id**<br>_optional_ | List of IDs to filter by | < string > array |
| **name**<br>_optional_ | Get only projects whose name matches this pattern (python regular expression <br>syntax) | string |
| **only\_fields**<br>_optional_ | List of document's field names (nesting is supported using '.', e.g. <br>execution.model\_labels). If provided, this list defines the query's projection <br>(only these fields will be returned for each result entry) | < string > array |
| **order\_by**<br>_optional_ | List of field names to order by. When search\_text is used, '@text\_score' can be <br>used as a field representing the text score of returned documents. Use '-' <br>prefix to specify descending order. Optional, recommended when using page | < string > array |
| **page**<br>_optional_ | Page number, returns a specific page out of the resulting list of dataviews <br>**Minimum value** : `0` | integer |
| **page\_size**<br>_optional_ | Page size, specifies the number of results returned in each page (last page may <br>contain fewer results) <br>**Minimum value** : `1` | integer |
| **refresh\_scroll**<br>_optional_ | If set then all the data received with this scroll will be requeried | boolean |
| **scroll\_id**<br>_optional_ | Scroll ID returned from the previos calls to get\_all\_ex | string |
| **search\_hidden**<br>_optional_ | If set to 'true' then hidden projects are included in the search results <br>**Default** : `false` | boolean |
| **search\_text**<br>_optional_ | Free text search query | string |
| **shallow\_search**<br>_optional_ | If set to 'true' then the search with the specified criteria is performed among <br>top level projects only (or if parents specified, among the direct children of <br>the these parents). Otherwise the search is performed among all the company <br>projects (or among all of the descendants of the specified parents). <br>**Default** : `false` | boolean |
| **size**<br>_optional_ | The number of projects to retrieve <br>**Minimum value** : `1` | integer |
| **system\_tags**<br>_optional_ | System tags list used to filter results. Prepend '-' to system tag name to <br>indicate exclusion | < string > array |
| **tags**<br>_optional_ | User-defined tags list used to filter results. Prepend '-' to tag name to <br>indicate exclusion | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#responses-2 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-get_all-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **projects**<br>_optional_ | Projects list | < [projects.projects\_get\_all\_response\_single](https://clear.ml/docs/latest/docs/references/enterprise/definitions#projectsprojects_get_all_response_single) \> array |
| **scroll\_id**<br>_optional_ | Scroll ID that can be used with the next calls to get\_all\_ex to retrieve more <br>data | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#security-2 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /projects.get\_all\_ex [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#post-projectsget_all_ex "Direct link to POST /projects.get_all_ex")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#description-3 "Direct link to Description")

Internal. Get all the company's projects and all public projects

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#parameters-3 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-get_all_ex-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **_all_**<br>_optional_ | Multi-field pattern condition (all fields match pattern) | [projects.multi\_field\_pattern\_data](https://clear.ml/docs/latest/docs/references/enterprise/definitions#projectsmulti_field_pattern_data) |
| **_any_**<br>_optional_ | Multi-field pattern condition (any field matches pattern) | [projects.multi\_field\_pattern\_data](https://clear.ml/docs/latest/docs/references/enterprise/definitions#projectsmulti_field_pattern_data) |
| **active\_users**<br>_optional_ | The list of users that were active in the project. If passes then the resulting <br>projects are filtered to the ones that have tasks created by these users | < string > array |
| **allow\_public**<br>_optional_ | Allow public projects to be returned in the results <br>**Default** : `true` | boolean |
| **basename**<br>_optional_ | Project base name | string |
| **check\_own\_contents**<br>_optional_ | If set to 'true' and project ids are passed to the query then for these <br>projects their own tasks, models and dataviews are counted <br>**Default** : `false` | boolean |
| **children\_tags**<br>_optional_ | The list of tag values to filter children by. Takes effect only if <br>children\_type is set. Use 'null' value to specify empty tags. Use '\_\_Snot' <br>value to specify that the following value should be excluded | < string > array |
| **children\_tags\_filter**<br>_optional_ | Filter on a field that includes combination of 'any' or 'all' included and <br>excluded terms | [children\_tags\_filter](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-get_all_ex-post-children_tags_filter) |
| **children\_type**<br>_optional_ | If specified that only the projects under which the entities of this type can <br>be found will be returned | enum (pipeline, report, hyperdataset, dataset) |
| **description**<br>_optional_ | Get only projects whose description matches this pattern (python regular <br>expression syntax) | string |
| **filters**<br>_optional_ | List of FilterRule ('OR' connection) | < string, [filters](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-get_all_ex-post-filters) \> map |
| **id**<br>_optional_ | List of IDs to filter by | < string > array |
| **include\_dataset\_stats**<br>_optional_ | If true, include project dataset statistic in response <br>**Default** : `false` | boolean |
| **include\_stats**<br>_optional_ | If true, include project statistic in response. <br>**Default** : `false` | boolean |
| **include\_stats\_filter**<br>_optional_ | The filter for selecting entities that participate in statistics calculation. <br>For each task field that you want to filter on pass the list of allowed values. <br>Prepend the value with '-' to exclude | object |
| **name**<br>_optional_ | Get only projects whose name matches this pattern (python regular expression <br>syntax) | string |
| **non\_public**<br>_optional_ | Return only non-public projects <br>**Default** : `false` | boolean |
| **only\_fields**<br>_optional_ | List of document's field names (nesting is supported using '.', e.g. <br>execution.model\_labels). If provided, this list defines the query's projection <br>(only these fields will be returned for each result entry) | < string > array |
| **order\_by**<br>_optional_ | List of field names to order by. When search\_text is used, '@text\_score' can be <br>used as a field representing the text score of returned documents. Use '-' <br>prefix to specify descending order. Optional, recommended when using page | < string > array |
| **page**<br>_optional_ | Page number, returns a specific page out of the resulting list of dataviews <br>**Minimum value** : `0` | integer |
| **page\_size**<br>_optional_ | Page size, specifies the number of results returned in each page (last page may <br>contain fewer results) <br>**Minimum value** : `1` | integer |
| **permission\_roots\_only**<br>_optional_ | If Truethen the shallow search is done among all the top projects that the user <br>has access to beneath the requested parent. Even if these projects are not <br>direct children of the parent <br>**Default** : `false` | boolean |
| **refresh\_scroll**<br>_optional_ | If set then all the data received with this scroll will be requeried | boolean |
| **scroll\_id**<br>_optional_ | Scroll ID returned from the previos calls to get\_all | string |
| **search\_hidden**<br>_optional_ | If set to 'true' then hidden projects are included in the search results <br>**Default** : `false` | boolean |
| **search\_text**<br>_optional_ | Free text search query | string |
| **shallow\_search**<br>_optional_ | If set to 'true' then the search with the specified criteria is performed among <br>top level projects only (or if parents specified, among the direct children of <br>the these parents). Otherwise the search is performed among all the company <br>projects (or among all of the descendants of the specified parents). <br>**Default** : `false` | boolean |
| **size**<br>_optional_ | The number of projects to retrieve <br>**Minimum value** : `1` | integer |
| **stats\_for\_state**<br>_optional_ | Obsolete! Statistics is calculated always for the 'active' state <br>**Default** : `"active"` | enum (active, archived) |
| **stats\_with\_children**<br>_optional_ | If include\_stats flag is set then this flag contols whether the child projects <br>tasks are taken into statistics or not <br>**Default** : `true` | boolean |
| **system\_tags**<br>_optional_ | System tags list used to filter results. Prepend '-' to system tag name to <br>indicate exclusion | < string > array |
| **tags**<br>_optional_ | User-defined tags list used to filter results. Prepend '-' to tag name to <br>indicate exclusion | < string > array |

**children\_tags\_filter**

| Name | Description | Schema |
| --- | --- | --- |
| **all**<br>_optional_ | All the terms in 'all' condition are combined with 'and' operation | [all](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-get_all_ex-post-children_tags_filter-all) |
| **any**<br>_optional_ | All the terms in 'any' condition are combined with 'or' operation | [any](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-get_all_ex-post-children_tags_filter-any) |
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

**filters**

| Name | Description | Schema |
| --- | --- | --- |
| **all**<br>_optional_ | All the terms in 'all' condition are combined with 'and' operation | [all](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-get_all_ex-post-filters-all) |
| **any**<br>_optional_ | All the terms in 'any' condition are combined with 'or' operation | [any](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-get_all_ex-post-filters-any) |
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

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#responses-3 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-get_all_ex-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **projects**<br>_optional_ | Projects list | < [projects.projects\_get\_all\_response\_single](https://clear.ml/docs/latest/docs/references/enterprise/definitions#projectsprojects_get_all_response_single) \> array |
| **scroll\_id**<br>_optional_ | Scroll ID that can be used with the next calls to get\_all to retrieve more data | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#security-3 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /projects.get\_by\_id [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#post-projectsget_by_id "Direct link to POST /projects.get_by_id")

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#parameters-4 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-get_by_id-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **project**<br>_required_ | Project id | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#responses-4 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-get_by_id-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **project**<br>_optional_ | Project info | [projects.project](https://clear.ml/docs/latest/docs/references/enterprise/definitions#projectsproject) |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#security-4 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /projects.get\_hyper\_parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#post-projectsget_hyper_parameters "Direct link to POST /projects.get_hyper_parameters")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#description-4 "Direct link to Description")

Get a list of all hyper parameter sections and names used in tasks within the

given project.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#parameters-5 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-get_hyper_parameters-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **include\_subprojects**<br>_optional_ | If set to 'true' and the project field is set then the result includes hyper <br>parameters from the subproject tasks <br>**Default** : `true` | boolean |
| **page**<br>_optional_ | Page number | integer |
| **page\_size**<br>_optional_ | Page size | integer |
| **project**<br>_required_ | Project ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#responses-5 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-get_hyper_parameters-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **parameters**<br>_optional_ | A list of parameter sections and names | < object > array |
| **remaining**<br>_optional_ | Remaining results | integer |
| **total**<br>_optional_ | Total number of results | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#security-5 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /projects.get\_hyperdataset\_stats [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#post-projectsget_hyperdataset_stats "Direct link to POST /projects.get_hyperdataset_stats")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#description-5 "Direct link to Description")

Internal. Get statistics for hyperdatasets that are direct children of the

passed project

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#parameters-6 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-get_hyperdataset_stats-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **active\_users**<br>_optional_ | Only hyperdatasets created by those users are counted | < string > array |
| **project**<br>_optional_ | Project ID. <pyhocon.config\_tree.NoneValue object at 0x7f68238e82e0>for the <br>Root project | string |
| **tags**<br>_optional_ | Only hyperdatasets with any of those tags counted | < string > array |
| **tags\_filter**<br>_optional_ | Filter on a field that includes combination of 'any' or 'all' included and <br>excluded terms | [tags\_filter](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-get_hyperdataset_stats-post-tags_filter) |

**tags\_filter**

| Name | Description | Schema |
| --- | --- | --- |
| **all**<br>_optional_ | All the terms in 'all' condition are combined with 'and' operation | [all](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-get_hyperdataset_stats-post-tags_filter-all) |
| **any**<br>_optional_ | All the terms in 'any' condition are combined with 'or' operation | [any](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-get_hyperdataset_stats-post-tags_filter-any) |
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

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#responses-6 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-get_hyperdataset_stats-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **stats**<br>_optional_ | Stats for children hyperdatasets | [projects.stats\_datasets](https://clear.ml/docs/latest/docs/references/enterprise/definitions#projectsstats_datasets) |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#security-6 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /projects.get\_hyperparam\_values [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#post-projectsget_hyperparam_values "Direct link to POST /projects.get_hyperparam_values")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#description-6 "Direct link to Description")

Get a list of distinct values for the chosen hyperparameter

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#parameters-7 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-get_hyperparam_values-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **allow\_public**<br>_optional_ | If set to 'true' then collect values from both company and public tasks <br>otherwise company tasks only. The default is 'true' | boolean |
| **include\_subprojects**<br>_optional_ | If set to 'true' and the project field is set then the result includes hyper <br>parameters values from the subproject tasks <br>**Default** : `true` | boolean |
| **name**<br>_required_ | Hyperparameter name | string |
| **page**<br>_optional_ | Page number | integer |
| **page\_size**<br>_optional_ | Page size | integer |
| **pattern**<br>_optional_ | The search pattern regex | string |
| **projects**<br>_optional_ | Project IDs | < string > array |
| **section**<br>_required_ | Hyperparameter section name | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#responses-7 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-get_hyperparam_values-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **total**<br>_optional_ | Total number of distinct parameter values | integer |
| **values**<br>_optional_ | The list of the unique values for the parameter | < string > array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#security-7 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /projects.get\_model\_metadata\_keys [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#post-projectsget_model_metadata_keys "Direct link to POST /projects.get_model_metadata_keys")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#description-7 "Direct link to Description")

Get a list of all metadata keys used in models within the given project.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#parameters-8 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-get_model_metadata_keys-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **include\_subprojects**<br>_optional_ | If set to 'true' and the project field is set then the result includes metadate <br>keys from the subproject models <br>**Default** : `true` | boolean |
| **page**<br>_optional_ | Page number | integer |
| **page\_size**<br>_optional_ | Page size | integer |
| **project**<br>_required_ | Project ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#responses-8 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-get_model_metadata_keys-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **keys**<br>_optional_ | A list of model keys | < string > array |
| **remaining**<br>_optional_ | Remaining results | integer |
| **total**<br>_optional_ | Total number of results | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#security-8 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /projects.get\_model\_metadata\_values [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#post-projectsget_model_metadata_values "Direct link to POST /projects.get_model_metadata_values")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#description-8 "Direct link to Description")

Get a list of distinct values for the chosen model metadata key

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#parameters-9 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-get_model_metadata_values-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **allow\_public**<br>_optional_ | If set to 'true' then collect values from both company and public models <br>otherwise company modeels only. The default is 'true' | boolean |
| **include\_subprojects**<br>_optional_ | If set to 'true' and the project field is set then the result includes metadata <br>values from the subproject models <br>**Default** : `true` | boolean |
| **key**<br>_required_ | Metadata key | string |
| **page**<br>_optional_ | Page number | integer |
| **page\_size**<br>_optional_ | Page size | integer |
| **projects**<br>_optional_ | Project IDs | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#responses-9 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-get_model_metadata_values-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **total**<br>_optional_ | Total number of distinct values | integer |
| **values**<br>_optional_ | The list of the unique values | < string > array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#security-9 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /projects.get\_model\_tags [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#post-projectsget_model_tags "Direct link to POST /projects.get_model_tags")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#description-9 "Direct link to Description")

Get user and system tags used for the models under the specified projects

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#parameters-10 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-get_model_tags-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **filter**<br>_optional_ | Filter on entities to collect tags from | [filter](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-get_model_tags-post-filter) |
| **include\_system**<br>_optional_ | If set to 'true' then the list of the system tags is also returned. The default <br>value is 'false' <br>**Default** : `false` | boolean |
| **projects**<br>_optional_ | The list of projects under which the tags are searched. If not passed or empty <br>then all the projects are searched | < string > array |

**filter**

| Name | Description | Schema |
| --- | --- | --- |
| **system\_tags**<br>_optional_ | The list of system tag values to filter by. Use 'null' value to specify empty <br>system tags. Use '\_\_Snot' value to specify that the following value should be <br>excluded | < string > array |
| **tags**<br>_optional_ | The list of tag values to filter by. Use 'null' value to specify empty tags. <br>Use '\_\_Snot' value to specify that the following value should be excluded | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#responses-10 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-get_model_tags-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **system\_tags**<br>_optional_ | The list of unique system tag values. Returned only if 'include\_system' is set <br>to 'true' in the request | < string > array |
| **tags**<br>_optional_ | The list of unique tag values | < string > array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#security-10 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /projects.get\_project\_tags [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#post-projectsget_project_tags "Direct link to POST /projects.get_project_tags")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#description-10 "Direct link to Description")

Get user and system tags used for the specified projects and their children

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#parameters-11 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-get_project_tags-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **filter**<br>_optional_ | Filter on entities to collect tags from | [filter](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-get_project_tags-post-filter) |
| **include\_system**<br>_optional_ | If set to 'true' then the list of the system tags is also returned. The default <br>value is 'false' <br>**Default** : `false` | boolean |
| **projects**<br>_optional_ | The list of projects under which the tags are searched. If not passed or empty <br>then all the projects are searched | < string > array |

**filter**

| Name | Description | Schema |
| --- | --- | --- |
| **system\_tags**<br>_optional_ | The list of system tag values to filter by. Use 'null' value to specify empty <br>system tags. Use '\_\_Snot' value to specify that the following value should be <br>excluded | < string > array |
| **tags**<br>_optional_ | The list of tag values to filter by. Use 'null' value to specify empty tags. <br>Use '\_\_Snot' value to specify that the following value should be excluded | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#responses-11 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-get_project_tags-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **system\_tags**<br>_optional_ | The list of unique system tag values. Returned only if 'include\_system' is set <br>to 'true' in the request | < string > array |
| **tags**<br>_optional_ | The list of unique tag values | < string > array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#security-11 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /projects.get\_task\_parents [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#post-projectsget_task_parents "Direct link to POST /projects.get_task_parents")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#description-11 "Direct link to Description")

Get unique parent tasks for the tasks in the specified projects

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#parameters-12 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-get_task_parents-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **include\_subprojects**<br>_optional_ | If set to 'true' and the projects field is not empty then the result includes <br>tasks parents from the subproject tasks <br>**Default** : `true` | boolean |
| **projects**<br>_optional_ | The list of projects which task parents are retieved. If not passed or empty <br>then all the projects are searched | < string > array |
| **task\_name**<br>_optional_ | Task name pattern for the returned parent tasks | string |
| **tasks\_state**<br>_optional_ | Return parents for tasks in the specified state. If Null is provided, parents <br>for all task states will be returned. <br>**Default** : `"active"` | enum (active, archived) |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#responses-12 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-get_task_parents-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **parents**<br>_optional_ | The list of unique task parents sorted by their names | < [parents](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-get_task_parents-post-parents) \> array |

**parents**

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_optional_ | The ID of the parent task | string |
| **name**<br>_optional_ | The name of the parent task | string |
| **project**<br>_optional_ |  | [project](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-get_task_parents-post-parents-project) |

**project**

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_optional_ | The ID of the parent task project | string |
| **name**<br>_optional_ | The name of the parent task project | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#security-12 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /projects.get\_task\_tags [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#post-projectsget_task_tags "Direct link to POST /projects.get_task_tags")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#description-12 "Direct link to Description")

Get user and system tags used for the tasks under the specified projects

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#parameters-13 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-get_task_tags-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **filter**<br>_optional_ | Filter on entities to collect tags from | [filter](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-get_task_tags-post-filter) |
| **include\_system**<br>_optional_ | If set to 'true' then the list of the system tags is also returned. The default <br>value is 'false' <br>**Default** : `false` | boolean |
| **projects**<br>_optional_ | The list of projects under which the tags are searched. If not passed or empty <br>then all the projects are searched | < string > array |

**filter**

| Name | Description | Schema |
| --- | --- | --- |
| **system\_tags**<br>_optional_ | The list of system tag values to filter by. Use 'null' value to specify empty <br>system tags. Use '\_\_Snot' value to specify that the following value should be <br>excluded | < string > array |
| **tags**<br>_optional_ | The list of tag values to filter by. Use 'null' value to specify empty tags. <br>Use '\_\_Snot' value to specify that the following value should be excluded | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#responses-13 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-get_task_tags-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **system\_tags**<br>_optional_ | The list of unique system tag values. Returned only if 'include\_system' is set <br>to 'true' in the request | < string > array |
| **tags**<br>_optional_ | The list of unique tag values | < string > array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#security-13 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /projects.get\_unique\_metric\_variants [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#post-projectsget_unique_metric_variants "Direct link to POST /projects.get_unique_metric_variants")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#description-13 "Direct link to Description")

Get all metric/variant pairs reported for tasks in a specific project. If no

project is specified, metrics/variant paris reported for all tasks will be

returned. If the project does not exist, an empty list will be returned.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#parameters-14 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-get_unique_metric_variants-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **ids**<br>_optional_ | IDs of the tasks or models to get metrics from | < string > array |
| **include\_subprojects**<br>_optional_ | If set to 'true' and the project field is set then the result includes <br>metrics/variants from the subproject tasks <br>**Default** : `true` | boolean |
| **model\_metrics**<br>_optional_ | If set to Truethen bring unique metric and variant names from the project <br>models otherwise from the project tasks <br>**Default** : `false` | boolean |
| **project**<br>_optional_ | Project ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#responses-14 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-get_unique_metric_variants-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **metrics**<br>_optional_ | A list of metric variants reported for tasks in this project | < [projects.metric\_variant\_result](https://clear.ml/docs/latest/docs/references/enterprise/definitions#projectsmetric_variant_result) \> array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#security-14 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /projects.get\_user\_names [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#post-projectsget_user_names "Direct link to POST /projects.get_user_names")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#description-14 "Direct link to Description")

Get names and ids of the users who created child entitites under the passed

projects

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#parameters-15 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-get_user_names-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **entity**<br>_optional_ | The type of the child entity to look for <br>**Default** : `"task"` | enum (task, model, dataview) |
| **include\_subprojects**<br>_optional_ | If set to 'true' and the projects field is not empty then the result includes <br>user name from the subprojects children <br>**Default** : `true` | boolean |
| **projects**<br>_optional_ | The list of projects. If not passed or empty then all the projects are searched | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#responses-15 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-get_user_names-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **users**<br>_optional_ | The list of users sorted by their names | < [users](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-get_user_names-post-users) \> array |

**users**

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_optional_ | The ID of the user | string |
| **name**<br>_optional_ | The name of the user | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#security-15 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /projects.merge [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#post-projectsmerge "Direct link to POST /projects.merge")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#description-15 "Direct link to Description")

Moves all the source project's contents to the destination project and remove

the source project

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#parameters-16 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-merge-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **destination\_project**<br>_optional_ | The ID of the destination project | string |
| **project**<br>_required_ | Project id | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#responses-16 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-merge-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **moved\_entities**<br>_optional_ | The number of tasks, models and dataviews moved from the merged project into <br>the destination | integer |
| **moved\_projects**<br>_optional_ | The number of child projects moved from the merged project into the destination | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#security-16 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /projects.move [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#post-projectsmove "Direct link to POST /projects.move")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#description-16 "Direct link to Description")

Moves a project and all of its subprojects under the different location

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#parameters-17 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-move-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **new\_location**<br>_optional_ | The name location for the project | string |
| **project**<br>_required_ | Project id | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#responses-17 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-move-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **moved**<br>_optional_ | The number of projects moved | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#security-17 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /projects.update [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#post-projectsupdate "Direct link to POST /projects.update")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#description-17 "Direct link to Description")

Update project information

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#parameters-18 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-update-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **default\_output\_destination**<br>_optional_ | The default output destination URL for new tasks under this project | string |
| **description**<br>_optional_ | Project description | string |
| **name**<br>_optional_ | Project name. Unique within the company. | string |
| **project**<br>_required_ | Project id | string |
| **system\_tags**<br>_optional_ | System tags list. This field is reserved for system use, please don't use it. | < string > array |
| **tags**<br>_optional_ | User-defined tags list | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#responses-18 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-update-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **fields**<br>_optional_ | Updated fields names and values | object |
| **updated**<br>_optional_ | Number of projects updated (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#security-18 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /projects.validate\_delete [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#post-projectsvalidate_delete "Direct link to POST /projects.validate_delete")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#description-18 "Direct link to Description")

Validates that the project existis and can be deleted

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#parameters-19 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-validate_delete-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **project**<br>_required_ | Project ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#responses-19 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/projects/#projects-validate_delete-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **datasets**<br>_optional_ | The total number of non-empty datasets under the project and all its children | integer |
| **dataviews**<br>_optional_ | The total number of dataviews under the project and all its children | integer |
| **hyper\_datasets**<br>_optional_ | The total number of hyper-datasets under the project and all its children | integer |
| **models**<br>_optional_ | The total number of models under the project and all its children | integer |
| **non\_archived\_dataviews**<br>_optional_ | The total number of non-archived dataviews under the project and all its <br>children | integer |
| **non\_archived\_models**<br>_optional_ | The total number of non-archived models under the project and all its children | integer |
| **non\_archived\_reports**<br>_optional_ | The total number of non-archived reports under the project and all its children | integer |
| **non\_archived\_tasks**<br>_optional_ | The total number of non-archived tasks under the project and all its children | integer |
| **pipelines**<br>_optional_ | The total number of pipelines with active controllers under the project and all <br>its children | integer |
| **reports**<br>_optional_ | The total number of reports under the project and all its children | integer |
| **tasks**<br>_optional_ | The total number of tasks under the project and all its children | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/projects/\#security-19 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

- [POST /projects.create](https://clear.ml/docs/latest/docs/references/enterprise/projects/#post-projectscreate)
- [POST /projects.delete](https://clear.ml/docs/latest/docs/references/enterprise/projects/#post-projectsdelete)
- [POST /projects.get\_all](https://clear.ml/docs/latest/docs/references/enterprise/projects/#post-projectsget_all)
- [POST /projects.get\_all\_ex](https://clear.ml/docs/latest/docs/references/enterprise/projects/#post-projectsget_all_ex)
- [POST /projects.get\_by\_id](https://clear.ml/docs/latest/docs/references/enterprise/projects/#post-projectsget_by_id)
- [POST /projects.get\_hyper\_parameters](https://clear.ml/docs/latest/docs/references/enterprise/projects/#post-projectsget_hyper_parameters)
- [POST /projects.get\_hyperdataset\_stats](https://clear.ml/docs/latest/docs/references/enterprise/projects/#post-projectsget_hyperdataset_stats)
- [POST /projects.get\_hyperparam\_values](https://clear.ml/docs/latest/docs/references/enterprise/projects/#post-projectsget_hyperparam_values)
- [POST /projects.get\_model\_metadata\_keys](https://clear.ml/docs/latest/docs/references/enterprise/projects/#post-projectsget_model_metadata_keys)
- [POST /projects.get\_model\_metadata\_values](https://clear.ml/docs/latest/docs/references/enterprise/projects/#post-projectsget_model_metadata_values)
- [POST /projects.get\_model\_tags](https://clear.ml/docs/latest/docs/references/enterprise/projects/#post-projectsget_model_tags)
- [POST /projects.get\_project\_tags](https://clear.ml/docs/latest/docs/references/enterprise/projects/#post-projectsget_project_tags)
- [POST /projects.get\_task\_parents](https://clear.ml/docs/latest/docs/references/enterprise/projects/#post-projectsget_task_parents)
- [POST /projects.get\_task\_tags](https://clear.ml/docs/latest/docs/references/enterprise/projects/#post-projectsget_task_tags)
- [POST /projects.get\_unique\_metric\_variants](https://clear.ml/docs/latest/docs/references/enterprise/projects/#post-projectsget_unique_metric_variants)
- [POST /projects.get\_user\_names](https://clear.ml/docs/latest/docs/references/enterprise/projects/#post-projectsget_user_names)
- [POST /projects.merge](https://clear.ml/docs/latest/docs/references/enterprise/projects/#post-projectsmerge)
- [POST /projects.move](https://clear.ml/docs/latest/docs/references/enterprise/projects/#post-projectsmove)
- [POST /projects.update](https://clear.ml/docs/latest/docs/references/enterprise/projects/#post-projectsupdate)
- [POST /projects.validate\_delete](https://clear.ml/docs/latest/docs/references/enterprise/projects/#post-projectsvalidate_delete)