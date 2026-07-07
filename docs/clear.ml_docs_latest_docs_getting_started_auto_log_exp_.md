---
url: "https://clear.ml/docs/latest/docs/getting_started/auto_log_exp/"
title: "Auto-logging Experiments | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/getting_started/auto_log_exp/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

In ClearML, experiments are organized as [Tasks](https://clear.ml/docs/latest/docs/fundamentals/task).

When you integrate the ClearML SDK with your code, the ClearML task manager automatically captures:

- Source code and uncommitted changes
- Installed packages
- General information such as machine details, runtime, creation date etc.
- Model files, parameters, scalars, and plots from popular ML frameworks such as TensorFlow and PyTorch (see list of [supported frameworks](https://clear.ml/docs/latest/docs/clearml_sdk/task_sdk#automatic-logging))
- Console output

Automatic logging control

To control what ClearML automatically logs, see this [FAQ](https://clear.ml/docs/latest/docs/faq#controlling_logging).

## To Auto-log Your Experiments [​](https://clear.ml/docs/latest/docs/getting_started/auto_log_exp/\#to-auto-log-your-experiments "Direct link to To Auto-log Your Experiments")

1. Install `clearml` and connect it to the ClearML Server (see [instructions](https://clear.ml/docs/latest/docs/clearml_sdk/))

2. At the beginning of your code, import the `clearml` package:





```python
from clearml import Task
```











Full Automatic Logging





To ensure full automatic logging, it is recommended to import the `clearml` package at the top of your entry script.
Initializing the Task before training frameworks (e.g. TensorFlow, PyTorch) start executing prevents synchronization issues that
can lead to memory leaks or hanging child processes.

3. Initialize the Task object in your `main()` function, or the beginning of the script.





```python
task = Task.init(project_name='great project', task_name='best task')
```









If the project does not already exist, a new one is created automatically.

The console should display the following output:





```text
ClearML Task: created new task id=1ca59ef1f86d44bd81cb517d529d9e5a

2021-07-25 13:59:09

ClearML results page: https://app.clear.ml/projects/4043a1657f374e9298649c6ba72ad233/experiments/1ca59ef1f86d44bd81cb517d529d9e5a/output/log

2025-01-25 13:59:16
```

4. Click the results page link to go to the [task's detail page in the ClearML WebApp](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual),
where you can monitor the task's status, view all its logged data, visualize its results, and more!

![Info panel](https://clear.ml/docs/latest/assets/images/webapp_tracking_40-3609b1a01adf34e7a13961511832226e.png#light-mode-only)![Info panel](https://clear.ml/docs/latest/assets/images/webapp_tracking_40_dark-f333647114477ed86eaea994a5b95081.png#dark-mode-only)


**That's it!** You are done integrating ClearML with your code :)

Now, [command-line arguments](https://clear.ml/docs/latest/docs/fundamentals/hyperparameters#tracking-hyperparameters), [console output](https://clear.ml/docs/latest/docs/fundamentals/logger#types-of-logged-results), TensorBoard and Matplotlib, and much more will automatically be
logged in the UI under the created Task.

Sit back, relax, and watch your models converge :)

- [To Auto-log Your Experiments](https://clear.ml/docs/latest/docs/getting_started/auto_log_exp/#to-auto-log-your-experiments)