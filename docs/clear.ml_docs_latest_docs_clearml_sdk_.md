---
url: "https://clear.ml/docs/latest/docs/clearml_sdk/"
title: "ClearML SDK | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/clearml_sdk/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The ClearML Python Package supports the [automatic logging](https://clear.ml/docs/latest/docs/fundamentals/logger#automatic-reporting) that documents
tasks for you, and an extensive set of powerful features and functionality you can use to improve experimentation
and other workflows.

Installation

For installation instructions, see [ClearML Setup](https://clear.ml/docs/latest/docs/clearml_sdk/clearml_sdk_setup#install-clearml).

The ClearML Python Package collects the scripts' entire execution information, including:

- Git repository (branch, commit ID, and uncommitted changes)
- Working directory and entry point
- Hyperparameters
- Initial weights model, model snapshots (checkpoints), output model
- Artifacts, metrics, logs, other reported data (from libraries and visualization toolkits), and debug samples.

In conjunction with the ClearML Hosted Service (or self-hosted [ClearML Server](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server))
and [ClearML Agent](https://clear.ml/docs/latest/docs/clearml_agent), the ClearML Python Package allows you and your teammates to collaborate
programmatically and use the [ClearML Web UI](https://clear.ml/docs/latest/docs/webapp/webapp_overview).

## Classes and Modules [​](https://clear.ml/docs/latest/docs/clearml_sdk/\#classes-and-modules "Direct link to Classes and Modules")

### Task [​](https://clear.ml/docs/latest/docs/clearml_sdk/\#task "Direct link to Task")

The `Task` class is the code template for all Task features and functionality including:

- Data collection and storage from scripts
- Automatic bindings with frameworks, libraries, and visualization tools
- A robust set of methods for Task execution (cloning, connecting parameter dictionaries, configurations, and models)
- and more!

See an [overview](https://clear.ml/docs/latest/docs/clearml_sdk/task_sdk) of `Task`'s pythonic methods or the [Task SDK reference page](https://clear.ml/docs/latest/docs/clearml_sdk/task_sdk).

### Model [​](https://clear.ml/docs/latest/docs/clearml_sdk/\#model "Direct link to Model")

The `model` module contains three classes that provide support for working with models in ClearML:

- `Model` \- represents an existing model in ClearML that can be loaded and connected to a Task
- `InputModel` \- represents an existing model that you can load into ClearML
- `OutputModel` \- represents the task output model that is always connected to the Task

See an [overview](https://clear.ml/docs/latest/docs/clearml_sdk/model_sdk) of the Model classes' pythonic methods, or the SDK reference pages for [`Model`](https://clear.ml/docs/latest/docs/references/sdk/model_model),
[`InputModel`](https://clear.ml/docs/latest/docs/references/sdk/model_inputmodel), and [`OutputModel`](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel).

### Logger [​](https://clear.ml/docs/latest/docs/clearml_sdk/\#logger "Direct link to Logger")

The `Logger` class is the ClearML console log and metric statistics interface. The class contains methods for:

- Explicit reporting
- Setting an upload destination for debug sample storage
- Controlling ClearML's logging of TensorBoard and Matplotlib outputs

See the [Logger SDK reference page](https://clear.ml/docs/latest/docs/references/sdk/logger).

### Hyperparameter Optimization [​](https://clear.ml/docs/latest/docs/clearml_sdk/\#hyperparameter-optimization "Direct link to Hyperparameter Optimization")

ClearML's `optimization` module includes classes that support hyperparameter optimization (HPO):

- [HyperParameterOptimizer](https://clear.ml/docs/latest/docs/references/sdk/hpo_optimization_hyperparameteroptimizer) \- Hyperparameter search
controller class
- Optimization search strategy classes including [Optuna](https://clear.ml/docs/latest/docs/references/sdk/hpo_optuna_optuna_optimizeroptuna), [HpBandSter](https://clear.ml/docs/latest/docs/references/sdk/hpo_hpbandster_bandster_optimizerbohb),
[GridSearch](https://clear.ml/docs/latest/docs/references/sdk/hpo_optimization_gridsearch), [RandomSearch](https://clear.ml/docs/latest/docs/references/sdk/hpo_optimization_randomsearch),
and a base [SearchStrategy](https://github.com/clearml/clearml/blob/master/clearml/automation/optimization.py#L310)
that can be customized

See the [HyperParameterOptimizer SDK reference page](https://clear.ml/docs/latest/docs/references/sdk/hpo_optimization_hyperparameteroptimizer).

### Pipeline [​](https://clear.ml/docs/latest/docs/clearml_sdk/\#pipeline "Direct link to Pipeline")

ClearML's `automation` module includes classes that support creating pipelines:

- [PipelineController](https://clear.ml/docs/latest/docs/pipelines/pipelines_sdk_tasks) \- A Pythonic interface for
defining and configuring a pipeline controller and its steps. The controller and steps can be functions in your
python code, or ClearML [tasks](https://clear.ml/docs/latest/docs/fundamentals/task).
- [PipelineDecorator](https://clear.ml/docs/latest/docs/pipelines/pipelines_sdk_function_decorators) \- A set
of Python decorators which transform your functions into the pipeline controller and steps.

### Dataset [​](https://clear.ml/docs/latest/docs/clearml_sdk/\#dataset "Direct link to Dataset")

The `Dataset` class supports creating, modifying, and managing datasets,
as well as retrieving them for use in code.

See [ClearML Data](https://clear.ml/docs/latest/docs/clearml_data/) or the [Dataset SDK reference page](https://clear.ml/docs/latest/docs/references/sdk/dataset).

### StorageManager [​](https://clear.ml/docs/latest/docs/clearml_sdk/\#storagemanager "Direct link to StorageManager")

The `StorageManager` class provides support for downloading and uploading from storage,
including local folders, S3, Google Cloud Storage, Azure Storage, and http(s).

See [examples](https://clear.ml/docs/latest/docs/guides/storage/examples_storagehelper) of `StorageManager` usage or the [StorageManager SDK reference page](https://clear.ml/docs/latest/docs/references/sdk/storage).

### APIClient [​](https://clear.ml/docs/latest/docs/clearml_sdk/\#apiclient "Direct link to APIClient")

The `APIClient` class provides a Pythonic interface to access ClearML's backend REST API.

See an [overview](https://clear.ml/docs/latest/docs/clearml_sdk/apiclient_sdk) for APIClient usage.

### ClearmlJob [​](https://clear.ml/docs/latest/docs/clearml_sdk/\#clearmljob "Direct link to ClearmlJob")

Use the ClearmlJob to create and manage jobs based on existing tasks. The class supports changing a job's parameters,
configurations, and other execution details.

See [reference page](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob).

### AutoScaler [​](https://clear.ml/docs/latest/docs/clearml_sdk/\#autoscaler "Direct link to AutoScaler")

The `AutoScaler` class facilitates implementing resource budgeting. See class methods [here](https://github.com/clearml/clearml/blob/master/clearml/automation/auto_scaler.py).
ClearML also provides a class specifically for AWS autoscaling. See [code](https://github.com/clearml/clearml/blob/master/clearml/automation/aws_auto_scaler.py#L22)
and [example script](https://github.com/clearml/clearml/blob/master/examples/services/aws-autoscaler/aws_autoscaler.py).

### TaskScheduler [​](https://clear.ml/docs/latest/docs/clearml_sdk/\#taskscheduler "Direct link to TaskScheduler")

The `TaskScheduler` class supports methods for scheduling periodic execution (like cron jobs). See the [code](https://github.com/clearml/clearml/blob/master/clearml/automation/scheduler.py#L481)
and [example](https://github.com/clearml/clearml/blob/master/examples/scheduler/cron_example.py).

### TriggerScheduler [​](https://clear.ml/docs/latest/docs/clearml_sdk/\#triggerscheduler "Direct link to TriggerScheduler")

The `TriggerScheduler` class facilitates triggering task execution in the case that specific events occur in the system
(such as model publication, dataset creation, task failure). See [code](https://github.com/clearml/clearml/blob/master/clearml/automation/trigger.py#L148)
and [usage example](https://github.com/clearml/clearml/blob/master/examples/scheduler/trigger_example.py).

## Examples [​](https://clear.ml/docs/latest/docs/clearml_sdk/\#examples "Direct link to Examples")

The `clearml` GitHub repository includes an [examples folder](https://github.com/clearml/clearml/tree/master/examples)
with example scripts demonstrating how to use the various functionalities of the ClearML SDK.

These examples are preloaded in the [ClearML Hosted Service](https://app.clear.ml/), and can be viewed, cloned,
and edited in the ClearML Web UI's `ClearML Examples` project. Each example is explained in the [examples section](https://clear.ml/docs/latest/docs/guides).

- [Classes and Modules](https://clear.ml/docs/latest/docs/clearml_sdk/#classes-and-modules)
  - [Task](https://clear.ml/docs/latest/docs/clearml_sdk/#task)
  - [Model](https://clear.ml/docs/latest/docs/clearml_sdk/#model)
  - [Logger](https://clear.ml/docs/latest/docs/clearml_sdk/#logger)
  - [Hyperparameter Optimization](https://clear.ml/docs/latest/docs/clearml_sdk/#hyperparameter-optimization)
  - [Pipeline](https://clear.ml/docs/latest/docs/clearml_sdk/#pipeline)
  - [Dataset](https://clear.ml/docs/latest/docs/clearml_sdk/#dataset)
  - [StorageManager](https://clear.ml/docs/latest/docs/clearml_sdk/#storagemanager)
  - [APIClient](https://clear.ml/docs/latest/docs/clearml_sdk/#apiclient)
  - [ClearmlJob](https://clear.ml/docs/latest/docs/clearml_sdk/#clearmljob)
  - [AutoScaler](https://clear.ml/docs/latest/docs/clearml_sdk/#autoscaler)
  - [TaskScheduler](https://clear.ml/docs/latest/docs/clearml_sdk/#taskscheduler)
  - [TriggerScheduler](https://clear.ml/docs/latest/docs/clearml_sdk/#triggerscheduler)
- [Examples](https://clear.ml/docs/latest/docs/clearml_sdk/#examples)