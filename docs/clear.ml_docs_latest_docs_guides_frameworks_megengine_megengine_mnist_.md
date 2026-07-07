---
url: "https://clear.ml/docs/latest/docs/guides/frameworks/megengine/megengine_mnist/"
title: "MegEngine | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/frameworks/megengine/megengine_mnist/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The [megengine\_mnist.py](https://github.com/clearml/clearml/blob/master/examples/frameworks/megengine/megengine_mnist.py)
example demonstrates the integration of ClearML into code that uses [MegEngine](https://github.com/MegEngine/MegEngine)
and [TensorBoardX](https://github.com/lanpa/tensorboardX). ClearML automatically captures models saved with `megengine`.

The example script does the following:

- Trains a simple deep neural network on MegEngine's built-in [MNIST](https://github.com/MegEngine/MegEngine/blob/master/imperative/python/megengine/data/dataset/vision/mnist.py)
dataset.
- Creates a TensorBoardX `SummaryWriter` object to log scalars during training.
- Creates a ClearML task named `megengine mnist train` in the `examples` project.

## Hyperparameters [​](https://clear.ml/docs/latest/docs/guides/frameworks/megengine/megengine_mnist/\#hyperparameters "Direct link to Hyperparameters")

ClearML automatically logs command line options defined with `argparse`. They appear in the task's **CONFIGURATION**
tab under **HYPERPARAMETERS** **>** **Args**.

![Configuration tab](https://clear.ml/docs/latest/assets/images/examples_megengine_mnist_config-7d7d019a64691fbdd21f4402f750396f.png#light-mode-only)![Configuration tab](https://clear.ml/docs/latest/assets/images/examples_megengine_mnist_config_dark-ba4d0e694c62e611194abd125252be9c.png#dark-mode-only)

## Scalars [​](https://clear.ml/docs/latest/docs/guides/frameworks/megengine/megengine_mnist/\#scalars "Direct link to Scalars")

The example script's `train` function calls TensorBoardX's `SummaryWriter.add_scalar` method to report `loss`.
ClearML automatically captures the data that is added to the `SummaryWriter` object.

These scalars can be visualized in plots, which appear in the ClearML [WebApp](https://clear.ml/docs/latest/docs/webapp/webapp_home), in the
task's **SCALARS** tab.

![Scalars tab](https://clear.ml/docs/latest/assets/images/examples_megengine_mnist_scalars-042d709f640d73f782b31e9a47452f5c.png#light-mode-only)![Scalars tab](https://clear.ml/docs/latest/assets/images/examples_megengine_mnist_scalars_dark-ce0a9a3f11562cfe5f0b91c9a45d8ff2.png#dark-mode-only)

## Models [​](https://clear.ml/docs/latest/docs/guides/frameworks/megengine/megengine_mnist/\#models "Direct link to Models")

ClearML automatically captures the model logged using the `megengine.save` method, and saves it as an artifact.

View saved snapshots in the task's **ARTIFACTS** tab.

![Artifacts tab](https://clear.ml/docs/latest/assets/images/examples_megengine_models_1-5058ead4b86aead9a4414feef9d44334.png#light-mode-only)![Artifacts tab](https://clear.ml/docs/latest/assets/images/examples_megengine_models_1_dark-78213c62413b1789ed7ef55745f1ec87.png#dark-mode-only)

To view the model details, click the model name in the **ARTIFACTS** page, which will open the model's info tab. Alternatively, download the model.

The model info panel contains the model details, including:

- Model URL
- Framework
- Snapshot locations.

![Model info panel](https://clear.ml/docs/latest/assets/images/examples_megengine_models_2-cace8836c21b944ce3a6dc4781214f43.png#light-mode-only)![Model info panel](https://clear.ml/docs/latest/assets/images/examples_megengine_models_2_dark-ac5d7b7ac02f8a08244b67de830c7768.png#dark-mode-only)

## Console [​](https://clear.ml/docs/latest/docs/guides/frameworks/megengine/megengine_mnist/\#console "Direct link to Console")

All console output during the script's execution appears in the task's **CONSOLE** page.

![Console tab](https://clear.ml/docs/latest/assets/images/examples_megengine_console-e4841575d4238409e5759601afe79dc1.png#light-mode-only)![Console tab](https://clear.ml/docs/latest/assets/images/examples_megengine_console_dark-f70672eb872d614ed8179cdf216b5817.png#dark-mode-only)

- [Hyperparameters](https://clear.ml/docs/latest/docs/guides/frameworks/megengine/megengine_mnist/#hyperparameters)
- [Scalars](https://clear.ml/docs/latest/docs/guides/frameworks/megengine/megengine_mnist/#scalars)
- [Models](https://clear.ml/docs/latest/docs/guides/frameworks/megengine/megengine_mnist/#models)
- [Console](https://clear.ml/docs/latest/docs/guides/frameworks/megengine/megengine_mnist/#console)