---
url: "https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob/"
title: "ClearmlJob | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

## _class_ automation.ClearmlJob(base\_task\_id, parameter\_override=None, task\_overrides=None, configuration\_overrides=None, tags=None, parent=None, disable\_clone\_task=False, allow\_caching=False, target\_project=None, output\_uri=None, enable\_local\_imports=True, \*\*kwargs) [​](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob/\#class-automationclearmljobbase_task_id-parameter_overridenone-task_overridesnone-configuration_overridesnone-tagsnone-parentnone-disable_clone_taskfalse-allow_cachingfalse-target_projectnone-output_urinone-enable_local_importstrue-kwargs "Direct link to class-automationclearmljobbase_task_id-parameter_overridenone-task_overridesnone-configuration_overridesnone-tagsnone-parentnone-disable_clone_taskfalse-allow_cachingfalse-target_projectnone-output_urinone-enable_local_importstrue-kwargs")

Create a new Task based on a base\_task\_id with a different set of parameters

- **Parameters**


  - **base\_task\_id** ( _str_ ) – base task ID to clone from

  - **parameter\_override** ( _dict_ ) – dictionary of parameters and values to set fo the cloned task

  - **task\_overrides** ( _dict_ ) – Task object specific overrides.
    for example `{'script.version_num': None, 'script.branch': 'main'}`

  - **configuration\_overrides** (`Optional`\[`Mapping`\[`str`, `Union`\[`str`, `Mapping`\]\]\]) – Optional, override Task configuration objects.
    Expected dictionary of configuration object name and configuration object content.
    Examples:


> `{'config_section': dict(key='value')}``{'config_file': 'configuration file content'}``{'OmegaConf': YAML.dumps(full_hydra_dict)}`

  - **tags** ( _list_ ) – additional tags to add to the newly cloned task

  - **parent** ( _str_ ) – Set newly created Task parent task field, default: base\_tak\_id.

  - **kwargs** ( _dict_ ) – additional Task creation parameters

  - **disable\_clone\_task** ( _bool_ ) – if False (default), clone base task id.
    If True, use the base\_task\_id directly (base-task must be in draft-mode / created),

  - **allow\_caching** ( _bool_ ) – If True, check if we have a previously executed Task with the same specification.
    If we do, use it and set internal is\_cached flag. Default False (always create new Task).

  - **output\_uri** (`Union`\[`str`, `bool`, `None`\]) – The storage / output url for this job. This is the default location for
    output models and other artifacts. Check Task.init reference docs for more info (output\_uri is a parameter).

  - **target\_project** ( _str_ ) – Optional, Set the target project name to create the cloned Task in.

  - **enable\_local\_imports** (`bool`) – If True, allow jobs to import from local files
    by appending PYTHONPATH sys.path\[0\].
    If False, the current path directory won’t be appended to PYTHONPATH. Default is True.
    Ignored while running remotely.

* * *

### abort [​](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob/\#abort "Direct link to abort")

**abort()**

Abort currently running job (can be called multiple times)

- **Return type**

`None`


* * *

### delete [​](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob/\#delete "Direct link to delete")

**delete()**

Delete the current temporary job (before launching)
Return False if the Job/Task could not deleted

- **Return type**

`bool`


* * *

### elapsed [​](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob/\#elapsed "Direct link to elapsed")

**elapsed()**

Return the time in seconds since job started. Return -1 if job is still pending

- **Return type**

`float`

- **Returns**

Seconds from start.


* * *

### get\_console\_output [​](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob/\#get_console_output "Direct link to get_console_output")

**get\_console\_output(number\_of\_reports=1)**

Return a list of console outputs reported by the Task.
Returned console outputs are retrieved from the most updated console outputs.

- **Parameters**

**number\_of\_reports** ( _int_ ) – number of reports to return, default 1, the last (most updated) console output

- **Return type**

`Sequence`\[`str`\]

- **Returns**

List of strings each entry corresponds to one report.


