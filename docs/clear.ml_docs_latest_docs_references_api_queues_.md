---
url: "https://clear.ml/docs/latest/docs/references/api/queues/"
title: "queues | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/api/queues/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

### POST /queues.add\_or\_update\_metadata [​](https://clear.ml/docs/latest/docs/references/api/queues/\#post-queuesadd_or_update_metadata "Direct link to POST /queues.add_or_update_metadata")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/queues/\#description "Direct link to Description")

Add or update queue metadata

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/queues/\#parameters "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/queues/#queues-add_or_update_metadata-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **metadata**<br>_required_ | Metadata items to add or update | < [queues.metadata\_item](https://clear.ml/docs/latest/docs/references/api/definitions#queuesmetadata_item) \> array |
| **queue**<br>_required_ | ID of the queue | string |
| **replace\_metadata**<br>_optional_ | If set then the all the metadata items will be replaced with the provided ones. <br>Otherwise only the provided metadata items will be updated or added <br>**Default** : `false` | boolean |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/queues/\#responses "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/queues/#queues-add_or_update_metadata-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **updated**<br>_optional_ | Number of queues updated (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/queues/\#security "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /queues.add\_task [​](https://clear.ml/docs/latest/docs/references/api/queues/\#post-queuesadd_task "Direct link to POST /queues.add_task")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/queues/\#description-1 "Direct link to Description")

Adds a task entry to the queue.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/queues/\#parameters-1 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/queues/#queues-add_task-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **queue**<br>_required_ | Queue id | string |
| **task**<br>_required_ | Task id | string |
| **update\_execution\_queue**<br>_optional_ | If set to Falsethen the task 'execution.queue' is not updated <br>**Default** : `true` | boolean |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/queues/\#responses-1 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/queues/#queues-add_task-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **added**<br>_optional_ | Number of tasks added (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/queues/\#security-1 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /queues.clear\_queue [​](https://clear.ml/docs/latest/docs/references/api/queues/\#post-queuesclear_queue "Direct link to POST /queues.clear_queue")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/queues/\#description-2 "Direct link to Description")

Remove all tasks from the queue and change their statuses to what they were

prior to enqueuing or 'created'

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/queues/\#parameters-2 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/queues/#queues-clear_queue-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **queue**<br>_required_ | Queue id | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/queues/\#responses-2 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/queues/#queues-clear_queue-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **removed\_tasks**<br>_optional_ | IDs of the removed tasks | < string > array |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/queues/\#security-2 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /queues.create [​](https://clear.ml/docs/latest/docs/references/api/queues/\#post-queuescreate "Direct link to POST /queues.create")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/queues/\#description-3 "Direct link to Description")

