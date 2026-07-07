---
url: "https://clear.ml/docs/latest/docs/guides/distributed/subprocess_example/"
title: "Subprocess | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/distributed/subprocess_example/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The [subprocess\_example.py](https://github.com/clearml/clearml/blob/master/examples/distributed/subprocess_example.py)
script demonstrates multiple subprocesses interacting and reporting to a main Task. The following happens in the script:

- This script initializes a main Task and spawns subprocesses, each for an instances of that Task.
- Each Task in a subprocess references the main Task by calling [`Task.current_task()`](https://clear.ml/docs/latest/docs/references/sdk/task#taskcurrent_task),
which always returns the main Task.
- The Task in each subprocess reports the following to the main Task:
  - Hyperparameters - Additional, different hyperparameters.
  - Console - Text logged to the console as the Task in each subprocess executes.
- When the script runs, it creates a task named `Popen example` in the `examples` project.

## Hyperparameters [​](https://clear.ml/docs/latest/docs/guides/distributed/subprocess_example/\#hyperparameters "Direct link to Hyperparameters")

ClearML automatically logs the command line options defined with `argparse`. A parameter dictionary is logged by
connecting it to the Task using [`Task.connect()`](https://clear.ml/docs/latest/docs/references/sdk/task#connect).

```python
additional_parameters = {

  'stuff_' + str(randint(0, 100)): 'some stuff ' + str(randint(0, 100))

}

Task.current_task().connect(additional_parameters)
```

Command line options appear in **CONFIGURATION** **>** **HYPERPARAMETERS** **>** **Args**.

![Hyperparameter Args](https://clear.ml/docs/latest/assets/images/examples_subprocess_example_01-4b1c3e557a0121046c5a4da79b04850f.png#light-mode-only)![Hyperparameter Args](https://clear.ml/docs/latest/assets/images/examples_subprocess_example_01_dark-fe7f590db1add6f344409da0e7593d45.png#dark-mode-only)

Parameter dictionaries appear in **General**.

![Hyperparameter General](https://clear.ml/docs/latest/assets/images/examples_subprocess_example_01a-b8bb909ebb246e52b6366c8e9e3f9e39.png#light-mode-only)![Hyperparameter General](https://clear.ml/docs/latest/assets/images/examples_subprocess_example_01a_dark-d8c4218a596fd1eb386eba1f901e08d3.png#dark-mode-only)

## Console [​](https://clear.ml/docs/latest/docs/guides/distributed/subprocess_example/\#console "Direct link to Console")

Output to the console, including the text messages from the Task in each subprocess, appear in **CONSOLE**.

![Console](https://clear.ml/docs/latest/assets/images/examples_subprocess_example_02-0fcd7ab19037df1d2c6da0b282c5b1f9.png#light-mode-only)![Console](https://clear.ml/docs/latest/assets/images/examples_subprocess_example_02_dark-b6c81bfeb20548c0bba3d9f1a72a33e4.png#dark-mode-only)

- [Hyperparameters](https://clear.ml/docs/latest/docs/guides/distributed/subprocess_example/#hyperparameters)
- [Console](https://clear.ml/docs/latest/docs/guides/distributed/subprocess_example/#console)