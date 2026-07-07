---
url: "https://clear.ml/docs/latest/docs/references/api/events/"
title: "events | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/api/events/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

### POST /events.add [​](https://clear.ml/docs/latest/docs/references/api/events/\#post-eventsadd "Direct link to POST /events.add")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/events/\#description "Direct link to Description")

Adds a single event

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/events/\#parameters "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/events/#events-add-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **allow\_locked**<br>_optional_ | Allow adding events to published tasks or models <br>**Default** : `false` | boolean |
| **model\_event**<br>_optional_ | If set then the event is for a model. Otherwise for a task. Cannot be used with <br>task log events. If used in batch then all the events should be marked the same <br>**Default** : `false` | boolean |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/events/\#responses "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/events/\#security "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /events.add\_batch [​](https://clear.ml/docs/latest/docs/references/api/events/\#post-eventsadd_batch "Direct link to POST /events.add_batch")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/events/\#description-1 "Direct link to Description")

Adds a batch of events in a single call (json-lines format, stream-friendly)

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/events/\#parameters-1 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **requests**<br>_required_ | Json encoded newline-terminated lines, each representing an event in the batch and uses the same parameters used for events.add | < object > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/events/\#responses-1 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/events/#events-add_batch-response-200) |

**Response 200**

| Name | Schema |
| --- | --- |
| **added**<br>_optional_ | integer |
| **errors**<br>_optional_ | integer |
| **errors\_info**<br>_optional_ | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/events/\#security-1 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /events.clear\_scroll [​](https://clear.ml/docs/latest/docs/references/api/events/\#post-eventsclear_scroll "Direct link to POST /events.clear_scroll")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/events/\#description-2 "Direct link to Description")

Clear an open Scroll ID

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/events/\#parameters-2 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/events/#events-clear_scroll-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **scroll\_id**<br>_required_ | Scroll ID as returned by previous events service calls | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/events/\#responses-2 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/events/\#security-2 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /events.clear\_task\_log [​](https://clear.ml/docs/latest/docs/references/api/events/\#post-eventsclear_task_log "Direct link to POST /events.clear_task_log")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/events/\#description-3 "Direct link to Description")

Remove old logs from task

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/events/\#parameters-3 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/events/#events-clear_task_log-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **allow\_locked**<br>_optional_ | Allow deleting events even if the task is locked <br>**Default** : `false` | boolean |
| **exclude\_metrics**<br>_optional_ | If passed then events for these metrics are retained | < string > array |
| **include\_metrics**<br>_optional_ | If passed then only events for these metrics are deleted | < string > array |
| **task**<br>_required_ | Task ID | string |
| **threshold\_sec**<br>_optional_ | The amount of seconds ago to retain the log records. The older log records will <br>be deleted. If not passed or 0 then all the log records for the task will be <br>deleted | integer |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/events/\#responses-3 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/events/#events-clear_task_log-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **deleted**<br>_optional_ | The number of deleted log records | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/events/\#security-3 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /events.debug\_images [​](https://clear.ml/docs/latest/docs/references/api/events/\#post-eventsdebug_images "Direct link to POST /events.debug_images")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/events/\#description-4 "Direct link to Description")

