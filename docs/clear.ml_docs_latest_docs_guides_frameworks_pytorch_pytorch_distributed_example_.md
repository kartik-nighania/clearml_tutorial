---
url: "https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/pytorch_distributed_example/"
title: "PyTorch Distributed | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/pytorch_distributed_example/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The [pytorch\_distributed\_example.py](https://github.com/clearml/clearml/blob/master/examples/frameworks/pytorch/pytorch_distributed_example.py)
script demonstrates integrating ClearML into a code that uses the [PyTorch Distributed Communications Package](https://pytorch.org/docs/stable/distributed.html)
(`torch.distributed`).

The script does the following:

1. It initializes a main Task and spawns subprocesses, each for an instance of that Task.

2. The Task in each subprocess trains a neural network over a partitioned dataset (the torchvision built-in [MNIST](https://pytorch.org/vision/stable/datasets.html#mnist)
dataset), and reports the following to the main Task:


   - Artifacts - A dictionary containing different key-value pairs is uploaded from the Task in each subprocess to the main Task.

   - Scalars - Loss reported as a scalar during training in each subprocess Task is logged in the main Task.

   - Hyperparameters - Hyperparameters created in each subprocess Task are added to the main Task's hyperparameters.


Each Task in a subprocess references the main Task by calling [`Task.current_task()`](https://clear.ml/docs/latest/docs/references/sdk/task#taskcurrent_task),
which always returns the main Task.

3. When the script runs, it creates a task named `test torch distributed` in the `examples` project in the **ClearML Web UI**.


### Artifacts [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/pytorch_distributed_example/\#artifacts "Direct link to Artifacts")

The example uploads a dictionary as an artifact in the main Task by calling [`Task.upload_artifact()`](https://clear.ml/docs/latest/docs/references/sdk/task#upload_artifact)
on `Task.current_task` (the main Task). The dictionary contains the `dist.rank` of the subprocess, making each unique.

```python
Task.current_task().upload_artifact(

    name='temp {:02d}'.format(dist.get_rank()),

    artifact_object={'worker_rank': dist.get_rank()}

)
```

All of these artifacts appear in the main Task, **ARTIFACTS** **>** **OTHER**.

![Artifacts](https://clear.ml/docs/latest/assets/images/examples_pytorch_distributed_example_09-17534b819a5b7a9327da438e5767bf0f.png#light-mode-only)![Artifacts](https://clear.ml/docs/latest/assets/images/examples_pytorch_distributed_example_09_dark-bfccacff19a0441ecf5fd92f90d37c6f.png#dark-mode-only)

## Scalars [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/pytorch_distributed_example/\#scalars "Direct link to Scalars")

Report loss to the main Task by calling [`Logger.report_scalar()`](https://clear.ml/docs/latest/docs/references/sdk/logger#report_scalar)
on `Task.current_task().get_logger`, which is the logger for the main Task. Since `Logger.report_scalar` is called with the
same title (`loss`), but a different series name (containing the subprocess' `rank`), all loss scalar series are logged together.

```python
Task.current_task().get_logger().report_scalar(

    title='loss',

    series='worker {:02d}'.format(dist.get_rank()),

    value=loss.item(),

    iteration=i

)
```

The single scalar plot for loss appears in **SCALARS**.

![Scalars](https://clear.ml/docs/latest/assets/images/examples_pytorch_distributed_example_08-0d13ce6dd51f1d5d1a4ffc1d081d25a9.png#light-mode-only)![Scalars](https://clear.ml/docs/latest/assets/images/examples_pytorch_distributed_example_08_dark-594535893f5a4e249fcf149aa6b7d818.png#dark-mode-only)

## Hyperparameters [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/pytorch_distributed_example/\#hyperparameters "Direct link to Hyperparameters")

ClearML automatically logs the command line options defined using `argparse`.

A parameter dictionary is logged by connecting it to the Task using [`Task.connect()`](https://clear.ml/docs/latest/docs/references/sdk/task#connect).

```python
param = {'worker_{}_stuff'.format(dist.get_rank()): 'some stuff ' + str(randint(0, 100))}

Task.current_task().connect(param)
```

Command line options appear in **CONFIGURATION** **>** **HYPERPARAMETERS** **>** **Args**.

![Hyperparameter Args](https://clear.ml/docs/latest/assets/images/examples_pytorch_distributed_example_01-8e71a59a3fa37659feec9bd401666f16.png#light-mode-only)![Hyperparameter Args](https://clear.ml/docs/latest/assets/images/examples_pytorch_distributed_example_01_dark-ea1ef7588cbc0d18509f8b3db3843e47.png#dark-mode-only)

Parameter dictionaries appear in the **General** section of **HYPERPARAMETERS**.

```python
param = {'worker_{}_stuff'.format(dist.get_rank()): 'some stuff ' + str(randint(0, 100))}

Task.current_task().connect(param)
```

![Hyperparameter General args](https://clear.ml/docs/latest/assets/images/examples_pytorch_distributed_example_02-bfeae5abc190bc7fee66e643a367ed1d.png#light-mode-only)![Hyperparameter General args](https://clear.ml/docs/latest/assets/images/examples_pytorch_distributed_example_02_dark-048e2e64afb4f56a86cbba5f0048be81.png#dark-mode-only)

## Log [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/pytorch_distributed_example/\#log "Direct link to Log")

Output to the console, including the text messages printed from the main Task object and each subprocess, appears in **CONSOLE**.

![Console log](https://clear.ml/docs/latest/assets/images/examples_pytorch_distributed_example_06-20e3c05a02a033c22b6ac4ba14edc293.png#light-mode-only)![Console log](https://clear.ml/docs/latest/assets/images/examples_pytorch_distributed_example_06_dark-03937e39336262f42969b2f3538ae22f.png#dark-mode-only)

- [Artifacts](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/pytorch_distributed_example/#artifacts)
- [Scalars](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/pytorch_distributed_example/#scalars)
- [Hyperparameters](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/pytorch_distributed_example/#hyperparameters)
- [Log](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/pytorch_distributed_example/#log)