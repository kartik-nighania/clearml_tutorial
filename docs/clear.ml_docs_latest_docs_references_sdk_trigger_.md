---
url: "https://clear.ml/docs/latest/docs/references/sdk/trigger/"
title: "TriggerScheduler | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/sdk/trigger/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

## _class_ automation.TriggerScheduler(pooling\_frequency\_minutes=3.0, sync\_frequency\_minutes=15, force\_create\_task\_name=None, force\_create\_task\_project=None) [​](https://clear.ml/docs/latest/docs/references/sdk/trigger/\#class-automationtriggerschedulerpooling_frequency_minutes30-sync_frequency_minutes15-force_create_task_namenone-force_create_task_projectnone "Direct link to class-automationtriggerschedulerpooling_frequency_minutes30-sync_frequency_minutes15-force_create_task_namenone-force_create_task_projectnone")

Trigger Task execution if an event happens in the system.

Examples:

- New model is published/tagged,

- New Dataset is created,

- General Task failed,

- Task metric below/above threshold, alert every X minutes


Create a Task trigger service

- **Parameters**
  - **pooling\_frequency\_minutes** (`float`) – Check for new events every X minutes (default 3)

  - **sync\_frequency\_minutes** (`float`) – Sync task scheduler configuration every X minutes.
    Allow to change scheduler in runtime by editing the Task configuration object

  - **force\_create\_task\_name** (`Optional`\[`str`\]) – Optional, force creation of Task Scheduler service,
    even if main Task.init already exists.

  - **force\_create\_task\_project** (`Optional`\[`str`\]) – Optional, force creation of Task Scheduler service,
    even if main Task.init already exists.

* * *

### add\_dataset\_trigger [​](https://clear.ml/docs/latest/docs/references/sdk/trigger/\#add_dataset_trigger "Direct link to add_dataset_trigger")

**add\_dataset\_trigger(schedule\_task\_id=None, schedule\_queue=None, schedule\_function=None, trigger\_project=None, trigger\_name=None, trigger\_on\_publish=None, trigger\_on\_tags=None, trigger\_on\_archive=None, trigger\_required\_tags=None, name=None, target\_project=None, add\_tag=True, single\_instance=False, reuse\_task=False, task\_parameters=None, task\_overrides=None)**

Create a cron job alike scheduling for a pre existing Task or function.
Trigger the Task/function execution on changes in the dataset repository (notice this is not the hyper-datasets).
Notice, it is recommended to give the trigger a descriptive unique name. If not provided, a task ID is used.

Notice task\_overrides can except reference to the trigger model ID:
example: `task_overrides={'Args/dataset_id': '${dataset.id}'}`.

Notice if schedule\_function is passed, use the following function interface:

```py
def schedule_function(dataset_id):

    pass
```

