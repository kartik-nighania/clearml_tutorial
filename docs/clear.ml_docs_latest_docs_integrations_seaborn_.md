---
url: "https://clear.ml/docs/latest/docs/integrations/seaborn/"
title: "Seaborn | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/integrations/seaborn/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

tip

If you are not already using ClearML, see [ClearML Setup instructions](https://clear.ml/docs/latest/docs/clearml_sdk/clearml_sdk_setup).

[seaborn](https://seaborn.pydata.org/) is a Python library for data visualization.
ClearML automatically captures plots created using `seaborn`. All you have to do is add two
lines of code to your script:

```python
from clearml import Task

task = Task.init(task_name="<task_name>", project_name="<project_name>")
```

This will create a [ClearML Task](https://clear.ml/docs/latest/docs/fundamentals/task) that captures your script's information, including Git details,
uncommitted code, Python environment, your `seaborn` plots, and more. View the seaborn plots in the [WebApp](https://clear.ml/docs/latest/docs/webapp/webapp_overview),
in the task's **Plots** tab.

![Seaborn plot](https://clear.ml/docs/latest/assets/images/integrations_seaborn_plots-29dd99e8a7d9b9af13fc76402643ce9f.png)

View code example [here](https://github.com/clearml/clearml/blob/master/examples/frameworks/matplotlib/matplotlib_example.py).