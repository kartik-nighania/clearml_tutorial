---
url: "https://clear.ml/docs/latest/docs/references/enterprise/workers/"
title: "workers | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/enterprise/workers/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

### POST /workers.cluster\_report [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#post-workerscluster_report "Direct link to POST /workers.cluster_report")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#description "Direct link to Description")

Report cluster properties. Should be called periodically so that the cluster

info does not expire.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#parameters "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-cluster_report-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **key**<br>_required_ | Unique cluster key that is used as a prefix in its workers ids | string |
| **partial**<br>_optional_ | For the partial cluster report need to sum up data from different reports to <br>get the cluster limits <br>**Default** : `false` | boolean |
| **properties**<br>_optional_ | Cluster properties | [properties](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-cluster_report-post-properties) |
| **resource\_groups**<br>_optional_ | resource\_groups | < string > array |
| **timeout**<br>_optional_ | Registration timeout in seconds. If timeout seconds have passed since the last <br>call to cluster\_report, the cluster info is automatically removed from the list <br>of the registered clusters | integer |
| **timestamp**<br>_required_ | UNIX time in seconds since epoch. | integer |
| **worker**<br>_optional_ | Worker ID. Should be specified for the partial cluster report | string |

**properties**

| Name | Description | Schema |
| --- | --- | --- |
| **max\_cpus**<br>_optional_ | The max amount of cpu cores that can be allocated in the cluster | number |
| **max\_gpus**<br>_optional_ | The max amount of gpu cores that can be allocated in the cluster | number |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#responses "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#security "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /workers.cluster\_unregister [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#post-workerscluster_unregister "Direct link to POST /workers.cluster_unregister")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#description-1 "Direct link to Description")

Unregister a cluster in the system

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#parameters-1 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-cluster_unregister-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **key**<br>_required_ | Unique cluster key | string |
| **partial**<br>_optional_ | For the partial cluster report need to sum up data from different reports to <br>get the cluster limits <br>**Default** : `false` | boolean |
| **worker**<br>_optional_ | Worker ID. Should be specified for the partial cluster report | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#responses-1 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-cluster_unregister-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **unregistered**<br>_optional_ | 1 if the cluster info was found and removed. Otherwise 0 | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#security-1 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /workers.download\_events\_log [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#post-workersdownload_events_log "Direct link to POST /workers.download_events_log")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#description-2 "Direct link to Description")

Dowloads worker events log

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#parameters-2 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-download_events_log-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **max\_age\_days**<br>_optional_ | The maximun age in days for retrieving the logs | integer |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#responses-2 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#security-2 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /workers.get\_activity\_report [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#post-workersget_activity_report "Direct link to POST /workers.get_activity_report")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#description-3 "Direct link to Description")

