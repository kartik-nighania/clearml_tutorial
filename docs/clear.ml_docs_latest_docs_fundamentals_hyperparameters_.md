---
url: "https://clear.ml/docs/latest/docs/fundamentals/hyperparameters/"
title: "Hyperparameters | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/fundamentals/hyperparameters/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

Hyperparameters are a script's configuration options. Since hyperparameters can have substantial impact on
model performance, it is crucial to efficiently track and manage them.

ClearML supports tracking and managing hyperparameters in each task and provides a dedicated [hyperparameter\\
optimization module](https://clear.ml/docs/latest/docs/getting_started/hpo). With ClearML's logging and tracking capabilities, tasks can be reproduced, and their
hyperparameters and results can be saved and compared, which is key to understanding model behavior.

ClearML lets you easily try out different hyperparameter values without changing your original code. ClearML's [execution\\
agent](https://clear.ml/docs/latest/docs/clearml_agent) will override the original values with any new ones you specify through the web UI (see
[Configuration](https://clear.ml/docs/latest/docs/webapp/webapp_exp_tuning#configuration) in the Tuning Tasks page). You can also
programmatically set task parameters.

## Tracking Hyperparameters [​](https://clear.ml/docs/latest/docs/fundamentals/hyperparameters/\#tracking-hyperparameters "Direct link to Tracking Hyperparameters")

Hyperparameters can be added from anywhere in your code, and ClearML provides multiple ways to obtain them! ClearML logs
and tracks hyperparameters of various types, supporting automatic logging and explicit reporting.

### Automatic Logging [​](https://clear.ml/docs/latest/docs/fundamentals/hyperparameters/\#automatic-logging "Direct link to Automatic Logging")

Once a ClearML Task has been [initialized](https://clear.ml/docs/latest/docs/references/sdk/task#taskinit) in a script, ClearML automatically captures and tracks
the following types of parameters:

- Command line parsing - command line parameters passed when invoking code that uses standard Python packages, including:
  - [click](https://clear.ml/docs/latest/docs/integrations/click)
  - [argparse](https://clear.ml/docs/latest/docs/guides/reporting/hyper_parameters#argparse-command-line-options)
  - [Python Fire](https://clear.ml/docs/latest/docs/integrations/python_fire)
  - [LightningCLI](https://clear.ml/docs/latest/docs/integrations/pytorch_lightning)
- TensorFlow Definitions (`absl-py`). See examples of ClearML's automatic logging of TF Defines:

  - [TensorFlow MNIST](https://clear.ml/docs/latest/docs/guides/frameworks/tensorflow/tensorflow_mnist)
  - [TensorBoard PR Curve](https://clear.ml/docs/latest/docs/guides/frameworks/tensorflow/tensorboard_pr_curve)
- [Hydra](https://clear.ml/docs/latest/docs/integrations/hydra) \- ClearML logs the `OmegaConf` which holds all the configuration files,
as well as values overridden during runtime.

Disabling Automatic Logging

Automatic logging can be disabled. See [Control Automatic Logging](https://clear.ml/docs/latest/docs/clearml_sdk/task_sdk#control-automatic-logging).

### Environment Variables [​](https://clear.ml/docs/latest/docs/fundamentals/hyperparameters/\#environment-variables "Direct link to Environment Variables")

Task Reproducibility

Relying on environment variables makes a task not fully reproducible, since ClearML Agent can't reproduce them at
runtime.

Environment variables can be logged to a task by specifying the variables in the `sdk.development.log_os_environments`
field of the [`clearml.conf`](https://clear.ml/docs/latest/docs/configs/clearml_conf) file:

```editorconfig
log_os_environments: ["AWS_*", "CUDA_VERSION"]
```

You can also specify environment variables using the `CLEARML_LOG_ENVIRONMENT` environment variable:

- All environment variables:





```text
export CLEARML_LOG_ENVIRONMENT=*
```

- Specific environment variables. For example, log `PWD` and `PYTHONPATH`:





```text
export CLEARML_LOG_ENVIRONMENT=PWD,PYTHONPATH
```

- No environment variables:





```text
export CLEARML_LOG_ENVIRONMENT=
```


Overriding clearml.conf

The `CLEARML_LOG_ENVIRONMENT` variable always overrides the `clearml.conf` file.

When a script that has integrated ClearML is executed, the environment variables listed in the `clearml.conf` or specified by
the `CLEARML_LOG_ENVIRONMENT` variable are logged by ClearML.

### Explicit Logging [​](https://clear.ml/docs/latest/docs/fundamentals/hyperparameters/\#explicit-logging "Direct link to Explicit Logging")

To augment its automatic logging, ClearML supports explicitly logging parameters. ClearML provides methods to directly
connect Python objects and configuration objects, as well as manually set and update task parameters.

#### Connecting Python Objects [​](https://clear.ml/docs/latest/docs/fundamentals/hyperparameters/\#connecting-python-objects "Direct link to Connecting Python Objects")

Users can directly connect Python objects, such as dictionaries and custom classes, to tasks, using the
[`Task.connect`](https://clear.ml/docs/latest/docs/references/sdk/task#connect) method. Once objects are connected to a task, all object elements
(e.g. class members, dictionary key-values pairs) are automatically logged by ClearML. Additionally, ClearML tracks these
values as they change through your code.

When connecting objects to ClearML, users can directly access and modify an object's elements (e.g. a specific key-value
pair in a parameter dictionary).

#### Connecting Configuration Objects [​](https://clear.ml/docs/latest/docs/fundamentals/hyperparameters/\#connecting-configuration-objects "Direct link to Connecting Configuration Objects")

Configuration objects are dictionaries or configuration files connected to the task using
[`Task.connect_configuration()`](https://clear.ml/docs/latest/docs/references/sdk/task#connect_configuration). With this method, configuration
objects are saved as blobs i.e. ClearML is not aware of their internal structure.

#### Setting and Updating Parameters [​](https://clear.ml/docs/latest/docs/fundamentals/hyperparameters/\#setting-and-updating-parameters "Direct link to Setting and Updating Parameters")

ClearML provides methods to set and update task parameters manually. Use [`Task.set_parameters()`](https://clear.ml/docs/latest/docs/references/sdk/task#set_parameters)
to define parameters manually. To update the parameters in a task, use [`Task.set_parameters_as_dict()`](https://clear.ml/docs/latest/docs/references/sdk/task#set_parameters_as_dict).
The `set_parameters_as_dict` method updates parameters while the `set_parameters` method overrides the parameters.

ClearML does not automatically track changes to explicitly set parameters.

### User Properties [​](https://clear.ml/docs/latest/docs/fundamentals/hyperparameters/\#user-properties "Direct link to User Properties")

User properties do not impact task execution and can be modified at any stage. They are convenient for setting
helpful values which are displayed in the [task table](https://clear.ml/docs/latest/docs/webapp/webapp_exp_table) (i.e. customize columns),
making it easier to search / filter tasks. Add user properties to a task with the
[`Task.set_user_properties`](https://clear.ml/docs/latest/docs/references/sdk/task#set_user_properties) method.

### Accessing Parameters [​](https://clear.ml/docs/latest/docs/fundamentals/hyperparameters/\#accessing-parameters "Direct link to Accessing Parameters")

ClearML provides methods to directly access a task's logged parameters.

To get all of a task's parameters and properties (hyperparameters, configuration objects, and user properties), use
[`Task.get_parameters()`](https://clear.ml/docs/latest/docs/references/sdk/task#get_parameters), which will return a dictionary with the parameters,
including their subsections (see [WebApp sections](https://clear.ml/docs/latest/docs/fundamentals/hyperparameters/#webapp-interface) below).

## WebApp Interface [​](https://clear.ml/docs/latest/docs/fundamentals/hyperparameters/\#webapp-interface "Direct link to WebApp Interface")

Configurations can be viewed in web UI task pages, in the **CONFIGURATION** tab.

The configuration panel is split into three sections according to type:

- **User Properties** \- Modifiable section that can be edited post-execution
- **Hyperparameters** \- Individual parameters for configuration
- **Configuration Objects** \- Usually configuration files (JSON / YAML) or Python objects

These sections are further broken down into subsections based on how the parameters were logged (General / Args / TF\_Define / Environment).

![Task hyperparameters sections](https://clear.ml/docs/latest/assets/images/hyperparameters_sections-a2f208998fca692c9611a847cc136f38.png#light-mode-only)![Task hyperparameters sections](https://clear.ml/docs/latest/assets/images/hyperparameters_sections_dark-05b0b727f5fed967e2d895525074359e.png#dark-mode-only)

## SDK Interface [​](https://clear.ml/docs/latest/docs/fundamentals/hyperparameters/\#sdk-interface "Direct link to SDK Interface")

See the [Configuration section](https://clear.ml/docs/latest/docs/clearml_sdk/task_sdk#configuration) of the Task SDK page for an overview of basic Pythonic
methods for working with hyperparameters.

- [Tracking Hyperparameters](https://clear.ml/docs/latest/docs/fundamentals/hyperparameters/#tracking-hyperparameters)
  - [Automatic Logging](https://clear.ml/docs/latest/docs/fundamentals/hyperparameters/#automatic-logging)
  - [Environment Variables](https://clear.ml/docs/latest/docs/fundamentals/hyperparameters/#environment-variables)
  - [Explicit Logging](https://clear.ml/docs/latest/docs/fundamentals/hyperparameters/#explicit-logging)
  - [User Properties](https://clear.ml/docs/latest/docs/fundamentals/hyperparameters/#user-properties)
  - [Accessing Parameters](https://clear.ml/docs/latest/docs/fundamentals/hyperparameters/#accessing-parameters)
- [WebApp Interface](https://clear.ml/docs/latest/docs/fundamentals/hyperparameters/#webapp-interface)
- [SDK Interface](https://clear.ml/docs/latest/docs/fundamentals/hyperparameters/#sdk-interface)