---
url: "https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/text/text_classification_AG_NEWS/"
title: "Text Classification - Jupyter Notebook | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/text/text_classification_AG_NEWS/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The example [text\_classification\_AG\_NEWS.ipynb](https://github.com/clearml/clearml/blob/master/examples/frameworks/pytorch/notebooks/text/text_classification_AG_NEWS.ipynb)
demonstrates using Jupyter Notebook for ClearML, and the integration of ClearML into code which trains a network
to classify text in the `torchtext` [AG\_NEWS](https://pytorch.org/text/stable/datasets.html#ag-news) dataset, and then applies the model to predict the classification of sample text.

ClearML automatically logs the scalars and text samples reported with TensorBoard methods. The example code explicitly logs parameters to the Task. When the script runs, it creates a task named `text classifier` in the `Text Example` project.

## Scalars [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/text/text_classification_AG_NEWS/\#scalars "Direct link to Scalars")

Accuracy, learning rate, and training loss appear in **SCALARS**, along with the resource utilization plots, which are titled **:monitor: machine**.

![Scalars](https://clear.ml/docs/latest/assets/images/text_classification_AG_NEWS_03-51a99fba7a06f124b6905dcb87f22fdf.png)

## Debug Samples [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/text/text_classification_AG_NEWS/\#debug-samples "Direct link to Debug Samples")

ClearML automatically logs the text samples reported to TensorBoard. They are displayed in the task's **DEBUG SAMPLES**.

![Debug samples](https://clear.ml/docs/latest/assets/images/text_classification_AG_NEWS_04-93a5da037349ed323ff306c919924cdc.png)

## Hyperparameters [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/text/text_classification_AG_NEWS/\#hyperparameters "Direct link to Hyperparameters")

A parameter dictionary is logged by connecting it to the Task using [`Task.connect()`](https://clear.ml/docs/latest/docs/references/sdk/task#connect):

```python
configuration_dict = {

    'number_of_epochs': 6, 'batch_size': 16, 'ngrams': 2, 'base_lr': 1.0

}

# enabling configuration override by clearml

configuration_dict = task.connect(configuration_dict)
```

The parameters are displayed in the task's **CONFIGURATION** **>** **HYPERPARAMETERS** **>** **General** section.

![Hyperparameters](https://clear.ml/docs/latest/assets/images/text_classification_AG_NEWS_01-e22dd5c253805b6a378dedb36052ea62.png)

## Console [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/text/text_classification_AG_NEWS/\#console "Direct link to Console")

Text printed to the console for training progress, as well as all other console output, appear in **CONSOLE**.

![Console](https://clear.ml/docs/latest/assets/images/text_classification_AG_NEWS_02-8f290681c5fad37291fceeec6b229f27.png)

- [Scalars](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/text/text_classification_AG_NEWS/#scalars)
- [Debug Samples](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/text/text_classification_AG_NEWS/#debug-samples)
- [Hyperparameters](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/text/text_classification_AG_NEWS/#hyperparameters)
- [Console](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/text/text_classification_AG_NEWS/#console)