* * *

### get\_metric [​](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob/\#get_metric "Direct link to get_metric")

**get\_metric(title, series)**

Retrieve a specific scalar metric from the running Task.

- **Parameters**
  - **title** ( _str_ ) – Graph title (metric)

  - **series** ( _str_ ) – Series on the specific graph (variant)
- **Return type**

(<class ‘float’>, <class ‘float’>, <class ‘float’>)

- **Returns**

A tuple of min value, max value, last value


* * *

### is\_aborted [​](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob/\#is_aborted "Direct link to is_aborted")

**is\_aborted()**

Return True, if job was executed and aborted

- **Return type**

`bool`

- **Returns**

True the task is currently in aborted state


* * *

### is\_cached\_task [​](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob/\#is_cached_task "Direct link to is_cached_task")

**is\_cached\_task()**

- **Return type**

`bool`

- **Returns**

True if the internal Task is a cached one, False otherwise.


* * *

### is\_completed [​](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob/\#is_completed "Direct link to is_completed")

**is\_completed()**

Return True, if job was executed and completed successfully

- **Return type**

`bool`

- **Returns**

True the task is currently in completed or published state


* * *

### is\_failed [​](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob/\#is_failed "Direct link to is_failed")

**is\_failed()**

Return True, if job is has executed and failed

- **Return type**

`bool`

- **Returns**

True the task is currently in failed state


* * *

### is\_pending [​](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob/\#is_pending "Direct link to is_pending")

**is\_pending()**

Return True, if job is waiting for execution

- **Return type**

`bool`

- **Returns**

True if the task is currently queued.


* * *

### is\_running [​](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob/\#is_running "Direct link to is_running")

**is\_running()**

Return True, if job is currently running (pending is considered False)

- **Return type**

`bool`

- **Returns**

True, if the task is currently in progress.


* * *

### is\_stopped [​](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob/\#is_stopped "Direct link to is_stopped")

**is\_stopped(aborted\_nonresponsive\_as\_running=False)**

Return True, if job finished executing (for any reason)

- **Parameters**

**aborted\_nonresponsive\_as\_running** (`bool`) – (default: False) If True, ignore the stopped state if the backend
non-responsive watchdog sets this Task to stopped. This scenario could happen if
an instance running the job is killed without warning (e.g. spot instances)

- **Return type**

`bool`

- **Returns**

True the task is currently one of these states, stopped / completed / failed / published.


* * *

### iterations [​](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob/\#iterations "Direct link to iterations")

**iterations()**

Return the last iteration value of the current job. -1 if job has not started yet

- **Return type**

`int`

- **Returns**

Task last iteration.


* * *

### launch [​](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob/\#launch "Direct link to launch")

**launch(queue\_name=None)**

Send Job for execution on the requested execution queue

- **Parameters**

**queue\_name** ( _str_ ) –

- **Return type**

bool


:return False if Task is not in “created” status (i.e. cannot be enqueued) or cannot be enqueued

- **Return type**

`bool`

- **Parameters**

**queue\_name** ( _Optional_ _\[_ _str_ _\]_ ) –


* * *

### ClearmlJob.register\_hashing\_callback [​](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob/\#clearmljobregister_hashing_callback "Direct link to ClearmlJob.register_hashing_callback")

**_classmethod_ register\_hashing\_callback(a\_function)**

Allow to customize the dict used for hashing the Task.
Provided function will be called with a dict representing a Task,
allowing to return a modified version of the representation dict.

- **Parameters**

**a\_function** (`Callable`\[\[`dict`\], `dict`\]) – Function manipulating the representation dict of a function

- **Return type**

`None`


* * *

### started [​](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob/\#started "Direct link to started")

**started()**

Return True, if job already started, or ended. False, if created/pending.

- **Return type**

`bool`

- **Returns**

False, if the task is currently in draft mode or pending.


* * *

### status [​](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob/\#status "Direct link to status")

**status(force=False)**

