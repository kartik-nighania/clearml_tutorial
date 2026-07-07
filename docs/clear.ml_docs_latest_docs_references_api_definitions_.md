---
url: "https://clear.ml/docs/latest/docs/references/api/definitions/"
title: "API Definitions | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/api/definitions/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

## Definitions [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#definitions "Direct link to Definitions")

## auth.credential\_key [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#authcredential_key "Direct link to auth.credential_key")

| Name | Description | Schema |
| --- | --- | --- |
| **access\_key**<br>_optional_ |  | string |
| **created**<br>_optional_ |  | string (date-time) |
| **label**<br>_optional_ | Optional credentials label | string |
| **last\_used**<br>_optional_ |  | string (date-time) |
| **last\_used\_from**<br>_optional_ |  | string |

## auth.credentials [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#authcredentials "Direct link to auth.credentials")

| Name | Description | Schema |
| --- | --- | --- |
| **access\_key**<br>_optional_ | Credentials access key | string |
| **label**<br>_optional_ | Optional credentials label | string |
| **secret\_key**<br>_optional_ | Credentials secret key | string |

## auth.role [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#authrole "Direct link to auth.role")

_Type_ : enum (admin, superuser, user, annotator)

## events.debug\_image\_sample\_response [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#eventsdebug_image_sample_response "Direct link to events.debug_image_sample_response")

| Name | Description | Schema |
| --- | --- | --- |
| **event**<br>_optional_ | Debug image event | object |
| **max\_iteration**<br>_optional_ | maximal valid iteration for the variant | integer |
| **min\_iteration**<br>_optional_ | minimal valid iteration for the variant | integer |
| **scroll\_id**<br>_optional_ | Scroll ID to pass to the next calls to get\_debug\_image\_sample or <br>next\_debug\_image\_sample | string |

## events.debug\_images\_response [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#eventsdebug_images_response "Direct link to events.debug_images_response")

