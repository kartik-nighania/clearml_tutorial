---
url: "https://clear.ml/docs/latest/docs/references/enterprise/pipelines/"
title: "pipelines | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/enterprise/pipelines/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

### POST /pipelines.check\_new\_run [​](https://clear.ml/docs/latest/docs/references/enterprise/pipelines/\#post-pipelinescheck_new_run "Direct link to POST /pipelines.check_new_run")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/pipelines/\#description "Direct link to Description")

Check whether the pipeline can be started under the given project

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/pipelines/\#parameters "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/pipelines/#pipelines-check_new_run-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **new\_pipeline\_name**<br>_optional_ | The name of the pipeline. If not passed then the controller task name is used | string |
| **new\_project\_name**<br>_required_ | The name of the target project | string |
| **task**<br>_required_ | ID of the existing controller task | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/pipelines/\#responses "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/pipelines/#pipelines-check_new_run-response-200) |

**Response 200**

| Name | Schema |
| --- | --- |
| **existing\_project**<br>_optional_ | [existing\_project](https://clear.ml/docs/latest/docs/references/enterprise/pipelines/#pipelines-check_new_run-post-existing_project) |

**existing\_project**

| Name | Schema |
| --- | --- |
| **id**<br>_optional_ | string |
| **name**<br>_optional_ | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/pipelines/\#security "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /pipelines.delete\_runs [​](https://clear.ml/docs/latest/docs/references/enterprise/pipelines/\#post-pipelinesdelete_runs "Direct link to POST /pipelines.delete_runs")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/pipelines/\#description-1 "Direct link to Description")

Delete pipeline runs

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/pipelines/\#parameters-1 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/pipelines/#pipelines-delete_runs-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **ids**<br>_required_ | IDs of the pipeline runs to delete. Should be the ids of pipeline controller <br>tasks | < string > array |
| **project**<br>_required_ | Pipeline project ids. When deleting at least one run should be left | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/pipelines/\#responses-1 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/pipelines/#pipelines-delete_runs-response-200) |

**Response 200**

| Name | Schema |
| --- | --- |
| **failed**<br>_optional_ | < [failed](https://clear.ml/docs/latest/docs/references/enterprise/pipelines/#pipelines-delete_runs-post-failed) \> array |
| **succeeded**<br>_optional_ | < [succeeded](https://clear.ml/docs/latest/docs/references/enterprise/pipelines/#pipelines-delete_runs-post-succeeded) \> array |

**failed**

| Name | Description | Schema |
| --- | --- | --- |
| **error**<br>_optional_ | Error info | [error](https://clear.ml/docs/latest/docs/references/enterprise/pipelines/#pipelines-delete_runs-post-failed-error) |
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

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/pipelines/\#security-1 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /pipelines.start\_pipeline [​](https://clear.ml/docs/latest/docs/references/enterprise/pipelines/\#post-pipelinesstart_pipeline "Direct link to POST /pipelines.start_pipeline")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/pipelines/\#description-2 "Direct link to Description")

Start a pipeline

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/pipelines/\#parameters-2 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/pipelines/#pipelines-start_pipeline-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **args**<br>_optional_ | Task arguments, name/value to be placed in the hyperparameters Args section | < [args](https://clear.ml/docs/latest/docs/references/enterprise/pipelines/#pipelines-start_pipeline-post-args) \> array |
| **new\_pipeline\_name**<br>_optional_ | New pipeline name to start a pipeline in. Used only if new project name is <br>passed. If not passed then task name is used | string |
| **new\_pipeline\_version**<br>_optional_ | New pipeline version | string |
| **new\_project\_name**<br>_optional_ | Existing project name to start a pipeline in. If not provider then run in the <br>current project | string |
| **queue**<br>_optional_ | Queue ID in which the created pipeline task will be enqueued | string |
| **task**<br>_required_ | ID of the task on which the pipeline will be based | string |
| **verify\_watched\_queue**<br>_optional_ | If passed then check wheter there are any workers watiching the queue <br>**Default** : `false` | boolean |

**args**

| Name | Schema |
| --- | --- |
| **name**<br>_optional_ | string |
| **value**<br>_optional_ | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/pipelines/\#responses-2 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/pipelines/#pipelines-start_pipeline-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **enqueued**<br>_optional_ | True if the task was successfuly enqueued | boolean |
| **new\_project**<br>_optional_ | In case the project\_name was specified returns the target project details | [new\_project](https://clear.ml/docs/latest/docs/references/enterprise/pipelines/#pipelines-start_pipeline-post-new_project) |
| **pipeline**<br>_optional_ | ID of the new pipeline task | string |
| **queue\_watched**<br>_optional_ | Returns Trueif there are workers or autscalers working with the queue | boolean |

**new\_project**

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_optional_ | The ID of the target project | string |
| **name**<br>_optional_ | The name of the target project | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/pipelines/\#security-2 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

- [POST /pipelines.check\_new\_run](https://clear.ml/docs/latest/docs/references/enterprise/pipelines/#post-pipelinescheck_new_run)
- [POST /pipelines.delete\_runs](https://clear.ml/docs/latest/docs/references/enterprise/pipelines/#post-pipelinesdelete_runs)
- [POST /pipelines.start\_pipeline](https://clear.ml/docs/latest/docs/references/enterprise/pipelines/#post-pipelinesstart_pipeline)