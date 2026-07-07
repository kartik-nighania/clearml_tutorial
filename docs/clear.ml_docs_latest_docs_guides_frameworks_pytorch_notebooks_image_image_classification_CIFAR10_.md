---
url: "https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/image/image_classification_CIFAR10/"
title: "Image Classification - Jupyter Notebook | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/image/image_classification_CIFAR10/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The example [image\_classification\_CIFAR10.ipynb](https://github.com/clearml/clearml/blob/master/examples/frameworks/pytorch/notebooks/image/image_classification_CIFAR10.ipynb)
demonstrates integrating ClearML into a Jupyter Notebook, which uses PyTorch, TensorBoard, and TorchVision to train a
neural network on the CIFAR-10 dataset for image classification. ClearML automatically logs the example script's
calls to TensorBoard methods in training and testing which report scalars and image debug samples, as well as the model
and console log. The example also demonstrates connecting parameters to a Task and logging them. When the script runs,
it creates a task named `image_classification_CIFAR10` in the `Image Example` project.

Another example optimizes the hyperparameters for this image classification example (see the [Hyperparameter Optimization - Jupyter Notebook](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/image/hyperparameter_search) documentation page). This image classification example must run before the hyperparameter optimization example.

## Scalars [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/image/image_classification_CIFAR10/\#scalars "Direct link to Scalars")

The accuracy, accuracy per class, and training loss scalars are automatically logged, along with the resource utilization plots (titled **:monitor: machine**), and appear **SCALARS**.

![image](https://clear.ml/docs/latest/assets/images/examples_image_classification_CIFAR10_05-57ae84876f009e16bfc78c7400b6d1a9.png)

## Debug Samples [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/image/image_classification_CIFAR10/\#debug-samples "Direct link to Debug Samples")

The image samples are automatically logged and appear in **DEBUG SAMPLES**.

![image](https://clear.ml/docs/latest/assets/images/examples_image_classification_CIFAR10_07-f47ba9c70e1f6907ae6e3666ba47ea9b.png)

By doubling clicking a thumbnail, you can view a spectrogram plot in the image viewer.

![image](https://clear.ml/docs/latest/assets/images/examples_image_classification_CIFAR10_06-8f1e7ebd8f271686b267bb73328b7c0e.png)

## Hyperparameters [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/image/image_classification_CIFAR10/\#hyperparameters "Direct link to Hyperparameters")

ClearML automatically logs TensorFlow Definitions. A parameter dictionary is logged by connecting it to the Task using
[`Task.connect()`](https://clear.ml/docs/latest/docs/references/sdk/task#connect).

```python
configuration_dict = {'number_of_epochs': 3, 'batch_size': 4, 'dropout': 0.25, 'base_lr': 0.001}

# enabling configuration override by clearml

configuration_dict = task.connect(configuration_dict)
```

Parameter dictionaries appear in **CONFIGURATION** **>** **HYPERPARAMETERS** **>** **General**.

![image](https://clear.ml/docs/latest/assets/images/examples_image_classification_CIFAR10_01-016a9bed36959ab232f1357a5b1aa43a.png)

TensorFlow Definitions appear in the **TF\_DEFINE** subsection.

![image](https://clear.ml/docs/latest/assets/images/examples_image_classification_CIFAR10_01a-ff9b16e0d00346b01c3ebe5ec75f6032.png)

## Console [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/image/image_classification_CIFAR10/\#console "Direct link to Console")

Text printed to the console for training progress, as well as all other console output, appear in **CONSOLE**.

![image](https://clear.ml/docs/latest/assets/images/examples_image_classification_CIFAR10_04-ad7d5b25dfdb05a367bffb7dfd47f4de.png)

- [Scalars](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/image/image_classification_CIFAR10/#scalars)
- [Debug Samples](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/image/image_classification_CIFAR10/#debug-samples)
- [Hyperparameters](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/image/image_classification_CIFAR10/#hyperparameters)
- [Console](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/image/image_classification_CIFAR10/#console)