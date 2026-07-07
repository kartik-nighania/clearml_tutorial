---
url: "https://clear.ml/docs/latest/docs/guides/frameworks/tensorboardx/"
title: "TensorBoardX with PyTorch | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/frameworks/tensorboardx/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The [pytorch\_tensorboardX.py](https://github.com/clearml/clearml/blob/master/examples/frameworks/tensorboardx/pytorch_tensorboardX.py)
example demonstrates the integration of ClearML into code that uses PyTorch and TensorBoardX.

The script does the following:

- Trains a simple deep neural network on the PyTorch built-in [MNIST](https://pytorch.org/vision/stable/datasets.html#mnist) dataset
- Creates a task named `pytorch with tensorboardX` in the `examples` project
- ClearML automatically captures scalars and text logged using the TensorBoardX `SummaryWriter` object, and
the model created by PyTorch

## Scalars [​](https://clear.ml/docs/latest/docs/guides/frameworks/tensorboardx/\#scalars "Direct link to Scalars")

The loss and accuracy metric scalar plots appear in the task's page in the **ClearML web UI**, under
**SCALARS**. The also includes resource utilization plots, which are titled **:monitor: machine**.

![Scalars](https://clear.ml/docs/latest/assets/images/examples_pytorch_tensorboardx_03-cc9a52da470f480760c45916ad6e0809.png#light-mode-only)![Scalars](https://clear.ml/docs/latest/assets/images/examples_pytorch_tensorboardx_03_dark-54990fc149cbdef40f7d86d3ad1fb557.png#dark-mode-only)

## Hyperparameters [​](https://clear.ml/docs/latest/docs/guides/frameworks/tensorboardx/\#hyperparameters "Direct link to Hyperparameters")

ClearML automatically logs command line options defined with `argparse`. They appear in **CONFIGURATION** **>** **HYPERPARAMETERS** **>** **Args**.

![Hyperparameters](https://clear.ml/docs/latest/assets/images/examples_pytorch_tensorboardx_01-bd775ece1ea5678715eb8c4f4039feef.png#light-mode-only)![Hyperparameters](https://clear.ml/docs/latest/assets/images/examples_pytorch_tensorboardx_01_dark-a98570338b26d9b73d508eee186e7c15.png#dark-mode-only)

## Console [​](https://clear.ml/docs/latest/docs/guides/frameworks/tensorboardx/\#console "Direct link to Console")

Text printed to the console for training progress, as well as all other console output, appear in **CONSOLE**.

![Console log](https://clear.ml/docs/latest/assets/images/examples_pytorch_tensorboardx_02-f341703ffa43a8dbdecbf037f8cb6ad3.png#light-mode-only)![Console log](https://clear.ml/docs/latest/assets/images/examples_pytorch_tensorboardx_02_dark-c5a472d4098aa74c874e0eb09b56ced7.png#dark-mode-only)

## Artifacts [​](https://clear.ml/docs/latest/docs/guides/frameworks/tensorboardx/\#artifacts "Direct link to Artifacts")

Models created by the task appear in the task's **ARTIFACTS** tab. ClearML automatically logs and tracks
models and any snapshots created using PyTorch.

![Artifacts](https://clear.ml/docs/latest/assets/images/examples_pytorch_tensorboardx_04-4d849d46e719e1e284d63792fce4426c.png#light-mode-only)![Artifacts](https://clear.ml/docs/latest/assets/images/examples_pytorch_tensorboardx_04_dark-6dce9147f1e29ccd57d8daeb1a7c0944.png#dark-mode-only)

Clicking on the model's name takes you to the [model's page](https://clear.ml/docs/latest/docs/webapp/webapp_model_viewing), where you can
view the model's details and access the model.

![Model details](https://clear.ml/docs/latest/assets/images/examples_pytorch_tensorboardx_model-e26fad89151e36079557d9438c0d3bd6.png#light-mode-only)![Model details](https://clear.ml/docs/latest/assets/images/examples_pytorch_tensorboardx_model_dark-e0bfe8a7592be6eb89f0a070ca83448e.png#dark-mode-only)

- [Scalars](https://clear.ml/docs/latest/docs/guides/frameworks/tensorboardx/#scalars)
- [Hyperparameters](https://clear.ml/docs/latest/docs/guides/frameworks/tensorboardx/#hyperparameters)
- [Console](https://clear.ml/docs/latest/docs/guides/frameworks/tensorboardx/#console)
- [Artifacts](https://clear.ml/docs/latest/docs/guides/frameworks/tensorboardx/#artifacts)