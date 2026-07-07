---
url: "https://clear.ml/docs/latest/docs/integrations/tensorboard/"
title: "TensorBoard | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/integrations/tensorboard/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

tip

If you are not already using ClearML, see [ClearML Setup instructions](https://clear.ml/docs/latest/docs/clearml_sdk/clearml_sdk_setup).

[TensorBoard](https://www.tensorflow.org/tensorboard) is TensorFlow's data visualization toolkit.
ClearML automatically captures all data logged to TensorBoard. All you have to do is add two
lines of code to your script:

```python
from clearml import Task

task = Task.init(task_name="<task_name>", project_name="<project_name>")
```

This will create a [ClearML Task](https://clear.ml/docs/latest/docs/fundamentals/task) that captures your script's information, including Git details,
uncommitted code, Python environment, your TensorBoard metrics, plots, images, and text.

View the TensorBoard outputs in the [WebApp](https://clear.ml/docs/latest/docs/webapp/webapp_overview), in the task's page.

![TensorBoard WebApp scalars](https://clear.ml/docs/latest/assets/images/examples_pytorch_tensorboard_07-2a202931fe27a0a8258619bd09f8f7ce.png#light-mode-only)![TensorBoard WebApp scalars](https://clear.ml/docs/latest/assets/images/examples_pytorch_tensorboard_07_dark-b77a7e8387c60dea1ebe4f10e428d36a.png#dark-mode-only)

![Tensorboard WebApp debug samples](https://clear.ml/docs/latest/assets/images/examples_tensorboard_toy_pytorch_02-86bed2e774111d015be73a671d8f90bb.png#light-mode-only)![Tensorboard WebApp debug samples](https://clear.ml/docs/latest/assets/images/examples_tensorboard_toy_pytorch_02_dark-515dbd960daabb550fd640c0bdf908e7.png#dark-mode-only)

## Automatic Logging Control [​](https://clear.ml/docs/latest/docs/integrations/tensorboard/\#automatic-logging-control "Direct link to Automatic Logging Control")

By default, when ClearML is integrated into your script, it captures all of your TensorBoard plots, images, and metrics.
But, you may want to have more control over what your task logs.

To control a task's framework logging, use the `auto_connect_frameworks` parameter of [`Task.init()`](https://clear.ml/docs/latest/docs/references/sdk/task#taskinit).
Completely disable all automatic logging by setting the parameter to `False`. For finer grained control of logged
frameworks, input a dictionary, with framework-boolean pairs.

For example:

```python
auto_connect_frameworks={

   'tensorboard': False,'matplotlib': False, 'tensorflow': False,  'pytorch': True,

   'xgboost': False, 'scikit': True, 'fastai': True, 'lightgbm': False,

   'hydra': True, 'detect_repository': True, 'tfdefines': True, 'joblib': True,

   'megengine': True, 'catboost': True

}
```

Note that the `tensorboard` key enables/disables automatic logging for both `TensorBoard` and `TensorboardX`.

## Manual Logging [​](https://clear.ml/docs/latest/docs/integrations/tensorboard/\#manual-logging "Direct link to Manual Logging")

To augment its automatic logging, ClearML also provides an explicit logging interface.

See more information about explicitly logging information to a ClearML Task:

- [Models](https://clear.ml/docs/latest/docs/clearml_sdk/model_sdk#manually-logging-models)
- [Configuration](https://clear.ml/docs/latest/docs/clearml_sdk/task_sdk#configuration) (e.g. parameters, configuration files)
- [Artifacts](https://clear.ml/docs/latest/docs/clearml_sdk/task_sdk#artifacts) (e.g. output files or Python objects created by a task)
- [Scalars](https://clear.ml/docs/latest/docs/clearml_sdk/task_sdk#scalars)
- [Text/Plots/Debug Samples](https://clear.ml/docs/latest/docs/fundamentals/logger#manual-reporting)

### Examples [​](https://clear.ml/docs/latest/docs/integrations/tensorboard/\#examples "Direct link to Examples")

Take a look at ClearML's TensorBoard examples:

- [TensorBoard PR Curve](https://clear.ml/docs/latest/docs/guides/frameworks/tensorflow/tensorboard_pr_curve) \- Demonstrates logging TensorBoard outputs and TensorFlow flags
- [TensorBoard Toy](https://clear.ml/docs/latest/docs/guides/frameworks/tensorflow/tensorboard_toy) \- Demonstrates logging TensorBoard histograms, scalars, images, text, and TensorFlow flags
- [Tensorboard with PyTorch](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/pytorch_tensorboard) \- Demonstrates logging TensorBoard scalars, debug samples, and text integrated in code that uses PyTorch

- [Automatic Logging Control](https://clear.ml/docs/latest/docs/integrations/tensorboard/#automatic-logging-control)
- [Manual Logging](https://clear.ml/docs/latest/docs/integrations/tensorboard/#manual-logging)
  - [Examples](https://clear.ml/docs/latest/docs/integrations/tensorboard/#examples)