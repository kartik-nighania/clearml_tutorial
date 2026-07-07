---
url: "https://clear.ml/docs/latest/docs/guides/reporting/model_config/"
title: "Model Reporting | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/reporting/model_config/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The [model\_reporting.py](https://github.com/clearml/clearml/blob/master/examples/reporting/model_reporting.py) example
demonstrates logging a model using the [OutputModel](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel)
class.

The example does the following:

- Creates a task named `Model reporting example` in the `examples` project.
- Uses an OutputModel object to register a previously trained model and log its label enumeration.

## Initialization [​](https://clear.ml/docs/latest/docs/guides/reporting/model_config/\#initialization "Direct link to Initialization")

An OutputModel object is instantiated for the task.

```python
from clearml import Task, OutputModel

# Connecting ClearML with the current process,

task = Task.init(project_name="examples", task_name="Model logging example")



# Create output model and connect it to the task

output_model = OutputModel(task=task)
```

## Label Enumeration [​](https://clear.ml/docs/latest/docs/guides/reporting/model_config/\#label-enumeration "Direct link to Label Enumeration")

Set the model's label enumeration using [`OutputModel.update_labels()`](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel#update_labels).

```python
labels = {"background": 0, "cat": 1, "dog": 2}

output_model.update_labels(labels)
```

## Registering Models [​](https://clear.ml/docs/latest/docs/guides/reporting/model_config/\#registering-models "Direct link to Registering Models")

Register a previously trained model using [`OutputModel.update_weights()`](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel#update_weights).
The example code uses a model stored in S3.

```python
# Manually log a model file, which will have the labels connected above

output_model.update_weights(register_uri=model_url)
```

## WebApp [​](https://clear.ml/docs/latest/docs/guides/reporting/model_config/\#webapp "Direct link to WebApp")

The model appears in the task's **ARTIFACTS** tab.

![Task artifacts](https://clear.ml/docs/latest/assets/images/examples_model_logging_artifacts-03f06c540446b397884ba90d330f4d60.png#light-mode-only)![Task artifacts](https://clear.ml/docs/latest/assets/images/examples_model_logging_artifacts_dark-16afd688c911ae7d7c074b07719c8e44.png#dark-mode-only)

Clicking on the model name takes you to the [model's page](https://clear.ml/docs/latest/docs/webapp/webapp_model_viewing), where you can view the
model's details and access the model.

The model's **LABELS** tab displays its label enumeration.

![Model Labels tab](https://clear.ml/docs/latest/assets/images/examples_model_logging_labels-bdc3e6cff7c87e385accfe1e0b7703f8.png#light-mode-only)![Model Labels tab](https://clear.ml/docs/latest/assets/images/examples_model_logging_labels_dark-e36ef56fb4f0d1f921669fdf66ceb113.png#dark-mode-only)

## Additional Example [​](https://clear.ml/docs/latest/docs/guides/reporting/model_config/\#additional-example "Direct link to Additional Example")

See [PyTorch Model Updating](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/model_updating) for a more robust example, which trains a model,
and then logs it with OutputModel.

- [Initialization](https://clear.ml/docs/latest/docs/guides/reporting/model_config/#initialization)
- [Label Enumeration](https://clear.ml/docs/latest/docs/guides/reporting/model_config/#label-enumeration)
- [Registering Models](https://clear.ml/docs/latest/docs/guides/reporting/model_config/#registering-models)
- [WebApp](https://clear.ml/docs/latest/docs/guides/reporting/model_config/#webapp)
- [Additional Example](https://clear.ml/docs/latest/docs/guides/reporting/model_config/#additional-example)