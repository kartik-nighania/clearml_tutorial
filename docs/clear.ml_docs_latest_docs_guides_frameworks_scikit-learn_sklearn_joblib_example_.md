---
url: "https://clear.ml/docs/latest/docs/guides/frameworks/scikit-learn/sklearn_joblib_example/"
title: "scikit-learn with Joblib | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/frameworks/scikit-learn/sklearn_joblib_example/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The [sklearn\_joblib\_example.py](https://github.com/clearml/clearml/blob/master/examples/frameworks/scikit-learn/sklearn_joblib_example.py)
demonstrates the integration of ClearML into code that uses `scikit-learn` and `joblib` to store a model and model snapshots,
and `matplotlib` to create a scatter diagram. When the script runs, it creates a task named
`scikit-learn joblib example` in the `examples` project.

## Plots [​](https://clear.ml/docs/latest/docs/guides/frameworks/scikit-learn/sklearn_joblib_example/\#plots "Direct link to Plots")

ClearML automatically logs the scatter plot, which appears in the [task's page](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual)
in the ClearML web UI, under **PLOTS**.

![Plots](https://clear.ml/docs/latest/assets/images/examples_sklearn_joblib_example_06-3c2e720f00cac9a16fd52cb3f156096a.png#light-mode-only)![Plots](https://clear.ml/docs/latest/assets/images/examples_sklearn_joblib_example_06_dark-41bb5d2648d3b005e926b0576f553e46.png#dark-mode-only)

## Artifacts [​](https://clear.ml/docs/latest/docs/guides/frameworks/scikit-learn/sklearn_joblib_example/\#artifacts "Direct link to Artifacts")

Models created by the task appear in the task's **ARTIFACTS** tab.

![Artifacts](https://clear.ml/docs/latest/assets/images/examples_sklearn_joblib_example_01-ced094f6613874061d57fb54a37f1d56.png#light-mode-only)![Artifacts](https://clear.ml/docs/latest/assets/images/examples_sklearn_joblib_example_01_dark-36792ac02766fd00014609746d8aabe7.png#dark-mode-only)

Clicking on the model name takes you to the [model's page](https://clear.ml/docs/latest/docs/webapp/webapp_model_viewing), where you can
view the model's details and access the model.

![Model details](https://clear.ml/docs/latest/assets/images/examples_sklearn_joblib_example_02-25291d50b423f2f771a06bae0e700c87.png#light-mode-only)![Model details](https://clear.ml/docs/latest/assets/images/examples_sklearn_joblib_example_02_dark-b2a8c46b3786360f9a66b2ee020cc236.png#dark-mode-only)

- [Plots](https://clear.ml/docs/latest/docs/guides/frameworks/scikit-learn/sklearn_joblib_example/#plots)
- [Artifacts](https://clear.ml/docs/latest/docs/guides/frameworks/scikit-learn/sklearn_joblib_example/#artifacts)