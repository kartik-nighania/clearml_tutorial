---
url: "https://clear.ml/docs/latest/docs/guides/frameworks/xgboost/xgboost_sample/"
title: "XGBoost and scikit-learn | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/frameworks/xgboost/xgboost_sample/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The [xgboost\_sample.py](https://github.com/clearml/clearml/blob/master/examples/frameworks/xgboost/xgboost_sample.py)
example demonstrates integrating ClearML into code that uses [XGBoost](https://xgboost.readthedocs.io/en/stable/).

The example does the following:

- Trains a network on the scikit-learn [iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris)
classification dataset using XGBoost
- Scores accuracy using scikit-learn
- ClearML automatically logs the input model registered by XGBoost, and the output model (and its checkpoints),
feature importance plot, and tree plot created with XGBoost.
- Creates a task named `XGBoost simple example` in the `examples` project.

## Plots [​](https://clear.ml/docs/latest/docs/guides/frameworks/xgboost/xgboost_sample/\#plots "Direct link to Plots")

The feature importance plot and tree plot appear in the task's page in the **ClearML web UI**, under
**PLOTS**.

![Feature importance plot](https://clear.ml/docs/latest/assets/images/examples_xgboost_sample_06-07c4ba0bf9b444e05ed3579405d1efc6.png#light-mode-only)![Feature importance plot](https://clear.ml/docs/latest/assets/images/examples_xgboost_sample_06_dark-e07455fd8c454d4b1f24e887699ae006.png#dark-mode-only)

![Tree plot](https://clear.ml/docs/latest/assets/images/examples_xgboost_sample_06a-c9328005f0ca95e46873534d251637b2.png#light-mode-only)![Tree plot](https://clear.ml/docs/latest/assets/images/examples_xgboost_sample_06a_dark-72ab643ff3988f29c2d75b922c00b166.png#dark-mode-only)

## Console [​](https://clear.ml/docs/latest/docs/guides/frameworks/xgboost/xgboost_sample/\#console "Direct link to Console")

All other console output appear in **CONSOLE**.

![Console log](https://clear.ml/docs/latest/assets/images/examples_xgboost_sample_05-e8cdaeca88d24e162b0bdcfd8698ac9a.png#light-mode-only)![Console log](https://clear.ml/docs/latest/assets/images/examples_xgboost_sample_05_dark-8288889496b2d7929c1509dde764509e.png#dark-mode-only)

## Artifacts [​](https://clear.ml/docs/latest/docs/guides/frameworks/xgboost/xgboost_sample/\#artifacts "Direct link to Artifacts")

Models created by the task appear in the task's **ARTIFACTS** tab. ClearML automatically logs and tracks
models and any snapshots created using XGBoost.

![Artifacts](https://clear.ml/docs/latest/assets/images/examples_xgboost_sample_10-015b4966439c369bbb1a023317266f4a.png#light-mode-only)![Artifacts](https://clear.ml/docs/latest/assets/images/examples_xgboost_sample_10_dark-483c06bfc8980abd76f72ad6ac037ad9.png#dark-mode-only)

Clicking on the model's name takes you to the [model's page](https://clear.ml/docs/latest/docs/webapp/webapp_model_viewing), where you can
view the model's details and access the model.

![Model details](https://clear.ml/docs/latest/assets/images/examples_xgboost_sample_03-5029de84ba89d14d7dc4171bd9b651f2.png#light-mode-only)![Model details](https://clear.ml/docs/latest/assets/images/examples_xgboost_sample_03_dark-653878257473f2bd2081d746f8c50c68.png#dark-mode-only)

- [Plots](https://clear.ml/docs/latest/docs/guides/frameworks/xgboost/xgboost_sample/#plots)
- [Console](https://clear.ml/docs/latest/docs/guides/frameworks/xgboost/xgboost_sample/#console)
- [Artifacts](https://clear.ml/docs/latest/docs/guides/frameworks/xgboost/xgboost_sample/#artifacts)