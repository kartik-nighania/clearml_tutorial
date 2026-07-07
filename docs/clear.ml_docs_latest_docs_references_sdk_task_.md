---
url: "https://clear.ml/docs/latest/docs/references/sdk/task/"
title: "Task | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/sdk/task/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

## _class_ Task(private=None, \*\*kwargs) [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#class-taskprivatenone-kwargs "Direct link to class-taskprivatenone-kwargs")

The `Task` class is a code template for a Task object which, together with its connected experiment components,
represents the current running experiment. These connected components include hyperparameters, loggers,
configuration, label enumeration, models, and other artifacts.

The term “main execution Task” refers to the Task context for the current running experiment. Python experiment scripts
can create one, and only one, main execution Task. It is traceable, and after a script runs and ClearML stores
the Task in the **ClearML Server** (backend), it is modifiable, reproducible, executable by a worker, and you
can duplicate it for further experimentation.

The `Task` class and its methods allow you to create and manage experiments, as well as perform
advanced experimentation functions, such as autoML.

warning

Do not construct Task objects directly. Use one of the methods listed below to create experiments or
reference existing experiments.
Do not define `CLEARML_TASK_*` and `CLEARML_PROC_*` environment variables. They are used internally
for bookkeeping between processes and agents.

For detailed information about creating Task objects, see the following methods:

- Create a new reproducible Task - `Task.init`

important

In some cases, `Task.init` may return a Task object which is already stored in ClearML Server (already
initialized), instead of creating a new Task. For a detailed explanation of those cases, see the `Task.init`
method.

- Manually create a new Task (no auto-logging will apply) - `Task.create`

- Get the current running Task - `Task.current_task`

- Get a different Task - `Task.get_task`


info

The ClearML documentation often refers to a Task as “Task (experiment)”.

“Task” refers to the class in the ClearML Python Client Package, the object in your Python experiment script,
and the entity with which ClearML Server and ClearML Agent work.

“Experiment” refers to your deep learning solution, including its connected components, inputs, and outputs,
and is the experiment you can view, analyze, compare, modify, duplicate, and manage using the ClearML
Web-App (UI).

Therefore, a “Task” is effectively an “experiment”, and “Task (experiment)” encompasses its usage throughout
the ClearML.

The exception to this Task behavior is sub-tasks (non-reproducible Tasks), which do not use the main execution
Task. Creating a sub-task always creates a new Task with a new Task ID.

warning

Do not construct Task objects manually!
Please use `Task.init` or `Task.get_task`

* * *

### Task.add\_requirements [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#taskadd_requirements "Direct link to Task.add_requirements")

**_classmethod_ add\_requirements(package\_name, package\_version=None)**

Force the adding of a package to the requirements list. If `package_version` is `None`, use the
installed package version, if found.

Example: `Task.add_requirements('tensorflow', '2.4.0')`

Example: Task.add\_requirements(‘tensorflow’, ‘>=2.4’)

Example: `Task.add_requirements('tensorflow')` -\> use the installed tensorflow version

Example: `Task.add_requirements('tensorflow', '')` -\> no version limit

Alternatively, you can add all requirements from a file:

Example: `Task.add_requirements('/path/to/your/project/requirements.txt')`

info

`Task.add_requirements` does not directly modify the task’s requirements. Instead, it improves the accuracy
of capturing a task’s Python packages. To explicitly change task requirements, use
`Task.set_packages`, which overwrites existing packages with the specified ones.

- **Parameters**
  - **package\_name** ( _str_ ) – The package name or path to a requirements file
    to add to the “Installed Packages” section of the task.

  - **package\_version** (`Optional`\[`str`\]) – The package version requirements. If `None`, then use the installed version.
- **Return type**

`None`


* * *

### add\_tags [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#add_tags "Direct link to add_tags")

**add\_tags(tags)**

Add Tags to this task. Old tags are not deleted. When executing a Task (experiment) remotely,
this method has no effect.

- **Parameters**

**tags** (`Union`\[`Sequence`\[`str`\], `str`\]) – A list of tags which describe the Task to add.

- **Return type**

`None`


* * *

### artifacts [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#artifacts "Direct link to artifacts")

**property artifacts: Dict\[str, Artifact\]**

A read-only dictionary of Task artifacts (name, artifact).

- **Return type**

`Dict`\[`str`, `Artifact`\]

- **Returns**

The artifacts.


* * *

### cache\_dir [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#cache_dir "Direct link to cache_dir")

**property cache\_dir: Path**

The cache directory which is used to store the Task related files.

- **Return type**

`Path`


* * *

### Task.clone [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#taskclone "Direct link to Task.clone")

**_classmethod_ clone(source\_task=None, name=None, comment=None, parent=None, project=None)**

Create a duplicate (a clone) of a Task (experiment). The status of the cloned Task is `Draft`
and modifiable.

Use this method to manage experiments and for autoML.

- **Parameters**
  - **source\_task** ( _str_ ) – The Task to clone. Specify a Task object or a Task ID. (Optional)

  - **name** ( _str_ ) – The name of the new cloned Task. (Optional)

  - **comment** ( _str_ ) – A comment / description for the new cloned Task. (Optional)

  - **parent** ( _str_ ) – The ID of the parent Task of the new Task.
    - If `parent` is not specified, then `parent` is set to `source_task.parent`.

    - If `parent` is not specified and `source_task.parent` is not available, then `parent` set to `source_task`.
  - **project** ( _str_ ) – The ID of the project in which to create the new Task.
    If `None`, the new task inherits the original Task’s project. (Optional)
- **Returns**

The new cloned Task (experiment).

- **Return type**

Task


* * *

### close [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#close "Direct link to close")

**close()**

Closes the current Task and changes its status to “Completed”.
Enables you to manually shut down the task from the process which opened the task.

This method does not terminate the (current) Python process, in contrast to `Task.mark_completed`.

After calling `Task.close` on a task, the respective object cannot be used anymore and
methods like `Task.connect` or `Task.connect_configuration` will throw a `ValueError`.
In order to obtain an object representing the task again, use methods like `Task.get_task`.

warning

Only call `Task.close` if you are certain the Task is not needed.

- **Return type**

`None`


* * *

### comment [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#comment "Direct link to comment")

**property comment: str**

Returns the current Task’s (user defined) comments.

- **Return type**

`str`


* * *

### completed [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#completed "Direct link to completed")

**completed(ignore\_errors=True)**

info

Deprecated, use `Task.mark_completed()` instead

- **Return type**

`Optional`\[`CallResult`\]

- **Parameters**

**ignore\_errors** ( _bool_ ) –


* * *

### connect [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#connect "Direct link to connect")

**connect(mutable, name=None, ignore\_remote\_overrides=False)**

