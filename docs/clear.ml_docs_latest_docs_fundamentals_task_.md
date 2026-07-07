---
url: "https://clear.ml/docs/latest/docs/fundamentals/task/"
title: "Tasks | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/fundamentals/task/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

**ClearML Task** lies at the heart of ClearML's experiment manager.

A Task is a single code execution session, which can represent an experiment, a step in a workflow, a workflow controller,
or any custom implementation you choose.

To transform an existing script into a **ClearML Task**, call the [`Task.init()`](https://clear.ml/docs/latest/docs/references/sdk/task#taskinit) method
and specify a task name and its project. This creates a Task object that automatically captures code execution
information as well as execution outputs.

All the information captured by a task is by default uploaded to the [ClearML Server](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server),
and it can be visualized in the [ClearML WebApp (UI)](https://clear.ml/docs/latest/docs/webapp/webapp_overview). ClearML can also be configured to upload
model checkpoints, artifacts, and charts to cloud storage (see [Storage](https://clear.ml/docs/latest/docs/integrations/storage)). Additionally,
you can work with tasks in Offline Mode, in which all information is saved in a local folder (see
[Storing Task Data Offline](https://clear.ml/docs/latest/docs/guides/set_offline)).

Tasks are grouped into a [project](https://clear.ml/docs/latest/docs/fundamentals/projects) hierarchical structure, similar to file folders. Users can decide
how to group tasks, though different models or objectives are usually grouped into different projects.

Tasks can be accessed and utilized with code. [Access a task](https://clear.ml/docs/latest/docs/clearml_sdk/task_sdk#accessing-tasks) by
specifying project name and task name combination or by a unique ID.

You can create copies of a task ( [clone](https://clear.ml/docs/latest/docs/webapp/webapp_exp_reproducing)) then execute them with
[ClearML Agent](https://clear.ml/docs/latest/docs/clearml_agent). When an agent executes a task, it uses the specified configuration to:

- Install required Python packages
- Apply code patches
- Set hyperparameter and run-time configuration values

Modifying a task clone's configuration will have the executing ClearML agent override the original values:

- Modified package requirements will have the task script run with updated packages
- Modified recorded command line arguments will have the ClearML agent inject the new values in their stead
- Code-level configuration instrumented with [`Task.connect`](https://clear.ml/docs/latest/docs/references/sdk/task#connect) will be overridden by
modified hyperparameters

![Task](https://clear.ml/docs/latest/assets/images/fundamentals_task-3378428922f237c6064c1b6d52b8675c.png#light-mode-only)![Task](https://clear.ml/docs/latest/assets/images/fundamentals_task_dark-49bafcfadbd7aaef0ffc4d0df4fad22f.png#dark-mode-only)

## Task Sections [​](https://clear.ml/docs/latest/docs/fundamentals/task/\#task-sections "Direct link to Task Sections")

The sections of ClearML Task are made up of the information that a task captures and stores, which consists of code
execution details and execution outputs. This information is used for tracking
and visualizing results, reproducing, tuning, and comparing tasks, and executing workflows.

The captured [code execution information](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual#execution) includes:

- Git information
- Uncommitted code modifications
- Python environment
- [Execution configuration](https://clear.ml/docs/latest/docs/fundamentals/task/#execution-configuration) and hyperparameters

The captured [execution output](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual#task-results) includes:

- [Console output](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual#console)
- [Scalars](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual#scalars)
- [Plots](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual#plots)
- [Debug samples](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual#debug-samples)
- [Models](https://clear.ml/docs/latest/docs/fundamentals/models)

For a more in-depth description of each task section, see [Tracking Tasks and Visualizing Results](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual).

### Execution Configuration [​](https://clear.ml/docs/latest/docs/fundamentals/task/\#execution-configuration "Direct link to Execution Configuration")

ClearML logs a task's hyperparameters specified as command line arguments, environment or code level variables. This
allows tasks to be reproduced, and their hyperparameters and results can be saved and compared, which is key to
understanding model behavior.

Hyperparameters can be added from anywhere in your code, and ClearML provides multiple ways to log them. If you specify
your parameters using popular Python packages, such as [argparse](https://docs.python.org/3/library/argparse.html) and
[click](https://click.palletsprojects.com/), all you need to do is [initialize](https://clear.ml/docs/latest/docs/references/sdk/task#taskinit) a task, and
ClearML will automatically log the parameters. ClearML also provides methods to explicitly report parameters.

When executing a task through a ClearML agent, the ClearML instrumentation of your code allows for using the ClearML UI
to override the original specified values of your parameters.

See [Hyperparameters](https://clear.ml/docs/latest/docs/fundamentals/hyperparameters) for more information.

### Artifacts [​](https://clear.ml/docs/latest/docs/fundamentals/task/\#artifacts "Direct link to Artifacts")

ClearML allows easy storage of tasks' output products as artifacts that can later be accessed easily and used,
through the [web UI](https://clear.ml/docs/latest/docs/webapp/webapp_overview) or programmatically.

ClearML provides methods to easily track files generated throughout your tasks' execution such as:

- Numpy objects
- Pandas DataFrames
- PIL
- Files and folders
- Python objects
- and more!

Most importantly, ClearML also logs tasks' input and output models as well as interim model snapshots (see
[Models](https://clear.ml/docs/latest/docs/fundamentals/models)).

#### Logging Artifacts [​](https://clear.ml/docs/latest/docs/fundamentals/task/\#logging-artifacts "Direct link to Logging Artifacts")

ClearML provides an explicit logging interface that supports manually reporting a variety of artifacts. Any type of
artifact can be logged to a task using [`Task.upload_artifact()`](https://clear.ml/docs/latest/docs/references/sdk/task#upload_artifact).
See more details in the [Artifacts Reporting example](https://clear.ml/docs/latest/docs/guides/reporting/artifacts).

ClearML can be configured to upload artifacts to any of the supported types of storage, which include local and shared
folders, AWS S3 buckets, Google Cloud Storage, and Azure Storage. For more information, see [Storage](https://clear.ml/docs/latest/docs/integrations/storage).

Debug Sample Storage

Debug samples are handled differently, see [`Logger.set_default_upload_destination`](https://clear.ml/docs/latest/docs/references/sdk/logger#set_default_upload_destination).

#### Accessing Artifacts [​](https://clear.ml/docs/latest/docs/fundamentals/task/\#accessing-artifacts "Direct link to Accessing Artifacts")

Artifacts that have been logged can be accessed by other tasks [through the task](https://clear.ml/docs/latest/docs/clearml_sdk/task_sdk#accessing-tasks)
they are attached to, and then retrieving the artifact with one of its following methods:

- `get_local_copy()` \- caches the files for later use and returns a path to the cached file.
- `get()` \- use for Python objects. The method that returns the Python object.

See more details in the [Using Artifacts example](https://github.com/clearml/clearml/blob/master/examples/reporting/using_artifacts_example.py).

## Task Types [​](https://clear.ml/docs/latest/docs/fundamentals/task/\#task-types "Direct link to Task Types")

Tasks have a _type_ attribute, which denotes their purpose. This helps to further
organize projects and ensure tasks are easy to [search and find](https://clear.ml/docs/latest/docs/clearml_sdk/task_sdk#querying--searching-tasks).
Available task types are:

- _training_ (default) - Training a model
- _testing_ \- Testing a component, for example model performance
- _inference_ \- Model inference job (e.g. offline / batch model execution)
- _controller_ \- A task that lays out the logic for other tasks' interactions, manual or automatic (e.g. a pipeline
controller)
- _optimizer_ \- A specific type of controller for optimization tasks (e.g. [hyperparameter optimization](https://clear.ml/docs/latest/docs/getting_started/hpo))
- _service_ \- Long lasting or recurring service (e.g. server cleanup, auto ingress, sync services etc.)
- _monitor_ \- A specific type of service for monitoring
- _application_ \- A task implementing custom applicative logic, like [autoscaler](https://clear.ml/docs/latest/docs/guides/services/aws_autoscaler)
or [clearml-session](https://clear.ml/docs/latest/docs/apps/clearml_session)
- _data\_processing_ \- Any data ingress / preprocessing (see [ClearML Data](https://clear.ml/docs/latest/docs/clearml_data/))
- _qc_ \- Quality Control (e.g. evaluating model performance vs. blind dataset)
- _custom_ \- A task not matching any of the above

## Task Lifecycle [​](https://clear.ml/docs/latest/docs/fundamentals/task/\#task-lifecycle "Direct link to Task Lifecycle")

ClearML Tasks are created in one of the following methods:

- Manually running code that is instrumented with the ClearML SDK and invokes [`Task.init`](https://clear.ml/docs/latest/docs/references/sdk/task#taskinit).
- Cloning an existing task.
- Creating a task via CLI using [clearml-task](https://clear.ml/docs/latest/docs/apps/clearml_task).

### Logging Task Information [​](https://clear.ml/docs/latest/docs/fundamentals/task/\#logging-task-information "Direct link to Logging Task Information")

![Logging ClearML Task information diagram](https://clear.ml/docs/latest/assets/images/clearml_logging_diagram-7d33d5008395a46583da5b5d6f323281.png)

The above diagram describes how execution information is recorded when running code instrumented with ClearML:

1. Once a ClearML Task is initialized, ClearML automatically logs the complete environment information
including:
   - Source code
   - Python environment
   - Configuration parameters
2. As the execution progresses, any outputs produced are recorded including:
   - Console logs
   - Metrics and graphs
   - Models and other artifacts
3. Once the script terminates, the task will change its status to either `Completed`, `Failed`, or `Aborted` (see [Task states](https://clear.ml/docs/latest/docs/fundamentals/task/#task-states) below).

All information logged can be viewed in the [task details UI](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual).

### Cloning Tasks [​](https://clear.ml/docs/latest/docs/fundamentals/task/\#cloning-tasks "Direct link to Cloning Tasks")

![ClearML Task lifecycle diagram](https://clear.ml/docs/latest/assets/images/clearml_task_life_cycle_diagram-acfcd55d0b1eaedde59502912ca0bd11.png)

The above diagram demonstrates how a previously run task can be used as a baseline for experimentation:

1. A previously run task is cloned, creating a new task, in `Draft` mode (see [Task states](https://clear.ml/docs/latest/docs/fundamentals/task/#task-states) below).


The new task retains all the source task's configuration. The original task's outputs are not carried over.
2. The new task's configuration is modified to reflect the desired parameters for the new execution.
3. The new task is enqueued for execution.
4. A `clearml-agent` servicing the queue pulls the new task and executes it (where ClearML again logs all the execution outputs).

## Task States [​](https://clear.ml/docs/latest/docs/fundamentals/task/\#task-states "Direct link to Task States")

The state of a task represents its stage in the task lifecycle. It indicates whether the task is read-write (editable) or
read-only. For each state, a state transition indicates which actions can be performed on a task, and the new state
after performing an action.

The following table describes the task states and state transitions.

| State | Description / Usage | State Transition |
| --- | --- | --- |
| _Draft_ | The task is editable. Only tasks in _Draft_ mode are editable. The task is not running locally or remotely. | If the task is enqueued for a [worker](https://clear.ml/docs/latest/docs/fundamentals/agents_and_queues) to fetch and execute, the state becomes _Pending_. |
| _Pending_ | The task was enqueued and is waiting in a queue for a worker to fetch and execute it. | If the task is dequeued, the state becomes _Draft_. |
| _Running_ | The task is running locally or remotely. | If the task is manually or programmatically terminated, the state becomes _Aborted_. |
| _Completed_ | The task ran and terminated successfully. | If the task is reset or cloned, the state of the cloned task or newly cloned task becomes _Draft_. Resetting deletes the logs and output of a previous run. Cloning creates an exact, editable copy. |
| _Failed_ | The task ran and terminated with an error. | The same as _Completed_. |
| _Aborted_ | The task ran, and was manually or programmatically terminated. The server's [non-responsive task monitor](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_config#non-responsive-task-watchdog) aborts a task automatically after no activity has been detected for a specified time interval (configurable). | The same as _Completed_. |
| _Published_ | The task is read-only. Publish a task to prevent changes to its inputs and outputs. | A _Published_ task cannot be reset. If it is cloned, the state of the newly cloned task becomes _Draft_. |

## SDK Interface [​](https://clear.ml/docs/latest/docs/fundamentals/task/\#sdk-interface "Direct link to SDK Interface")

See the [Task SDK interface](https://clear.ml/docs/latest/docs/clearml_sdk/task_sdk) for an overview for using the most basic Pythonic methods of the `Task` class.
See the [Task reference page](https://clear.ml/docs/latest/docs/references/sdk/task) for a complete list of available methods.

- [Task Sections](https://clear.ml/docs/latest/docs/fundamentals/task/#task-sections)
  - [Execution Configuration](https://clear.ml/docs/latest/docs/fundamentals/task/#execution-configuration)
  - [Artifacts](https://clear.ml/docs/latest/docs/fundamentals/task/#artifacts)
- [Task Types](https://clear.ml/docs/latest/docs/fundamentals/task/#task-types)
- [Task Lifecycle](https://clear.ml/docs/latest/docs/fundamentals/task/#task-lifecycle)
  - [Logging Task Information](https://clear.ml/docs/latest/docs/fundamentals/task/#logging-task-information)
  - [Cloning Tasks](https://clear.ml/docs/latest/docs/fundamentals/task/#cloning-tasks)
- [Task States](https://clear.ml/docs/latest/docs/fundamentals/task/#task-states)
- [SDK Interface](https://clear.ml/docs/latest/docs/fundamentals/task/#sdk-interface)