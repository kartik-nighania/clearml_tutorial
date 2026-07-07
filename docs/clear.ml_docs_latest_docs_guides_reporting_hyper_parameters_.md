---
url: "https://clear.ml/docs/latest/docs/guides/reporting/hyper_parameters/"
title: "Hyperparameters Reporting | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/reporting/hyper_parameters/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The [hyper\_parameters.py](https://github.com/clearml/clearml/blob/master/examples/reporting/hyper_parameters.py) example
script demonstrates:

- ClearML's automatic logging of `argparse` command line options and TensorFlow Definitions
- Logging user-defined hyperparameters with a parameter dictionary and connecting the dictionary to a Task.

Hyperparameters appear in the **web UI** in the task's page, under **CONFIGURATION** **>** **HYPERPARAMETERS**.
Each type is in its own subsection. Parameters from older tasks are grouped together with the `argparse` command
line options (in the **Args** subsection).

When the script runs, it creates a task named `hyper-parameters example` in the `examples` project.

## Argparse Command Line Options [​](https://clear.ml/docs/latest/docs/guides/reporting/hyper_parameters/\#argparse-command-line-options "Direct link to Argparse Command Line Options")

If a code uses argparse and initializes a Task, ClearML automatically logs the argparse arguments.

```python
parser = ArgumentParser()

parser.add_argument('--argparser_int_value', help='integer value', type=int, default=1)

parser.add_argument(

    '--argparser_disabled', action='store_true', default=False, help='disables something'

)

parser.add_argument('--argparser_str_value', help='string value', default='a string')



args = parser.parse_args()
```

Command line options appears in **HYPERPARAMETERS** **>** **Args**.

![Command line options](https://clear.ml/docs/latest/assets/images/examples_reporting_hyper_param_01-01b056a55dd04d91d3c1a7d7fe475f2f.png#light-mode-only)![Command line options](https://clear.ml/docs/latest/assets/images/examples_reporting_hyper_param_01_dark-79a8644400588c12be096c5ade4ef1e8.png#dark-mode-only)

## TensorFlow Definitions [​](https://clear.ml/docs/latest/docs/guides/reporting/hyper_parameters/\#tensorflow-definitions "Direct link to TensorFlow Definitions")

ClearML automatically logs TensorFlow Definitions, whether they are defined before or after the Task is initialized.

```python
flags.DEFINE_string('echo', None, 'Text to echo.')

flags.DEFINE_string('another_str', 'My string', 'A string', module_name='test')

task = Task.init(project_name='examples', task_name='hyperparameters example')



flags.DEFINE_integer('echo3', 3, 'Text to echo.')



flags.DEFINE_string('echo5', '5', 'Text to echo.', module_name='test')
```

TensorFlow Definitions appear in **HYPERPARAMETERS** **>** **TF\_DEFINE**.

![TF Defines](https://clear.ml/docs/latest/assets/images/examples_reporting_hyper_param_03-1f0414ffd06625cf5cdc1bd9433475bb.png#light-mode-only)![TF Defines](https://clear.ml/docs/latest/assets/images/examples_reporting_hyper_param_03_dark-f53a96d94b5fccaad9511c4d8c3f8359.png#dark-mode-only)

## Parameter Dictionaries [​](https://clear.ml/docs/latest/docs/guides/reporting/hyper_parameters/\#parameter-dictionaries "Direct link to Parameter Dictionaries")

Connect a parameter dictionary to a Task by calling [`Task.connect()`](https://clear.ml/docs/latest/docs/references/sdk/task#connect),
and ClearML logs the parameters. ClearML also tracks changes to the parameters.

```python
parameters = {

    'list': [1, 2, 3],

    'dict': {'a': 1, 'b': 2},

    'tuple': (1, 2, 3),

    'int': 3,

    'float': 2.2,

    'string': 'my string',

}



parameters = task.connect(parameters)



# adding new parameter after connect (will be logged as well)

parameters['new_param'] = 'this is new'



# changing the value of a parameter (new value will be stored instead of previous one)

parameters['float'] = '9.9'
```

Parameters from dictionaries connected to Tasks appear in **HYPERPARAMETERS** **>** **General**.

![Parameter dictionaries](https://clear.ml/docs/latest/assets/images/examples_reporting_hyper_param_02-5f2c0e67f0f5d6ac3a3018b554fa9356.png#light-mode-only)![Parameter dictionaries](https://clear.ml/docs/latest/assets/images/examples_reporting_hyper_param_02_dark-a78ecc871bdfc49857b192b2378aa12f.png#dark-mode-only)

- [Argparse Command Line Options](https://clear.ml/docs/latest/docs/guides/reporting/hyper_parameters/#argparse-command-line-options)
- [TensorFlow Definitions](https://clear.ml/docs/latest/docs/guides/reporting/hyper_parameters/#tensorflow-definitions)
- [Parameter Dictionaries](https://clear.ml/docs/latest/docs/guides/reporting/hyper_parameters/#parameter-dictionaries)