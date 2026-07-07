---
url: "https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/model_updating/"
title: "PyTorch Model Updating | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/model_updating/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The [pytorch\_model\_update.py](https://github.com/clearml/clearml/blob/master/examples/frameworks/pytorch/pytorch_model_update.py)
example demonstrates training a model and logging it using the [OutputModel](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel)
class.

The example does the following:

- Creates a task named `Model update pytorch` in the `examples` project.
- Trains a neural network on the CIFAR-10 dataset for image classification.
- Uses an OutputModel object to log the model, its label enumeration and configuration dictionary.

Disabling automatic framework logging

This example disables the default automatic capturing of PyTorch outputs, to demonstrate how to manually control what is
logged from PyTorch. See [this FAQ](https://clear.ml/docs/latest/docs/faq#controlling_logging) for more information.

## Initialization [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/model_updating/\#initialization "Direct link to Initialization")

An OutputModel object is instantiated for the task.

```python
from clearml import Task, OutputModel

task = Task.init(

        project_name="examples",

        task_name="Model update pytorch",

        auto_connect_frameworks={"pytorch": False}

)



output_model = OutputModel(task=task)
```

## Label Enumeration [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/model_updating/\#label-enumeration "Direct link to Label Enumeration")

The label enumeration dictionary is logged using the [`Task.connect_label_enumeration`](https://clear.ml/docs/latest/docs/references/sdk/task#connect_label_enumeration)
method which will update the task's resulting model information. The current running task is accessed using the
[`Task.current_task`](https://clear.ml/docs/latest/docs/references/sdk/task#taskcurrent_task) class method.

```python
# store the label enumeration of the training model

classes = ("plane", "car", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck",)

enumeration = {k: v for v, k in enumerate(classes, 1)}

Task.current_task().connect_label_enumeration(enumeration)
```

Directly Setting Model Enumeration

You can set a model's label enumeration directly using the [`OutputModel.update_labels`](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel#update_labels)
method.

## Model Configuration [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/model_updating/\#model-configuration "Direct link to Model Configuration")

Add a configuration dictionary to the model using the [`OutputModel.update_design`](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel#update_design)
method.

```python
model_config_dict = {

        "list_of_ints": [1, 2, 3, 4],

        "dict": {

            "sub_value": "string",

            "sub_integer": 11

            },

        "value": 13.37

}



model.update_design(config_dict=model_config_dict)
```

## Updating Models [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/model_updating/\#updating-models "Direct link to Updating Models")

To update a model, use [`OutputModel.update_weights()`](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel#update_weights).
This uploads the model to the set storage destination (see [Setting Upload Destination](https://clear.ml/docs/latest/docs/fundamentals/models#setting-upload-destination)),
and registers that location to the task as the output model.

```python
# CONDITION depicts a custom condition for when to save the model. The model is saved and then updated in ClearML

CONDITION = True

if CONDITION:

        torch.save(net.state_dict(), PATH)

        model.update_weights(weights_filename=PATH)
```

## WebApp [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/model_updating/\#webapp "Direct link to WebApp")

The model appears in the task's **ARTIFACTS** tab.

![Task artifacts](https://clear.ml/docs/latest/assets/images/examples_model_update_artifacts-4aa88c1bd56adda731cf30b097241d82.png#light-mode-only)![Task artifacts](https://clear.ml/docs/latest/assets/images/examples_model_update_artifacts_dark-3fd95882351221beb81f96759adf2284.png#dark-mode-only)

Clicking on the model name takes you to the [model's page](https://clear.ml/docs/latest/docs/webapp/webapp_model_viewing), where you can view the
model's details and access the model.

![Model page](https://clear.ml/docs/latest/assets/images/examples_model_update_model-e9fc12d56774cb64ea95b43296d101af.png#light-mode-only)![Model page](https://clear.ml/docs/latest/assets/images/examples_model_update_model_dark-c1d8c1beef8f43a9ccf1289a96a0c83d.png#dark-mode-only)

The model's **NETWORK** tab displays its configuration.

![Model network tab](https://clear.ml/docs/latest/assets/images/examples_model_update_network-1b7ab06799f30b8aaf0dbb29263fe867.png#light-mode-only)![Model network tab](https://clear.ml/docs/latest/assets/images/examples_model_update_network_dark-740c817a6636fe11ad71b06b033330b5.png#dark-mode-only)

The model's **LABELS** tab displays its label enumeration.

![Model labels](https://clear.ml/docs/latest/assets/images/examples_model_update_labels-a73c93621a8b8f76edd9329b3edb6ab9.png#light-mode-only)![Model labels](https://clear.ml/docs/latest/assets/images/examples_model_update_labels_dark-5c8ec83b6d692bf254412a3bfe28f85d.png#dark-mode-only)

- [Initialization](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/model_updating/#initialization)
- [Label Enumeration](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/model_updating/#label-enumeration)
- [Model Configuration](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/model_updating/#model-configuration)
- [Updating Models](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/model_updating/#updating-models)
- [WebApp](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/model_updating/#webapp)