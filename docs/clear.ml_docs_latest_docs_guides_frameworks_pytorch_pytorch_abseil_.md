---
url: "https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/pytorch_abseil/"
title: "PyTorch Abseil | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/pytorch_abseil/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The [pytorch\_abseil.py](https://github.com/clearml/clearml/blob/master/examples/frameworks/pytorch/pytorch_abseil.py)
example demonstrates the integration of ClearML into code that uses PyTorch and [`absl.flags`](https://abseil.io/docs/python/guides/flags).

The example script does the following:

- Trains a simple deep neural network on the PyTorch built-in [MNIST](https://pytorch.org/vision/stable/datasets.html#mnist)
dataset
- Creates a task named `pytorch mnist train with abseil` in the `examples` project
- ClearML automatically logs the `absl.flags`, and the models (and their snapshots) created by PyTorch
- Additional metrics are logged by calling [`Logger.report_scalar()`](https://clear.ml/docs/latest/docs/references/sdk/logger#report_scalar)

## Scalars [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/pytorch_abseil/\#scalars "Direct link to Scalars")

In the example script's `train` function, the following code explicitly reports scalars to ClearML:

```python
Logger.current_logger().report_scalar(

    "train",

    "loss",

    iteration=(epoch * len(train_loader) + batch_idx),

    value=loss.item()

)
```

In the `test` method, the code explicitly reports `loss` and `accuracy` scalars.

```python
Logger.current_logger().report_scalar(

    "test", "loss", iteration=epoch, value=test_loss

)

Logger.current_logger().report_scalar(

    "test",

    "accuracy",

    iteration=epoch,

    value=(correct / len(test_loader.dataset))

)
```

These scalars can be visualized in plots, which appear in the [ClearML web UI](https://clear.ml/docs/latest/docs/webapp/webapp_overview), in
the task's **SCALARS** tab.

![Scalars](https://clear.ml/docs/latest/assets/images/examples_pytorch_mnist_07-7a449692f9d3feb79b8e9e5e519cc5e4.png#light-mode-only)![Scalars](https://clear.ml/docs/latest/assets/images/examples_pytorch_mnist_07_dark-eb096d9773c37e3cccc508159ef1d6c1.png#dark-mode-only)

## Hyperparameters [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/pytorch_abseil/\#hyperparameters "Direct link to Hyperparameters")

ClearML automatically logs command line options defined with abseil flags. They appear in **CONFIGURATION** **>** **HYPERPARAMETERS** **>** **TF\_DEFINE**.

![Hyperparameters](https://clear.ml/docs/latest/assets/images/examples_pytorch_abseil_params-f51b25a50d6ad9435f16d2154a077ed4.png#light-mode-only)![Hyperparameters](https://clear.ml/docs/latest/assets/images/examples_pytorch_abseil_params_dark-2fe88a4532f479fac648ebaef2c31262.png#dark-mode-only)

## Console [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/pytorch_abseil/\#console "Direct link to Console")

Text printed to the console for training progress, as well as all other console output, appear in **CONSOLE**.

![Console](https://clear.ml/docs/latest/assets/images/examples_pytorch_mnist_06-3bf370af437ddc31f0b970a31bd6986c.png#light-mode-only)![Console](https://clear.ml/docs/latest/assets/images/examples_pytorch_mnist_06_dark-c5b3194d24eb5a72dddbca797610b0ec.png#dark-mode-only)

## Artifacts [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/pytorch_abseil/\#artifacts "Direct link to Artifacts")

Models created by the task appear in the task's **ARTIFACTS** tab. ClearML automatically logs and tracks
models and any snapshots created using PyTorch.

![Artifacts](https://clear.ml/docs/latest/assets/images/examples_pytorch_abseil_models-86c2d21fe8bec0d4bafdb054aa7d8000.png#light-mode-only)![Artifacts](https://clear.ml/docs/latest/assets/images/examples_pytorch_abseil_models_dark-2b8e6d774a084540dc46dc8886571218.png#dark-mode-only)

Clicking on the model name takes you to the [model's page](https://clear.ml/docs/latest/docs/webapp/webapp_model_viewing), where you can view
the model's details and access the model.

![Model](https://clear.ml/docs/latest/assets/images/examples_pytorch_abseil_models_2-71f5dd52e4c940a8fbc5d3ff6b07a31c.png#light-mode-only)![Model](https://clear.ml/docs/latest/assets/images/examples_pytorch_abseil_models_2_dark-158ffd0353275ad8bf7dc872fc64fb0f.png#dark-mode-only)

- [Scalars](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/pytorch_abseil/#scalars)
- [Hyperparameters](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/pytorch_abseil/#hyperparameters)
- [Console](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/pytorch_abseil/#console)
- [Artifacts](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/pytorch_abseil/#artifacts)