Connects an experiment component to a Task. An experiment component can be an object containing
some hyperparameters, or a [`Model`](https://clear.ml/docs/latest/docs/references/sdk/model_model#clearml.Model).
When running remotely, the value of the connected object is overridden by the corresponding value found
under the experiment’s UI/backend (unless `ignore_remote_overrides` is `True`).

- **Parameters**
  - **mutable** ( _object_ ) – The experiment component to connect. The object must be one of the following types:
    - argparse - An argparse object for parameters.

    - dict - A dictionary for parameters. Note: only keys of type `str` are supported.

    - `TaskParameters` \- A `TaskParameters` object.

    - `Model` \- A model object for initial model warmup, or for model update/snapshot uploading. In practice the model should be either [`InputModel`](https://clear.ml/docs/latest/docs/references/sdk/model_inputmodel#clearml.InputModel) or [`OutputModel`](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel#clearml.OutputModel).

    - type - A Class type, storing all class properties (excluding ‘\_’ prefixed properties).

    - object - A class instance, storing all instance properties (excluding ‘\_’ prefixed properties).
  - **name** ( _str_ ) – A section name for the connected object (defaults to ‘General’).
    Currently, `name` is only supported for `dict` and `TaskParameter` objects, and should be omitted for the other supported types. (Optional)
    For example, by setting `name='General'` the connected dictionary will be under the General section in the hyperparameters section.

  - **ignore\_remote\_overrides** (`bool`) – If `True`, ignore UI/backend overrides when running remotely.
    Default is `False`, meaning that any changes made in the UI/backend will be applied in remote execution.
- **Return type**

`Any`

- **Returns**

Returns the same object passed as `mutable`, unless the object is a dict.
For dicts `Task.connect` will return the dict decorated as a `ProxyDictPostWrite`.
This is done to allow propagating the updates from the connected object.

- **Raise**

Raises an exception if passed an unsupported object.


* * *

### connect\_configuration [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#connect_configuration "Direct link to connect_configuration")

**connect\_configuration(configuration, name=None, description=None, ignore\_remote\_overrides=False)**

Connect a configuration dictionary or configuration file (`pathlib.Path` / str) to a Task object.
This method should be called before reading the configuration file.

For example, a local file:

```py
config_file = task.connect_configuration(config_file)

my_params = json.load(open(config_file,'rt'))
```

A parameter dictionary/list:

```py
my_params = task.connect_configuration(my_params)
```

When running remotely, the value of the connected configuration is overridden by the corresponding value found
under the experiment’s UI/backend (unless `ignore_remote_overrides` is `True`).

- **Parameters**
  - **configuration** (`Union`\[`Mapping`, `list`, `Path`, `str`\]) – The configuration. This is usually the configuration used in the model training process.

    Specify one of the following:
    - A dictionary/list - A dictionary containing the configuration. ClearML stores the configuration in
      the **ClearML Server** (backend), in a HOCON format (JSON-like format) which is editable.

    - A `pathlib2.Path` string - A path to the configuration file. ClearML stores the content of the file.
      A local path must be relative path. When executing a Task remotely in a worker, the contents brought
      from the **ClearML Server** (backend) overwrites the contents of the file.
  - **name** ( _str_ ) – Configuration section name. default: ‘General’.
    Allows users to store multiple configuration dicts/files

  - **description** ( _str_ ) – Configuration section description (text). Default: `None`

  - **ignore\_remote\_overrides** ( _bool_ ) – If `True`, ignore UI/backend overrides when running remotely.
    Default is `False`, meaning that any changes made in the UI/backend will be applied in remote execution.
- **Return type**

`Union`\[`dict`, `Path`, `str`\]

- **Returns**

If a dictionary is specified, then a dictionary is returned. If `pathlib2.Path` / `str` is
specified, then a path to a local configuration file is returned. Configuration object.


* * *

### connect\_label\_enumeration [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#connect_label_enumeration "Direct link to connect_label_enumeration")

**connect\_label\_enumeration(enumeration, ignore\_remote\_overrides=False)**

Connect a label enumeration dictionary to a Task (experiment) object.

Later, when creating an output model, the model will include the label enumeration dictionary.

- **Parameters**


  - **enumeration** ( _dict_ ) – A label enumeration dictionary of string (label) to integer (value) pairs.

For example:

```javascript
{

     "background": 0,

     "person": 1

}
```

  - **ignore\_remote\_overrides** (`bool`) – If `True`, ignore UI/backend overrides when running remotely.
    Default is `False`, meaning that any changes made in the UI/backend will be applied in remote execution.
- **Return type**

`Dict`\[`str`, `int`\]

- **Returns**

The label enumeration dictionary (JSON).


* * *

### Task.create [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#taskcreate "Direct link to Task.create")

**_classmethod_ create(project\_name=None, task\_name=None, task\_type=None, repo=None, branch=None, commit=None, script=None, working\_directory=None, packages=None, requirements\_file=None, docker=None, docker\_args=None, docker\_bash\_setup\_script=None, argparse\_args=None, base\_task\_id=None, add\_task\_init\_call=True, force\_single\_script\_file=False, binary=None, module=None, detect\_repository=True)**

Manually create and populate a new Task (experiment) in the system.
If the code does not already contain a call to `Task.init`, pass `add_task_init_call=True`,
and the code will be patched in remote execution (i.e. when executed by `clearml-agent`).

info

This method always creates a new Task.
Use `Task.init` method to automatically create and populate a task for the running process.
To reference an existing Task, call the `Task.get_task` method.

- **Parameters**
  - **project\_name** (`Optional`\[`str`\]) – Set the project name for the task. Required if base\_task\_id is `None`.

  - **task\_name** (`Optional`\[`str`\]) – Set the name of the remote task. Required if base\_task\_id is `None`.

  - **task\_type** (`Optional`\[`str`\]) – Optional, The task type to be created. Supported values: ‘training’, ‘testing’, ‘inference’,
    ‘data\_processing’, ‘application’, ‘monitor’, ‘controller’, ‘optimizer’, ‘service’, ‘qc’, ‘custom’

  - **repo** (`Optional`\[`str`\]) – Remote URL for the repository to use, or path to local copy of the git repository.
    Example: ‘ [https://github.com/allegroai/clearml.git](https://github.com/allegroai/clearml.git)’ or ‘~/project/repo’. If `repo` is specified, then
    the `script` parameter must also be specified

  - **branch** (`Optional`\[`str`\]) – Select specific repository branch/tag (implies the latest commit from the branch)

  - **commit** (`Optional`\[`str`\]) – Select specific commit ID to use (default: latest commit,
    or when used with local repository matching the local commit ID)

  - **script** (`Optional`\[`str`\]) – Specify the entry point script for the remote execution. When used in tandem with
    remote git repository the script should be a relative path inside the repository,
    for example: ‘./source/train.py’ . When used with local repository path it supports a
    direct path to a file inside the local repository itself, for example: ‘~/project/source/train.py’

  - **working\_directory** (`Optional`\[`str`\]) – Working directory to launch the script from. Default: repository root folder.
    Relative to repo root or local folder.

  - **packages** (`Union`\[`bool`, `Sequence`\[`str`\], `None`\]) – Manually specify a list of required packages. Example: `["tqdm&gt;=2.1", "scikit-learn"]`
    or `True` to automatically create requirements
    based on locally installed packages (repository must be local).
    Pass an empty string to not install any packages (not even from the repository)

  - **requirements\_file** (`Union`\[`str`, `Path`, `None`\]) – Specify requirements.txt file to install when setting the session.
    If not provided, the requirements.txt from the repository will be used.

  - **docker** (`Optional`\[`str`\]) – Select the docker image to be executed in by the remote session

  - **docker\_args** (`Optional`\[`str`\]) – Add docker arguments, pass a single string

  - **docker\_bash\_setup\_script** (`Optional`\[`str`\]) – Add bash script to be executed
    inside the docker before setting up the Task’s environment

  - **argparse\_args** (`Optional`\[`Sequence`\[`Tuple`\[`str`, `str`\]\]\]) – Arguments to pass to the remote execution, list of string pairs (argument, value)
    Notice, only supported if the codebase itself uses `argparse.ArgumentParser`

  - **base\_task\_id** (`Optional`\[`str`\]) – Use a pre-existing task in the system, instead of a local repo/script.
    Essentially clones an existing task and overrides arguments/requirements.

  - **add\_task\_init\_call** (`bool`) – If `True`, a `Task.init()` call is added to the script entry point in remote execution.

  - **force\_single\_script\_file** (`bool`) – If `True`, do not auto-detect local repository

  - **binary** (`Optional`\[`str`\]) – Binary used to launch the entry point

  - **module** (`Optional`\[`str`\]) – If specified instead of executing `script`, a module named `module` is executed.
    Implies script is empty. Module can contain multiple argument for execution,
    for example: `module="my.module arg1 arg2"`

  - **detect\_repository** (`bool`) – If `True`, detect the repository if no repository has been specified.
    If `False`, don’t detect repository under any circumstance. Ignored if `repo` is specified
- **Returns**

The newly created Task (experiment)

- **Return type**

Task


* * *

### create\_function\_task [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#create_function_task "Direct link to create_function_task")

**create\_function\_task(func, func\_name=None, task\_name=None, \*\*kwargs)**

Create a new task, and call `func` with the specified kwargs.
One can think of this call as remote forking, where the newly created instance is the new Task
calling the specified func with the appropriate kwargs and leaving once the func terminates.
Notice that a remote executed function cannot create another child remote executed function.

info

Must be called from the main Task, i.e. the one created by `Task.init()`.

The remote Tasks inherits the environment from the creating Task.

In the remote Task, the entrypoint is the same as the creating Task.

In the remote Task, the execution is the same until reaching this function call.

- **Parameters**
  - **func** (`Callable`) – A function to execute remotely as a single Task.
    On the remote executed Task the entry-point and the environment are copied from this
    calling process, only this function call redirect the execution flow to the called func,
    alongside the passed arguments

  - **func\_name** (`Optional`\[`str`\]) – A unique identifier of the function. Default the function name without the namespace.
    For example Class.foo() becomes ‘foo’

  - **task\_name** (`Optional`\[`str`\]) – The newly created Task name. Default: the calling Task name + function name

  - **kwargs** (`Optional`\[`Any`\]) – Name specific arguments for the target function.
    These arguments will appear under the configuration, “Function” section
- **Return Task**

Return the newly created Task or `None` if running remotely and execution is skipped

- **Return type**

`Optional`\[`Task`\]


* * *

### Task.current\_task [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#taskcurrent_task "Direct link to Task.current_task")

**_classmethod_ current\_task()**

Get the current running Task (experiment). This is the main execution Task (task context) returned as a Task
object.

- **Returns**

The current running Task (experiment).

- **Return type**

Task


* * *

### data [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#data "Direct link to data")

**property data: Any**

A decorator indicating abstract properties.

Deprecated, use ‘property’ with ‘abstractmethod’ instead.

- **Return type**

`Any`


* * *

### Task.debug\_simulate\_remote\_task [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#taskdebug_simulate_remote_task "Direct link to Task.debug_simulate_remote_task")

**_classmethod_ debug\_simulate\_remote\_task(task\_id, reset\_task=False)**

Simulate remote execution of a specified Task as if executed by a ClearML Agent.
This means configurations will be pulled from the backend server into the code
(the opposite from manual execution, where the backend logs the code arguments).
Use with care.

- **Parameters**
  - **task\_id** (`str`) – Task ID to simulate, notice that all configuration will be taken from the specified
    Task, regardless of the code initial values, just like it as if executed by ClearML agent

  - **reset\_task** (`bool`) – If `True`, target Task, is automatically cleared / reset.
- **Return type**

`None`


* * *

### delete [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#delete "Direct link to delete")

**delete(delete\_artifacts\_and\_models=True, skip\_models\_used\_by\_other\_tasks=True, raise\_on\_error=False, callback=None)**

Delete the task as well as its output models and artifacts.
Models and artifacts are deleted from their storage locations, each using its URI.

Note: in order to delete models and artifacts using their URI, make sure the proper storage credentials are
configured in your configuration file (e.g. if an artifact is stored in S3, make sure `sdk.aws.s3.credentials`
are properly configured and that you have delete permission in the related buckets).

- **Parameters**
  - **delete\_artifacts\_and\_models** (`bool`) – If `True` (default), artifacts and models would also be deleted.
    If callback is provided, this argument is ignored.

  - **skip\_models\_used\_by\_other\_tasks** (`bool`) – If `True` (default), models used by other tasks would not be deleted

  - **raise\_on\_error** (`bool`) – If `True`, an exception will be raised when encountering an error.
    If `False` an error would be printed and no exception will be raised.

  - **callback** (`Optional`\[`Callable`\[\[`str`, `str`\], `bool`\]\]) – An optional callback accepting a URI type (`str`) and a URI (`str`) that will be called
    for each artifact and model. If provided, the `delete_artifacts_and_models` is ignored.
    Return `True` to indicate the artifact/model should be deleted.
- **Return type**

`bool`

- **Returns**

`True` if the task was deleted successfully.


* * *

### delete\_artifacts [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#delete_artifacts "Direct link to delete_artifacts")

**delete\_artifacts(artifact\_names, raise\_on\_errors=True, delete\_from\_storage=True, silent\_on\_errors=False)**

Delete a list of artifacts, by artifact name, from the Task.

- **Parameters**
  - **artifact\_names** ( _list_ ) – List of artifact names

  - **raise\_on\_errors** ( _bool_ ) – If `True`, do not suppress connectivity related exceptions

  - **delete\_from\_storage** ( _bool_ ) – If `True`, try to delete the actual
    file from the external storage (e.g. S3, GS, Azure, File Server etc.)

  - **silent\_on\_errors** (`bool`) – If `True`, do not log connectivity related errors
- **Return type**

`bool`

- **Returns**

`True` if successful


* * *

### delete\_parameter [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#delete_parameter "Direct link to delete_parameter")

**delete\_parameter(name, force=False)**

Delete a parameter by its full name Section/name.

- **Parameters**
  - **name** (`str`) – Parameter name in full, i.e. Section/name. For example, ‘Args/batch\_size’

  - **force** (`bool`) – If set to `True` then both new and running task hyperparams can be deleted.
    Otherwise, only the new task ones. Default is `False`
- **Return type**

`bool`

- **Returns**

`True` if the parameter was deleted successfully


* * *

### delete\_user\_properties [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#delete_user_properties "Direct link to delete_user_properties")

**delete\_user\_properties(\*iterables)**

Delete hyperparameters for this task.

- **Parameters**

**iterables** (`Iterable`\[`Union`\[`dict`, `Iterable`\[`str`\]\]\]) – One or more iterables, each identifying a hyperparameter to delete. Each entry can be either:
  - A dictionary with ‘section’ and ‘name’ keys

  - An iterable (e.g. tuple, list etc.) whose first two items denote ‘section’ and ‘name’
- **Return type**

`bool`


* * *

### Task.dequeue [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#taskdequeue "Direct link to Task.dequeue")

**_classmethod_ dequeue(task)**

Dequeue (remove) a Task from an execution queue.

- **Parameters**

**task** ( _Task/str_ ) – The Task to dequeue. Specify a Task object or Task ID.

- **Return type**

`Any`

- **Returns**

A dequeue JSON response.


```javascript
{

     "dequeued": 1,

     "updated": 1,

     "fields": {

         "status": "created",

         "status_reason": "",

         "status_message": "",

         "status_changed": "2020-02-24T16:43:43.057320+00:00",

         "last_update": "2020-02-24T16:43:43.057320+00:00",

         "execution.queue": null

         }

 }
```

- `dequeued` \- The number of Tasks enqueued (an integer or `null`).

- `fields`
  - `status` \- The status of the experiment.

  - `status_reason` \- The reason for the last status change.

  - `status_message` \- Information about the status.

  - `status_changed` \- The last status change date and time in ISO 8601 format.

  - `last_update` \- The last time the Task was created, updated, changed, or events for this task were reported.

  - `execution.queue` \- The ID of the queue where the Task is enqueued. `null` indicates not enqueued.
- `updated` \- The number of Tasks updated (an integer or `null`).


* * *

### Task.enqueue [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#taskenqueue "Direct link to Task.enqueue")

**_classmethod_ enqueue(task, queue\_name=None, queue\_id=None, force=False)**

Enqueue a Task for execution, by adding it to an execution queue.

info

A worker daemon must be listening at the queue for the worker to fetch the Task and execute it,
see “ClearML Agent” in the ClearML Documentation.

- **Parameters**
  - **task** ( _Task/str_ ) – The Task to enqueue. Specify a Task object or Task ID.

  - **queue\_name** ( _str_ ) – The name of the queue. If not specified, then `queue_id` must be specified.

  - **queue\_id** ( _str_ ) – The ID of the queue. If not specified, then `queue_name` must be specified.

  - **force** ( _bool_ ) – If `True`, reset the Task if necessary before enqueuing it
- **Return type**

`Any`

- **Returns**

An enqueue JSON response.





```javascript
{

       "queued": 1,

       "updated": 1,

       "fields": {

           "status": "queued",

           "status_reason": "",

           "status_message": "",

           "status_changed": "2020-02-24T15:05:35.426770+00:00",

           "last_update": "2020-02-24T15:05:35.426770+00:00",

           "execution.queue": "2bd96ab2d9e54b578cc2fb195e52c7cf"

           }

}
```








  - `queued` \- The number of Tasks enqueued (an integer or `null`).

  - `updated` \- The number of Tasks updated (an integer or `null`).

  - `fields`
    - `status` \- The status of the experiment.

    - `status_reason` \- The reason for the last status change.

    - `status_message` \- Information about the status.

    - `status_changed` \- The last status change date and time (ISO 8601 format).

    - `last_update` \- The last Task update time, including Task creation, update, change, or events for this task (ISO 8601 format).

    - `execution.queue` \- The ID of the queue where the Task is enqueued. `null` indicates not enqueued.

* * *

### execute\_remotely [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#execute_remotely "Direct link to execute_remotely")

**execute\_remotely(queue\_name=None, clone=False, exit\_process=True)**

If task is running locally (i.e., not by `clearml-agent`), then clone the Task and enqueue it for remote
execution; or, stop the execution of the current Task, reset its state, and enqueue it. If `exit_process==True`,
_exit_ this process.

info

If the task is running remotely (i.e., `clearml-agent` is executing it), this call is a no-op
(i.e., does nothing).

- **Parameters**
  - **queue\_name** (`Optional`\[`str`\]) – The queue name used for enqueueing the task. If `None`, this call exits the process
    without enqueuing the task.

  - **clone** (`bool`) – Clone the Task and execute the newly cloned Task

    The values are:
    - `True` \- A cloned copy of the Task will be created, and enqueued, instead of this Task.

    - `False` \- The Task will be enqueued.
  - **exit\_process** (`bool`) – The function call will leave the calling process at the end.
    - `True` \- Exit the process (exit(0)). Note: if `clone==False`, then `exit_process` must be `True`.

    - `False` \- Do not exit the process.
- **Return Task**

return the task object of the newly generated remotely executing task

- **Return type**

`Optional`\[`Task`\]


* * *

### export\_task [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#export_task "Direct link to export_task")

**export\_task()**

Export Task’s configuration into a dictionary (for serialization purposes).
A Task can be copied/modified by calling `Task.import_task()`.
Notice: Export task does not include the tasks outputs, such as results
(scalar/plots etc.) or Task artifacts/models

- **Return type**

`dict`

- **Returns**

dictionary of the Task’s configuration.


* * *

### flush [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#flush "Direct link to flush")

**flush(wait\_for\_uploads=False)**

Flush any outstanding reports or console logs.

- **Parameters**

**wait\_for\_uploads** ( _bool_ ) – Wait for all outstanding uploads to complete
  - `True` \- Wait

  - `False` \- Do not wait (default)
- **Return type**

`bool`


* * *

### Task.force\_requirements\_env\_freeze [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#taskforce_requirements_env_freeze "Direct link to Task.force_requirements_env_freeze")

**_classmethod_ force\_requirements\_env\_freeze(force=True, requirements\_file=None)**

Force the use of `pip freeze` or `conda list` to capture the requirements from the active
environment (instead of statically analyzing the running code and listing directly imported packages).
Notice: Must be called before `Task.init` !

- **Parameters**
  - **force** (`bool`) – If `True` (default), force the use of `pip freeze` or `conda list` to capture the
    requirements. If `False`, ClearML statistically analyzes the code for requirements.

  - **requirements\_file** (`Union`\[`str`, `Path`, `None`\]) – (Optional) Pass a requirements.txt file to specify the required packages (instead of
    `pip freeze` or automatic analysis). This will overwrite any existing requirement listing.
- **Return type**

`None`


* * *

### Task.force\_store\_standalone\_script [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#taskforce_store_standalone_script "Direct link to Task.force_store_standalone_script")

**_classmethod_ force\_store\_standalone\_script(force=True)**

Force using storing the main python file as a single standalone script, instead of linking with the
local git repository/commit ID.

Notice: Must be called before `Task.init` !

- **Parameters**

**force** (`bool`) – Set force storing the main python file as a single standalone script

- **Return type**

`None`


* * *

### Task.get\_all [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#taskget_all "Direct link to Task.get_all")

**_classmethod_ get\_all(session=None, log=None, \*\*kwargs)**

List all the Tasks based on specific projection.

- **Parameters**


  - **session** ( _Session_ ) – The session object used for sending requests to the API.

  - **log** ( _logging.Logger_ ) – The Log object.

  - **kwargs** ( _dict_ ) – Keyword args passed to the `GetAllRequest`
    (see `backend_api.service.v?.tasks.GetAllRequest` for details; the `?` needs to be replaced by the appropriate version.)


For example:

```bash
status='completed', 'search_text'='specific_word', 'user'='user_id', 'project'='project_id'
```

- **Return type**

`Any`

- **Returns**

The API response.


* * *

### get\_all\_reported\_scalars [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#get_all_reported_scalars "Direct link to get_all_reported_scalars")

**get\_all\_reported\_scalars(x\_axis='iter')**

Return a nested dictionary for the all scalar graphs, containing all the registered samples,
where the first key is the graph title and the second is the series name.
Value is a dict with ‘x’: values and ‘y’: values.
To fetch downsampled scalar values, please see the `Task.get_reported_scalars`.

info

This call is not cached, any call will retrieve all the scalar reports from the backend.
If the Task has many scalars reported, it might take long for the call to return.

- **Parameters**

**x\_axis** ( _str_ ) – scalar x\_axis, possible values:
‘iter’: iteration (default), ‘timestamp’: timestamp as milliseconds since epoch, ‘iso\_time’: absolute time

- **Return type**

`Mapping`\[`str`, `Mapping`\[`str`, `Mapping`\[`str`, `Sequence`\[`float`\]\]\]\]

- **Returns**

dict: Nested scalar graphs: `dict[title(str), dict[series(str), dict[axis(str), list(float)]]]`


* * *

### get\_archived [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#get_archived "Direct link to get_archived")

**get\_archived()**

Return the Archive state of the Task

- **Return type**

`bool`

- **Returns**

If `True`, the Task is archived, otherwise it is not.


* * *

### get\_base\_docker [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#get_base_docker "Direct link to get_base_docker")

**get\_base\_docker()**

Get the base Docker command (image) that is set for this experiment.

- **Return type**

`str`


* * *

### Task.get\_by\_name [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#taskget_by_name "Direct link to Task.get_by_name")

**_classmethod_ get\_by\_name(task\_name)**

info

This method is deprecated, use `Task.get_task` instead.

Returns the most recent task with the given name from anywhere in the system as a Task object.

- **Parameters**

**task\_name** ( _str_ ) – The name of the task to search for.

- **Return type**

~TaskInstance

- **Returns**

Task object of the most recent task with that name.


* * *

### get\_configuration\_object [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#get_configuration_object "Direct link to get_configuration_object")

**get\_configuration\_object(name)**

Get the Task’s configuration object section as a blob of text.
Use only for automation (externally), otherwise use `Task.connect_configuration`.

- **Parameters**

**name** ( _str_ ) – Configuration section name

- **Return type**

`Optional`\[`str`\]

- **Returns**

The Task’s configuration as a text blob (unconstrained text string).
Return `None` if configuration name is not valid


* * *

### get\_configuration\_object\_as\_dict [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#get_configuration_object_as_dict "Direct link to get_configuration_object_as_dict")

**get\_configuration\_object\_as\_dict(name)**

Get the Task’s configuration object section as parsed dictionary.
Parsing supports JSON and HOCON, otherwise parse manually with `get_configuration_object()`.
Use only for automation (externally), otherwise use `Task.connect_configuration`.

- **Parameters**

**name** ( _str_ ) – Configuration section name

- **Return type**

`Union`\[`dict`, `list`, `None`\]

- **Returns**

The Task’s configuration as a parsed dict.
Return `None` if configuration name is not valid


* * *

### get\_configuration\_objects [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#get_configuration_objects "Direct link to get_configuration_objects")

**get\_configuration\_objects()**

Get the Task’s configuration object section as a blob of text.
Use only for automation (externally), otherwise use `Task.connect_configuration`.

- **Return type**

`Optional`\[`Mapping`\[`str`, `str`\]\]

- **Returns**

The Task’s configurations as a dict (config name as key) and text blob as value (unconstrained text
string)


* * *

### get\_dataviews [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#get_dataviews "Direct link to get_dataviews")

**get\_dataviews()**

Return a dictionary of HyperDatasets DataView objects reconstructed from this Task
task properties (primarily from input.\*). Keys are arbitrary labels.

- **Return type**

`Dict`\[`str`, `Any`\]


* * *

### get\_debug\_samples [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#get_debug_samples "Direct link to get_debug_samples")

**get\_debug\_samples(title, series, n\_last\_iterations=None)**

- **Parameters**
  - **title** ( _str_ ) – Debug sample’s title, also called metric in the UI

  - **series** ( _str_ ) – Debug sample’s series,
    corresponding to debug sample’s file name in the UI, also known as variant

  - **n\_last\_iterations** ( _int_ ) – How many debug sample iterations to fetch in reverse chronological order.
    Leave empty to get all debug samples.
- **Raise**

TypeError if `n_last_iterations` is explicitly set to anything other than a positive integer value

- **Return type**

`List`\[`dict`\]

- **Returns**

A list of dicts, each containing the debug sample’s URL and other metadata.
The URLs can be passed to `StorageManager.get_local_copy` to fetch local copies of debug samples.


* * *

### get\_executed\_queue [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#get_executed_queue "Direct link to get_executed_queue")

**get\_executed\_queue(return\_name=False)**

Get the queue the task was executed on.

- **Parameters**

**return\_name** (`bool`) – If `True`, return the name of the queue. Otherwise, return its ID

- **Return type**

`Optional`\[`str`\]

- **Returns**

Return the ID or name of the queue the task was executed on.
If no queue was found, return `None`


* * *

### get\_http\_router [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#get_http_router "Direct link to get_http_router")

**get\_http\_router()**

Retrieve an instance of `HttpRouter` to manage an external HTTP endpoint and intercept traffic.
The `HttpRouter` serves as a traffic manager, enabling the creation and configuration of local and external
routes to redirect, monitor, or manipulate HTTP requests and responses. It is designed to handle routing
needs via a proxy setup which handles request/response interception and telemetry reporting for
applications that require HTTP endpoint management.

Example usage:

```py
def request_callback(request, persistent_state):

    persistent_state["last_request_time"] = time.time()

def response_callback(response, request, persistent_state):

    print("Latency:", time.time() - persistent_state["last_request_time"])

    if urllib.parse.urlparse(str(request.url).rstrip("/")).path == "/modify":

        new_content = response.body.replace(b"modify", b"modified")

        headers = copy.deepcopy(response.headers)

        headers["Content-Length"] = str(len(new_content))

        return Response(status_code=response.status_code, headers=headers, content=new_content)

router = Task.current_task().get_http_router()

router.set_local_proxy_parameters(incoming_port=9000)

router.create_local_route(

    source="/",

    target="http://localhost:8000",

    request_callback=request_callback,

    response_callback=response_callback,

    endpoint_telemetry={"model": "MyModel"}

)

router.deploy(wait=True)
```

- **Return type**

[HttpRouter](https://clear.ml/docs/latest/docs/references/sdk/http_router#clearml.router.router.HttpRouter)


* * *

### get\_initial\_iteration [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#get_initial_iteration "Direct link to get_initial_iteration")

**get\_initial\_iteration()**

Return the initial iteration offset, default is 0.
Useful when continuing training from previous checkpoints.

- **Return type**

`int`

- **Returns**

Initial iteration offset.


* * *

### get\_label\_num\_description [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#get_label_num_description "Direct link to get_label_num_description")

**get\_label\_num\_description()**

Get a dictionary of label number to string pairs representing all labels associated with this number
on the model labels.

- **Return type**

`Dict`\[`int`, `str`\]


* * *

### get\_labels\_enumeration [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#get_labels_enumeration "Direct link to get_labels_enumeration")

**get\_labels\_enumeration()**

Get the label enumeration dictionary label enumeration dictionary of string (label) to integer (value) pairs.

- **Return type**

`Mapping`\[`str`, `int`\]

- **Returns**

A dictionary containing the label enumeration.


* * *

### get\_last\_iteration [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#get_last_iteration "Direct link to get_last_iteration")

**get\_last\_iteration()**

Returns the last iteration for which the Task reported a metric.

info

The maximum reported iteration is not in the local cache. This method
sends a request to the ClearML Server (backend).

- **Return type**

`int`

- **Returns**

The last reported iteration number.


* * *

### get\_last\_scalar\_metrics [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#get_last_scalar_metrics "Direct link to get_last_scalar_metrics")

**get\_last\_scalar\_metrics()**

Get the last scalar metrics which the Task reported. This is a nested dictionary, ordered by title and series.

For example:

```javascript
{

 "title": {

     "series": {

         "last": 0.5,

         "min": 0.1,

         "max": 0.9

         }

     }

 }
```

- **Return type**

`Dict`\[`str`, `Dict`\[`str`, `Dict`\[`str`, `float`\]\]\]

- **Returns**

The last scalar metrics.


* * *

### get\_logger [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#get_logger "Direct link to get_logger")

**get\_logger()**

Get a Logger object for reporting, for this task context. You can view all Logger report output associated with
the Task for which this method is called, including metrics, plots, text, tables, and images, in the
**ClearML Web-App (UI)**.

- **Return type**

[`Logger`](https://clear.ml/docs/latest/docs/references/sdk/logger#clearml.Logger)

- **Returns**

The Logger for the Task (experiment).


* * *

### get\_model\_config\_dict [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#get_model_config_dict "Direct link to get_model_config_dict")

**get\_model\_config\_dict()**

info

This method is deprecated, use `Task.connect_configuration` instead.

- **Return type**

`Dict`


* * *

### get\_model\_config\_text [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#get_model_config_text "Direct link to get_model_config_text")

**get\_model\_config\_text()**

info

This method is deprecated, use `Task.connect_configuration` instead.

- **Return type**

`str`


* * *

### get\_model\_design [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#get_model_design "Direct link to get_model_design")

**get\_model\_design()**

Get the model configuration as blob of text.

- **Return type**

`str`

- **Returns**

The model configuration as blob of text.


* * *

### get\_models [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#get_models "Direct link to get_models")

**get\_models()**

Return a dictionary with `{'input': [], 'output': []}` loaded/stored models of the current Task
Input models are files loaded in the task, either manually or automatically logged.
Output models are files stored in the task, either manually or automatically logged.
Automatically logged frameworks include: TensorFlow, Keras, PyTorch, ScikitLearn(joblib) etc.

- **Return type**

`Mapping`\[`str`, `Sequence`\[ [`Model`](https://clear.ml/docs/latest/docs/references/sdk/model_model#clearml.Model)\]\]

- **Returns**

A dictionary-like object with “input”/”output” keys and input/output properties, pointing to a
list-like object containing Model objects. Each list-like object also acts as a dictionary, mapping
model name to an appropriate model instance.

Example:





```py
{'input': [clearml.Model()], 'output': [clearml.Model()]}
```


* * *

### Task.get\_num\_enqueued\_tasks [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#taskget_num_enqueued_tasks "Direct link to Task.get_num_enqueued_tasks")

**_classmethod_ get\_num\_enqueued\_tasks(queue\_name=None, queue\_id=None)**

Get the number of tasks enqueued in a given queue.

- **Parameters**
  - **queue\_name** (`Optional`\[`str`\]) – The name of the queue. If not specified, then `queue_id` must be specified

  - **queue\_id** (`Optional`\[`str`\]) – The ID of the queue. If not specified, then `queue_name` must be specified
- **Return type**

`int`

- **Returns**

The number of tasks enqueued in the given queue


* * *

### get\_num\_of\_classes [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#get_num_of_classes "Direct link to get_num_of_classes")

**get\_num\_of\_classes()**

number of classes based on the task’s labels

- **Return type**

`int`


* * *

### get\_offline\_mode\_folder [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#get_offline_mode_folder "Direct link to get_offline_mode_folder")

**get\_offline\_mode\_folder()**

Return the folder where all the task outputs and logs are stored in the offline session.

- **Return type**

`Optional`\[`Path`\]

- **Returns**

Path object, local folder, later to be used with `report_offline_session()`


* * *

### get\_output\_destination [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#get_output_destination "Direct link to get_output_destination")

**get\_output\_destination(extra\_path=None, \*\*kwargs)**

Get the task’s output destination, with an optional suffix

- **Return type**

`str`

- **Parameters**
  - **extra\_path** ( _Optional_ _\[_ _str_ _\]_ ) –

  - **kwargs** ( _Any_ ) –

* * *

### get\_output\_log\_web\_page [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#get_output_log_web_page "Direct link to get_output_log_web_page")

**get\_output\_log\_web\_page()**

Return the Task results & outputs web page address.
For example: [https://demoapp.demo.clear.ml/projects/216431/experiments/60763e04/output/log](https://demoapp.demo.clear.ml/projects/216431/experiments/60763e04/output/log)

- **Return type**

`str`

- **Returns**

`http/s` URL link.


* * *

### get\_parameter [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#get_parameter "Direct link to get_parameter")

**get\_parameter(name, default=None, cast=False)**

Get a value for a parameter.

- **Parameters**
  - **name** (`str`) – Parameter name

  - **default** (`Optional`\[`Any`\]) – Default value

  - **cast** (`bool`) – If value is found, cast to original type. If `False`, return string.
- **Return type**

`Any`

- **Returns**

The Parameter value (or default value if parameter is not defined).


* * *

### get\_parameters [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#get_parameters "Direct link to get_parameters")

**get\_parameters(backwards\_compatibility=True, cast=False)**

Get the parameters for a Task. This method returns a complete group of key-value parameter pairs, but does not
support parameter descriptions (the result is a dictionary of key-value pairs).
Notice the returned parameter dict is flat:
i.e. `{'Args/param': 'value'}` is the argument “param” from section “Args”

- **Parameters**
  - **backwards\_compatibility** (`bool`) – If `True` (default), parameters without section name
    (API version <2.9, clearml-server <0.16) will be at dict root level.
    If `False`, parameters without section name, will be nested under “Args/” key.

  - **cast** (`bool`) – If `True`, cast the parameter to the original type. Default `False`,
    values are returned in their string representation
- **Return type**

`Optional`\[`dict`\]

- **Returns**

dict of the task parameters, all flattened to key/value.
Different sections with key prefix “section/”


* * *

### get\_parameters\_as\_dict [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#get_parameters_as_dict "Direct link to get_parameters_as_dict")

**get\_parameters\_as\_dict(cast=False)**

Get the Task parameters as a raw nested dictionary.

info

If `cast` is `False` (default), the values are not parsed. They are returned as is.

- **Parameters**

**cast** (`bool`) – If `True`, cast the parameter to the original type. Default `False`,
values are returned in their string representation

- **Return type**

`Dict`


* * *

### get\_progress [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#get_progress "Direct link to get_progress")

**get\_progress()**

Gets Task’s progress (0 - 100)

- **Return type**

`Optional`\[`int`\]

- **Returns**

Task’s progress as an int.
In case the progress doesn’t exist, `None` will be returned


* * *

### Task.get\_project\_id [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#taskget_project_id "Direct link to Task.get_project_id")

**_classmethod_ get\_project\_id(project\_name, search\_hidden=True)**

Return a project’s unique ID (`str`).
If more than one project matched the `project_name`, return the last updated project.
If no project matched the requested name, returns `None`

- **Return type**

`Optional`\[`str`\]

- **Returns**

Unique Project ID (`str`), or `None` if no project was found.

- **Parameters**
  - **project\_name** ( _str_ ) –

  - **search\_hidden** ( _bool_ ) –

* * *

### get\_project\_name [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#get_project_name "Direct link to get_project_name")

**get\_project\_name()**

Get the current Task’s project name.

- **Return type**

`Optional`\[`str`\]


* * *

### get\_project\_object [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#get_project_object "Direct link to get_project_object")

**get\_project\_object()**

Get the current Task’s project as a python object.

- **Return type**

`Project`


* * *

### Task.get\_projects [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#taskget_projects "Direct link to Task.get_projects")

**_classmethod_ get\_projects(\*\*kwargs)**

Return a list of projects in the system, sorted by last updated time

- **Return type**

`List`\[`Project`\]

- **Returns**

A list of all the projects in the system. Each entry is a `services.projects.Project` object.

- **Parameters**

**kwargs** ( _Any_ ) –


* * *

### get\_registered\_artifacts [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#get_registered_artifacts "Direct link to get_registered_artifacts")

**get\_registered\_artifacts()**

Get a dictionary containing the Task’s registered (dynamically synchronized) artifacts (name, artifact object).

info

After calling `get_registered_artifacts`, you can still modify the registered artifacts.

- **Return type**

`Dict`\[`str`, `Artifact`\]

- **Returns**

The registered (dynamically synchronized) artifacts.


* * *

### get\_reported\_console\_output [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#get_reported_console_output "Direct link to get_reported_console_output")

**get\_reported\_console\_output(number\_of\_reports=1)**

Return a list of console outputs reported by the Task. Retrieved outputs are the most updated console outputs.

- **Parameters**

**number\_of\_reports** ( _int_ ) – The number of reports to return. The default value is `1`, indicating the
last (most updated) console output

- **Return type**

`Sequence`\[`str`\]

- **Returns**

A list of strings, each entry corresponds to one report.


* * *

### get\_reported\_plots [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#get_reported_plots "Direct link to get_reported_plots")

**get\_reported\_plots(max\_iterations=None)**

Return a list of all the plots reported for this Task,
Notice the plot data is plotly compatible.

info

This call is not cached, any call will retrieve all the plot reports from the backend.
If the Task has many plots reported, it might take long for the call to return.

Example:

```py
[{\
\
    "timestamp": 1636921296370,\
\
    "type": "plot",\
\
    "task": "0ce5e89bbe484f428e43e767f1e2bb11",\
\
    "iter": 0,\
\
    "metric": "Manual Reporting",\
\
    "variant": "Just a plot",\
\
    "plot_str": "{'data': [{'type': 'scatter', 'mode': 'markers', 'name': null,\
\
                            'x': [0.2620246750155817], 'y': [0.2620246750155817]}]}",\
\
    "@timestamp": "2021-11-14T20:21:42.387Z",\
\
    "worker": "machine-ml",\
\
    "plot_len": 6135,\
\
},]
```

- **Parameters**

**max\_iterations** ( _int_ ) – Maximum number of historic plots (iterations from end) to return.

- **Return type**

`List`\[`dict`\]

- **Returns**

list: List of dicts, each one represents a single plot


* * *

### get\_reported\_scalars [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#get_reported_scalars "Direct link to get_reported_scalars")

**get\_reported\_scalars(max\_samples=0, x\_axis='iter')**

Return a nested dictionary for the scalar graphs,
where the first key is the graph title and the second is the series name.
Value is a dict with ‘x’: values and ‘y’: values

info

This call is not cached, any call will retrieve all the scalar reports from the backend.
If the Task has many scalars reported, it might take long for the call to return.

info

Calling this method will return potentially downsampled scalars. The maximum number of returned samples is 5000.
Even when setting max\_samples to a value larger than 5000, it will be limited to at most 5000 samples.
To fetch all scalar values, see `Task.get_all_reported_scalars`.

Example:

```py
{

    "title":

    {

        "series": {

            "x": [0, 1 ,2],

            "y": [10, 11 ,12]

        }

    }

}
```

- **Parameters**
  - **max\_samples** ( _int_ ) – Maximum samples per series to return. Default is 0 returning up to 5000 samples.
    With sample limit, average scalar values inside sampling window.

  - **x\_axis** ( _str_ ) – scalar x\_axis, possible values:
    ‘iter’: iteration (default), ‘timestamp’: timestamp as milliseconds since epoch, ‘iso\_time’: absolute time
- **Return type**

`Mapping`\[`str`, `Mapping`\[`str`, `Mapping`\[`str`, `Sequence`\[`float`\]\]\]\]

- **Returns**

dict: Nested scalar graphs: `dict[title(str), dict[series(str), dict[axis(str), list(float)]]]`


* * *

### get\_reported\_single\_value [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#get_reported_single_value "Direct link to get_reported_single_value")

**get\_reported\_single\_value(name)**

Get a single reported value identified by its name. Note that this function calls
`Task.get_reported_single_values`.

- **Parameters**

**name** (`str`) – The name of the reported value

- **Return type**

`Optional`\[`float`\]

- **Returns**

The actual value of the reported value, if found. Otherwise, returns `None`


* * *

### get\_reported\_single\_values [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#get_reported_single_values "Direct link to get_reported_single_values")

**get\_reported\_single\_values()**

Get all reported single values as a dictionary, where the keys are the names of the values
and the values of the dictionary are the actual reported values.

- **Return type**

`Dict`\[`str`, `float`\]

- **Returns**

A dict containing the reported values


* * *

### get\_requirements [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#get_requirements "Direct link to get_requirements")

**get\_requirements()**

Get the task’s requirements

- **Return type**

`RequirementsDict`

- **Returns**

A `RequirementsDict` object that holds the `pip`, `conda`, `orig_pip` requirements.


* * *

### get\_script [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#get_script "Direct link to get_script")

**get\_script()**

Get task’s script details.

Returns a dictionary containing the script details.

- **Return type**

`Mapping`\[`str`, `Optional`\[`str`\]\]

- **Returns**

Dictionary with script properties. For example:


```javascript
{

     'working_dir': 'examples/reporting',

     'entry_point': 'artifacts.py',

     'branch': 'master',

     'repository': 'https://github.com/allegroai/clearml.git'

}
```

* * *

### get\_status [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#get_status "Direct link to get_status")

**get\_status()**

Return The task status without refreshing the entire Task object (only the status property)

TaskStatusEnum: \[“created”, “in\_progress”, “stopped”, “closed”, “failed”, “completed”,\
“queued”, “published”, “publishing”, “unknown”\]

- **Return type**

`str`

- **Returns**

str: Task status as string (TaskStatusEnum)


* * *

### get\_status\_message [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#get_status_message "Direct link to get_status_message")

**get\_status\_message()**

Return the task status without refreshing the entire Task object (only the status property)
Return also the last message coupled with the status change

Task Status options: \[“created”, “in\_progress”, “stopped”, “closed”, “failed”, “completed”,\
“queued”, “published”, “publishing”, “unknown”\].
Message is a string

- **Return type**

( _Optional_\[str\], _Optional_\[str\])

- **Returns**

Task status as string, last message


* * *

### get\_tags [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#get_tags "Direct link to get_tags")

**get\_tags()**

Get all current Task’s tags.

- **Return type**

`Sequence`\[`str`\]


* * *

### Task.get\_task [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#taskget_task "Direct link to Task.get_task")

**_classmethod_ get\_task(task\_id=None, project\_name=None, task\_name=None, tags=None, allow\_archived=True, task\_filter=None)**

Get a Task by ID, or project name / task name combination.

For example:

The following code demonstrates calling `Task.get_task` to report a scalar to another Task. The output
of `Logger.report_scalar` from testing is associated with the Task named `training`. It allows
training and testing to run concurrently, because they initialized different Tasks (see `Task.init`
for information about initializing Tasks).

The training script:

```py
# initialize the training Task

task = Task.init('myProject', 'training')

# do some training
```

The testing script:

```py
# initialize the testing Task

task = Task.init('myProject', 'testing')

# get the training Task

train_task = Task.get_task(project_name='myProject', task_name='training')

# report metrics in the training Task

for x in range(10):

    train_task.get_logger().report_scalar('title', 'series', value=x * 2, iteration=x)
```

- **Parameters**


  - **task\_id** ( _str_ ) – The ID (system UUID) of the experiment to get.
    If specified, `project_name` and `task_name` are ignored.

  - **project\_name** ( _str_ ) – The project name of the Task to get.

  - **task\_name** ( _str_ ) – The name of the Task within `project_name` to get.

  - **tags** ( _list_ ) – Filter based on the requested list of tags (`str`). To exclude a tag add “-” prefix to the
    tag. Example: `["best", "-debug"]`.
    The default behaviour is to join all tags with a logical “OR” operator.
    To join all tags with a logical “AND” operator instead, use “\_\_$all” as the first string, for example:


```py
["__$all", "best", "experiment", "ever"]
```

To join all tags with AND, but exclude a tag use “\_\_$not” before the excluded tag, for example:

```py
["__$all", "best", "experiment", "ever", "__$not", "internal", "__$not", "test"]
```

The “OR” and “AND” operators apply to all tags that follow them until another operator is specified.
The NOT operator applies only to the immediately following tag.
For example:

```py
["__$all", "a", "b", "c", "__$or", "d", "__$not", "e", "__$and", "__$or", "f", "g"]
```

This example means (“a” AND “b” AND “c” AND (“d” OR NOT “e”) AND (“f” OR “g”)).
See [https://clear.ml/docs/latest/docs/clearml\_sdk/task\_sdk/#tag-filters](https://clear.ml/docs/latest/docs/clearml_sdk/task_sdk/#tag-filters) for more information.
  - **allow\_archived** ( _bool_ ) – Only applicable if _not_ using specific `task_id`,
    If `True` (default), allow to return archived Tasks. If `False` filter out archived Tasks

  - **task\_filter** ( _bool_ ) – Only applicable if _not_ using specific `task_id`,
    Pass additional query filters, on top of project/name. See details in `Task.get_tasks`.
- **Returns**

The Task specified by ID, or project name / experiment name combination.

- **Return type**

Task


* * *

### Task.get\_task\_output\_log\_web\_page [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#taskget_task_output_log_web_page "Direct link to Task.get_task_output_log_web_page")

**_classmethod_ get\_task\_output\_log\_web\_page(task\_id, project\_id=None, app\_server\_host=None)**

Return the Task results & outputs web page address.
For example: [https://demoapp.demo.clear.ml/projects/216431/experiments/60763e04/output/log](https://demoapp.demo.clear.ml/projects/216431/experiments/60763e04/output/log)

- **Parameters**
  - **task\_id** ( _str_ ) – Task ID.

  - **project\_id** ( _str_ ) – Project ID for this task.

  - **app\_server\_host** ( _str_ ) – ClearML Application server host name.
    If not provided, the current session will be used to resolve the host name.
- **Return type**

`str`

- **Returns**

`http/s` URL link.


* * *

### Task.get\_tasks [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#taskget_tasks "Direct link to Task.get_tasks")

**_classmethod_ get\_tasks(task\_ids=None, project\_name=None, task\_name=None, tags=None, allow\_archived=True, task\_filter=None)**

Get a list of Tasks objects matching the queries/filters:

- A list of specific Task IDs.

- Filter Tasks based on specific fields:

project name (including partial match), task name (including partial match), tags
Apply Additional advanced filtering with `task_filter`


info

This function returns the most recent 500 tasks. If you wish to retrieve older tasks
use `Task.query_tasks()`

- **Parameters**


  - **task\_ids** ( _list_ _(_ _str_ _)_ ) – The IDs (system UUID) of experiments to get.
    If `task_ids` specified, then `project_name` and `task_name` are ignored.

  - **project\_name** ( _str_ ) – The project name of the Tasks to get. To get the experiment
    in all projects, use the default value of `None`. (Optional)
    Use a list of strings for multiple optional project names.

  - **task\_name** ( _str_ ) – The full name or partial name of the Tasks to match within the specified
    `project_name` (or all projects if `project_name` is `None`).
    This method supports regular expressions for name matching (if you wish to match special characters and
    avoid any regex behaviour, use re.escape()). (Optional)
    To match an exact task name (i.e. not partial matching),
    add ^/$ at the beginning/end of the string, for example: “^exact\_task\_name\_here$”

  - **tags** ( _list_ ) – Filter based on the requested list of tags (`str`). To exclude a tag add “-” prefix to the
    tag. Example: `["best", "-debug"]`.
    The default behaviour is to join all tags with a logical “OR” operator.
    To join all tags with a logical “AND” operator instead, use “\_\_$all” as the first string, for example:


```py
["__$all", "best", "experiment", "ever"]
```

To join all tags with AND, but exclude a tag use “\_\_$not” before the excluded tag, for example:

```py
["__$all", "best", "experiment", "ever", "__$not", "internal", "__$not", "test"]
```

The “OR” and “AND” operators apply to all tags that follow them until another operator is specified.
The NOT operator applies only to the immediately following tag.
For example:

```py
["__$all", "a", "b", "c", "__$or", "d", "__$not", "e", "__$and", "__$or", "f", "g"]
```

This example means (“a” AND “b” AND “c” AND (“d” OR NOT “e”) AND (“f” OR “g”)).
See [https://clear.ml/docs/latest/docs/clearml\_sdk/task\_sdk/#tag-filters](https://clear.ml/docs/latest/docs/clearml_sdk/task_sdk/#tag-filters) for more information.
  - **allow\_archived** ( _bool_ ) – If `True` (default), allow to return archived Tasks. If `False` filter out archived Tasks

  - **task\_filter** ( _dict_ ) – Filter and order Tasks.

    See `backend_api.service.v?.tasks.GetAllRequest` for details; the ? needs to be replaced by the appropriate version.
    - `parent` (`str`) \- Filter by parent task-id matching

    - `search_text` (`str`) \- Free text search (in task fields comment/name/id)

    - `status` (`List[str]`) \- List of valid statuses. Options are: “created”, “queued”, “in\_progress”, “stopped”, “published”, “publishing”, “closed”, “failed”, “completed”, “unknown”

    - `type` (`List[str]`) \- List of valid task types. Options are: ‘training’, ‘testing’, ‘inference’, ‘data\_processing’, ‘application’, ‘monitor’, ‘controller’, ‘optimizer’, ‘service’, ‘qc’. ‘custom’

    - `user` (`List[str]`) \- Filter based on Task’s user owner, provide list of valid user IDs.

    - `order_by` (`List[str]`) \- List of field names to order by. When `search_text` is used. Use ‘-‘ prefix to specify descending order. Optional, recommended when using page. Example: `order_by=['-last_update']`

    - `_all_` (`dict(fields=[], pattern='')`) \- Match string `pattern` (regular expression) appearing in All `fields`. Example: `dict(fields=['script.repository'], pattern='github.com/user')`

    - `_any_` (`dict(fields=[], pattern='')`) \- Match string `pattern` (regular expression) appearing in any of the `fields`. Example: `dict(fields=['comment', 'name'], pattern='my comment')`

    - Examples: `{'status': ['stopped'], 'order_by': ["-last_update"]}` , `{'order_by'=['-last_update'], '_all_'=dict(fields=['script.repository'], pattern='github.com/user'))`
- **Returns**

The Tasks specified by the parameter combinations (see the parameters).

- **Return type**

List\[Task\]


* * *

### get\_user\_properties [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#get_user_properties "Direct link to get_user_properties")

**get\_user\_properties(value\_only=False)**

Get user properties for this task.
Returns a dictionary mapping user property name to user property details dict.

- **Parameters**

**value\_only** (`bool`) – If `True`, returned user property details will be a string representing the property value.

- **Return type**

`Dict`\[`str`, `Union`\[`str`, `dict`\]\]


* * *

### Task.ignore\_requirements [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#taskignore_requirements "Direct link to Task.ignore_requirements")

**_classmethod_ ignore\_requirements(package\_name)**

Ignore a specific package when auto generating the requirements list.
Example: Task.ignore\_requirements(‘pywin32’)

- **Parameters**

**package\_name** ( _str_ ) – The package name to remove/ignore from the “Installed Packages” section of the task.

- **Return type**

`None`


* * *

### Task.import\_offline\_session [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#taskimport_offline_session "Direct link to Task.import_offline_session")

**_classmethod_ import\_offline\_session(session\_folder\_zip, previous\_task\_id=None, iteration\_offset=0)**

Upload an offline session (execution) of a Task.
Full Task execution includes repository details, installed packages, artifacts, logs, metric and debug samples.
This function may also be used to continue a previously executed task with a task executed offline.

- **Parameters**
  - **session\_folder\_zip** (`str`) – Path to a folder containing the session, or zip-file of the session folder.

  - **previous\_task\_id** (`Optional`\[`str`\]) – Task ID of the task you wish to continue with this offline session.

  - **iteration\_offset** (`Optional`\[`int`\]) – Reporting of the offline session will be offset with the
    number specified by this parameter. Useful for avoiding overwriting metrics.
- **Return type**

`Optional`\[`str`\]

- **Returns**

Newly created task ID or the ID of the continued task (`previous_task_id`)


* * *

### Task.import\_task [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#taskimport_task "Direct link to Task.import_task")

**_classmethod_ import\_task(task\_data, target\_task=None, update=False)**

Import (create) Task from previously exported Task configuration (see `Task.export_task`).
Can also be used to edit/update an existing Task (by passing `target_task` and `update=True`).

- **Parameters**
  - **task\_data** (`dict`) – dictionary of a Task’s configuration

  - **target\_task** (`Union`\[`Task`, `str`, `None`\]) – Import `task_data` into an existing Task. Can be either `task_id` (`str`) or Task object.

  - **update** (`bool`) – If `True`, merge `task_data` with current Task configuration.
- **Return type**

`Optional`\[`Task`\]

- **Returns**

`True` if Task was imported/updated


* * *

### Task.init [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#taskinit "Direct link to Task.init")

**_classmethod_ init(project\_name=None, task\_name=None, task\_type=TaskTypes.training, tags=None, reuse\_last\_task\_id=True, continue\_last\_task=False, output\_uri=None, auto\_connect\_arg\_parser=True, auto\_connect\_frameworks=True, auto\_resource\_monitoring=True, auto\_connect\_streams=True, deferred\_init=False)**

Creates a new Task (experiment) if:

- The Task never ran before. No Task with the same `task_name` and `project_name` is stored in
**ClearML Server**.

- The Task has run before (the same `task_name` and `project_name`), and (a) it stored models and / or
artifacts, or (b) its status is Published , or (c) it is Archived.

- A new Task is forced by calling `Task.init` with `reuse_last_task_id=False`.


Otherwise, the already initialized Task object for the same `task_name` and `project_name` is returned,
or, when being executed remotely on a clearml-agent, the task returned is the existing task from the backend.

info

To reference another Task, instead of initializing the same Task more than once, call
`Task.get_task`. For example, to “share” the same experiment in more than one script,
call `Task.get_task`. See the `Task.get_task` method for an example.

For example:
The first time the following code runs, it will create a new Task. The status will be Completed.

```py
from clearml import Task

task = Task.init('myProject', 'myTask')
```

If this code runs again, it will not create a new Task. It does not store a model or artifact,
it is not Published (its status Completed) , it was not Archived, and a new Task is not forced.

If the Task is Published or Archived, and run again, it will create a new Task with a new Task ID.

The following code will create a new Task every time it runs, because it stores an artifact.

```py
task = Task.init('myProject', 'myOtherTask')

d = {'a': '1'}

task.upload_artifact('myArtifact', d)
```

info

Call `Task.init` at the very beginning of your script’s execution
(you can define classes and functions before that if needed).
The `clearml` code intercepts the execution done by your libraries such as pytorch,
so if you execute code before initializing your task, this might lead to memory leaks,
zombie child processes, etc.

An ideal location to call it is right after the `if __name__ == "__main__":` line
(assuming all your code execution is in this `if` statement block).

- **Parameters**


  - **project\_name** ( _str_ ) – The name of the project in which the experiment will be created. If the project does
    not exist, it is created. If `project_name` is `None`, the repository name is used. (Optional)

  - **task\_name** ( _str_ ) – The name of Task (experiment). If `task_name` is `None`, the Python experiment
    script’s file name is used. (Optional)

  - **task\_type** ( _TaskTypes_ ) – The task type. Valid task types:
    - `TaskTypes.training` (default)

    - `TaskTypes.testing`

    - `TaskTypes.inference`

    - `TaskTypes.data_processing`

    - `TaskTypes.application`

    - `TaskTypes.monitor`

    - `TaskTypes.controller`

    - `TaskTypes.optimizer`

    - `TaskTypes.service`

    - `TaskTypes.qc`

    - `TaskTypes.custom`
  - **tags** (`Optional`\[`Sequence`\[`str`\]\]) – Add a list of tags (`str`) to the created Task. For example: `tags=['512x512', 'yolov3']`

  - **reuse\_last\_task\_id** ( _bool_ ) – Force a new Task (experiment) with a previously used Task ID, and the same project and Task name.

    If the previously executed Task has artifacts or models, it will not be
    reused (overwritten), and a new Task will be created. When a Task is reused, the previous execution outputs
    are deleted, including console outputs and logs. The values are:
    - `True` \- Reuse the last Task ID. (default)

    - `False` \- Force a new Task (experiment).

    - A string - You can also specify a Task ID to be reused, instead of the cached ID based on the project/name combination.
  - **continue\_last\_task** ( _bool_ ) – Continue the execution of a previously executed Task (experiment).

    When continuing the executing of a previously executed Task,
    all previous artifacts / models / logs remain intact.
    New logs will continue iteration/step based on the previous execution maximum iteration value.
    For example, The last train/loss scalar reported was iteration 100, the next report will be iteration 101.
    The values are:
    - `True` \- Continue the last Task ID. Specified explicitly by reuse\_last\_task\_id or implicitly with the same logic as reuse\_last\_task\_id

    - `False` \- Overwrite the execution of previous Task (default).

    - A string - You can also specify a Task ID to be continued. This is equivalent to `continue_last_task=True` and `reuse_last_task_id=a_task_id_string`.

    - An integer - Specify initial iteration offset (override the auto automatic `last_iteration_offset`). Pass 0, to disable the automatic `last_iteration_offset` or specify a different initial offset. You can specify a Task ID to be used with `reuse_last_task_id='task_id_here'`
  - **output\_uri** ( _str_ ) – The default location for output models and other artifacts.

    If `True`, the default `files_server` will be used for model storage. In the default location, ClearML creates a subfolder for the
    output. If set to `False`, local runs will not upload output models and artifacts,
    and remote runs will not use any default values provided using `default_output_uri`.
    The subfolder structure is the following: <output destination name> / <project name> / <task name>.<Task ID>.
    Note that for cloud storage, you must install the **ClearML** package for your cloud storage type,
    and then configure your storage credentials. For detailed information, see “Storage” in the ClearML
    Documentation.
    The following are examples of `output_uri` values for the supported locations:
    - A shared folder: `/mnt/share/folder`

    - S3: `s3://bucket/folder`

    - Google Cloud Storage: `gs://bucket-name/folder`

    - Azure Storage: `azure://company.blob.core.windows.net/folder/`

    - Default file server: `True`
  - **auto\_connect\_arg\_parser** (`Union`\[`bool`, `Mapping`\[`str`, `bool`\]\]) – Automatically connect an argparse object to the Task.

    Supported argument parser packages are: argparse, click, python-fire, jsonargparse. The values are:
    - `True` \- Automatically connect. (default)

    - `False` \- Do not automatically connect.

    - A dictionary - In addition to a boolean, you can use a dictionary for fine-grained control of connected
      arguments. The dictionary keys are argparse variable names and the values are booleans.
      The `False` value excludes the specified argument from the Task’s parameter section.
      Keys missing from the dictionary default to `True`, you can change it to be `False` by adding
      `\*` key as `False` to the dictionary.
      An empty dictionary defaults to `False`.

For example:

```py
auto_connect_arg_parser={"do_not_include_me": False, }
```

```py
auto_connect_arg_parser={"only_include_me": True, "*": False}
```

info

To manually connect an argparse, use `Task.connect`.

  - **auto\_connect\_frameworks** (`Union`\[`bool`, `Mapping`\[`str`, `Union`\[`bool`, `str`, `list`\]\]\]) – Automatically connect frameworks.

    This includes patching MatplotLib, XGBoost,
    scikit-learn, Keras callbacks, and TensorBoard/X to serialize plots, graphs, and the model location to
    the **ClearML Server** (backend), in addition to original output destination.
    The values are:
    - `True` \- Automatically connect (default)

    - `False` \- Do not automatically connect

    - A dictionary - In addition to a boolean, you can use a dictionary for fine-grained control of connected
      frameworks. The dictionary keys are frameworks and the values are booleans, other dictionaries used for
      finer control or wildcard strings.
      In case of wildcard strings, the local path of a model file has to match at least one wildcard to be
      saved/loaded by ClearML. Example: `{'pytorch' : '\*.pt', 'tensorflow': ['\*.h5', '\*']}`
      Keys missing from the dictionary default to `True`, and an empty dictionary defaults to `False`.
      Supported keys for finer control: `{'tensorboard': {'report_hparams': bool}}` # whether to report TensorBoard hyperparameters

For example:

```py
auto_connect_frameworks={

    'matplotlib': True,

    'tensorflow': ['*.hdf5', 'something_else*'],

    'tensorboard': True,

    'pytorch': ['*.pt'],

    'xgboost': True,

    'scikit': True,

    'fastai': True,

    'lightgbm': True,

    'hydra': True,

    'detect_repository': True,

    'tfdefines': True,

    'joblib': True,

    'megengine': True,

    'catboost': True,

    'gradio': True

}
```

```py
auto_connect_frameworks={'tensorboard': {'report_hparams': False}}
```

  - **auto\_resource\_monitoring** ( _bool_ ) – Automatically create machine resource monitoring plots.

    These plots appear in the **ClearML Web-App (UI)**, **RESULTS** tab, **SCALARS** sub-tab,
    with a title of **:resource monitor:**.

    The values are:


    - `True` \- Automatically create resource monitoring plots. (default)

    - `False` \- Do not automatically create.

    - Class Type - Create ResourceMonitor object of the specified class type.

    - dict - Dictionary of kwargs to be passed to the ResourceMonitor instance. The keys can be:


    - `report_start_sec` OR `first_report_sec` OR `seconds_from_start` \- Maximum number of seconds
      to wait for scalar/plot reporting before defaulting
      to machine statistics reporting based on seconds from experiment start time
      - `wait_for_first_iteration_to_start_sec` \- Set the initial time (seconds) to wait for iteration
        reporting to be used as x-axis for the resource monitoring,
        if timeout exceeds then reverts to `seconds_from_start`

      - `max_wait_for_first_iteration_to_start_sec` \- Set the maximum time (seconds) to allow the resource
        monitoring to revert back to iteration reporting x-axis after starting to report `seconds_from_start`

      - `report_mem_used_per_process` OR `report_global_mem_used` \- Compatibility feature,
        report memory usage for the entire machine.
        Default (`False`), report only on the running process and its sub-processes
  - **auto\_connect\_streams** (`Union`\[`bool`, `Mapping`\[`str`, `bool`\]\]) – Control the automatic logging of stdout and stderr.

    The values are:
    - `True` \- Automatically connect (default)

    - `False` \- Do not automatically connect

    - A dictionary - In addition to a boolean, you can use a dictionary for fine-grained control of stdout and
      stderr. The dictionary keys are ‘stdout’ , ‘stderr’ and ‘logging’, the values are booleans.
      Keys missing from the dictionary default to `False`, and an empty dictionary defaults to `False`.
      Notice, the default behaviour is logging stdout/stderr. The `logging` module is logged as a by product
      of the stderr logging

For example:

```py
auto_connect_streams={'stdout': True, 'stderr': True, 'logging': False}
```

  - **deferred\_init** (`bool`) – (default: `False`) Wait for Task to be fully initialized (regular behaviour).

    \\*\\* BETA feature! use with care \*\*.

    If set to `True`, `Task.init` function returns immediately and all initialization / communication
    to the clearml-server is running in a background thread. The returned object is
    a full proxy to the regular Task object, hence everything will be working as expected.
    Default behaviour can be controlled with: `CLEARML_DEFERRED_TASK_INIT=1`. Notes:
    - Any access to the returned proxy `Task` object will essentially wait for the `Task.init` to be completed.
      For example: `print(task.name)` will wait for `Task.init` to complete in the
      background and then return the `name` property of the task original object

    - Before `Task.init` completes in the background, auto-magic logging (console/metric) might be missed

    - If running via an agent, this argument is ignored, and Task init is called synchronously (default)
- **Returns**

The main execution Task (Task context)

- **Return type**

Task


* * *

### input\_models\_id [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#input_models_id "Direct link to input_models_id")

**property input\_models\_id: Mapping\[str, str\]**

Returns the current Task’s input model IDs as a dictionary.

- **Return type**

`Mapping`\[`str`, `str`\]


* * *

### is\_current\_task [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#is_current_task "Direct link to is_current_task")

**is\_current\_task()**

info

This method is deprecated, use `Task.is_main_task` instead.

Is this Task object the main execution Task (initially returned by `Task.init`)

- **Return type**

`bool`

- **Returns**

Is this Task object the main execution Task
  - `True` \- Is the main execution Task.

  - `False` \- Is not the main execution Task.

* * *

### is\_main\_task [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#is_main_task "Direct link to is_main_task")

**is\_main\_task()**

Is this Task object the main execution Task (initially returned by `Task.init`)

info

If `Task.init` was never called, this method will not create
it, making this test more efficient than:

`Task.init() == task`

- **Return type**

`bool`

- **Returns**

Is this Task object the main execution Task
  - `True` \- Is the main execution Task.

  - `False` \- Is not the main execution Task.

* * *

### Task.is\_offline [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#taskis_offline "Direct link to Task.is_offline")

**_classmethod_ is\_offline()**

Return offline-mode state, If in offline-mode, no communication to the backend is enabled.

- **Return type**

`bool`

- **Returns**

boolean offline-mode state


* * *

### labels\_stats [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#labels_stats "Direct link to labels_stats")

**property labels\_stats: dict**

Get accumulated label stats for the current/last frames iteration

- **Return type**

`dict`


* * *

### last\_worker [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#last_worker "Direct link to last_worker")

**property last\_worker: str**

ID of last worker that handled the task.

- **Return type**

`str`

- **Returns**

The worker ID.


* * *

### launch\_multi\_node [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#launch_multi_node "Direct link to launch_multi_node")

**launch\_multi\_node(total\_num\_nodes, port=29500, queue=None, wait=False, addr=None, devices=None, hide\_children=False)**

Enqueue multiple clones of the current task to a queue, allowing the task
to be run by multiple workers in parallel. Each task running this way is called a node.
Each node has a rank. The node that initialized the execution of the other nodes
is called the `master` node, and it has a rank equal to 0.

A dictionary named `multi_node_instance` will be connected to the tasks.
One can use this dictionary to modify the behaviour of this function when running remotely.
The contents of this dictionary correspond to the parameters of this function, and they are:

- `total_num_nodes` \- the total number of nodes, including the master node
- `queue` \- the queue to enqueue the nodes to

The following environment variables, will be set:

- `MASTER_ADDR` \- the address of the machine that the master node is running on
- `MASTER_PORT` \- the open port of the machine that the master node is running on
- `WORLD_SIZE` \- the total number of nodes, including the master
- `RANK` \- the rank of the current node (master has rank 0)

One may use this function in conjunction with PyTorch’s distributed communication package.
Note that `Task.launch_multi_node` should be called before `torch.distributed.init_process_group`.
For example:

```py
from clearml import Task

import torch

import torch.distributed as dist

def run(rank, size):

    print(f"World size is {size}")

    tensor = torch.zeros(1)

    if rank == 0:

        for i in range(1, size):

            tensor += 1

            dist.send(tensor=tensor, dst=i)

            print(f"Sending from rank {rank} to rank {i} data: {tensor[0]}")

    else:

        dist.recv(tensor=tensor, src=0)

        print(f"Rank {rank} received data: {tensor[0]}")

if __name__ == '__main__':

    task = Task.init('some_name', 'some_name')

    task.execute_remotely(queue_name='queue')

    config = task.launch_multi_node(4)

    dist.init_process_group('gloo')

    run(config.get('node_rank'), config.get('total_num_nodes'))
```

When using the ClearML cloud autoscaler apps, one needs to make sure the nodes can reach each other.
The machines need to be in the same security group, the `MASTER_PORT` needs to be exposed and the
`MASTER_ADDR` needs to be the right private IP of the instance the master is running on.
For example, to achieve this, one can set the following Docker arguments in the `Additional ClearML Configuration` section:

```py
agent.extra_docker_arguments=[\
\
    "--ipc=host",\
\
    "--network=host",\
\
    "-p", "29500:29500",\
\
    "--env", "CLEARML_MULTI_NODE_MASTER_DEF_ADDR=`hostname -I | awk '{print $1}'`"\
\
]`
```

- **Parameters**
  - **total\_num\_nodes** (`int`) – The total number of nodes to be enqueued, including the master node,
    which should already be enqueued when running remotely

  - **port** (`Optional`\[`int`\]) – Port opened by the master node. If the environment variable `CLEARML_MULTI_NODE_MASTER_DEF_PORT`
    is set, the value of this parameter will be set to the one defined in `CLEARML_MULTI_NODE_MASTER_DEF_PORT`.
    If `CLEARML_MULTI_NODE_MASTER_DEF_PORT` doesn’t exist, but `MASTER_PORT` does, then the value of this
    parameter will be set to the one defined in `MASTER_PORT`. If neither environment variables exist,
    the value passed to the parameter will be used

  - **queue** (`Optional`\[`str`\]) – The queue to enqueue the nodes to. Can be different from the queue the master
    node is enqueued to. If `None`, the nodes will be enqueued to the same queue as the master node

  - **wait** (`bool`) – If `True`, the master node will wait for the other nodes to start

  - **addr** (`Optional`\[`str`\]) – The address of the master node’s worker. If the environment variable
    `CLEARML_MULTI_NODE_MASTER_DEF_ADDR` is set, the value of this parameter will be set to
    the one defined in `CLEARML_MULTI_NODE_MASTER_DEF_ADDR`.
    If `CLEARML_MULTI_NODE_MASTER_DEF_ADDR` doesn’t exist, but `MASTER_ADDR` does, then the value of this
    parameter will be set to the one defined in `MASTER_ADDR`. If neither environment variables exist,
    the value passed to the parameter will be used. If this value is `None` (default), the private IP of
    the machine the master node is running on will be used.

  - **devices** (`Union`\[`int`, `Sequence`\[`int`\], `None`\]) – The devices to use. This can be a positive number indicating the number of devices to use,
    a sequence of indices or the value `-1` to indicate all available devices should be used.

  - **hide\_children** – If `True`, the children tasks will be hidden. Otherwise, they will be visible in the UI
- **Returns**

A dictionary containing relevant information regarding the multi node run. This dictionary has the following entries:
  - `master_addr` \- The address of the machine that the master node is running on

  - `master_port` \- The open port of the machine that the master node is running on

  - `total_num_nodes` \- The total number of nodes, including the master

  - `queue` \- The queue the nodes are enqueued to, excluding the master

  - `node_rank` \- The rank of the current node (master has rank 0)

  - `wait` \- If `True`, the master node will wait for the other nodes to start

* * *

### list\_external\_endpoints [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#list_external_endpoints "Direct link to list_external_endpoints")

**list\_external\_endpoints(protocol=None)**

List all external endpoints assigned

- **Parameters**

**protocol** (`Optional`\[`str`\]) – If `None`, list all external endpoints. Otherwise, only list endpoints
that use this protocol

- **Return type**

`List`\[`Dict`\]

- **Returns**

A list of dictionaries. Each dictionary contains the following values:
  - `endpoint` \- Raw endpoint. One might need to authenticate in order to use this endpoint

  - `browser_endpoint` \- Endpoint to be used in browser. Authentication will be handled via the browser

  - `port` \- The port exposed by the application

  - `protocol` \- The protocol used by the endpoint

  - `name` \- The identifier used for this endpoint

* * *

### log [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#log "Direct link to log")

**property log: Logger**

A decorator indicating abstract properties.

Deprecated, use ‘property’ with ‘abstractmethod’ instead.

- **Return type**

`Logger`


* * *

### logger [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#logger "Direct link to logger")

**property logger: Logger**

Get a Logger object for reporting, for this task context. You can view all Logger report output associated with
the Task for which this method is called, including metrics, plots, text, tables, and images, in the
**ClearML Web-App (UI)**.

- **Return type**

[`Logger`](https://clear.ml/docs/latest/docs/references/sdk/logger#clearml.Logger)

- **Returns**

The Logger object for the current Task (experiment).


* * *

### mark\_completed [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#mark_completed "Direct link to mark_completed")

**mark\_completed(ignore\_errors=True, status\_message=None, force=False)**

Use this method to close and change status of (remotely!) executed tasks.

This method closes the task it is a member of,
changes its status to “Completed”, and
terminates the Python process that created the task.
This is in contrast to `Task.close`, which does the first two steps, but does not terminate any Python process.

Let’s say that process A created the task and process B has a handle on the task, e.g., with `Task.get_task`.
Then, if we call `Task.mark_completed`, process A is terminated, but process B is not.

However, if `Task.mark_completed` was called from the same process in which the task was created,
then - effectively - the process terminates itself.
For example, in

```py
task = Task.init(...)

task.mark_completed()

from time import sleep

sleep(30)

print('This text will not be printed!')
```

the text will not be printed, because the Python process is immediately terminated.

- **Parameters**
  - **ignore\_errors** ( _bool_ ) – If `True` (default), ignore any errors raised

  - **force** ( _bool_ ) – If `True`, the task status will be changed to `stopped` regardless of the current Task state.

  - **status\_message** ( _str_ ) – Optional, add status change message to the stop request.
    This message will be stored as status\_message on the Task’s info panel
- **Return type**

`Optional`\[`CallResult`\]


* * *

### mark\_failed [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#mark_failed "Direct link to mark_failed")

**mark\_failed(ignore\_errors=True, status\_reason=None, status\_message=None, force=False)**

The signal that this Task stopped.

- **Return type**

`Optional`\[`CallResult`\]

- **Parameters**
  - **ignore\_errors** ( _bool_ ) –

  - **status\_reason** ( _Optional_ _\[_ _str_ _\]_ ) –

  - **status\_message** ( _Optional_ _\[_ _str_ _\]_ ) –

  - **force** ( _bool_ ) –

* * *

### mark\_started [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#mark_started "Direct link to mark_started")

**mark\_started(force=False)**

Manually mark a Task as started (happens automatically)

- **Parameters**

**force** ( _bool_ ) – If `True`, the task status will be changed to `started` regardless of the current Task state.

- **Return type**

`None`


* * *

### mark\_stop\_request [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#mark_stop_request "Direct link to mark_stop_request")

**mark\_stop\_request(force=False, status\_message=None)**

Request a task to stop. this will not change the task status
but mark a request for an agent or SDK to actually stop the Task.
This will trigger the Task’s abort callback, and at the end will
change the task status to stopped and kill the Task’s processes

Notice: calling this on your own Task, will cause
the watchdog to call the `on_abort` callback and kill the process

- **Parameters**
  - **force** ( _bool_ ) – If not `True`, call fails if the task status is not ‘in\_progress’

  - **status\_message** ( _str_ ) – Optional, add status change message to the stop request.
    This message will be stored as `status_message` on the Task’s info panel
- **Return type**

`Optional`\[`CallResult`\]


* * *

### mark\_stopped [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#mark_stopped "Direct link to mark_stopped")

**mark\_stopped(force=False, status\_message=None)**

Manually mark a Task as stopped (also used in `_at_exit`)

- **Parameters**
  - **force** ( _bool_ ) – If `True`, the task status will be changed to `stopped` regardless of the current Task state.

  - **status\_message** ( _str_ ) – Optional, add status change message to the stop request.
    This message will be stored as status\_message on the Task’s info panel
- **Return type**

`None`


* * *

### metrics\_manager [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#metrics_manager "Direct link to metrics_manager")

**property metrics\_manager: Metrics**

A metrics manager used to manage the metrics related to this task

- **Return type**

`Metrics`


* * *

### models [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#models "Direct link to models")

**property models: Mapping\[str, Sequence\[Model\]\]**

Read-only dictionary of the Task’s loaded/stored models.

- **Return type**

`Mapping`\[`str`, `Sequence`\[ [`Model`](https://clear.ml/docs/latest/docs/references/sdk/model_model#clearml.Model)\]\]

- **Returns**

A dictionary-like object with “input”/”output” keys and input/output properties, pointing to a
list-like object containing Model objects. Each list-like object also acts as a dictionary, mapping
model name to an appropriate model instance.

Get input/output models:





```py
task.models.input

task.models["input"]



task.models.output

task.models["output"]
```









Get the last output model:





```py
task.models.output[-1]
```









Get a model by name:





```py
task.models.output["model name"]
```


* * *

### move\_to\_project [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#move_to_project "Direct link to move_to_project")

**move\_to\_project(new\_project\_id=None, new\_project\_name=None, system\_tags=None)**

Move this task to another project

- **Parameters**
  - **new\_project\_id** (`Optional`\[`str`\]) – The ID of the project the task should be moved to.
    Not required if `new_project_name` is passed.

  - **new\_project\_name** (`Optional`\[`str`\]) – Name of the new project the task should be moved to.
    Not required if `new_project_id` is passed.

  - **system\_tags** (`Optional`\[`Sequence`\[`str`\]\]) – System tags for the project the task should be moved to.
- **Return type**

`bool`

- **Returns**

`True` if the move was successful and `False` otherwise


* * *

### name [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#name "Direct link to name")

**property name: str**

Returns the current Task’s name.

- **Return type**

`str`


* * *

### output\_models\_id [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#output_models_id "Direct link to output_models_id")

**property output\_models\_id: Mapping\[str, str\]**

Returns the current Task’s output model IDs as a dictionary.

- **Return type**

`Mapping`\[`str`, `str`\]


* * *

### output\_uri [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#output_uri "Direct link to output_uri")

**property output\_uri: str**

The storage / output URL for this task. This is the default location for output models and other artifacts.

- **Return type**

`str`

- **Returns**

The URL string.


* * *

### parent [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#parent "Direct link to parent")

**property parent: str**

Returns the current Task’s parent task ID (`str`).

- **Return type**

`str`


* * *

### project [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#project "Direct link to project")

**property project: str**

Returns the current Task’s project ID.

- **Return type**

`str`


* * *

### publish [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#publish "Direct link to publish")

**publish(ignore\_errors=True)**

The signal that this task will be published

- **Return type**

`PublishResponse`

- **Parameters**

**ignore\_errors** ( _bool_ ) –


* * *

### publish\_on\_completion [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#publish_on_completion "Direct link to publish_on_completion")

**publish\_on\_completion(enable=True)**

The signal that this task will be published automatically on task completion

- **Return type**

`None`

- **Parameters**

**enable** ( _bool_ ) –


* * *

### Task.query\_tasks [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#taskquery_tasks "Direct link to Task.query_tasks")

**_classmethod_ query\_tasks(project\_name=None, task\_name=None, tags=None, additional\_return\_fields=None, task\_filter=None)**

Get a list of Tasks ID matching the specific query/filter.
Notice, if `additional_return_fields` is specified, returns a list of
dictionaries with requested fields (dict per Task)

- **Parameters**


  - **project\_name** ( _str_ ) – The project name of the Tasks to get. To get the experiment
    in all projects, use the default value of `None`. (Optional)
    Use a list of strings for multiple optional project names.

  - **task\_name** ( _str_ ) – The full name or partial name of the Tasks to match within the specified
    `project_name` (or all projects if `project_name` is `None`).
    This method supports regular expressions for name matching (if you wish to match special characters and
    avoid any regex behaviour, use re.escape()). (Optional)

  - **project\_name** – project name (`str`) the task belongs to (use `None` for all projects)

  - **task\_name** – task name (`str`) within the selected project
    Return any partial match of task\_name, regular expressions matching is also supported.
    If `None` is passed, returns all tasks within the project

  - **tags** ( _list_ ) – Filter based on the requested list of tags (`str`).
    To exclude a tag add “-” prefix to the tag. Example: `["best", "-debug"]`.
    The default behaviour is to join all tags with a logical “OR” operator.
    To join all tags with a logical “AND” operator instead, use “\_\_$all” as the first string, for example:


```py
["__$all", "best", "experiment", "ever"]
```

To join all tags with AND, but exclude a tag use “\_\_$not” before the excluded tag, for example:

```py
["__$all", "best", "experiment", "ever", "__$not", "internal", "__$not", "test"]
```

The “OR” and “AND” operators apply to all tags that follow them until another operator is specified.
The NOT operator applies only to the immediately following tag.
For example:

```py
["__$all", "a", "b", "c", "__$or", "d", "__$not", "e", "__$and", "__$or", "f", "g"]
```

This example means (“a” AND “b” AND “c” AND (“d” OR NOT “e”) AND (“f” OR “g”)).
See [https://clear.ml/docs/latest/docs/clearml\_sdk/task\_sdk/#tag-filters](https://clear.ml/docs/latest/docs/clearml_sdk/task_sdk/#tag-filters) for more information.
  - **additional\_return\_fields** ( _list_ ) – Optional, if not provided return a list of Task IDs.
    If provided return dict per Task with the additional requested fields.
    Example: `returned_fields=['last_updated', 'user', 'script.repository']` will return a list of dict:
    `[{'id': 'task_id', 'last_update': datetime.datetime(), 'user': 'user_id', 'script.repository': 'https://github.com/user/'}, ]`

  - **task\_filter** ( _dict_ ) – filter and order Tasks.

    See `backend_api.service.v?.tasks.GetAllRequest` for details; the ? needs to be replaced by the appropriate version.
    - `parent` (`str`) \- Filter by parent task-id matching

    - `search_text` (`str`) \- Free text search (in task fields comment/name/id)

    - `status` (`List[str]`) \- List of valid statuses. Options are: “created”, “queued”, “in\_progress”, “stopped”, “published”, “publishing”, “closed”, “failed”, “completed”, “unknown”

    - `type` (`List[Union[str, TaskTypes]]`) \- List of valid task types. Options are: ‘training’, ‘testing’, ‘inference’, ‘data\_processing’, ‘application’, ‘monitor’, ‘controller’, ‘optimizer’, ‘service’, ‘qc’. ‘custom’

    - `user` (`List[str]`) \- Filter based on Task’s user owner, provide list of valid user IDs.

    - `order_by` (`List[str]`) \- List of field names to order by. When `search_text` is used. Use ‘-‘ prefix to specify descending order. Optional, recommended when using page. Example: `order_by=['-last_update']`

    - `_all_` (`dict(fields=[], pattern='')`) \- Match string `pattern` (regular expression) appearing in All `fields`. Example: `dict(fields=['script.repository'], pattern='github.com/user')`

    - `_any_` (`dict(fields=[], pattern='')`) \- Match string `pattern` (regular expression) appearing in any of the `fields`. Example: `dict(fields=['comment', 'name'], pattern='my comment')`

    - Examples: `{'status': ['stopped'], 'order_by': ["-last_update"]}` , `{'order_by'=['-last_update'], '_all_'=dict(fields=['script.repository'], pattern='github.com/user'))`
- **Return type**

`Union`\[`List`\[`str`\], `List`\[`Dict`\[`str`, `str`\]\]\]

- **Returns**

The Tasks specified by the parameter combinations (see the parameters).


* * *

### register\_abort\_callback [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#register_abort_callback "Direct link to register_abort_callback")

**register\_abort\_callback(callback\_function, callback\_execution\_timeout=30.0)**

Register a Task abort callback (single callback function support only).
Pass a function to be called from a background thread when the Task is **externally** being aborted.
Users must specify a timeout for the callback function execution (default 30 seconds)
if the callback execution function exceeds the timeout, the Task’s process will be terminated

Call this register function from the main process only.

Note: Ctrl-C is Not considered external, only backend induced abort is covered here

- **Parameters**
  - **callback\_function** (`Optional`\[`Callable`\]) – Callback function to be called via external thread (from the main process).
    pass `None` to remove existing callback

  - **callback\_execution\_timeout** (`float`) – Maximum callback execution time in seconds, after which the process
    will be terminated even if the callback did not return

* * *

### register\_artifact [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#register_artifact "Direct link to register_artifact")

**register\_artifact(name, artifact, metadata=None, uniqueness\_columns=True)**

Register (add) an artifact for the current Task. Registered artifacts are dynamically synchronized with the
**ClearML Server** (backend). If a registered artifact is updated, the update is stored in the
**ClearML Server** (backend). Registered artifacts are primarily used for data auditing.

The currently supported registered artifact object type is a pandas.DataFrame.

See also `Task.unregister_artifact` and `Task.get_registered_artifacts`.

info

ClearML also supports uploaded artifacts which are one-time uploads of static artifacts that are not
dynamically synchronized with the ClearML Server (backend). These static artifacts include
additional object types. For more information, see `Task.upload_artifact`.

- **Parameters**


  - **name** ( _str_ ) – The name of the artifact.

warning

If an artifact with the same name was previously registered, it is overwritten.

  - **artifact** ( _object_ ) – The artifact object.

  - **metadata** ( _dict_ ) – A dictionary of key-value pairs for any metadata. This dictionary appears with the
    experiment in the **ClearML Web-App (UI)**, **ARTIFACTS** tab.

  - **uniqueness\_columns** (`Union`\[`bool`, `Sequence`\[`str`\]\]) – A Sequence of columns for artifact uniqueness comparison criteria, or the default
    value of `True`. If `True`, the artifact uniqueness comparison criteria is all the columns,
    which is the same as `artifact.columns`.
- **Return type**

`None`


* * *

### reload [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#reload "Direct link to reload")

**reload()**

Reload current Task’s state from clearml-server.
Refresh all task’s fields, including artifacts / models / parameters etc.

- **Return type**

`None`


* * *

### remove\_input\_models [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#remove_input_models "Direct link to remove_input_models")

**remove\_input\_models(models\_to\_remove)**

Remove input models from the current task. Note that the models themselves are not deleted,
but the tasks’ reference to the models is removed.
To delete the models themselves, see `Models.remove`

- **Parameters**

**models\_to\_remove** (`Sequence`\[`Union`\[`str`, `ForwardRef`\]\]) – The models to remove from the task. Can be a list of IDs,
or of `BaseModel` (including its subclasses: `Model` and `InputModel`)

- **Return type**

`None`


* * *

### remove\_tags [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#remove_tags "Direct link to remove_tags")

**remove\_tags(tags)**

Remove Tags from this task. Old tags that aren’t specified are not deleted. When executing a Task (experiment) remotely,
this method has no effect).

- **Parameters**

**tags** (`Union`\[`Sequence`\[`str`\], `str`\]) – A list of tags to add to the Task.


* * *

### rename [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#rename "Direct link to rename")

**rename(new\_name)**

Rename this task

- **Parameters**

**new\_name** (`str`) – The new name of this task

- **Return type**

`bool`

- **Returns**

`True` if the rename was successful and `False` otherwise


* * *

### request\_external\_endpoint [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#request_external_endpoint "Direct link to request_external_endpoint")

**request\_external\_endpoint(port, protocol='http', wait=False, wait\_interval\_seconds=3.0, wait\_timeout\_seconds=90.0, static\_route=None, endpoint\_name=None)**

Request an external endpoint for an application

- **Parameters**
  - **port** (`int`) – Port the application is listening to

  - **protocol** (`str`) – `http` or `tcp`

  - **wait** (`bool`) – If `True`, wait for the endpoint to be assigned

  - **wait\_interval\_seconds** (`float`) – The poll frequency when waiting for the endpoint

  - **wait\_timeout\_seconds** (`float`) – If this timeout is exceeded while waiting for the endpoint,
    the method will no longer wait and `None` will be returned

  - **static\_route** (`Optional`\[`str`\]) – The static route name (not the route path).
    When set, the external endpoint requested will use this route
    instead of generating it based on the task ID. Useful for creating
    persistent, load balanced routes.

  - **endpoint\_name** (`Optional`\[`str`\]) – Optional identifier for this endpoint. Useful to distinguish
    between multiple endpoints. If not provided, the endpoint\_name is auto-generated
- **Return type**

`Optional`\[`Dict`\]

- **Returns**

If wait is `False`, this method will return `None`. If no endpoint could be found while waiting, this method returns `None`. Otherwise, it returns a dictionary containing the following values:
  - `endpoint` \- raw endpoint. One might need to authenticate in order to use this endpoint

  - `browser_endpoint` \- endpoint to be used in browser. Authentication will be handled via the browser

  - `port` \- the port exposed by the application

  - `protocol` \- the protocol used by the endpoint

  - `name` \- the identifier used for this endpoint

* * *

### reset [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#reset "Direct link to reset")

**reset(set\_started\_on\_success=False, force=False)**

Reset a Task. ClearML reloads a Task after a successful reset.
When a worker executes a Task remotely, the Task does not reset unless
the `force` parameter is set to `True` (this avoids accidentally clearing logs and metrics).

- **Parameters**
  - **set\_started\_on\_success** ( _bool_ ) – If successful, automatically set the Task to `started`
    - `True` \- If successful, set to started.

    - `False` \- If successful, do not set to started. (default)
  - **force** ( _bool_ ) – Force a Task reset, even when executing the Task (experiment) remotely in a worker
    - `True` \- Force

    - `False` \- Do not force (default)
- **Return type**

`None`


* * *

### running\_locally [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#running_locally "Direct link to running_locally")

**static running\_locally()**

Is the task running locally (i.e., `clearml-agent` is not executing it)

- **Return type**

`bool`

- **Returns**

`True`, if the task is running locally. `False`, if the task is not running locally.


* * *

### save\_exec\_model\_design\_file [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#save_exec_model_design_file "Direct link to save_exec_model_design_file")

**save\_exec\_model\_design\_file(filename='model\_design.txt', use\_cache=False)**

Save execution model design to file

- **Return type**

`str`

- **Parameters**
  - **filename** ( _str_ ) –

  - **use\_cache** ( _bool_ ) –

* * *

### session [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#session "Direct link to session")

**property session: Session**

A decorator indicating abstract properties.

Deprecated, use ‘property’ with ‘abstractmethod’ instead.

- **Return type**

`Session`


* * *

### set\_archived [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#set_archived "Direct link to set_archived")

**set\_archived(archive)**

Archive the Task or remove it from the archived folder.

- **Parameters**

**archive** (`bool`) – If `True`, archive the Task. If `False`, make sure it is removed from the archived folder

- **Return type**

`None`


* * *

### set\_artifacts [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#set_artifacts "Direct link to set_artifacts")

**set\_artifacts(artifacts\_list=None)**

List of artifacts (`tasks.Artifact`) to update the task

- **Parameters**

**artifacts\_list** ( _list_ ) – list of artifacts (type `tasks.Artifact`)

- **Return type**

`Optional`\[`List`\[`Artifact`\]\]

- **Returns**

List of current Task’s Artifacts or None if error.


* * *

### set\_base\_docker [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#set_base_docker "Direct link to set_base_docker")

**set\_base\_docker(docker\_cmd=None, docker\_image=None, docker\_arguments=None, docker\_setup\_bash\_script=None)**

Set the base docker image for this experiment.
If provided, this value will be used by clearml-agent to execute this experiment
inside the provided docker image.
When running remotely the call is ignored

- **Parameters**
  - **docker\_cmd** (`Optional`\[`str`\]) – Deprecated! compound docker container image + arguments
    (example: `'nvidia/cuda:11.1 -e test=1'`). Deprecated, use specific arguments.

  - **docker\_image** (`Optional`\[`str`\]) – docker container image (example: `'nvidia/cuda:11.1'`)

  - **docker\_arguments** (`Union`\[`Sequence`\[`str`\], `str`, `None`\]) – docker execution parameters (example: `'-e ENV=1'`)

  - **docker\_setup\_bash\_script** (`Union`\[`Sequence`\[`str`\], `str`, `None`\]) – bash script to run at the
    beginning of the docker before launching the Task itself. Example: `['apt update', 'apt-get install -y gcc']`
- **Return type**

`None`


* * *

### set\_comment [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#set_comment "Direct link to set_comment")

**set\_comment(comment)**

Set a comment / description for the Task.

- **Parameters**

**comment** ( _str_ ) – The comment / description for the Task.

- **Return type**

`None`


* * *

### set\_configuration\_object [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#set_configuration_object "Direct link to set_configuration_object")

**set\_configuration\_object(name, config\_text=None, description=None, config\_type=None, config\_dict=None)**

Set the Task’s configuration object as a blob of text or automatically encoded dictionary/list.
Use only for automation (externally), otherwise use `Task.connect_configuration`.

- **Parameters**
  - **name** ( _str_ ) – Configuration section name

  - **config\_text** (`Optional`\[`str`\]) – Configuration as a blob of text (unconstrained text string)
    usually the content of a configuration file of a sort

  - **description** ( _str_ ) – Configuration section description

  - **config\_type** ( _str_ ) – Optional configuration format type

  - **config\_dict** ( _dict_ ) – Configuration dictionary/list to be encoded using HOCON (json alike) into stored text
    Notice you can either pass `config_text` or `config_dict`, not both
- **Return type**

`None`


* * *

### Task.set\_credentials [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#taskset_credentials "Direct link to Task.set_credentials")

**_classmethod_ set\_credentials(api\_host=None, web\_host=None, files\_host=None, key=None, secret=None, store\_conf\_file=False)**

Set new default **ClearML Server** (backend) host and credentials.

These credentials will be overridden by either OS environment variables, or the ClearML configuration
file, `clearml.conf`.

warning

Credentials must be set before initializing a Task object.

For example, to set credentials for a remote computer:

```py
Task.set_credentials(

    api_host='http://localhost:8008', web_host='http://localhost:8080', files_host='http://localhost:8081',

    key='optional_credentials',  secret='optional_credentials'

)

task = Task.init('project name', 'experiment name')
```

- **Parameters**
  - **api\_host** ( _str_ ) – The API server URL. For example, `host='http://localhost:8008'`

  - **web\_host** ( _str_ ) – The Web server URL. For example, `host='http://localhost:8080'`

  - **files\_host** ( _str_ ) – The file server URL. For example, `host='http://localhost:8081'`

  - **key** ( _str_ ) – The user key (in the key/secret pair). For example, `key='thisisakey123'`

  - **secret** ( _str_ ) – The user secret (in the key/secret pair). For example, `secret='thisisseceret123'`

  - **store\_conf\_file** ( _bool_ ) – If `True`, store the current configuration into the ~/clearml.conf file.
    If the configuration file exists, no change will be made (outputs a warning).
    Not applicable when running remotely (i.e. clearml-agent).
- **Return type**

`None`


* * *

### set\_dataview [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#set_dataview "Direct link to set_dataview")

**set\_dataview(dataview)**

Store a HyperDatasets DataView definition into this Task using task properties
(i.e. under input.\*), so the DataView appears in the UI, without using
runtime properties.

- If `dataview` is a string ID, the backend is queried to fetch its full
definition, and it is serialized into the task’s `input` section.

- If `dataview` is a `DataView`, its current state is serialized
into the task’s `input` section.


- **Parameters**

**dataview** – DataView instance or dataview ID string

- **Return type**

`None`


* * *

### set\_initial\_iteration [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#set_initial_iteration "Direct link to set_initial_iteration")

**set\_initial\_iteration(offset=0)**

Set initial iteration, instead of zero. Useful when continuing training from previous checkpoints

- **Parameters**

**offset** ( _int_ ) – Initial iteration (at starting point)

- **Return type**

`int`

- **Returns**

Newly set initial offset.


* * *

### set\_input\_model [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#set_input_model "Direct link to set_input_model")

**set\_input\_model(model\_id=None, model\_name=None, update\_task\_design=True, update\_task\_labels=True, name=None)**

Set a new input model for the Task. The model must be “ready” (status is `Published`) to be used as the
Task’s input model.

- **Parameters**
  - **model\_id** (`Optional`\[`str`\]) – The ID of the model on the **ClearML Server** (backend). If `model_name` is not specified,
    then `model_id` must be specified.

  - **model\_name** (`Optional`\[`str`\]) – The model name in the artifactory. The model\_name is used to locate an existing model
    in the **ClearML Server** (backend). If `model_id` is not specified,
    then `model_name` must be specified.

  - **update\_task\_design** (`bool`) – Update the Task’s design
    - `True` \- ClearML copies the Task’s model design from the input model.

    - `False` \- ClearML does not copy the Task’s model design from the input model.
  - **update\_task\_labels** (`bool`) – Update the Task’s label enumeration
    - `True` \- ClearML copies the Task’s label enumeration from the input model.

    - `False` \- ClearML does not copy the Task’s label enumeration from the input model.
  - **name** (`Optional`\[`str`\]) – Model section name to be stored on the Task (unrelated to the model object name itself).
    Default: the model weight filename is used (excluding file extension)
- **Return type**

`None`


* * *

### set\_model\_config [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#set_model_config "Direct link to set_model_config")

**set\_model\_config(config\_text=None, config\_dict=None)**

info

This method is deprecated, use `Task.connect_configuration` instead.

- **Return type**

`None`

- **Parameters**
  - **config\_text** ( _Optional_ _\[_ _str_ _\]_ ) –

  - **config\_dict** ( _Optional_ _\[_ _Mapping_ _\]_ ) –

* * *

### set\_model\_label\_enumeration [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#set_model_label_enumeration "Direct link to set_model_label_enumeration")

**set\_model\_label\_enumeration(enumeration=None)**

Set the label enumeration for the Task object before creating an output model.
Later, when creating an output model, the model will inherit these properties.

- **Parameters**

**enumeration** ( _dict_ ) – A label enumeration dictionary of string (label) to integer (value) pairs.

For example:





```javascript
{

       "background": 0,

       "person": 1

}
```

- **Return type**

`None`


* * *

### set\_name [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#set_name "Direct link to set_name")

**set\_name(name)**

Set the Task name.

- **Parameters**

**name** ( _str_ ) – The name of the Task.

- **Return type**

`None`


* * *

### Task.set\_offline [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#taskset_offline "Direct link to Task.set_offline")

**_classmethod_ set\_offline(offline\_mode=False)**

Set offline mode, where all data and logs are stored into local folder, for later transmission

info

`Task.set_offline` can’t move the same task from offline to online, nor can it be applied before `Task.create`.
See below an example of incorrect usage of `Task.set_offline`:

```text
from clearml import Task

Task.set_offline(True)

task = Task.create(project_name=’DEBUG’, task_name=”offline”)

# ^^^ an error or warning is raised, saying that Task.set_offline(True)

#     is supported only for Task.init

Task.set_offline(False)

# ^^^ an error or warning is raised, saying that running Task.set_offline(False)

#     while the current task is not closed is not supported

data = task.export_task()

imported_task = Task.import_task(task_data=data)
```

The correct way to use `Task.set_offline` can be seen in the following example:

```text
from clearml import Task

Task.set_offline(True)

task = Task.init(project_name=’DEBUG’, task_name=”offline”)

task.upload_artifact(“large_artifact”, “test_string”)

task.close()

Task.set_offline(False)

imported_task = Task.import_offline_session(task.get_offline_mode_folder())
```

- **Parameters**

**offline\_mode** (`bool`) – If `True`, offline-mode is turned on, and no communication to the backend is enabled.

- **Return type**

`None`

- **Returns**


* * *

### set\_packages [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#set_packages "Direct link to set_packages")

**set\_packages(packages)**

Manually specify a list of required packages or a local requirements.txt file. Note that this will
overwrite all existing packages.

When running remotely this call is ignored

- **Parameters**

**packages** (`Union`\[`str`, `Path`, `Sequence`\[`str`\]\]) – The list of packages or the path to the requirements.txt file.

Example: `["tqdm==2.1", "scikit-learn"]` or `"./requirements.txt"` or `""`
Use an empty string (`packages=""`) to clear the requirements section (remote execution will use
requirements.txt from the git repository if the file exists)

- **Return type**

`None`


* * *

### set\_parameter [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#set_parameter "Direct link to set_parameter")

**set\_parameter(name, value, description=None, value\_type=None)**

Set a single Task parameter. This overrides any previous value for this parameter.

- **Parameters**
  - **name** (`str`) – The parameter name.

  - **value** (`str`) – The parameter value.

  - **description** (`Optional`\[`str`\]) – The parameter description.

  - **value\_type** (`Optional`\[`Any`\]) – The type of the parameters (cast to string and store)
- **Return type**

`None`


* * *

### set\_parameters [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#set_parameters "Direct link to set_parameters")

**set\_parameters(\*args, \*\*kwargs)**

Set the parameters for a Task. This method sets a complete group of key-value parameter pairs, but does not
support parameter descriptions (the input is a dictionary of key-value pairs).
Notice the parameter dict is flat:
i.e. `{'Args/param': 'value'}` will set the argument “param” in section “Args” to “value”

- **Parameters**
  - **args** (`dict`) – Positional arguments, which are one or more dictionaries or (key, value) iterable. They are
    merged into a single key-value pair dictionary.

  - **kwargs** (`Any`) – Key-value pairs, merged into the parameters dictionary created from `args`.
- **Return type**

`None`


* * *

### set\_parameters\_as\_dict [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#set_parameters_as_dict "Direct link to set_parameters_as_dict")

**set\_parameters\_as\_dict(dictionary)**

Set the parameters for the Task object from a dictionary. The dictionary can be nested.
This does not link the dictionary to the Task object. It does a one-time update. This
is the same behavior as the `Task.connect` method.

- **Return type**

`None`

- **Parameters**

**dictionary** ( _Dict_ ) –


* * *

### set\_parent [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#set_parent "Direct link to set_parent")

**set\_parent(parent)**

Set the parent task for the Task.

- **Parameters**

**parent** (`str`, `None`, or `Task`) – The parent task ID (or parent Task object) for the Task. Set `None` for no parent.

- **Return type**

`None`


* * *

### set\_progress [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#set_progress "Direct link to set_progress")

**set\_progress(progress)**

Sets Task’s progress (0 - 100)
Progress is a field computed and reported by the user.

- **Parameters**

**progress** (`int`) – numeric value (0 - 100)

- **Return type**

`None`


* * *

### set\_project [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#set_project "Direct link to set_project")

**set\_project(project\_id=None, project\_name=None)**

Set the project of the current task by either specifying a project name or ID

- **Parameters**
  - **project\_id** (`Optional`\[`str`\]) – The ClearML project ID. If provided, `project_name` is ignored.

  - **project\_name** (`Optional`\[`str`\]) – The name of the project. Must match **exactly** one existing project.
- **Return type**

`Optional`\[`bool`\]

- **Returns**

`None` if running as a remote main task, or if a unique project was found.
`False` if the project name matched zero or multiple projects.


* * *

### Task.set\_random\_seed [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#taskset_random_seed "Direct link to Task.set_random_seed")

**_classmethod_ set\_random\_seed(random\_seed)**

Set the default random seed for any new initialized tasks

- **Parameters**

**random\_seed** (`Optional`\[`int`\]) – If `None` or `False`, disable random seed initialization. If `True`, use the default random seed.
Otherwise, use the provided int value for random seed initialization when initializing a new task.

- **Return type**

`None`


* * *

### set\_repo [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#set_repo "Direct link to set_repo")

**set\_repo(repo=None, branch=None, commit=None)**

Specify a repository to attach to the function.
Allow users to execute the task inside the specified repository, enabling them to load modules/script
from the repository. Notice the execution work directory will be the repository root folder.
Supports both git repo URL link, and local repository path (automatically converted into the remote
git/commit as is currently checkout).

Example remote URL: `"https://github.com/user/repo.git"`.

Example local repo copy: `"./repo"` \- will automatically store the remote
repo URL and commit ID based on the locally cloned copy.

When executing remotely, this call will not override the repository data (it is ignored)

- **Parameters**
  - **repo** (`Optional`\[`str`\]) – Optional, remote URL for the repository to use, OR path to local copy of the git repository.
    Use an empty string to clear the repo.
    Example: `"https://github.com/clearml/clearml.git"` or `"~/project/repo"` or `""`

  - **branch** (`Optional`\[`str`\]) – Optional, specify the remote repository branch (Ignored, if local repo path is used).
    Use an empty string to clear the branch.

  - **commit** (`Optional`\[`str`\]) – Optional, specify the repository commit ID (Ignored, if local repo path is used).
    Use an empty string to clear the commit.
- **Return type**

`None`


* * *

### Task.set\_resource\_monitor\_iteration\_timeout [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#taskset_resource_monitor_iteration_timeout "Direct link to Task.set_resource_monitor_iteration_timeout")

**_classmethod_ set\_resource\_monitor\_iteration\_timeout(seconds\_from\_start=30.0, wait\_for\_first\_iteration\_to\_start\_sec=180.0, max\_wait\_for\_first\_iteration\_to\_start\_sec=1800.0)**

Set the `ResourceMonitor` maximum duration (in seconds) to wait until first scalar/plot is reported.
If timeout is reached without any reporting, the `ResourceMonitor` will start reporting machine statistics based
on seconds from Task start time (instead of based on iteration).
Notice! Should be called before `Task.init`.

- **Parameters**
  - **seconds\_from\_start** (`float`) – Maximum number of seconds to wait for scalar/plot reporting before defaulting
    to machine statistics reporting based on seconds from experiment start time

  - **wait\_for\_first\_iteration\_to\_start\_sec** (`float`) – Set the initial time (seconds) to wait for iteration reporting
    to be used as x-axis for the resource monitoring. If timeout exceeds then reverts to `seconds_from_start`

  - **max\_wait\_for\_first\_iteration\_to\_start\_sec** (`float`) – Set the maximum time (seconds) to allow the resource
    monitoring to revert back to iteration reporting x-axis after starting to report `seconds_from_start`
- **Return type**

`bool`

- **Returns**

`True` if success


* * *

### set\_script [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#set_script "Direct link to set_script")

**set\_script(repository=None, branch=None, commit=None, diff=None, working\_dir=None, entry\_point=None, binary=None)**

Set task’s script.

Examples:

```py
task.set_script(

    repository='https://github.com/allegroai/clearml.git,

    branch='main',

    working_dir='examples/reporting',

    entry_point='artifacts.py'

)
```

- **Parameters**
  - **repository** (`Optional`\[`str`\]) – Optional, URL of remote repository. use empty string (`""`) to clear repository entry.

  - **branch** (`Optional`\[`str`\]) – Optional, Select specific repository branch / tag. use empty string (`""`) to clear branch entry.

  - **commit** (`Optional`\[`str`\]) – Optional, set specific git commit id. use empty string (`""`) to clear commit ID entry.

  - **diff** (`Optional`\[`str`\]) – Optional, set “git diff” section. use empty string (`""`) to clear git-diff entry.

  - **working\_dir** (`Optional`\[`str`\]) – Optional, Working directory to launch the script from.

  - **entry\_point** (`Optional`\[`str`\]) – Optional, Path to execute within the repository.

  - **binary** (`Optional`\[`str`\]) – Optional, binary used to launch the entry point
- **Return type**

`None`


* * *

### set\_tags [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#set_tags "Direct link to set_tags")

**set\_tags(tags)**

Set the current Task’s tags. Please note this will overwrite anything that is there already.

- **Parameters**

**tags** ( _Sequence_ _(_ _str_ _)_ ) – Any sequence of tags to set.

- **Return type**

`None`


* * *

### set\_task\_type [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#set_task_type "Direct link to set_task_type")

**set\_task\_type(task\_type)**

Set the `task_type` for the Task.

- **Parameters**

**task\_type** (`str` or `TaskTypes`) – The `task_type` of the Task.

Valid task types:
  - `TaskTypes.training`

  - `TaskTypes.testing`

  - `TaskTypes.inference`

  - `TaskTypes.data_processing`

  - `TaskTypes.application`

  - `TaskTypes.monitor`

  - `TaskTypes.controller`

  - `TaskTypes.optimizer`

  - `TaskTypes.service`

  - `TaskTypes.qc`

  - `TaskTypes.custom`
- **Return type**

`None`


* * *

### set\_user\_properties [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#set_user_properties "Direct link to set_user_properties")

**set\_user\_properties(\*iterables, \*\*properties)**

Set user properties for this task.
A user property can contain the following fields (all of type string):
name / value / description / type

Examples:

```py
task.set_user_properties(backbone='great', stable=True)

task.set_user_properties(backbone={"type": int, "description": "network type", "value": "great"}, )

task.set_user_properties(

    {"name": "backbone", "description": "network type", "value": "great"},

    {"name": "stable", "description": "is stable", "value": True},

)
```

- **Parameters**


  - **iterables** (`Union`\[`Mapping`\[`str`, `Union`\[`str`, `dict`, `None`\]\], `Iterable`\[`dict`\]\]) – Properties iterables, each can be:


    - A dictionary of string key (name) to either a string value (value) or a dict (property details). If the value

is a dict, it must contain a “value” field. For example:

```javascript
{

    "property_name": {"description": "This is a user property", "value": "property value"},

    "another_property_name": {"description": "This is user property", "value": "another value"},

    "yet_another_property_name": "some value"

}
```

    - An iterable of dicts (each representing property details). Each dict must contain a “name” field and a

”value” field. For example:

```javascript
[\
\
    {\
\
        "name": "property_name",\
\
        "description": "This is a user property",\
\
        "value": "property value"\
\
    },\
\
    {\
\
        "name": "another_property_name",\
\
        "description": "This is another user property",\
\
        "value": "another value"\
\
    }\
\
]
```

  - **properties** (`Union`\[`str`, `dict`, `int`, `float`, `None`\]) – Additional properties keyword arguments. Key is the property name, and value can be
    a string (property value) or a dict (property details). If the value is a dict, it must contain a “value”
    field. For example:


> ```javascript
> {
>
>     "property_name": "string as property value",
>
>     "another_property_name": {
>
>         "type": "string",
>
>         "description": "This is user property",
>
>         "value": "another value"
>
>     }
>
> }
> ```

- **Return type**

`bool`


* * *

### setup\_aws\_upload [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#setup_aws_upload "Direct link to setup_aws_upload")

**setup\_aws\_upload(bucket, subdir=None, host=None, key=None, secret=None, token=None, region=None, multipart=True, secure=True, verify=True, profile=None)**

Setup S3 upload options.

- **Parameters**
  - **bucket** (`str`) – AWS bucket name

  - **subdir** (`Optional`\[`str`\]) – Subdirectory in the AWS bucket

  - **host** (`Optional`\[`str`\]) – Hostname. Only required in case a Non-AWS S3 solution such as a local Minio server is used)

  - **key** (`Optional`\[`str`\]) – AWS access key. If not provided, we’ll attempt to obtain the key from the
    configuration file (bucket-specific, than global)

  - **secret** (`Optional`\[`str`\]) – AWS secret key. If not provided, we’ll attempt to obtain the secret from the
    configuration file (bucket-specific, than global)

  - **token** (`Optional`\[`str`\]) – AWS 2FA token

  - **region** (`Optional`\[`str`\]) – Bucket region. Required if the bucket doesn’t reside in the default region (us-east-1)

  - **multipart** (`bool`) – Server supports multipart. Only required when using a Non-AWS S3 solution that doesn’t support
    multipart.

  - **secure** (`bool`) – Server supports HTTPS. Only required when using a Non-AWS S3 solution that only supports HTTPS.

  - **verify** (`bool`) – Whether or not to verify SSL certificates.

  - **profile** (`Optional`\[`str`\]) – The AWS profile
    Only required when using a Non-AWS S3 solution that only supports HTTPS with self-signed certificate.
- **Return type**

`None`


* * *

### setup\_azure\_upload [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#setup_azure_upload "Direct link to setup_azure_upload")

**setup\_azure\_upload(account\_name, account\_key=None, container\_name=None, use\_default\_credential=False)**

Setup Azure upload options.

- **Parameters**
  - **account\_name** (`str`) – Name of the account

  - **account\_key** (`Optional`\[`str`\]) – Secret key used to authenticate the account. Not required when
    `use_default_credential` is True.

  - **container\_name** (`Optional`\[`str`\]) – The name of the blob container to upload to

  - **use\_default\_credential** (`bool`) – If True, authenticate using
    `azure.identity.DefaultAzureCredential` (e.g. managed identity, environment, CLI,
    etc.) instead of an account key. Requires the `azure-identity` package.
- **Return type**

`None`


* * *

### setup\_gcp\_upload [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#setup_gcp_upload "Direct link to setup_gcp_upload")

**setup\_gcp\_upload(bucket, subdir='', project=None, credentials\_json=None, pool\_connections=None, pool\_maxsize=None)**

Setup GCP upload options.

- **Parameters**
  - **bucket** (`str`) – Bucket to upload to

  - **subdir** (`str`) – Subdir in bucket to upload to

  - **project** (`Optional`\[`str`\]) – Project the bucket belongs to

  - **credentials\_json** (`Optional`\[`str`\]) – Path to the JSON file that contains the credentials

  - **pool\_connections** (`Optional`\[`int`\]) – The number of urllib3 connection pools to cache

  - **pool\_maxsize** (`Optional`\[`int`\]) – The maximum number of connections to save in the pool
- **Return type**

`None`


* * *

### started [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#started "Direct link to started")

**started(ignore\_errors=True, force=False)**

The signal that this Task started.

- **Return type**

`Optional`\[`CallResult`\]

- **Parameters**
  - **ignore\_errors** ( _bool_ ) –

  - **force** ( _bool_ ) –

* * *

### status [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#status "Direct link to status")

**property status: str**

The Task’s status. To keep the Task updated.
ClearML reloads the Task status information only, when this value is accessed.

return str: TaskStatusEnum status

- **Return type**

`str`


* * *

### stop\_request [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#stop_request "Direct link to stop_request")

**stop\_request(ignore\_errors=True, force=False, status\_message=None)**

Request a task to stop. this will not change the task status
but mark a request for an agent or SDK to actually stop the Task.
This will trigger the Task’s abort callback, and at the end will
change the task status to stopped and kill the Task’s processes

Notice: calling this on your own Task, will cause
the watchdog to call the `on_abort` callback and kill the process

- **Parameters**
  - **force** ( _bool_ ) – If not `True`, call fails if the task status is not `in_progress`

  - **ignore\_errors** ( _bool_ ) – If `False`, raise exception on error

  - **status\_message** ( _str_ ) – Optional, add status change message to the stop request.
    This message will be stored as `status_message` on the Task’s info panel
- **Return type**

`Optional`\[`CallResult`\]


* * *

### stopped [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#stopped "Direct link to stopped")

**stopped(ignore\_errors=True, force=False, status\_reason=None, status\_message=None)**

The signal that this Task stopped.

- **Return type**

`Optional`\[`CallResult`\]

- **Parameters**
  - **ignore\_errors** ( _bool_ ) –

  - **force** ( _bool_ ) –

  - **status\_reason** ( _Optional_ _\[_ _str_ _\]_ ) –

  - **status\_message** ( _Optional_ _\[_ _str_ _\]_ ) –

* * *

### task\_id [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#task_id "Direct link to task_id")

**property task\_id: str**

Returns the current Task’s ID.

- **Return type**

`str`


* * *

### task\_type [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#task_type "Direct link to task_type")

**property task\_type: str**

Returns the current Task’s type.

Valid task types:

- `TaskTypes.training` (default)

- `TaskTypes.testing`

- `TaskTypes.inference`

- `TaskTypes.data_processing`

- `TaskTypes.application`

- `TaskTypes.monitor`

- `TaskTypes.controller`

- `TaskTypes.optimizer`

- `TaskTypes.service`

- `TaskTypes.qc`

- `TaskTypes.custom`


- **Return type**

`str`


* * *

### unregister\_artifact [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#unregister_artifact "Direct link to unregister_artifact")

**unregister\_artifact(name)**

Unregister (remove) a registered artifact. This removes the artifact from the watch list that ClearML uses
to synchronize artifacts with the **ClearML Server** (backend).

important

Calling this method does not remove the artifact from a Task. It only stops ClearML from
monitoring the artifact.

When this method is called, ClearML immediately takes the last snapshot of the artifact.

- **Return type**

`None`

- **Parameters**

**name** ( _str_ ) –


* * *

### update\_model\_desc [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#update_model_desc "Direct link to update_model_desc")

**update\_model\_desc(new\_model\_desc\_file=None)**

Change the Task’s model description.

- **Return type**

`Response`

- **Parameters**

**new\_model\_desc\_file** ( _Optional_ _\[_ _str_ _\]_ ) –


* * *

### update\_output\_model [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#update_output_model "Direct link to update_output_model")

**update\_output\_model(model\_path, name=None, comment=None, tags=None, model\_name=None, iteration=None, auto\_delete\_file=True)**

Update the Task’s output model weights file. First, ClearML uploads the file to the preconfigured output
destination (see the Task’s `output.destination` property or call the `setup_upload` method),
then ClearML updates the model object associated with the Task. The API call uses the URI
of the uploaded file, and other values provided by additional arguments.

Notice: A local model file will be uploaded to the task’s `output_uri` destination,
If no `output_uri` was specified, the default files-server will be used to store the model file/s.

- **Parameters**
  - **model\_path** (`str`) – A local weights file or folder to be uploaded.
    If remote URI is provided (e.g. `http://` or `s3://` etc.) then the URI is stored as is, without any upload

  - **name** (`Optional`\[`str`\]) – The updated model name.
    If not provided, the name is the model weights file filename without the extension.

  - **comment** (`Optional`\[`str`\]) – The updated model description. (Optional)

  - **tags** (`Optional`\[`Sequence`\[`str`\]\]) – The updated model tags. (Optional)

  - **model\_name** (`Optional`\[`str`\]) – If provided the model name as it will appear in the model artifactory. (Optional)
    Default: Task.name - name

  - **iteration** (`Optional`\[`int`\]) – iteration number for the current stored model (Optional)

  - **auto\_delete\_file** ( _bool_ ) – Delete the temporary file after uploading (Optional)
    - `True` \- Delete (Default)

    - `False` \- Do not delete
- **Return type**

`str`

- **Returns**

The URI of the uploaded weights file.
Notice: upload is done is a background thread, while the function call returns immediately


* * *

### update\_parameters [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#update_parameters "Direct link to update_parameters")

**update\_parameters(\*args, \*\*kwargs)**

Update the parameters for a Task. This method updates a complete group of key-value parameter pairs, but does
not support parameter descriptions (the input is a dictionary of key-value pairs).
Notice the parameter dict is flat:
i.e. `{'Args/param': 'value'}` will set the argument “param” in section “Args” to “value”

- **Parameters**
  - **args** (`dict`) – Positional arguments, which are one or more dictionaries or (key, value) iterable. They are
    merged into a single key-value pair dictionary.

  - **kwargs** (`Any`) – Key-value pairs, merged into the parameters dictionary created from `args`.
- **Return type**

`None`


* * *

### update\_task [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#update_task "Direct link to update_task")

**update\_task(task\_data)**

Update current task with configuration found on the `task_data` dictionary.
See also `export_task()` for retrieving Task configuration.

- **Parameters**

**task\_data** (`dict`) – dictionary with full Task configuration

- **Return type**

`bool`

- **Returns**

`True` if Task update was successful


* * *

### upload\_artifact [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#upload_artifact "Direct link to upload_artifact")

**upload\_artifact(name, artifact\_object, metadata=None, delete\_after\_upload=False, auto\_pickle=None, preview=None, wait\_on\_upload=False, extension\_name=None, serialization\_function=None, retries=0, sort\_keys=True)**

Upload a static artifact to a Task object. The artifact is uploaded in the background.

The currently supported upload (static) artifact types include:

- `str` / `pathlib2.Path` \- A path to artifact file. If a wildcard or a folder is specified, then ClearML
creates and uploads a ZIP file.

- dict - ClearML stores a dictionary as `.json` (or see `extension_name`) file and uploads it.

- `pandas.DataFrame` \- ClearML stores a `pandas.DataFrame` as `.csv.gz` (compressed CSV)
(or see `extension_name`) file and uploads it.

- `numpy.ndarray` \- ClearML stores a `numpy.ndarray` as `.npz` (or see `extension_name`) file and uploads it.

- `PIL.Image`\- ClearML stores a PIL.Image as `.png` (or see `extension_name`) file and uploads it.

- Any - If called with `auto_pickle=True`, the object will be pickled and uploaded.


- **Parameters**


  - **name** (`str`) – The artifact name.

warning

If an artifact with the same name was previously uploaded, then it is overwritten.

  - **artifact\_object** (`Union`\[`str`, `Mapping`, `ForwardRef`, `ndarray`, `ForwardRef`, `Any`\]) – The artifact object.

  - **metadata** (`Optional`\[`Mapping`\]) – A dictionary of key-value pairs for any metadata. This dictionary appears with the
    experiment in the **ClearML Web-App (UI)**, **ARTIFACTS** tab.

  - **delete\_after\_upload** ( _bool_ ) – After the upload, delete the local copy of the artifact
    - `True` \- Delete the local copy of the artifact.

    - `False` \- Do not delete. (default)
  - **auto\_pickle** (`Optional`\[`bool`\]) – If `True` and the `artifact_object` is not one of the following types:
    `pathlib2.Path`, dict, `pandas.DataFrame`, `numpy.ndarray`, `PIL.Image`, URL (`str`), `local_file` (`str`),
    the `artifact_object` will be pickled and uploaded as pickle file artifact (with file extension `.pkl`).
    If set to `None` (default), the `sdk.development.artifacts.auto_pickle` configuration value will be used.

  - **preview** (`Any`) – The artifact preview

  - **wait\_on\_upload** (`bool`) – Whether the upload should be synchronous, forcing the upload to complete
    before continuing.

  - **extension\_name** (`Optional`\[`str`\]) – File extension which indicates the format the artifact should be stored as.

    The following are supported, depending on the artifact type (default value applies when `extension_name` is `None`):
    - Any - `.pkl` if passed supersedes any other serialization type, and always pickles the object

    - dict - `.json`, `.yaml` (default `.json`)

    - `pandas.DataFrame` \- `.csv.gz`, `.parquet`, `.feather`, `.pickle` (default `.csv.gz`)

    - `numpy.ndarray` \- `.npz`, `.csv.gz` (default `.npz`)

    - PIL.Image - whatever extensions PIL supports (default `.png`)

    - In case the `serialization_function` argument is set - any extension is supported
  - **serialization\_function** (`Optional`\[`Callable`\[\[`Any`\], `Union`\[`bytes`, `bytearray`\]\]\]) – A serialization function that takes one
    parameter of any type which is the object to be serialized. The function should return
    a `bytes` or `bytearray` object, which represents the serialized object. Note that the object will be
    immediately serialized using this function, thus other serialization methods will not be used
    (e.g. `pandas.DataFrame.to_csv`), even if possible. To deserialize this artifact when getting
    it using the `Artifact.get` method, use its `deserialization_function` argument.

  - **retries** (`int`) – Number of retries before failing to upload artifact. If 0, the upload is not retried

  - **sort\_keys** (`bool`) – If `True` (default), sort the keys of the artifact if it is yaml/json serializable.
    Otherwise, don’t sort the keys. Ignored if the artifact is not yaml/json serializable.
- **Return type**

`bool`

- **Returns**

The status of the upload.
  - `True` \- Upload succeeded.

  - `False` \- Upload failed.
- **Raise**

If the artifact object type is not supported, raise a `ValueError`.


* * *

### wait\_for\_external\_endpoint [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#wait_for_external_endpoint "Direct link to wait_for_external_endpoint")

**wait\_for\_external\_endpoint(wait\_interval\_seconds=3.0, wait\_timeout\_seconds=90.0, protocol='http', endpoint\_name=None)**

Wait for an external endpoint to be assigned

- **Parameters**
  - **wait\_interval\_seconds** (`float`) – The poll frequency when waiting for the endpoint

  - **wait\_timeout\_seconds** (`float`) – If this timeout is exceeded while waiting for the endpoint,
    the method will no longer wait

  - **protocol** (`Optional`\[`str`\]) – `http` or `tcp`. Wait for an endpoint to be assigned based on the protocol.
    If `None`, wait for all supported protocols

  - **endpoint\_name** (`Optional`\[`str`\]) – Optional identifier of the endpoint to wait on.
- **Return type**

`Union`\[`Dict`, `None`, `List`\[`Optional`\[`Dict`\]\]\]

- **Returns**

If no endpoint could be found while waiting, this method returns `None`. If a protocol has been specified, it returns a dictionary containing the following values:
  - `endpoint` \- raw endpoint. One might need to authenticate in order to use this endpoint

  - `browser_endpoint` \- endpoint to be used in browser. Authentication will be handled via the browser

  - `port` \- the port exposed by the application

  - `protocol` \- the protocol used by the endpoint

  - `name` \- the identifier used for this endpoint.
    If protocol is not specified, it returns a list of dictionaries containing the values above,
    for each protocol requested and waited

* * *

### wait\_for\_status [​](https://clear.ml/docs/latest/docs/references/sdk/task/\#wait_for_status "Direct link to wait_for_status")

**wait\_for\_status(status=(TaskTypes.completed, TaskTypes.stopped, TaskTypes.closed), raise\_on\_status=(TaskTypes.failed,), check\_interval\_sec=60.0)**

Wait for a task to reach a defined status.

- **Parameters**
  - **status** (`Iterable`\[`TaskStatusEnum`\]) – Status to wait for. Defaults to (‘completed’, ‘stopped’, ‘closed’, )

  - **raise\_on\_status** (`Optional`\[`Iterable`\[`TaskStatusEnum`\]\]) – Raise RuntimeError if the status of the tasks matches one of these values.
    Defaults to (‘failed’).

  - **check\_interval\_sec** (`float`) – Interval in seconds between two checks. Defaults to 60 seconds.
- **Raise**

RuntimeError if the status is one of `{raise_on_status}`.

- **Return type**

`None`


- [_class_ Task(private=None, \*\*kwargs)](https://clear.ml/docs/latest/docs/references/sdk/task/#class-taskprivatenone-kwargs)
  - [Task.add\_requirements](https://clear.ml/docs/latest/docs/references/sdk/task/#taskadd_requirements)
  - [add\_tags](https://clear.ml/docs/latest/docs/references/sdk/task/#add_tags)
  - [artifacts](https://clear.ml/docs/latest/docs/references/sdk/task/#artifacts)
  - [cache\_dir](https://clear.ml/docs/latest/docs/references/sdk/task/#cache_dir)
  - [Task.clone](https://clear.ml/docs/latest/docs/references/sdk/task/#taskclone)
  - [close](https://clear.ml/docs/latest/docs/references/sdk/task/#close)
  - [comment](https://clear.ml/docs/latest/docs/references/sdk/task/#comment)
  - [completed](https://clear.ml/docs/latest/docs/references/sdk/task/#completed)
  - [connect](https://clear.ml/docs/latest/docs/references/sdk/task/#connect)
  - [connect\_configuration](https://clear.ml/docs/latest/docs/references/sdk/task/#connect_configuration)
  - [connect\_label\_enumeration](https://clear.ml/docs/latest/docs/references/sdk/task/#connect_label_enumeration)
  - [Task.create](https://clear.ml/docs/latest/docs/references/sdk/task/#taskcreate)
  - [create\_function\_task](https://clear.ml/docs/latest/docs/references/sdk/task/#create_function_task)
  - [Task.current\_task](https://clear.ml/docs/latest/docs/references/sdk/task/#taskcurrent_task)
  - [data](https://clear.ml/docs/latest/docs/references/sdk/task/#data)
  - [Task.debug\_simulate\_remote\_task](https://clear.ml/docs/latest/docs/references/sdk/task/#taskdebug_simulate_remote_task)
  - [delete](https://clear.ml/docs/latest/docs/references/sdk/task/#delete)
  - [delete\_artifacts](https://clear.ml/docs/latest/docs/references/sdk/task/#delete_artifacts)
  - [delete\_parameter](https://clear.ml/docs/latest/docs/references/sdk/task/#delete_parameter)
  - [delete\_user\_properties](https://clear.ml/docs/latest/docs/references/sdk/task/#delete_user_properties)
  - [Task.dequeue](https://clear.ml/docs/latest/docs/references/sdk/task/#taskdequeue)
  - [Task.enqueue](https://clear.ml/docs/latest/docs/references/sdk/task/#taskenqueue)
  - [execute\_remotely](https://clear.ml/docs/latest/docs/references/sdk/task/#execute_remotely)
  - [export\_task](https://clear.ml/docs/latest/docs/references/sdk/task/#export_task)
  - [flush](https://clear.ml/docs/latest/docs/references/sdk/task/#flush)
  - [Task.force\_requirements\_env\_freeze](https://clear.ml/docs/latest/docs/references/sdk/task/#taskforce_requirements_env_freeze)
  - [Task.force\_store\_standalone\_script](https://clear.ml/docs/latest/docs/references/sdk/task/#taskforce_store_standalone_script)
  - [Task.get\_all](https://clear.ml/docs/latest/docs/references/sdk/task/#taskget_all)
  - [get\_all\_reported\_scalars](https://clear.ml/docs/latest/docs/references/sdk/task/#get_all_reported_scalars)
  - [get\_archived](https://clear.ml/docs/latest/docs/references/sdk/task/#get_archived)
  - [get\_base\_docker](https://clear.ml/docs/latest/docs/references/sdk/task/#get_base_docker)
  - [Task.get\_by\_name](https://clear.ml/docs/latest/docs/references/sdk/task/#taskget_by_name)
  - [get\_configuration\_object](https://clear.ml/docs/latest/docs/references/sdk/task/#get_configuration_object)
  - [get\_configuration\_object\_as\_dict](https://clear.ml/docs/latest/docs/references/sdk/task/#get_configuration_object_as_dict)
  - [get\_configuration\_objects](https://clear.ml/docs/latest/docs/references/sdk/task/#get_configuration_objects)
  - [get\_dataviews](https://clear.ml/docs/latest/docs/references/sdk/task/#get_dataviews)
  - [get\_debug\_samples](https://clear.ml/docs/latest/docs/references/sdk/task/#get_debug_samples)
  - [get\_executed\_queue](https://clear.ml/docs/latest/docs/references/sdk/task/#get_executed_queue)
  - [get\_http\_router](https://clear.ml/docs/latest/docs/references/sdk/task/#get_http_router)
  - [get\_initial\_iteration](https://clear.ml/docs/latest/docs/references/sdk/task/#get_initial_iteration)
  - [get\_label\_num\_description](https://clear.ml/docs/latest/docs/references/sdk/task/#get_label_num_description)
  - [get\_labels\_enumeration](https://clear.ml/docs/latest/docs/references/sdk/task/#get_labels_enumeration)
  - [get\_last\_iteration](https://clear.ml/docs/latest/docs/references/sdk/task/#get_last_iteration)
  - [get\_last\_scalar\_metrics](https://clear.ml/docs/latest/docs/references/sdk/task/#get_last_scalar_metrics)
  - [get\_logger](https://clear.ml/docs/latest/docs/references/sdk/task/#get_logger)
  - [get\_model\_config\_dict](https://clear.ml/docs/latest/docs/references/sdk/task/#get_model_config_dict)
  - [get\_model\_config\_text](https://clear.ml/docs/latest/docs/references/sdk/task/#get_model_config_text)
  - [get\_model\_design](https://clear.ml/docs/latest/docs/references/sdk/task/#get_model_design)
  - [get\_models](https://clear.ml/docs/latest/docs/references/sdk/task/#get_models)
  - [Task.get\_num\_enqueued\_tasks](https://clear.ml/docs/latest/docs/references/sdk/task/#taskget_num_enqueued_tasks)
  - [get\_num\_of\_classes](https://clear.ml/docs/latest/docs/references/sdk/task/#get_num_of_classes)
  - [get\_offline\_mode\_folder](https://clear.ml/docs/latest/docs/references/sdk/task/#get_offline_mode_folder)
  - [get\_output\_destination](https://clear.ml/docs/latest/docs/references/sdk/task/#get_output_destination)
  - [get\_output\_log\_web\_page](https://clear.ml/docs/latest/docs/references/sdk/task/#get_output_log_web_page)
  - [get\_parameter](https://clear.ml/docs/latest/docs/references/sdk/task/#get_parameter)
  - [get\_parameters](https://clear.ml/docs/latest/docs/references/sdk/task/#get_parameters)
  - [get\_parameters\_as\_dict](https://clear.ml/docs/latest/docs/references/sdk/task/#get_parameters_as_dict)
  - [get\_progress](https://clear.ml/docs/latest/docs/references/sdk/task/#get_progress)
  - [Task.get\_project\_id](https://clear.ml/docs/latest/docs/references/sdk/task/#taskget_project_id)
  - [get\_project\_name](https://clear.ml/docs/latest/docs/references/sdk/task/#get_project_name)
  - [get\_project\_object](https://clear.ml/docs/latest/docs/references/sdk/task/#get_project_object)
  - [Task.get\_projects](https://clear.ml/docs/latest/docs/references/sdk/task/#taskget_projects)
  - [get\_registered\_artifacts](https://clear.ml/docs/latest/docs/references/sdk/task/#get_registered_artifacts)
  - [get\_reported\_console\_output](https://clear.ml/docs/latest/docs/references/sdk/task/#get_reported_console_output)
  - [get\_reported\_plots](https://clear.ml/docs/latest/docs/references/sdk/task/#get_reported_plots)
  - [get\_reported\_scalars](https://clear.ml/docs/latest/docs/references/sdk/task/#get_reported_scalars)
  - [get\_reported\_single\_value](https://clear.ml/docs/latest/docs/references/sdk/task/#get_reported_single_value)
  - [get\_reported\_single\_values](https://clear.ml/docs/latest/docs/references/sdk/task/#get_reported_single_values)
  - [get\_requirements](https://clear.ml/docs/latest/docs/references/sdk/task/#get_requirements)
  - [get\_script](https://clear.ml/docs/latest/docs/references/sdk/task/#get_script)
  - [get\_status](https://clear.ml/docs/latest/docs/references/sdk/task/#get_status)
  - [get\_status\_message](https://clear.ml/docs/latest/docs/references/sdk/task/#get_status_message)
  - [get\_tags](https://clear.ml/docs/latest/docs/references/sdk/task/#get_tags)
  - [Task.get\_task](https://clear.ml/docs/latest/docs/references/sdk/task/#taskget_task)
  - [Task.get\_task\_output\_log\_web\_page](https://clear.ml/docs/latest/docs/references/sdk/task/#taskget_task_output_log_web_page)
  - [Task.get\_tasks](https://clear.ml/docs/latest/docs/references/sdk/task/#taskget_tasks)
  - [get\_user\_properties](https://clear.ml/docs/latest/docs/references/sdk/task/#get_user_properties)
  - [Task.ignore\_requirements](https://clear.ml/docs/latest/docs/references/sdk/task/#taskignore_requirements)
  - [Task.import\_offline\_session](https://clear.ml/docs/latest/docs/references/sdk/task/#taskimport_offline_session)
  - [Task.import\_task](https://clear.ml/docs/latest/docs/references/sdk/task/#taskimport_task)
  - [Task.init](https://clear.ml/docs/latest/docs/references/sdk/task/#taskinit)
  - [input\_models\_id](https://clear.ml/docs/latest/docs/references/sdk/task/#input_models_id)
  - [is\_current\_task](https://clear.ml/docs/latest/docs/references/sdk/task/#is_current_task)
  - [is\_main\_task](https://clear.ml/docs/latest/docs/references/sdk/task/#is_main_task)
  - [Task.is\_offline](https://clear.ml/docs/latest/docs/references/sdk/task/#taskis_offline)
  - [labels\_stats](https://clear.ml/docs/latest/docs/references/sdk/task/#labels_stats)
  - [last\_worker](https://clear.ml/docs/latest/docs/references/sdk/task/#last_worker)
  - [launch\_multi\_node](https://clear.ml/docs/latest/docs/references/sdk/task/#launch_multi_node)
  - [list\_external\_endpoints](https://clear.ml/docs/latest/docs/references/sdk/task/#list_external_endpoints)
  - [log](https://clear.ml/docs/latest/docs/references/sdk/task/#log)
  - [logger](https://clear.ml/docs/latest/docs/references/sdk/task/#logger)
  - [mark\_completed](https://clear.ml/docs/latest/docs/references/sdk/task/#mark_completed)
  - [mark\_failed](https://clear.ml/docs/latest/docs/references/sdk/task/#mark_failed)
  - [mark\_started](https://clear.ml/docs/latest/docs/references/sdk/task/#mark_started)
  - [mark\_stop\_request](https://clear.ml/docs/latest/docs/references/sdk/task/#mark_stop_request)
  - [mark\_stopped](https://clear.ml/docs/latest/docs/references/sdk/task/#mark_stopped)
  - [metrics\_manager](https://clear.ml/docs/latest/docs/references/sdk/task/#metrics_manager)
  - [models](https://clear.ml/docs/latest/docs/references/sdk/task/#models)
  - [move\_to\_project](https://clear.ml/docs/latest/docs/references/sdk/task/#move_to_project)
  - [name](https://clear.ml/docs/latest/docs/references/sdk/task/#name)
  - [output\_models\_id](https://clear.ml/docs/latest/docs/references/sdk/task/#output_models_id)
  - [output\_uri](https://clear.ml/docs/latest/docs/references/sdk/task/#output_uri)
  - [parent](https://clear.ml/docs/latest/docs/references/sdk/task/#parent)
  - [project](https://clear.ml/docs/latest/docs/references/sdk/task/#project)
  - [publish](https://clear.ml/docs/latest/docs/references/sdk/task/#publish)
  - [publish\_on\_completion](https://clear.ml/docs/latest/docs/references/sdk/task/#publish_on_completion)
  - [Task.query\_tasks](https://clear.ml/docs/latest/docs/references/sdk/task/#taskquery_tasks)
  - [register\_abort\_callback](https://clear.ml/docs/latest/docs/references/sdk/task/#register_abort_callback)
  - [register\_artifact](https://clear.ml/docs/latest/docs/references/sdk/task/#register_artifact)
  - [reload](https://clear.ml/docs/latest/docs/references/sdk/task/#reload)
  - [remove\_input\_models](https://clear.ml/docs/latest/docs/references/sdk/task/#remove_input_models)
  - [remove\_tags](https://clear.ml/docs/latest/docs/references/sdk/task/#remove_tags)
  - [rename](https://clear.ml/docs/latest/docs/references/sdk/task/#rename)
  - [request\_external\_endpoint](https://clear.ml/docs/latest/docs/references/sdk/task/#request_external_endpoint)
  - [reset](https://clear.ml/docs/latest/docs/references/sdk/task/#reset)
  - [running\_locally](https://clear.ml/docs/latest/docs/references/sdk/task/#running_locally)
  - [save\_exec\_model\_design\_file](https://clear.ml/docs/latest/docs/references/sdk/task/#save_exec_model_design_file)
  - [session](https://clear.ml/docs/latest/docs/references/sdk/task/#session)
  - [set\_archived](https://clear.ml/docs/latest/docs/references/sdk/task/#set_archived)
  - [set\_artifacts](https://clear.ml/docs/latest/docs/references/sdk/task/#set_artifacts)
  - [set\_base\_docker](https://clear.ml/docs/latest/docs/references/sdk/task/#set_base_docker)
  - [set\_comment](https://clear.ml/docs/latest/docs/references/sdk/task/#set_comment)
  - [set\_configuration\_object](https://clear.ml/docs/latest/docs/references/sdk/task/#set_configuration_object)
  - [Task.set\_credentials](https://clear.ml/docs/latest/docs/references/sdk/task/#taskset_credentials)
  - [set\_dataview](https://clear.ml/docs/latest/docs/references/sdk/task/#set_dataview)
  - [set\_initial\_iteration](https://clear.ml/docs/latest/docs/references/sdk/task/#set_initial_iteration)
  - [set\_input\_model](https://clear.ml/docs/latest/docs/references/sdk/task/#set_input_model)
  - [set\_model\_config](https://clear.ml/docs/latest/docs/references/sdk/task/#set_model_config)
  - [set\_model\_label\_enumeration](https://clear.ml/docs/latest/docs/references/sdk/task/#set_model_label_enumeration)
  - [set\_name](https://clear.ml/docs/latest/docs/references/sdk/task/#set_name)
  - [Task.set\_offline](https://clear.ml/docs/latest/docs/references/sdk/task/#taskset_offline)
  - [set\_packages](https://clear.ml/docs/latest/docs/references/sdk/task/#set_packages)
  - [set\_parameter](https://clear.ml/docs/latest/docs/references/sdk/task/#set_parameter)
  - [set\_parameters](https://clear.ml/docs/latest/docs/references/sdk/task/#set_parameters)
  - [set\_parameters\_as\_dict](https://clear.ml/docs/latest/docs/references/sdk/task/#set_parameters_as_dict)
  - [set\_parent](https://clear.ml/docs/latest/docs/references/sdk/task/#set_parent)
  - [set\_progress](https://clear.ml/docs/latest/docs/references/sdk/task/#set_progress)
  - [set\_project](https://clear.ml/docs/latest/docs/references/sdk/task/#set_project)
  - [Task.set\_random\_seed](https://clear.ml/docs/latest/docs/references/sdk/task/#taskset_random_seed)
  - [set\_repo](https://clear.ml/docs/latest/docs/references/sdk/task/#set_repo)
  - [Task.set\_resource\_monitor\_iteration\_timeout](https://clear.ml/docs/latest/docs/references/sdk/task/#taskset_resource_monitor_iteration_timeout)
  - [set\_script](https://clear.ml/docs/latest/docs/references/sdk/task/#set_script)
  - [set\_tags](https://clear.ml/docs/latest/docs/references/sdk/task/#set_tags)
  - [set\_task\_type](https://clear.ml/docs/latest/docs/references/sdk/task/#set_task_type)
  - [set\_user\_properties](https://clear.ml/docs/latest/docs/references/sdk/task/#set_user_properties)
  - [setup\_aws\_upload](https://clear.ml/docs/latest/docs/references/sdk/task/#setup_aws_upload)
  - [setup\_azure\_upload](https://clear.ml/docs/latest/docs/references/sdk/task/#setup_azure_upload)
  - [setup\_gcp\_upload](https://clear.ml/docs/latest/docs/references/sdk/task/#setup_gcp_upload)
  - [started](https://clear.ml/docs/latest/docs/references/sdk/task/#started)
  - [status](https://clear.ml/docs/latest/docs/references/sdk/task/#status)
  - [stop\_request](https://clear.ml/docs/latest/docs/references/sdk/task/#stop_request)
  - [stopped](https://clear.ml/docs/latest/docs/references/sdk/task/#stopped)
  - [task\_id](https://clear.ml/docs/latest/docs/references/sdk/task/#task_id)
  - [task\_type](https://clear.ml/docs/latest/docs/references/sdk/task/#task_type)
  - [unregister\_artifact](https://clear.ml/docs/latest/docs/references/sdk/task/#unregister_artifact)
  - [update\_model\_desc](https://clear.ml/docs/latest/docs/references/sdk/task/#update_model_desc)
  - [update\_output\_model](https://clear.ml/docs/latest/docs/references/sdk/task/#update_output_model)
  - [update\_parameters](https://clear.ml/docs/latest/docs/references/sdk/task/#update_parameters)
  - [update\_task](https://clear.ml/docs/latest/docs/references/sdk/task/#update_task)
  - [upload\_artifact](https://clear.ml/docs/latest/docs/references/sdk/task/#upload_artifact)
  - [wait\_for\_external\_endpoint](https://clear.ml/docs/latest/docs/references/sdk/task/#wait_for_external_endpoint)
  - [wait\_for\_status](https://clear.ml/docs/latest/docs/references/sdk/task/#wait_for_status)