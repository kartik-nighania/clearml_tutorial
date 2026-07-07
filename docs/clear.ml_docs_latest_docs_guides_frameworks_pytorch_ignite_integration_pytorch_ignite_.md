---
url: "https://clear.ml/docs/latest/docs/guides/frameworks/pytorch_ignite/integration_pytorch_ignite/"
title: "PyTorch Ignite TensorboardLogger | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch_ignite/integration_pytorch_ignite/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The [cifar\_ignite.py](https://github.com/clearml/clearml/blob/master/examples/frameworks/ignite/cifar_ignite.py) example
script integrates ClearML into code that uses [PyTorch Ignite](https://github.com/pytorch/ignite).

The example script does the following:

- Trains a neural network on the CIFAR-10 dataset for image classification.
- Creates a [ClearML Task](https://clear.ml/docs/latest/docs/fundamentals/task) named `image classification CIFAR10` in
the `examples` project.
- Calls the [`Task.connect`](https://clear.ml/docs/latest/docs/references/sdk/task#connect) method to track task configuration.
- Uses `ignite`'s `TensorboardLogger` and attaches handlers to it. See [`TensorboardLogger`](https://github.com/pytorch/ignite/blob/master/ignite/contrib/handlers/tensorboard_logger.py).

ClearML's automatic logging captures information and outputs logged with `TensorboardLogger`.

## Hyperparameters [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch_ignite/integration_pytorch_ignite/\#hyperparameters "Direct link to Hyperparameters")

Parameters are explicitly reported to ClearML using the [`Task.connect`](https://clear.ml/docs/latest/docs/references/sdk/task#connect) method.

```python
params = {'number_of_epochs': 20, 'batch_size': 64, 'dropout': 0.25, 'base_lr': 0.001, 'momentum': 0.9, 'loss_report': 100}

params = task.connect(params)  # enabling configuration override by clearml
```

The hyperparameter configurations can be viewed in the WebApp in the task's **CONFIGURATION** tab.

![Hyperparameters](https://clear.ml/docs/latest/assets/images/examples_integration_pytorch_ignite_config-27e52d3612df24427c611adef44eca7e.png#light-mode-only)![Hyperparameters](https://clear.ml/docs/latest/assets/images/examples_integration_pytorch_ignite_config_dark-0509e9cbea703aae9758a2089f79ba89.png#dark-mode-only)

## Ignite TensorboardLogger [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch_ignite/integration_pytorch_ignite/\#ignite-tensorboardlogger "Direct link to Ignite TensorboardLogger")

`TensorboardLogger` is a handler to log metrics, parameters, and gradients when training a model. When ClearML is integrated
into a script which uses `TensorboardLogger`, all information logged through the handler is automatically captured by ClearML.

## Scalars [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch_ignite/integration_pytorch_ignite/\#scalars "Direct link to Scalars")

ClearML automatically captures scalars logged through `TensorboardLogger`.

View the scalars in the task's page in the **ClearML Web UI**, in **SCALARS**.

![Task scalars](https://clear.ml/docs/latest/assets/images/examples_cifar_scalars-4df44ac28557bec117e421cd376c41e0.png#light-mode-only)![Task scalars](https://clear.ml/docs/latest/assets/images/examples_cifar_scalars_dark-645e91a598a1dad6b9f26df46503fbcb.png#dark-mode-only)

## Model Snapshots [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch_ignite/integration_pytorch_ignite/\#model-snapshots "Direct link to Model Snapshots")

ClearML automatically captures the model logged with Torch, and saves it as an artifact.

View saved snapshots in the task's **ARTIFACTS** tab.

![Task models](https://clear.ml/docs/latest/assets/images/examples_cifar_artifacts-801aa6996b461d9b7a2000c81cd37d8e.png#light-mode-only)![Task models](https://clear.ml/docs/latest/assets/images/examples_cifar_artifacts_dark-b8b31cab009c6f9dfe93ddbecb7749b0.png#dark-mode-only)

To view the model, in the **ARTIFACTS** tab, click the model name (or download it).

![Model details](https://clear.ml/docs/latest/assets/images/examples_cifar_model-e04356df888742c24537e9bff84d7804.png#light-mode-only)![Model details](https://clear.ml/docs/latest/assets/images/examples_cifar_model_dark-e36cb2e5eb1b5b41e6b7f0efb2159746.png#dark-mode-only)

## Debug Samples [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch_ignite/integration_pytorch_ignite/\#debug-samples "Direct link to Debug Samples")

ClearML automatically tracks images logged to TensorboardLogger. They appear in **DEBUG SAMPLES**.

![Debug Samples](https://clear.ml/docs/latest/assets/images/examples_integration_pytorch_ignite_debug-6bcf86ff36ee2f8a0f54ecbc487575b3.png#light-mode-only)![Debug Samples](https://clear.ml/docs/latest/assets/images/examples_integration_pytorch_ignite_debug_dark-23e79575e805126ab0dcb2c4e11f5497.png#dark-mode-only)

## Ignite ClearMLLogger [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch_ignite/integration_pytorch_ignite/\#ignite-clearmllogger "Direct link to Ignite ClearMLLogger")

PyTorch Ignite also supports a dedicated `ClearMLLogger` handler to log metrics, text, model / optimizer parameters, plots, and model
checkpoints during training and validation.

For more information, see the [PyTorch Ignite ClearMLLogger](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch_ignite/pytorch_ignite_mnist)
example.

- [Hyperparameters](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch_ignite/integration_pytorch_ignite/#hyperparameters)
- [Ignite TensorboardLogger](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch_ignite/integration_pytorch_ignite/#ignite-tensorboardlogger)
- [Scalars](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch_ignite/integration_pytorch_ignite/#scalars)
- [Model Snapshots](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch_ignite/integration_pytorch_ignite/#model-snapshots)
- [Debug Samples](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch_ignite/integration_pytorch_ignite/#debug-samples)
- [Ignite ClearMLLogger](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch_ignite/integration_pytorch_ignite/#ignite-clearmllogger)