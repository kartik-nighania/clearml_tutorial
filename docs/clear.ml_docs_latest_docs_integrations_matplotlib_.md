---
url: "https://clear.ml/docs/latest/docs/integrations/matplotlib/"
title: "Matplotlib | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/integrations/matplotlib/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

tip

If you are not already using ClearML, see [ClearML Setup instructions](https://clear.ml/docs/latest/docs/clearml_sdk/clearml_sdk_setup).

[Matplotlib](https://matplotlib.org/) is a Python library for data visualization. ClearML automatically captures plots
and images created with `matplotlib`.

All you have to do is add two lines of code to your script:

```python
from clearml import Task

task = Task.init(task_name="<task_name>", project_name="<project_name>")
```

This will create a ClearML Task that captures:

- Git details
- Source code and uncommitted changes
- Installed packages
- Matplotlib visualizations
- And more

View captured Matplotlib plots and images in the [WebApp](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual),
in the task's **Plots** and **Debug Samples** tabs respectively.

![Task plots](https://clear.ml/docs/latest/assets/images/examples_matplotlib_example_01-51d0dff7d82097adce2e2890f57c42c6.png#light-mode-only)![Task plots](https://clear.ml/docs/latest/assets/images/examples_matplotlib_example_01_dark-ec555a187f5c804535a2c3ee6252aed2.png#dark-mode-only)

## Automatic Logging Control [​](https://clear.ml/docs/latest/docs/integrations/matplotlib/\#automatic-logging-control "Direct link to Automatic Logging Control")

By default, when ClearML is integrated into your script, it captures all of your matplotlib visualizations.
But, you may want to have more control over what your task logs.

To control a task's framework logging, use the `auto_connect_frameworks` parameter of [`Task.init()`](https://clear.ml/docs/latest/docs/references/sdk/task#taskinit).
Completely disable all automatic logging by setting the parameter to `False`. For finer grained control of logged
frameworks, input a dictionary, with framework-boolean pairs.

For example:

```python
auto_connect_frameworks={

   'matplotlib': False, 'tensorflow': False, 'tensorboard': False, 'pytorch': True,

   'xgboost': False, 'scikit': True, 'fastai': True, 'lightgbm': False,

   'hydra': True, 'detect_repository': True, 'tfdefines': True, 'joblib': True,

   'megengine': True, 'catboost': True

}
```

## Manual Logging [​](https://clear.ml/docs/latest/docs/integrations/matplotlib/\#manual-logging "Direct link to Manual Logging")

To augment its automatic logging, ClearML also provides an explicit logging interface.

Use [`Logger.report_matplotlib_figure()`](https://clear.ml/docs/latest/docs/references/sdk/logger#report_matplotlib_figure) to explicitly log
a matplotlib figure, and specify its title and series names, and iteration number:

```python
logger = task.get_logger()

area = (40 * np.random.rand(N))**2

plt.scatter(x, y, s=area, c=colors, alpha=0.5)

logger.report_matplotlib_figure(title="My Plot Title", series="My Plot Series", iteration=10, figure=plt)

plt.show()
```

The logged figure is displayed in the task's **Plots** tab.

![Task Matplotlib plots](https://clear.ml/docs/latest/assets/images/manual_matplotlib_reporting_01-b430c778753774bb97b963d540d5aaaa.png#light-mode-only)![Task Matplotlib plots](https://clear.ml/docs/latest/assets/images/manual_matplotlib_reporting_01_dark-ceb5608f94ca1ccd9147318eebd290d1.png#dark-mode-only)

Matplotlib figures can be logged as images by passing `report_image=True` to `Logger.report_matplotlib_figure()`.
View the images in the task's **DEBUG SAMPLES** tab.

![Task debug sample](https://clear.ml/docs/latest/assets/images/manual_matplotlib_reporting_03-8a5c7d228efb87857db3981e1d910b20.png#light-mode-only)![Task debug sample](https://clear.ml/docs/latest/assets/images/manual_matplotlib_reporting_03_dark-acc4dc955d5018aca55bce3c0dbe57ed.png#dark-mode-only)

See [Manual Matplotlib Reporting](https://clear.ml/docs/latest/docs/guides/reporting/manual_matplotlib_reporting) example.

- [Automatic Logging Control](https://clear.ml/docs/latest/docs/integrations/matplotlib/#automatic-logging-control)
- [Manual Logging](https://clear.ml/docs/latest/docs/integrations/matplotlib/#manual-logging)