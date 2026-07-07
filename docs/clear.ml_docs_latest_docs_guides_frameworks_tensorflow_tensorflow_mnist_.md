---
url: "https://clear.ml/docs/latest/docs/guides/frameworks/tensorflow/tensorflow_mnist/"
title: "TensorFlow MNIST | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/frameworks/tensorflow/tensorflow_mnist/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The [tensorflow\_mnist.py](https://github.com/clearml/clearml/blob/master/examples/frameworks/tensorflow/tensorflow_mnist.py)
example demonstrates the integration of ClearML into code that uses TensorFlow and Keras to train a neural network on
the Keras built-in [MNIST](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/mnist) handwritten digit dataset.

When the script runs, it creates a task named `Tensorflow v2 mnist with summaries` in the `examples` project.

## Scalars [​](https://clear.ml/docs/latest/docs/guides/frameworks/tensorflow/tensorflow_mnist/\#scalars "Direct link to Scalars")

The loss and accuracy metric scalar plots appear in the task's page in the **ClearML web UI** under
**SCALARS**. Resource utilization plots, which are titled **:monitor: machine**, also appear in the **SCALARS** tab.

![Task scalars](https://clear.ml/docs/latest/assets/images/examples_tensorflow_mnist_06-2da774056823de9a7a0aada5872c0cda.png#light-mode-only)![Task scalars](https://clear.ml/docs/latest/assets/images/examples_tensorflow_mnist_06_dark-0070e38e9bf4a260320d72a3d7f8b0ff.png#dark-mode-only)

## Hyperparameters [​](https://clear.ml/docs/latest/docs/guides/frameworks/tensorflow/tensorflow_mnist/\#hyperparameters "Direct link to Hyperparameters")

ClearML automatically logs TensorFlow Definitions. They appear in **CONFIGURATION** **>** **HYPERPARAMETERS** **>** **TF\_DEFINE**.

![Task hyperparameters](https://clear.ml/docs/latest/assets/images/examples_tensorflow_mnist_01-7aed5a512daae8505e3db56c34c3bdd3.png#light-mode-only)![Task hyperparameters](https://clear.ml/docs/latest/assets/images/examples_tensorflow_mnist_01_dark-60f172dc7b1b431f8236b03404ca72ce.png#dark-mode-only)

## Console [​](https://clear.ml/docs/latest/docs/guides/frameworks/tensorflow/tensorflow_mnist/\#console "Direct link to Console")

All console output appears in **CONSOLE**.

![Task console](https://clear.ml/docs/latest/assets/images/examples_tensorflow_mnist_05-ee0e0c292165aad60f53f55a94ae3081.png#light-mode-only)![Task console](https://clear.ml/docs/latest/assets/images/examples_tensorflow_mnist_05_dark-9c349790c1fd7b7a3d6c0c5dc4d45053.png#dark-mode-only)

## Artifacts [​](https://clear.ml/docs/latest/docs/guides/frameworks/tensorflow/tensorflow_mnist/\#artifacts "Direct link to Artifacts")

Models created by the task appear in the task's **ARTIFACTS** tab. ClearML automatically logs and tracks
models and any snapshots created using TensorFlow.

![Task models](https://clear.ml/docs/latest/assets/images/examples_tensorflow_mnist_03-e9a62488ff234a851038d3e7360bbe40.png#light-mode-only)![Task models](https://clear.ml/docs/latest/assets/images/examples_tensorflow_mnist_03_dark-7040c6b8ad1115fd7b6824e0e14f178a.png#dark-mode-only)

Clicking on a model's name takes you to the [model's page](https://clear.ml/docs/latest/docs/webapp/webapp_model_viewing), where you can
view the model's details and access the model.

![Model details](https://clear.ml/docs/latest/assets/images/examples_tensorflow_mnist_10-554888f669816b9b2416327d53d369a0.png#light-mode-only)![Model details](https://clear.ml/docs/latest/assets/images/examples_tensorflow_mnist_10_dark-c75fed260fc6dfd0bcc6201fbf6f3f46.png#dark-mode-only)

- [Scalars](https://clear.ml/docs/latest/docs/guides/frameworks/tensorflow/tensorflow_mnist/#scalars)
- [Hyperparameters](https://clear.ml/docs/latest/docs/guides/frameworks/tensorflow/tensorflow_mnist/#hyperparameters)
- [Console](https://clear.ml/docs/latest/docs/guides/frameworks/tensorflow/tensorflow_mnist/#console)
- [Artifacts](https://clear.ml/docs/latest/docs/guides/frameworks/tensorflow/tensorflow_mnist/#artifacts)