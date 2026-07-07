---
url: "https://clear.ml/docs/latest/docs/guides/frameworks/keras/jupyter/"
title: "Keras with Matplotlib - Jupyter Notebook | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/frameworks/keras/jupyter/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The [jupyter.ipynb](https://github.com/clearml/clearml/blob/master/examples/frameworks/keras/jupyter.ipynb) example
demonstrates ClearML's automatic logging of code running in a Jupyter Notebook that uses Keras and Matplotlib.

The example does the following:

1. Trains a simple deep neural network on the Keras built-in [MNIST](https://keras.io/api/datasets/mnist/#load_data-function)
dataset.

2. Builds a sequential model using a categorical cross entropy loss objective function.

3. Specifies accuracy as the metric, and uses two callbacks: a TensorBoard callback and a model checkpoint callback.

4. During script execution, creates a task named `notebook example` in the `examples` project.


## Scalars [​](https://clear.ml/docs/latest/docs/guides/frameworks/keras/jupyter/\#scalars "Direct link to Scalars")

The loss and accuracy metric scalar plots appear in **SCALARS**, along with the resource utilization plots, which are titled **:monitor: machine**.

![Scalars](https://clear.ml/docs/latest/assets/images/examples_keras_jupyter_08-95118f876369fef2357716a887924d7f.png#light-mode-only)![Scalars](https://clear.ml/docs/latest/assets/images/examples_keras_jupyter_08_dark-646ff0a51a1c4c535065cfddca55e546.png#dark-mode-only)

## Plots [​](https://clear.ml/docs/latest/docs/guides/frameworks/keras/jupyter/\#plots "Direct link to Plots")

The example calls Matplotlib methods to create several sample plots, and TensorBoard methods to plot histograms for layer density.
They appear in **PLOTS**.

![Plots 1](https://clear.ml/docs/latest/assets/images/examples_keras_jupyter_03-92630e788df232244937c33261526103.png#light-mode-only)![Plots 1](https://clear.ml/docs/latest/assets/images/examples_keras_jupyter_03_dark-3e94206c435803a06e6fbc34c0ba6130.png#dark-mode-only)

![Plots 2](https://clear.ml/docs/latest/assets/images/examples_keras_jupyter_03a-4074e9acf7695ec0b1818797e909c4f7.png#light-mode-only)![Plots 2](https://clear.ml/docs/latest/assets/images/examples_keras_jupyter_03a_dark-b37049720c1216ea30187348ee3968ae.png#dark-mode-only)

## Debug Samples [​](https://clear.ml/docs/latest/docs/guides/frameworks/keras/jupyter/\#debug-samples "Direct link to Debug Samples")

The example calls Matplotlib methods to log debug sample images. They appear in **DEBUG SAMPLES**.

![Debug Samples](https://clear.ml/docs/latest/assets/images/examples_keras_jupyter_04-7c207128fa2d9d9a4bc304c40122cd15.png#light-mode-only)![Debug Samples](https://clear.ml/docs/latest/assets/images/examples_keras_jupyter_04_dark-cb8031ce381dbac5ee3d612945c7968b.png#dark-mode-only)

## Hyperparameters [​](https://clear.ml/docs/latest/docs/guides/frameworks/keras/jupyter/\#hyperparameters "Direct link to Hyperparameters")

ClearML automatically logs TensorFlow Definitions. A parameter dictionary is logged by connecting it to the Task, by
calling [`Task.connect()`](https://clear.ml/docs/latest/docs/references/sdk/task#connect).

```python
task_params = {'num_scatter_samples': 60, 'sin_max_value': 20, 'sin_steps': 30}

task_params = task.connect(task_params)
```

Later in the Jupyter Notebook, more parameters are added to the dictionary.

```python
task_params['batch_size'] = 128

task_params['nb_classes'] = 10

task_params['nb_epoch'] = 6

task_params['hidden_dim'] = 512
```

Parameter dictionaries appear in **CONFIGURATION** **>** **HYPERPARAMETERS** **>** **General**.

![General Hyperparameters](https://clear.ml/docs/latest/assets/images/examples_keras_jupyter_20-47c9f245c002f7357983ee6d326bea98.png#light-mode-only)![General Hyperparameters](https://clear.ml/docs/latest/assets/images/examples_keras_jupyter_20_dark-8e3ad705b42567a4874694dbea4de8d5.png#dark-mode-only)

The TensorFlow Definitions appear in the **TF\_DEFINE** subsection.

![TF Define](https://clear.ml/docs/latest/assets/images/examples_keras_jupyter_21-d385b425c098e288d61dda3631ac5b9f.png#light-mode-only)![TF Define](https://clear.ml/docs/latest/assets/images/examples_keras_jupyter_21_dark-181a3ae324fdd0822d902ebab8abb58e.png#dark-mode-only)

## Console [​](https://clear.ml/docs/latest/docs/guides/frameworks/keras/jupyter/\#console "Direct link to Console")

Text printed to the console for training appears in **CONSOLE**.

![Console Log](https://clear.ml/docs/latest/assets/images/examples_keras_jupyter_07-833f9d9084a0e3bcbdf4631b1cc60b9a.png#light-mode-only)![Console Log](https://clear.ml/docs/latest/assets/images/examples_keras_jupyter_07_dark-ed690707ffffabf490041d1af6619570.png#dark-mode-only)

## Artifacts [​](https://clear.ml/docs/latest/docs/guides/frameworks/keras/jupyter/\#artifacts "Direct link to Artifacts")

Models created by the task appear in the task's **ARTIFACTS** tab. ClearML automatically logs and tracks models
created using Keras.

The task info panel shows model tracking, including the model name and design in **ARTIFACTS** **>** **Output Model**.

![Artifacts](https://clear.ml/docs/latest/assets/images/examples_keras_jupyter_23-22d5fa678b90f8417cfe98f6ed65718e.png#light-mode-only)![Artifacts](https://clear.ml/docs/latest/assets/images/examples_keras_jupyter_23_dark-684cf0d237b938d1b538498ee847571e.png#dark-mode-only)

Clicking on the model name takes you to the [model's page](https://clear.ml/docs/latest/docs/webapp/webapp_model_viewing), where you can view
the model's details and access the model.

![Model details](https://clear.ml/docs/latest/assets/images/examples_keras_jupyter_24-434ba9a12c7b4f416f5b485dbcb883fd.png#light-mode-only)![Model details](https://clear.ml/docs/latest/assets/images/examples_keras_jupyter_24_dark-a75ec1e91301dd79482bd571da0bde36.png#dark-mode-only)

- [Scalars](https://clear.ml/docs/latest/docs/guides/frameworks/keras/jupyter/#scalars)
- [Plots](https://clear.ml/docs/latest/docs/guides/frameworks/keras/jupyter/#plots)
- [Debug Samples](https://clear.ml/docs/latest/docs/guides/frameworks/keras/jupyter/#debug-samples)
- [Hyperparameters](https://clear.ml/docs/latest/docs/guides/frameworks/keras/jupyter/#hyperparameters)
- [Console](https://clear.ml/docs/latest/docs/guides/frameworks/keras/jupyter/#console)
- [Artifacts](https://clear.ml/docs/latest/docs/guides/frameworks/keras/jupyter/#artifacts)