Get the debug image events for the requested amount of iterations per each task

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/events/\#parameters-4 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/events/#events-debug_images-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **iters**<br>_optional_ | Max number of latest iterations for which to return debug images | integer |
| **metrics**<br>_required_ | List of metrics and variants | < [events.task\_metric\_variants](https://clear.ml/docs/latest/docs/references/api/definitions#eventstask_metric_variants) \> array |
| **model\_events**<br>_optional_ | If set then the retrieving model events. Otherwise task events <br>**Default** : `false` | boolean |
| **navigate\_earlier**<br>_optional_ | If set then events are retreived from latest iterations to earliest ones. <br>Otherwise from earliest iterations to the latest. The default is True | boolean |
| **refresh**<br>_optional_ | If set then scroll will be moved to the latest iterations. The default is False | boolean |
| **scroll\_id**<br>_optional_ | Scroll ID of previous call (used for getting more results) | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/events/\#responses-4 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [events.debug\_images\_response](https://clear.ml/docs/latest/docs/references/api/definitions#eventsdebug_images_response) |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/events/\#security-4 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /events.delete\_for\_model [​](https://clear.ml/docs/latest/docs/references/api/events/\#post-eventsdelete_for_model "Direct link to POST /events.delete_for_model")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/events/\#description-5 "Direct link to Description")

Delete all model events. _This cannot be undone!_

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/events/\#parameters-5 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/events/#events-delete_for_model-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **allow\_locked**<br>_optional_ | Allow deleting events even if the model is locked <br>**Default** : `false` | boolean |
| **model**<br>_required_ | Model ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/events/\#responses-5 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/events/#events-delete_for_model-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **deleted**<br>_optional_ | Number of deleted events | boolean |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/events/\#security-5 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /events.delete\_for\_task [​](https://clear.ml/docs/latest/docs/references/api/events/\#post-eventsdelete_for_task "Direct link to POST /events.delete_for_task")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/events/\#description-6 "Direct link to Description")

Delete all task events. _This cannot be undone!_

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/events/\#parameters-6 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/events/#events-delete_for_task-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **allow\_locked**<br>_optional_ | Allow deleting events even if the task is locked <br>**Default** : `false` | boolean |
| **task**<br>_required_ | Task ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/events/\#responses-6 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/events/#events-delete_for_task-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **deleted**<br>_optional_ | Number of deleted events | boolean |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/events/\#security-6 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /events.download\_task\_log [​](https://clear.ml/docs/latest/docs/references/api/events/\#post-eventsdownload_task_log "Direct link to POST /events.download_task_log")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/events/\#description-7 "Direct link to Description")

Get an attachment containing the task's log

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/events/\#parameters-7 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/events/#events-download_task_log-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **line\_format**<br>_optional_ | Line string format. Used if the line type is 'text' <br>**Default** : `"{asctime} {worker} {level} {msg}"` | string |
| **line\_type**<br>_optional_ | Line format type | enum (json, text) |
| **task**<br>_required_ | Task ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/events/\#responses-7 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/events/\#security-7 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /events.get\_debug\_image\_sample [​](https://clear.ml/docs/latest/docs/references/api/events/\#post-eventsget_debug_image_sample "Direct link to POST /events.get_debug_image_sample")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/events/\#description-8 "Direct link to Description")

Return the debug image per metric and variant for the provided iteration

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/events/\#parameters-8 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/events/#events-get_debug_image_sample-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **iteration**<br>_optional_ | The iteration to bring debug image from. If not specified then the latest <br>reported image is retrieved | integer |
| **metric**<br>_required_ | Metric name | string |
| **model\_events**<br>_optional_ | If set then the retrieving model debug images. Otherwise task debug images <br>**Default** : `false` | boolean |
| **navigate\_current\_metric**<br>_optional_ | If set then subsequent navigation with next\_debug\_image\_sample is done on the <br>debug images for the passed metric only. Otherwise for all the metrics <br>**Default** : `true` | boolean |
| **refresh**<br>_optional_ | If set then scroll state will be refreshed to reflect the latest changes in the <br>debug images | boolean |
| **scroll\_id**<br>_optional_ | Scroll ID from the previous call to get\_debug\_image\_sample or empty | string |
| **task**<br>_required_ | Task ID | string |
| **variant**<br>_required_ | Metric variant | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/events/\#responses-8 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [events.debug\_image\_sample\_response](https://clear.ml/docs/latest/docs/references/api/definitions#eventsdebug_image_sample_response) |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/events/\#security-8 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /events.get\_multi\_task\_metrics [​](https://clear.ml/docs/latest/docs/references/api/events/\#post-eventsget_multi_task_metrics "Direct link to POST /events.get_multi_task_metrics")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/events/\#description-9 "Direct link to Description")

Get unique metrics and variants from the events of the specified type. Only

events reported for the passed task or model ids are analyzed.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/events/\#parameters-9 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/events/#events-get_multi_task_metrics-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **event\_type**<br>_optional_ | Event type. If not specified then metrics are collected from the reported <br>events of all types | [events.event\_type\_enum](https://clear.ml/docs/latest/docs/references/api/definitions#eventsevent_type_enum) |
| **model\_events**<br>_optional_ | If not set or set to Falsethen passed ids are task ids otherwise model ids <br>**Default** : `false` | boolean |
| **tasks**<br>_required_ | task ids to get metrics from | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/events/\#responses-9 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/events/#events-get_multi_task_metrics-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **metrics**<br>_optional_ | List of metrics and variants | < [events.metric\_variants](https://clear.ml/docs/latest/docs/references/api/definitions#eventsmetric_variants) \> array |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/events/\#security-9 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /events.get\_multi\_task\_plots [​](https://clear.ml/docs/latest/docs/references/api/events/\#post-eventsget_multi_task_plots "Direct link to POST /events.get_multi_task_plots")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/events/\#description-10 "Direct link to Description")

Get 'plot' events for the given tasks

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/events/\#parameters-10 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/events/#events-get_multi_task_plots-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **iters**<br>_optional_ | Max number of latest iterations for which to return plots | integer |
| **last\_iters\_per\_task\_metric**<br>_optional_ | If set to 'true' and iters passed then last iterations for each task metrics <br>are retrieved. Otherwise last iterations for the whole task are retrieved <br>**Default** : `true` | boolean |
| **metrics**<br>_optional_ | List of metrics and variants | < [events.metric\_variants](https://clear.ml/docs/latest/docs/references/api/definitions#eventsmetric_variants) \> array |
| **model\_events**<br>_optional_ | If set then the retrieving model events. Otherwise task events <br>**Default** : `false` | boolean |
| **no\_scroll**<br>_optional_ | If Truethen no scroll is created. Suitable for one time calls <br>**Default** : `false` | boolean |
| **scroll\_id**<br>_optional_ | Scroll ID of previous call (used for getting more results) | string |
| **tasks**<br>_required_ | List of task IDs | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/events/\#responses-10 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/events/#events-get_multi_task_plots-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **plots**<br>_optional_ | Plots mapping (keyed by task name) | object |
| **returned**<br>_optional_ | Number of results returned | integer |
| **scroll\_id**<br>_optional_ | Scroll ID for getting more results | string |
| **total**<br>_optional_ | Total number of results available for this query. In case there are more than <br>10000 results it is set to 10000 | number |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/events/\#security-10 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /events.get\_plot\_sample [​](https://clear.ml/docs/latest/docs/references/api/events/\#post-eventsget_plot_sample "Direct link to POST /events.get_plot_sample")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/events/\#description-11 "Direct link to Description")

Return plots for the provided iteration

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/events/\#parameters-11 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/events/#events-get_plot_sample-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **iteration**<br>_optional_ | The iteration to bring plot from. If not specified then the latest reported <br>plot is retrieved | integer |
| **metric**<br>_required_ | Metric name | string |
| **model\_events**<br>_optional_ | If set then the retrieving model plots. Otherwise task plots <br>**Default** : `false` | boolean |
| **navigate\_current\_metric**<br>_optional_ | If set then subsequent navigation with next\_plot\_sample is done on the plots <br>for the passed metric only. Otherwise for all the metrics <br>**Default** : `true` | boolean |
| **refresh**<br>_optional_ | If set then scroll state will be refreshed to reflect the latest changes in the <br>plots | boolean |
| **scroll\_id**<br>_optional_ | Scroll ID from the previous call to get\_plot\_sample or empty | string |
| **task**<br>_required_ | Task ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/events/\#responses-11 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [events.plot\_sample\_response](https://clear.ml/docs/latest/docs/references/api/definitions#eventsplot_sample_response) |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/events/\#security-11 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /events.get\_scalar\_metric\_data [​](https://clear.ml/docs/latest/docs/references/api/events/\#post-eventsget_scalar_metric_data "Direct link to POST /events.get_scalar_metric_data")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/events/\#description-12 "Direct link to Description")

get scalar metric data for task

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/events/\#parameters-12 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/events/#events-get_scalar_metric_data-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **metric**<br>_optional_ | type of metric | string |
| **model\_events**<br>_optional_ | If set then the retrieving model events. Otherwise task events <br>**Default** : `false` | boolean |
| **no\_scroll**<br>_optional_ | If Truethen no scroll is created. Suitable for one time calls <br>**Default** : `false` | boolean |
| **scroll\_id**<br>_optional_ | Scroll ID of previous call (used for getting more results) | string |
| **task**<br>_optional_ | task ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/events/\#responses-12 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/events/#events-get_scalar_metric_data-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **events**<br>_optional_ | task scalar metric events | < object > array |
| **returned**<br>_optional_ | amount of events returned | integer |
| **scroll\_id**<br>_optional_ | Scroll ID for getting more results | string |
| **total**<br>_optional_ | amount of events in task | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/events/\#security-12 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /events.get\_scalar\_metrics\_and\_variants [​](https://clear.ml/docs/latest/docs/references/api/events/\#post-eventsget_scalar_metrics_and_variants "Direct link to POST /events.get_scalar_metrics_and_variants")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/events/\#description-13 "Direct link to Description")

get task scalar metrics and variants

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/events/\#parameters-13 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/events/#events-get_scalar_metrics_and_variants-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **model\_events**<br>_optional_ | If set then the retrieving model events. Otherwise task events <br>**Default** : `false` | boolean |
| **task**<br>_required_ | task ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/events/\#responses-13 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/events/#events-get_scalar_metrics_and_variants-response-200) |

**Response 200**

| Name | Schema |
| --- | --- |
| **metrics**<br>_optional_ | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/events/\#security-13 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /events.get\_task\_events [​](https://clear.ml/docs/latest/docs/references/api/events/\#post-eventsget_task_events "Direct link to POST /events.get_task_events")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/events/\#description-14 "Direct link to Description")

Scroll through task events, sorted by timestamp

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/events/\#parameters-14 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/events/#events-get_task_events-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **batch\_size**<br>_optional_ | Number of events to return each time (default 500) | integer |
| **event\_type**<br>_optional_ | Return only events of this type | string |
| **metrics**<br>_optional_ | List of metrics and variants | < [events.metric\_variants](https://clear.ml/docs/latest/docs/references/api/definitions#eventsmetric_variants) \> array |
| **model\_events**<br>_optional_ | If set then get retrieving model events. Otherwise task events <br>**Default** : `false` | boolean |
| **order**<br>_optional_ | 'asc' (default) or 'desc'. | enum (asc, desc) |
| **scroll\_id**<br>_optional_ | Pass this value on next call to get next page | string |
| **task**<br>_required_ | Task ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/events/\#responses-14 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/events/#events-get_task_events-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **events**<br>_optional_ | Events list | < object > array |
| **returned**<br>_optional_ | Number of results returned | integer |
| **scroll\_id**<br>_optional_ | Scroll ID for getting more results | string |
| **total**<br>_optional_ | Total number of results available for this query. In case there are more than <br>10000 results it is set to 10000 | number |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/events/\#security-14 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /events.get\_task\_latest\_scalar\_values [​](https://clear.ml/docs/latest/docs/references/api/events/\#post-eventsget_task_latest_scalar_values "Direct link to POST /events.get_task_latest_scalar_values")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/events/\#description-15 "Direct link to Description")

Get the tasks's latest scalar values

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/events/\#parameters-15 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/events/#events-get_task_latest_scalar_values-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **task**<br>_required_ | Task ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/events/\#responses-15 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/events/#events-get_task_latest_scalar_values-response-200) |

**Response 200**

| Name | Schema |
| --- | --- |
| **metrics**<br>_optional_ | < [metrics](https://clear.ml/docs/latest/docs/references/api/events/#events-get_task_latest_scalar_values-post-metrics) \> array |

**metrics**

| Name | Description | Schema |
| --- | --- | --- |
| **name**<br>_optional_ | Metric name | string |
| **variants**<br>_optional_ |  | < [variants](https://clear.ml/docs/latest/docs/references/api/events/#events-get_task_latest_scalar_values-post-metrics-variants) \> array |

**variants**

| Name | Description | Schema |
| --- | --- | --- |
| **last\_100\_value**<br>_optional_ | Average of 100 last reported values | number |
| **last\_value**<br>_optional_ | Last reported value | number |
| **name**<br>_optional_ | Variant name | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/events/\#security-15 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /events.get\_task\_log [​](https://clear.ml/docs/latest/docs/references/api/events/\#post-eventsget_task_log "Direct link to POST /events.get_task_log")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/events/\#description-16 "Direct link to Description")

Get 'log' events for this task

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/events/\#parameters-16 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/events/#events-get_task_log-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **batch\_size**<br>_optional_ | The amount of log events to return | integer |
| **from\_timestamp**<br>_optional_ | Epoch time in UTC ms to use as the navigation start. Optional. If not provided, <br>reference timestamp is determined by the 'navigate\_earlier' parameter (if true, <br>reference timestamp is the last timestamp and if false, reference timestamp is <br>the first timestamp) | number |
| **metrics**<br>_optional_ | List of metrics and variants | < [events.metric\_variants](https://clear.ml/docs/latest/docs/references/api/definitions#eventsmetric_variants) \> array |
| **navigate\_earlier**<br>_optional_ | If set then log events are retreived from the latest to the earliest ones (in <br>timestamp descending order, unless order='asc'). Otherwise from the earliest to <br>the latest ones (in timestamp ascending order, unless order='desc'). The <br>default is True | boolean |
| **order**<br>_optional_ | If set, changes the order in which log events are returned based on the value <br>of 'navigate\_earlier' | enum (asc, desc) |
| **task**<br>_required_ | Task ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/events/\#responses-16 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/events/#events-get_task_log-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **events**<br>_optional_ | Log items list | < object > array |
| **returned**<br>_optional_ | Number of log events returned | integer |
| **total**<br>_optional_ | Total number of log events available for this query. In case there are more <br>than 10000 events it is set to 10000 | number |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/events/\#security-16 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /events.get\_task\_metrics [​](https://clear.ml/docs/latest/docs/references/api/events/\#post-eventsget_task_metrics "Direct link to POST /events.get_task_metrics")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/events/\#description-17 "Direct link to Description")

For each task, get a list of metrics for which the requested event type was

reported

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/events/\#parameters-17 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/events/#events-get_task_metrics-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **event\_type**<br>_optional_ | Event type | [events.event\_type\_enum](https://clear.ml/docs/latest/docs/references/api/definitions#eventsevent_type_enum) |
| **model\_events**<br>_optional_ | If set then get metrics from model events. Otherwise from task events <br>**Default** : `false` | boolean |
| **tasks**<br>_required_ | Task IDs | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/events/\#responses-17 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/events/#events-get_task_metrics-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **metrics**<br>_optional_ | List of task with their metrics | < object > array |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/events/\#security-17 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /events.get\_task\_plots [​](https://clear.ml/docs/latest/docs/references/api/events/\#post-eventsget_task_plots "Direct link to POST /events.get_task_plots")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/events/\#description-18 "Direct link to Description")

Get all 'plot' events for this task

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/events/\#parameters-18 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/events/#events-get_task_plots-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **iters**<br>_optional_ | Max number of latest iterations for which to return plots | integer |
| **metrics**<br>_optional_ | List of metrics and variants | < [events.metric\_variants](https://clear.ml/docs/latest/docs/references/api/definitions#eventsmetric_variants) \> array |
| **model\_events**<br>_optional_ | If set then the retrieving model events. Otherwise task events <br>**Default** : `false` | boolean |
| **no\_scroll**<br>_optional_ | If Truethen no scroll is created. Suitable for one time calls <br>**Default** : `false` | boolean |
| **scroll\_id**<br>_optional_ | Scroll ID of previous call (used for getting more results) | string |
| **task**<br>_required_ | Task ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/events/\#responses-18 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/events/#events-get_task_plots-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **plots**<br>_optional_ | Plots list | < object > array |
| **returned**<br>_optional_ | Number of results returned | integer |
| **scroll\_id**<br>_optional_ | Scroll ID for getting more results | string |
| **total**<br>_optional_ | Total number of results available for this query. In case there are more than <br>10000 results it is set to 10000 | number |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/events/\#security-18 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /events.get\_task\_single\_value\_metrics [​](https://clear.ml/docs/latest/docs/references/api/events/\#post-eventsget_task_single_value_metrics "Direct link to POST /events.get_task_single_value_metrics")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/events/\#description-19 "Direct link to Description")

Get single value metrics for the passed tasks

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/events/\#parameters-19 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/events/#events-get_task_single_value_metrics-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **metrics**<br>_optional_ | List of metrics and variants | < [events.metric\_variants](https://clear.ml/docs/latest/docs/references/api/definitions#eventsmetric_variants) \> array |
| **model\_events**<br>_optional_ | If set then the retrieving model events. Otherwise task events <br>**Default** : `false` | boolean |
| **tasks**<br>_required_ | List of task Task IDs | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/events/\#responses-19 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [events.single\_value\_metrics\_response](https://clear.ml/docs/latest/docs/references/api/definitions#eventssingle_value_metrics_response) |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/events/\#security-19 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /events.get\_vector\_metrics\_and\_variants [​](https://clear.ml/docs/latest/docs/references/api/events/\#post-eventsget_vector_metrics_and_variants "Direct link to POST /events.get_vector_metrics_and_variants")

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/events/\#parameters-20 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/events/#events-get_vector_metrics_and_variants-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **model\_events**<br>_optional_ | If set then the retrieving model events. Otherwise task events <br>**Default** : `false` | boolean |
| **task**<br>_required_ | Task ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/events/\#responses-20 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/events/#events-get_vector_metrics_and_variants-response-200) |

**Response 200**

| Name | Schema |
| --- | --- |
| **metrics**<br>_optional_ | < object > array |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/events/\#security-20 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /events.multi\_task\_scalar\_metrics\_iter\_histogram [​](https://clear.ml/docs/latest/docs/references/api/events/\#post-eventsmulti_task_scalar_metrics_iter_histogram "Direct link to POST /events.multi_task_scalar_metrics_iter_histogram")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/events/\#description-20 "Direct link to Description")

Used to compare scalar stats histogram of multiple tasks

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/events/\#parameters-21 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/events/#events-multi_task_scalar_metrics_iter_histogram-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **key**<br>_optional_ | Histogram x axis to use: iter - iteration number iso\_time - event time as ISO <br>formatted string timestamp - event timestamp as milliseconds since epoch | [events.scalar\_key\_enum](https://clear.ml/docs/latest/docs/references/api/definitions#eventsscalar_key_enum) |
| **metrics**<br>_optional_ | List of metrics and variants | < [events.metric\_variants](https://clear.ml/docs/latest/docs/references/api/definitions#eventsmetric_variants) \> array |
| **model\_events**<br>_optional_ | If set then the retrieving model events. Otherwise task events <br>**Default** : `false` | boolean |
| **samples**<br>_optional_ | The amount of histogram points to return. Optional, the default value is 6000 | integer |
| **tasks**<br>_required_ | List of task Task IDs. Maximum amount of tasks is 100 | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/events/\#responses-21 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/events/\#security-21 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /events.next\_debug\_image\_sample [​](https://clear.ml/docs/latest/docs/references/api/events/\#post-eventsnext_debug_image_sample "Direct link to POST /events.next_debug_image_sample")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/events/\#description-21 "Direct link to Description")

Get the image for the next variant for the same iteration or for the next

iteration

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/events/\#parameters-22 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/events/#events-next_debug_image_sample-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **model\_events**<br>_optional_ | If set then the retrieving model debug images. Otherwise task debug images <br>**Default** : `false` | boolean |
| **navigate\_earlier**<br>_optional_ | If set then get the either previous variant event from the current iteration or <br>(if does not exist) the last variant event from the previous iteration. <br>Otherwise next variant event from the current iteration or first variant event <br>from the next iteration | boolean |
| **next\_iteration**<br>_optional_ | If set then navigate to the next/previous iteration <br>**Default** : `false` | boolean |
| **scroll\_id**<br>_required_ | Scroll ID from the previous call to get\_debug\_image\_sample | string |
| **task**<br>_required_ | Task ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/events/\#responses-22 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [events.debug\_image\_sample\_response](https://clear.ml/docs/latest/docs/references/api/definitions#eventsdebug_image_sample_response) |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/events/\#security-22 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /events.next\_plot\_sample [​](https://clear.ml/docs/latest/docs/references/api/events/\#post-eventsnext_plot_sample "Direct link to POST /events.next_plot_sample")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/events/\#description-22 "Direct link to Description")

Get the plot for the next metric for the same iteration or for the next

iteration

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/events/\#parameters-23 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/events/#events-next_plot_sample-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **model\_events**<br>_optional_ | If set then the retrieving model plots. Otherwise task plots <br>**Default** : `false` | boolean |
| **navigate\_earlier**<br>_optional_ | If set then get the either previous metric events from the current iteration or <br>(if does not exist) the last metric events from the previous iteration. <br>Otherwise next metric events from the current iteration or first metric events <br>from the next iteration | boolean |
| **next\_iteration**<br>_optional_ | If set then navigate to the next/previous iteration <br>**Default** : `false` | boolean |
| **scroll\_id**<br>_required_ | Scroll ID from the previous call to get\_plot\_sample | string |
| **task**<br>_required_ | Task ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/events/\#responses-23 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [events.plot\_sample\_response](https://clear.ml/docs/latest/docs/references/api/definitions#eventsplot_sample_response) |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/events/\#security-23 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /events.plots [​](https://clear.ml/docs/latest/docs/references/api/events/\#post-eventsplots "Direct link to POST /events.plots")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/events/\#description-23 "Direct link to Description")

Get plot events for the requested amount of iterations per each task

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/events/\#parameters-24 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/events/#events-plots-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **iters**<br>_optional_ | Max number of latest iterations for which to return plots | integer |
| **metrics**<br>_required_ | List of metrics and variants | < [events.task\_metric\_variants](https://clear.ml/docs/latest/docs/references/api/definitions#eventstask_metric_variants) \> array |
| **model\_events**<br>_optional_ | If set then the retrieving model plots. Otherwise task plots <br>**Default** : `false` | boolean |
| **navigate\_earlier**<br>_optional_ | If set then events are retreived from latest iterations to earliest ones. <br>Otherwise from earliest iterations to the latest. The default is True | boolean |
| **refresh**<br>_optional_ | If set then scroll will be moved to the latest iterations. The default is False | boolean |
| **scroll\_id**<br>_optional_ | Scroll ID of previous call (used for getting more results) | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/events/\#responses-24 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [events.plots\_response](https://clear.ml/docs/latest/docs/references/api/definitions#eventsplots_response) |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/events/\#security-24 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /events.scalar\_metrics\_iter\_histogram [​](https://clear.ml/docs/latest/docs/references/api/events/\#post-eventsscalar_metrics_iter_histogram "Direct link to POST /events.scalar_metrics_iter_histogram")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/events/\#description-24 "Direct link to Description")

Get histogram data of all the vector metrics and variants in the task

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/events/\#parameters-25 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/events/#events-scalar_metrics_iter_histogram-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **key**<br>_optional_ | Histogram x axis to use: iter - iteration number iso\_time - event time as ISO <br>formatted string timestamp - event timestamp as milliseconds since epoch | [events.scalar\_key\_enum](https://clear.ml/docs/latest/docs/references/api/definitions#eventsscalar_key_enum) |
| **metrics**<br>_optional_ | List of metrics and variants | < [events.metric\_variants](https://clear.ml/docs/latest/docs/references/api/definitions#eventsmetric_variants) \> array |
| **model\_events**<br>_optional_ | If set then the retrieving model events. Otherwise task events <br>**Default** : `false` | boolean |
| **samples**<br>_optional_ | The amount of histogram points to return (0 to return all the points). <br>Optional, the default value is 6000. | integer |
| **task**<br>_required_ | Task ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/events/\#responses-25 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/events/#events-scalar_metrics_iter_histogram-response-200) |

**Response 200**

| Name | Schema |
| --- | --- |
| **images**<br>_optional_ | < object > array |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/events/\#security-25 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /events.scalar\_metrics\_iter\_raw [​](https://clear.ml/docs/latest/docs/references/api/events/\#post-eventsscalar_metrics_iter_raw "Direct link to POST /events.scalar_metrics_iter_raw")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/events/\#description-25 "Direct link to Description")

Get raw data for a specific metric variants in the task

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/events/\#parameters-26 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/events/#events-scalar_metrics_iter_raw-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **batch\_size**<br>_optional_ | The number of data points to return for this call. Optional, the default value <br>is 10000. Maximum batch size is 200000 | integer |
| **count\_total**<br>_optional_ | Count the total number of data points. If false, total number of data points is <br>not counted and null is returned <br>**Default** : `false` | boolean |
| **key**<br>_optional_ | Array of x axis to return. Supported values: iter - iteration number timestamp <br>\- event timestamp as milliseconds since epoch | [events.scalar\_key\_enum](https://clear.ml/docs/latest/docs/references/api/definitions#eventsscalar_key_enum) |
| **metric**<br>_required_ | Metric and variants for which to return data points | [events.metric\_variants](https://clear.ml/docs/latest/docs/references/api/definitions#eventsmetric_variants) |
| **model\_events**<br>_optional_ | If set then the retrieving model events. Otherwise task events <br>**Default** : `false` | boolean |
| **scroll\_id**<br>_optional_ | Optional Scroll ID. Use to get more data points following a previous call | string |
| **task**<br>_required_ | Task ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/events/\#responses-26 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/events/#events-scalar_metrics_iter_raw-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **returned**<br>_optional_ | Number of data points returned in this call. If 0 results were returned, no <br>more results are avilable | integer |
| **scroll\_id**<br>_optional_ | Scroll ID. Use to get more data points when calling this endpoint again | string |
| **total**<br>_optional_ | Total data points count. If count\_total is false, null is returned | integer |
| **variants**<br>_optional_ | Raw data points for each variant | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/events/\#security-26 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /events.vector\_metrics\_iter\_histogram [​](https://clear.ml/docs/latest/docs/references/api/events/\#post-eventsvector_metrics_iter_histogram "Direct link to POST /events.vector_metrics_iter_histogram")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/events/\#description-26 "Direct link to Description")

Get histogram data of all the scalar metrics and variants in the task

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/events/\#parameters-27 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/events/#events-vector_metrics_iter_histogram-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **metric**<br>_required_ |  | string |
| **model\_events**<br>_optional_ | If set then the retrieving model events. Otherwise task events <br>**Default** : `false` | boolean |
| **task**<br>_required_ | Task ID | string |
| **variant**<br>_required_ |  | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/events/\#responses-27 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/events/#events-vector_metrics_iter_histogram-response-200) |

**Response 200**

| Name | Schema |
| --- | --- |
| **images**<br>_optional_ | < object > array |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/events/\#security-27 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

- [POST /events.add](https://clear.ml/docs/latest/docs/references/api/events/#post-eventsadd)
- [POST /events.add\_batch](https://clear.ml/docs/latest/docs/references/api/events/#post-eventsadd_batch)
- [POST /events.clear\_scroll](https://clear.ml/docs/latest/docs/references/api/events/#post-eventsclear_scroll)
- [POST /events.clear\_task\_log](https://clear.ml/docs/latest/docs/references/api/events/#post-eventsclear_task_log)
- [POST /events.debug\_images](https://clear.ml/docs/latest/docs/references/api/events/#post-eventsdebug_images)
- [POST /events.delete\_for\_model](https://clear.ml/docs/latest/docs/references/api/events/#post-eventsdelete_for_model)
- [POST /events.delete\_for\_task](https://clear.ml/docs/latest/docs/references/api/events/#post-eventsdelete_for_task)
- [POST /events.download\_task\_log](https://clear.ml/docs/latest/docs/references/api/events/#post-eventsdownload_task_log)
- [POST /events.get\_debug\_image\_sample](https://clear.ml/docs/latest/docs/references/api/events/#post-eventsget_debug_image_sample)
- [POST /events.get\_multi\_task\_metrics](https://clear.ml/docs/latest/docs/references/api/events/#post-eventsget_multi_task_metrics)
- [POST /events.get\_multi\_task\_plots](https://clear.ml/docs/latest/docs/references/api/events/#post-eventsget_multi_task_plots)
- [POST /events.get\_plot\_sample](https://clear.ml/docs/latest/docs/references/api/events/#post-eventsget_plot_sample)
- [POST /events.get\_scalar\_metric\_data](https://clear.ml/docs/latest/docs/references/api/events/#post-eventsget_scalar_metric_data)
- [POST /events.get\_scalar\_metrics\_and\_variants](https://clear.ml/docs/latest/docs/references/api/events/#post-eventsget_scalar_metrics_and_variants)
- [POST /events.get\_task\_events](https://clear.ml/docs/latest/docs/references/api/events/#post-eventsget_task_events)
- [POST /events.get\_task\_latest\_scalar\_values](https://clear.ml/docs/latest/docs/references/api/events/#post-eventsget_task_latest_scalar_values)
- [POST /events.get\_task\_log](https://clear.ml/docs/latest/docs/references/api/events/#post-eventsget_task_log)
- [POST /events.get\_task\_metrics](https://clear.ml/docs/latest/docs/references/api/events/#post-eventsget_task_metrics)
- [POST /events.get\_task\_plots](https://clear.ml/docs/latest/docs/references/api/events/#post-eventsget_task_plots)
- [POST /events.get\_task\_single\_value\_metrics](https://clear.ml/docs/latest/docs/references/api/events/#post-eventsget_task_single_value_metrics)
- [POST /events.get\_vector\_metrics\_and\_variants](https://clear.ml/docs/latest/docs/references/api/events/#post-eventsget_vector_metrics_and_variants)
- [POST /events.multi\_task\_scalar\_metrics\_iter\_histogram](https://clear.ml/docs/latest/docs/references/api/events/#post-eventsmulti_task_scalar_metrics_iter_histogram)
- [POST /events.next\_debug\_image\_sample](https://clear.ml/docs/latest/docs/references/api/events/#post-eventsnext_debug_image_sample)
- [POST /events.next\_plot\_sample](https://clear.ml/docs/latest/docs/references/api/events/#post-eventsnext_plot_sample)
- [POST /events.plots](https://clear.ml/docs/latest/docs/references/api/events/#post-eventsplots)
- [POST /events.scalar\_metrics\_iter\_histogram](https://clear.ml/docs/latest/docs/references/api/events/#post-eventsscalar_metrics_iter_histogram)
- [POST /events.scalar\_metrics\_iter\_raw](https://clear.ml/docs/latest/docs/references/api/events/#post-eventsscalar_metrics_iter_raw)
- [POST /events.vector\_metrics\_iter\_histogram](https://clear.ml/docs/latest/docs/references/api/events/#post-eventsvector_metrics_iter_histogram)