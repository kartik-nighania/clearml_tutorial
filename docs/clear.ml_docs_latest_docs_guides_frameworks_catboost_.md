---
url: "https://clear.ml/docs/latest/docs/guides/frameworks/catboost/"
title: "CatBoost | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/frameworks/catboost/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The [catboost\_example.py](https://github.com/clearml/clearml/blob/master/examples/frameworks/catboost/catboost_example.py)
example demonstrates the integration of ClearML into code that uses [CatBoost](https://catboost.ai/).

The example script does the following:

- Trains a simple deep neural network on the CatBoost built-in [msrank](https://catboost.ai/en/docs/concepts/python-reference_datasets_msrank)
dataset.
- Creates a task named `CatBoost simple example` in the `examples` project
- ClearML automatically logs argparse command line options, and models and metrics logged by CatBoost

## Scalars [​](https://clear.ml/docs/latest/docs/guides/frameworks/catboost/\#scalars "Direct link to Scalars")

ClearML automatically captures scalars logged by CatBoost. These scalars can be visualized in plots, which appear in the
[ClearML web UI](https://clear.ml/docs/latest/docs/webapp/webapp_overview), in the task's **SCALARS** tab.

![Task scalars](https://clear.ml/docs/latest/assets/images/examples_catboost_scalars-b5a6e3146596bc510451073de422b399.png#light-mode-only)![Task scalars](https://clear.ml/docs/latest/assets/images/examples_catboost_scalars_dark-6e94c3047535d847f263d33546820625.png#dark-mode-only)

## Hyperparameters [​](https://clear.ml/docs/latest/docs/guides/frameworks/catboost/\#hyperparameters "Direct link to Hyperparameters")

ClearML automatically logs command line options defined with argparse. They appear in **CONFIGURATIONS > HYPERPARAMETERS > Args**.

![Task hyperparameters](https://clear.ml/docs/latest/assets/images/examples_catboost_configurations-3d9a0e33427f8e3fafca4c4d5d440870.png#light-mode-only)![Task hyperparameters](https://clear.ml/docs/latest/assets/images/examples_catboost_configurations_dark-b0816f18190ac1db30e351db41ce16cd.png#dark-mode-only)

## Console [​](https://clear.ml/docs/latest/docs/guides/frameworks/catboost/\#console "Direct link to Console")

Text printed to the console for training progress, as well as all other console output, appear in **CONSOLE**.

![Task console](https://clear.ml/docs/latest/assets/images/examples_catboost_console-f956d257bb7a00019c83bf66eaed2a8e.png#light-mode-only)![Task console](https://clear.ml/docs/latest/assets/images/examples_catboost_console_dark-c7d6741cf9d77ca423045e9d19ff6a52.png#dark-mode-only)

## Artifacts [​](https://clear.ml/docs/latest/docs/guides/frameworks/catboost/\#artifacts "Direct link to Artifacts")

Models created by the task appear in the task's **ARTIFACTS** tab. ClearML automatically logs and tracks
models created using CatBoost.

![Task artifacts](https://clear.ml/docs/latest/assets/images/examples_catboost_artifacts-4c35517d8996773f206f09f1e06be64d.png#light-mode-only)![Task artifacts](https://clear.ml/docs/latest/assets/images/examples_catboost_artifacts_dark-9f2562393951c235108b62d647aad867.png#dark-mode-only)

Clicking on the model name takes you to the [model's page](https://clear.ml/docs/latest/docs/webapp/webapp_model_viewing), where you can view
the model's details and access the model.

![Model page](https://clear.ml/docs/latest/assets/images/examples_catboost_model-23ffeabd9047a2574db95757a0417cb2.png#light-mode-only)![Model page](https://clear.ml/docs/latest/assets/images/examples_catboost_model_dark-0636a2ad5ffed1a2d1d19a06e66cc942.png#dark-mode-only)

- [Scalars](https://clear.ml/docs/latest/docs/guides/frameworks/catboost/#scalars)
- [Hyperparameters](https://clear.ml/docs/latest/docs/guides/frameworks/catboost/#hyperparameters)
- [Console](https://clear.ml/docs/latest/docs/guides/frameworks/catboost/#console)
- [Artifacts](https://clear.ml/docs/latest/docs/guides/frameworks/catboost/#artifacts)