- **Parameters**
  - **schedule\_task\_id** (`Union`\[`str`, [`Task`](https://clear.ml/docs/latest/docs/references/sdk/task#clearml.Task), `None`\]) – Task/task ID to be cloned and scheduled for execution

  - **schedule\_queue** (`Optional`\[`str`\]) – Queue name or ID to put the Task into (i.e. schedule)

  - **schedule\_function** (`Optional`\[`Callable`\[\[`str`\], `None`\]\]) – Optional, instead of providing Task ID to be scheduled,
    provide a function to be called. Notice the function is called from the scheduler context
    (i.e. running on the same machine as the scheduler)

  - **name** (`Optional`\[`str`\]) – Name or description for the cron Task (should be unique if provided otherwise randomly generated)

  - **trigger\_project** (`Optional`\[`str`\]) – Only monitor datasets from this specific project (not recursive)

  - **trigger\_name** (`Optional`\[`str`\]) – Trigger only on datasets with name matching (regexp)

  - **trigger\_on\_publish** (`Optional`\[`bool`\]) – Trigger when dataset is published.

  - **trigger\_on\_tags** (`Optional`\[`List`\[`str`\]\]) – Trigger when all tags in the list are present

  - **trigger\_on\_archive** (`Optional`\[`bool`\]) – Trigger when dataset is archived

  - **trigger\_required\_tags** (`Optional`\[`List`\[`str`\]\]) – Trigger only on datasets with the
    following additional tags (must include all tags)

  - **target\_project** (`Optional`\[`str`\]) – Specify target project to put the cloned scheduled Task in.

  - **add\_tag** (`Union`\[`bool`, `str`\]) – Add tag to the executed Task. Provide specific tag (str) or
    pass True (default) to use the trigger name as tag

  - **single\_instance** (`bool`) – If True, do not launch the Task job if the previous instance is still running
    (skip until the next scheduled time period). Default False.

  - **reuse\_task** (`bool`) – If True, re-enqueue the same Task (i.e. do not clone it) every time, default False.

  - **task\_parameters** (`Optional`\[`dict`\]) – Configuration parameters to the executed Task.
    For example: `{'Args/batch': '12'}`. Notice: not available when reuse\_task=True/

  - **task\_overrides** (`Optional`\[`dict`\]) – Change task definition.
    For example `{'script.version_num': None, 'script.branch': 'main'}`. Notice: not available when reuse\_task=True
- **Return type**

`None`

- **Returns**

True if job is successfully added to the scheduling list


* * *

### add\_model\_trigger [​](https://clear.ml/docs/latest/docs/references/sdk/trigger/\#add_model_trigger "Direct link to add_model_trigger")

**add\_model\_trigger(schedule\_task\_id=None, schedule\_queue=None, schedule\_function=None, trigger\_project=None, trigger\_name=None, trigger\_on\_publish=None, trigger\_on\_tags=None, trigger\_on\_archive=None, trigger\_required\_tags=None, name=None, target\_project=None, add\_tag=True, single\_instance=False, reuse\_task=False, task\_parameters=None, task\_overrides=None)**

Create a cron job alike scheduling for a pre existing Task or function.
Trigger the Task/function execution on changes in the model repository
Notice it is recommended to give the trigger a descriptive unique name, if not provided a task ID is used.

Notice task\_overrides can except reference to the trigger model ID:
example: `task_overrides={'Args/model_id': '${model.id}'}`
Notice if schedule\_function is passed, use the following function interface:

```py
def schedule_function(model_id):

    pass
```

- **Parameters**
  - **schedule\_task\_id** (`Union`\[`str`, [`Task`](https://clear.ml/docs/latest/docs/references/sdk/task#clearml.Task), `None`\]) – Task/task ID to be cloned and scheduled for execution

  - **schedule\_queue** (`Optional`\[`str`\]) – Queue name or ID to put the Task into (i.e. schedule)

  - **schedule\_function** (`Optional`\[`Callable`\[\[`str`\], `None`\]\]) – Optional, instead of providing Task ID to be scheduled,
    provide a function to be called. Notice the function is called from the scheduler context
    (i.e. running on the same machine as the scheduler)

  - **name** (`Optional`\[`str`\]) – Name or description for the cron Task (should be unique if provided otherwise randomly generated)

  - **trigger\_project** (`Optional`\[`str`\]) – Only monitor models from this specific project (not recursive)

  - **trigger\_name** (`Optional`\[`str`\]) – Trigger only on models with name matching (regexp)

  - **trigger\_on\_publish** (`Optional`\[`bool`\]) – Trigger when model is published.

  - **trigger\_on\_tags** (`Optional`\[`List`\[`str`\]\]) – Trigger when all tags in the list are present

  - **trigger\_on\_archive** (`Optional`\[`bool`\]) – Trigger when model is archived

  - **trigger\_required\_tags** (`Optional`\[`List`\[`str`\]\]) – Trigger only on models with the following additional tags (must include all tags)

  - **target\_project** (`Optional`\[`str`\]) – Specify target project to put the cloned scheduled Task in.

  - **add\_tag** (`Union`\[`bool`, `str`\]) – Add tag to the executed Task. Provide specific tag (str) or
    pass True (default) to use the trigger name as tag

  - **single\_instance** (`bool`) – If True, do not launch the Task job if the previous instance is still running
    (skip until the next scheduled time period). Default False.

  - **reuse\_task** (`bool`) – If True, re-enqueue the same Task (i.e. do not clone it) every time, default False.

  - **task\_parameters** (`Optional`\[`dict`\]) – Configuration parameters to the executed Task.
    for example: `{'Args/batch': '12'}` Notice: not available when reuse\_task=True

  - **task\_overrides** (`Optional`\[`dict`\]) – Change task definition.
    for example `{'script.version_num': None, 'script.branch': 'main'}` Notice: not available when reuse\_task=True
- **Return type**

`None`

- **Returns**

True if job is successfully added to the scheduling list


* * *

### add\_task\_trigger [​](https://clear.ml/docs/latest/docs/references/sdk/trigger/\#add_task_trigger "Direct link to add_task_trigger")

**add\_task\_trigger(schedule\_task\_id=None, schedule\_queue=None, schedule\_function=None, trigger\_project=None, trigger\_name=None, trigger\_on\_tags=None, trigger\_on\_status=None, trigger\_exclude\_dev\_tasks=None, trigger\_on\_metric=None, trigger\_on\_variant=None, trigger\_on\_threshold=None, trigger\_on\_sign=None, trigger\_required\_tags=None, name=None, target\_project=None, add\_tag=True, single\_instance=False, reuse\_task=False, task\_parameters=None, task\_overrides=None)**

Create a cron job alike scheduling for a pre existing Task or function.
Trigger the Task/function execution on changes in the Task
Notice it is recommended to give the trigger a descriptive unique name, if not provided a task ID is used.

Notice task\_overrides can except reference to the trigger model ID:
example: `task_overrides={'Args/task_id': '${task.id}'}`
Notice if schedule\_function is passed, use the following function interface:

```py
def schedule_function(task_id):

    pass
```

- **Parameters**
  - **schedule\_task\_id** (`Union`\[`str`, [`Task`](https://clear.ml/docs/latest/docs/references/sdk/task#clearml.Task), `None`\]) – Task/task ID to be cloned and scheduled for execution

  - **schedule\_queue** (`Optional`\[`str`\]) – Queue name or ID to put the Task into (i.e. schedule)

  - **schedule\_function** (`Optional`\[`Callable`\[\[`str`\], `None`\]\]) – Optional, instead of providing Task ID to be scheduled,
    provide a function to be called. Notice the function is called from the scheduler context
    (i.e. running on the same machine as the scheduler)

  - **name** (`Optional`\[`str`\]) – Name or description for the cron Task (should be unique if provided otherwise randomly generated)

  - **trigger\_project** (`Optional`\[`str`\]) – Only monitor tasks from this specific project (not recursive)

  - **trigger\_name** (`Optional`\[`str`\]) – Trigger only on tasks with name matching (regexp)

  - **trigger\_on\_tags** (`Optional`\[`List`\[`str`\]\]) – Trigger when all tags in the list are present

  - **trigger\_required\_tags** (`Optional`\[`List`\[`str`\]\]) – Trigger only on tasks with the following additional tags (must include all tags)

  - **trigger\_on\_status** (`Optional`\[`List`\[`str`\]\]) – Trigger on Task status change. Expect list of status strings, e.g. \[‘failed’, ‘published’\].
    TaskStatusEnum: \[“created”, “in\_progress”, “stopped”, “closed”, “failed”, “completed”, “queued”, “published”,\
    “publishing”, “unknown”\]

  - **trigger\_exclude\_dev\_tasks** (`Optional`\[`bool`\]) – If True only trigger on Tasks executed by clearml-agent (and not manually)

  - **trigger\_on\_metric** (`Optional`\[`str`\]) – Trigger on metric/variant above/under threshold (metric=title, variant=series)

  - **trigger\_on\_variant** (`Optional`\[`str`\]) – Trigger on metric/variant above/under threshold (metric=title, variant=series)

  - **trigger\_on\_threshold** (`Optional`\[`float`\]) – Trigger on metric/variant above/under threshold (float number)

  - **trigger\_on\_sign** (`Optional`\[`str`\]) – possible values “max”/”maximum” or “min”/”minimum”,
    trigger Task if metric below “min” or “above” maximum. Default: “minimum”

  - **target\_project** (`Optional`\[`str`\]) – Specify target project to put the cloned scheduled Task in.

  - **add\_tag** (`Union`\[`bool`, `str`\]) – Add tag to the executed Task. Provide specific tag (str) or
    pass True (default) to use the trigger name as tag

  - **single\_instance** (`bool`) – If True, do not launch the Task job if the previous instance is still running
    (skip until the next scheduled time period). Default False.

  - **reuse\_task** (`bool`) – If True, re-enqueue the same Task (i.e. do not clone it) every time, default False.

  - **task\_parameters** (`Optional`\[`dict`\]) – Configuration parameters to the executed Task.
    for example: `{'Args/batch': '12'}` Notice: not available when reuse\_task=True/

  - **task\_overrides** (`Optional`\[`dict`\]) – Change task definition.
    for example `{'script.version_num': None, 'script.branch': 'main'}`. Notice: not available when reuse\_task=True
- **Return type**

`None`

- **Returns**

True if job is successfully added to the scheduling list


* * *

### get\_triggers [​](https://clear.ml/docs/latest/docs/references/sdk/trigger/\#get_triggers "Direct link to get_triggers")

**get\_triggers()**

Return all triggers (models, datasets, tasks)
:rtype: `List`\[`BaseTrigger`\]
:return: List of trigger objects

- **Return type**

_List_\[ _BaseTrigger_\]


* * *

### start [​](https://clear.ml/docs/latest/docs/references/sdk/trigger/\#start "Direct link to start")

**start()**

Start the Task trigger loop (notice this function does not return)

- **Return type**

`None`


* * *

### start\_remotely [​](https://clear.ml/docs/latest/docs/references/sdk/trigger/\#start_remotely "Direct link to start_remotely")

**start\_remotely(queue='services')**

Start the Task TaskScheduler loop (notice this function does not return)

- **Parameters**

**queue** (`str`) – Remote queue to run the scheduler on, default ‘services’ queue.

- **Return type**

`None`


- [_class_ automation.TriggerScheduler(pooling\_frequency\_minutes=3.0, sync\_frequency\_minutes=15, force\_create\_task\_name=None, force\_create\_task\_project=None)](https://clear.ml/docs/latest/docs/references/sdk/trigger/#class-automationtriggerschedulerpooling_frequency_minutes30-sync_frequency_minutes15-force_create_task_namenone-force_create_task_projectnone)
  - [add\_dataset\_trigger](https://clear.ml/docs/latest/docs/references/sdk/trigger/#add_dataset_trigger)
  - [add\_model\_trigger](https://clear.ml/docs/latest/docs/references/sdk/trigger/#add_model_trigger)
  - [add\_task\_trigger](https://clear.ml/docs/latest/docs/references/sdk/trigger/#add_task_trigger)
  - [get\_triggers](https://clear.ml/docs/latest/docs/references/sdk/trigger/#get_triggers)
  - [start](https://clear.ml/docs/latest/docs/references/sdk/trigger/#start)
  - [start\_remotely](https://clear.ml/docs/latest/docs/references/sdk/trigger/#start_remotely)