Returns count of active company workers in the selected time range.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#parameters-3 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_activity_report-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **from\_date**<br>_required_ | Starting time (in seconds from epoch) for collecting statistics | number |
| **interval**<br>_required_ | Time interval in seconds for a single statistics point. The minimal value is 1 | integer |
| **to\_date**<br>_required_ | Ending time (in seconds from epoch) for collecting statistics | number |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#responses-3 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_activity_report-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **active**<br>_optional_ | Activity series that include only workers that worked on a task in the given <br>time interval. | [workers.activity\_series](https://clear.ml/docs/latest/docs/references/enterprise/definitions#workersactivity_series) |
| **total**<br>_optional_ | Activity series that include all the workers that sent reports in the given <br>time interval. | [workers.activity\_series](https://clear.ml/docs/latest/docs/references/enterprise/definitions#workersactivity_series) |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#security-3 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /workers.get\_all [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#post-workersget_all "Direct link to POST /workers.get_all")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#description-4 "Direct link to Description")

Returns information on all registered workers.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#parameters-4 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_all-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **last\_seen**<br>_optional_ | Filter out workers not active for more than last\_seen seconds. A value or 0 or <br>'none' will disable the filter. | integer |
| **system\_tags**<br>_optional_ | The list of allowed worker system tags. Prepend tag value with '-' in order to <br>exclude | < string > array |
| **tags**<br>_optional_ | The list of allowed worker tags. Prepend tag value with '-' in order to exclude | < string > array |
| **worker\_pattern**<br>_optional_ | The worker name pattern. If specified then only matching keys returned | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#responses-4 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_all-response-200) |

**Response 200**

| Name | Schema |
| --- | --- |
| **workers**<br>_optional_ | < [workers.worker](https://clear.ml/docs/latest/docs/references/enterprise/definitions#workersworker) \> array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#security-4 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /workers.get\_count [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#post-workersget_count "Direct link to POST /workers.get_count")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#description-5 "Direct link to Description")

Returns the number of registered workers.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#parameters-5 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_count-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **last\_seen**<br>_optional_ | Filter out workers not active for more than last\_seen seconds. A value or 0 or <br>'none' will disable the filter. | integer |
| **system\_tags**<br>_optional_ | The list of allowed worker system tags. Prepend tag value with '-' in order to <br>exclude | < string > array |
| **tags**<br>_optional_ | The list of allowed worker tags. Prepend tag value with '-' in order to exclude | < string > array |
| **worker\_pattern**<br>_optional_ | The worker name pattern. If specified then only matching keys are counted | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#responses-5 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_count-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **count**<br>_optional_ | Workers count | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#security-5 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /workers.get\_metric\_keys [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#post-workersget_metric_keys "Direct link to POST /workers.get_metric_keys")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#description-6 "Direct link to Description")

Returns worker statistics metric keys grouped by categories.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#parameters-6 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_metric_keys-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **worker\_ids**<br>_optional_ | List of worker ids to collect metrics for. If not provided or empty then all <br>the company workers metrics are analyzed. | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#responses-6 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_metric_keys-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **categories**<br>_optional_ | List of unique metric categories found in the statistics of the requested <br>workers. | < [workers.metrics\_category](https://clear.ml/docs/latest/docs/references/enterprise/definitions#workersmetrics_category) \> array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#security-6 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /workers.get\_resource\_history [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#post-workersget_resource_history "Direct link to POST /workers.get_resource_history")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#description-7 "Direct link to Description")

Returns cpus and gpus count historgram in the passed dates range

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#parameters-7 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_resource_history-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **category**<br>_optional_ | Workers category for collecting statistics | string |
| **from\_date**<br>_required_ | Starting time (in seconds from epoch) for collecting statistics | number |
| **interval**<br>_required_ | Time interval in seconds for a single statistics point. The minimal value is 1 | integer |
| **resource\_group**<br>_optional_ | Workers resource group for collecting statistics | string |
| **resource\_type**<br>_optional_ | The type of the resources to return on the chart <br>**Default** : `"computation_count"` | enum (computation\_count, computation\_util, memory, storage, network) |
| **to\_date**<br>_required_ | Ending time (in seconds from epoch) for collecting statistics | number |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#responses-7 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_resource_history-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **avg\_cpu\_load**<br>_optional_ | Activity series that display the average cpu load percentage in the given time <br>interval. | [workers.resource\_usage\_series](https://clear.ml/docs/latest/docs/references/enterprise/definitions#workersresource_usage_series) |
| **avg\_gpu\_util**<br>_optional_ | Activity series that display the average gpu utilizations percentage in the <br>given time interval. | [workers.resource\_usage\_series](https://clear.ml/docs/latest/docs/references/enterprise/definitions#workersresource_usage_series) |
| **computed\_interval**<br>_optional_ | The inteval that was actually used for the histogram. May be larger then the <br>requested one | integer |
| **cpu\_count**<br>_optional_ | Activity series that display the number of unique cpus that reported in the <br>given time interval. | [workers.resource\_usage\_series](https://clear.ml/docs/latest/docs/references/enterprise/definitions#workersresource_usage_series) |
| **cpu\_idle\_count**<br>_optional_ | Activity series that display the number of unique cpus whose usage was below <br>predefined utilization threshold in the given time interval. | [workers.resource\_usage\_series](https://clear.ml/docs/latest/docs/references/enterprise/definitions#workersresource_usage_series) |
| **cpu\_max\_allowed**<br>_optional_ | Series of maximum CPUs declared by cluster reports at each interval. | [workers.resource\_usage\_series](https://clear.ml/docs/latest/docs/references/enterprise/definitions#workersresource_usage_series) |
| **gpu\_count**<br>_optional_ | Activity series that display the number of unique gpus that reported in the <br>given time interval. | [workers.resource\_usage\_series](https://clear.ml/docs/latest/docs/references/enterprise/definitions#workersresource_usage_series) |
| **gpu\_idle\_count**<br>_optional_ | Activity series that display the number of unique gpus whose usage was below <br>predefined utilization threshold in the given time interval. | [workers.resource\_usage\_series](https://clear.ml/docs/latest/docs/references/enterprise/definitions#workersresource_usage_series) |
| **gpu\_max\_allowed**<br>_optional_ | Series of maximum GPUs declared by cluster reports at each interval. | [workers.resource\_usage\_series](https://clear.ml/docs/latest/docs/references/enterprise/definitions#workersresource_usage_series) |
| **gpu\_ram\_free**<br>_optional_ | Activity series that display the total amount of free gpu memory in Gb in the <br>given time interval. | [workers.resource\_usage\_series](https://clear.ml/docs/latest/docs/references/enterprise/definitions#workersresource_usage_series) |
| **gpu\_ram\_total**<br>_optional_ | Activity series that display the total amount of gpu memory in Gb in the given <br>time interval. | [workers.resource\_usage\_series](https://clear.ml/docs/latest/docs/references/enterprise/definitions#workersresource_usage_series) |
| **home\_free**<br>_optional_ | Activity series that display free disk space percentage in the given time <br>interval. | [workers.resource\_usage\_series](https://clear.ml/docs/latest/docs/references/enterprise/definitions#workersresource_usage_series) |
| **network\_rx**<br>_optional_ | Activity series that display the network receive rate in Mb per second in the <br>given time interval. | [workers.resource\_usage\_series](https://clear.ml/docs/latest/docs/references/enterprise/definitions#workersresource_usage_series) |
| **network\_tx**<br>_optional_ | Activity series that display the network transfer rate in Mb per second in the <br>given time interval. | [workers.resource\_usage\_series](https://clear.ml/docs/latest/docs/references/enterprise/definitions#workersresource_usage_series) |
| **ram\_free**<br>_optional_ | Activity series that display the total amount of free ram in Gb in the given <br>time interval. | [workers.resource\_usage\_series](https://clear.ml/docs/latest/docs/references/enterprise/definitions#workersresource_usage_series) |
| **ram\_total**<br>_optional_ | Activity series that display the total amount of ram in Gb in the given time <br>interval. | [workers.resource\_usage\_series](https://clear.ml/docs/latest/docs/references/enterprise/definitions#workersresource_usage_series) |
| **worker\_count**<br>_optional_ | Activity series with the number of unique workers that reported in the given <br>time interval. | [workers.resource\_usage\_series](https://clear.ml/docs/latest/docs/references/enterprise/definitions#workersresource_usage_series) |
| **worker\_max\_allowed**<br>_optional_ | Series of maximum workers declared by cluster reports at each interval. | [workers.resource\_usage\_series](https://clear.ml/docs/latest/docs/references/enterprise/definitions#workersresource_usage_series) |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#security-7 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /workers.get\_resource\_thresholds [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#post-workersget_resource_thresholds "Direct link to POST /workers.get_resource_thresholds")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#description-8 "Direct link to Description")

Get company resource thresholds

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#parameters-8 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#responses-8 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_resource_thresholds-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **cpu\_load**<br>_optional_ | Average CPU load percentage | number |
| **gpu\_util**<br>_optional_ | Average GPU utilizaton percentage | number |
| **home\_free**<br>_optional_ | Free disk space percentage | number |
| **last\_update**<br>_optional_ | 1 if the thresholds were updated. 0 otherwise | integer |
| **ram\_free**<br>_optional_ | Free RAM in Gb | number |
| **updated\_by**<br>_optional_ | ID of the user who performed the last update | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#security-8 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /workers.get\_resource\_usages [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#post-workersget_resource_usages "Direct link to POST /workers.get_resource_usages")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#description-9 "Direct link to Description")

Get resource groups with their usages

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#parameters-9 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_resource_usages-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **events\_from\_date**<br>_optional_ | Starting time (in seconds from epoch) for retrieving events | number |
| **expand\_groups**<br>_optional_ | The keys of the groups for which separate worker usages will be returned | < string > array |
| **filters**<br>_optional_ | List of FilterRule ('OR' connection) | < string, [filters](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_resource_usages-post-filters) \> map |
| **last\_events**<br>_optional_ | The amount of last worker events to retrieve. Pass 0 in order not to retrieve <br>any | integer |

**filters**

| Name | Description | Schema |
| --- | --- | --- |
| **allowed\_values**<br>_optional_ | The list of allowed string values | < string > array |
| **max\_value**<br>_optional_ | Max value | number |
| **min\_value**<br>_optional_ | Min value | number |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#responses-9 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_resource_usages-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **categories**<br>_optional_ |  | < [categories](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_resource_usages-post-categories) \> array |
| **events**<br>_optional_ |  | < < string, [events](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_resource_usages-post-events) \> map > array |
| **resource\_groups**<br>_optional_ | resource\_groups | < [resource\_groups](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_resource_usages-post-resource_groups) \> array |
| **settings**<br>_optional_ |  | [settings](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_resource_usages-post-settings) |
| **total**<br>_optional_ |  | [total](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_resource_usages-post-total) |

**categories**

| Name | Description | Schema |
| --- | --- | --- |
| **cpus**<br>_optional_ |  | [cpus](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_resource_usages-post-categories-cpus) |
| **gpus**<br>_optional_ |  | [gpus](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_resource_usages-post-categories-gpus) |
| **key**<br>_optional_ | Category key | string |
| **workers**<br>_optional_ |  | [workers](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_resource_usages-post-categories-workers) |

**cpus**

| Name | Description | Schema |
| --- | --- | --- |
| **idle**<br>_optional_ | Idle count. CPU or GPU core is considered idle if it does not pass the <br>predefined utilization threshold. Worker is considered idle when all of its <br>cpus and gpus are idle | integer |
| **max\_allowed**<br>_optional_ | Max allowed count | number |
| **total**<br>_optional_ | Total count | integer |

**gpus**

| Name | Description | Schema |
| --- | --- | --- |
| **idle**<br>_optional_ | Idle count. CPU or GPU core is considered idle if it does not pass the <br>predefined utilization threshold. Worker is considered idle when all of its <br>cpus and gpus are idle | integer |
| **max\_allowed**<br>_optional_ | Max allowed count | number |
| **total**<br>_optional_ | Total count | integer |

**workers**

| Name | Description | Schema |
| --- | --- | --- |
| **idle**<br>_optional_ | Idle count. CPU or GPU core is considered idle if it does not pass the <br>predefined utilization threshold. Worker is considered idle when all of its <br>cpus and gpus are idle | integer |
| **max\_allowed**<br>_optional_ | Max allowed count | number |
| **total**<br>_optional_ | Total count | integer |

**events**

| Name | Description | Schema |
| --- | --- | --- |
| **event\_type**<br>_optional_ | Type of the worker event | enum (registered, unregistered, idle, busy) |
| **msg**<br>_optional_ | Additional event message | string |
| **resource\_group**<br>_optional_ | Worker resource group | string |
| **timestamp**<br>_optional_ | The time of the event | string (date) |
| **worker**<br>_optional_ | Worker ID | string |
| **worker\_category**<br>_optional_ | Worker category | string |

**resource\_groups**

| Name | Description | Schema |
| --- | --- | --- |
| **avg\_cpu\_load**<br>_optional_ | Average CPU usage in percents | [avg\_cpu\_load](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_resource_usages-post-resource_groups-avg_cpu_load) |
| **avg\_gpu\_util**<br>_optional_ | Average GPU usage in percents | [avg\_gpu\_util](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_resource_usages-post-resource_groups-avg_gpu_util) |
| **cpu\_count**<br>_optional_ | Total CPUs count | [cpu\_count](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_resource_usages-post-resource_groups-cpu_count) |
| **gpu\_count**<br>_optional_ | Total GPUs count | [gpu\_count](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_resource_usages-post-resource_groups-gpu_count) |
| **gpu\_ram\_free**<br>_optional_ | Total free GPU memory in Gb | [gpu\_ram\_free](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_resource_usages-post-resource_groups-gpu_ram_free) |
| **gpu\_ram\_total**<br>_optional_ | Total GPU memory in Gb | [gpu\_ram\_total](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_resource_usages-post-resource_groups-gpu_ram_total) |
| **home\_free**<br>_optional_ | The percentage of the user free storage | [home\_free](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_resource_usages-post-resource_groups-home_free) |
| **idle\_time**<br>_optional_ | Total idle time for the resource group in seconds. The cpu or gpu core is <br>considered idle if it does not pass the predefined utitilization threshold | [idle\_time](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_resource_usages-post-resource_groups-idle_time) |
| **key**<br>_optional_ | Key | string |
| **network\_rx**<br>_optional_ | Network received in Mbs | [network\_rx](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_resource_usages-post-resource_groups-network_rx) |
| **network\_tx**<br>_optional_ | Network transmitted in Mbs | [network\_tx](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_resource_usages-post-resource_groups-network_tx) |
| **ram\_free**<br>_optional_ | Total free RAM in Gb | [ram\_free](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_resource_usages-post-resource_groups-ram_free) |
| **ram\_total**<br>_optional_ | Total RAM in Gb | [ram\_total](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_resource_usages-post-resource_groups-ram_total) |
| **worker\_count**<br>_optional_ | The number of workers in the group | [worker\_count](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_resource_usages-post-resource_groups-worker_count) |
| **workers**<br>_optional_ |  | < [workers](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_resource_usages-post-resource_groups-workers) \> array |

**avg\_cpu\_load**

| Name | Description | Schema |
| --- | --- | --- |
| **alarm**<br>_optional_ | Alarm code. 0 or <pyhocon.config\_tree.NoneValue object at 0x7f6851f3a220>for no <br>alarm | integer |
| **value**<br>_optional_ | Value | number |

**avg\_gpu\_util**

| Name | Description | Schema |
| --- | --- | --- |
| **alarm**<br>_optional_ | Alarm code. 0 or <pyhocon.config\_tree.NoneValue object at 0x7f6851f3a220>for no <br>alarm | integer |
| **value**<br>_optional_ | Value | number |

**cpu\_count**

| Name | Description | Schema |
| --- | --- | --- |
| **alarm**<br>_optional_ | Alarm code. 0 or <pyhocon.config\_tree.NoneValue object at 0x7f6851f3a220>for no <br>alarm | integer |
| **value**<br>_optional_ | Value | number |

**gpu\_count**

| Name | Description | Schema |
| --- | --- | --- |
| **alarm**<br>_optional_ | Alarm code. 0 or <pyhocon.config\_tree.NoneValue object at 0x7f6851f3a220>for no <br>alarm | integer |
| **value**<br>_optional_ | Value | number |

**gpu\_ram\_free**

| Name | Description | Schema |
| --- | --- | --- |
| **alarm**<br>_optional_ | Alarm code. 0 or <pyhocon.config\_tree.NoneValue object at 0x7f6851f3a220>for no <br>alarm | integer |
| **value**<br>_optional_ | Value | number |

**gpu\_ram\_total**

| Name | Description | Schema |
| --- | --- | --- |
| **alarm**<br>_optional_ | Alarm code. 0 or <pyhocon.config\_tree.NoneValue object at 0x7f6851f3a220>for no <br>alarm | integer |
| **value**<br>_optional_ | Value | number |

**home\_free**

| Name | Description | Schema |
| --- | --- | --- |
| **alarm**<br>_optional_ | Alarm code. 0 or <pyhocon.config\_tree.NoneValue object at 0x7f6851f3a220>for no <br>alarm | integer |
| **value**<br>_optional_ | Value | number |

**idle\_time**

| Name | Description | Schema |
| --- | --- | --- |
| **alarm**<br>_optional_ | Alarm code. 0 or <pyhocon.config\_tree.NoneValue object at 0x7f6851f3a220>for no <br>alarm | integer |
| **value**<br>_optional_ | Value | number |

**network\_rx**

| Name | Description | Schema |
| --- | --- | --- |
| **alarm**<br>_optional_ | Alarm code. 0 or <pyhocon.config\_tree.NoneValue object at 0x7f6851f3a220>for no <br>alarm | integer |
| **value**<br>_optional_ | Value | number |

**network\_tx**

| Name | Description | Schema |
| --- | --- | --- |
| **alarm**<br>_optional_ | Alarm code. 0 or <pyhocon.config\_tree.NoneValue object at 0x7f6851f3a220>for no <br>alarm | integer |
| **value**<br>_optional_ | Value | number |

**ram\_free**

| Name | Description | Schema |
| --- | --- | --- |
| **alarm**<br>_optional_ | Alarm code. 0 or <pyhocon.config\_tree.NoneValue object at 0x7f6851f3a220>for no <br>alarm | integer |
| **value**<br>_optional_ | Value | number |

**ram\_total**

| Name | Description | Schema |
| --- | --- | --- |
| **alarm**<br>_optional_ | Alarm code. 0 or <pyhocon.config\_tree.NoneValue object at 0x7f6851f3a220>for no <br>alarm | integer |
| **value**<br>_optional_ | Value | number |

**worker\_count**

| Name | Description | Schema |
| --- | --- | --- |
| **alarm**<br>_optional_ | Alarm code. 0 or <pyhocon.config\_tree.NoneValue object at 0x7f6851f3a220>for no <br>alarm | integer |
| **value**<br>_optional_ | Value | number |

**workers**

| Name | Description | Schema |
| --- | --- | --- |
| **avg\_cpu\_load**<br>_optional_ | Average CPU usage in percents | [avg\_cpu\_load](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_resource_usages-post-resource_groups-workers-avg_cpu_load) |
| **avg\_gpu\_util**<br>_optional_ | Average GPU usage in percents | [avg\_gpu\_util](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_resource_usages-post-resource_groups-workers-avg_gpu_util) |
| **cpu\_count**<br>_optional_ | Total CPUs count | [cpu\_count](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_resource_usages-post-resource_groups-workers-cpu_count) |
| **gpu\_count**<br>_optional_ | Total GPUs count | [gpu\_count](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_resource_usages-post-resource_groups-workers-gpu_count) |
| **gpu\_ram\_free**<br>_optional_ | Total free GPU memory in Gb | [gpu\_ram\_free](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_resource_usages-post-resource_groups-workers-gpu_ram_free) |
| **gpu\_ram\_total**<br>_optional_ | Total GPU memory in Gb | [gpu\_ram\_total](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_resource_usages-post-resource_groups-workers-gpu_ram_total) |
| **home\_free**<br>_optional_ | The percentage of the user free storage | [home\_free](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_resource_usages-post-resource_groups-workers-home_free) |
| **id**<br>_optional_ | Worker ID | string |
| **idle\_time**<br>_optional_ | Total idle time for the resource group in seconds. The cpu or gpu core is <br>considered idle if it does not pass the predefined utitilization threshold | [idle\_time](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_resource_usages-post-resource_groups-workers-idle_time) |
| **key**<br>_optional_ | Key | string |
| **network\_rx**<br>_optional_ | Network received in Mbs | [network\_rx](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_resource_usages-post-resource_groups-workers-network_rx) |
| **network\_tx**<br>_optional_ | Network transmitted in Mbs | [network\_tx](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_resource_usages-post-resource_groups-workers-network_tx) |
| **ram\_free**<br>_optional_ | Total free RAM in Gb | [ram\_free](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_resource_usages-post-resource_groups-workers-ram_free) |
| **ram\_total**<br>_optional_ | Total RAM in Gb | [ram\_total](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_resource_usages-post-resource_groups-workers-ram_total) |

**avg\_cpu\_load**

| Name | Description | Schema |
| --- | --- | --- |
| **alarm**<br>_optional_ | Alarm code. 0 or <pyhocon.config\_tree.NoneValue object at 0x7f6851f3a220>for no <br>alarm | integer |
| **value**<br>_optional_ | Value | number |

**avg\_gpu\_util**

| Name | Description | Schema |
| --- | --- | --- |
| **alarm**<br>_optional_ | Alarm code. 0 or <pyhocon.config\_tree.NoneValue object at 0x7f6851f3a220>for no <br>alarm | integer |
| **value**<br>_optional_ | Value | number |

**cpu\_count**

| Name | Description | Schema |
| --- | --- | --- |
| **alarm**<br>_optional_ | Alarm code. 0 or <pyhocon.config\_tree.NoneValue object at 0x7f6851f3a220>for no <br>alarm | integer |
| **value**<br>_optional_ | Value | number |

**gpu\_count**

| Name | Description | Schema |
| --- | --- | --- |
| **alarm**<br>_optional_ | Alarm code. 0 or <pyhocon.config\_tree.NoneValue object at 0x7f6851f3a220>for no <br>alarm | integer |
| **value**<br>_optional_ | Value | number |

**gpu\_ram\_free**

| Name | Description | Schema |
| --- | --- | --- |
| **alarm**<br>_optional_ | Alarm code. 0 or <pyhocon.config\_tree.NoneValue object at 0x7f6851f3a220>for no <br>alarm | integer |
| **value**<br>_optional_ | Value | number |

**gpu\_ram\_total**

| Name | Description | Schema |
| --- | --- | --- |
| **alarm**<br>_optional_ | Alarm code. 0 or <pyhocon.config\_tree.NoneValue object at 0x7f6851f3a220>for no <br>alarm | integer |
| **value**<br>_optional_ | Value | number |

**home\_free**

| Name | Description | Schema |
| --- | --- | --- |
| **alarm**<br>_optional_ | Alarm code. 0 or <pyhocon.config\_tree.NoneValue object at 0x7f6851f3a220>for no <br>alarm | integer |
| **value**<br>_optional_ | Value | number |

**idle\_time**

| Name | Description | Schema |
| --- | --- | --- |
| **alarm**<br>_optional_ | Alarm code. 0 or <pyhocon.config\_tree.NoneValue object at 0x7f6851f3a220>for no <br>alarm | integer |
| **value**<br>_optional_ | Value | number |

**network\_rx**

| Name | Description | Schema |
| --- | --- | --- |
| **alarm**<br>_optional_ | Alarm code. 0 or <pyhocon.config\_tree.NoneValue object at 0x7f6851f3a220>for no <br>alarm | integer |
| **value**<br>_optional_ | Value | number |

**network\_tx**

| Name | Description | Schema |
| --- | --- | --- |
| **alarm**<br>_optional_ | Alarm code. 0 or <pyhocon.config\_tree.NoneValue object at 0x7f6851f3a220>for no <br>alarm | integer |
| **value**<br>_optional_ | Value | number |

**ram\_free**

| Name | Description | Schema |
| --- | --- | --- |
| **alarm**<br>_optional_ | Alarm code. 0 or <pyhocon.config\_tree.NoneValue object at 0x7f6851f3a220>for no <br>alarm | integer |
| **value**<br>_optional_ | Value | number |

**ram\_total**

| Name | Description | Schema |
| --- | --- | --- |
| **alarm**<br>_optional_ | Alarm code. 0 or <pyhocon.config\_tree.NoneValue object at 0x7f6851f3a220>for no <br>alarm | integer |
| **value**<br>_optional_ | Value | number |

**settings**

| Name | Description | Schema |
| --- | --- | --- |
| **used\_cpu\_threshold\_percentage**<br>_optional_ | CPU usage in percents above which the CPU is considered busy | integer |
| **used\_gpu\_threshold\_percentage**<br>_optional_ | GPU usage in percents above which the GPU is considered busy | integer |

**total**

| Name | Schema |
| --- | --- |
| **cpus**<br>_optional_ | [cpus](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_resource_usages-post-total-cpus) |
| **gpus**<br>_optional_ | [gpus](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_resource_usages-post-total-gpus) |
| **workers**<br>_optional_ | [workers](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_resource_usages-post-total-workers) |

**cpus**

| Name | Description | Schema |
| --- | --- | --- |
| **idle**<br>_optional_ | Idle count. CPU or GPU core is considered idle if it does not pass the <br>predefined utilization threshold. Worker is considered idle when all of its <br>cpus and gpus are idle | integer |
| **max\_allowed**<br>_optional_ | Max allowed count | number |
| **total**<br>_optional_ | Total count | integer |

**gpus**

| Name | Description | Schema |
| --- | --- | --- |
| **idle**<br>_optional_ | Idle count. CPU or GPU core is considered idle if it does not pass the <br>predefined utilization threshold. Worker is considered idle when all of its <br>cpus and gpus are idle | integer |
| **max\_allowed**<br>_optional_ | Max allowed count | number |
| **total**<br>_optional_ | Total count | integer |

**workers**

| Name | Description | Schema |
| --- | --- | --- |
| **idle**<br>_optional_ | Idle count. CPU or GPU core is considered idle if it does not pass the <br>predefined utilization threshold. Worker is considered idle when all of its <br>cpus and gpus are idle | integer |
| **max\_allowed**<br>_optional_ | Max allowed count | number |
| **total**<br>_optional_ | Total count | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#security-9 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /workers.get\_runtime\_properties [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#post-workersget_runtime_properties "Direct link to POST /workers.get_runtime_properties")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#description-10 "Direct link to Description")

Get runtime properties for a worker

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#parameters-10 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_runtime_properties-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **worker**<br>_required_ | Worker ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#responses-10 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_runtime_properties-response-200) |

**Response 200**

| Name | Schema |
| --- | --- |
| **runtime\_properties**<br>_optional_ | < [runtime\_properties](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_runtime_properties-post-runtime_properties) \> array |

**runtime\_properties**

| Name | Description | Schema |
| --- | --- | --- |
| **expiry**<br>_optional_ | Expiry (in seconds) for a runtime property | integer |
| **key**<br>_optional_ |  | string |
| **value**<br>_optional_ |  | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#security-10 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /workers.get\_stats [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#post-workersget_stats "Direct link to POST /workers.get_stats")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#description-11 "Direct link to Description")

Returns statistics for the selected workers and time range aggregated by date

intervals.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#parameters-11 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_stats-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **from\_date**<br>_required_ | Starting time (in seconds from epoch) for collecting statistics | number |
| **interval**<br>_required_ | Time interval in seconds for a single statistics point. The minimal value is 1 | integer |
| **items**<br>_required_ | List of metric keys and requested statistics | < [workers.stat\_item](https://clear.ml/docs/latest/docs/references/enterprise/definitions#workersstat_item) \> array |
| **split\_by\_resource**<br>_optional_ | If set then for GPU related keys return the per GPU charts in addition to the <br>aggregated one <br>**Default** : `false` | boolean |
| **split\_by\_variant**<br>_optional_ | Obsolete, please do not use <br>**Default** : `false` | boolean |
| **to\_date**<br>_required_ | Ending time (in seconds from epoch) for collecting statistics | number |
| **worker\_ids**<br>_optional_ | List of worker ids to collect metrics for. If not provided or empty then all <br>the company workers metrics are analyzed. | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#responses-11 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-get_stats-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **workers**<br>_optional_ | List of the requested workers with their statistics | < [workers.worker\_stats](https://clear.ml/docs/latest/docs/references/enterprise/definitions#workersworker_stats) \> array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#security-11 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /workers.listener\_report [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#post-workerslistener_report "Direct link to POST /workers.listener_report")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#description-12 "Direct link to Description")

Report listener status

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#parameters-12 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-listener_report-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_required_ | Listener ID | string |
| **name**<br>_optional_ | Listener name | string |
| **queues**<br>_optional_ | List of queue IDs reported by the listener | < string > array |
| **timeout**<br>_optional_ | Timeout in seconds | integer |
| **type**<br>_optional_ | Listener type | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#responses-12 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#security-12 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /workers.listener\_unregister [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#post-workerslistener_unregister "Direct link to POST /workers.listener_unregister")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#description-13 "Direct link to Description")

Unregister listener

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#parameters-13 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-listener_unregister-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_required_ | Listener ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#responses-13 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#security-13 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /workers.register [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#post-workersregister "Direct link to POST /workers.register")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#description-14 "Direct link to Description")

Register a worker in the system. Called by the Worker Daemon.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#parameters-14 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-register-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **queues**<br>_optional_ | List of queue IDs on which the worker is listening. | < string > array |
| **resources**<br>_optional_ | Resources that this worker uses | [resources](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-register-post-resources) |
| **system\_tags**<br>_optional_ | System tags for the worker | < string > array |
| **tags**<br>_optional_ | User tags for the worker | < string > array |
| **timeout**<br>_optional_ | Registration timeout in seconds. If timeout seconds have passed since the <br>worker's last call to register or status\_report, the worker is automatically <br>removed from the list of registered workers. | integer |
| **worker**<br>_required_ | Worker id. Must be unique in company. | string |

**resources**

| Name | Description | Schema |
| --- | --- | --- |
| **cpu\_usage**<br>_optional_ | CPU Usage | number |
| **gpu\_usage**<br>_optional_ | GPU Usage | number |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#responses-14 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#security-14 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /workers.set\_resource\_thresholds [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#post-workersset_resource_thresholds "Direct link to POST /workers.set_resource_thresholds")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#description-15 "Direct link to Description")

Set company resource thresholds. All the thresholds should be set. 0 or

<pyhocon.config\_tree.NoneValue object at 0x7f6851f3a220>means no threshold

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#parameters-15 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-set_resource_thresholds-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **cpu\_load**<br>_optional_ | Average CPU load percentage | number |
| **gpu\_util**<br>_optional_ | Average GPU utilizaton percentage | number |
| **home\_free**<br>_optional_ | Free disk space percentage | number |
| **ram\_free**<br>_optional_ | Free RAM in Gb | number |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#responses-15 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-set_resource_thresholds-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **updated**<br>_optional_ | 1 if the thresholds were updated. 0 otherwise | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#security-15 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /workers.set\_runtime\_properties [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#post-workersset_runtime_properties "Direct link to POST /workers.set_runtime_properties")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#description-16 "Direct link to Description")

Set runtime properties for a worker

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#parameters-16 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-set_runtime_properties-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **runtime\_properties**<br>_required_ | runtime\_properties | < [runtime\_properties](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-set_runtime_properties-post-runtime_properties) \> array |
| **worker**<br>_required_ | Worker ID | string |

**runtime\_properties**

| Name | Description | Schema |
| --- | --- | --- |
| **expiry**<br>_optional_ | Expiry (in seconds) for a runtime property. When set to null no expiry is set, <br>when set to 0 the specified key is removed | integer |
| **key**<br>_optional_ |  | string |
| **value**<br>_optional_ |  | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#responses-16 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-set_runtime_properties-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **added**<br>_optional_ | keys of runtime properties added to redis | < string > array |
| **errors**<br>_optional_ | errors for keys failed to be added to redis | < string > array |
| **removed**<br>_optional_ | keys of runtime properties removed from redis | < string > array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#security-16 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /workers.status\_report [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#post-workersstatus_report "Direct link to POST /workers.status_report")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#description-17 "Direct link to Description")

Called periodically by the worker daemon to report machine status

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#parameters-17 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-status_report-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **is\_daemon**<br>_optional_ | Whether the status report is for the daemon worker that should not be counted <br>in resource usages dashboard <br>**Default** : `false` | boolean |
| **machine\_stats**<br>_optional_ | The machine statistics. | [workers.machine\_stats](https://clear.ml/docs/latest/docs/references/enterprise/definitions#workersmachine_stats) |
| **queue**<br>_optional_ | ID of the queue from which task was received. If no queue is sent, the worker's <br>queue field will be cleared. | string |
| **queues**<br>_optional_ | List of queue IDs on which the worker is listening. If null, the worker's <br>queues list will not be updated. | < string > array |
| **system\_tags**<br>_optional_ | New system tags for the worker | < string > array |
| **tags**<br>_optional_ | New user tags for the worker | < string > array |
| **task**<br>_optional_ | ID of a task currently being run by the worker. If no task is sent, the <br>worker's task field will be cleared. | string |
| **timestamp**<br>_required_ | UNIX time in seconds since epoch. | integer |
| **worker**<br>_required_ | Worker id. | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#responses-17 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#security-17 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /workers.unregister [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#post-workersunregister "Direct link to POST /workers.unregister")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#description-18 "Direct link to Description")

Unregister a worker in the system. Called by the Worker Daemon.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#parameters-18 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/workers/#workers-unregister-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **worker**<br>_required_ | Worker id. Must be unique in company. | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#responses-18 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/workers/\#security-18 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

- [POST /workers.cluster\_report](https://clear.ml/docs/latest/docs/references/enterprise/workers/#post-workerscluster_report)
- [POST /workers.cluster\_unregister](https://clear.ml/docs/latest/docs/references/enterprise/workers/#post-workerscluster_unregister)
- [POST /workers.download\_events\_log](https://clear.ml/docs/latest/docs/references/enterprise/workers/#post-workersdownload_events_log)
- [POST /workers.get\_activity\_report](https://clear.ml/docs/latest/docs/references/enterprise/workers/#post-workersget_activity_report)
- [POST /workers.get\_all](https://clear.ml/docs/latest/docs/references/enterprise/workers/#post-workersget_all)
- [POST /workers.get\_count](https://clear.ml/docs/latest/docs/references/enterprise/workers/#post-workersget_count)
- [POST /workers.get\_metric\_keys](https://clear.ml/docs/latest/docs/references/enterprise/workers/#post-workersget_metric_keys)
- [POST /workers.get\_resource\_history](https://clear.ml/docs/latest/docs/references/enterprise/workers/#post-workersget_resource_history)
- [POST /workers.get\_resource\_thresholds](https://clear.ml/docs/latest/docs/references/enterprise/workers/#post-workersget_resource_thresholds)
- [POST /workers.get\_resource\_usages](https://clear.ml/docs/latest/docs/references/enterprise/workers/#post-workersget_resource_usages)
- [POST /workers.get\_runtime\_properties](https://clear.ml/docs/latest/docs/references/enterprise/workers/#post-workersget_runtime_properties)
- [POST /workers.get\_stats](https://clear.ml/docs/latest/docs/references/enterprise/workers/#post-workersget_stats)
- [POST /workers.listener\_report](https://clear.ml/docs/latest/docs/references/enterprise/workers/#post-workerslistener_report)
- [POST /workers.listener\_unregister](https://clear.ml/docs/latest/docs/references/enterprise/workers/#post-workerslistener_unregister)
- [POST /workers.register](https://clear.ml/docs/latest/docs/references/enterprise/workers/#post-workersregister)
- [POST /workers.set\_resource\_thresholds](https://clear.ml/docs/latest/docs/references/enterprise/workers/#post-workersset_resource_thresholds)
- [POST /workers.set\_runtime\_properties](https://clear.ml/docs/latest/docs/references/enterprise/workers/#post-workersset_runtime_properties)
- [POST /workers.status\_report](https://clear.ml/docs/latest/docs/references/enterprise/workers/#post-workersstatus_report)
- [POST /workers.unregister](https://clear.ml/docs/latest/docs/references/enterprise/workers/#post-workersunregister)