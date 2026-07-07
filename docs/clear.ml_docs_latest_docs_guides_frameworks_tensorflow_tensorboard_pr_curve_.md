---
url: "https://clear.ml/docs/latest/docs/guides/frameworks/tensorflow/tensorboard_pr_curve/"
title: "TensorBoard PR Curve | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/frameworks/tensorflow/tensorboard_pr_curve/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The [tensorboard\_pr\_curve.py](https://github.com/clearml/clearml/blob/master/examples/frameworks/tensorflow/tensorboard_pr_curve.py)
example demonstrates the integration of ClearML into code that uses TensorFlow and TensorBoard.

The example script does the following:

- Creates a task named `tensorboard pr_curve` in the `examples` project.
- Creates three classes, R, G, and B, and generates colors within the RGB space from normal distributions. The true
label of each random color is associated with the normal distribution that generated it.
- Computes the probability that each color belongs to the class, using three other normal distributions.
- Generate PR curves using those probabilities.
- Creates a summary per class using [`tensorboard.plugins.pr_curve.summary`](https://github.com/tensorflow/tensorboard/blob/master/tensorboard/plugins/pr_curve/summary.py).
- ClearML automatically captures TensorBoard output, TensorFlow Definitions, and output to the console.

## Plots [​](https://clear.ml/docs/latest/docs/guides/frameworks/tensorflow/tensorboard_pr_curve/\#plots "Direct link to Plots")

In the **ClearML Web UI**, the PR Curve summaries appear in the task's page under **PLOTS**.

- Blue PR curves

![Blue PR curves](https://clear.ml/docs/latest/assets/images/examples_tensorboard_pr_curve_01-91139563d52820647a202ee9d9d5c007.png#light-mode-only)![Blue PR curves](https://clear.ml/docs/latest/assets/images/examples_tensorboard_pr_curve_01_dark-186bd2ff589119fe829b501dc02261fc.png#dark-mode-only)

- Green PR curves

![Green PR curves](https://clear.ml/docs/latest/assets/images/examples_tensorboard_pr_curve_02-b5ca52d3f15fb52a3602157887d87e6e.png#light-mode-only)![Green PR curves](https://clear.ml/docs/latest/assets/images/examples_tensorboard_pr_curve_02_dark-ba13c8f6602b5433085794a7da3e67a3.png#dark-mode-only)

- Red PR curves

![Red PR curves](https://clear.ml/docs/latest/assets/images/examples_tensorboard_pr_curve_03-5de69eeb95a02acfc65f30ce5a3263d1.png#light-mode-only)![Red PR curves](https://clear.ml/docs/latest/assets/images/examples_tensorboard_pr_curve_03_dark-538eb9f885238c6c3eb0ff1c596c0444.png#dark-mode-only)


## Hyperparameters [​](https://clear.ml/docs/latest/docs/guides/frameworks/tensorflow/tensorboard_pr_curve/\#hyperparameters "Direct link to Hyperparameters")

ClearML automatically logs TensorFlow Definitions. They appear in **CONFIGURATION** **>** **HYPERPARAMETERS** **>** **TF\_DEFINE**.

![Hyperparameters](https://clear.ml/docs/latest/assets/images/examples_tensorboard_pr_curve_04-5b34a9e3421712c324464c1139604ba8.png#light-mode-only)![Hyperparameters](https://clear.ml/docs/latest/assets/images/examples_tensorboard_pr_curve_04_dark-c3f42084e30d4d58bc8ffbe54bdb36e7.png#dark-mode-only)

## Console [​](https://clear.ml/docs/latest/docs/guides/frameworks/tensorflow/tensorboard_pr_curve/\#console "Direct link to Console")

All console output appears in **CONSOLE** tab.

![Console log](https://clear.ml/docs/latest/assets/images/examples_tensorboard_pr_curve_05-beb3907192ff20ef13f6f08635c059dd.png#light-mode-only)![Console log](https://clear.ml/docs/latest/assets/images/examples_tensorboard_pr_curve_05_dark-9beebb7ab9c75fe3090719b093cb5335.png#dark-mode-only)

- [Plots](https://clear.ml/docs/latest/docs/guides/frameworks/tensorflow/tensorboard_pr_curve/#plots)
- [Hyperparameters](https://clear.ml/docs/latest/docs/guides/frameworks/tensorflow/tensorboard_pr_curve/#hyperparameters)
- [Console](https://clear.ml/docs/latest/docs/guides/frameworks/tensorflow/tensorboard_pr_curve/#console)