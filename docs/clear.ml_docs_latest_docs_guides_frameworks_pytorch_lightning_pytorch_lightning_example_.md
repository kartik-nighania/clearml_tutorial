---
url: "https://clear.ml/docs/latest/docs/guides/frameworks/pytorch_lightning/pytorch_lightning_example/"
title: "PyTorch Lightning | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch_lightning/pytorch_lightning_example/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The [pytorch-lightning](https://github.com/clearml/clearml/blob/master/examples/frameworks/pytorch-lightning/pytorch_lightning_example.py)
script demonstrates the integration of ClearML into code that uses [PyTorch Lightning](https://www.pytorchlightning.ai/).

The example script does the following:

- Trains a simple deep neural network on the PyTorch built-in MNIST dataset
- Defines Argparse command line options, which are automatically captured by ClearML
- Creates a task named `pytorch lightning mnist example` in the `examples` project.

## Scalars [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch_lightning/pytorch_lightning_example/\#scalars "Direct link to Scalars")

The test loss and validation loss plots appear in the task's page in the ClearML web UI under **SCALARS**.
Resource utilization plots, which are titled **:monitor: machine**, also appear in the **SCALARS** tab. All of these
plots are automatically captured by ClearML.

![PyTorch Lightning scalars](https://clear.ml/docs/latest/assets/images/examples_pytorch_lightning_scalars-c1b1e4a59402def9bb62591b6d0e871e.png#light-mode-only)![PyTorch Lightning scalars](https://clear.ml/docs/latest/assets/images/examples_pytorch_lightning_scalars_dark-b725ebe4736f3b9242fc314bff8c3fde.png#dark-mode-only)

## Hyperparameters [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch_lightning/pytorch_lightning_example/\#hyperparameters "Direct link to Hyperparameters")

ClearML automatically logs command line options defined with argparse and TensorFlow Definitions, which appear in
**CONFIGURATIONS > HYPERPARAMETERS > Args** and **TF\_DEFINE** respectively.

![PyTorch Lightning parameters](https://clear.ml/docs/latest/assets/images/examples_pytorch_lightning_params-65ac9e7926b8499c29e50c6914e940d1.png#light-mode-only)![PyTorch Lightning parameters](https://clear.ml/docs/latest/assets/images/examples_pytorch_lightning_params_dark-b8d8c2e78150b6fd1f8b4ab6653281b5.png#dark-mode-only)

## Artifacts [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch_lightning/pytorch_lightning_example/\#artifacts "Direct link to Artifacts")

Models created by the task appear in the task's **ARTIFACTS** tab.

![PyTorch Lightning model](https://clear.ml/docs/latest/assets/images/examples_pytorch_lightning_model-11696af62cfd165aa62066ac176f7fa1.png#light-mode-only)![PyTorch Lightning model](https://clear.ml/docs/latest/assets/images/examples_pytorch_lightning_model_dark-4ab4918a01f44cf04f00163b5f59d959.png#dark-mode-only)

Clicking on a model name takes you to the [model's page](https://clear.ml/docs/latest/docs/webapp/webapp_model_viewing), where you can view
the model's details and access the model.

## Console [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch_lightning/pytorch_lightning_example/\#console "Direct link to Console")

All other console output appears in **CONSOLE**.

![PyTorch Lightning console](https://clear.ml/docs/latest/assets/images/examples_pytorch_lightning_console-49430cc3c737b04ee9191609c3708a14.png#light-mode-only)![PyTorch Lightning console](https://clear.ml/docs/latest/assets/images/examples_pytorch_lightning_console_dark-fa8c032edc9d821c510e53c849d2a21f.png#dark-mode-only)

- [Scalars](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch_lightning/pytorch_lightning_example/#scalars)
- [Hyperparameters](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch_lightning/pytorch_lightning_example/#hyperparameters)
- [Artifacts](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch_lightning/pytorch_lightning_example/#artifacts)
- [Console](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch_lightning/pytorch_lightning_example/#console)