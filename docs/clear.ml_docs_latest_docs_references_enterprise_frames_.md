---
url: "https://clear.ml/docs/latest/docs/references/enterprise/frames/"
title: "frames | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/enterprise/frames/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

### POST /frames.clear\_get\_next\_state [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#post-framesclear_get_next_state "Direct link to POST /frames.clear_get_next_state")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#description "Direct link to Description")

Clears the scroll state received from the get\_next family of functions and

releases all of its resources

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#parameters "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/frames/#frames-clear_get_next_state-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **scroll\_id**<br>_required_ | Scroll session id | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#responses "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#security "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /frames.download\_for\_dataview [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#post-framesdownload_for_dataview "Direct link to POST /frames.download_for_dataview")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#description-1 "Direct link to Description")

Get an attachment containing the frames returned by the dataview specified in

`prepare_download_for_dataview`

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#parameters-1 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/frames/#frames-download_for_dataview-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **prepare\_id**<br>_required_ | Call ID returned by a call to prepare\_download\_for\_dataview | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#responses-1 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#security-1 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /frames.get\_by\_id [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#post-framesget_by_id "Direct link to POST /frames.get_by_id")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#description-2 "Direct link to Description")

Get a specific frame for a dataset version using the frame's id. Random Access

API.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#parameters-2 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/frames/#frames-get_by_id-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **dataset**<br>_required_ | Dataset id | string |
| **frame**<br>_required_ | Frame id | string |
| **projection**<br>_optional_ | Used to select which parts of the frame will be returned. Each string <br>represents a field or sub-field (using dot-separated notation). In order to <br>specify a specific array element, use array index as a field name. To specify <br>all array elements, use '\*'. | < string > array |
| **version**<br>_required_ | Version id | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#responses-2 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/frames/#frames-get_by_id-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **frame**<br>_optional_ | Frame data | [frames.frame](https://clear.ml/docs/latest/docs/references/enterprise/definitions#framesframe) |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#security-2 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /frames.get\_by\_ids [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#post-framesget_by_ids "Direct link to POST /frames.get_by_ids")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#description-3 "Direct link to Description")

Get specific frames for a dataset version using the frame ids. Random Access

API.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#parameters-3 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/frames/#frames-get_by_ids-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **dataset**<br>_required_ | Dataset ID | string |
| **frame\_ids**<br>_required_ | Frame IDs | < string > array |
| **projection**<br>_optional_ | Used to select which parts of the frame will be returned. Each string <br>represents a field or sub-field (using dot-separated notation). In order to <br>specify a specific array element, use array index as a field name. To specify <br>all array elements, use '\*'. | < string > array |
| **version**<br>_required_ | Version ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#responses-3 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/frames/#frames-get_by_ids-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **frames**<br>_optional_ | Frames data | < [frames.frame](https://clear.ml/docs/latest/docs/references/enterprise/definitions#framesframe) \> array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#security-3 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /frames.get\_count [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#post-framesget_count "Direct link to POST /frames.get_count")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#description-4 "Direct link to Description")

Gets the count of frames who's ROIs contain at least one of the given label(s)

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#parameters-4 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/frames/#frames-get_count-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **dataset**<br>_optional_ | Dataset id | string |
| **labels**<br>_optional_ | List of labels. Only frames containing labels from this list should be counted. <br>Used only if scroll\_id is not provided. | < string > array |
| **version**<br>_required_ | Dataset version id | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#responses-4 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/frames/#frames-get_count-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **total**<br>_optional_ | Total count of frames for the entire query. | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#security-4 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /frames.get\_count\_for\_dataview [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#post-framesget_count_for_dataview "Direct link to POST /frames.get_count_for_dataview")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#description-5 "Direct link to Description")

Gets the count of frames matching the given dataview

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#parameters-5 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/frames/#frames-get_count_for_dataview-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **dataview**<br>_required_ | Dataview specification | [frames.dataview](https://clear.ml/docs/latest/docs/references/enterprise/definitions#framesdataview) |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#responses-5 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/frames/#frames-get_count_for_dataview-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **rules**<br>_optional_ | Specific information for each rule of this query. | < [frames.rule\_count](https://clear.ml/docs/latest/docs/references/enterprise/definitions#framesrule_count) \> array |
| **total**<br>_optional_ | Total count of frames for the entire query. | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#security-5 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /frames.get\_count\_for\_dataview\_id [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#post-framesget_count_for_dataview_id "Direct link to POST /frames.get_count_for_dataview_id")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#description-6 "Direct link to Description")