| Name | Description | Schema |
| --- | --- | --- |
| **metrics**<br>_optional_ | Debug image events grouped by tasks and iterations | < [events.debug\_images\_response\_task\_metrics](https://clear.ml/docs/latest/docs/references/api/definitions/#events-debug_images_response_task_metrics) \> array |
| **scroll\_id**<br>_optional_ | Scroll ID for getting more results | string |

## events.debug\_images\_response\_task\_metrics [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#eventsdebug_images_response_task_metrics "Direct link to events.debug_images_response_task_metrics")

| Name | Description | Schema |
| --- | --- | --- |
| **iterations**<br>_optional_ |  | < [iterations](https://clear.ml/docs/latest/docs/references/api/definitions/#events-debug_images_response_task_metrics-iterations) \> array |
| **task**<br>_optional_ | Task ID | string |

**iterations**

| Name | Description | Schema |
| --- | --- | --- |
| **events**<br>_optional_ |  | < object > array |
| **iter**<br>_optional_ | Iteration number | integer |

## events.event\_type\_enum [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#eventsevent_type_enum "Direct link to events.event_type_enum")

_Type_ : enum (training\_stats\_scalar, training\_stats\_vector, training\_debug\_image, plot, log)

## events.log\_level\_enum [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#eventslog_level_enum "Direct link to events.log_level_enum")

_Type_ : enum (notset, debug, verbose, info, warn, warning, error, fatal, critical)

## events.metric\_variants [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#eventsmetric_variants "Direct link to events.metric_variants")

| Name | Description | Schema |
| --- | --- | --- |
| **metric**<br>_optional_ | The metric name | string |
| **variants**<br>_optional_ | The names of the metric variants | < string > array |

## events.metrics\_image\_event [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#eventsmetrics_image_event "Direct link to events.metrics_image_event")

An image or video was dumped to storage for debugging

| Name | Description | Schema |
| --- | --- | --- |
| **iter**<br>_optional_ | Iteration | integer |
| **key**<br>_optional_ | File key | string |
| **metric**<br>_optional_ | Metric name, e.g. 'count', 'loss', 'accuracy' | string |
| **task**<br>_required_ | Task ID (required) | string |
| **timestamp**<br>_optional_ | Epoch milliseconds UTC, will be set by the server if not set. | number |
| **type**<br>_required_ | 'training\_debug\_image' | string |
| **url**<br>_optional_ | File URL | string |
| **variant**<br>_optional_ | E.g. 'class\_1', 'total', 'average | string |

## events.metrics\_plot\_event [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#eventsmetrics_plot_event "Direct link to events.metrics_plot_event")

An entire plot (not single datapoint) and it's layout. Used for plotting ROC

curves, confidence matrices, etc. when evaluating the net.

| Name | Description | Schema |
| --- | --- | --- |
| **iter**<br>_optional_ | Iteration | integer |
| **metric**<br>_optional_ | Metric name, e.g. 'count', 'loss', 'accuracy' | string |
| **plot\_str**<br>_optional_ | An entire plot (not single datapoint) and it's layout. Used for plotting ROC <br>curves, confidence matrices, etc. when evaluating the net. | string |
| **skip\_validation**<br>_optional_ | If set then plot\_str is not checked for a valid json. The default is False | boolean |
| **task**<br>_required_ | Task ID (required) | string |
| **timestamp**<br>_optional_ | Epoch milliseconds UTC, will be set by the server if not set. | number |
| **type**<br>_required_ | 'plot' | string |
| **variant**<br>_optional_ | E.g. 'class\_1', 'total', 'average | string |

## events.metrics\_scalar\_event [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#eventsmetrics_scalar_event "Direct link to events.metrics_scalar_event")

Used for reporting scalar metrics during training task

| Name | Description | Schema |
| --- | --- | --- |
| **iter**<br>_optional_ | Iteration | integer |
| **metric**<br>_optional_ | Metric name, e.g. 'count', 'loss', 'accuracy' | string |
| **task**<br>_required_ | Task ID (required) | string |
| **timestamp**<br>_optional_ | Epoch milliseconds UTC, will be set by the server if not set. | number |
| **type**<br>_required_ | 'training\_stats\_scalar' | string |
| **value**<br>_optional_ |  | number |
| **variant**<br>_optional_ | E.g. 'class\_1', 'total', 'average' | string |
| **x\_axis\_label**<br>_optional_ | Custom X-Axis label to be used when displaying the scalars histogram | string |

## events.metrics\_vector\_event [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#eventsmetrics_vector_event "Direct link to events.metrics_vector_event")

Used for reporting vector metrics during training task

| Name | Description | Schema |
| --- | --- | --- |
| **iter**<br>_optional_ | Iteration | integer |
| **metric**<br>_optional_ | Metric name, e.g. 'count', 'loss', 'accuracy' | string |
| **task**<br>_required_ | Task ID (required) | string |
| **timestamp**<br>_optional_ | Epoch milliseconds UTC, will be set by the server if not set. | number |
| **type**<br>_optional_ | 'training\_stats\_vector' | string |
| **values**<br>_optional_ | vector of float values | < number > array |
| **variant**<br>_optional_ | E.g. 'class\_1', 'total', 'average | string |

## events.plot\_sample\_response [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#eventsplot_sample_response "Direct link to events.plot_sample_response")

| Name | Description | Schema |
| --- | --- | --- |
| **events**<br>_optional_ | Plot events | < object > array |
| **max\_iteration**<br>_optional_ | maximal valid iteration for the metric | integer |
| **min\_iteration**<br>_optional_ | minimal valid iteration for the metric | integer |
| **scroll\_id**<br>_optional_ | Scroll ID to pass to the next calls to get\_plot\_sample or next\_plot\_sample | string |

## events.plots\_response [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#eventsplots_response "Direct link to events.plots_response")

| Name | Description | Schema |
| --- | --- | --- |
| **metrics**<br>_optional_ | Plot events grouped by tasks and iterations | < [events.plots\_response\_task\_metrics](https://clear.ml/docs/latest/docs/references/api/definitions/#events-plots_response_task_metrics) \> array |
| **scroll\_id**<br>_optional_ | Scroll ID for getting more results | string |

## events.plots\_response\_task\_metrics [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#eventsplots_response_task_metrics "Direct link to events.plots_response_task_metrics")

| Name | Description | Schema |
| --- | --- | --- |
| **iterations**<br>_optional_ |  | < [iterations](https://clear.ml/docs/latest/docs/references/api/definitions/#events-plots_response_task_metrics-iterations) \> array |
| **task**<br>_optional_ | Task ID | string |

**iterations**

| Name | Description | Schema |
| --- | --- | --- |
| **events**<br>_optional_ |  | < object > array |
| **iter**<br>_optional_ | Iteration number | integer |

## events.scalar\_key\_enum [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#eventsscalar_key_enum "Direct link to events.scalar_key_enum")

_Type_ : enum (iter, timestamp, iso\_time)

## events.single\_value\_metrics\_response [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#eventssingle_value_metrics_response "Direct link to events.single_value_metrics_response")

| Name | Description | Schema |
| --- | --- | --- |
| **tasks**<br>_optional_ | Single value metrics grouped by task | < [events.single\_value\_task\_metrics](https://clear.ml/docs/latest/docs/references/api/definitions/#events-single_value_task_metrics) \> array |

## events.single\_value\_task\_metrics [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#eventssingle_value_task_metrics "Direct link to events.single_value_task_metrics")

| Name | Description | Schema |
| --- | --- | --- |
| **task**<br>_optional_ | Task ID | string |
| **task\_name**<br>_optional_ | Task name | string |
| **values**<br>_optional_ |  | < [values](https://clear.ml/docs/latest/docs/references/api/definitions/#events-single_value_task_metrics-values) \> array |

**values**

| Name | Schema |
| --- | --- |
| **metric**<br>_optional_ | string |
| **timestamp**<br>_optional_ | number |
| **value**<br>_optional_ | number |
| **variant**<br>_optional_ | string |

## events.task\_log\_event [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#eventstask_log_event "Direct link to events.task_log_event")

A log event associated with a task.

| Name | Description | Schema |
| --- | --- | --- |
| **level**<br>_optional_ | Log level. | [events.log\_level\_enum](https://clear.ml/docs/latest/docs/references/api/definitions/#events-log_level_enum) |
| **msg**<br>_optional_ | Log message. | string |
| **task**<br>_required_ | Task ID (required) | string |
| **timestamp**<br>_optional_ | Epoch milliseconds UTC, will be set by the server if not set. | number |
| **type**<br>_required_ | 'log' | string |
| **worker**<br>_optional_ | Name of machine running the task. | string |

## events.task\_metric [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#eventstask_metric "Direct link to events.task_metric")

| Name | Description | Schema |
| --- | --- | --- |
| **metric**<br>_optional_ | Metric name | string |
| **task**<br>_required_ | Task ID | string |

## events.task\_metric\_variants [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#eventstask_metric_variants "Direct link to events.task_metric_variants")

| Name | Description | Schema |
| --- | --- | --- |
| **metric**<br>_optional_ | Metric name | string |
| **task**<br>_required_ | Task ID | string |
| **variants**<br>_optional_ | Metric variant names | < string > array |

## models.last\_metrics\_event [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#modelslast_metrics_event "Direct link to models.last_metrics_event")

| Name | Description | Schema |
| --- | --- | --- |
| **count**<br>_optional_ | The total count of reported values | integer |
| **first\_value**<br>_optional_ | First value reported | number |
| **first\_value\_iteration**<br>_optional_ | The iteration at which the first value was reported | integer |
| **max\_value**<br>_optional_ | Maximum value reported | number |
| **max\_value\_iteration**<br>_optional_ | The iteration at which the maximum value was reported | integer |
| **mean\_value**<br>_optional_ | The mean value | number |
| **metric**<br>_optional_ | Metric name | string |
| **min\_value**<br>_optional_ | Minimum value reported | number |
| **min\_value\_iteration**<br>_optional_ | The iteration at which the minimum value was reported | integer |
| **value**<br>_optional_ | Last value reported | number |
| **variant**<br>_optional_ | Variant name | string |
| **x\_axis\_label**<br>_optional_ | The user defined value for the X-Axis name stored with the event | string |

## models.last\_metrics\_variants [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#modelslast_metrics_variants "Direct link to models.last_metrics_variants")

Last metric events, one for each variant hash

_Type_ : < string, [models.last\_metrics\_event](https://clear.ml/docs/latest/docs/references/api/definitions/#models-last_metrics_event) \> map

## models.metadata\_item [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#modelsmetadata_item "Direct link to models.metadata_item")

| Name | Description | Schema |
| --- | --- | --- |
| **key**<br>_optional_ | The key uniquely identifying the metadata item inside the given entity | string |
| **type**<br>_optional_ | The type of the metadata item | string |
| **value**<br>_optional_ | The value stored in the metadata item | string |

## models.model [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#modelsmodel "Direct link to models.model")

| Name | Description | Schema |
| --- | --- | --- |
| **comment**<br>_optional_ | Model comment | string |
| **company**<br>_optional_ | Company id | string |
| **created**<br>_optional_ | Model creation time | string (date-time) |
| **design**<br>_optional_ | Json object representing the model design. Should be identical to the network <br>design of the task which created the model | object |
| **framework**<br>_optional_ | Framework on which the model is based. Should be identical to the framework of <br>the task which created the model | string |
| **id**<br>_optional_ | Model id | string |
| **labels**<br>_optional_ | Json object representing the ids of the labels in the model. The keys are the <br>layers' names and the values are the ids. | < string, integer > map |
| **last\_iteration**<br>_optional_ | Last iteration reported for this model | integer |
| **last\_metrics**<br>_optional_ | Last metric variants (hash to events), one for each metric hash | < string, [models.last\_metrics\_variants](https://clear.ml/docs/latest/docs/references/api/definitions/#models-last_metrics_variants) \> map |
| **last\_update**<br>_optional_ | Model last update time | string (date-time) |
| **metadata**<br>_optional_ | Model metadata | < string, [models.metadata\_item](https://clear.ml/docs/latest/docs/references/api/definitions/#models-metadata_item) \> map |
| **name**<br>_optional_ | Model name | string |
| **parent**<br>_optional_ | Parent model ID | string |
| **project**<br>_optional_ | Associated project ID | string |
| **ready**<br>_optional_ | Indication if the model is final and can be used by other tasks | boolean |
| **stats**<br>_optional_ | Model statistics | [stats](https://clear.ml/docs/latest/docs/references/api/definitions/#models-model-stats) |
| **system\_tags**<br>_optional_ | System tags. This field is reserved for system use, please don't use it. | < string > array |
| **tags**<br>_optional_ | User-defined tags | < string > array |
| **task**<br>_optional_ | Task ID of task in which the model was created | string |
| **ui\_cache**<br>_optional_ | UI cache for this model | object |
| **uri**<br>_optional_ | URI for the model, pointing to the destination storage. | string |
| **user**<br>_optional_ | Associated user id | string |

**stats**

| Name | Description | Schema |
| --- | --- | --- |
| **labels\_count**<br>_optional_ | Number of the model labels | integer |

## models.multi\_field\_pattern\_data [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#modelsmulti_field_pattern_data "Direct link to models.multi_field_pattern_data")

| Name | Description | Schema |
| --- | --- | --- |
| **datetime**<br>_optional_ | Date time conditions (applicable only to datetime fields). Either 'pattern' or <br>'datetime' should be specified | string |
| **fields**<br>_optional_ | List of field names | < string > array |
| **pattern**<br>_optional_ | Pattern string (regex). Either 'pattern' or 'datetime' should be specified | string |

## organization.field\_mapping [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#organizationfield_mapping "Direct link to organization.field_mapping")

| Name | Description | Schema |
| --- | --- | --- |
| **field**<br>_required_ | The source field name as specified in the only\_fields | string |
| **name**<br>_optional_ | The column name in the exported csv file | string |
| **values**<br>_optional_ |  | < [organization.value\_mapping](https://clear.ml/docs/latest/docs/references/api/definitions/#organization-value_mapping) \> array |

## organization.value\_mapping [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#organizationvalue_mapping "Direct link to organization.value_mapping")

| Name | Description | Schema |
| --- | --- | --- |
| **key**<br>_required_ | Original value | object |
| **value**<br>_required_ | Translated value | object |

## organization.workloads [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#organizationworkloads "Direct link to organization.workloads")

| Name | Schema |
| --- | --- |
| **series**<br>_optional_ | < [series](https://clear.ml/docs/latest/docs/references/api/definitions/#organization-workloads-series) \> array |
| **total**<br>_optional_ | < [total](https://clear.ml/docs/latest/docs/references/api/definitions/#organization-workloads-total) \> array |

**series**

| Name | Description | Schema |
| --- | --- | --- |
| **cpu\_usage**<br>_optional_ | Tasks running task multiplied by cpu resource | < number > array |
| **cpu\_usage\_artifical\_weights**<br>_optional_ | Indicate whether artificial cpu resource weights were used | boolean |
| **dates**<br>_optional_ | Date timestamp in seconds | < number > array |
| **duration**<br>_optional_ | Tasks running time in seconds | < number > array |
| **gpu\_usage**<br>_optional_ | Tasks running task multiplied by gpu resource | < number > array |
| **gpu\_usage\_artifical\_weights**<br>_optional_ | Indicate whether artificial gpu resource weights were used | boolean |
| **id**<br>_optional_ |  | string |
| **name**<br>_optional_ |  | string |

**total**

| Name | Description | Schema |
| --- | --- | --- |
| **cpu\_artificial\_weights**<br>_optional_ | Indicate whether artificial cpu resource weights were used | boolean |
| **cpu\_usage**<br>_optional_ | Tasks running task multiplied by cpu resource | number |
| **duration**<br>_optional_ | Tasks running time in seconds | integer |
| **gpu\_artificial\_weights**<br>_optional_ | Indicate whether artificial gpu resource weights were used | boolean |
| **gpu\_usage**<br>_optional_ | Tasks running task multiplied by gpu resource | number |
| **id**<br>_optional_ |  | string |
| **name**<br>_optional_ |  | string |

## projects.metric\_variant\_result [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#projectsmetric_variant_result "Direct link to projects.metric_variant_result")

| Name | Description | Schema |
| --- | --- | --- |
| **metric**<br>_optional_ | Metric name | string |
| **metric\_hash**<br>_optional_ | Metric name hash. Used instead of the metric name when categorizing last <br>metrics events in task objects. | string |
| **variant**<br>_optional_ | Variant name | string |
| **variant\_hash**<br>_optional_ | Variant name hash. Used instead of the variant name when categorizing last <br>metrics events in task objects. | string |

## projects.multi\_field\_pattern\_data [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#projectsmulti_field_pattern_data "Direct link to projects.multi_field_pattern_data")

| Name | Description | Schema |
| --- | --- | --- |
| **datetime**<br>_optional_ | Date time conditions (applicable only to datetime fields). Either 'pattern' or <br>'datetime' should be specified | string |
| **fields**<br>_optional_ | List of field names | < string > array |
| **pattern**<br>_optional_ | Pattern string (regex). Either 'pattern' or 'datetime' should be specified | string |

## projects.project [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#projectsproject "Direct link to projects.project")

| Name | Description | Schema |
| --- | --- | --- |
| **basename**<br>_optional_ | Project base name | string |
| **company**<br>_optional_ | Company id | string |
| **created**<br>_optional_ | Creation time | string (date-time) |
| **default\_output\_destination**<br>_optional_ | The default output destination URL for new tasks under this project | string |
| **description**<br>_optional_ | Project description | string |
| **id**<br>_optional_ | Project id | string |
| **last\_update**<br>_optional_ | Last project update time. Reflects the last time the project metadata was <br>changed or a task in this project has changed status | string (date-time) |
| **name**<br>_optional_ | Project name | string |
| **system\_tags**<br>_optional_ | System tags. This field is reserved for system use, please don't use it. | < string > array |
| **tags**<br>_optional_ | User-defined tags | < string > array |
| **user**<br>_optional_ | Associated user id | string |

## projects.projects\_get\_all\_response\_single [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#projectsprojects_get_all_response_single "Direct link to projects.projects_get_all_response_single")

| Name | Description | Schema |
| --- | --- | --- |
| **basename**<br>_optional_ | Project base name | string |
| **company**<br>_optional_ | Company id | string |
| **created**<br>_optional_ | Creation time | string (date-time) |
| **dataset\_stats**<br>_optional_ | Project dataset statistics | [dataset\_stats](https://clear.ml/docs/latest/docs/references/api/definitions/#projects-projects_get_all_response_single-dataset_stats) |
| **default\_output\_destination**<br>_optional_ | The default output destination URL for new tasks under this project | string |
| **description**<br>_optional_ | Project description | string |
| **hidden**<br>_optional_ | Returned if the search\_hidden flag was specified in the get\_all\_ex call and the <br>project is hidden | boolean |
| **id**<br>_optional_ | Project id | string |
| **last\_update**<br>_optional_ | Last project update time. Reflects the last time the project metadata was <br>changed or a task in this project has changed status | string (date-time) |
| **name**<br>_optional_ | Project name | string |
| **own\_datasets**<br>_optional_ | The amount of datasets/hyperdatasers under this project (without children <br>projects). Returned if 'check\_own\_contents' flag is set in the request and <br>children\_type is set to 'dataset' or 'hyperdataset' | integer |
| **own\_models**<br>_optional_ | The amount of models under this project (without children projects). Returned <br>if 'check\_own\_contents' flag is set in the request | integer |
| **own\_tasks**<br>_optional_ | The amount of tasks under this project (without children projects). Returned if <br>'check\_own\_contents' flag is set in the request | integer |
| **stats**<br>_optional_ | Additional project stats | [projects.stats](https://clear.ml/docs/latest/docs/references/api/definitions/#projects-stats) |
| **sub\_projects**<br>_optional_ | The list of sub projects | < [sub\_projects](https://clear.ml/docs/latest/docs/references/api/definitions/#projects-projects_get_all_response_single-sub_projects) \> array |
| **system\_tags**<br>_optional_ | System tags. This field is reserved for system use, please don't use it. | < string > array |
| **tags**<br>_optional_ | User-defined tags | < string > array |
| **user**<br>_optional_ | Associated user id | string |

**dataset\_stats**

| Name | Description | Schema |
| --- | --- | --- |
| **file\_count**<br>_optional_ | The number of files stored in the dataset | integer |
| **total\_size**<br>_optional_ | The total dataset size in bytes | integer |

**sub\_projects**

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_optional_ | Subproject ID | string |
| **name**<br>_optional_ | Subproject name | string |

## projects.stats [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#projectsstats "Direct link to projects.stats")

| Name | Description | Schema |
| --- | --- | --- |
| **active**<br>_optional_ | Stats for active tasks | [projects.stats\_status\_count](https://clear.ml/docs/latest/docs/references/api/definitions/#projects-stats_status_count) |
| **archived**<br>_optional_ | Stats for archived tasks | [projects.stats\_status\_count](https://clear.ml/docs/latest/docs/references/api/definitions/#projects-stats_status_count) |
| **datasets**<br>_optional_ | Stats for childrent datasets | [projects.stats\_datasets](https://clear.ml/docs/latest/docs/references/api/definitions/#projects-stats_datasets) |

## projects.stats\_datasets [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#projectsstats_datasets "Direct link to projects.stats_datasets")

| Name | Description | Schema |
| --- | --- | --- |
| **count**<br>_optional_ | Number of datasets | integer |
| **tags**<br>_optional_ | Dataset tags | < string > array |

## projects.stats\_status\_count [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#projectsstats_status_count "Direct link to projects.stats_status_count")

| Name | Description | Schema |
| --- | --- | --- |
| **completed\_tasks\_24h**<br>_optional_ | Number of tasks completed in the last 24 hours | integer |
| **last\_task\_run**<br>_optional_ | The most recent started time of a task | integer |
| **status\_count**<br>_optional_ | Status counts | [status\_count](https://clear.ml/docs/latest/docs/references/api/definitions/#projects-stats_status_count-status_count) |
| **total\_runtime**<br>_optional_ | Total run time of all tasks in project (in seconds) | integer |
| **total\_tasks**<br>_optional_ | Number of tasks | integer |

**status\_count**

| Name | Description | Schema |
| --- | --- | --- |
| **closed**<br>_optional_ | Number of 'closed' tasks in project | integer |
| **completed**<br>_optional_ | Number of 'completed' tasks in project | integer |
| **created**<br>_optional_ | Number of 'created' tasks in project | integer |
| **failed**<br>_optional_ | Number of 'failed' tasks in project | integer |
| **in\_progress**<br>_optional_ | Number of 'in\_progress' tasks in project | integer |
| **published**<br>_optional_ | Number of 'published' tasks in project | integer |
| **queued**<br>_optional_ | Number of 'queued' tasks in project | integer |
| **stopped**<br>_optional_ | Number of 'stopped' tasks in project | integer |
| **unknown**<br>_optional_ | Number of 'unknown' tasks in project | integer |

## projects.urls [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#projectsurls "Direct link to projects.urls")

| Name | Schema |
| --- | --- |
| **artifact\_urls**<br>_optional_ | < string > array |
| **event\_urls**<br>_optional_ | < string > array |
| **model\_urls**<br>_optional_ | < string > array |

## queues.entry [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#queuesentry "Direct link to queues.entry")

| Name | Description | Schema |
| --- | --- | --- |
| **added**<br>_optional_ | Time this entry was added to the queue | string (date-time) |
| **task**<br>_optional_ | Queued task ID | string |

## queues.metadata\_item [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#queuesmetadata_item "Direct link to queues.metadata_item")

| Name | Description | Schema |
| --- | --- | --- |
| **key**<br>_optional_ | The key uniquely identifying the metadata item inside the given entity | string |
| **type**<br>_optional_ | The type of the metadata item | string |
| **value**<br>_optional_ | The value stored in the metadata item | string |

## queues.queue [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#queuesqueue "Direct link to queues.queue")

| Name | Description | Schema |
| --- | --- | --- |
| **company**<br>_optional_ | Company id | string |
| **created**<br>_optional_ | Queue creation time | string (date-time) |
| **display\_name**<br>_optional_ | Display name | string |
| **entries**<br>_optional_ | List of ordered queue entries | < [queues.entry](https://clear.ml/docs/latest/docs/references/api/definitions/#queues-entry) \> array |
| **id**<br>_optional_ | Queue id | string |
| **metadata**<br>_optional_ | Queue metadata | < string, [queues.metadata\_item](https://clear.ml/docs/latest/docs/references/api/definitions/#queues-metadata_item) \> map |
| **name**<br>_optional_ | Queue name | string |
| **system\_tags**<br>_optional_ | System tags. This field is reserved for system use, please don't use it. | < string > array |
| **tags**<br>_optional_ | User-defined tags | < string > array |
| **user**<br>_optional_ | Associated user id | string |

## queues.queue\_metrics [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#queuesqueue_metrics "Direct link to queues.queue_metrics")

| Name | Description | Schema |
| --- | --- | --- |
| **avg\_waiting\_times**<br>_optional_ | List of average waiting times for tasks in the queue. The points correspond to <br>the timestamps in the dates list. If more than one value exists for the given <br>interval then the maximum value is taken. | < number > array |
| **dates**<br>_optional_ | List of timestamps (in seconds from epoch) in the acceding order. The <br>timestamps are separated by the requested interval. Timestamps where no queue <br>status change was recorded are omitted. | < integer > array |
| **queue**<br>_optional_ | ID of the queue | string |
| **queue\_lengths**<br>_optional_ | List of tasks counts in the queue. The points correspond to the timestamps in <br>the dates list. If more than one value exists for the given interval then the <br>count that corresponds to the maximum average value is taken. | < integer > array |

## reports.artifact [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#reportsartifact "Direct link to reports.artifact")

| Name | Description | Schema |
| --- | --- | --- |
| **content\_size**<br>_optional_ | Raw data length in bytes | integer |
| **display\_data**<br>_optional_ | User-defined list of key/value pairs, sorted | < < string > array > array |
| **hash**<br>_optional_ | Hash of entire raw data | string |
| **key**<br>_required_ | Entry key | string |
| **mode**<br>_optional_ | System defined input/output indication | [reports.artifact\_mode\_enum](https://clear.ml/docs/latest/docs/references/api/definitions/#reports-artifact_mode_enum) |
| **timestamp**<br>_optional_ | Epoch time when artifact was created | integer |
| **type**<br>_required_ | System defined type | string |
| **type\_data**<br>_optional_ | Additional fields defined by the system | [reports.artifact\_type\_data](https://clear.ml/docs/latest/docs/references/api/definitions/#reports-artifact_type_data) |
| **uri**<br>_optional_ | Raw data location | string |

## reports.artifact\_mode\_enum [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#reportsartifact_mode_enum "Direct link to reports.artifact_mode_enum")

_Type_ : enum (input, output)

## reports.artifact\_type\_data [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#reportsartifact_type_data "Direct link to reports.artifact_type_data")

| Name | Description | Schema |
| --- | --- | --- |
| **content\_type**<br>_optional_ | System defined raw data content type | string |
| **data\_hash**<br>_optional_ | Hash of raw data, without any headers or descriptive parts | string |
| **preview**<br>_optional_ | Description or textual data | string |

## reports.configuration\_item [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#reportsconfiguration_item "Direct link to reports.configuration_item")

| Name | Description | Schema |
| --- | --- | --- |
| **description**<br>_optional_ | The parameter description. Optional | string |
| **name**<br>_optional_ | Name of the parameter. Should be unique | string |
| **type**<br>_optional_ | Type of the parameter. Optional | string |
| **value**<br>_optional_ | Value of the parameter | string |

## reports.debug\_images\_response\_task\_metrics [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#reportsdebug_images_response_task_metrics "Direct link to reports.debug_images_response_task_metrics")

| Name | Description | Schema |
| --- | --- | --- |
| **iterations**<br>_optional_ |  | < [iterations](https://clear.ml/docs/latest/docs/references/api/definitions/#reports-debug_images_response_task_metrics-iterations) \> array |
| **task**<br>_optional_ | Task ID | string |

**iterations**

| Name | Description | Schema |
| --- | --- | --- |
| **events**<br>_optional_ |  | < object > array |
| **iter**<br>_optional_ | Iteration number | integer |

## reports.execution [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#reportsexecution "Direct link to reports.execution")

| Name | Description | Schema |
| --- | --- | --- |
| **artifacts**<br>_optional_ | Task artifacts | < [reports.artifact](https://clear.ml/docs/latest/docs/references/api/definitions/#reports-artifact) \> array |
| **docker\_cmd**<br>_optional_ | Command for running docker script for the execution of the task | string |
| **framework**<br>_optional_ | Framework related to the task. Case insensitive. Mandatory for Training tasks. | string |
| **model**<br>_optional_ | Execution input model ID Not applicable for Register (Import) tasks | string |
| **model\_desc**<br>_optional_ | Json object representing the Model descriptors | object |
| **model\_labels**<br>_optional_ | Json object representing the ids of the labels in the model. The keys are the <br>layers' names and the values are the IDs. Not applicable for Register (Import) <br>tasks. Mandatory for Training tasks | < string, integer > map |
| **parameters**<br>_optional_ | Json object containing the Task parameters | object |
| **queue**<br>_optional_ | Queue ID where task was queued. | string |

## reports.last\_metrics\_event [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#reportslast_metrics_event "Direct link to reports.last_metrics_event")

| Name | Description | Schema |
| --- | --- | --- |
| **count**<br>_optional_ | The total count of reported values | integer |
| **first\_value**<br>_optional_ | First value reported | number |
| **first\_value\_iteration**<br>_optional_ | The iteration at which the first value was reported | integer |
| **max\_value**<br>_optional_ | Maximum value reported | number |
| **max\_value\_iteration**<br>_optional_ | The iteration at which the maximum value was reported | integer |
| **mean\_value**<br>_optional_ | The mean value | number |
| **metric**<br>_optional_ | Metric name | string |
| **min\_value**<br>_optional_ | Minimum value reported | number |
| **min\_value\_iteration**<br>_optional_ | The iteration at which the minimum value was reported | integer |
| **value**<br>_optional_ | Last value reported | number |
| **variant**<br>_optional_ | Variant name | string |
| **x\_axis\_label**<br>_optional_ | The user defined value for the X-Axis name stored with the event | string |

## reports.last\_metrics\_variants [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#reportslast_metrics_variants "Direct link to reports.last_metrics_variants")

Last metric events, one for each variant hash

_Type_ : < string, [reports.last\_metrics\_event](https://clear.ml/docs/latest/docs/references/api/definitions/#reports-last_metrics_event) \> map

## reports.metric\_variants [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#reportsmetric_variants "Direct link to reports.metric_variants")

| Name | Description | Schema |
| --- | --- | --- |
| **metric**<br>_optional_ | The metric name | string |
| **variants**<br>_optional_ | The names of the metric variants | < string > array |

## reports.multi\_field\_pattern\_data [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#reportsmulti_field_pattern_data "Direct link to reports.multi_field_pattern_data")

| Name | Description | Schema |
| --- | --- | --- |
| **datetime**<br>_optional_ | Date time conditions (applicable only to datetime fields). Either 'pattern' or <br>'datetime' should be specified | string |
| **fields**<br>_optional_ | List of field names | < string > array |
| **pattern**<br>_optional_ | Pattern string (regex). Either 'pattern' or 'datetime' should be specified | string |

## reports.output [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#reportsoutput "Direct link to reports.output")

| Name | Description | Schema |
| --- | --- | --- |
| **destination**<br>_optional_ | Storage id. This is where output files will be stored. | string |
| **error**<br>_optional_ | Last error text | string |
| **model**<br>_optional_ | Model id. | string |
| **result**<br>_optional_ | Task result. Values: 'success', 'failure' | string |

## reports.params\_item [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#reportsparams_item "Direct link to reports.params_item")

| Name | Description | Schema |
| --- | --- | --- |
| **description**<br>_optional_ | The parameter description. Optional | string |
| **name**<br>_optional_ | Name of the parameter. The combination of section and name should be unique | string |
| **section**<br>_optional_ | Section that the parameter belongs to | string |
| **type**<br>_optional_ | Type of the parameter. Optional | string |
| **value**<br>_optional_ | Value of the parameter | string |

## reports.report [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#reportsreport "Direct link to reports.report")

| Name | Description | Schema |
| --- | --- | --- |
| **comment**<br>_optional_ | Free text comment | string |
| **company**<br>_optional_ | Company ID | string |
| **created**<br>_optional_ | Report creation time (UTC) | string (date-time) |
| **id**<br>_optional_ | Report id | string |
| **last\_update**<br>_optional_ | Last time this report was created, edited, changed | string (date-time) |
| **name**<br>_optional_ | Report Name | string |
| **project**<br>_optional_ | Project ID of the project to which this report is assigned | string |
| **published**<br>_optional_ | Report publish time | string (date-time) |
| **report**<br>_optional_ | Report template | string |
| **report\_assets**<br>_optional_ | List of the external report assets | < string > array |
| **status**<br>_optional_ |  | [reports.report\_status\_enum](https://clear.ml/docs/latest/docs/references/api/definitions/#reports-report_status_enum) |
| **status\_changed**<br>_optional_ | Last status change time | string (date-time) |
| **status\_message**<br>_optional_ | free text string representing info about the status | string |
| **status\_reason**<br>_optional_ | Reason for last status change | string |
| **system\_tags**<br>_optional_ | System tags list. This field is reserved for system use, please don't use it. | < string > array |
| **tags**<br>_optional_ | User-defined tags list | < string > array |
| **user**<br>_optional_ | Associated user id | string |

## reports.report\_status\_enum [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#reportsreport_status_enum "Direct link to reports.report_status_enum")

_Type_ : enum (created, published)

## reports.scalar\_key\_enum [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#reportsscalar_key_enum "Direct link to reports.scalar_key_enum")

_Type_ : enum (iter, timestamp, iso\_time)

## reports.script [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#reportsscript "Direct link to reports.script")

| Name | Description | Schema |
| --- | --- | --- |
| **binary**<br>_optional_ | Binary to use when running the script <br>**Default** : `"python"` | string |
| **branch**<br>_optional_ | Repository branch id If not provided and tag not provided, default repository <br>branch is used. | string |
| **diff**<br>_optional_ | Uncommitted changes found in the repository when task was run | string |
| **entry\_point**<br>_optional_ | Path to execute within the repository | string |
| **repository**<br>_optional_ | Name of the repository where the script is located | string |
| **requirements**<br>_optional_ | A JSON object containing requirements strings by key | object |
| **tag**<br>_optional_ | Repository tag | string |
| **version\_num**<br>_optional_ | Version (changeset) number. Optional (default is head version) Unused if tag is <br>provided. | string |
| **working\_dir**<br>_optional_ | Path to the folder from which to run the script Default - root folder of <br>repository | string |

## reports.section\_params [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#reportssection_params "Direct link to reports.section_params")

Task section params

_Type_ : < string, [reports.params\_item](https://clear.ml/docs/latest/docs/references/api/definitions/#reports-params_item) \> map

## reports.single\_value\_task\_metrics [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#reportssingle_value_task_metrics "Direct link to reports.single_value_task_metrics")

| Name | Description | Schema |
| --- | --- | --- |
| **task**<br>_optional_ | Task ID | string |
| **task\_name**<br>_optional_ | Task name | string |
| **values**<br>_optional_ |  | < [values](https://clear.ml/docs/latest/docs/references/api/definitions/#reports-single_value_task_metrics-values) \> array |

**values**

| Name | Schema |
| --- | --- |
| **metric**<br>_optional_ | string |
| **timestamp**<br>_optional_ | number |
| **value**<br>_optional_ | number |
| **variant**<br>_optional_ | string |

## reports.task [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#reportstask "Direct link to reports.task")

| Name | Description | Schema |
| --- | --- | --- |
| **active\_duration**<br>_optional_ | Task duration time (seconds) | integer |
| **comment**<br>_optional_ | Free text comment | string |
| **company**<br>_optional_ | Company ID | string |
| **completed**<br>_optional_ | Task end time (UTC) | string (date-time) |
| **configuration**<br>_optional_ | Task configuration params | < string, [reports.configuration\_item](https://clear.ml/docs/latest/docs/references/api/definitions/#reports-configuration_item) \> map |
| **container**<br>_optional_ | Docker container parameters | < string, string > map |
| **created**<br>_optional_ | Task creation time (UTC) | string (date-time) |
| **execution**<br>_optional_ | Task execution params | [reports.execution](https://clear.ml/docs/latest/docs/references/api/definitions/#reports-execution) |
| **hyperparams**<br>_optional_ | Task hyper params per section | < string, [reports.section\_params](https://clear.ml/docs/latest/docs/references/api/definitions/#reports-section_params) \> map |
| **id**<br>_optional_ | Task id | string |
| **last\_change**<br>_optional_ | Last time any update was done to the task | string (date-time) |
| **last\_iteration**<br>_optional_ | Last iteration reported for this task | integer |
| **last\_metrics**<br>_optional_ | Last metric variants (hash to events), one for each metric hash | < string, [reports.last\_metrics\_variants](https://clear.ml/docs/latest/docs/references/api/definitions/#reports-last_metrics_variants) \> map |
| **last\_update**<br>_optional_ | Last time this task was created, edited, changed or events for this task were <br>reported | string (date-time) |
| **last\_worker**<br>_optional_ | ID of last worker that handled the task | string |
| **last\_worker\_report**<br>_optional_ | Last time a worker reported while working on this task | string (date-time) |
| **models**<br>_optional_ | Task models | [reports.task\_models](https://clear.ml/docs/latest/docs/references/api/definitions/#reports-task_models) |
| **name**<br>_optional_ | Task Name | string |
| **output**<br>_optional_ | Task output params | [reports.output](https://clear.ml/docs/latest/docs/references/api/definitions/#reports-output) |
| **parent**<br>_optional_ | Parent task id | string |
| **project**<br>_optional_ | Project ID of the project to which this task is assigned | string |
| **published**<br>_optional_ | Task publish time | string (date-time) |
| **runtime**<br>_optional_ | Task runtime mapping | object |
| **script**<br>_optional_ | Script info | [reports.script](https://clear.ml/docs/latest/docs/references/api/definitions/#reports-script) |
| **started**<br>_optional_ | Task start time (UTC) | string (date-time) |
| **status**<br>_optional_ |  | [reports.task\_status\_enum](https://clear.ml/docs/latest/docs/references/api/definitions/#reports-task_status_enum) |
| **status\_changed**<br>_optional_ | Last status change time | string (date-time) |
| **status\_message**<br>_optional_ | free text string representing info about the status | string |
| **status\_reason**<br>_optional_ | Reason for last status change | string |
| **system\_tags**<br>_optional_ | System tags list. This field is reserved for system use, please don't use it. | < string > array |
| **tags**<br>_optional_ | User-defined tags list | < string > array |
| **type**<br>_optional_ | Type of task. Values: 'training', 'testing' | [reports.task\_type\_enum](https://clear.ml/docs/latest/docs/references/api/definitions/#reports-task_type_enum) |
| **user**<br>_optional_ | Associated user id | string |

## reports.task\_model\_item [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#reportstask_model_item "Direct link to reports.task_model_item")

| Name | Description | Schema |
| --- | --- | --- |
| **model**<br>_required_ | The model ID | string |
| **name**<br>_required_ | The task model name | string |

## reports.task\_models [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#reportstask_models "Direct link to reports.task_models")

| Name | Description | Schema |
| --- | --- | --- |
| **input**<br>_optional_ | The list of task input models | < [reports.task\_model\_item](https://clear.ml/docs/latest/docs/references/api/definitions/#reports-task_model_item) \> array |
| **output**<br>_optional_ | The list of task output models | < [reports.task\_model\_item](https://clear.ml/docs/latest/docs/references/api/definitions/#reports-task_model_item) \> array |

## reports.task\_status\_enum [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#reportstask_status_enum "Direct link to reports.task_status_enum")

_Type_ : enum (created, queued, in\_progress, stopped, published, publishing, closed, failed, completed, unknown)

## reports.task\_type\_enum [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#reportstask_type_enum "Direct link to reports.task_type_enum")

_Type_ : enum (training, testing, inference, data\_processing, application, monitor, controller, optimizer, service, qc, custom)

## serving.container\_info [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#servingcontainer_info "Direct link to serving.container_info")

| Name | Description | Schema |
| --- | --- | --- |
| **age\_sec**<br>_optional_ | Amount of seconds since the container registration | integer |
| **endpoint**<br>_optional_ | Endpoint name | string |
| **id**<br>_optional_ | Container ID | string |
| **input\_size**<br>_optional_ | Input size | string |
| **input\_type**<br>_optional_ | Input type | string |
| **last\_update**<br>_optional_ | The latest time when the container instance sent update | string (date-time) |
| **model**<br>_optional_ | Model name | string |
| **model\_source**<br>_optional_ | Model source | string |
| **model\_version**<br>_optional_ | Model version | string |
| **preprocess\_artifact**<br>_optional_ | Preprocess Artifact | string |
| **uptime\_sec**<br>_optional_ | Model instance uptime in seconds | integer |
| **url**<br>_optional_ | Model url | string |

## serving.container\_instance\_stats [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#servingcontainer_instance_stats "Direct link to serving.container_instance_stats")

| Name | Description | Schema |
| --- | --- | --- |
| **cpu\_count**<br>_optional_ | CPU Count | integer |
| **gpu\_count**<br>_optional_ | GPU Count | integer |
| **id**<br>_optional_ | Container ID | string |
| **last\_update**<br>_optional_ | The latest time when the container instance sent update | string (date-time) |
| **latency\_ms**<br>_optional_ | Average request latency in ms | integer |
| **reference**<br>_optional_ | Array of reference items provided by the container instance. Can contain <br>multiple reference items with the same type | < [reference](https://clear.ml/docs/latest/docs/references/api/definitions/#serving-container_instance_stats-reference) \> array |
| **requests**<br>_optional_ | Number of requests | integer |
| **requests\_min**<br>_optional_ | Average requests per minute | number |
| **uptime\_sec**<br>_optional_ | Uptime in seconds | integer |

**reference**

| Name | Description | Schema |
| --- | --- | --- |
| **type**<br>_required_ | The type of the reference item | enum (app\_id, app\_instance, model, task, url) |
| **value**<br>_required_ | The reference item value | string |

## serving.endpoint\_stats [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#servingendpoint_stats "Direct link to serving.endpoint_stats")

| Name | Description | Schema |
| --- | --- | --- |
| **endpoint**<br>_optional_ | Endpoint name | string |
| **instances**<br>_optional_ | The number of model serving instances | integer |
| **last\_update**<br>_optional_ | The latest time when one of the model instances was updated | string (date-time) |
| **latency\_ms**<br>_optional_ | Average of latency of model instances in ms | integer |
| **model**<br>_optional_ | Model name | string |
| **requests**<br>_optional_ | Total requests processed by model instances | integer |
| **requests\_min**<br>_optional_ | Average of request rate of model instances per minute | number |
| **uptime\_sec**<br>_optional_ | Max of model instance uptime in seconds | integer |
| **url**<br>_optional_ | Model url | string |

## serving.machine\_stats [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#servingmachine_stats "Direct link to serving.machine_stats")

| Name | Description | Schema |
| --- | --- | --- |
| **cpu\_temperature**<br>_optional_ | CPU temperature | < number > array |
| **cpu\_usage**<br>_optional_ | Average CPU usage per core | < number > array |
| **disk\_free\_home**<br>_optional_ | Free space in % of /home drive | number |
| **disk\_free\_temp**<br>_optional_ | Free space in % of /tmp drive | number |
| **disk\_read**<br>_optional_ | Mbytes read per second | number |
| **disk\_write**<br>_optional_ | Mbytes write per second | number |
| **gpu\_memory\_free**<br>_optional_ | GPU free memory MBs | < number > array |
| **gpu\_memory\_used**<br>_optional_ | GPU used memory MBs | < number > array |
| **gpu\_temperature**<br>_optional_ | GPU temperature | < number > array |
| **gpu\_usage**<br>_optional_ | Average GPU usage per GPU card | < number > array |
| **memory\_free**<br>_optional_ | Free memory MBs | number |
| **memory\_used**<br>_optional_ | Used memory MBs | number |
| **network\_rx**<br>_optional_ | Mbytes per second | number |
| **network\_tx**<br>_optional_ | Mbytes per second | number |

## storage.aws [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#storageaws "Direct link to storage.aws")

AWS S3 storage settings

| Name | Description | Schema |
| --- | --- | --- |
| **buckets**<br>_optional_ | Credential settings per bucket | < [storage.aws\_bucket](https://clear.ml/docs/latest/docs/references/api/definitions/#storage-aws_bucket) \> array |
| **key**<br>_optional_ | Access key | string |
| **region**<br>_optional_ | AWS region | string |
| **secret**<br>_optional_ | Secret key | string |
| **token**<br>_optional_ | Access token | string |
| **use\_credentials\_chain**<br>_optional_ | If set then use host credentials <br>**Default** : `false` | boolean |

## storage.aws\_bucket [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#storageaws_bucket "Direct link to storage.aws_bucket")

Settings per S3 bucket

| Name | Description | Schema |
| --- | --- | --- |
| **acl**<br>_optional_ | ACL | string |
| **bucket**<br>_optional_ | The name of the bucket | string |
| **host**<br>_optional_ | Host address (for minio servers) | string |
| **key**<br>_optional_ | Access key | string |
| **multipart**<br>_optional_ | Multipart upload <br>**Default** : `true` | boolean |
| **region**<br>_optional_ | AWS Region | string |
| **secret**<br>_optional_ | Secret key | string |
| **secure**<br>_optional_ | Use SSL connection <br>**Default** : `true` | boolean |
| **subdir**<br>_optional_ | The path to match | string |
| **token**<br>_optional_ | Access token | string |
| **use\_credentials\_chain**<br>_optional_ | Use host configured credentials <br>**Default** : `false` | boolean |
| **verify**<br>_optional_ | Verify server certificate <br>**Default** : `true` | boolean |

## storage.azure [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#storageazure "Direct link to storage.azure")

Azure storage settings

| Name | Description | Schema |
| --- | --- | --- |
| **containers**<br>_optional_ | Credentials per container | < [storage.azure\_container](https://clear.ml/docs/latest/docs/references/api/definitions/#storage-azure_container) \> array |

## storage.azure\_container [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#storageazure_container "Direct link to storage.azure_container")

Azure container settings

| Name | Description | Schema |
| --- | --- | --- |
| **account\_key**<br>_optional_ | Account key | string |
| **account\_name**<br>_optional_ | Account name | string |
| **container\_name**<br>_optional_ | The name of the container | string |

## storage.google [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#storagegoogle "Direct link to storage.google")

Google storage settings

| Name | Description | Schema |
| --- | --- | --- |
| **buckets**<br>_optional_ | Credentials per bucket | < [storage.google\_bucket](https://clear.ml/docs/latest/docs/references/api/definitions/#storage-google_bucket) \> array |
| **credentials\_json**<br>_optional_ | The contents of the credentials json file | string |
| **project**<br>_optional_ | Project name | string |

## storage.google\_bucket [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#storagegoogle_bucket "Direct link to storage.google_bucket")

Settings per Google storage bucket

| Name | Description | Schema |
| --- | --- | --- |
| **bucket**<br>_optional_ | The name of the bucket | string |
| **credentials\_json**<br>_optional_ | The contents of the credentials json file | string |
| **project**<br>_optional_ | The name of the project | string |
| **subdir**<br>_optional_ | The path to match | string |

## tasks.artifact [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#tasksartifact "Direct link to tasks.artifact")

| Name | Description | Schema |
| --- | --- | --- |
| **content\_size**<br>_optional_ | Raw data length in bytes | integer |
| **display\_data**<br>_optional_ | User-defined list of key/value pairs, sorted | < < string > array > array |
| **hash**<br>_optional_ | Hash of entire raw data | string |
| **key**<br>_required_ | Entry key | string |
| **mode**<br>_optional_ | System defined input/output indication | [tasks.artifact\_mode\_enum](https://clear.ml/docs/latest/docs/references/api/definitions/#tasks-artifact_mode_enum) |
| **timestamp**<br>_optional_ | Epoch time when artifact was created | integer |
| **type**<br>_required_ | System defined type | string |
| **type\_data**<br>_optional_ | Additional fields defined by the system | [tasks.artifact\_type\_data](https://clear.ml/docs/latest/docs/references/api/definitions/#tasks-artifact_type_data) |
| **uri**<br>_optional_ | Raw data location | string |

## tasks.artifact\_id [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#tasksartifact_id "Direct link to tasks.artifact_id")

| Name | Description | Schema |
| --- | --- | --- |
| **key**<br>_required_ | Entry key | string |
| **mode**<br>_optional_ | System defined input/output indication | [tasks.artifact\_mode\_enum](https://clear.ml/docs/latest/docs/references/api/definitions/#tasks-artifact_mode_enum) |

## tasks.artifact\_mode\_enum [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#tasksartifact_mode_enum "Direct link to tasks.artifact_mode_enum")

_Type_ : enum (input, output)

## tasks.artifact\_type\_data [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#tasksartifact_type_data "Direct link to tasks.artifact_type_data")

| Name | Description | Schema |
| --- | --- | --- |
| **content\_type**<br>_optional_ | System defined raw data content type | string |
| **data\_hash**<br>_optional_ | Hash of raw data, without any headers or descriptive parts | string |
| **preview**<br>_optional_ | Description or textual data | string |

## tasks.configuration\_item [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#tasksconfiguration_item "Direct link to tasks.configuration_item")

| Name | Description | Schema |
| --- | --- | --- |
| **description**<br>_optional_ | The parameter description. Optional | string |
| **name**<br>_optional_ | Name of the parameter. Should be unique | string |
| **type**<br>_optional_ | Type of the parameter. Optional | string |
| **value**<br>_optional_ | Value of the parameter | string |

## tasks.execution [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#tasksexecution "Direct link to tasks.execution")

| Name | Description | Schema |
| --- | --- | --- |
| **artifacts**<br>_optional_ | Task artifacts | < [tasks.artifact](https://clear.ml/docs/latest/docs/references/api/definitions/#tasks-artifact) \> array |
| **docker\_cmd**<br>_optional_ | Command for running docker script for the execution of the task | string |
| **framework**<br>_optional_ | Framework related to the task. Case insensitive. Mandatory for Training tasks. | string |
| **model**<br>_optional_ | Execution input model ID Not applicable for Register (Import) tasks | string |
| **model\_desc**<br>_optional_ | Json object representing the Model descriptors | object |
| **model\_labels**<br>_optional_ | Json object representing the ids of the labels in the model. The keys are the <br>layers' names and the values are the IDs. Not applicable for Register (Import) <br>tasks. Mandatory for Training tasks | < string, integer > map |
| **parameters**<br>_optional_ | Json object containing the Task parameters | object |
| **queue**<br>_optional_ | Queue ID where task was queued. | string |

## tasks.last\_metrics\_event [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#taskslast_metrics_event "Direct link to tasks.last_metrics_event")

| Name | Description | Schema |
| --- | --- | --- |
| **count**<br>_optional_ | The total count of reported values | integer |
| **first\_value**<br>_optional_ | First value reported | number |
| **first\_value\_iteration**<br>_optional_ | The iteration at which the first value was reported | integer |
| **max\_value**<br>_optional_ | Maximum value reported | number |
| **max\_value\_iteration**<br>_optional_ | The iteration at which the maximum value was reported | integer |
| **mean\_value**<br>_optional_ | The mean value | number |
| **metric**<br>_optional_ | Metric name | string |
| **min\_value**<br>_optional_ | Minimum value reported | number |
| **min\_value\_iteration**<br>_optional_ | The iteration at which the minimum value was reported | integer |
| **value**<br>_optional_ | Last value reported | number |
| **variant**<br>_optional_ | Variant name | string |
| **x\_axis\_label**<br>_optional_ | The user defined value for the X-Axis name stored with the event | string |

## tasks.last\_metrics\_variants [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#taskslast_metrics_variants "Direct link to tasks.last_metrics_variants")

Last metric events, one for each variant hash

_Type_ : < string, [tasks.last\_metrics\_event](https://clear.ml/docs/latest/docs/references/api/definitions/#tasks-last_metrics_event) \> map

## tasks.model\_type\_enum [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#tasksmodel_type_enum "Direct link to tasks.model_type_enum")

_Type_ : enum (input, output)

## tasks.multi\_field\_pattern\_data [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#tasksmulti_field_pattern_data "Direct link to tasks.multi_field_pattern_data")

| Name | Description | Schema |
| --- | --- | --- |
| **datetime**<br>_optional_ | Date time conditions (applicable only to datetime fields). Either 'pattern' or <br>'datetime' should be specified | string |
| **fields**<br>_optional_ | List of field names | < string > array |
| **pattern**<br>_optional_ | Pattern string (regex). Either 'pattern' or 'datetime' should be specified | string |

## tasks.output [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#tasksoutput "Direct link to tasks.output")

| Name | Description | Schema |
| --- | --- | --- |
| **destination**<br>_optional_ | Storage id. This is where output files will be stored. | string |
| **error**<br>_optional_ | Last error text | string |
| **model**<br>_optional_ | Model id. | string |
| **result**<br>_optional_ | Task result. Values: 'success', 'failure' | string |

## tasks.param\_key [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#tasksparam_key "Direct link to tasks.param_key")

| Name | Description | Schema |
| --- | --- | --- |
| **name**<br>_optional_ | Name of the parameter. If the name is ommitted then the corresponding operation <br>is performed on the whole section | string |
| **section**<br>_optional_ | Section that the parameter belongs to | string |

## tasks.params\_item [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#tasksparams_item "Direct link to tasks.params_item")

| Name | Description | Schema |
| --- | --- | --- |
| **description**<br>_optional_ | The parameter description. Optional | string |
| **name**<br>_optional_ | Name of the parameter. The combination of section and name should be unique | string |
| **section**<br>_optional_ | Section that the parameter belongs to | string |
| **type**<br>_optional_ | Type of the parameter. Optional | string |
| **value**<br>_optional_ | Value of the parameter | string |

## tasks.replace\_hyperparams\_enum [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#tasksreplace_hyperparams_enum "Direct link to tasks.replace_hyperparams_enum")

_Type_ : enum (none, section, all)

## tasks.script [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#tasksscript "Direct link to tasks.script")

| Name | Description | Schema |
| --- | --- | --- |
| **binary**<br>_optional_ | Binary to use when running the script <br>**Default** : `"python"` | string |
| **branch**<br>_optional_ | Repository branch id If not provided and tag not provided, default repository <br>branch is used. | string |
| **diff**<br>_optional_ | Uncommitted changes found in the repository when task was run | string |
| **entry\_point**<br>_optional_ | Path to execute within the repository | string |
| **repository**<br>_optional_ | Name of the repository where the script is located | string |
| **requirements**<br>_optional_ | A JSON object containing requirements strings by key | object |
| **tag**<br>_optional_ | Repository tag | string |
| **version\_num**<br>_optional_ | Version (changeset) number. Optional (default is head version) Unused if tag is <br>provided. | string |
| **working\_dir**<br>_optional_ | Path to the folder from which to run the script Default - root folder of <br>repository | string |

## tasks.section\_params [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#taskssection_params "Direct link to tasks.section_params")

Task section params

_Type_ : < string, [tasks.params\_item](https://clear.ml/docs/latest/docs/references/api/definitions/#tasks-params_item) \> map

## tasks.task [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#taskstask "Direct link to tasks.task")

| Name | Description | Schema |
| --- | --- | --- |
| **active\_duration**<br>_optional_ | Task duration time (seconds) | integer |
| **comment**<br>_optional_ | Free text comment | string |
| **company**<br>_optional_ | Company ID | string |
| **completed**<br>_optional_ | Task end time (UTC) | string (date-time) |
| **configuration**<br>_optional_ | Task configuration params | < string, [tasks.configuration\_item](https://clear.ml/docs/latest/docs/references/api/definitions/#tasks-configuration_item) \> map |
| **container**<br>_optional_ | Docker container parameters | < string, string > map |
| **created**<br>_optional_ | Task creation time (UTC) | string (date-time) |
| **execution**<br>_optional_ | Task execution params | [tasks.execution](https://clear.ml/docs/latest/docs/references/api/definitions/#tasks-execution) |
| **hyperparams**<br>_optional_ | Task hyper params per section | < string, [tasks.section\_params](https://clear.ml/docs/latest/docs/references/api/definitions/#tasks-section_params) \> map |
| **id**<br>_optional_ | Task id | string |
| **last\_change**<br>_optional_ | Last time any update was done to the task | string (date-time) |
| **last\_iteration**<br>_optional_ | Last iteration reported for this task | integer |
| **last\_metrics**<br>_optional_ | Last metric variants (hash to events), one for each metric hash | < string, [tasks.last\_metrics\_variants](https://clear.ml/docs/latest/docs/references/api/definitions/#tasks-last_metrics_variants) \> map |
| **last\_update**<br>_optional_ | Last time this task was created, edited, changed or events for this task were <br>reported | string (date-time) |
| **last\_worker**<br>_optional_ | ID of last worker that handled the task | string |
| **last\_worker\_report**<br>_optional_ | Last time a worker reported while working on this task | string (date-time) |
| **models**<br>_optional_ | Task models | [tasks.task\_models](https://clear.ml/docs/latest/docs/references/api/definitions/#tasks-task_models) |
| **name**<br>_optional_ | Task Name | string |
| **output**<br>_optional_ | Task output params | [tasks.output](https://clear.ml/docs/latest/docs/references/api/definitions/#tasks-output) |
| **parent**<br>_optional_ | Parent task id | string |
| **project**<br>_optional_ | Project ID of the project to which this task is assigned | string |
| **published**<br>_optional_ | Task publish time | string (date-time) |
| **runtime**<br>_optional_ | Task runtime mapping | object |
| **script**<br>_optional_ | Script info | [tasks.script](https://clear.ml/docs/latest/docs/references/api/definitions/#tasks-script) |
| **started**<br>_optional_ | Task start time (UTC) | string (date-time) |
| **status**<br>_optional_ |  | [tasks.task\_status\_enum](https://clear.ml/docs/latest/docs/references/api/definitions/#tasks-task_status_enum) |
| **status\_changed**<br>_optional_ | Last status change time | string (date-time) |
| **status\_message**<br>_optional_ | free text string representing info about the status | string |
| **status\_reason**<br>_optional_ | Reason for last status change | string |
| **system\_tags**<br>_optional_ | System tags list. This field is reserved for system use, please don't use it. | < string > array |
| **tags**<br>_optional_ | User-defined tags list | < string > array |
| **type**<br>_optional_ | Type of task. Values: 'training', 'testing' | [tasks.task\_type\_enum](https://clear.ml/docs/latest/docs/references/api/definitions/#tasks-task_type_enum) |
| **user**<br>_optional_ | Associated user id | string |

## tasks.task\_model\_item [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#taskstask_model_item "Direct link to tasks.task_model_item")

| Name | Description | Schema |
| --- | --- | --- |
| **model**<br>_required_ | The model ID | string |
| **name**<br>_required_ | The task model name | string |

## tasks.task\_models [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#taskstask_models "Direct link to tasks.task_models")

| Name | Description | Schema |
| --- | --- | --- |
| **input**<br>_optional_ | The list of task input models | < [tasks.task\_model\_item](https://clear.ml/docs/latest/docs/references/api/definitions/#tasks-task_model_item) \> array |
| **output**<br>_optional_ | The list of task output models | < [tasks.task\_model\_item](https://clear.ml/docs/latest/docs/references/api/definitions/#tasks-task_model_item) \> array |

## tasks.task\_status\_enum [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#taskstask_status_enum "Direct link to tasks.task_status_enum")

_Type_ : enum (created, queued, in\_progress, stopped, published, publishing, closed, failed, completed, unknown)

## tasks.task\_type\_enum [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#taskstask_type_enum "Direct link to tasks.task_type_enum")

_Type_ : enum (training, testing, inference, data\_processing, application, monitor, controller, optimizer, service, qc, custom)

## tasks.task\_urls [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#taskstask_urls "Direct link to tasks.task_urls")

| Name | Schema |
| --- | --- |
| **artifact\_urls**<br>_optional_ | < string > array |
| **event\_urls**<br>_optional_ | < string > array |
| **model\_urls**<br>_optional_ | < string > array |

## users.get\_current\_user\_response\_user\_object [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#usersget_current_user_response_user_object "Direct link to users.get_current_user_response_user_object")

like user, but returns company object instead of ID

| Name | Description | Schema |
| --- | --- | --- |
| **avatar**<br>_optional_ |  | string |
| **company**<br>_optional_ |  | [company](https://clear.ml/docs/latest/docs/references/api/definitions/#users-get_current_user_response_user_object-company) |
| **family\_name**<br>_optional_ |  | string |
| **given\_name**<br>_optional_ |  | string |
| **id**<br>_optional_ |  | string |
| **name**<br>_optional_ |  | string |
| **preferences**<br>_optional_ | User preferences | object |
| **role**<br>_optional_ |  | string |

**company**

| Name | Schema |
| --- | --- |
| **id**<br>_optional_ | string |
| **name**<br>_optional_ | string |

## users.user [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#usersuser "Direct link to users.user")

| Name | Description | Schema |
| --- | --- | --- |
| **avatar**<br>_optional_ | Avatar URL | string |
| **company**<br>_optional_ | Company ID | string |
| **created**<br>_optional_ | User creation date | string (date-time) |
| **email**<br>_optional_ | User email | string (email) |
| **family\_name**<br>_optional_ | Family name | string |
| **given\_name**<br>_optional_ | Given name | string |
| **id**<br>_optional_ | User ID | string |
| **name**<br>_optional_ | Full name | string |
| **providers**<br>_optional_ | Providers uses has logged-in with | object |
| **role**<br>_optional_ | User's role (admin only) | string |

## workers.activity\_series [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#workersactivity_series "Direct link to workers.activity_series")

| Name | Description | Schema |
| --- | --- | --- |
| **counts**<br>_optional_ | List of worker counts corresponding to the timestamps in the dates list. None <br>values are returned for the dates with no workers. | < integer > array |
| **dates**<br>_optional_ | List of timestamps (in seconds from epoch) in the acceding order. The <br>timestamps are separated by the requested interval. | < integer > array |

## workers.aggregation\_stats [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#workersaggregation_stats "Direct link to workers.aggregation_stats")

| Name | Description | Schema |
| --- | --- | --- |
| **aggregation**<br>_optional_ |  | [workers.aggregation\_type](https://clear.ml/docs/latest/docs/references/api/definitions/#workers-aggregation_type) |
| **dates**<br>_optional_ | List of timestamps (in seconds from epoch) in the acceding order. The <br>timestamps are separated by the requested interval. Timestamps where no workers <br>activity was recorded are omitted. | < integer > array |
| **resource\_series**<br>_optional_ | Metric data per single resource. Return only if split\_by\_resource request <br>parameter is set to True | < [workers.metric\_resource\_series](https://clear.ml/docs/latest/docs/references/api/definitions/#workers-metric_resource_series) \> array |
| **values**<br>_optional_ | List of values corresponding to the dates in metric statistics | < number > array |

## workers.aggregation\_type [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#workersaggregation_type "Direct link to workers.aggregation_type")

Metric aggregation type

_Type_ : enum (avg, min, max)

## workers.current\_task\_entry [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#workerscurrent_task_entry "Direct link to workers.current_task_entry")

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_optional_ | Worker ID | string |
| **last\_iteration**<br>_optional_ | Last task iteration | integer |
| **name**<br>_optional_ | Worker name | string |
| **running\_time**<br>_optional_ | Task running time | integer |

## workers.id\_name\_entry [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#workersid_name_entry "Direct link to workers.id_name_entry")

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_optional_ | Worker ID | string |
| **name**<br>_optional_ | Worker name | string |

## workers.machine\_stats [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#workersmachine_stats "Direct link to workers.machine_stats")

| Name | Description | Schema |
| --- | --- | --- |
| **cpu\_temperature**<br>_optional_ | CPU temperature | < number > array |
| **cpu\_usage**<br>_optional_ | Average CPU usage per core | < number > array |
| **disk\_free\_home**<br>_optional_ | Free space in % of /home drive | number |
| **disk\_free\_temp**<br>_optional_ | Free space in % of /tmp drive | number |
| **disk\_read**<br>_optional_ | Mbytes read per second | number |
| **disk\_write**<br>_optional_ | Mbytes write per second | number |
| **gpu\_memory\_free**<br>_optional_ | GPU free memory MBs | < number > array |
| **gpu\_memory\_used**<br>_optional_ | GPU used memory MBs | < number > array |
| **gpu\_temperature**<br>_optional_ | GPU temperature | < number > array |
| **gpu\_usage**<br>_optional_ | Average GPU usage per GPU card | < number > array |
| **memory\_free**<br>_optional_ | Free memory MBs | number |
| **memory\_used**<br>_optional_ | Used memory MBs | number |
| **network\_rx**<br>_optional_ | Mbytes per second | number |
| **network\_tx**<br>_optional_ | Mbytes per second | number |

## workers.metric\_resource\_series [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#workersmetric_resource_series "Direct link to workers.metric_resource_series")

| Name | Description | Schema |
| --- | --- | --- |
| **name**<br>_optional_ | Resource name | string |
| **values**<br>_optional_ | List of values corresponding to the dates in metric statistics | < number > array |

## workers.metric\_stats [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#workersmetric_stats "Direct link to workers.metric_stats")

| Name | Description | Schema |
| --- | --- | --- |
| **metric**<br>_optional_ | Name of the metric (cpu\_usage, memory\_used etc.) | string |
| **stats**<br>_optional_ | Statistics data by type | < [workers.aggregation\_stats](https://clear.ml/docs/latest/docs/references/api/definitions/#workers-aggregation_stats) \> array |
| **variant**<br>_optional_ | Name of the metric component. Set only if 'split\_by\_variant' was set in the <br>request | string |

## workers.metrics\_category [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#workersmetrics_category "Direct link to workers.metrics_category")

| Name | Description | Schema |
| --- | --- | --- |
| **metric\_keys**<br>_optional_ | The names of the metrics in the category. | < string > array |
| **name**<br>_optional_ | Name of the metrics category. | string |

## workers.queue\_entry [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#workersqueue_entry "Direct link to workers.queue_entry")

| Name | Description | Schema |
| --- | --- | --- |
| **display\_name**<br>_optional_ | Display name for the queue (if defined) | string |
| **id**<br>_optional_ | Worker ID | string |
| **name**<br>_optional_ | Worker name | string |
| **next\_task**<br>_optional_ | Next task in the queue | [workers.id\_name\_entry](https://clear.ml/docs/latest/docs/references/api/definitions/#workers-id_name_entry) |
| **num\_tasks**<br>_optional_ | Number of task entries in the queue | integer |

## workers.stat\_item [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#workersstat_item "Direct link to workers.stat_item")

| Name | Description | Schema |
| --- | --- | --- |
| **category**<br>_optional_ |  | [workers.aggregation\_type](https://clear.ml/docs/latest/docs/references/api/definitions/#workers-aggregation_type) |
| **key**<br>_optional_ | Name of a metric | enum (cpu\_usage, cpu\_temperature, memory\_used, memory\_free, gpu\_usage, gpu\_temperature, gpu\_fraction, gpu\_memory\_free, gpu\_memory\_used, network\_tx, network\_rx, disk\_free\_home, disk\_free\_temp, disk\_read, disk\_write) |

## workers.worker [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#workersworker "Direct link to workers.worker")

| Name | Description | Schema |
| --- | --- | --- |
| **company**<br>_optional_ | Associated company | [workers.id\_name\_entry](https://clear.ml/docs/latest/docs/references/api/definitions/#workers-id_name_entry) |
| **id**<br>_optional_ | Worker ID | string |
| **ip**<br>_optional_ | IP of the worker | string |
| **key**<br>_optional_ | Worker entry key | string |
| **last\_activity\_time**<br>_optional_ | Last activity time (even if an error occurred) | string (date-time) |
| **last\_report\_time**<br>_optional_ | Last successful report time | string (date-time) |
| **project**<br>_optional_ | Project in which currently executing task resides | [workers.id\_name\_entry](https://clear.ml/docs/latest/docs/references/api/definitions/#workers-id_name_entry) |
| **queue**<br>_optional_ | Queue from which running task was taken | [workers.queue\_entry](https://clear.ml/docs/latest/docs/references/api/definitions/#workers-queue_entry) |
| **queues**<br>_optional_ | List of queues on which the worker is listening | < [workers.queue\_entry](https://clear.ml/docs/latest/docs/references/api/definitions/#workers-queue_entry) \> array |
| **register\_time**<br>_optional_ | Registration time | string (date-time) |
| **system\_tags**<br>_optional_ | System tags for the worker | < string > array |
| **tags**<br>_optional_ | User tags for the worker | < string > array |
| **task**<br>_optional_ | Task currently being run by the worker | [workers.current\_task\_entry](https://clear.ml/docs/latest/docs/references/api/definitions/#workers-current_task_entry) |
| **user**<br>_optional_ | Associated user (under whose credentials are used by the worker daemon) | [workers.id\_name\_entry](https://clear.ml/docs/latest/docs/references/api/definitions/#workers-id_name_entry) |

## workers.worker\_stats [​](https://clear.ml/docs/latest/docs/references/api/definitions/\#workersworker_stats "Direct link to workers.worker_stats")

| Name | Description | Schema |
| --- | --- | --- |
| **metrics**<br>_optional_ | List of the metrics statistics for the worker | < [workers.metric\_stats](https://clear.ml/docs/latest/docs/references/api/definitions/#workers-metric_stats) \> array |
| **worker**<br>_optional_ | ID of the worker | string |

- [Definitions](https://clear.ml/docs/latest/docs/references/api/definitions/#definitions)
- [auth.credential\_key](https://clear.ml/docs/latest/docs/references/api/definitions/#authcredential_key)
- [auth.credentials](https://clear.ml/docs/latest/docs/references/api/definitions/#authcredentials)
- [auth.role](https://clear.ml/docs/latest/docs/references/api/definitions/#authrole)
- [events.debug\_image\_sample\_response](https://clear.ml/docs/latest/docs/references/api/definitions/#eventsdebug_image_sample_response)
- [events.debug\_images\_response](https://clear.ml/docs/latest/docs/references/api/definitions/#eventsdebug_images_response)
- [events.debug\_images\_response\_task\_metrics](https://clear.ml/docs/latest/docs/references/api/definitions/#eventsdebug_images_response_task_metrics)
- [events.event\_type\_enum](https://clear.ml/docs/latest/docs/references/api/definitions/#eventsevent_type_enum)
- [events.log\_level\_enum](https://clear.ml/docs/latest/docs/references/api/definitions/#eventslog_level_enum)
- [events.metric\_variants](https://clear.ml/docs/latest/docs/references/api/definitions/#eventsmetric_variants)
- [events.metrics\_image\_event](https://clear.ml/docs/latest/docs/references/api/definitions/#eventsmetrics_image_event)
- [events.metrics\_plot\_event](https://clear.ml/docs/latest/docs/references/api/definitions/#eventsmetrics_plot_event)
- [events.metrics\_scalar\_event](https://clear.ml/docs/latest/docs/references/api/definitions/#eventsmetrics_scalar_event)
- [events.metrics\_vector\_event](https://clear.ml/docs/latest/docs/references/api/definitions/#eventsmetrics_vector_event)
- [events.plot\_sample\_response](https://clear.ml/docs/latest/docs/references/api/definitions/#eventsplot_sample_response)
- [events.plots\_response](https://clear.ml/docs/latest/docs/references/api/definitions/#eventsplots_response)
- [events.plots\_response\_task\_metrics](https://clear.ml/docs/latest/docs/references/api/definitions/#eventsplots_response_task_metrics)
- [events.scalar\_key\_enum](https://clear.ml/docs/latest/docs/references/api/definitions/#eventsscalar_key_enum)
- [events.single\_value\_metrics\_response](https://clear.ml/docs/latest/docs/references/api/definitions/#eventssingle_value_metrics_response)
- [events.single\_value\_task\_metrics](https://clear.ml/docs/latest/docs/references/api/definitions/#eventssingle_value_task_metrics)
- [events.task\_log\_event](https://clear.ml/docs/latest/docs/references/api/definitions/#eventstask_log_event)
- [events.task\_metric](https://clear.ml/docs/latest/docs/references/api/definitions/#eventstask_metric)
- [events.task\_metric\_variants](https://clear.ml/docs/latest/docs/references/api/definitions/#eventstask_metric_variants)
- [models.last\_metrics\_event](https://clear.ml/docs/latest/docs/references/api/definitions/#modelslast_metrics_event)
- [models.last\_metrics\_variants](https://clear.ml/docs/latest/docs/references/api/definitions/#modelslast_metrics_variants)
- [models.metadata\_item](https://clear.ml/docs/latest/docs/references/api/definitions/#modelsmetadata_item)
- [models.model](https://clear.ml/docs/latest/docs/references/api/definitions/#modelsmodel)
- [models.multi\_field\_pattern\_data](https://clear.ml/docs/latest/docs/references/api/definitions/#modelsmulti_field_pattern_data)
- [organization.field\_mapping](https://clear.ml/docs/latest/docs/references/api/definitions/#organizationfield_mapping)
- [organization.value\_mapping](https://clear.ml/docs/latest/docs/references/api/definitions/#organizationvalue_mapping)
- [organization.workloads](https://clear.ml/docs/latest/docs/references/api/definitions/#organizationworkloads)
- [projects.metric\_variant\_result](https://clear.ml/docs/latest/docs/references/api/definitions/#projectsmetric_variant_result)
- [projects.multi\_field\_pattern\_data](https://clear.ml/docs/latest/docs/references/api/definitions/#projectsmulti_field_pattern_data)
- [projects.project](https://clear.ml/docs/latest/docs/references/api/definitions/#projectsproject)
- [projects.projects\_get\_all\_response\_single](https://clear.ml/docs/latest/docs/references/api/definitions/#projectsprojects_get_all_response_single)
- [projects.stats](https://clear.ml/docs/latest/docs/references/api/definitions/#projectsstats)
- [projects.stats\_datasets](https://clear.ml/docs/latest/docs/references/api/definitions/#projectsstats_datasets)
- [projects.stats\_status\_count](https://clear.ml/docs/latest/docs/references/api/definitions/#projectsstats_status_count)
- [projects.urls](https://clear.ml/docs/latest/docs/references/api/definitions/#projectsurls)
- [queues.entry](https://clear.ml/docs/latest/docs/references/api/definitions/#queuesentry)
- [queues.metadata\_item](https://clear.ml/docs/latest/docs/references/api/definitions/#queuesmetadata_item)
- [queues.queue](https://clear.ml/docs/latest/docs/references/api/definitions/#queuesqueue)
- [queues.queue\_metrics](https://clear.ml/docs/latest/docs/references/api/definitions/#queuesqueue_metrics)
- [reports.artifact](https://clear.ml/docs/latest/docs/references/api/definitions/#reportsartifact)
- [reports.artifact\_mode\_enum](https://clear.ml/docs/latest/docs/references/api/definitions/#reportsartifact_mode_enum)
- [reports.artifact\_type\_data](https://clear.ml/docs/latest/docs/references/api/definitions/#reportsartifact_type_data)
- [reports.configuration\_item](https://clear.ml/docs/latest/docs/references/api/definitions/#reportsconfiguration_item)
- [reports.debug\_images\_response\_task\_metrics](https://clear.ml/docs/latest/docs/references/api/definitions/#reportsdebug_images_response_task_metrics)
- [reports.execution](https://clear.ml/docs/latest/docs/references/api/definitions/#reportsexecution)
- [reports.last\_metrics\_event](https://clear.ml/docs/latest/docs/references/api/definitions/#reportslast_metrics_event)
- [reports.last\_metrics\_variants](https://clear.ml/docs/latest/docs/references/api/definitions/#reportslast_metrics_variants)
- [reports.metric\_variants](https://clear.ml/docs/latest/docs/references/api/definitions/#reportsmetric_variants)
- [reports.multi\_field\_pattern\_data](https://clear.ml/docs/latest/docs/references/api/definitions/#reportsmulti_field_pattern_data)
- [reports.output](https://clear.ml/docs/latest/docs/references/api/definitions/#reportsoutput)
- [reports.params\_item](https://clear.ml/docs/latest/docs/references/api/definitions/#reportsparams_item)
- [reports.report](https://clear.ml/docs/latest/docs/references/api/definitions/#reportsreport)
- [reports.report\_status\_enum](https://clear.ml/docs/latest/docs/references/api/definitions/#reportsreport_status_enum)
- [reports.scalar\_key\_enum](https://clear.ml/docs/latest/docs/references/api/definitions/#reportsscalar_key_enum)
- [reports.script](https://clear.ml/docs/latest/docs/references/api/definitions/#reportsscript)
- [reports.section\_params](https://clear.ml/docs/latest/docs/references/api/definitions/#reportssection_params)
- [reports.single\_value\_task\_metrics](https://clear.ml/docs/latest/docs/references/api/definitions/#reportssingle_value_task_metrics)
- [reports.task](https://clear.ml/docs/latest/docs/references/api/definitions/#reportstask)
- [reports.task\_model\_item](https://clear.ml/docs/latest/docs/references/api/definitions/#reportstask_model_item)
- [reports.task\_models](https://clear.ml/docs/latest/docs/references/api/definitions/#reportstask_models)
- [reports.task\_status\_enum](https://clear.ml/docs/latest/docs/references/api/definitions/#reportstask_status_enum)
- [reports.task\_type\_enum](https://clear.ml/docs/latest/docs/references/api/definitions/#reportstask_type_enum)
- [serving.container\_info](https://clear.ml/docs/latest/docs/references/api/definitions/#servingcontainer_info)
- [serving.container\_instance\_stats](https://clear.ml/docs/latest/docs/references/api/definitions/#servingcontainer_instance_stats)
- [serving.endpoint\_stats](https://clear.ml/docs/latest/docs/references/api/definitions/#servingendpoint_stats)
- [serving.machine\_stats](https://clear.ml/docs/latest/docs/references/api/definitions/#servingmachine_stats)
- [storage.aws](https://clear.ml/docs/latest/docs/references/api/definitions/#storageaws)
- [storage.aws\_bucket](https://clear.ml/docs/latest/docs/references/api/definitions/#storageaws_bucket)
- [storage.azure](https://clear.ml/docs/latest/docs/references/api/definitions/#storageazure)
- [storage.azure\_container](https://clear.ml/docs/latest/docs/references/api/definitions/#storageazure_container)
- [storage.google](https://clear.ml/docs/latest/docs/references/api/definitions/#storagegoogle)
- [storage.google\_bucket](https://clear.ml/docs/latest/docs/references/api/definitions/#storagegoogle_bucket)
- [tasks.artifact](https://clear.ml/docs/latest/docs/references/api/definitions/#tasksartifact)
- [tasks.artifact\_id](https://clear.ml/docs/latest/docs/references/api/definitions/#tasksartifact_id)
- [tasks.artifact\_mode\_enum](https://clear.ml/docs/latest/docs/references/api/definitions/#tasksartifact_mode_enum)
- [tasks.artifact\_type\_data](https://clear.ml/docs/latest/docs/references/api/definitions/#tasksartifact_type_data)
- [tasks.configuration\_item](https://clear.ml/docs/latest/docs/references/api/definitions/#tasksconfiguration_item)
- [tasks.execution](https://clear.ml/docs/latest/docs/references/api/definitions/#tasksexecution)
- [tasks.last\_metrics\_event](https://clear.ml/docs/latest/docs/references/api/definitions/#taskslast_metrics_event)
- [tasks.last\_metrics\_variants](https://clear.ml/docs/latest/docs/references/api/definitions/#taskslast_metrics_variants)
- [tasks.model\_type\_enum](https://clear.ml/docs/latest/docs/references/api/definitions/#tasksmodel_type_enum)
- [tasks.multi\_field\_pattern\_data](https://clear.ml/docs/latest/docs/references/api/definitions/#tasksmulti_field_pattern_data)
- [tasks.output](https://clear.ml/docs/latest/docs/references/api/definitions/#tasksoutput)
- [tasks.param\_key](https://clear.ml/docs/latest/docs/references/api/definitions/#tasksparam_key)
- [tasks.params\_item](https://clear.ml/docs/latest/docs/references/api/definitions/#tasksparams_item)
- [tasks.replace\_hyperparams\_enum](https://clear.ml/docs/latest/docs/references/api/definitions/#tasksreplace_hyperparams_enum)
- [tasks.script](https://clear.ml/docs/latest/docs/references/api/definitions/#tasksscript)
- [tasks.section\_params](https://clear.ml/docs/latest/docs/references/api/definitions/#taskssection_params)
- [tasks.task](https://clear.ml/docs/latest/docs/references/api/definitions/#taskstask)
- [tasks.task\_model\_item](https://clear.ml/docs/latest/docs/references/api/definitions/#taskstask_model_item)
- [tasks.task\_models](https://clear.ml/docs/latest/docs/references/api/definitions/#taskstask_models)
- [tasks.task\_status\_enum](https://clear.ml/docs/latest/docs/references/api/definitions/#taskstask_status_enum)
- [tasks.task\_type\_enum](https://clear.ml/docs/latest/docs/references/api/definitions/#taskstask_type_enum)
- [tasks.task\_urls](https://clear.ml/docs/latest/docs/references/api/definitions/#taskstask_urls)
- [users.get\_current\_user\_response\_user\_object](https://clear.ml/docs/latest/docs/references/api/definitions/#usersget_current_user_response_user_object)
- [users.user](https://clear.ml/docs/latest/docs/references/api/definitions/#usersuser)
- [workers.activity\_series](https://clear.ml/docs/latest/docs/references/api/definitions/#workersactivity_series)
- [workers.aggregation\_stats](https://clear.ml/docs/latest/docs/references/api/definitions/#workersaggregation_stats)
- [workers.aggregation\_type](https://clear.ml/docs/latest/docs/references/api/definitions/#workersaggregation_type)
- [workers.current\_task\_entry](https://clear.ml/docs/latest/docs/references/api/definitions/#workerscurrent_task_entry)
- [workers.id\_name\_entry](https://clear.ml/docs/latest/docs/references/api/definitions/#workersid_name_entry)
- [workers.machine\_stats](https://clear.ml/docs/latest/docs/references/api/definitions/#workersmachine_stats)
- [workers.metric\_resource\_series](https://clear.ml/docs/latest/docs/references/api/definitions/#workersmetric_resource_series)
- [workers.metric\_stats](https://clear.ml/docs/latest/docs/references/api/definitions/#workersmetric_stats)
- [workers.metrics\_category](https://clear.ml/docs/latest/docs/references/api/definitions/#workersmetrics_category)
- [workers.queue\_entry](https://clear.ml/docs/latest/docs/references/api/definitions/#workersqueue_entry)
- [workers.stat\_item](https://clear.ml/docs/latest/docs/references/api/definitions/#workersstat_item)
- [workers.worker](https://clear.ml/docs/latest/docs/references/api/definitions/#workersworker)
- [workers.worker\_stats](https://clear.ml/docs/latest/docs/references/api/definitions/#workersworker_stats)