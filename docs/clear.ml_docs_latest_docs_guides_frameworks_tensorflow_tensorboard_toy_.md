---
url: "https://clear.ml/docs/latest/docs/guides/frameworks/tensorflow/tensorboard_toy/"
title: "TensorBoard Toy | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/frameworks/tensorflow/tensorboard_toy/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The [tensorboard\_toy.py](https://github.com/clearml/clearml/blob/master/examples/frameworks/tensorflow/tensorboard_toy.py)
example demonstrates ClearML's automatic logging of TensorBoard scalars, histograms, images, and text, as well as
all other console output and TensorFlow Definitions.

When the script runs, it creates a task named `tensorboard toy example` in the `examples`
project.

## Scalars [​](https://clear.ml/docs/latest/docs/guides/frameworks/tensorflow/tensorboard_toy/\#scalars "Direct link to Scalars")

The `tf.summary.scalar` output appears in the ClearML web UI, in the task's
**SCALARS**. Resource utilization plots, which are titled **:monitor: machine**, also appear in the **SCALARS** tab.

![Scalars](https://clear.ml/docs/latest/assets/images/examples_tensorboard_toy_03-1261a2ec6b61377bc77c7e7c5fec1609.png#light-mode-only)![Scalars](https://clear.ml/docs/latest/assets/images/examples_tensorboard_toy_03_dark-4bfcb3e977dd1f4eec0bdb1ac4619037.png#dark-mode-only)

## Plots [​](https://clear.ml/docs/latest/docs/guides/frameworks/tensorflow/tensorboard_toy/\#plots "Direct link to Plots")

The `tf.summary.histogram` output appears in **PLOTS**.

![Plots](https://clear.ml/docs/latest/assets/images/examples_tensorboard_toy_04-f52f18c80dfa17428b32278af1477e32.png#light-mode-only)![Plots](https://clear.ml/docs/latest/assets/images/examples_tensorboard_toy_04_dark-a436520d26c3b128186f2e8fdda24c6b.png#dark-mode-only)

## Debug Samples [​](https://clear.ml/docs/latest/docs/guides/frameworks/tensorflow/tensorboard_toy/\#debug-samples "Direct link to Debug Samples")

ClearML automatically tracks images and text output to TensorFlow. They appear in **DEBUG SAMPLES**.

![Debug Samples](https://clear.ml/docs/latest/assets/images/examples_tensorboard_toy_05-d88f57a8309cb9e25ad2e898b835adc6.png#light-mode-only)![Debug Samples](https://clear.ml/docs/latest/assets/images/examples_tensorboard_toy_05_dark-42ced8cc209e180f86b711bc10341ed8.png#dark-mode-only)

## Hyperparameters [​](https://clear.ml/docs/latest/docs/guides/frameworks/tensorflow/tensorboard_toy/\#hyperparameters "Direct link to Hyperparameters")

ClearML automatically logs TensorFlow Definitions. They appear in **CONFIGURATION** **>** **HYPERPARAMETERS** **>** **TF\_DEFINE**.

![Hyperparameters](https://clear.ml/docs/latest/assets/images/examples_tensorboard_toy_01-3917c7638014cbdb52d57df9cd7a55cb.png#light-mode-only)![Hyperparameters](https://clear.ml/docs/latest/assets/images/examples_tensorboard_toy_01_dark-474d08b1fe48d7d81b210ac9c33bf1a5.png#dark-mode-only)

- [Scalars](https://clear.ml/docs/latest/docs/guides/frameworks/tensorflow/tensorboard_toy/#scalars)
- [Plots](https://clear.ml/docs/latest/docs/guides/frameworks/tensorflow/tensorboard_toy/#plots)
- [Debug Samples](https://clear.ml/docs/latest/docs/guides/frameworks/tensorflow/tensorboard_toy/#debug-samples)
- [Hyperparameters](https://clear.ml/docs/latest/docs/guides/frameworks/tensorflow/tensorboard_toy/#hyperparameters)