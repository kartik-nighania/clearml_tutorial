---
url: "https://clear.ml/docs/latest/docs/fundamentals/models/"
title: "Models | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/fundamentals/models/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

ClearML supports tracking, updating, and visualizing models.

Models are stored in ClearML as experiment artifacts, but unlike other artifacts that are dependent on their creating
task, models are independent entities with their own unique ID. Models can be accessed directly with a model object or
indirectly via their creating task. This property makes Models a standalone entry that can be used as an artifactory
interface.

## Automatically Logging Models [​](https://clear.ml/docs/latest/docs/fundamentals/models/\#automatically-logging-models "Direct link to Automatically Logging Models")

Once integrated into code, ClearML automatically logs and tracks models and any snapshots created by the following
frameworks:

- [TensorFlow](https://clear.ml/docs/latest/docs/integrations/tensorflow)
- [Keras](https://clear.ml/docs/latest/docs/integrations/keras)
- [PyTorch](https://clear.ml/docs/latest/docs/integrations/pytorch)
- [scikit-learn](https://clear.ml/docs/latest/docs/integrations/scikit_learn) (only using joblib)
- [XGBoost](https://clear.ml/docs/latest/docs/integrations/xgboost) (only using joblib)
- [Fast.ai](https://clear.ml/docs/latest/docs/integrations/fastai)
- [MegEngine](https://clear.ml/docs/latest/docs/integrations/megengine)
- [CatBoost](https://clear.ml/docs/latest/docs/integrations/catboost)
- [MONAI](https://clear.ml/docs/latest/docs/integrations/monai)

When a supported framework loads a weights file, the running task will be automatically updated, with its input model
pointing directly to the original training task's model.

## Manually Logging Models [​](https://clear.ml/docs/latest/docs/fundamentals/models/\#manually-logging-models "Direct link to Manually Logging Models")

### Output Models [​](https://clear.ml/docs/latest/docs/fundamentals/models/\#output-models "Direct link to Output Models")

ClearML stores training results as output models. The `OutputModel` object is instantiated with a task object as an
argument (see [`task`](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel) parameter), so it's automatically registered as the Task's
output model. Since OutputModel objects are connected to tasks, the models are traceable in experiments.

Output models are read-write so weights can be updated throughout training. Additionally, users can specify a model's
network design and label enumeration. Once an output model is registered, it can be used as the input model for another
experiment.

The snapshots of manually uploaded models aren't automatically captured, but ClearML provides methods to update them
through a `Task` or `OutputModel` object.

### Input Models [​](https://clear.ml/docs/latest/docs/fundamentals/models/\#input-models "Direct link to Input Models")

ClearML provides flexibility for explicitly connecting input models and experimentation, including:

- Importing pre-trained models from external sources such as Amazon AWS, GIT repositories, PyTorch, and TensorFlow
- Using standalone models already registered in ClearML by previously run experiments
- Defining your own input models in scripts

## Setting Upload Destination [​](https://clear.ml/docs/latest/docs/fundamentals/models/\#setting-upload-destination "Direct link to Setting Upload Destination")

- ClearML automatically captures the storage path of Models created by supported frameworks. By default, it stores the
local path they are saved to.
- Upload destinations can be specified explicitly on a per OutputModel or per experiment basis. Alternatively, the upload
destination of all OutputModels can be specified in the ClearML [configuration file](https://clear.ml/docs/latest/docs/configs/clearml_conf).

## WebApp Interface [​](https://clear.ml/docs/latest/docs/fundamentals/models/\#webapp-interface "Direct link to WebApp Interface")

In the ClearML web UI, model information can be located through a project's Model Table or through the model's creating
task.

Models associated with a task appear in the task's **ARTIFACTS** tab. To see further model details, including design,
label enumeration, lineage, and general information, click the model name, which is a hyperlink to the
[model's detail page](https://clear.ml/docs/latest/docs/webapp/webapp_model_viewing).

Models can also be accessed through their associated project's [Model Table](https://clear.ml/docs/latest/docs/webapp/webapp_model_table), where all
the models associated with a project are listed.

![WebApp Model](https://clear.ml/docs/latest/assets/images/webapp_model_general-246ba0e91e712c4b542325b84f63bc1c.png#light-mode-only)![WebApp Model](https://clear.ml/docs/latest/assets/images/webapp_model_general_dark-88986e2821136707145f01dccbeae4f6.png#dark-mode-only)

## SDK Interface [​](https://clear.ml/docs/latest/docs/fundamentals/models/\#sdk-interface "Direct link to SDK Interface")

See [the Models SDK interface](https://clear.ml/docs/latest/docs/clearml_sdk/model_sdk) for an overview for using the most basic Pythonic methods of the model
classes. See a detailed list of all available methods in the [Model](https://clear.ml/docs/latest/docs/references/sdk/model_model), [OutputModel](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel), and [InputModel](https://clear.ml/docs/latest/docs/references/sdk/model_inputmodel)
reference pages.

- [Automatically Logging Models](https://clear.ml/docs/latest/docs/fundamentals/models/#automatically-logging-models)
- [Manually Logging Models](https://clear.ml/docs/latest/docs/fundamentals/models/#manually-logging-models)
  - [Output Models](https://clear.ml/docs/latest/docs/fundamentals/models/#output-models)
  - [Input Models](https://clear.ml/docs/latest/docs/fundamentals/models/#input-models)
- [Setting Upload Destination](https://clear.ml/docs/latest/docs/fundamentals/models/#setting-upload-destination)
- [WebApp Interface](https://clear.ml/docs/latest/docs/fundamentals/models/#webapp-interface)
- [SDK Interface](https://clear.ml/docs/latest/docs/fundamentals/models/#sdk-interface)