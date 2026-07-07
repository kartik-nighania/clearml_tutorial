---
url: "https://clear.ml/docs/latest/docs/guides/automation/manual_random_param_search_example/"
title: "Manual Random Parameter Search | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/automation/manual_random_param_search_example/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

The [manual\_random\_param\_search\_example.py](https://github.com/clearml/clearml/blob/master/examples/automation/manual_random_param_search_example.py)
script demonstrates a random parameter search by automating the execution of a task multiple times, each time with
a different set of random hyperparameters.

This example accomplishes the automated random parameter search by doing the following:

1. Creating a template Task named `Keras HP optimization base`. To create it, run the [base\_template\_keras\_simple.py](https://github.com/clearml/clearml/blob/master/examples/optimization/hyper-parameter-optimization/base_template_keras_simple.py)
script. This task must be executed first, so it will be stored in the server, and then it can be accessed, cloned,
and modified by another Task.
2. Creating a parameter dictionary, which is connected to the Task by calling [`Task.connect()`](https://clear.ml/docs/latest/docs/references/sdk/task#connect)
so that the parameters are logged by ClearML.
3. Adding the random search hyperparameters and parameters defining the search (e.g., the task name, and number of
times to run the task).
4. Creating a Task object referencing the template task, `Keras HP optimization base`. See [`Task.get_task`](https://clear.ml/docs/latest/docs/references/sdk/task#taskget_task).
5. For each set of parameters:
1. Cloning the Task object. See [`Task.clone`](https://clear.ml/docs/latest/docs/references/sdk/task#taskclone).
2. Getting the newly cloned Task's parameters. See [`Task.get_parameters`](https://clear.ml/docs/latest/docs/references/sdk/task#get_parameters).
3. Setting the newly cloned Task's parameters to the search values in the parameter dictionary (Step 1). See [`Task.set_parameters`](https://clear.ml/docs/latest/docs/references/sdk/task#set_parameters).
4. Enqueuing the newly cloned Task to execute. See [`Task.enqueue`](https://clear.ml/docs/latest/docs/references/sdk/task#taskenqueue).

When the example script runs, it creates a task named `Random Hyper-Parameter Search Example` in
the `examples` project. This starts the parameter search, and creates the tasks:

- `Keras HP optimization base 0`
- `Keras HP optimization base 1`
- `Keras HP optimization base 2`.

When these tasks are completed, their [results can be compared](https://clear.ml/docs/latest/docs/webapp/webapp_exp_comparing).

![Comparison parallel coordinates](https://clear.ml/docs/latest/assets/images/examples_hpo_parallel_coordinates-42959a778a4d4cfa8071c420419d9ebb.png#light-mode-only)![Comparison parallel coordinates](https://clear.ml/docs/latest/assets/images/examples_hpo_parallel_coordinates_dark-21e3dac54bba8dbd2b6e02e965314947.png#dark-mode-only)