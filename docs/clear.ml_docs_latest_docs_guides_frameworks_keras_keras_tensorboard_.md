---
url: "https://clear.ml/docs/latest/docs/guides/frameworks/keras/keras_tensorboard/"
title: "Keras with TensorBoard | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/frameworks/keras/keras_tensorboard/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The example below demonstrates the integration of ClearML into code which uses Keras and TensorBoard.
View it in [script](https://github.com/clearml/clearml/blob/master/examples/frameworks/keras/keras_tensorboard.py)
or in [Jupyter Notebook](https://github.com/clearml/clearml/blob/master/examples/frameworks/keras/jupyter_keras_TB_example.ipynb).

note

The example in [Jupyter Notebook](https://github.com/clearml/clearml/blob/master/examples/frameworks/keras/jupyter_keras_TB_example.ipynb)
includes a clickable icon to open the notebook in Google Colab.

The example script does the following:

1. Trains a simple deep neural network on the Keras built-in [MNIST](https://keras.io/api/datasets/mnist/#load_data-function)
dataset.
2. Builds a sequential model using a categorical cross entropy loss objective function.
3. Specifies accuracy as the metric, and uses two callbacks: a TensorBoard callback and a model checkpoint callback.
4. During script execution, creates a task named `Keras with TensorBoard example` in the
`examples` project (in script) or the `Colab notebooks` project (in Jupyter Notebook).

## Scalars [​](https://clear.ml/docs/latest/docs/guides/frameworks/keras/keras_tensorboard/\#scalars "Direct link to Scalars")

The loss and accuracy metric scalar plots appear in **SCALARS**, along with the resource utilization plots,
which are titled **:monitor: machine**.

![Scalars](https://clear.ml/docs/latest/assets/images/examples_keras_01-a7c44feb47e20400f2a7ea75041d0519.png#light-mode-only)![Scalars](https://clear.ml/docs/latest/assets/images/examples_keras_01_dark-f7f7fd3c8efd6e9d58559123f6f83b23.png#dark-mode-only)

## Histograms [​](https://clear.ml/docs/latest/docs/guides/frameworks/keras/keras_tensorboard/\#histograms "Direct link to Histograms")

Histograms for layer density appear in **PLOTS**.

![Histograms](https://clear.ml/docs/latest/assets/images/examples_keras_02-a2475621329e11c941c911d03821cbff.png#light-mode-only)![Histograms](https://clear.ml/docs/latest/assets/images/examples_keras_02_dark-d5d56e70e1bbeea58c93ae4a239cd036.png#dark-mode-only)

## Hyperparameters [​](https://clear.ml/docs/latest/docs/guides/frameworks/keras/keras_tensorboard/\#hyperparameters "Direct link to Hyperparameters")

ClearML automatically logs command line options generated with `argparse` and TensorFlow Definitions.

Command line options appear in **CONFIGURATION** **>** **HYPERPARAMETERS** **>** **Args**.

![Hyperparameters Args](https://clear.ml/docs/latest/assets/images/examples_keras_00-b354eeffd9736b2090a05e9bc83df0a0.png#light-mode-only)![Hyperparameters Args](https://clear.ml/docs/latest/assets/images/examples_keras_00_dark-f932a9873d2ceb5d067eb4e768fa968a.png#dark-mode-only)

TensorFlow Definitions appear in **TF\_DEFINE**.

![TF Defines](https://clear.ml/docs/latest/assets/images/examples_keras_00a-9de274029095433447dc751bcc111413.png#light-mode-only)![TF Defines](https://clear.ml/docs/latest/assets/images/examples_keras_00a_dark-84fddf738815b7fce15db1abf9e9e4c2.png#dark-mode-only)

## Console [​](https://clear.ml/docs/latest/docs/guides/frameworks/keras/keras_tensorboard/\#console "Direct link to Console")

Text printed to the console for training progress, as well as all other console output, appear in **CONSOLE**.

![Console Log](https://clear.ml/docs/latest/assets/images/keras_colab_01-b9af8ee108ebc6c1e1a3c52ebf42953e.png#light-mode-only)![Console Log](https://clear.ml/docs/latest/assets/images/keras_colab_01_dark-32e9665920dfd5d2b552d9f025cee010.png#dark-mode-only)

## Configuration Objects [​](https://clear.ml/docs/latest/docs/guides/frameworks/keras/keras_tensorboard/\#configuration-objects "Direct link to Configuration Objects")

A configuration dictionary is connected to the Task by calling [`Task.connect()`](https://clear.ml/docs/latest/docs/references/sdk/task#connect).

```python
task.connect_configuration(

   name="MyConfig",

   configuration={'test': 1337, 'nested': {'key': 'value', 'number': 1}}

)
```

It appears in **CONFIGURATION** **>** **CONFIGURATION OBJECTS** **>** **MyConfig**.

![Custom configuration](https://clear.ml/docs/latest/assets/images/keras_colab_02-c07e3eb78818993ecfd2dc200cd20f03.png#light-mode-only)![Custom configuration](https://clear.ml/docs/latest/assets/images/keras_colab_02_dark-b6ae5177e37f2ea3d8ef5faad848967d.png#dark-mode-only)

- [Scalars](https://clear.ml/docs/latest/docs/guides/frameworks/keras/keras_tensorboard/#scalars)
- [Histograms](https://clear.ml/docs/latest/docs/guides/frameworks/keras/keras_tensorboard/#histograms)
- [Hyperparameters](https://clear.ml/docs/latest/docs/guides/frameworks/keras/keras_tensorboard/#hyperparameters)
- [Console](https://clear.ml/docs/latest/docs/guides/frameworks/keras/keras_tensorboard/#console)
- [Configuration Objects](https://clear.ml/docs/latest/docs/guides/frameworks/keras/keras_tensorboard/#configuration-objects)