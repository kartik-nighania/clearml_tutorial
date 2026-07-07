---
url: "https://clear.ml/docs/latest/docs/integrations/tensorboardx/"
title: "TensorboardX | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/integrations/tensorboardx/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

tip

If you are not already using ClearML, see [ClearML Setup instructions](https://clear.ml/docs/latest/docs/clearml_sdk/clearml_sdk_setup).

[TensorboardX](https://tensorboardx.readthedocs.io/en/latest/tutorial.html#what-is-tensorboard-x) is a data
visualization toolkit to log information through PyTorch and visualize it through [TensorBoard](https://www.tensorflow.org/tensorboard).
ClearML automatically captures all data logged to TensorboardX, including scalars, images, video, plots, and text. All you have
to do is add two lines of code to your script:

```python
from clearml import Task

task = Task.init(task_name="<task_name>", project_name="<project_name>")
```

This will create a [ClearML Task](https://clear.ml/docs/latest/docs/fundamentals/task) that captures your script's information, including Git details,
uncommitted code, Python environment, your TensorboardX metrics, plots, images, and text.

View the TensorboardX outputs in the [WebApp](https://clear.ml/docs/latest/docs/webapp/webapp_overview), in the task's page.

![TensorboardX WebApp scalars](https://clear.ml/docs/latest/assets/images/examples_pytorch_tensorboardx_03-cc9a52da470f480760c45916ad6e0809.png#light-mode-only)![TensorboardX WebApp scalars](https://clear.ml/docs/latest/assets/images/examples_pytorch_tensorboardx_03_dark-54990fc149cbdef40f7d86d3ad1fb557.png#dark-mode-only)

## Automatic Logging Control [​](https://clear.ml/docs/latest/docs/integrations/tensorboardx/\#automatic-logging-control "Direct link to Automatic Logging Control")

By default, when ClearML is integrated into your script, it captures all of your TensorboardX plots, images, metrics, videos, and text.
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

Note that the `tensorboard` key enables/disables automatic logging for both `TensorboardX` and `TensorBoard`.

## Manual Logging [​](https://clear.ml/docs/latest/docs/integrations/tensorboardx/\#manual-logging "Direct link to Manual Logging")

To augment its automatic logging, ClearML also provides an explicit logging interface.

See more information about explicitly logging information to a ClearML Task:

- [Models](https://clear.ml/docs/latest/docs/clearml_sdk/model_sdk#manually-logging-models)
- [Configuration](https://clear.ml/docs/latest/docs/clearml_sdk/task_sdk#configuration) (e.g. parameters, configuration files)
- [Artifacts](https://clear.ml/docs/latest/docs/clearml_sdk/task_sdk#artifacts) (e.g. output files or Python objects created by a task)
- [Scalars](https://clear.ml/docs/latest/docs/clearml_sdk/task_sdk#scalars)
- [Text/Plots/Debug Samples](https://clear.ml/docs/latest/docs/fundamentals/logger#manual-reporting)

### Examples [​](https://clear.ml/docs/latest/docs/integrations/tensorboardx/\#examples "Direct link to Examples")

Take a look at ClearML's TensorboardX examples:

- [TensorboardX with PyTorch](https://clear.ml/docs/latest/docs/guides/frameworks/tensorboardx/) \- Demonstrates ClearML logging TensorboardX scalars, debug
samples, and text in code using PyTorch
- [MegEngine MNIST](https://clear.ml/docs/latest/docs/guides/frameworks/megengine/megengine_mnist) \- Demonstrates ClearML logging TensorboardX scalars in code using MegEngine
- [TensorboardX Video](https://clear.ml/docs/latest/docs/guides/frameworks/tensorboardx/video_tensorboardx) \- Demonstrates ClearML logging TensorBoardX video data.

- [Automatic Logging Control](https://clear.ml/docs/latest/docs/integrations/tensorboardx/#automatic-logging-control)
- [Manual Logging](https://clear.ml/docs/latest/docs/integrations/tensorboardx/#manual-logging)
  - [Examples](https://clear.ml/docs/latest/docs/integrations/tensorboardx/#examples)