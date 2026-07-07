---
url: "https://clear.ml/docs/latest/docs/references/enterprise/serving/"
title: "serving | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/enterprise/serving/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

### POST /serving.container\_status\_report [​](https://clear.ml/docs/latest/docs/references/enterprise/serving/\#post-servingcontainer_status_report "Direct link to POST /serving.container_status_report")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/serving/\#description "Direct link to Description")

Container status report

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/serving/\#parameters "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/serving/#serving-container_status_report-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **container\_id**<br>_required_ | Container ID. Should uniquely identify a specific container instance | string |
| **endpoint\_name**<br>_required_ | Endpoint name | string |
| **endpoint\_url**<br>_optional_ | Endpoint URL | string |
| **input\_size**<br>_optional_ | Input size | string |
| **input\_type**<br>_optional_ | Input type | string |
| **latency\_ms**<br>_optional_ | Average request latency in ms | integer |
| **machine\_stats**<br>_optional_ | The machine statistics | [serving.machine\_stats](https://clear.ml/docs/latest/docs/references/enterprise/definitions#servingmachine_stats) |
| **model\_name**<br>_required_ | Model name | string |
| **model\_source**<br>_optional_ | Model source | string |
| **model\_version**<br>_optional_ | Model version | string |
| **preprocess\_artifact**<br>_optional_ | Preprocess Artifact | string |
| **reference**<br>_optional_ | Array of reference items provided by the container instance. Can contain <br>multiple reference items with the same type | < [reference](https://clear.ml/docs/latest/docs/references/enterprise/serving/#serving-container_status_report-post-reference) \> array |
| **requests\_min**<br>_optional_ | Average requests per minute | number |
| **requests\_num**<br>_optional_ | Number of requests | integer |
| **uptime\_sec**<br>_optional_ | Uptime in seconds | integer |

**reference**

| Name | Description | Schema |
| --- | --- | --- |
| **type**<br>_required_ | The type of the reference item | enum (app\_id, app\_instance, model, task, url) |
| **value**<br>_required_ | The reference item value | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/serving/\#responses "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/serving/\#security "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /serving.get\_endpoint\_details [​](https://clear.ml/docs/latest/docs/references/enterprise/serving/\#post-servingget_endpoint_details "Direct link to POST /serving.get_endpoint_details")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/serving/\#description-1 "Direct link to Description")

Get endpoint details

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/serving/\#parameters-1 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/serving/#serving-get_endpoint_details-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **endpoint\_url**<br>_required_ | Endpoint URL | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/serving/\#responses-1 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/serving/#serving-get_endpoint_details-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **endpoint**<br>_optional_ | Endpoint name | string |
| **input\_size**<br>_optional_ | Input size | string |
| **input\_type**<br>_optional_ | Input type | string |
| **instances**<br>_optional_ |  | < [serving.container\_instance\_stats](https://clear.ml/docs/latest/docs/references/enterprise/definitions#servingcontainer_instance_stats) \> array |
| **last\_update**<br>_optional_ | The latest time when one of the model instances was updated | string (date-time) |
| **model**<br>_optional_ | Model name | string |
| **model\_source**<br>_optional_ | Model source | string |
| **model\_version**<br>_optional_ | Model version | string |
| **preprocess\_artifact**<br>_optional_ | Preprocess Artifact | string |
| **uptime\_sec**<br>_optional_ | Max of model instance uptime in seconds | integer |
| **url**<br>_optional_ | Model url | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/serving/\#security-1 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /serving.get\_endpoint\_metrics\_history [​](https://clear.ml/docs/latest/docs/references/enterprise/serving/\#post-servingget_endpoint_metrics_history "Direct link to POST /serving.get_endpoint_metrics_history")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/serving/\#description-2 "Direct link to Description")

Get endpoint charts

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/serving/\#parameters-2 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/serving/#serving-get_endpoint_metrics_history-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **endpoint\_url**<br>_required_ | Endpoint Url | string |
| **from\_date**<br>_required_ | Starting time (in seconds from epoch) for collecting statistics | number |
| **instance\_charts**<br>_optional_ | If set then return instance charts and total. Otherwise total only <br>**Default** : `true` | boolean |
| **interval**<br>_required_ | Time interval in seconds for a single statistics point. The minimal value is 1 | integer |
| **metric\_type**<br>_optional_ | The type of the metrics to return on the chart <br>**Default** : `"requests"` | enum (requests, requests\_min, latency\_ms, cpu\_count, gpu\_count, cpu\_util, gpu\_util, ram\_total, ram\_used, ram\_free, gpu\_ram\_total, gpu\_ram\_used, gpu\_ram\_free, network\_rx, network\_tx) |
| **to\_date**<br>_required_ | Ending time (in seconds from epoch) for collecting statistics | number |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/serving/\#responses-2 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/serving/#serving-get_endpoint_metrics_history-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **computed\_interval**<br>_optional_ | The inteval that was actually used for the histogram. May be larger then the <br>requested one | integer |
| **instances**<br>_optional_ | Instance charts | < string, [instances](https://clear.ml/docs/latest/docs/references/enterprise/serving/#serving-get_endpoint_metrics_history-post-instances) \> map |
| **total**<br>_optional_ | The total histogram | [total](https://clear.ml/docs/latest/docs/references/enterprise/serving/#serving-get_endpoint_metrics_history-post-total) |

**instances**

| Name | Description | Schema |
| --- | --- | --- |
| **dates**<br>_optional_ | List of timestamps (in seconds from epoch) in the acceding order. The <br>timestamps are separated by the requested interval. | < integer > array |
| **title**<br>_optional_ | The title of the series | string |
| **values**<br>_optional_ | List of values corresponding to the timestamps in the dates list. | < number > array |

**total**

| Name | Description | Schema |
| --- | --- | --- |
| **dates**<br>_optional_ | List of timestamps (in seconds from epoch) in the acceding order. The <br>timestamps are separated by the requested interval. | < integer > array |
| **title**<br>_optional_ | The title of the series | string |
| **values**<br>_optional_ | List of values corresponding to the timestamps in the dates list. | < number > array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/serving/\#security-2 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /serving.get\_endpoints [​](https://clear.ml/docs/latest/docs/references/enterprise/serving/\#post-servingget_endpoints "Direct link to POST /serving.get_endpoints")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/serving/\#description-3 "Direct link to Description")

Get all the registered endpoints

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/serving/\#parameters-3 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/serving/\#responses-3 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/serving/#serving-get_endpoints-response-200) |

**Response 200**

| Name | Schema |
| --- | --- |
| **endpoints**<br>_optional_ | < [serving.endpoint\_stats](https://clear.ml/docs/latest/docs/references/enterprise/definitions#servingendpoint_stats) \> array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/serving/\#security-3 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /serving.get\_loading\_instances [​](https://clear.ml/docs/latest/docs/references/enterprise/serving/\#post-servingget_loading_instances "Direct link to POST /serving.get_loading_instances")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/serving/\#description-4 "Direct link to Description")

Get loading instances (enpoint\_url not set yet)

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/serving/\#parameters-4 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/serving/\#responses-4 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/serving/#serving-get_loading_instances-response-200) |

**Response 200**

| Name | Schema |
| --- | --- |
| **instances**<br>_optional_ | < [serving.container\_info](https://clear.ml/docs/latest/docs/references/enterprise/definitions#servingcontainer_info) \> array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/serving/\#security-4 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /serving.register\_container [​](https://clear.ml/docs/latest/docs/references/enterprise/serving/\#post-servingregister_container "Direct link to POST /serving.register_container")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/serving/\#description-5 "Direct link to Description")

Register container

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/serving/\#parameters-5 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/serving/#serving-register_container-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **container\_id**<br>_required_ | Container ID. Should uniquely identify a specific container instance | string |
| **endpoint\_name**<br>_required_ | Endpoint name | string |
| **endpoint\_url**<br>_optional_ | Endpoint URL | string |
| **input\_size**<br>_optional_ | Input size | string |
| **input\_type**<br>_optional_ | Input type | string |
| **model\_name**<br>_required_ | Model name | string |
| **model\_source**<br>_optional_ | Model source | string |
| **model\_version**<br>_optional_ | Model version | string |
| **preprocess\_artifact**<br>_optional_ | Preprocess Artifact | string |
| **reference**<br>_optional_ | Array of reference items provided by the container instance. Can contain <br>multiple reference items with the same type | < [reference](https://clear.ml/docs/latest/docs/references/enterprise/serving/#serving-register_container-post-reference) \> array |
| **timeout**<br>_optional_ | Registration timeout in seconds. If timeout seconds have passed since the <br>service container last call to register or status\_report, the container is <br>automatically removed from the list of registered containers. | integer |

**reference**

| Name | Description | Schema |
| --- | --- | --- |
| **type**<br>_required_ | The type of the reference item | enum (app\_id, app\_instance, model, task, url) |
| **value**<br>_required_ | The reference item value | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/serving/\#responses-5 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/serving/\#security-5 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /serving.unregister\_container [​](https://clear.ml/docs/latest/docs/references/enterprise/serving/\#post-servingunregister_container "Direct link to POST /serving.unregister_container")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/serving/\#description-6 "Direct link to Description")

Unregister container

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/serving/\#parameters-6 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/serving/#serving-unregister_container-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **container\_id**<br>_required_ | Container ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/serving/\#responses-6 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/serving/\#security-6 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

- [POST /serving.container\_status\_report](https://clear.ml/docs/latest/docs/references/enterprise/serving/#post-servingcontainer_status_report)
- [POST /serving.get\_endpoint\_details](https://clear.ml/docs/latest/docs/references/enterprise/serving/#post-servingget_endpoint_details)
- [POST /serving.get\_endpoint\_metrics\_history](https://clear.ml/docs/latest/docs/references/enterprise/serving/#post-servingget_endpoint_metrics_history)
- [POST /serving.get\_endpoints](https://clear.ml/docs/latest/docs/references/enterprise/serving/#post-servingget_endpoints)
- [POST /serving.get\_loading\_instances](https://clear.ml/docs/latest/docs/references/enterprise/serving/#post-servingget_loading_instances)
- [POST /serving.register\_container](https://clear.ml/docs/latest/docs/references/enterprise/serving/#post-servingregister_container)
- [POST /serving.unregister\_container](https://clear.ml/docs/latest/docs/references/enterprise/serving/#post-servingunregister_container)