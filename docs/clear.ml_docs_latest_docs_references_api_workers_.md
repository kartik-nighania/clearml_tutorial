---
url: "https://clear.ml/docs/latest/docs/references/api/workers/"
title: "workers | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/api/workers/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

### POST /workers.get\_activity\_report [​](https://clear.ml/docs/latest/docs/references/api/workers/\#post-workersget_activity_report "Direct link to POST /workers.get_activity_report")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/workers/\#description "Direct link to Description")

Returns count of active company workers in the selected time range.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/workers/\#parameters "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/workers/#workers-get_activity_report-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **from\_date**<br>_required_ | Starting time (in seconds from epoch) for collecting statistics | number |
| **interval**<br>_required_ | Time interval in seconds for a single statistics point. The minimal value is 1 | integer |
| **to\_date**<br>_required_ | Ending time (in seconds from epoch) for collecting statistics | number |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/workers/\#responses "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/workers/#workers-get_activity_report-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **active**<br>_optional_ | Activity series that include only workers that worked on a task in the given <br>time interval. | [workers.activity\_series](https://clear.ml/docs/latest/docs/references/api/definitions#workersactivity_series) |
| **total**<br>_optional_ | Activity series that include all the workers that sent reports in the given <br>time interval. | [workers.activity\_series](https://clear.ml/docs/latest/docs/references/api/definitions#workersactivity_series) |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/workers/\#security "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /workers.get\_all [​](https://clear.ml/docs/latest/docs/references/api/workers/\#post-workersget_all "Direct link to POST /workers.get_all")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/workers/\#description-1 "Direct link to Description")

Returns information on all registered workers.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/workers/\#parameters-1 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/workers/#workers-get_all-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **last\_seen**<br>_optional_ | Filter out workers not active for more than last\_seen seconds. A value or 0 or <br>'none' will disable the filter. | integer |
| **system\_tags**<br>_optional_ | The list of allowed worker system tags. Prepend tag value with '-' in order to <br>exclude | < string > array |
| **tags**<br>_optional_ | The list of allowed worker tags. Prepend tag value with '-' in order to exclude | < string > array |
| **worker\_pattern**<br>_optional_ | The worker name pattern. If specified then only matching keys returned | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/workers/\#responses-1 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/workers/#workers-get_all-response-200) |

**Response 200**

| Name | Schema |
| --- | --- |
| **workers**<br>_optional_ | < [workers.worker](https://clear.ml/docs/latest/docs/references/api/definitions#workersworker) \> array |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/workers/\#security-1 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /workers.get\_count [​](https://clear.ml/docs/latest/docs/references/api/workers/\#post-workersget_count "Direct link to POST /workers.get_count")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/workers/\#description-2 "Direct link to Description")

Returns the number of registered workers.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/workers/\#parameters-2 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/workers/#workers-get_count-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **last\_seen**<br>_optional_ | Filter out workers not active for more than last\_seen seconds. A value or 0 or <br>'none' will disable the filter. | integer |
| **system\_tags**<br>_optional_ | The list of allowed worker system tags. Prepend tag value with '-' in order to <br>exclude | < string > array |
| **tags**<br>_optional_ | The list of allowed worker tags. Prepend tag value with '-' in order to exclude | < string > array |
| **worker\_pattern**<br>_optional_ | The worker name pattern. If specified then only matching keys are counted | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/workers/\#responses-2 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/workers/#workers-get_count-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **count**<br>_optional_ | Workers count | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/workers/\#security-2 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /workers.get\_metric\_keys [​](https://clear.ml/docs/latest/docs/references/api/workers/\#post-workersget_metric_keys "Direct link to POST /workers.get_metric_keys")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/workers/\#description-3 "Direct link to Description")

Returns worker statistics metric keys grouped by categories.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/workers/\#parameters-3 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/workers/#workers-get_metric_keys-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **worker\_ids**<br>_optional_ | List of worker ids to collect metrics for. If not provided or empty then all <br>the company workers metrics are analyzed. | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/workers/\#responses-3 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/workers/#workers-get_metric_keys-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **categories**<br>_optional_ | List of unique metric categories found in the statistics of the requested <br>workers. | < [workers.metrics\_category](https://clear.ml/docs/latest/docs/references/api/definitions#workersmetrics_category) \> array |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/workers/\#security-3 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /workers.get\_stats [​](https://clear.ml/docs/latest/docs/references/api/workers/\#post-workersget_stats "Direct link to POST /workers.get_stats")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/workers/\#description-4 "Direct link to Description")

Returns statistics for the selected workers and time range aggregated by date

intervals.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/workers/\#parameters-4 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/workers/#workers-get_stats-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **from\_date**<br>_required_ | Starting time (in seconds from epoch) for collecting statistics | number |
| **interval**<br>_required_ | Time interval in seconds for a single statistics point. The minimal value is 1 | integer |
| **items**<br>_required_ | List of metric keys and requested statistics | < [workers.stat\_item](https://clear.ml/docs/latest/docs/references/api/definitions#workersstat_item) \> array |
| **split\_by\_resource**<br>_optional_ | If set then for GPU related keys return the per GPU charts in addition to the <br>aggregated one <br>**Default** : `false` | boolean |
| **split\_by\_variant**<br>_optional_ | Obsolete, please do not use <br>**Default** : `false` | boolean |
| **to\_date**<br>_required_ | Ending time (in seconds from epoch) for collecting statistics | number |
| **worker\_ids**<br>_optional_ | List of worker ids to collect metrics for. If not provided or empty then all <br>the company workers metrics are analyzed. | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/workers/\#responses-4 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/workers/#workers-get_stats-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **workers**<br>_optional_ | List of the requested workers with their statistics | < [workers.worker\_stats](https://clear.ml/docs/latest/docs/references/api/definitions#workersworker_stats) \> array |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/workers/\#security-4 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /workers.register [​](https://clear.ml/docs/latest/docs/references/api/workers/\#post-workersregister "Direct link to POST /workers.register")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/workers/\#description-5 "Direct link to Description")

Register a worker in the system. Called by the Worker Daemon.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/workers/\#parameters-5 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/workers/#workers-register-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **queues**<br>_optional_ | List of queue IDs on which the worker is listening. | < string > array |
| **resources**<br>_optional_ | Resources that this worker uses | [resources](https://clear.ml/docs/latest/docs/references/api/workers/#workers-register-post-resources) |
| **system\_tags**<br>_optional_ | System tags for the worker | < string > array |
| **tags**<br>_optional_ | User tags for the worker | < string > array |
| **timeout**<br>_optional_ | Registration timeout in seconds. If timeout seconds have passed since the <br>worker's last call to register or status\_report, the worker is automatically <br>removed from the list of registered workers. | integer |
| **worker**<br>_required_ | Worker id. Must be unique in company. | string |

**resources**

| Name | Description | Schema |
| --- | --- | --- |
| **cpu\_usage**<br>_optional_ | CPU Usage | number |
| **gpu\_usage**<br>_optional_ | GPU Usage | number |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/workers/\#responses-5 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/workers/\#security-5 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /workers.status\_report [​](https://clear.ml/docs/latest/docs/references/api/workers/\#post-workersstatus_report "Direct link to POST /workers.status_report")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/workers/\#description-6 "Direct link to Description")

Called periodically by the worker daemon to report machine status

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/workers/\#parameters-6 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/workers/#workers-status_report-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **machine\_stats**<br>_optional_ | The machine statistics. | [workers.machine\_stats](https://clear.ml/docs/latest/docs/references/api/definitions#workersmachine_stats) |
| **queue**<br>_optional_ | ID of the queue from which task was received. If no queue is sent, the worker's <br>queue field will be cleared. | string |
| **queues**<br>_optional_ | List of queue IDs on which the worker is listening. If null, the worker's <br>queues list will not be updated. | < string > array |
| **system\_tags**<br>_optional_ | New system tags for the worker | < string > array |
| **tags**<br>_optional_ | New user tags for the worker | < string > array |
| **task**<br>_optional_ | ID of a task currently being run by the worker. If no task is sent, the <br>worker's task field will be cleared. | string |
| **timestamp**<br>_required_ | UNIX time in seconds since epoch. | integer |
| **worker**<br>_required_ | Worker id. | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/workers/\#responses-6 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/workers/\#security-6 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /workers.unregister [​](https://clear.ml/docs/latest/docs/references/api/workers/\#post-workersunregister "Direct link to POST /workers.unregister")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/workers/\#description-7 "Direct link to Description")

Unregister a worker in the system. Called by the Worker Daemon.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/workers/\#parameters-7 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/workers/#workers-unregister-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **worker**<br>_required_ | Worker id. Must be unique in company. | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/workers/\#responses-7 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/workers/\#security-7 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

- [POST /workers.get\_activity\_report](https://clear.ml/docs/latest/docs/references/api/workers/#post-workersget_activity_report)
- [POST /workers.get\_all](https://clear.ml/docs/latest/docs/references/api/workers/#post-workersget_all)
- [POST /workers.get\_count](https://clear.ml/docs/latest/docs/references/api/workers/#post-workersget_count)
- [POST /workers.get\_metric\_keys](https://clear.ml/docs/latest/docs/references/api/workers/#post-workersget_metric_keys)
- [POST /workers.get\_stats](https://clear.ml/docs/latest/docs/references/api/workers/#post-workersget_stats)
- [POST /workers.register](https://clear.ml/docs/latest/docs/references/api/workers/#post-workersregister)
- [POST /workers.status\_report](https://clear.ml/docs/latest/docs/references/api/workers/#post-workersstatus_report)
- [POST /workers.unregister](https://clear.ml/docs/latest/docs/references/api/workers/#post-workersunregister)