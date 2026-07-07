---
url: "https://clear.ml/docs/latest/docs/guides/frameworks/lightgbm/lightgbm_example/"
title: "LightGBM | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/frameworks/lightgbm/lightgbm_example/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The [lightgbm\_example](https://github.com/clearml/clearml/blob/master/examples/frameworks/lightgbm/lightgbm_example.py)
script demonstrates the integration of ClearML into code that uses LightGBM.

The example script does the following:

- Creates a dataset for LightGBM to train a model
- Specifies configuration which are automatically captured by ClearML
- Saves model which ClearML automatically captures
- Creates a task named `LightGBM` in the `examples` project.

## Scalars [​](https://clear.ml/docs/latest/docs/guides/frameworks/lightgbm/lightgbm_example/\#scalars "Direct link to Scalars")

The scalars logged in the task can be visualized in a plot, which appears in the ClearML web UI, in the task's **SCALARS** tab.

![LightGBM scalars](https://clear.ml/docs/latest/assets/images/examples_lightgbm_scalars-de21074edc9f73d3db91bc0be759b5ae.png#light-mode-only)![LightGBM scalars](https://clear.ml/docs/latest/assets/images/examples_lightgbm_scalars_dark-d6aa766b075488c9b8e77c5343d24e5e.png#dark-mode-only)

## Hyperparameters [​](https://clear.ml/docs/latest/docs/guides/frameworks/lightgbm/lightgbm_example/\#hyperparameters "Direct link to Hyperparameters")

ClearML automatically logs the configurations applied to LightGBM. They appear in **CONFIGURATIONS > HYPERPARAMETERS > GENERAL**.

![LightGBM hyperparameters](https://clear.ml/docs/latest/assets/images/examples_lightgbm_config-2f743aa926f1b8dbc6b4f256075925de.png#light-mode-only)![LightGBM hyperparameters](https://clear.ml/docs/latest/assets/images/examples_lightgbm_config_dark-2cd22960eaa2204b7979ac5324c21dbc.png#dark-mode-only)

## Artifacts [​](https://clear.ml/docs/latest/docs/guides/frameworks/lightgbm/lightgbm_example/\#artifacts "Direct link to Artifacts")

Models created by the task appear in the task's **ARTIFACTS** tab. ClearML automatically logs and tracks
models and any snapshots created using LightGBM.

![LightGBM model](https://clear.ml/docs/latest/assets/images/examples_lightgbm_model-0576bbe620710d5b604980b225d81f0d.png#light-mode-only)![LightGBM model](https://clear.ml/docs/latest/assets/images/examples_lightgbm_model_dark-fd74b1e30dbd1430a91dd62ef796f7bb.png#dark-mode-only)

## Console [​](https://clear.ml/docs/latest/docs/guides/frameworks/lightgbm/lightgbm_example/\#console "Direct link to Console")

All other console output appears in **CONSOLE**.

![LightGBM console](https://clear.ml/docs/latest/assets/images/examples_lightgbm_console-15595027f153d5aacacb2ba6b15ea127.png#light-mode-only)![LightGBM console](https://clear.ml/docs/latest/assets/images/examples_lightgbm_console_dark-c49ef67bc0c0e636372b442048e11a8c.png#dark-mode-only)

- [Scalars](https://clear.ml/docs/latest/docs/guides/frameworks/lightgbm/lightgbm_example/#scalars)
- [Hyperparameters](https://clear.ml/docs/latest/docs/guides/frameworks/lightgbm/lightgbm_example/#hyperparameters)
- [Artifacts](https://clear.ml/docs/latest/docs/guides/frameworks/lightgbm/lightgbm_example/#artifacts)
- [Console](https://clear.ml/docs/latest/docs/guides/frameworks/lightgbm/lightgbm_example/#console)