Return the Job Task current status. Options are: “created”, “queued”, “in\_progress”, “stopped”, “published”,
“publishing”, “closed”, “failed”, “completed”, “unknown”.

- **Parameters**

**force** (`bool`) – Force status update, otherwise, only refresh state every 1 sec

- **Return type**

`str`

- **Returns**

Task status Task.TaskStatusEnum in string.


* * *

### status\_message [​](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob/\#status_message "Direct link to status_message")

**status\_message()**

Gets the status message of the task. Note that the message is updated only after BaseJob.status()
is called

- **Return type**

`str`

- **Returns**

The status message of the corresponding task as a string


* * *

### task\_id [​](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob/\#task_id "Direct link to task_id")

**task\_id()**

Return the Task id.

- **Return type**

`str`

- **Returns**

The Task ID.


* * *

### ClearmlJob.update\_status\_batch [​](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob/\#clearmljobupdate_status_batch "Direct link to ClearmlJob.update_status_batch")

**_classmethod_ update\_status\_batch(jobs)**

Update the status of jobs, in batch\_size

- **Parameters**

**jobs** (`Sequence`\[`BaseJob`\]) – The jobs to update the status of

- **Return type**

`None`


* * *

### wait [​](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob/\#wait "Direct link to wait")

**wait(timeout=None, pool\_period=30.0, aborted\_nonresponsive\_as\_running=False)**

Wait until the task is fully executed (i.e., aborted/completed/failed)

- **Parameters**
  - **timeout** (`Optional`\[`float`\]) – maximum time (minutes) to wait for Task to finish

  - **pool\_period** (`float`) – check task status every pool\_period seconds

  - **aborted\_nonresponsive\_as\_running** (`bool`) – (default: False) If True, ignore the stopped state if the backend
    non-responsive watchdog sets this Task to stopped. This scenario could happen if
    an instance running the job is killed without warning (e.g. spot instances)
- **Return type**

`bool`

- **Returns**

True, if Task finished.


* * *

### worker [​](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob/\#worker "Direct link to worker")

**worker()**

Return the current worker ID executing this Job. If job is pending, returns None

- **Return type**

`Optional`\[`str`\]

- **Returns**

ID of the worker executing / executed the job, or None if job is still pending.


- [_class_ automation.ClearmlJob(base\_task\_id, parameter\_override=None, task\_overrides=None, configuration\_overrides=None, tags=None, parent=None, disable\_clone\_task=False, allow\_caching=False, target\_project=None, output\_uri=None, enable\_local\_imports=True, \*\*kwargs)](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob/#class-automationclearmljobbase_task_id-parameter_overridenone-task_overridesnone-configuration_overridesnone-tagsnone-parentnone-disable_clone_taskfalse-allow_cachingfalse-target_projectnone-output_urinone-enable_local_importstrue-kwargs)
  - [abort](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob/#abort)
  - [delete](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob/#delete)
  - [elapsed](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob/#elapsed)
  - [get\_console\_output](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob/#get_console_output)
  - [get\_metric](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob/#get_metric)
  - [is\_aborted](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob/#is_aborted)
  - [is\_cached\_task](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob/#is_cached_task)
  - [is\_completed](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob/#is_completed)
  - [is\_failed](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob/#is_failed)
  - [is\_pending](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob/#is_pending)
  - [is\_running](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob/#is_running)
  - [is\_stopped](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob/#is_stopped)
  - [iterations](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob/#iterations)
  - [launch](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob/#launch)
  - [ClearmlJob.register\_hashing\_callback](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob/#clearmljobregister_hashing_callback)
  - [started](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob/#started)
  - [status](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob/#status)
  - [status\_message](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob/#status_message)
  - [task\_id](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob/#task_id)
  - [ClearmlJob.update\_status\_batch](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob/#clearmljobupdate_status_batch)
  - [wait](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob/#wait)
  - [worker](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob/#worker)