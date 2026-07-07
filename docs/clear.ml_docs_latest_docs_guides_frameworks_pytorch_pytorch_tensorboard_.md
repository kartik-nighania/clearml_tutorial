---
url: "https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/pytorch_tensorboard/"
title: "PyTorch with TensorBoard | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/pytorch_tensorboard/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The [pytorch\_tensorboard.py](https://github.com/clearml/clearml/blob/master/examples/frameworks/pytorch/pytorch_tensorboard.py)
example demonstrates the integration of ClearML into code that uses PyTorch and TensorBoard.

The example does the following:

- Trains a simple deep neural network on the PyTorch built-in [MNIST](https://pytorch.org/vision/stable/datasets.html#mnist)
dataset.
- Creates a task named `pytorch with tensorboard` in the `examples` project.
- ClearML automatically captures scalars and text logged using the TensorBoard `SummaryWriter` object, and
the model created by PyTorch.

## Scalars [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/pytorch_tensorboard/\#scalars "Direct link to Scalars")

In the example script, the `train` and `test` functions call the TensorBoard `SummaryWriter.add_scalar` method to log loss.
These scalars, along with the resource utilization plots, which are titled **:monitor: machine**, appear in the task's
page in the [ClearML web UI](https://clear.ml/docs/latest/docs/webapp/webapp_overview) under **SCALARS**.

![Scalars](https://clear.ml/docs/latest/assets/images/examples_pytorch_tensorboard_07-2a202931fe27a0a8258619bd09f8f7ce.png#light-mode-only)![Scalars](https://clear.ml/docs/latest/assets/images/examples_pytorch_tensorboard_07_dark-b77a7e8387c60dea1ebe4f10e428d36a.png#dark-mode-only)

## Debug Samples [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/pytorch_tensorboard/\#debug-samples "Direct link to Debug Samples")

ClearML automatically tracks images and text output to TensorFlow. They appear in **DEBUG SAMPLES**.

![Debug Samples](https://clear.ml/docs/latest/assets/images/examples_pytorch_tensorboard_08-d87bad802328b87a72dd4d2373b668d3.png#light-mode-only)![Debug Samples](https://clear.ml/docs/latest/assets/images/examples_pytorch_tensorboard_08_dark-3d3b737af2e500e826e9c40fc5b73136.png#dark-mode-only)

## Hyperparameters [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/pytorch_tensorboard/\#hyperparameters "Direct link to Hyperparameters")

ClearML automatically logs TensorFlow Definitions. They appear in **CONFIGURATION** **>** **HYPERPARAMETERS** **>** **TF\_DEFINE**.

![Hyperparameters](https://clear.ml/docs/latest/assets/images/examples_pytorch_tensorboard_01-88171ffdf97930b5c72b9c71f0a095db.png#light-mode-only)![Hyperparameters](https://clear.ml/docs/latest/assets/images/examples_pytorch_tensorboard_01_dark-19c761bf505b8f0ad03c06b98b0e2be6.png#dark-mode-only)

## Console [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/pytorch_tensorboard/\#console "Direct link to Console")

Text printed to the console for training progress, as well as all other console output, appear in **CONSOLE**.

![Console Log](https://clear.ml/docs/latest/assets/images/examples_pytorch_tensorboard_06-28989392407c26f851ab87bf47f4c4eb.png#light-mode-only)![Console Log](https://clear.ml/docs/latest/assets/images/examples_pytorch_tensorboard_06_dark-95c770713f673a663a80d78492b1e849.png#dark-mode-only)

## Artifacts [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/pytorch_tensorboard/\#artifacts "Direct link to Artifacts")

Models created by the task appear in the task's **ARTIFACTS** tab. ClearML automatically logs and tracks
models and any snapshots created using PyTorch.

![Artifacts](https://clear.ml/docs/latest/assets/images/examples_pytorch_tensorboard_02-cb96ee7fe6015ab9aa4302004dbdd448.png#light-mode-only)![Artifacts](https://clear.ml/docs/latest/assets/images/examples_pytorch_tensorboard_02_dark-08e63da7a9e7a8eab94250f712abdc2e.png#dark-mode-only)

Clicking on a model's name takes you to the [model's page](https://clear.ml/docs/latest/docs/webapp/webapp_model_viewing), where you can view
the model's details and access the model.

![Model details](https://clear.ml/docs/latest/assets/images/examples_pytorch_tensorboard_03-4ce642cfedc1caa733952800afbadd97.png#light-mode-only)![Model details](https://clear.ml/docs/latest/assets/images/examples_pytorch_tensorboard_03_dark-19b96c1450df1eef2a6392de5668ceea.png#dark-mode-only)

- [Scalars](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/pytorch_tensorboard/#scalars)
- [Debug Samples](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/pytorch_tensorboard/#debug-samples)
- [Hyperparameters](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/pytorch_tensorboard/#hyperparameters)
- [Console](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/pytorch_tensorboard/#console)
- [Artifacts](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/pytorch_tensorboard/#artifacts)