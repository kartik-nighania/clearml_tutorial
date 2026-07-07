---
url: "https://clear.ml/docs/latest/docs/integrations/keras/"
title: "Keras | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/integrations/keras/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

tip

If you are not already using ClearML, see [ClearML Setup instructions](https://clear.ml/docs/latest/docs/clearml_sdk/clearml_sdk_setup).

ClearML integrates with [Keras](https://keras.io/) out-of-the-box, automatically logging its models, scalars,
TensorFlow definitions, and TensorBoard outputs.

All you have to do is simply add two lines of code to your Keras script:

```python
from clearml import Task

task = Task.init(task_name="<task_name>", project_name="<project_name>")
```

And that's it! This creates a [ClearML Task](https://clear.ml/docs/latest/docs/fundamentals/task) which captures:

- Source code and uncommitted changes
- Installed packages
- Keras models
- Scalars (e.g. accuracy, loss)
- TensorFlow definitions
- [TensorBoard](https://www.tensorflow.org/tensorboard) outputs
- Console output
- General details such as machine details, runtime, creation date etc.
- And more

You can view all the task details in the [WebApp](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual).

![WebApp Gif](https://clear.ml/docs/latest/assets/images/tensorflow-d07a4c741764e0925f66bb8ec77a02bf.gif)

## Automatic Logging Control [​](https://clear.ml/docs/latest/docs/integrations/keras/\#automatic-logging-control "Direct link to Automatic Logging Control")

By default, when ClearML is integrated into your Keras script, it captures Keras models and scalars, as well as TensorFlow
definitions and TensorBoard outputs. But, you may want to have more control over what your task logs.

To control a task's framework logging, use the `auto_connect_frameworks` parameter of [`Task.init()`](https://clear.ml/docs/latest/docs/references/sdk/task#taskinit).
Completely disable all automatic logging by setting the parameter to `False`. For finer grained control of logged
frameworks, input a dictionary, with framework-boolean pairs.

For example:

```python
auto_connect_frameworks={

   'tensorflow': False, 'tensorboard': False, 'matplotlib': True, 'pytorch': True,

   'xgboost': False, 'scikit': True, 'fastai': True, 'lightgbm': False,

   'hydra': True, 'detect_repository': True, 'tfdefines': True, 'joblib': True,

   'megengine': True, 'catboost': True

}
```

To control Keras logging, use the `tensorflow` and `tensorboard` keys.

You can also input wildcards as dictionary values, so ClearML will log a model created by a framework only if its local
path matches at least one wildcard.

For example, in the code below, ClearML will log TensorFlow (and/or keras) models only if their paths have the `.keras` extension. The
unspecified frameworks' values default to true so all their models are automatically logged.

```python
auto_connect_frameworks={'tensorflow' : '*.keras'}
```

## Manual Logging [​](https://clear.ml/docs/latest/docs/integrations/keras/\#manual-logging "Direct link to Manual Logging")

To augment its automatic logging, ClearML also provides an explicit logging interface.

See more information about explicitly logging information to a ClearML Task:

- [Models](https://clear.ml/docs/latest/docs/clearml_sdk/model_sdk#manually-logging-models)
- [Configuration](https://clear.ml/docs/latest/docs/clearml_sdk/task_sdk#configuration) (e.g. parameters, configuration files)
- [Artifacts](https://clear.ml/docs/latest/docs/clearml_sdk/task_sdk#artifacts) (e.g. output files or Python objects created by a task)
- [Scalars](https://clear.ml/docs/latest/docs/clearml_sdk/task_sdk#scalars)
- [Text/Plots/Debug Samples](https://clear.ml/docs/latest/docs/fundamentals/logger#manual-reporting)

See [Explicit Reporting Tutorial](https://clear.ml/docs/latest/docs/guides/reporting/explicit_reporting).

## Examples [​](https://clear.ml/docs/latest/docs/integrations/keras/\#examples "Direct link to Examples")

Take a look at ClearML's Keras examples. The examples use Keras and ClearML in different configurations with
additional tools like TensorBoard and Matplotlib:

- [Keras with Tensorboard](https://clear.ml/docs/latest/docs/guides/frameworks/keras/keras_tensorboard) \- Demonstrates ClearML logging a Keras model,
and plots and scalars logged to TensorBoard
- [Keras with Matplotlib](https://clear.ml/docs/latest/docs/guides/frameworks/keras/jupyter) \- Demonstrates ClearML logging a Keras model, Matplotlib plots,
and debug samples, plots, and scalars logged to TensorBoard

## Remote Execution [​](https://clear.ml/docs/latest/docs/integrations/keras/\#remote-execution "Direct link to Remote Execution")

ClearML logs all the information required to reproduce a task run on a different machine (installed packages,
uncommitted changes etc.). The [ClearML Agent](https://clear.ml/docs/latest/docs/clearml_agent) listens to designated queues and when a task is enqueued,
the agent pulls it, recreates its execution environment, and runs it, reporting its scalars, plots, etc. to the
task manager.

Deploy a ClearML Agent onto any machine (e.g. a cloud VM, a local GPU machine, your own laptop) by simply running the
following command on it:

```commandline
clearml-agent daemon --queue <queues_to_listen_to> [--docker]
```

Use the ClearML [Autoscalers](https://clear.ml/docs/latest/docs/cloud_autoscaling/autoscaling_overview) to help you manage cloud workloads in the
cloud of your choice (AWS, GCP, Azure) and automatically deploy ClearML agents: the autoscaler automatically spins up
and shuts down instances as needed, according to a resource budget that you set.

### Reproducing Task Runs [​](https://clear.ml/docs/latest/docs/integrations/keras/\#reproducing-task-runs "Direct link to Reproducing Task Runs")

![Cloning, editing, enqueuing gif](https://clear.ml/docs/latest/assets/images/integrations_yolov5-65419387b0ce8048acf00f3b99e26a91.gif#light-mode-only)![Cloning, editing, enqueuing gif](https://clear.ml/docs/latest/assets/images/integrations_yolov5_dark-253af7b62a086b6b59ed9a8ad381cf5a.gif#dark-mode-only)

Use ClearML's web interface to edit task details, like configuration parameters or input models, then execute the task
with the new configuration on a remote machine:

- Clone the task
- Edit the hyperparameters and/or other details
- Enqueue the task

The ClearML Agent executing the task will use the new values to [override any hard coded values](https://clear.ml/docs/latest/docs/clearml_agent).

### Executing a Task Remotely [​](https://clear.ml/docs/latest/docs/integrations/keras/\#executing-a-task-remotely "Direct link to Executing a Task Remotely")

You can set a task to be executed remotely programmatically by adding [`Task.execute_remotely()`](https://clear.ml/docs/latest/docs/references/sdk/task#execute_remotely)
to your script. This method stops the current local execution of the task, and then enqueues it to a specified queue to
re-run it on a remote machine.

```python
# If executed locally, process will terminate, and a copy will be executed by an agent instead

task.execute_remotely(queue_name='default', exit_process=True)
```

## Hyperparameter Optimization [​](https://clear.ml/docs/latest/docs/integrations/keras/\#hyperparameter-optimization "Direct link to Hyperparameter Optimization")

Use ClearML's [`HyperParameterOptimizer`](https://clear.ml/docs/latest/docs/references/sdk/hpo_optimization_hyperparameteroptimizer) class to find
the hyperparameter values that yield the best performing models. See [Hyperparameter Optimization](https://clear.ml/docs/latest/docs/getting_started/hpo)
for more information.

- [Automatic Logging Control](https://clear.ml/docs/latest/docs/integrations/keras/#automatic-logging-control)
- [Manual Logging](https://clear.ml/docs/latest/docs/integrations/keras/#manual-logging)
- [Examples](https://clear.ml/docs/latest/docs/integrations/keras/#examples)
- [Remote Execution](https://clear.ml/docs/latest/docs/integrations/keras/#remote-execution)
  - [Reproducing Task Runs](https://clear.ml/docs/latest/docs/integrations/keras/#reproducing-task-runs)
  - [Executing a Task Remotely](https://clear.ml/docs/latest/docs/integrations/keras/#executing-a-task-remotely)
- [Hyperparameter Optimization](https://clear.ml/docs/latest/docs/integrations/keras/#hyperparameter-optimization)