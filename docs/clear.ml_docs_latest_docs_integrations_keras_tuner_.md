---
url: "https://clear.ml/docs/latest/docs/integrations/keras_tuner/"
title: "Keras Tuner | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/integrations/keras_tuner/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

tip

If you are not already using ClearML, see [ClearML Setup instructions](https://clear.ml/docs/latest/docs/clearml_sdk/clearml_sdk_setup).

[Keras Tuner](https://www.tensorflow.org/tutorials/keras/keras_tuner) is a library that helps you pick the optimal set
of hyperparameters for training your models. ClearML integrates seamlessly with `kerastuner` and automatically logs
task scalars, the output model, and hyperparameter optimization summary.

Integrate ClearML into your Keras Tuner optimization script by doing the following:

- Instantiate a ClearML Task:





```python
from clearml import Task

task = Task.init(task_name="<task_name>", project_name="<project_name>")
```

- Specify `ClearMLTunerLogger` as the Keras Tuner logger:





```python
from clearml.external.kerastuner import ClearmlTunerLogger

import keras_tuner as kt



# Create tuner object

tuner = kt.Hyperband(

     build_model,

     project_name='kt examples',

     logger=ClearMLTunerLogger(),    # specify ClearMLTunerLogger

     objective='val_accuracy',

     max_epochs=10,

     hyperband_iterations=6

)
```


And that's it! This creates a [ClearML Task](https://clear.ml/docs/latest/docs/fundamentals/task) which captures:

- Output Keras model
- Optimization trial scalars - scalar plot showing metrics for all runs
- Hyperparameter optimization summary plot - Tabular summary of hyperparameters tested and their metrics by trial ID
- Source code and uncommitted changes
- Installed packages
- TensorFlow definitions
- Console output
- General details such as machine details, runtime, creation date etc.
- And more

You can view all the task details in the [WebApp](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual).

## WebApp [​](https://clear.ml/docs/latest/docs/integrations/keras_tuner/\#webapp "Direct link to WebApp")

ClearML logs the scalars from training each network. They appear in the task's **SCALARS** tab in the Web UI.

![Optimization scalars](https://clear.ml/docs/latest/assets/images/integration_keras_tuner_06-8ca4e2c20b5b51b9a0e23c0c7ac4ef29.png#light-mode-only)![Optimization scalars](https://clear.ml/docs/latest/assets/images/integration_keras_tuner_06_dark-e1ef64aeef29eed4e387c8f899b90f4f.png#dark-mode-only)

ClearML automatically logs the parameters of each task run in the hyperparameter search. They appear in tabular
form in the task's **PLOTS**.

![Optimization plot](https://clear.ml/docs/latest/assets/images/integration_keras_tuner_07-936198be54e00d4e855732ae6a903f82.png#light-mode-only)![Optimization plot](https://clear.ml/docs/latest/assets/images/integration_keras_tuner_07_dark-fdd1e9689b2be1ebd01619717282e422.png#dark-mode-only)

ClearML automatically stores the output model. It appears in the task's **ARTIFACTS** **>** **Output Model**.

![output model](https://clear.ml/docs/latest/assets/images/integration_keras_tuner_03-7f8b47c41edaed5c2b3ca88b1fd20b95.png#light-mode-only)![output model](https://clear.ml/docs/latest/assets/images/integration_keras_tuner_03_dark-d260c1ffe2431a34008416865fcd517e.png#dark-mode-only)

## Example [​](https://clear.ml/docs/latest/docs/integrations/keras_tuner/\#example "Direct link to Example")

See Keras Tuner and ClearML in action in the [keras\_tuner\_cifar.py](https://clear.ml/docs/latest/docs/guides/frameworks/tensorflow/integration_keras_tuner)
example script.

- [WebApp](https://clear.ml/docs/latest/docs/integrations/keras_tuner/#webapp)
- [Example](https://clear.ml/docs/latest/docs/integrations/keras_tuner/#example)