Gets the count of frames matching the given dataview

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#parameters-6 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/frames/#frames-get_count_for_dataview_id-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **dataview**<br>_required_ | Dataview ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#responses-6 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/frames/#frames-get_count_for_dataview_id-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **rules**<br>_optional_ | Specific information for each rule of this query. | < [frames.rule\_count](https://clear.ml/docs/latest/docs/references/enterprise/definitions#framesrule_count) \> array |
| **total**<br>_optional_ | Total count of frames for the entire query. | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#security-6 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /frames.get\_group\_snippets\_for\_dataview [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#post-framesget_group_snippets_for_dataview "Direct link to POST /frames.get_group_snippets_for_dataview")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#description-7 "Direct link to Description")

Get sample frames for the specified aggregation group

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#parameters-7 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/frames/#frames-get_group_snippets_for_dataview-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **dataview**<br>_optional_ | Dataview specification | [frames.dataview](https://clear.ml/docs/latest/docs/references/enterprise/definitions#framesdataview) |
| **group\_key**<br>_optional_ | The requested group key | string |
| **order\_by**<br>_optional_ | The list of fields to sort on. | < [order\_by](https://clear.ml/docs/latest/docs/references/enterprise/frames/#frames-get_group_snippets_for_dataview-post-order_by) \> array |
| **projection**<br>_optional_ | Used to select which parts of the frame will be returned. Each string <br>represents a field or sub-field (using dot-separated notation). In order to <br>specify a specific array element, use array index as a field name. To specify <br>all array elements, use '\*'. | < string > array |
| **sample\_aggregation**<br>_optional_ | Definition of the property for sampling | [sample\_aggregation](https://clear.ml/docs/latest/docs/references/enterprise/frames/#frames-get_group_snippets_for_dataview-post-sample_aggregation) |

**order\_by**

| Name | Description | Schema |
| --- | --- | --- |
| **field**<br>_optional_ | The name of the field | string |
| **order**<br>_optional_ | The order of the sorting <br>**Default** : `"asc"` | enum (asc, desc) |

**sample\_aggregation**

| Name | Description | Schema |
| --- | --- | --- |
| **field**<br>_required_ | The name of the frame, roi or source field | string |
| **filter**<br>_optional_ | Lucene query filter to choose particular roi or source elements | string |
| **samples**<br>_optional_ | The number of samples to return for each aggregation value | integer |
| **type**<br>_required_ | Part of the frame that the property field belongs to | enum (frame, roi, source) |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#responses-7 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/frames/#frames-get_group_snippets_for_dataview-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **frames**<br>_optional_ | List of frames samples for the requested aggregation group. Should be equal or <br>less to the requested aggregation samples amount | < [frames.snippet](https://clear.ml/docs/latest/docs/references/enterprise/definitions#framessnippet) \> array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#security-7 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /frames.get\_next [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#post-framesget_next "Direct link to POST /frames.get_next")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#description-8 "Direct link to Description")

Gets frames for a given dataset version.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#parameters-8 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/frames/#frames-get_next-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **batch\_size**<br>_optional_ | Max number of images to be returned. Used only if scroll\_id is not provided. | integer |
| **clean\_subfields**<br>_optional_ | If set to Truethen both frame toplevel fields and subfields are cleaned <br>according to the schema. Otherwise only top level fields <br>**Default** : `false` | boolean |
| **dataset**<br>_required_ | Dataset id | string |
| **labels**<br>_optional_ | List of labels. Only frames containing labels from this list should be <br>returned. Used only if scroll\_id is not provided. | < string > array |
| **merge\_with**<br>_optional_ | Version ID to merge with | string |
| **node**<br>_optional_ | Node number. This provides support for multi-node experiments running multiple <br>workers executing the same experiment on multiple processes or machines | integer |
| **projection**<br>_optional_ | Used to select which parts of the frame will be returned. Each string <br>represents a field or sub-field (using dot-separated notation). In order to <br>specify a specific array element, use array index as a field name. To specify <br>all array elements, use '\*'. | < string > array |
| **remove\_none\_values**<br>_optional_ | If set to Truethen none values are removed from frames (except for metadata) <br>**Default** : `false` | boolean |
| **scroll\_id**<br>_optional_ | Scroll session ID for getting the next batch of images | string |
| **version**<br>_required_ | Dataset version id | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#responses-8 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/frames/#frames-get_next-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **eof**<br>_optional_ | When 'frames' is empty, represents whether there are no more frames left. If <br>"false", client can retry the operation. | boolean |
| **frames**<br>_optional_ | Frames list | < [frames.frame](https://clear.ml/docs/latest/docs/references/enterprise/definitions#framesframe) \> array |
| **frames\_returned**<br>_optional_ | Number of frames returned | integer |
| **roi\_stats**<br>_optional_ | Json object containing the count per labels in frames, e.g. { 'background': <br>312, 'boat': 2, 'bus': 4, 'car': 2, } | < string, integer > map |
| **scroll\_id**<br>_optional_ | Scroll session id to be provided in order to get the next batch of images | string |
| **scroll\_state**<br>_optional_ | JSON object representing the scroll state | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#security-8 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /frames.get\_next\_for\_dataview [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#post-framesget_next_for_dataview "Direct link to POST /frames.get_next_for_dataview")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#description-9 "Direct link to Description")

Gets frames for a given view specification

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#parameters-9 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/frames/#frames-get_next_for_dataview-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **batch\_size**<br>_optional_ | Max number of images to be returned. Used only if scroll\_id is not provided. | integer |
| **clean\_subfields**<br>_optional_ | If set to Truethen both frame toplevel fields and subfields are cleaned <br>according to the schema. Otherwise only top level fields <br>**Default** : `false` | boolean |
| **dataview**<br>_required_ | Dataview specification | [frames.dataview](https://clear.ml/docs/latest/docs/references/enterprise/definitions#framesdataview) |
| **flow\_control**<br>_optional_ | Contol if frames retreival always navigate in one direction (the default) or <br>can navigate forwards and backwards | [frames.flow\_control](https://clear.ml/docs/latest/docs/references/enterprise/definitions#framesflow_control) |
| **force\_scroll\_id**<br>_optional_ |  | boolean |
| **node**<br>_optional_ | Node number. This provides support for multi-node experiments running multiple <br>workers executing the same experiment on multiple processes or machines | integer |
| **projection**<br>_optional_ | Used to select which parts of the frame will be returned. Each string <br>represents a field or sub-field (using dot-separated notation). In order to <br>specify a specific array element, use array index as a field name. To specify <br>all array elements, use '\*'. | < string > array |
| **random\_seed**<br>_optional_ | Optional random seed used for frame selection. If not provided, one will be <br>generated. | integer |
| **remove\_none\_values**<br>_optional_ | If set to Truethen none values are removed from frames (except for metadata) <br>**Default** : `false` | boolean |
| **reset\_scroll**<br>_optional_ |  | boolean |
| **scroll\_id**<br>_optional_ | Scroll session id for getting the next batch of images | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#responses-9 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/frames/#frames-get_next_for_dataview-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **eof**<br>_optional_ | When 'frames' is empty, represents whether there are no more frames left. If <br>"false", client can retry the operation. | boolean |
| **frames**<br>_optional_ | Frames list | < [frames.frame](https://clear.ml/docs/latest/docs/references/enterprise/definitions#framesframe) \> array |
| **frames\_returned**<br>_optional_ | Number of frames returned | integer |
| **random\_seed**<br>_optional_ | Random seed used for frame selection | integer |
| **roi\_stats**<br>_optional_ | Json object containing the count per labels in frames, e.g. { 'background': <br>312, 'boat': 2, 'bus': 4, 'car': 2, } | < string, integer > map |
| **scroll\_id**<br>_optional_ | Scroll session id to be provided in order to get the next batch of images | string |
| **scroll\_state**<br>_optional_ | JSON object representing the scroll state | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#security-9 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /frames.get\_next\_for\_dataview\_and\_context\_id [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#post-framesget_next_for_dataview_and_context_id "Direct link to POST /frames.get_next_for_dataview_and_context_id")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#description-10 "Direct link to Description")

Get frames for the given dataview specification and context id

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#parameters-10 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/frames/#frames-get_next_for_dataview_and_context_id-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **batch\_size**<br>_optional_ | Max number of images to be returned. Used only if scroll\_id is not provided. | integer |
| **clean\_subfields**<br>_optional_ | If set to Truethen both frame toplevel fields and subfields are cleaned <br>according to the schema. Otherwise only top level fields <br>**Default** : `false` | boolean |
| **context\_id**<br>_required_ | Retrieve only frames associated with this context\_id | string |
| **dataview**<br>_required_ | Dataview specification | [frames.dataview](https://clear.ml/docs/latest/docs/references/enterprise/definitions#framesdataview) |
| **flow\_control**<br>_optional_ | Contol if frames retreival always navigate in one direction (the default) or <br>can navigate forwards and backwards | [frames.flow\_control](https://clear.ml/docs/latest/docs/references/enterprise/definitions#framesflow_control) |
| **node**<br>_optional_ | Node number. This provides support for multi-node experiments running multiple <br>workers executing the same experiment on multiple processes or machines | integer |
| **projection**<br>_optional_ | Used to select which parts of the frame will be returned. Each string <br>represents a field or sub-field (using dot-separated notation). In order to <br>specify a specific array element, use array index as a field name. To specify <br>all array elements, use '\*'. | < string > array |
| **random\_seed**<br>_optional_ | Optional random seed used for frame selection. If not provided, one will be <br>generated. | integer |
| **remove\_none\_values**<br>_optional_ | If set to Truethen none values are removed from frames (except for metadata) <br>**Default** : `false` | boolean |
| **scroll\_id**<br>_optional_ | Scroll session id for getting the next batch of images | string |
| **timestamp**<br>_optional_ | Start timestamp for frames returned. Optional. Default is 0 | integer |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#responses-10 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/frames/#frames-get_next_for_dataview_and_context_id-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **eof**<br>_optional_ | When 'frames' is empty, represents whether there are no more frames left. If <br>"false", client can retry the operation. | boolean |
| **frames**<br>_optional_ | Frames list | < [frames.frame](https://clear.ml/docs/latest/docs/references/enterprise/definitions#framesframe) \> array |
| **frames\_returned**<br>_optional_ | Number of frames returned | integer |
| **random\_seed**<br>_optional_ | Random seed used for frame selection | integer |
| **roi\_stats**<br>_optional_ | Json object containing the count per labels in frames, e.g. { 'background': <br>312, 'boat': 2, 'bus': 4, 'car': 2, } | < string, integer > map |
| **scroll\_id**<br>_optional_ | Scroll session id to be provided in order to get the next batch of images | string |
| **scroll\_state**<br>_optional_ | JSON object representing the scroll state | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#security-10 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /frames.get\_next\_for\_dataview\_id [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#post-framesget_next_for_dataview_id "Direct link to POST /frames.get_next_for_dataview_id")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#description-11 "Direct link to Description")

Gets frames for a given view specification

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#parameters-11 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/frames/#frames-get_next_for_dataview_id-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **batch\_size**<br>_optional_ | Max number of images to be returned. Used only if scroll\_id is not provided. | integer |
| **clean\_subfields**<br>_optional_ | If set to Truethen both frame toplevel fields and subfields are cleaned <br>according to the schema. Otherwise only top level fields <br>**Default** : `false` | boolean |
| **dataview**<br>_required_ | Dataview ID | string |
| **flow\_control**<br>_optional_ | Frames retreival that allows eiter one-directional navigation (the default) or <br>bidirectional | [frames.flow\_control](https://clear.ml/docs/latest/docs/references/enterprise/definitions#framesflow_control) |
| **force\_scroll\_id**<br>_optional_ |  | boolean |
| **node**<br>_optional_ | Node number. This provides support for multi-node experiments running multiple <br>workers executing the same experiment on multiple processes or machines | integer |
| **projection**<br>_optional_ | Used to select which parts of the frame will be returned. Each string <br>represents a field or sub-field (using dot-separated notation). In order to <br>specify a specific array element, use array index as a field name. To specify <br>all array elements, use '\*'. | < string > array |
| **random\_seed**<br>_optional_ | Optional random seed used for frame selection. If not provided, one will be <br>generated. | integer |
| **remove\_none\_values**<br>_optional_ | If set to Truethen none values are removed from frames (except for metadata) <br>**Default** : `false` | boolean |
| **reset\_scroll**<br>_optional_ |  | boolean |
| **scroll\_id**<br>_optional_ | Scroll session id for getting the next batch of images | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#responses-11 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/frames/#frames-get_next_for_dataview_id-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **eof**<br>_optional_ | When 'frames' is empty, represents whether there are no more frames left. If <br>"false", client can retry the operation. | boolean |
| **frames**<br>_optional_ | Frames list | < [frames.frame](https://clear.ml/docs/latest/docs/references/enterprise/definitions#framesframe) \> array |
| **frames\_returned**<br>_optional_ | Number of frames returned | integer |
| **random\_seed**<br>_optional_ | Random seed used for frame selection | integer |
| **roi\_stats**<br>_optional_ | Json object containing the count per labels in frames, e.g. { 'background': <br>312, 'boat': 2, 'bus': 4, 'car': 2, } | < string, integer > map |
| **scroll\_id**<br>_optional_ | Scroll session id to be provided in order to get the next batch of images | string |
| **scroll\_state**<br>_optional_ | JSON object representing the scroll state | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#security-11 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /frames.get\_snippets\_for\_dataview [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#post-framesget_snippets_for_dataview "Direct link to POST /frames.get_snippets_for_dataview")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#description-12 "Direct link to Description")

Return first frame per unique URI for the given dataview specification. Note:

'count\_range' option for label rules is not supported and does not affect the

returned snippets

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#parameters-12 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/frames/#frames-get_snippets_for_dataview-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **aggregate\_on\_context\_id**<br>_optional_ | If set to Truethen one frame is returned per unique context\_id. If set to <br>Falseall frames are retuned. If not set then defaults to the server configured <br>value | boolean |
| **dataview**<br>_required_ | Dataview specification | [frames.dataview](https://clear.ml/docs/latest/docs/references/enterprise/definitions#framesdataview) |
| **page**<br>_optional_ | The page to return. default=0, Optional | integer |
| **page\_size**<br>_optional_ | The amount of snippets to return for the page. Cannot be changed after the <br>first call (after the paging session is created). default=50, Optional. To <br>change the page size use 'paging\_id'=0 that will reset the paging session. | integer |
| **paging\_id**<br>_optional_ | Paging session id for getting the next page of frames | string |
| **projection**<br>_optional_ | Used to select which parts of the frame will be returned. Each string <br>represents a field or sub-field (using dot-separated notation). In order to <br>specify a specific array element, use array index as a field name. To specify <br>all array elements, use '\*'. | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#responses-12 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/frames/#frames-get_snippets_for_dataview-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **frames**<br>_optional_ | List of frames for the requested page. The amount of frames returned is not <br>guaranteed to be equal to the requested page size. | < [frames.snippet](https://clear.ml/docs/latest/docs/references/enterprise/definitions#framessnippet) \> array |
| **frames\_total**<br>_optional_ | The total number of first frames per unique URI | integer |
| **page**<br>_optional_ | The currently requested page | integer |
| **pages\_total**<br>_optional_ | The total number of pages | integer |
| **paging\_id**<br>_optional_ | Paging session id to be provided in order to get the next page of frames | string |
| **total\_in\_versions**<br>_optional_ | The total number of snippets for the dataview versions (without applying the <br>dataview filters) | integer |
| **versions\_updated**<br>_optional_ | The list of versions whose frames were updated since the creation of the paging <br>iterator. If a version was updated after the iteration was started you may not <br>receive all the updated snippets. To make sure that you see all the snippets <br>after the update please reset the paging id (this may result in a different <br>total amount of pages for the same page size). | < string > array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#security-12 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /frames.get\_snippets\_for\_dataview2 [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#post-framesget_snippets_for_dataview2 "Direct link to POST /frames.get_snippets_for_dataview2")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#description-13 "Direct link to Description")

Return sample frames grouped by the requested field. Note: 'count\_range' option

for label rules is not supported and does not affect the returned snippets

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#parameters-13 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/frames/#frames-get_snippets_for_dataview2-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **aggregation**<br>_optional_ | Specifies whether the returned frames should be aggregated. If not passed then <br>'aggregate\_on\_context\_id' setting is consulted | [aggregation](https://clear.ml/docs/latest/docs/references/enterprise/frames/#frames-get_snippets_for_dataview2-post-aggregation) |
| **dataview**<br>_required_ | Dataview specification | [frames.dataview](https://clear.ml/docs/latest/docs/references/enterprise/definitions#framesdataview) |
| **disable\_aggregation**<br>_optional_ | Set this flag to 'true' to make sure that no aggregation is done regardless of <br>the server configuration <br>**Default** : `false` | boolean |
| **order\_by**<br>_optional_ | The list of fields to sort on. | < [order\_by](https://clear.ml/docs/latest/docs/references/enterprise/frames/#frames-get_snippets_for_dataview2-post-order_by) \> array |
| **projection**<br>_optional_ | Used to select which parts of the frame will be returned. Each string <br>represents a field or sub-field (using dot-separated notation). In order to <br>specify a specific array element, use array index as a field name. To specify <br>all array elements, use '\*'. | < string > array |
| **sample\_aggregation**<br>_optional_ | Definition of the property for sampling | [sample\_aggregation](https://clear.ml/docs/latest/docs/references/enterprise/frames/#frames-get_snippets_for_dataview2-post-sample_aggregation) |
| **search\_after**<br>_optional_ | For getting the next portion of snippets should be set to the value returned <br>from the previous call. Either this parameter or search\_before can be passed in <br>the query. To get snippets from the beginning both should be set to null or <br>empty string | string |
| **search\_before**<br>_optional_ | For getting the previous portion of snippets should be set to the value <br>returned from the previous call. Either this parameter or search\_after can be <br>passed in the query. To get snippets from the beginning both should be set to <br>null or empty string | string |
| **size**<br>_optional_ | The amount of snippets to return. | integer |
| **vector\_search**<br>_optional_ | Search frames closest to the provided vector. Cannot be used together with <br>aggregation | [vector\_search](https://clear.ml/docs/latest/docs/references/enterprise/frames/#frames-get_snippets_for_dataview2-post-vector_search) |

**aggregation**

| Name | Description | Schema |
| --- | --- | --- |
| **aggregate**<br>_required_ | If set to Truethen the returned frames are aggregated on the provided fields | boolean |
| **fields**<br>_optional_ | The list of the fields to aggragate on. Only if the aggregate parameter is set <br>to True | < string > array |

**order\_by**

| Name | Description | Schema |
| --- | --- | --- |
| **field**<br>_optional_ | The name of the field | string |
| **order**<br>_optional_ | The order of the sorting <br>**Default** : `"asc"` | enum (asc, desc) |

**sample\_aggregation**

| Name | Description | Schema |
| --- | --- | --- |
| **field**<br>_required_ | The name of the frame, roi or source field | string |
| **filter**<br>_optional_ | Lucene query filter to choose particular roi or source elements | string |
| **samples**<br>_optional_ | The number of samples to return for each aggregation value | integer |
| **type**<br>_required_ | Part of the frame that the property field belongs to | enum (frame, roi, source) |

**vector\_search**

| Name | Description | Schema |
| --- | --- | --- |
| **field**<br>_required_ | Vector field name | string |
| **method**<br>_optional_ | The search method. 'fast' for indexed search. 'exact' for script search <br>**Default** : `"exact"` | enum (fast, exact) |
| **neighbors**<br>_optional_ | The maximum amount of snippets to return | integer |
| **similarity\_func**<br>_optional_ | The function for calculating distance from search vector <br>**Default** : `"cosine"` | enum (l2\_norm, dot\_product, cosine) |
| **vector**<br>_required_ | The search vector | < number > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#responses-13 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/frames/#frames-get_snippets_for_dataview2-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **frames**<br>_optional_ | List of frames for the requested page. The amount of frames returned is not <br>guaranteed to be equal to the requested page size. | < [frames.snippet](https://clear.ml/docs/latest/docs/references/enterprise/definitions#framessnippet) \> array |
| **frames\_total**<br>_optional_ | The total number of first frames per unique URI | integer |
| **search\_after**<br>_optional_ | The key for querying next batch of frames (according to the specified sorting <br>order) | string |
| **search\_before**<br>_optional_ | The key for querying previous batch of frames (according to the specified <br>sorting order) | string |
| **total\_in\_versions**<br>_optional_ | The total number of snippets for the dataview versions (without applying the <br>dataview filters) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#security-13 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /frames.get\_snippets\_query\_for\_dataview [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#post-framesget_snippets_query_for_dataview "Direct link to POST /frames.get_snippets_query_for_dataview")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#description-14 "Direct link to Description")

Get Elasticsearch query that returns frames with unique URIs for the given

dataview specification. The query is returned only for the clients that have

kibana space set up. Note: 'count\_range' option for label rules is not

supported and not reflected in the query

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#parameters-14 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/frames/#frames-get_snippets_query_for_dataview-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **dataview**<br>_required_ | Dataview specification | [frames.dataview](https://clear.ml/docs/latest/docs/references/enterprise/definitions#framesdataview) |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#responses-14 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/frames/#frames-get_snippets_query_for_dataview-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **kibana\_link**<br>_optional_ | The link to the Kibana discovery page with the dataview query | string |
| **query**<br>_optional_ | The Elasticsearch query filter that should bring the snippet frames according <br>to the provided dataview | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#security-14 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /frames.get\_source\_ids\_for\_dataview [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#post-framesget_source_ids_for_dataview "Direct link to POST /frames.get_source_ids_for_dataview")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#description-15 "Direct link to Description")

Get unique sorce id that exist in the frames in the given dataview

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#parameters-15 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/frames/#frames-get_source_ids_for_dataview-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **dataview**<br>_required_ | Dataview specification | [frames.dataview](https://clear.ml/docs/latest/docs/references/enterprise/definitions#framesdataview) |
| **max\_count**<br>_optional_ | Number of source IDs to return. default=100, Optional | integer |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#responses-15 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/frames/#frames-get_source_ids_for_dataview-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **source\_ids**<br>_optional_ | Unique source ids for the dataset version | < string > array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#security-15 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /frames.get\_stats\_for\_dataview [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#post-framesget_stats_for_dataview "Direct link to POST /frames.get_stats_for_dataview")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#description-16 "Direct link to Description")

Get labels' stats for a dataview

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#parameters-16 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/frames/#frames-get_stats_for_dataview-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **dataview**<br>_required_ | Dataview specification | [frames.dataview](https://clear.ml/docs/latest/docs/references/enterprise/definitions#framesdataview) |
| **labels\_property**<br>_optional_ | Definition of the property for labels calculation | [labels\_property](https://clear.ml/docs/latest/docs/references/enterprise/frames/#frames-get_stats_for_dataview-post-labels_property) |

**labels\_property**

| Name | Description | Schema |
| --- | --- | --- |
| **field**<br>_required_ | The name of the frame, roi or source field | string |
| **filter**<br>_optional_ | Lucene query filter to choose particular roi or source elements | string |
| **type**<br>_required_ | Part of the frame that the property field belongs to | enum (frame, roi, source) |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#responses-16 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/frames/#frames-get_stats_for_dataview-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **content\_types**<br>_optional_ | List of statistics for each content type | < [frames.stat\_count](https://clear.ml/docs/latest/docs/references/enterprise/definitions#framesstat_count) \> array |
| **frames**<br>_optional_ | List of statistics for each frame (annotated/unannotated) | < [frames.stat\_count](https://clear.ml/docs/latest/docs/references/enterprise/definitions#framesstat_count) \> array |
| **labels**<br>_optional_ | List of statistics for each label | < [frames.stat\_count](https://clear.ml/docs/latest/docs/references/enterprise/definitions#framesstat_count) \> array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#security-16 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /frames.get\_with\_projection [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#post-framesget_with_projection "Direct link to POST /frames.get_with_projection")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#description-17 "Direct link to Description")

For each passed query return projected frames matcing the conditions. One frame

is returned per unique query field value

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#parameters-17 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/frames/#frames-get_with_projection-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **query**<br>_optional_ | The list of field queries | < [query](https://clear.ml/docs/latest/docs/references/enterprise/frames/#frames-get_with_projection-post-query) \> array |
| **versions**<br>_optional_ | Dataset versions | < [frames.view\_entry](https://clear.ml/docs/latest/docs/references/enterprise/definitions#framesview_entry) \> array |

**query**

| Name | Description | Schema |
| --- | --- | --- |
| **field**<br>_optional_ | The field name | string |
| **projection**<br>_optional_ | List of projected fields | < string > array |
| **values**<br>_optional_ | The allowed field values | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#responses-17 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/frames/#frames-get_with_projection-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **frames**<br>_optional_ | Projected frames per rule indexed by the rule key | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#security-17 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /frames.prepare\_download\_for\_dataview [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#post-framesprepare_download_for_dataview "Direct link to POST /frames.prepare_download_for_dataview")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#description-18 "Direct link to Description")

Prepare request data for frames download. Intended for allowing the user to

send the data using a POST request (since a query string in a GET request

cannot accomodate large generic data structures), and use the resulting call's

ID as a handle for calling the `download_for_dataview` endpoint using a GET

method.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#parameters-18 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/frames/#frames-prepare_download_for_dataview-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **clean\_subfields**<br>_optional_ | If set to Truethen both frame toplevel fields and subfields are cleaned <br>according to the schema. Otherwise only top level fields <br>**Default** : `false` | boolean |
| **dataview**<br>_required_ | Dataview specification | [frames.dataview](https://clear.ml/docs/latest/docs/references/enterprise/definitions#framesdataview) |
| **download\_type**<br>_optional_ | Download type. Determines the downloaded file's formatting and mime type. <br>**Default** : `"json"` | enum (json, jsonlines) |
| **node**<br>_optional_ | Node number. This provides support for multi-node experiments running multiple <br>workers executing the same experiment on multiple processes or machines | integer |
| **projection**<br>_optional_ | Used to select which parts of the frame will be returned. Each string <br>represents a field or sub-field (using dot-separated notation). In order to <br>specify a specific array element, use array index as a field name. To specify <br>all array elements, use '\*'. | < string > array |
| **random\_seed**<br>_optional_ | Optional random seed used for frame selection. If not provided, one will be <br>generated. | integer |
| **remove\_none\_values**<br>_optional_ | If set to Truethen none values are removed from frames (except for metadata) <br>**Default** : `false` | boolean |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#responses-18 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/frames/#frames-prepare_download_for_dataview-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **prepare\_id**<br>_optional_ | Prepare ID (use when calling `download_for_dataview`) | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/frames/\#security-18 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

- [POST /frames.clear\_get\_next\_state](https://clear.ml/docs/latest/docs/references/enterprise/frames/#post-framesclear_get_next_state)
- [POST /frames.download\_for\_dataview](https://clear.ml/docs/latest/docs/references/enterprise/frames/#post-framesdownload_for_dataview)
- [POST /frames.get\_by\_id](https://clear.ml/docs/latest/docs/references/enterprise/frames/#post-framesget_by_id)
- [POST /frames.get\_by\_ids](https://clear.ml/docs/latest/docs/references/enterprise/frames/#post-framesget_by_ids)
- [POST /frames.get\_count](https://clear.ml/docs/latest/docs/references/enterprise/frames/#post-framesget_count)
- [POST /frames.get\_count\_for\_dataview](https://clear.ml/docs/latest/docs/references/enterprise/frames/#post-framesget_count_for_dataview)
- [POST /frames.get\_count\_for\_dataview\_id](https://clear.ml/docs/latest/docs/references/enterprise/frames/#post-framesget_count_for_dataview_id)
- [POST /frames.get\_group\_snippets\_for\_dataview](https://clear.ml/docs/latest/docs/references/enterprise/frames/#post-framesget_group_snippets_for_dataview)
- [POST /frames.get\_next](https://clear.ml/docs/latest/docs/references/enterprise/frames/#post-framesget_next)
- [POST /frames.get\_next\_for\_dataview](https://clear.ml/docs/latest/docs/references/enterprise/frames/#post-framesget_next_for_dataview)
- [POST /frames.get\_next\_for\_dataview\_and\_context\_id](https://clear.ml/docs/latest/docs/references/enterprise/frames/#post-framesget_next_for_dataview_and_context_id)
- [POST /frames.get\_next\_for\_dataview\_id](https://clear.ml/docs/latest/docs/references/enterprise/frames/#post-framesget_next_for_dataview_id)
- [POST /frames.get\_snippets\_for\_dataview](https://clear.ml/docs/latest/docs/references/enterprise/frames/#post-framesget_snippets_for_dataview)
- [POST /frames.get\_snippets\_for\_dataview2](https://clear.ml/docs/latest/docs/references/enterprise/frames/#post-framesget_snippets_for_dataview2)
- [POST /frames.get\_snippets\_query\_for\_dataview](https://clear.ml/docs/latest/docs/references/enterprise/frames/#post-framesget_snippets_query_for_dataview)
- [POST /frames.get\_source\_ids\_for\_dataview](https://clear.ml/docs/latest/docs/references/enterprise/frames/#post-framesget_source_ids_for_dataview)
- [POST /frames.get\_stats\_for\_dataview](https://clear.ml/docs/latest/docs/references/enterprise/frames/#post-framesget_stats_for_dataview)
- [POST /frames.get\_with\_projection](https://clear.ml/docs/latest/docs/references/enterprise/frames/#post-framesget_with_projection)
- [POST /frames.prepare\_download\_for\_dataview](https://clear.ml/docs/latest/docs/references/enterprise/frames/#post-framesprepare_download_for_dataview)