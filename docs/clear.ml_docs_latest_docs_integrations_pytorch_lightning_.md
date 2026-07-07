---
url: "https://clear.ml/docs/latest/docs/integrations/pytorch_lightning/"
title: "PyTorch Lightning | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/integrations/pytorch_lightning/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

tip

If you are not already using ClearML, see [ClearML Setup instructions](https://clear.ml/docs/latest/docs/clearml_sdk/clearml_sdk_setup).

[PyTorch Lightning](https://github.com/Lightning-AI/lightning) is a framework that simplifies the process of training and deploying PyTorch models. ClearML seamlessly
integrates with PyTorch Lightning, automatically logging PyTorch models, parameters supplied by [LightningCLI](https://lightning.ai/docs/pytorch/stable/cli/lightning_cli.html),
and more.

All you have to do is simply add two lines of code to your PyTorch Lightning script:

```python
from clearml import Task

task = Task.init(task_name="<task_name>", project_name="<project_name>")
```

And that's it! This creates a [ClearML Task](https://clear.ml/docs/latest/docs/fundamentals/task) which captures:

- Source code and uncommitted changes
- Installed packages
- PyTorch Models
- Parameters supplied by [LightningCLI](https://lightning.ai/docs/pytorch/stable/cli/lightning_cli.html) (when class is instantiated in script)
- [TensorBoard](https://www.tensorflow.org/tensorboard) outputs
- Console output
- General details such as machine details, runtime, creation date etc.
- And more

You can view all the task details in the [WebApp](https://clear.ml/docs/latest/docs/webapp/webapp_overview).

![LightningCLI params](https://clear.ml/docs/latest/assets/images/integrations_lightningcli_params-79558a9dd92ee8242f82c5530e8cf748.png#light-mode-only)![LightningCLI params](https://clear.ml/docs/latest/assets/images/integrations_lightningcli_params_dark-6daae0e2c64807fa51ee0d89a3689c0e.png#dark-mode-only)

See an example of PyTorch Lightning and ClearML in action [here](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch_lightning/pytorch_lightning_example).

## Automatic Logging Control [​](https://clear.ml/docs/latest/docs/integrations/pytorch_lightning/\#automatic-logging-control "Direct link to Automatic Logging Control")

By default, when ClearML is integrated into your script, it automatically captures information from supported frameworks,
and parameters from supported argument parsers. But, you may want to have more control over what your task logs.

### Frameworks [​](https://clear.ml/docs/latest/docs/integrations/pytorch_lightning/\#frameworks "Direct link to Frameworks")

To control a task's framework logging, use the `auto_connect_frameworks` parameter of [`Task.init()`](https://clear.ml/docs/latest/docs/references/sdk/task#taskinit).
Completely disable all automatic logging by setting the parameter to `False`. For finer grained control of logged
frameworks, input a dictionary, with framework-boolean pairs.

For example, the following code will log PyTorch models, but will not log any information reported to TensorBoard:

```python
auto_connect_frameworks={

   'pytorch': True, 'tensorboard': False, 'matplotlib': True, 'tensorflow': True,

   'xgboost': True, 'scikit': True, 'fastai': True, 'lightgbm': True,

   'hydra': True, 'detect_repository': True, 'tfdefines': True, 'joblib': True,

   'megengine': True, 'catboost': True

}
```

You can also input wildcards as dictionary values, so ClearML will log a model created by a framework only if its local
path matches at least one wildcard.

For example, in the code below, ClearML will log PyTorch models only if their paths have the `.pt` extension. The
unspecified frameworks' values default to true so all their models are automatically logged.

```python
auto_connect_frameworks={'pytorch' : '*.pt'}
```

### Argument Parsers [​](https://clear.ml/docs/latest/docs/integrations/pytorch_lightning/\#argument-parsers "Direct link to Argument Parsers")

To control a task's logging of parameters from argument parsers, use the `auto_connect_arg_parser` parameter of [`Task.init()`](https://clear.ml/docs/latest/docs/references/sdk/task#taskinit).
Completely disable all automatic logging by setting the parameter to `False` (this includes disabling logging of `LightningCLI` parameters).

```python
auto_connect_arg_parser=False
```

For finer grained control of logged parameters, input a dictionary with parameter-boolean pairs. The `False` value
excludes the specified parameter. Unspecified parameters default to `True`.

For example, the following code will not log the `Example_1` parameter, but will log all other arguments.

```python
auto_connect_arg_parser={"Example_1": False}
```

To exclude all unspecified parameters, set the `*` key to `False`. For example, the following code will log **only** the
`Example_2` parameter.

```python
auto_connect_arg_parser={"Example_2": True, "*": False}
```

## Manual Logging [​](https://clear.ml/docs/latest/docs/integrations/pytorch_lightning/\#manual-logging "Direct link to Manual Logging")

To augment its automatic logging, ClearML also provides an explicit logging interface.

See more information about explicitly logging information to a ClearML Task:

- [Models](https://clear.ml/docs/latest/docs/clearml_sdk/model_sdk#manually-logging-models)
- [Configuration](https://clear.ml/docs/latest/docs/clearml_sdk/task_sdk#configuration) (e.g. parameters, configuration files)
- [Artifacts](https://clear.ml/docs/latest/docs/clearml_sdk/task_sdk#artifacts) (e.g. output files or Python objects created by a task)
- [Scalars](https://clear.ml/docs/latest/docs/clearml_sdk/task_sdk#scalars)
- [Text/Plots/Debug Samples](https://clear.ml/docs/latest/docs/fundamentals/logger#manual-reporting)

See [Explicit Reporting Tutorial](https://clear.ml/docs/latest/docs/guides/reporting/explicit_reporting).

## Remote Execution [​](https://clear.ml/docs/latest/docs/integrations/pytorch_lightning/\#remote-execution "Direct link to Remote Execution")

ClearML logs all the information required to reproduce a task run on a different machine (installed packages,
uncommitted changes etc.). The [ClearML Agent](https://clear.ml/docs/latest/docs/clearml_agent) listens to designated queues and when a task is enqueued,
the agent pulls it, recreates its execution environment, and runs it, reporting its scalars, plots, etc. to the
task manager.

Deploy a ClearML Agent onto any machine (e.g. a cloud VM, a local GPU machine, your own laptop) by simply running the
following command on it:

```commandline
clearml-agent daemon --queue <queues_to_listen_to> [--docker]
```

Use the ClearML [Autoscalers](https://clear.ml/docs/latest/docs/cloud_autoscaling/autoscaling_overview), to help you manage cloud workloads in the
cloud of your choice (AWS, GCP, Azure) and automatically deploy ClearML agents: the autoscaler automatically spins up
and shuts down instances as needed, according to a resource budget that you set.

### Reproducing Task Runs [​](https://clear.ml/docs/latest/docs/integrations/pytorch_lightning/\#reproducing-task-runs "Direct link to Reproducing Task Runs")

![Cloning, editing, enqueuing gif](https://clear.ml/docs/latest/assets/images/integrations_yolov5-65419387b0ce8048acf00f3b99e26a91.gif#light-mode-only)![Cloning, editing, enqueuing gif](https://clear.ml/docs/latest/assets/images/integrations_yolov5_dark-253af7b62a086b6b59ed9a8ad381cf5a.gif#dark-mode-only)

Use ClearML's web interface to edit task details, like configuration parameters or input models, then execute the task
with the new configuration on a remote machine:

- Clone the task
- Edit the hyperparameters and/or other details
- Enqueue the task

The ClearML Agent executing the task will use the new values to [override any hard coded values](https://clear.ml/docs/latest/docs/clearml_agent).

### Executing a Task Remotely [​](https://clear.ml/docs/latest/docs/integrations/pytorch_lightning/\#executing-a-task-remotely "Direct link to Executing a Task Remotely")

You can set a task to be executed remotely programmatically by adding [`Task.execute_remotely()`](https://clear.ml/docs/latest/docs/references/sdk/task#execute_remotely)
to your script. This method stops the current local execution of the task, and then enqueues it to a specified queue to
re-run it on a remote machine.

```python
# If executed locally, process will terminate, and a copy will be executed by an agent instead

task.execute_remotely(queue_name='default', exit_process=True)
```

## Hyperparameter Optimization [​](https://clear.ml/docs/latest/docs/integrations/pytorch_lightning/\#hyperparameter-optimization "Direct link to Hyperparameter Optimization")

Use ClearML's [`HyperParameterOptimizer`](https://clear.ml/docs/latest/docs/references/sdk/hpo_optimization_hyperparameteroptimizer) class to find
the hyperparameter values that yield the best performing models. See [Hyperparameter Optimization](https://clear.ml/docs/latest/docs/getting_started/hpo)
for more information.

- [Automatic Logging Control](https://clear.ml/docs/latest/docs/integrations/pytorch_lightning/#automatic-logging-control)
  - [Frameworks](https://clear.ml/docs/latest/docs/integrations/pytorch_lightning/#frameworks)
  - [Argument Parsers](https://clear.ml/docs/latest/docs/integrations/pytorch_lightning/#argument-parsers)
- [Manual Logging](https://clear.ml/docs/latest/docs/integrations/pytorch_lightning/#manual-logging)
- [Remote Execution](https://clear.ml/docs/latest/docs/integrations/pytorch_lightning/#remote-execution)
  - [Reproducing Task Runs](https://clear.ml/docs/latest/docs/integrations/pytorch_lightning/#reproducing-task-runs)
  - [Executing a Task Remotely](https://clear.ml/docs/latest/docs/integrations/pytorch_lightning/#executing-a-task-remotely)
- [Hyperparameter Optimization](https://clear.ml/docs/latest/docs/integrations/pytorch_lightning/#hyperparameter-optimization)