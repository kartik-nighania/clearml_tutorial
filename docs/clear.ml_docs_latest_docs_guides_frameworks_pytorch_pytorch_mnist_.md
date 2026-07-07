---
url: "https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/pytorch_mnist/"
title: "PyTorch MNIST | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/pytorch_mnist/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The [pytorch\_mnist.py](https://github.com/clearml/clearml/blob/master/examples/frameworks/pytorch/pytorch_mnist.py) example
demonstrates the integration of ClearML into code that uses PyTorch.

The example script does the following:

- Trains a simple deep neural network on the PyTorch built-in [MNIST](https://pytorch.org/vision/stable/datasets.html#mnist)
dataset.
- Creates a task named `pytorch mnist train` in the `examples` project.
- ClearML automatically logs `argparse` command line options, and models (and their snapshots) created by PyTorch.
- Additional metrics are logged by calling [`Logger.report_scalar()`](https://clear.ml/docs/latest/docs/references/sdk/logger#report_scalar).

## Scalars [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/pytorch_mnist/\#scalars "Direct link to Scalars")

In the example script's `train` function, the following code explicitly reports scalars to ClearML:

```python
Logger.current_logger().report_scalar(

    "train", "loss", iteration=(epoch * len(train_loader) + batch_idx), value=loss.item()

)
```

In the `test` method, the code explicitly reports `loss` and `accuracy` scalars.

```python
Logger.current_logger().report_scalar(

    "test", "loss", iteration=epoch, value=test_loss

)

Logger.current_logger().report_scalar(

    "test", "accuracy", iteration=epoch, value=(correct / len(test_loader.dataset))

)
```

These scalars can be visualized in plots, which appear in the ClearML [web UI](https://clear.ml/docs/latest/docs/webapp/webapp_overview),
in the task's **SCALARS** tab.

![Scalars](https://clear.ml/docs/latest/assets/images/examples_pytorch_mnist_07-7a449692f9d3feb79b8e9e5e519cc5e4.png#light-mode-only)![Scalars](https://clear.ml/docs/latest/assets/images/examples_pytorch_mnist_07_dark-eb096d9773c37e3cccc508159ef1d6c1.png#dark-mode-only)

## Hyperparameters [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/pytorch_mnist/\#hyperparameters "Direct link to Hyperparameters")

ClearML automatically logs command line options defined with `argparse`. They appear in **CONFIGURATION** **>** **HYPERPARAMETERS** **>** **Args**.

![Hyperparameters](https://clear.ml/docs/latest/assets/images/examples_pytorch_mnist_01-3967d61d03d54b5686dd5a9d904031b4.png#light-mode-only)![Hyperparameters](https://clear.ml/docs/latest/assets/images/examples_pytorch_mnist_01_dark-7c734374621596c90ecae6a03650f89e.png#dark-mode-only)

## Console [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/pytorch_mnist/\#console "Direct link to Console")

Text printed to the console for training progress, as well as all other console output, appear in **CONSOLE**.

![Console Log](https://clear.ml/docs/latest/assets/images/examples_pytorch_mnist_06-3bf370af437ddc31f0b970a31bd6986c.png#light-mode-only)![Console Log](https://clear.ml/docs/latest/assets/images/examples_pytorch_mnist_06_dark-c5b3194d24eb5a72dddbca797610b0ec.png#dark-mode-only)

## Artifacts [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/pytorch_mnist/\#artifacts "Direct link to Artifacts")

Models created by the task appear in the task's **ARTIFACTS** tab. ClearML automatically logs and tracks models
and any snapshots created using PyTorch.

![Models](https://clear.ml/docs/latest/assets/images/examples_pytorch_mnist_02-b82245224aca98abc9bfd91d890a151e.png#light-mode-only)![Models](https://clear.ml/docs/latest/assets/images/examples_pytorch_mnist_02_dark-622ecb0823e0d0835b812044433111d8.png#dark-mode-only)

Clicking on the model name takes you to the [model's page](https://clear.ml/docs/latest/docs/webapp/webapp_model_viewing), where you can view
the model's details and access the model.

![Model details](https://clear.ml/docs/latest/assets/images/examples_pytorch_mnist_03-2955e516115a32855555a4093f092ecf.png#light-mode-only)![Model details](https://clear.ml/docs/latest/assets/images/examples_pytorch_mnist_03_dark-2331ac2c2ad776a6f290173140a4a673.png#dark-mode-only)

- [Scalars](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/pytorch_mnist/#scalars)
- [Hyperparameters](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/pytorch_mnist/#hyperparameters)
- [Console](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/pytorch_mnist/#console)
- [Artifacts](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/pytorch_mnist/#artifacts)