Create a new queue

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/queues/\#parameters-3 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/queues/#queues-create-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **display\_name**<br>_optional_ | Display name | string |
| **metadata**<br>_optional_ | Queue metadata | < string, [queues.metadata\_item](https://clear.ml/docs/latest/docs/references/api/definitions#queuesmetadata_item) \> map |
| **name**<br>_required_ | Queue name Unique within the company. | string |
| **system\_tags**<br>_optional_ | System tags list. This field is reserved for system use, please don't use it. | < string > array |
| **tags**<br>_optional_ | User-defined tags list | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/queues/\#responses-3 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/queues/#queues-create-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_optional_ | New queue ID | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/queues/\#security-3 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /queues.delete [​](https://clear.ml/docs/latest/docs/references/api/queues/\#post-queuesdelete "Direct link to POST /queues.delete")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/queues/\#description-4 "Direct link to Description")

Deletes a queue. If the queue is not empty and force is not set to true, queue

will not be deleted.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/queues/\#parameters-4 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/queues/#queues-delete-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **force**<br>_optional_ | Force delete of non-empty queue. Defaults to false <br>**Default** : `false` | boolean |
| **queue**<br>_required_ | Queue id | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/queues/\#responses-4 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/queues/#queues-delete-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **deleted**<br>_optional_ | Number of queues deleted (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/queues/\#security-4 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /queues.delete\_metadata [​](https://clear.ml/docs/latest/docs/references/api/queues/\#post-queuesdelete_metadata "Direct link to POST /queues.delete_metadata")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/queues/\#description-5 "Direct link to Description")

Delete metadata from queue

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/queues/\#parameters-5 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/queues/#queues-delete_metadata-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **keys**<br>_required_ | The list of metadata keys to delete | < string > array |
| **queue**<br>_required_ | ID of the queue | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/queues/\#responses-5 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/queues/#queues-delete_metadata-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **updated**<br>_optional_ | Number of queues updated (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/queues/\#security-5 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /queues.get\_all [​](https://clear.ml/docs/latest/docs/references/api/queues/\#post-queuesget_all "Direct link to POST /queues.get_all")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/queues/\#description-6 "Direct link to Description")

Get all queues

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/queues/\#parameters-6 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/queues/#queues-get_all-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_optional_ | List of Queue IDs used to filter results | < string > array |
| **max\_task\_entries**<br>_optional_ | Max number of queue task entries to return | integer |
| **name**<br>_optional_ | Get only queues whose name matches this pattern (python regular expression <br>syntax) | string |
| **only\_fields**<br>_optional_ | List of document field names (nesting is supported using '.', e.g. <br>execution.model\_labels). If provided, this list defines the query's projection <br>(only these fields will be returned for each result entry) | < string > array |
| **order\_by**<br>_optional_ | List of field names to order by. When search\_text is used, '@text\_score' can be <br>used as a field representing the text score of returned documents. Use '-' <br>prefix to specify descending order. Optional, recommended when using page | < string > array |
| **page**<br>_optional_ | Page number, returns a specific page out of the result list of results. <br>**Minimum value** : `0` | integer |
| **page\_size**<br>_optional_ | Page size, specifies the number of results returned in each page (last page may <br>contain fewer results) <br>**Minimum value** : `1` | integer |
| **refresh\_scroll**<br>_optional_ | If set then all the data received with this scroll will be requeried | boolean |
| **scroll\_id**<br>_optional_ | Scroll ID returned from the previos calls to get\_all | string |
| **search\_hidden**<br>_optional_ | If set to 'true' then hidden queues are included in the search results <br>**Default** : `false` | boolean |
| **search\_text**<br>_optional_ | Free text search query | string |
| **size**<br>_optional_ | The number of queues to retrieve <br>**Minimum value** : `1` | integer |
| **system\_tags**<br>_optional_ | System tags list used to filter results. Prepend '-' to system tag name to <br>indicate exclusion | < string > array |
| **tags**<br>_optional_ | User-defined tags list used to filter results. Prepend '-' to tag name to <br>indicate exclusion | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/queues/\#responses-6 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/queues/#queues-get_all-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **queues**<br>_optional_ | Queues list | < [queues.queue](https://clear.ml/docs/latest/docs/references/api/definitions#queuesqueue) \> array |
| **scroll\_id**<br>_optional_ | Scroll ID that can be used with the next calls to get\_all to retrieve more data | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/queues/\#security-6 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /queues.get\_by\_id [​](https://clear.ml/docs/latest/docs/references/api/queues/\#post-queuesget_by_id "Direct link to POST /queues.get_by_id")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/queues/\#description-7 "Direct link to Description")

Gets queue information

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/queues/\#parameters-7 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/queues/#queues-get_by_id-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **max\_task\_entries**<br>_optional_ | Max number of queue task entries to return | integer |
| **queue**<br>_required_ | Queue ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/queues/\#responses-7 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/queues/#queues-get_by_id-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **queue**<br>_optional_ | Queue info | [queues.queue](https://clear.ml/docs/latest/docs/references/api/definitions#queuesqueue) |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/queues/\#security-7 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /queues.get\_default [​](https://clear.ml/docs/latest/docs/references/api/queues/\#post-queuesget_default "Direct link to POST /queues.get_default")

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/queues/\#parameters-8 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/queues/\#responses-8 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/queues/#queues-get_default-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_optional_ | Queue id | string |
| **name**<br>_optional_ | Queue name | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/queues/\#security-8 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /queues.get\_next\_task [​](https://clear.ml/docs/latest/docs/references/api/queues/\#post-queuesget_next_task "Direct link to POST /queues.get_next_task")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/queues/\#description-8 "Direct link to Description")

Gets the next task from the top of the queue (FIFO). The task entry is removed

from the queue.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/queues/\#parameters-9 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/queues/#queues-get_next_task-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **get\_task\_info**<br>_optional_ | If set then additional task info is returned <br>**Default** : `false` | boolean |
| **queue**<br>_required_ | Queue id | string |
| **task**<br>_optional_ | Task company ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/queues/\#responses-9 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/queues/#queues-get_next_task-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **entry**<br>_optional_ | Entry information | [queues.entry](https://clear.ml/docs/latest/docs/references/api/definitions#queuesentry) |
| **task\_info**<br>_optional_ | Info about the returned task. Returned only if get\_task\_info is set to True | [task\_info](https://clear.ml/docs/latest/docs/references/api/queues/#queues-get_next_task-post-task_info) |

**task\_info**

| Name | Description | Schema |
| --- | --- | --- |
| **company**<br>_optional_ | Task company ID | string |
| **user**<br>_optional_ | ID of the user who created the task | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/queues/\#security-9 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /queues.get\_num\_entries [​](https://clear.ml/docs/latest/docs/references/api/queues/\#post-queuesget_num_entries "Direct link to POST /queues.get_num_entries")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/queues/\#description-9 "Direct link to Description")

Get the number of task entries in the given queue

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/queues/\#parameters-10 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/queues/#queues-get_num_entries-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **queue**<br>_required_ | ID of the queue | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/queues/\#responses-10 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/queues/#queues-get_num_entries-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **num**<br>_optional_ | Number of entries | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/queues/\#security-10 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /queues.get\_queue\_metrics [​](https://clear.ml/docs/latest/docs/references/api/queues/\#post-queuesget_queue_metrics "Direct link to POST /queues.get_queue_metrics")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/queues/\#description-10 "Direct link to Description")

Returns metrics of the company queues. The metrics are avaraged in the

specified interval.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/queues/\#parameters-11 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/queues/#queues-get_queue_metrics-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **from\_date**<br>_required_ | Starting time (in seconds from epoch) for collecting metrics | number |
| **interval**<br>_required_ | Time interval in seconds for a single metrics point. The minimal value is 1 | integer |
| **queue\_ids**<br>_optional_ | List of queue ids to collect metrics for. If not provided or empty then all <br>then average metrics across all the company queues will be returned. | < string > array |
| **refresh**<br>_optional_ | If set then the new queue metrics is taken <br>**Default** : `false` | boolean |
| **to\_date**<br>_required_ | Ending time (in seconds from epoch) for collecting metrics | number |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/queues/\#responses-11 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/queues/#queues-get_queue_metrics-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **queues**<br>_optional_ | List of the requested queues with their metrics. If no queue ids were requested <br>then 'all' queue is returned with the metrics averaged accross all the company <br>queues. | < [queues.queue\_metrics](https://clear.ml/docs/latest/docs/references/api/definitions#queuesqueue_metrics) \> array |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/queues/\#security-11 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /queues.move\_task\_backward [​](https://clear.ml/docs/latest/docs/references/api/queues/\#post-queuesmove_task_backward "Direct link to POST /queues.move_task_backward")

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/queues/\#parameters-12 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/queues/#queues-move_task_backward-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **count**<br>_optional_ | Number of positions in the queue to move the task forward relative to the <br>current position. Optional, the default value is 1. | integer |
| **queue**<br>_required_ | Queue id | string |
| **task**<br>_required_ | Task id | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/queues/\#responses-12 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/queues/#queues-move_task_backward-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **position**<br>_optional_ | The new position of the task entry in the queue (index, -1 represents bottom of <br>queue) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/queues/\#security-12 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /queues.move\_task\_forward [​](https://clear.ml/docs/latest/docs/references/api/queues/\#post-queuesmove_task_forward "Direct link to POST /queues.move_task_forward")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/queues/\#description-11 "Direct link to Description")

Moves a task entry one step forward towards the top of the queue.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/queues/\#parameters-13 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/queues/#queues-move_task_forward-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **count**<br>_optional_ | Number of positions in the queue to move the task forward relative to the <br>current position. Optional, the default value is 1. | integer |
| **queue**<br>_required_ | Queue id | string |
| **task**<br>_required_ | Task id | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/queues/\#responses-13 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/queues/#queues-move_task_forward-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **position**<br>_optional_ | The new position of the task entry in the queue (index, -1 represents bottom of <br>queue) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/queues/\#security-13 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /queues.move\_task\_to\_back [​](https://clear.ml/docs/latest/docs/references/api/queues/\#post-queuesmove_task_to_back "Direct link to POST /queues.move_task_to_back")

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/queues/\#parameters-14 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/queues/#queues-move_task_to_back-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **queue**<br>_required_ | Queue id | string |
| **task**<br>_required_ | Task id | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/queues/\#responses-14 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/queues/#queues-move_task_to_back-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **position**<br>_optional_ | The new position of the task entry in the queue (index, -1 represents bottom of <br>queue) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/queues/\#security-14 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /queues.move\_task\_to\_front [​](https://clear.ml/docs/latest/docs/references/api/queues/\#post-queuesmove_task_to_front "Direct link to POST /queues.move_task_to_front")

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/queues/\#parameters-15 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/queues/#queues-move_task_to_front-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **queue**<br>_required_ | Queue id | string |
| **task**<br>_required_ | Task id | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/queues/\#responses-15 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/queues/#queues-move_task_to_front-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **position**<br>_optional_ | The new position of the task entry in the queue (index, -1 represents bottom of <br>queue) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/queues/\#security-15 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /queues.move\_task\_to\_queue [​](https://clear.ml/docs/latest/docs/references/api/queues/\#post-queuesmove_task_to_queue "Direct link to POST /queues.move_task_to_queue")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/queues/\#description-12 "Direct link to Description")

Moves task to another queue

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/queues/\#parameters-16 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/queues/#queues-move_task_to_queue-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **queue**<br>_required_ | Queue ID | string |
| **target\_queue**<br>_required_ | Target queue ID | string |
| **task**<br>_required_ | Task ID | string |
| **update\_execution\_queue**<br>_optional_ | If set to Falsethen the task 'execution.queue' is not updated <br>**Default** : `true` | boolean |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/queues/\#responses-16 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/queues/#queues-move_task_to_queue-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **moved**<br>_optional_ | Number of tasks moved (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/queues/\#security-16 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /queues.peek\_task [​](https://clear.ml/docs/latest/docs/references/api/queues/\#post-queuespeek_task "Direct link to POST /queues.peek_task")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/queues/\#description-13 "Direct link to Description")

Peek the next task from a given queue

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/queues/\#parameters-17 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/queues/#queues-peek_task-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **queue**<br>_required_ | ID of the queue | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/queues/\#responses-17 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/queues/#queues-peek_task-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **task**<br>_optional_ | Task ID | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/queues/\#security-17 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /queues.remove\_task [​](https://clear.ml/docs/latest/docs/references/api/queues/\#post-queuesremove_task "Direct link to POST /queues.remove_task")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/queues/\#description-14 "Direct link to Description")

Removes a task entry from the queue.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/queues/\#parameters-18 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/queues/#queues-remove_task-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **queue**<br>_required_ | Queue id | string |
| **task**<br>_required_ | Task id | string |
| **update\_task\_status**<br>_optional_ | If set to 'true' then change the removed task status to the one it had prior to <br>enqueuing or 'created' <br>**Default** : `false` | boolean |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/queues/\#responses-18 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/queues/#queues-remove_task-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **removed**<br>_optional_ | Number of tasks removed (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/queues/\#security-18 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /queues.update [​](https://clear.ml/docs/latest/docs/references/api/queues/\#post-queuesupdate "Direct link to POST /queues.update")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/queues/\#description-15 "Direct link to Description")

Update queue information

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/queues/\#parameters-19 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/api/queues/#queues-update-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **display\_name**<br>_optional_ | Display name | string |
| **metadata**<br>_optional_ | Queue metadata | < string, [queues.metadata\_item](https://clear.ml/docs/latest/docs/references/api/definitions#queuesmetadata_item) \> map |
| **name**<br>_optional_ | Queue name Unique within the company. | string |
| **queue**<br>_required_ | Queue id | string |
| **system\_tags**<br>_optional_ | System tags list. This field is reserved for system use, please don't use it. | < string > array |
| **tags**<br>_optional_ | User-defined tags list | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/queues/\#responses-19 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/queues/#queues-update-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **fields**<br>_optional_ | Updated fields names and values | object |
| **updated**<br>_optional_ | Number of queues updated (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/api/queues/\#security-19 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

- [POST /queues.add\_or\_update\_metadata](https://clear.ml/docs/latest/docs/references/api/queues/#post-queuesadd_or_update_metadata)
- [POST /queues.add\_task](https://clear.ml/docs/latest/docs/references/api/queues/#post-queuesadd_task)
- [POST /queues.clear\_queue](https://clear.ml/docs/latest/docs/references/api/queues/#post-queuesclear_queue)
- [POST /queues.create](https://clear.ml/docs/latest/docs/references/api/queues/#post-queuescreate)
- [POST /queues.delete](https://clear.ml/docs/latest/docs/references/api/queues/#post-queuesdelete)
- [POST /queues.delete\_metadata](https://clear.ml/docs/latest/docs/references/api/queues/#post-queuesdelete_metadata)
- [POST /queues.get\_all](https://clear.ml/docs/latest/docs/references/api/queues/#post-queuesget_all)
- [POST /queues.get\_by\_id](https://clear.ml/docs/latest/docs/references/api/queues/#post-queuesget_by_id)
- [POST /queues.get\_default](https://clear.ml/docs/latest/docs/references/api/queues/#post-queuesget_default)
- [POST /queues.get\_next\_task](https://clear.ml/docs/latest/docs/references/api/queues/#post-queuesget_next_task)
- [POST /queues.get\_num\_entries](https://clear.ml/docs/latest/docs/references/api/queues/#post-queuesget_num_entries)
- [POST /queues.get\_queue\_metrics](https://clear.ml/docs/latest/docs/references/api/queues/#post-queuesget_queue_metrics)
- [POST /queues.move\_task\_backward](https://clear.ml/docs/latest/docs/references/api/queues/#post-queuesmove_task_backward)
- [POST /queues.move\_task\_forward](https://clear.ml/docs/latest/docs/references/api/queues/#post-queuesmove_task_forward)
- [POST /queues.move\_task\_to\_back](https://clear.ml/docs/latest/docs/references/api/queues/#post-queuesmove_task_to_back)
- [POST /queues.move\_task\_to\_front](https://clear.ml/docs/latest/docs/references/api/queues/#post-queuesmove_task_to_front)
- [POST /queues.move\_task\_to\_queue](https://clear.ml/docs/latest/docs/references/api/queues/#post-queuesmove_task_to_queue)
- [POST /queues.peek\_task](https://clear.ml/docs/latest/docs/references/api/queues/#post-queuespeek_task)
- [POST /queues.remove\_task](https://clear.ml/docs/latest/docs/references/api/queues/#post-queuesremove_task)
- [POST /queues.update](https://clear.ml/docs/latest/docs/references/api/queues/#post-queuesupdate)