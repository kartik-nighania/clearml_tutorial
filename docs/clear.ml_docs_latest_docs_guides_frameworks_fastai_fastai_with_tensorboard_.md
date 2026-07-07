---
url: "https://clear.ml/docs/latest/docs/guides/frameworks/fastai/fastai_with_tensorboard/"
title: "Fast.ai | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/frameworks/fastai/fastai_with_tensorboard/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The [fastai\_with\_tensorboard\_example.py](https://github.com/clearml/clearml/blob/master/examples/frameworks/fastai/legacy/fastai_with_tensorboard_example.py)
example demonstrates the integration of ClearML into code that uses FastAI v1 and TensorBoard.

FastAI V2

The ClearML repository also includes [examples using FastAI v2](https://github.com/clearml/clearml/tree/master/examples/frameworks/fastai).

The example code does the following:

1. Trains a simple deep neural network on the fastai built-in MNIST dataset (see the [fast.ai](https://fastai1.fast.ai/) documentation).
2. Uses the fastai `LearnerTensorboardWriter` callback, and ClearML automatically logs TensorBoard through the callback.
3. During script execution, creates a task named `fastai with tensorboard callback` in the `examples` project.

## Scalars [​](https://clear.ml/docs/latest/docs/guides/frameworks/fastai/fastai_with_tensorboard/\#scalars "Direct link to Scalars")

ClearML automatically logs the histogram output to TensorBoard. They appear in **PLOTS**.

![Scalars](https://clear.ml/docs/latest/assets/images/examples_reporting_fastai_01-133f32ac1d65360df927870d871b8440.png#light-mode-only)![Scalars](https://clear.ml/docs/latest/assets/images/examples_reporting_fastai_01_dark-1192bbf72e12c6071f09636fe5427ef5.png#dark-mode-only)

## Plots [​](https://clear.ml/docs/latest/docs/guides/frameworks/fastai/fastai_with_tensorboard/\#plots "Direct link to Plots")

Histograms output to TensorBoard. They appear in **PLOTS**.

![Plots](https://clear.ml/docs/latest/assets/images/examples_reporting_fastai_02-78ed33faabed33a0385c579110b51c05.png#light-mode-only)![Plots](https://clear.ml/docs/latest/assets/images/examples_reporting_fastai_02_dark-d3851395a535420c9bf5cf50cb1cf38d.png#dark-mode-only)

## Logs [​](https://clear.ml/docs/latest/docs/guides/frameworks/fastai/fastai_with_tensorboard/\#logs "Direct link to Logs")

Text printed to the console for training progress, as well as all other console output, appear in **CONSOLE**.

![Console](https://clear.ml/docs/latest/assets/images/examples_reporting_fastai_03-8360910cb31f5245348d9ca96bcfe20c.png#light-mode-only)![Console](https://clear.ml/docs/latest/assets/images/examples_reporting_fastai_03_dark-6c36ee21f00ca54a9ad9065a125119fa.png#dark-mode-only)

- [Scalars](https://clear.ml/docs/latest/docs/guides/frameworks/fastai/fastai_with_tensorboard/#scalars)
- [Plots](https://clear.ml/docs/latest/docs/guides/frameworks/fastai/fastai_with_tensorboard/#plots)
- [Logs](https://clear.ml/docs/latest/docs/guides/frameworks/fastai/fastai_with_tensorboard/#logs)