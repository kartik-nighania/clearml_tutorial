---
url: "https://clear.ml/docs/latest/docs/references/enterprise/tasks/"
title: "tasks | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

### POST /tasks.add\_or\_update\_artifacts [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#post-tasksadd_or_update_artifacts "Direct link to POST /tasks.add_or_update_artifacts")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#description "Direct link to Description")

Update existing artifacts (search by key/mode) and add new ones

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#parameters "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-add_or_update_artifacts-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **artifacts**<br>_required_ | Artifacts to add or update | < [tasks.artifact](https://clear.ml/docs/latest/docs/references/enterprise/definitions#tasksartifact) \> array |
| **force**<br>_optional_ | If set to True then both new and running task artifacts can be edited. <br>Otherwise only the new task ones. Default is False | boolean |
| **task**<br>_required_ | Task ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#responses "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-add_or_update_artifacts-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **updated**<br>_optional_ | Indicates if the task was updated successfully | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#security "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /tasks.add\_or\_update\_model [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#post-tasksadd_or_update_model "Direct link to POST /tasks.add_or_update_model")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#description-1 "Direct link to Description")

Add or update task model

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#parameters-1 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-add_or_update_model-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **iteration**<br>_optional_ | Iteration (used to update task statistics) | integer |
| **model**<br>_required_ | The model ID | string |
| **name**<br>_required_ | The task model name | string |
| **task**<br>_required_ | ID of the task | string |
| **type**<br>_required_ | The task model type | [tasks.model\_type\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions#tasksmodel_type_enum) |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#responses-1 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-add_or_update_model-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **updated**<br>_optional_ | Number of tasks updated (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#security-1 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /tasks.archive [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#post-tasksarchive "Direct link to POST /tasks.archive")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#description-2 "Direct link to Description")

Archive tasks. If a task is queued it will first be dequeued and then archived.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#parameters-2 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-archive-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **include\_pipeline\_steps**<br>_optional_ | If set then for the passed pipeline controller tasks also archive the pipeline <br>steps <br>**Default** : `false` | boolean |
| **status\_message**<br>_optional_ | Extra information regarding status change | string |
| **status\_reason**<br>_optional_ | Reason for status change | string |
| **tasks**<br>_required_ | List of task ids | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#responses-2 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-archive-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **archived**<br>_optional_ | Indicates number of archived tasks | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#security-2 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /tasks.archive\_many [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#post-tasksarchive_many "Direct link to POST /tasks.archive_many")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#description-3 "Direct link to Description")

Archive tasks

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#parameters-3 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-archive_many-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **ids**<br>_required_ | IDs of the tasks to archive | < string > array |
| **include\_pipeline\_steps**<br>_optional_ | If set then for the passed pipeline controller tasks also archive the pipeline <br>steps <br>**Default** : `false` | boolean |
| **status\_message**<br>_optional_ | Extra information regarding status change | string |
| **status\_reason**<br>_optional_ | Reason for status change | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#responses-3 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-archive_many-response-200) |

**Response 200**

| Name | Schema |
| --- | --- |
| **failed**<br>_optional_ | < [failed](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-archive_many-post-failed) \> array |
| **succeeded**<br>_optional_ | < [succeeded](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-archive_many-post-succeeded) \> array |

**failed**

| Name | Description | Schema |
| --- | --- | --- |
| **error**<br>_optional_ | Error info | [error](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-archive_many-post-failed-error) |
| **id**<br>_optional_ | ID of the failed entity | string |

**error**

| Name | Schema |
| --- | --- |
| **codes**<br>_optional_ | < integer > array |
| **data**<br>_optional_ | object |
| **msg**<br>_optional_ | string |

**succeeded**

| Name | Description | Schema |
| --- | --- | --- |
| **archived**<br>_optional_ | Indicates whether the task was archived | boolean |
| **id**<br>_optional_ | ID of the succeeded entity | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#security-3 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /tasks.clear\_operations\_log [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#post-tasksclear_operations_log "Direct link to POST /tasks.clear_operations_log")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#description-4 "Direct link to Description")

Clear the task operations log

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#parameters-4 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-clear_operations_log-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **task**<br>_required_ | Task ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#responses-4 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-clear_operations_log-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **deleted**<br>_optional_ | The amount of the deleted operations | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#security-4 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /tasks.clone [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#post-tasksclone "Direct link to POST /tasks.clone")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#description-5 "Direct link to Description")

Clone an existing task

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#parameters-5 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-clone-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **execution\_overrides**<br>_optional_ | The execution params for the cloned task. The params not specified are taken <br>from the original task | [tasks.execution](https://clear.ml/docs/latest/docs/references/enterprise/definitions#tasksexecution) |
| **input\_overrides**<br>_optional_ | The input params for the cloned task. The params not specified are taken from <br>the original task | [tasks.input](https://clear.ml/docs/latest/docs/references/enterprise/definitions#tasksinput) |
| **new\_project\_name**<br>_optional_ | Clone task to a new project by this name (only if `new_task_project` is not <br>provided). If a project by this name already exists, task will be cloned to <br>existing project. | string |
| **new\_task\_comment**<br>_optional_ | The comment of the cloned task. If not provided then taken from the original <br>task | string |
| **new\_task\_configuration**<br>_optional_ | The configuration for the new task. If not provided then taken from the <br>original task | < string, [tasks.configuration\_item](https://clear.ml/docs/latest/docs/references/enterprise/definitions#tasksconfiguration_item) \> map |
| **new\_task\_container**<br>_optional_ | The docker container properties for the new task. If not provided then taken <br>from the original task | < string, string > map |
| **new\_task\_hyperparams**<br>_optional_ | The hyper params for the new task. If not provided then taken from the original <br>task | < string, [tasks.section\_params](https://clear.ml/docs/latest/docs/references/enterprise/definitions#taskssection_params) \> map |
| **new\_task\_input\_models**<br>_optional_ | The list of input models for the cloned task. If not specifed then copied from <br>the original task | < [tasks.task\_model\_item](https://clear.ml/docs/latest/docs/references/enterprise/definitions#taskstask_model_item) \> array |
| **new\_task\_name**<br>_optional_ | The name of the cloned task. If not provided then taken from the original task | string |
| **new\_task\_parent**<br>_optional_ | The parent of the cloned task. If not provided then taken from the original <br>task | string |
| **new\_task\_project**<br>_optional_ | The project of the cloned task. If not provided then taken from the original <br>task | string |
| **new\_task\_system\_tags**<br>_optional_ | The system tags of the cloned task. If not provided then empty | < string > array |
| **new\_task\_tags**<br>_optional_ | The user-defined tags of the cloned task. If not provided then taken from the <br>original task | < string > array |
| **script\_overrides**<br>_optional_ | The script params for the cloned task. The params not specified are taken from <br>the original task | [tasks.script](https://clear.ml/docs/latest/docs/references/enterprise/definitions#tasksscript) |
| **task**<br>_required_ | ID of the task | string |
| **validate\_references**<br>_optional_ | If set to 'false' then the task fields that are copied from the original task <br>are not validated. The default is false. | boolean |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#responses-5 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-clone-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_optional_ | ID of the new task | string |
| **new\_project**<br>_optional_ | In case the new\_project\_name was specified returns the target project details | [new\_project](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-clone-post-new_project) |

**new\_project**

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_optional_ | The ID of the target project | string |
| **name**<br>_optional_ | The name of the target project | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#security-5 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /tasks.close [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#post-tasksclose "Direct link to POST /tasks.close")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#description-6 "Direct link to Description")

Indicates that task is closed

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#parameters-6 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-close-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **force**<br>_optional_ | Allows forcing state change even if transition is not supported <br>**Default** : `false` | boolean |
| **status\_message**<br>_optional_ | Extra information regarding status change | string |
| **status\_reason**<br>_optional_ | Reason for status change | string |
| **task**<br>_required_ | Task ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#responses-6 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-close-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **fields**<br>_optional_ | Updated fields names and values | object |
| **updated**<br>_optional_ | Number of tasks updated (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#security-6 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /tasks.completed [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#post-taskscompleted "Direct link to POST /tasks.completed")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#description-7 "Direct link to Description")

Signal a task has completed

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#parameters-7 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-completed-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **force**<br>_optional_ | If not true, call fails if the task status is not in\_progress/stopped <br>**Default** : `false` | boolean |
| **publish**<br>_optional_ | If set and the task is completed successfully then it is published <br>**Default** : `false` | boolean |
| **status\_message**<br>_optional_ | Extra information regarding status change | string |
| **status\_reason**<br>_optional_ | Reason for status change | string |
| **task**<br>_required_ | Task ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#responses-7 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-completed-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **fields**<br>_optional_ | Updated fields names and values | object |
| **published**<br>_optional_ | Number of tasks published (0 or 1) | integer |
| **updated**<br>_optional_ | Number of tasks updated (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#security-7 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /tasks.create [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#post-taskscreate "Direct link to POST /tasks.create")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#description-8 "Direct link to Description")

Create a new task

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#parameters-8 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-create-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **comment**<br>_optional_ | Free text comment | string |
| **configuration**<br>_optional_ | Task configuration params | < string, [tasks.configuration\_item](https://clear.ml/docs/latest/docs/references/enterprise/definitions#tasksconfiguration_item) \> map |
| **container**<br>_optional_ | Docker container parameters | < string, string > map |
| **execution**<br>_optional_ | Task execution params | [tasks.execution](https://clear.ml/docs/latest/docs/references/enterprise/definitions#tasksexecution) |
| **hyperparams**<br>_optional_ | Task hyper params per section | < string, [tasks.section\_params](https://clear.ml/docs/latest/docs/references/enterprise/definitions#taskssection_params) \> map |
| **input**<br>_optional_ |  | [tasks.input](https://clear.ml/docs/latest/docs/references/enterprise/definitions#tasksinput) |
| **models**<br>_optional_ | Task models | [tasks.task\_models](https://clear.ml/docs/latest/docs/references/enterprise/definitions#taskstask_models) |
| **name**<br>_required_ | Task name. Unique within the company. | string |
| **output\_dest**<br>_optional_ | Output storage id Must be a reference to an existing storage. | string |
| **parent**<br>_optional_ | Parent task id Must be a completed task. | string |
| **project**<br>_optional_ | Project ID of the project to which this task is assigned Must exist\[ab\] | string |
| **script**<br>_optional_ |  | [tasks.script](https://clear.ml/docs/latest/docs/references/enterprise/definitions#tasksscript) |
| **system\_tags**<br>_optional_ | System tags list. This field is reserved for system use, please don't use it. | < string > array |
| **tags**<br>_optional_ | User-defined tags list | < string > array |
| **type**<br>_required_ |  | [tasks.task\_type\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions#taskstask_type_enum) |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#responses-8 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-create-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_optional_ | ID of the task | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#security-8 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /tasks.delete [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#post-tasksdelete "Direct link to POST /tasks.delete")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#description-9 "Direct link to Description")

Delete a task along with any information stored for it (statistics, frame

updates etc.) Unless Force flag is provided, operation will fail if task has

objects associated with it - i.e. children tasks, projects or datasets. Models

that refer to the deleted task will be updated with a task ID indicating a

deleted task.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#parameters-9 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-delete-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **delete\_external\_artifacts**<br>_optional_ | If set to 'true' then BE will try to delete the extenal artifacts associated <br>with the task from the fileserver (if configured to do so) <br>**Default** : `true` | boolean |
| **delete\_output\_models**<br>_optional_ | If set to 'true' then delete output models of this task that are not referenced <br>by other tasks. Default value is 'true' | boolean |
| **force**<br>_optional_ | If not true, call fails if the task status is 'in\_progress' <br>**Default** : `false` | boolean |
| **include\_pipeline\_steps**<br>_optional_ | If set then and the passed task is a pipeline controller then delete the <br>pipeline tasks too <br>**Default** : `false` | boolean |
| **move\_to\_trash**<br>_optional_ | Move task to trash instead of deleting it. For internal use only, tasks in the <br>trash are not visible from the API and cannot be restored! <br>**Default** : `false` | boolean |
| **return\_file\_urls**<br>_optional_ | If set to 'true' then return the urls of the files that were uploaded by this <br>task. Default value is 'false' | boolean |
| **status\_message**<br>_optional_ | Extra information regarding status change | string |
| **status\_reason**<br>_optional_ | Reason for status change | string |
| **task**<br>_required_ | Task ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#responses-9 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-delete-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **deleted**<br>_optional_ | Indicates whether the task was deleted | boolean |
| **events**<br>_optional_ | Response from events.delete\_for\_task | object |
| **frames**<br>_optional_ | Response from frames.rollback | object |
| **updated\_children**<br>_optional_ | Number of child tasks whose parent property was updated | integer |
| **updated\_models**<br>_optional_ | Number of models whose task property was updated | integer |
| **updated\_versions**<br>_optional_ | Number of dataset versions whose task property was updated | integer |
| **urls**<br>_optional_ | The urls of the files that were uploaded by this task. Returned if the <br>'return\_file\_urls' was set to 'true' | [tasks.task\_urls](https://clear.ml/docs/latest/docs/references/enterprise/definitions#taskstask_urls) |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#security-9 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /tasks.delete\_artifacts [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#post-tasksdelete_artifacts "Direct link to POST /tasks.delete_artifacts")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#description-10 "Direct link to Description")

Delete existing artifacts (search by key/mode)

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#parameters-10 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-delete_artifacts-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **artifacts**<br>_required_ | Artifacts to delete | < [tasks.artifact\_id](https://clear.ml/docs/latest/docs/references/enterprise/definitions#tasksartifact_id) \> array |
| **force**<br>_optional_ | If set to True then both new and running task artifacts can be deleted. <br>Otherwise only the new task ones. Default is False | boolean |
| **task**<br>_required_ | Task ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#responses-10 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-delete_artifacts-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **deleted**<br>_optional_ | Indicates if the task was updated successfully | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#security-10 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /tasks.delete\_configuration [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#post-tasksdelete_configuration "Direct link to POST /tasks.delete_configuration")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#description-11 "Direct link to Description")

Delete task configuration items

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#parameters-11 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-delete_configuration-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **configuration**<br>_required_ | List of configuration itemss to delete | < string > array |
| **force**<br>_optional_ | If set to True then both new and running task configuration can be deleted. <br>Otherwise only the new task ones. Default is False | boolean |
| **task**<br>_required_ | Task ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#responses-11 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-delete_configuration-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **deleted**<br>_optional_ | Indicates if the task was updated successfully | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#security-11 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /tasks.delete\_hyper\_params [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#post-tasksdelete_hyper_params "Direct link to POST /tasks.delete_hyper_params")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#description-12 "Direct link to Description")

Delete task hyper parameters

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#parameters-12 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-delete_hyper_params-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **force**<br>_optional_ | If set to True then both new and running task hyper params can be deleted. <br>Otherwise only the new task ones. Default is False | boolean |
| **hyperparams**<br>_required_ | List of hyper parameters to delete. In case a parameter with an empty name is <br>passed all the section will be deleted | < [tasks.param\_key](https://clear.ml/docs/latest/docs/references/enterprise/definitions#tasksparam_key) \> array |
| **task**<br>_required_ | Task ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#responses-12 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-delete_hyper_params-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **deleted**<br>_optional_ | Indicates if the task was updated successfully | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#security-12 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /tasks.delete\_many [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#post-tasksdelete_many "Direct link to POST /tasks.delete_many")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#description-13 "Direct link to Description")

Delete tasks

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#parameters-13 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-delete_many-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **delete\_external\_artifacts**<br>_optional_ | If set to 'true' then BE will try to delete the extenal artifacts associated <br>with the tasks from the fileserver (if configured to do so) <br>**Default** : `true` | boolean |
| **delete\_output\_models**<br>_optional_ | If set to 'true' then delete output models of the tasks that are not referenced <br>by other tasks. Default value is 'true' | boolean |
| **force**<br>_optional_ | If not true, call fails if the task status is 'in\_progress' <br>**Default** : `false` | boolean |
| **ids**<br>_required_ | IDs of the tasks to delete | < string > array |
| **include\_pipeline\_steps**<br>_optional_ | If set then for the passed pipeline controller tasks also delete the pipeline <br>steps <br>**Default** : `false` | boolean |
| **move\_to\_trash**<br>_optional_ | Move task to trash instead of deleting it. For internal use only, tasks in the <br>trash are not visible from the API and cannot be restored! <br>**Default** : `false` | boolean |
| **return\_file\_urls**<br>_optional_ | If set to 'true' then return the urls of the files that were uploaded by the <br>tasks. Default value is 'false' | boolean |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#responses-13 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-delete_many-response-200) |

**Response 200**

| Name | Schema |
| --- | --- |
| **failed**<br>_optional_ | < [failed](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-delete_many-post-failed) \> array |
| **succeeded**<br>_optional_ | < [succeeded](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-delete_many-post-succeeded) \> array |

**failed**

| Name | Description | Schema |
| --- | --- | --- |
| **error**<br>_optional_ | Error info | [error](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-delete_many-post-failed-error) |
| **id**<br>_optional_ | ID of the failed entity | string |

**error**

| Name | Schema |
| --- | --- |
| **codes**<br>_optional_ | < integer > array |
| **data**<br>_optional_ | object |
| **msg**<br>_optional_ | string |

**succeeded**

| Name | Description | Schema |
| --- | --- | --- |
| **deleted**<br>_optional_ | Indicates whether the task was deleted | boolean |
| **deleted\_models**<br>_optional_ | Number of deleted output models | integer |
| **deleted\_versions**<br>_optional_ | Number of deleted dataset versions | integer |
| **id**<br>_optional_ | ID of the succeeded entity | string |
| **updated\_children**<br>_optional_ | Number of child tasks whose parent property was updated | integer |
| **updated\_models**<br>_optional_ | Number of models whose task property was updated | integer |
| **urls**<br>_optional_ | The urls of the files that were uploaded by the task. Returned if the <br>'return\_file\_urls' was set to 'true' | [tasks.task\_urls](https://clear.ml/docs/latest/docs/references/enterprise/definitions#taskstask_urls) |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#security-13 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /tasks.delete\_models [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#post-tasksdelete_models "Direct link to POST /tasks.delete_models")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#description-14 "Direct link to Description")

Delete models from task

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#parameters-14 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-delete_models-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **models**<br>_required_ | The list of models to delete | < [models](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-delete_models-post-models) \> array |
| **task**<br>_required_ | ID of the task | string |

**models**

| Name | Description | Schema |
| --- | --- | --- |
| **name**<br>_required_ | The task model name | string |
| **type**<br>_required_ | The task model type | [tasks.model\_type\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions#tasksmodel_type_enum) |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#responses-14 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-delete_models-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **updated**<br>_optional_ | Number of tasks updated (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#security-14 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /tasks.dequeue [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#post-tasksdequeue "Direct link to POST /tasks.dequeue")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#description-15 "Direct link to Description")

Remove a task from its queue. Fails if task status is not queued.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#parameters-15 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-dequeue-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **new\_status**<br>_optional_ | The new status to assign to the task after the dequeue instead of the default <br>one | string |
| **remove\_from\_all\_queues**<br>_optional_ | If set to 'true' then the task is searched and removed from all the queues. <br>Otherwise only from the queue stored in the task execution parameters <br>**Default** : `false` | boolean |
| **status\_message**<br>_optional_ | Extra information regarding status change | string |
| **status\_reason**<br>_optional_ | Reason for status change | string |
| **task**<br>_required_ | Task ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#responses-15 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-dequeue-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **dequeued**<br>_optional_ | Number of tasks dequeued (0 or 1) | integer |
| **fields**<br>_optional_ | Updated fields names and values | object |
| **updated**<br>_optional_ | Number of tasks updated (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#security-15 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /tasks.dequeue\_many [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#post-tasksdequeue_many "Direct link to POST /tasks.dequeue_many")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#description-16 "Direct link to Description")

Dequeue tasks

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#parameters-16 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-dequeue_many-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **ids**<br>_required_ | IDs of the tasks to dequeue | < string > array |
| **new\_status**<br>_optional_ | The new status to assign to the task after the dequeue instead of the default <br>one | string |
| **remove\_from\_all\_queues**<br>_optional_ | If set to 'true' then the tasks are searched and removed from all the queues. <br>Otherwise only from the queue stored in the task execution parameters <br>**Default** : `false` | boolean |
| **status\_message**<br>_optional_ | Extra information regarding status change | string |
| **status\_reason**<br>_optional_ | Reason for status change | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#responses-16 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-dequeue_many-response-200) |

**Response 200**

| Name | Schema |
| --- | --- |
| **failed**<br>_optional_ | < [failed](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-dequeue_many-post-failed) \> array |
| **succeeded**<br>_optional_ | < [succeeded](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-dequeue_many-post-succeeded) \> array |

**failed**

| Name | Description | Schema |
| --- | --- | --- |
| **error**<br>_optional_ | Error info | [error](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-dequeue_many-post-failed-error) |
| **id**<br>_optional_ | ID of the failed entity | string |

**error**

| Name | Schema |
| --- | --- |
| **codes**<br>_optional_ | < integer > array |
| **data**<br>_optional_ | object |
| **msg**<br>_optional_ | string |

**succeeded**

| Name | Description | Schema |
| --- | --- | --- |
| **dequeued**<br>_optional_ | Indicates whether the task was dequeued | boolean |
| **fields**<br>_optional_ | Updated fields names and values | object |
| **id**<br>_optional_ | ID of the succeeded entity | string |
| **updated**<br>_optional_ | Number of tasks updated (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#security-16 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /tasks.edit [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#post-tasksedit "Direct link to POST /tasks.edit")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#description-17 "Direct link to Description")

Edit task's details.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#parameters-17 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-edit-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **comment**<br>_optional_ | Free text comment | string |
| **configuration**<br>_optional_ | Task configuration params | < string, [tasks.configuration\_item](https://clear.ml/docs/latest/docs/references/enterprise/definitions#tasksconfiguration_item) \> map |
| **container**<br>_optional_ | Docker container parameters | < string, string > map |
| **execution**<br>_optional_ | Task execution params | [tasks.execution](https://clear.ml/docs/latest/docs/references/enterprise/definitions#tasksexecution) |
| **force**<br>_optional_ | If not true, call fails if the task status is not 'created' <br>**Default** : `false` | boolean |
| **hyperparams**<br>_optional_ | Task hyper params per section | < string, [tasks.section\_params](https://clear.ml/docs/latest/docs/references/enterprise/definitions#taskssection_params) \> map |
| **input**<br>_optional_ |  | [tasks.input](https://clear.ml/docs/latest/docs/references/enterprise/definitions#tasksinput) |
| **models**<br>_optional_ | Task models | [tasks.task\_models](https://clear.ml/docs/latest/docs/references/enterprise/definitions#taskstask_models) |
| **name**<br>_optional_ | Task name Unique within the company. | string |
| **output\_dest**<br>_optional_ | Output storage id Must be a reference to an existing storage. | string |
| **parent**<br>_optional_ | Parent task id Must be a completed task. | string |
| **project**<br>_optional_ | Project ID of the project to which this task is assigned Must exist\[ab\] | string |
| **runtime**<br>_optional_ | Task runtime mapping | object |
| **script**<br>_optional_ |  | [tasks.script](https://clear.ml/docs/latest/docs/references/enterprise/definitions#tasksscript) |
| **system\_tags**<br>_optional_ | System tags list. This field is reserved for system use, please don't use it. | < string > array |
| **tags**<br>_optional_ | User-defined tags list | < string > array |
| **task**<br>_required_ | ID of the task | string |
| **type**<br>_optional_ |  | [tasks.task\_type\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions#taskstask_type_enum) |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#responses-17 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-edit-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **fields**<br>_optional_ | Updated fields names and values | object |
| **updated**<br>_optional_ | Number of tasks updated (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#security-17 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /tasks.edit\_configuration [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#post-tasksedit_configuration "Direct link to POST /tasks.edit_configuration")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#description-18 "Direct link to Description")

Add or update task configuration

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#parameters-18 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-edit_configuration-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **configuration**<br>_required_ | Task configuration items. The new ones will be added and the already existing <br>ones will be updated | < [tasks.configuration\_item](https://clear.ml/docs/latest/docs/references/enterprise/definitions#tasksconfiguration_item) \> array |
| **force**<br>_optional_ | If set to True then both new and running task configuration can be edited. <br>Otherwise only the new task ones. Default is False | boolean |
| **replace\_configuration**<br>_optional_ | If set then the all the configuration items will be replaced with the provided <br>ones. Otherwise only the provided configuration items will be updated or added | boolean |
| **task**<br>_required_ | Task ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#responses-18 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-edit_configuration-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **updated**<br>_optional_ | Indicates if the task was updated successfully | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#security-18 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /tasks.edit\_hyper\_params [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#post-tasksedit_hyper_params "Direct link to POST /tasks.edit_hyper_params")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#description-19 "Direct link to Description")

Add or update task hyper parameters

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#parameters-19 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-edit_hyper_params-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **force**<br>_optional_ | If set to True then both new and running task hyper params can be edited. <br>Otherwise only the new task ones. Default is False | boolean |
| **hyperparams**<br>_required_ | Task hyper parameters. The new ones will be added and the already existing ones <br>will be updated | < [tasks.params\_item](https://clear.ml/docs/latest/docs/references/enterprise/definitions#tasksparams_item) \> array |
| **replace\_hyperparams**<br>_optional_ | Can be set to one of the following: 'all' - all the hyper parameters will be <br>replaced with the provided ones 'section' - the sections that present in the <br>new parameters will be replaced with the provided parameters 'none' (the <br>default value) - only the specific parameters will be updated or added | [tasks.replace\_hyperparams\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions#tasksreplace_hyperparams_enum) |
| **task**<br>_required_ | Task ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#responses-19 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-edit_hyper_params-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **updated**<br>_optional_ | Indicates if the task was updated successfully | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#security-19 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /tasks.edit\_runtime [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#post-tasksedit_runtime "Direct link to POST /tasks.edit_runtime")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#description-20 "Direct link to Description")

Edit task's runtime properties by adding, updating or removing existing fields

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#parameters-20 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-edit_runtime-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **add\_or\_update**<br>_optional_ | Runtime properties to be updated or added (key/value) | < string, string > map |
| **force**<br>_optional_ | If set to 'true' then both new and running task runtime can be edited. <br>Otherwise only the new task ones. Default is 'false' | boolean |
| **remove**<br>_optional_ | Runtime properties to be removed (list of keys) | < string > array |
| **task**<br>_required_ | Task ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#responses-20 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-edit_runtime-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **updated**<br>_optional_ | Indicates if the task was updated successfully | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#security-20 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /tasks.enqueue [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#post-tasksenqueue "Direct link to POST /tasks.enqueue")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#description-21 "Direct link to Description")

Adds a task into a queue. Fails if task state is not 'created'. Fails if the

following parameters in the task were not filled: \* execution.script.repository

- execution.script.entrypoint

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#parameters-21 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-enqueue-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **queue**<br>_optional_ | Queue id. If not provided and no queue name is passed then task is added to the <br>default queue. | string |
| **queue\_name**<br>_optional_ | The name of the queue. If the queue does not exist then it is auto-created. <br>Cannot be used together with the queue id | string |
| **status\_message**<br>_optional_ | Extra information regarding status change | string |
| **status\_reason**<br>_optional_ | Reason for status change | string |
| **task**<br>_required_ | Task ID | string |
| **update\_execution\_queue**<br>_optional_ | If set to false then the task 'execution.queue' is not updated. This can be <br>done only for the task that is already enqueued <br>**Default** : `true` | boolean |
| **verify\_watched\_queue**<br>_optional_ | If passed then check wheter there are any workers watiching the queue <br>**Default** : `false` | boolean |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#responses-21 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-enqueue-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **fields**<br>_optional_ | Updated fields names and values | object |
| **queue\_watched**<br>_optional_ | Returns Trueif there are workers or autscalers working with the queue | boolean |
| **queued**<br>_optional_ | Number of tasks queued (0 or 1) | integer |
| **updated**<br>_optional_ | Number of tasks updated (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#security-21 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /tasks.enqueue\_many [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#post-tasksenqueue_many "Direct link to POST /tasks.enqueue_many")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#description-22 "Direct link to Description")

Enqueue tasks

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#parameters-22 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-enqueue_many-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **ids**<br>_required_ | IDs of the tasks to enqueue | < string > array |
| **queue**<br>_optional_ | Queue id. If not provided and no queue name is passed then tasks are added to <br>the default queue. | string |
| **queue\_name**<br>_optional_ | The name of the queue. If the queue does not exist then it is auto-created. <br>Cannot be used together with the queue id | string |
| **status\_message**<br>_optional_ | Extra information regarding status change | string |
| **status\_reason**<br>_optional_ | Reason for status change | string |
| **validate\_tasks**<br>_optional_ | If set then tasks are validated before enqueue <br>**Default** : `false` | boolean |
| **verify\_watched\_queue**<br>_optional_ | If passed then check wheter there are any workers watiching the queue <br>**Default** : `false` | boolean |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#responses-22 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-enqueue_many-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **failed**<br>_optional_ |  | < [failed](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-enqueue_many-post-failed) \> array |
| **queue\_watched**<br>_optional_ | Returns Trueif there are workers or autscalers working with the queue | boolean |
| **succeeded**<br>_optional_ |  | < [succeeded](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-enqueue_many-post-succeeded) \> array |

**failed**

| Name | Description | Schema |
| --- | --- | --- |
| **error**<br>_optional_ | Error info | [error](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-enqueue_many-post-failed-error) |
| **id**<br>_optional_ | ID of the failed entity | string |

**error**

| Name | Schema |
| --- | --- |
| **codes**<br>_optional_ | < integer > array |
| **data**<br>_optional_ | object |
| **msg**<br>_optional_ | string |

**succeeded**

| Name | Description | Schema |
| --- | --- | --- |
| **fields**<br>_optional_ | Updated fields names and values | object |
| **id**<br>_optional_ | ID of the succeeded entity | string |
| **queued**<br>_optional_ | Indicates whether the task was queued | boolean |
| **updated**<br>_optional_ | Number of tasks updated (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#security-22 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /tasks.failed [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#post-tasksfailed "Direct link to POST /tasks.failed")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#description-23 "Direct link to Description")

Indicates that task has failed

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#parameters-23 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-failed-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **force**<br>_optional_ | Allows forcing state change even if transition is not supported <br>**Default** : `false` | boolean |
| **status\_message**<br>_optional_ | Extra information regarding status change | string |
| **status\_reason**<br>_optional_ | Reason for status change | string |
| **task**<br>_required_ | Task ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#responses-23 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-failed-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **fields**<br>_optional_ | Updated fields names and values | object |
| **updated**<br>_optional_ | Number of tasks updated (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#security-23 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /tasks.get\_all [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#post-tasksget_all "Direct link to POST /tasks.get_all")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#description-24 "Direct link to Description")

Get all the company's tasks and all public tasks

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#parameters-24 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-get_all-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **_all_**<br>_optional_ | Multi-field pattern condition (all fields match pattern) | [tasks.multi\_field\_pattern\_data](https://clear.ml/docs/latest/docs/references/enterprise/definitions#tasksmulti_field_pattern_data) |
| **_any_**<br>_optional_ | Multi-field pattern condition (any field matches pattern) | [tasks.multi\_field\_pattern\_data](https://clear.ml/docs/latest/docs/references/enterprise/definitions#tasksmulti_field_pattern_data) |
| **id**<br>_optional_ | List of IDs to filter by | < string > array |
| **include\_subprojects**<br>_optional_ | If set to 'true' and project field is set then tasks from the subprojects are <br>searched too <br>**Default** : `false` | boolean |
| **input.view.entries.dataset**<br>_optional_ | List of input dataset IDs | < string > array |
| **input.view.entries.version**<br>_optional_ | List of input dataset version IDs | < string > array |
| **name**<br>_optional_ | Get only tasks whose name matches this pattern (python regular expression <br>syntax) | string |
| **only\_fields**<br>_optional_ | List of task field names (nesting is supported using '.', e.g. <br>execution.model\_labels). If provided, this list defines the query's projection <br>(only these fields will be returned for each result entry) | < string > array |
| **order\_by**<br>_optional_ | List of field names to order by. When search\_text is used, '@text\_score' can be <br>used as a field representing the text score of returned documents. Use '-' <br>prefix to specify descending order. Optional, recommended when using page | < string > array |
| **page**<br>_optional_ | Page number, returns a specific page out of the resulting list of tasks <br>**Minimum value** : `0` | integer |
| **page\_size**<br>_optional_ | Page size, specifies the number of results returned in each page (last page may <br>contain fewer results) <br>**Minimum value** : `1` | integer |
| **parent**<br>_optional_ | Parent ID | string |
| **project**<br>_optional_ | List of project IDs | < string > array |
| **refresh\_scroll**<br>_optional_ | If set then all the data received with this scroll will be requeried | boolean |
| **scroll\_id**<br>_optional_ | Scroll ID returned from the previos calls to get\_all | string |
| **search\_hidden**<br>_optional_ | If set to 'true' then hidden tasks are included in the search results <br>**Default** : `false` | boolean |
| **search\_text**<br>_optional_ | Free text search query | string |
| **size**<br>_optional_ | The number of tasks to retrieve <br>**Minimum value** : `1` | integer |
| **status**<br>_optional_ | List of task status. | < [tasks.task\_status\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions#taskstask_status_enum) \> array |
| **status\_changed**<br>_optional_ | List of status changed constraint strings (utcformat, epoch) with an optional <br>prefix modifier (>, >=, <, <=) | < string > array |
| **system\_tags**<br>_optional_ | List of task system tags. Use '-' prefix to exclude system tags | < string > array |
| **tags**<br>_optional_ | List of task user-defined tags. Use '-' prefix to exclude tags | < string > array |
| **type**<br>_optional_ | List of task types. One or more of: 'training', 'testing', 'import', <br>'annotation', 'inference', 'data\_processing', 'application', 'monitor', <br>'controller', 'optimizer', 'service', 'qc' or 'custom' (case insensitive) | < string > array |
| **user**<br>_optional_ | List of user IDs used to filter results by the task's creating user | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#responses-24 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-get_all-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **scroll\_id**<br>_optional_ | Scroll ID that can be used with the next calls to get\_all to retrieve more data | string |
| **tasks**<br>_optional_ | List of tasks | < [tasks.task](https://clear.ml/docs/latest/docs/references/enterprise/definitions#taskstask) \> array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#security-24 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /tasks.get\_all\_ex [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#post-tasksget_all_ex "Direct link to POST /tasks.get_all_ex")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#description-25 "Direct link to Description")

Internal. Get all the company's tasks and all public tasks

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#parameters-25 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-get_all_ex-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **_all_**<br>_optional_ | Multi-field pattern condition (all fields match pattern) | [tasks.multi\_field\_pattern\_data](https://clear.ml/docs/latest/docs/references/enterprise/definitions#tasksmulti_field_pattern_data) |
| **_any_**<br>_optional_ | Multi-field pattern condition (any field matches pattern) | [tasks.multi\_field\_pattern\_data](https://clear.ml/docs/latest/docs/references/enterprise/definitions#tasksmulti_field_pattern_data) |
| **allow\_public**<br>_optional_ | Allow public tasks to be returned in the results <br>**Default** : `true` | boolean |
| **filters**<br>_optional_ | List of FilterRule ('OR' connection) | < string, [filters](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-get_all_ex-post-filters) \> map |
| **id**<br>_optional_ | List of IDs to filter by | < string > array |
| **include\_hidden\_projects**<br>_optional_ | If set to 'true' then tasks from hidden projects are included in search results <br>**Default** : `false` | boolean |
| **include\_subprojects**<br>_optional_ | If set to 'true' and project field is set then tasks from the subprojects are <br>searched too <br>**Default** : `false` | boolean |
| **input.view.entries.dataset**<br>_optional_ | List of input dataset IDs | < string > array |
| **input.view.entries.version**<br>_optional_ | List of input dataset version IDs | < string > array |
| **name**<br>_optional_ | Get only tasks whose name matches this pattern (python regular expression <br>syntax) | string |
| **only\_fields**<br>_optional_ | List of task field names (nesting is supported using '.', e.g. <br>execution.model\_labels). If provided, this list defines the query's projection <br>(only these fields will be returned for each result entry) | < string > array |
| **order\_by**<br>_optional_ | List of field names to order by. When search\_text is used, '@text\_score' can be <br>used as a field representing the text score of returned documents. Use '-' <br>prefix to specify descending order. Optional, recommended when using page | < string > array |
| **page**<br>_optional_ | Page number, returns a specific page out of the resulting list of tasks <br>**Minimum value** : `0` | integer |
| **page\_size**<br>_optional_ | Page size, specifies the number of results returned in each page (last page may <br>contain fewer results) <br>**Minimum value** : `1` | integer |
| **parent**<br>_optional_ | Parent ID | string |
| **project**<br>_optional_ | List of project IDs | < string > array |
| **refresh\_scroll**<br>_optional_ | If set then all the data received with this scroll will be requeried | boolean |
| **scroll\_id**<br>_optional_ | Scroll ID returned from the previos calls to get\_all\_ex | string |
| **search\_hidden**<br>_optional_ | If set to 'true' then hidden tasks are included in the search results <br>**Default** : `false` | boolean |
| **search\_text**<br>_optional_ | Free text search query | string |
| **size**<br>_optional_ | The number of tasks to retrieve <br>**Minimum value** : `1` | integer |
| **status**<br>_optional_ | List of task status. | < [tasks.task\_status\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions#taskstask_status_enum) \> array |
| **status\_changed**<br>_optional_ | List of status changed constraint strings (utcformat, epoch) with an optional <br>prefix modifier (>, >=, <, <=) | < string > array |
| **system\_tags**<br>_optional_ | List of task system tags. Use '-' prefix to exclude system tags | < string > array |
| **tags**<br>_optional_ | List of task user-defined tags. Use '-' prefix to exclude tags | < string > array |
| **type**<br>_optional_ | List of task types. One or more of: 'training', 'testing', 'import', <br>'annotation', 'inference', 'data\_processing', 'application', 'monitor', <br>'controller', 'optimizer', 'service', 'qc' or 'custom' (case insensitive) | < string > array |
| **user**<br>_optional_ | List of user IDs used to filter results by the task's creating user | < string > array |

**filters**

| Name | Description | Schema |
| --- | --- | --- |
| **all**<br>_optional_ | All the terms in 'all' condition are combined with 'and' operation | [all](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-get_all_ex-post-filters-all) |
| **any**<br>_optional_ | All the terms in 'any' condition are combined with 'or' operation | [any](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-get_all_ex-post-filters-any) |
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

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#responses-25 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-get_all_ex-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **scroll\_id**<br>_optional_ | Scroll ID that can be used with the next calls to get\_all\_ex to retrieve more <br>data | string |
| **tasks**<br>_optional_ | List of tasks | < [tasks.task](https://clear.ml/docs/latest/docs/references/enterprise/definitions#taskstask) \> array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#security-25 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /tasks.get\_by\_id [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#post-tasksget_by_id "Direct link to POST /tasks.get_by_id")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#description-26 "Direct link to Description")

Gets task information

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#parameters-26 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-get_by_id-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **task**<br>_required_ | Task ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#responses-26 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-get_by_id-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **task**<br>_optional_ | Task info | [tasks.task](https://clear.ml/docs/latest/docs/references/enterprise/definitions#taskstask) |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#security-26 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /tasks.get\_by\_id\_ex [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#post-tasksget_by_id_ex "Direct link to POST /tasks.get_by_id_ex")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#description-27 "Direct link to Description")

Internal. Get all the company's tasks and all public tasks

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#parameters-27 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-get_by_id_ex-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **_all_**<br>_optional_ | Multi-field pattern condition (all fields match pattern) | [tasks.multi\_field\_pattern\_data](https://clear.ml/docs/latest/docs/references/enterprise/definitions#tasksmulti_field_pattern_data) |
| **_any_**<br>_optional_ | Multi-field pattern condition (any field matches pattern) | [tasks.multi\_field\_pattern\_data](https://clear.ml/docs/latest/docs/references/enterprise/definitions#tasksmulti_field_pattern_data) |
| **id**<br>_optional_ | List of IDs to filter by | < string > array |
| **input.view.entries.dataset**<br>_optional_ | List of input dataset IDs | < string > array |
| **input.view.entries.version**<br>_optional_ | List of input dataset version IDs | < string > array |
| **name**<br>_optional_ | Get only tasks whose name matches this pattern (python regular expression <br>syntax) | string |
| **only\_fields**<br>_optional_ | List of task field names (nesting is supported using '.', e.g. <br>execution.model\_labels). If provided, this list defines the query's projection <br>(only these fields will be returned for each result entry) | < string > array |
| **order\_by**<br>_optional_ | List of field names to order by. When search\_text is used, '@text\_score' can be <br>used as a field representing the text score of returned documents. Use '-' <br>prefix to specify descending order. Optional, recommended when using page | < string > array |
| **page**<br>_optional_ | Page number, returns a specific page out of the resulting list of tasks <br>**Minimum value** : `0` | integer |
| **page\_size**<br>_optional_ | Page size, specifies the number of results returned in each page (last page may <br>contain fewer results) <br>**Minimum value** : `1` | integer |
| **parent**<br>_optional_ | Parent ID | string |
| **project**<br>_optional_ | List of project IDs | < string > array |
| **search\_text**<br>_optional_ | Free text search query | string |
| **status**<br>_optional_ | List of task status. | < [tasks.task\_status\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions#taskstask_status_enum) \> array |
| **status\_changed**<br>_optional_ | List of status changed constraint strings (utcformat, epoch) with an optional <br>prefix modifier (>, >=, <, <=) | < string > array |
| **system\_tags**<br>_optional_ | List of task system tags. Use '-' prefix to exclude system tags | < string > array |
| **tags**<br>_optional_ | List of task user-defined tags. Use '-' prefix to exclude tags | < string > array |
| **type**<br>_optional_ | List of task types. One or more of: 'training', 'testing', 'import', <br>'annotation', 'inference', 'data\_processing', 'application', 'monitor', <br>'controller', 'optimizer', 'service', 'qc' or 'custom' (case insensitive) | < string > array |
| **user**<br>_optional_ | List of user IDs used to filter results by the task's creating user | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#responses-27 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-get_by_id_ex-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **tasks**<br>_optional_ | List of tasks | < [tasks.task](https://clear.ml/docs/latest/docs/references/enterprise/definitions#taskstask) \> array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#security-27 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /tasks.get\_configuration\_names [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#post-tasksget_configuration_names "Direct link to POST /tasks.get_configuration_names")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#description-28 "Direct link to Description")

Get the list of task configuration items names

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#parameters-28 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-get_configuration_names-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **skip\_empty**<br>_optional_ | If set to 'true' then the names for configurations with missing values are not <br>returned <br>**Default** : `true` | boolean |
| **tasks**<br>_required_ | Task IDs | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#responses-28 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-get_configuration_names-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **configurations**<br>_optional_ | Names of task configuration items (keyed by task ID) | [configurations](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-get_configuration_names-post-configurations) |

**configurations**

| Name | Description | Schema |
| --- | --- | --- |
| **names**<br>_optional_ | Configuration names | < string > array |
| **task**<br>_optional_ | Task ID | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#security-28 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /tasks.get\_configurations [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#post-tasksget_configurations "Direct link to POST /tasks.get_configurations")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#description-29 "Direct link to Description")

Get the list of task configurations

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#parameters-29 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-get_configurations-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **names**<br>_optional_ | Names of the configuration items to retreive. If not passed or empty then all <br>the configurations will be retreived. | < string > array |
| **tasks**<br>_required_ | Task IDs | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#responses-29 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-get_configurations-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **configurations**<br>_optional_ | Configurations (keyed by task ID) | < [configurations](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-get_configurations-post-configurations) \> array |

**configurations**

| Name | Description | Schema |
| --- | --- | --- |
| **configuration**<br>_optional_ | Configuration list | < [tasks.configuration\_item](https://clear.ml/docs/latest/docs/references/enterprise/definitions#tasksconfiguration_item) \> array |
| **task**<br>_optional_ | Task ID | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#security-29 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /tasks.get\_hyper\_params [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#post-tasksget_hyper_params "Direct link to POST /tasks.get_hyper_params")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#description-30 "Direct link to Description")

Get the list of task hyper parameters

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#parameters-30 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-get_hyper_params-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **tasks**<br>_required_ | Task IDs | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#responses-30 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-get_hyper_params-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **params**<br>_optional_ | Hyper parameters (keyed by task ID) | < [params](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-get_hyper_params-post-params) \> array |

**params**

| Name | Description | Schema |
| --- | --- | --- |
| **hyperparams**<br>_optional_ | Hyper parameters | < [tasks.params\_item](https://clear.ml/docs/latest/docs/references/enterprise/definitions#tasksparams_item) \> array |
| **task**<br>_optional_ | Task ID | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#security-30 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /tasks.get\_operations\_log [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#post-tasksget_operations_log "Direct link to POST /tasks.get_operations_log")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#description-31 "Direct link to Description")

Get the task operations log

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#parameters-31 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-get_operations_log-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **group**<br>_optional_ | Group adjacent log records with the same operation. Turned on by default. Pass <br>'null' in order to cancel | [group](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-get_operations_log-post-group) |
| **order**<br>_optional_ | The time sorting <br>**Default** : `"desc"` | enum (asc, desc) |
| **page**<br>_optional_ | The page to retrieve | integer |
| **page\_size**<br>_optional_ | The amount of records to retrieve | integer |
| **task**<br>_required_ | Task ID | string |

**group**

| Name | Description | Schema |
| --- | --- | --- |
| **index**<br>_optional_ | Which element of the group to return. 0 - first, -1 - last | integer |
| **order**<br>_optional_ | Sorting inside the group <br>**Default** : `"asc"` | enum (asc, desc) |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#responses-31 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-get_operations_log-response-200) |

**Response 200**

| Name | Schema |
| --- | --- |
| **operations**<br>_optional_ | < [operations](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-get_operations_log-post-operations) \> array |

**operations**

| Name | Description | Schema |
| --- | --- | --- |
| **created**<br>_optional_ | Log record creation time | string (date-time) |
| **id**<br>_optional_ | Log record ID | string |
| **info**<br>_optional_ | The info that was passed by the client for the task operation if any | string |
| **ip**<br>_optional_ | The calling client IP | string |
| **operation**<br>_optional_ | The operation that was performed on the task. Either new task status or <br>'deleted' | string |
| **originator**<br>_optional_ | The calling agent | enum (agent, webapp, enterprise SDK, SDK, session, serving, task, python, curl, postman, other) |
| **originator\_id**<br>_optional_ | The calling client id | string |
| **originator\_version**<br>_optional_ | The calling agent version | string |
| **reason**<br>_optional_ | The reason for the task operation | string |
| **summary**<br>_optional_ | If grouped item contains more than one record then summary contains all the <br>records in the group | < [summary](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-get_operations_log-post-operations-summary) \> array |
| **user**<br>_optional_ |  | [user](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-get_operations_log-post-operations-user) |

**summary**

| Name | Description | Schema |
| --- | --- | --- |
| **created**<br>_optional_ | Log record creation time | string (date-time) |
| **id**<br>_optional_ | Log record ID | string |
| **info**<br>_optional_ | The info that was passed by the client for the task operation if any | string |
| **ip**<br>_optional_ | The calling client IP | string |
| **operation**<br>_optional_ | The operation that was performed on the task. Either new task status or <br>'deleted' | string |
| **originator**<br>_optional_ | The calling agent | enum (agent, webapp, enterprise SDK, SDK, session, serving, task, python, curl, postman, other) |
| **originator\_id**<br>_optional_ | The calling client id | string |
| **originator\_version**<br>_optional_ | The calling agent version | string |
| **reason**<br>_optional_ | The reason for the task operation | string |
| **user**<br>_optional_ |  | [user](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-get_operations_log-post-operations-summary-user) |

**user**

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_optional_ | User ID | string |
| **name**<br>_optional_ | User name | string |

**user**

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_optional_ | User ID | string |
| **name**<br>_optional_ | User name | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#security-31 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /tasks.get\_types [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#post-tasksget_types "Direct link to POST /tasks.get_types")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#description-32 "Direct link to Description")

Get the list of task types used in the specified projects

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#parameters-32 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-get_types-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **projects**<br>_optional_ | The list of projects which tasks will be analyzed. If not passed or empty then <br>all the company and public tasks will be analyzed | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#responses-32 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-get_types-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **types**<br>_optional_ | Unique list of the task types used in the requested projects | < string > array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#security-32 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /tasks.move [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#post-tasksmove "Direct link to POST /tasks.move")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#description-33 "Direct link to Description")

Move tasks to a project

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#parameters-33 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-move-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **ids**<br>_required_ | Tasks to move | < string > array |
| **project**<br>_optional_ | Target project ID. If not provided, `project_name` must be provided. Use null <br>for the root project | string |
| **project\_name**<br>_optional_ | Target project name. If provided and a project with this name does not exist, a <br>new project will be created. If not provided, `project` must be provided. | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#responses-33 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#security-33 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /tasks.ping [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#post-tasksping "Direct link to POST /tasks.ping")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#description-34 "Direct link to Description")

Refresh the task's last update time

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#parameters-34 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-ping-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **task**<br>_required_ | Task ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#responses-34 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#security-34 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /tasks.publish [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#post-taskspublish "Direct link to POST /tasks.publish")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#description-35 "Direct link to Description")

Mark a task status as published. For Annotation tasks - if any changes were

committed by this task, a new version in the dataset together with an output

view are created. For Training tasks - if a model was created, it should be set

to ready.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#parameters-35 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-publish-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **force**<br>_optional_ | If not true, call fails if the task status is not 'stopped' <br>**Default** : `false` | boolean |
| **publish\_model**<br>_optional_ | Indicates that the task output model (if exists) should be published. Optional, <br>the default value is True. | boolean |
| **status\_message**<br>_optional_ | Extra information regarding status change | string |
| **status\_reason**<br>_optional_ | Reason for status change | string |
| **task**<br>_required_ | Task ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#responses-35 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-publish-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **committed\_versions\_results**<br>_optional_ | Committed versions results | < object > array |
| **fields**<br>_optional_ | Updated fields names and values | object |
| **updated**<br>_optional_ | Number of tasks updated (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#security-35 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /tasks.publish\_many [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#post-taskspublish_many "Direct link to POST /tasks.publish_many")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#description-36 "Direct link to Description")

Publish tasks

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#parameters-36 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-publish_many-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **force**<br>_optional_ | If not true, call fails if the task status is not 'stopped' <br>**Default** : `false` | boolean |
| **ids**<br>_required_ | IDs of the tasks to publish | < string > array |
| **publish\_model**<br>_optional_ | Indicates that the task output model (if exists) should be published. Optional, <br>the default value is True. | boolean |
| **status\_message**<br>_optional_ | Extra information regarding status change | string |
| **status\_reason**<br>_optional_ | Reason for status change | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#responses-36 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-publish_many-response-200) |

**Response 200**

| Name | Schema |
| --- | --- |
| **failed**<br>_optional_ | < [failed](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-publish_many-post-failed) \> array |
| **succeeded**<br>_optional_ | < [succeeded](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-publish_many-post-succeeded) \> array |

**failed**

| Name | Description | Schema |
| --- | --- | --- |
| **error**<br>_optional_ | Error info | [error](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-publish_many-post-failed-error) |
| **id**<br>_optional_ | ID of the failed entity | string |

**error**

| Name | Schema |
| --- | --- |
| **codes**<br>_optional_ | < integer > array |
| **data**<br>_optional_ | object |
| **msg**<br>_optional_ | string |

**succeeded**

| Name | Description | Schema |
| --- | --- | --- |
| **committed\_versions\_results**<br>_optional_ | Committed versions results | < object > array |
| **fields**<br>_optional_ | Updated fields names and values | object |
| **id**<br>_optional_ | ID of the succeeded entity | string |
| **updated**<br>_optional_ | Number of tasks updated (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#security-36 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /tasks.reset [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#post-tasksreset "Direct link to POST /tasks.reset")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#description-37 "Direct link to Description")

Reset a task to its initial state, along with any information stored for it

(statistics, frame updates etc.).

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#parameters-37 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-reset-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **clear\_all**<br>_optional_ | Clear script and execution sections completely <br>**Default** : `false` | boolean |
| **delete\_external\_artifacts**<br>_optional_ | If set to 'true' then BE will try to delete the extenal artifacts associated <br>with the task from the fileserver (if configured to do so) <br>**Default** : `true` | boolean |
| **delete\_output\_models**<br>_optional_ | If set to 'true' then delete output models of this task that are not referenced <br>by other tasks. Default value is 'true' | boolean |
| **force**<br>_optional_ | If not true, call fails if the task status is 'completed' <br>**Default** : `false` | boolean |
| **return\_file\_urls**<br>_optional_ | If set to 'true' then return the urls of the files that were uploaded by this <br>task. Default value is 'false' | boolean |
| **status\_message**<br>_optional_ | Extra information regarding status change | string |
| **status\_reason**<br>_optional_ | Reason for status change | string |
| **task**<br>_required_ | Task ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#responses-37 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-reset-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **deleted\_indices**<br>_optional_ | List of deleted ES indices that were removed as part of the reset process | < string > array |
| **deleted\_models**<br>_optional_ | Number of output models deleted by the reset | integer |
| **dequeued**<br>_optional_ | Response from queues.remove\_task | object |
| **events**<br>_optional_ | Response from events.delete\_for\_task | object |
| **fields**<br>_optional_ | Updated fields names and values | object |
| **frames**<br>_optional_ | Response from frames.rollback | object |
| **updated**<br>_optional_ | Number of tasks updated (0 or 1) | integer |
| **urls**<br>_optional_ | The urls of the files that were uploaded by this task. Returned if the <br>'return\_file\_urls' was set to True | [tasks.task\_urls](https://clear.ml/docs/latest/docs/references/enterprise/definitions#taskstask_urls) |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#security-37 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /tasks.reset\_many [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#post-tasksreset_many "Direct link to POST /tasks.reset_many")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#description-38 "Direct link to Description")

Reset tasks

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#parameters-38 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-reset_many-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **clear\_all**<br>_optional_ | Clear script and execution sections completely <br>**Default** : `false` | boolean |
| **delete\_external\_artifacts**<br>_optional_ | If set to 'true' then BE will try to delete the extenal artifacts associated <br>with the tasks from the fileserver (if configured to do so) <br>**Default** : `true` | boolean |
| **delete\_output\_models**<br>_optional_ | If set to 'true' then delete output models of the tasks that are not referenced <br>by other tasks. Default value is 'true' | boolean |
| **force**<br>_optional_ | If not true, call fails if the task status is 'completed' <br>**Default** : `false` | boolean |
| **ids**<br>_required_ | IDs of the tasks to reset | < string > array |
| **return\_file\_urls**<br>_optional_ | If set to 'true' then return the urls of the files that were uploaded by the <br>tasks. Default value is 'false' | boolean |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#responses-38 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-reset_many-response-200) |

**Response 200**

| Name | Schema |
| --- | --- |
| **failed**<br>_optional_ | < [failed](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-reset_many-post-failed) \> array |
| **succeeded**<br>_optional_ | < [succeeded](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-reset_many-post-succeeded) \> array |

**failed**

| Name | Description | Schema |
| --- | --- | --- |
| **error**<br>_optional_ | Error info | [error](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-reset_many-post-failed-error) |
| **id**<br>_optional_ | ID of the failed entity | string |

**error**

| Name | Schema |
| --- | --- |
| **codes**<br>_optional_ | < integer > array |
| **data**<br>_optional_ | object |
| **msg**<br>_optional_ | string |

**succeeded**

| Name | Description | Schema |
| --- | --- | --- |
| **deleted\_models**<br>_optional_ | Number of output models deleted by the reset | integer |
| **deleted\_versions**<br>_optional_ | Number of deleted dataset versions | integer |
| **dequeued**<br>_optional_ | Indicates whether the task was dequeued | boolean |
| **fields**<br>_optional_ | Updated fields names and values | object |
| **id**<br>_optional_ | ID of the succeeded entity | string |
| **updated**<br>_optional_ | Number of tasks updated (0 or 1) | integer |
| **urls**<br>_optional_ | The urls of the files that were uploaded by the task. Returned if the <br>'return\_file\_urls' was set to 'true' | [tasks.task\_urls](https://clear.ml/docs/latest/docs/references/enterprise/definitions#taskstask_urls) |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#security-38 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /tasks.set\_requirements [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#post-tasksset_requirements "Direct link to POST /tasks.set_requirements")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#description-39 "Direct link to Description")

Set the script requirements for a task

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#parameters-39 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-set_requirements-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **requirements**<br>_required_ | A JSON object containing requirements strings by key | object |
| **task**<br>_required_ | Task ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#responses-39 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-set_requirements-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **fields**<br>_optional_ | Updated fields names and values | object |
| **updated**<br>_optional_ | Number of tasks updated (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#security-39 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /tasks.started [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#post-tasksstarted "Direct link to POST /tasks.started")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#description-40 "Direct link to Description")

Mark a task status as in\_progress. Optionally allows to set the task's

execution progress.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#parameters-40 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-started-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **force**<br>_optional_ | If not true, call fails if the task status is not 'not\_started' <br>**Default** : `false` | boolean |
| **status\_message**<br>_optional_ | Extra information regarding status change | string |
| **status\_reason**<br>_optional_ | Reason for status change | string |
| **task**<br>_required_ | Task ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#responses-40 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-started-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **fields**<br>_optional_ | Updated fields names and values | object |
| **started**<br>_optional_ | Number of tasks started (0 or 1) | integer |
| **updated**<br>_optional_ | Number of tasks updated (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#security-40 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /tasks.stop [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#post-tasksstop "Direct link to POST /tasks.stop")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#description-41 "Direct link to Description")

Request to stop a running task

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#parameters-41 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-stop-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **force**<br>_optional_ | If not true, call fails if the task status is not 'in\_progress' <br>**Default** : `false` | boolean |
| **include\_pipeline\_steps**<br>_optional_ | If set and the passed task is a pipeline controller then stop all its steps too <br>**Default** : `false` | boolean |
| **status\_message**<br>_optional_ | Extra information regarding status change | string |
| **status\_reason**<br>_optional_ | Reason for status change | string |
| **task**<br>_required_ | Task ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#responses-41 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-stop-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **fields**<br>_optional_ | Updated fields names and values | object |
| **updated**<br>_optional_ | Number of tasks updated (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#security-41 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /tasks.stop\_many [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#post-tasksstop_many "Direct link to POST /tasks.stop_many")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#description-42 "Direct link to Description")

Request to stop running tasks

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#parameters-42 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-stop_many-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **force**<br>_optional_ | If not true, call fails if the task status is not 'in\_progress' <br>**Default** : `false` | boolean |
| **ids**<br>_required_ | IDs of the tasks to stop | < string > array |
| **include\_pipeline\_steps**<br>_optional_ | If set then for all the passed pipeline controller tasks stop their steps too <br>**Default** : `false` | boolean |
| **status\_message**<br>_optional_ | Extra information regarding status change | string |
| **status\_reason**<br>_optional_ | Reason for status change | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#responses-42 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-stop_many-response-200) |

**Response 200**

| Name | Schema |
| --- | --- |
| **failed**<br>_optional_ | < [failed](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-stop_many-post-failed) \> array |
| **succeeded**<br>_optional_ | < [succeeded](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-stop_many-post-succeeded) \> array |

**failed**

| Name | Description | Schema |
| --- | --- | --- |
| **error**<br>_optional_ | Error info | [error](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-stop_many-post-failed-error) |
| **id**<br>_optional_ | ID of the failed entity | string |

**error**

| Name | Schema |
| --- | --- |
| **codes**<br>_optional_ | < integer > array |
| **data**<br>_optional_ | object |
| **msg**<br>_optional_ | string |

**succeeded**

| Name | Description | Schema |
| --- | --- | --- |
| **fields**<br>_optional_ | Updated fields names and values | object |
| **id**<br>_optional_ | ID of the succeeded entity | string |
| **updated**<br>_optional_ | Number of tasks updated (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#security-42 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /tasks.stopped [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#post-tasksstopped "Direct link to POST /tasks.stopped")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#description-43 "Direct link to Description")

Signal a task has stopped

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#parameters-43 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-stopped-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **force**<br>_optional_ | If not true, call fails if the task status is not 'stopped' <br>**Default** : `false` | boolean |
| **status\_message**<br>_optional_ | Extra information regarding status change | string |
| **status\_reason**<br>_optional_ | Reason for status change | string |
| **task**<br>_required_ | Task ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#responses-43 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-stopped-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **fields**<br>_optional_ | Updated fields names and values | object |
| **updated**<br>_optional_ | Number of tasks updated (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#security-43 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /tasks.unarchive\_many [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#post-tasksunarchive_many "Direct link to POST /tasks.unarchive_many")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#description-44 "Direct link to Description")

Unarchive tasks

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#parameters-44 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-unarchive_many-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **ids**<br>_required_ | IDs of the tasks to unarchive | < string > array |
| **include\_pipeline\_steps**<br>_optional_ | If set then for the passed pipeline controller tasks also archive the pipeline <br>steps <br>**Default** : `false` | boolean |
| **status\_message**<br>_optional_ | Extra information regarding status change | string |
| **status\_reason**<br>_optional_ | Reason for status change | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#responses-44 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-unarchive_many-response-200) |

**Response 200**

| Name | Schema |
| --- | --- |
| **failed**<br>_optional_ | < [failed](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-unarchive_many-post-failed) \> array |
| **succeeded**<br>_optional_ | < [succeeded](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-unarchive_many-post-succeeded) \> array |

**failed**

| Name | Description | Schema |
| --- | --- | --- |
| **error**<br>_optional_ | Error info | [error](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-unarchive_many-post-failed-error) |
| **id**<br>_optional_ | ID of the failed entity | string |

**error**

| Name | Schema |
| --- | --- |
| **codes**<br>_optional_ | < integer > array |
| **data**<br>_optional_ | object |
| **msg**<br>_optional_ | string |

**succeeded**

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_optional_ | ID of the succeeded entity | string |
| **unarchived**<br>_optional_ | Indicates whether the task was unarchived | boolean |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#security-44 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /tasks.update [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#post-tasksupdate "Direct link to POST /tasks.update")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#description-45 "Direct link to Description")

Update task's runtime parameters

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#parameters-45 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-update-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **comment**<br>_optional_ | Free text comment | string |
| **created**<br>_optional_ | Task creation time (UTC) | string (date-time) |
| **name**<br>_optional_ | Task name Unique within the company. | string |
| **output\_\_error**<br>_optional_ | Free text error | string |
| **project**<br>_optional_ | Project ID of the project to which this task is assigned | string |
| **system\_tags**<br>_optional_ | System tags list. This field is reserved for system use, please don't use it. | < string > array |
| **tags**<br>_optional_ | User-defined tags list | < string > array |
| **task**<br>_required_ | ID of the task | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#responses-45 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-update-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **fields**<br>_optional_ | Updated fields names and values | object |
| **updated**<br>_optional_ | Number of tasks updated (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#security-45 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /tasks.update\_batch [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#post-tasksupdate_batch "Direct link to POST /tasks.update_batch")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#description-46 "Direct link to Description")

Updates a batch of tasks. Headers Content type should be 'application/json-

lines'.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#parameters-46 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **requests**<br>_required_ | Json encoded newline-terminated lines, each representing an event in the batch and uses the same parameters used for tasks.update | < object > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#responses-46 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-update_batch-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **updated**<br>_optional_ | Number of tasks updated (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#security-46 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /tasks.update\_iteration [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#post-tasksupdate_iteration "Direct link to POST /tasks.update_iteration")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#description-47 "Direct link to Description")

Update task last iteration

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#parameters-47 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-update_iteration-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **iteration**<br>_required_ | Iteration value. Must be non-negative number | integer |
| **override\_iteration**<br>_optional_ | If set to 'true' then the task last\_iteration is set to the passed value. <br>Otherwise a max value between the existing task last iteration and the passed <br>one is chosen | integer |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#responses-47 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-update_iteration-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **updated**<br>_optional_ | 1 if the task was updated. 0 otherwise | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#security-47 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /tasks.update\_tags [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#post-tasksupdate_tags "Direct link to POST /tasks.update_tags")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#description-48 "Direct link to Description")

Add or remove tags from multiple tasks

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#parameters-48 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-update_tags-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **add\_tags**<br>_optional_ | User tags to add | < string > array |
| **ids**<br>_optional_ | IDs of the tasks to update | < string > array |
| **remove\_tags**<br>_optional_ | User tags to remove | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#responses-48 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-update_tags-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **updated**<br>_optional_ | The number of updated tasks | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#security-48 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /tasks.validate [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#post-tasksvalidate "Direct link to POST /tasks.validate")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#description-49 "Direct link to Description")

Validate task properties (before create)

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#parameters-49 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#tasks-validate-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **comment**<br>_optional_ | Free text comment | string |
| **configuration**<br>_optional_ | Task configuration params | < string, [tasks.configuration\_item](https://clear.ml/docs/latest/docs/references/enterprise/definitions#tasksconfiguration_item) \> map |
| **container**<br>_optional_ | Docker container parameters | < string, string > map |
| **execution**<br>_optional_ | Task execution params | [tasks.execution](https://clear.ml/docs/latest/docs/references/enterprise/definitions#tasksexecution) |
| **hyperparams**<br>_optional_ | Task hyper params per section | < string, [tasks.section\_params](https://clear.ml/docs/latest/docs/references/enterprise/definitions#taskssection_params) \> map |
| **input**<br>_optional_ |  | [tasks.input](https://clear.ml/docs/latest/docs/references/enterprise/definitions#tasksinput) |
| **models**<br>_optional_ | Task models | [tasks.task\_models](https://clear.ml/docs/latest/docs/references/enterprise/definitions#taskstask_models) |
| **name**<br>_required_ | Task name. Unique within the company. | string |
| **output\_dest**<br>_optional_ | Output storage id Must be a reference to an existing storage. | string |
| **parent**<br>_optional_ | Parent task id Must be a completed task. | string |
| **project**<br>_optional_ | Project ID of the project to which this task is assigned Must exist\[ab\] | string |
| **script**<br>_optional_ |  | [tasks.script](https://clear.ml/docs/latest/docs/references/enterprise/definitions#tasksscript) |
| **system\_tags**<br>_optional_ | System tags list. This field is reserved for system use, please don't use it. | < string > array |
| **tags**<br>_optional_ | User-defined tags list | < string > array |
| **type**<br>_required_ |  | [tasks.task\_type\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions#taskstask_type_enum) |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#responses-49 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tasks/\#security-49 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

- [POST /tasks.add\_or\_update\_artifacts](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#post-tasksadd_or_update_artifacts)
- [POST /tasks.add\_or\_update\_model](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#post-tasksadd_or_update_model)
- [POST /tasks.archive](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#post-tasksarchive)
- [POST /tasks.archive\_many](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#post-tasksarchive_many)
- [POST /tasks.clear\_operations\_log](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#post-tasksclear_operations_log)
- [POST /tasks.clone](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#post-tasksclone)
- [POST /tasks.close](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#post-tasksclose)
- [POST /tasks.completed](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#post-taskscompleted)
- [POST /tasks.create](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#post-taskscreate)
- [POST /tasks.delete](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#post-tasksdelete)
- [POST /tasks.delete\_artifacts](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#post-tasksdelete_artifacts)
- [POST /tasks.delete\_configuration](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#post-tasksdelete_configuration)
- [POST /tasks.delete\_hyper\_params](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#post-tasksdelete_hyper_params)
- [POST /tasks.delete\_many](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#post-tasksdelete_many)
- [POST /tasks.delete\_models](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#post-tasksdelete_models)
- [POST /tasks.dequeue](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#post-tasksdequeue)
- [POST /tasks.dequeue\_many](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#post-tasksdequeue_many)
- [POST /tasks.edit](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#post-tasksedit)
- [POST /tasks.edit\_configuration](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#post-tasksedit_configuration)
- [POST /tasks.edit\_hyper\_params](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#post-tasksedit_hyper_params)
- [POST /tasks.edit\_runtime](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#post-tasksedit_runtime)
- [POST /tasks.enqueue](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#post-tasksenqueue)
- [POST /tasks.enqueue\_many](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#post-tasksenqueue_many)
- [POST /tasks.failed](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#post-tasksfailed)
- [POST /tasks.get\_all](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#post-tasksget_all)
- [POST /tasks.get\_all\_ex](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#post-tasksget_all_ex)
- [POST /tasks.get\_by\_id](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#post-tasksget_by_id)
- [POST /tasks.get\_by\_id\_ex](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#post-tasksget_by_id_ex)
- [POST /tasks.get\_configuration\_names](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#post-tasksget_configuration_names)
- [POST /tasks.get\_configurations](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#post-tasksget_configurations)
- [POST /tasks.get\_hyper\_params](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#post-tasksget_hyper_params)
- [POST /tasks.get\_operations\_log](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#post-tasksget_operations_log)
- [POST /tasks.get\_types](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#post-tasksget_types)
- [POST /tasks.move](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#post-tasksmove)
- [POST /tasks.ping](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#post-tasksping)
- [POST /tasks.publish](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#post-taskspublish)
- [POST /tasks.publish\_many](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#post-taskspublish_many)
- [POST /tasks.reset](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#post-tasksreset)
- [POST /tasks.reset\_many](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#post-tasksreset_many)
- [POST /tasks.set\_requirements](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#post-tasksset_requirements)
- [POST /tasks.started](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#post-tasksstarted)
- [POST /tasks.stop](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#post-tasksstop)
- [POST /tasks.stop\_many](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#post-tasksstop_many)
- [POST /tasks.stopped](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#post-tasksstopped)
- [POST /tasks.unarchive\_many](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#post-tasksunarchive_many)
- [POST /tasks.update](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#post-tasksupdate)
- [POST /tasks.update\_batch](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#post-tasksupdate_batch)
- [POST /tasks.update\_iteration](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#post-tasksupdate_iteration)
- [POST /tasks.update\_tags](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#post-tasksupdate_tags)
- [POST /tasks.validate](https://clear.ml/docs/latest/docs/references/enterprise/tasks/#post-tasksvalidate)