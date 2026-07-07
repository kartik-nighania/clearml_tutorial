---
url: "https://clear.ml/docs/latest/docs/guides/frameworks/xgboost/xgboost_metrics/"
title: "XGBoost Metrics | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/frameworks/xgboost/xgboost_metrics/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The [xgboost\_metrics.py](https://github.com/clearml/clearml/blob/master/examples/frameworks/xgboost/xgboost_metrics.py)
example demonstrates the integration of ClearML into code that uses XGBoost to train a network on the scikit-learn [iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris)
classification dataset. ClearML automatically captures models and scalars logged with XGBoost.

When the script runs, it creates a ClearML task named `xgboost metric auto reporting` in
the `examples` project.

## Scalars [​](https://clear.ml/docs/latest/docs/guides/frameworks/xgboost/xgboost_metrics/\#scalars "Direct link to Scalars")

ClearML automatically captures scalars logged with XGBoost, which can be visualized in plots in the
ClearML WebApp, in the task's **SCALARS** tab.

![Scalars](https://clear.ml/docs/latest/assets/images/examples_xgboost_metric_scalars-ba5f134ccd09d9c616490c4a0e3f90cf.png#light-mode-only)![Scalars](https://clear.ml/docs/latest/assets/images/examples_xgboost_metric_scalars_dark-cd5dae767b4e172a939b8848f171e9e5.png#dark-mode-only)

## Models [​](https://clear.ml/docs/latest/docs/guides/frameworks/xgboost/xgboost_metrics/\#models "Direct link to Models")

ClearML automatically captures the model logged using the `xgboost.save` method, and saves it as an artifact.

View saved snapshots in the task's **ARTIFACTS** tab.

![Artifacts tab](https://clear.ml/docs/latest/assets/images/examples_xgboost_metric_artifacts-a06d0e3d93ae30e00e746176199c3146.png#light-mode-only)![Artifacts tab](https://clear.ml/docs/latest/assets/images/examples_xgboost_metric_artifacts_dark-4022795440ebd42c313338a6d2c522bb.png#dark-mode-only)

To view the model details, click the model name in the **ARTIFACTS** page to open its info tab. Alternatively, download the model.

![Model info panel](https://clear.ml/docs/latest/assets/images/examples_xgboost_metric_model-c6558ce71904ba79c8f08163de8157c6.png#light-mode-only)![Model info panel](https://clear.ml/docs/latest/assets/images/examples_xgboost_metric_model_dark-ca06302a50e7e4c16ba7a46069e2df61.png#dark-mode-only)

## Console [​](https://clear.ml/docs/latest/docs/guides/frameworks/xgboost/xgboost_metrics/\#console "Direct link to Console")

All console output during the script's execution appears in the task's **CONSOLE** page.

![Console output](https://clear.ml/docs/latest/assets/images/examples_xgboost_metric_console-66d32adc2b3f3df6bf81dd73c64b28af.png#light-mode-only)![Console output](https://clear.ml/docs/latest/assets/images/examples_xgboost_metric_console_dark-dadf1e2c317c98310d3eb4fb6eeb4883.png#dark-mode-only)

- [Scalars](https://clear.ml/docs/latest/docs/guides/frameworks/xgboost/xgboost_metrics/#scalars)
- [Models](https://clear.ml/docs/latest/docs/guides/frameworks/xgboost/xgboost_metrics/#models)
- [Console](https://clear.ml/docs/latest/docs/guides/frameworks/xgboost/xgboost_metrics/#console)