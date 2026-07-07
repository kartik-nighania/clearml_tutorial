---
url: "https://clear.ml/docs/latest/docs/guides/frameworks/autokeras/autokeras_imdb_example/"
title: "AutoKeras | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/frameworks/autokeras/autokeras_imdb_example/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The [autokeras\_imdb\_example.py](https://github.com/clearml/clearml/blob/master/examples/frameworks/autokeras/autokeras_imdb_example.py) example
script demonstrates the integration of ClearML into code, which uses [autokeras](https://github.com/keras-team/autokeras).

The example does the following:

- Trains text classification networks on the Keras built-in [IMDB](https://keras.io/api/datasets/imdb/) dataset, using
the autokeras [TextClassifier](https://autokeras.com/text_classifier/) class, and searches for the best model.
- Uses two TensorBoard callbacks, one for training and one for testing.
- ClearML automatically logs everything the code sends to TensorBoard.
- Creates a task named `autokeras imdb example with scalars` in the `autokeras` project.

## Scalars [​](https://clear.ml/docs/latest/docs/guides/frameworks/autokeras/autokeras_imdb_example/\#scalars "Direct link to Scalars")

The loss and accuracy metric scalar plots appear in **SCALARS**, along with the resource utilization plots,
which are titled **:monitor: machine**.

![image](https://clear.ml/docs/latest/assets/images/examples_keras_14-be9723b5914248d3e6469bb28f150a97.png)

## Hyperparameters [​](https://clear.ml/docs/latest/docs/guides/frameworks/autokeras/autokeras_imdb_example/\#hyperparameters "Direct link to Hyperparameters")

ClearML automatically logs TensorFlow Definitions. They appear in **CONFIGURATION** **>** **HYPERPARAMETERS** **>** **TF\_DEFINE**.

![image](https://clear.ml/docs/latest/assets/images/examples_keras_16-97880ae3f4f5615c0c1b89357b0d19cc.png)

## Console [​](https://clear.ml/docs/latest/docs/guides/frameworks/autokeras/autokeras_imdb_example/\#console "Direct link to Console")

Text printed to the console for training progress, as well as all other console output, appear in **CONSOLE**.

![image](https://clear.ml/docs/latest/assets/images/examples_keras_15-1209406d9f290eef6662c495d6eda0e1.png)

## Artifacts [​](https://clear.ml/docs/latest/docs/guides/frameworks/autokeras/autokeras_imdb_example/\#artifacts "Direct link to Artifacts")

Models created by the task appear in the task's **ARTIFACTS** tab.

![image](https://clear.ml/docs/latest/assets/images/examples_keras_18-04fce608d8d24b2e90f4ec2960a4ebb2.png)

Clicking on the model's name takes you to the [model's page](https://clear.ml/docs/latest/docs/webapp/webapp_model_viewing), where you can view
the model's details and access the model.

![image](https://clear.ml/docs/latest/assets/images/examples_keras_17-d96ff4798ca523d6ed458ad2eaf7f62b.png)

- [Scalars](https://clear.ml/docs/latest/docs/guides/frameworks/autokeras/autokeras_imdb_example/#scalars)
- [Hyperparameters](https://clear.ml/docs/latest/docs/guides/frameworks/autokeras/autokeras_imdb_example/#hyperparameters)
- [Console](https://clear.ml/docs/latest/docs/guides/frameworks/autokeras/autokeras_imdb_example/#console)
- [Artifacts](https://clear.ml/docs/latest/docs/guides/frameworks/autokeras/autokeras_imdb_example/#artifacts)