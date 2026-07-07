---
url: "https://clear.ml/docs/latest/docs/guides/distributed/distributed_pytorch_example/"
title: "PyTorch Distributed | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/distributed/distributed_pytorch_example/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The [pytorch\_distributed\_example.py](https://github.com/clearml/clearml/blob/master/examples/frameworks/pytorch/pytorch_distributed_example.py)
script demonstrates integrating ClearML into code that uses the [PyTorch Distributed Communications Package](https://pytorch.org/docs/stable/distributed.html)
(`torch.distributed`).

The script initializes a main Task and spawns subprocesses, each for an instance of that Task.
The Task in each subprocess trains a neural network over a partitioned dataset (the torchvision built-in [MNIST](https://pytorch.org/vision/stable/datasets.html#mnist)
dataset), and reports (uploads) the following to the main Task:

- Artifacts - A dictionary containing different key-value pairs.
- Scalars - Loss reported as a scalar during training in each Task in a subprocess.
- Hyperparameters - Hyperparameters created in each Task are added to the hyperparameters in the main Task.

Each Task in a subprocess references the main Task by calling [`Task.current_task()`](https://clear.ml/docs/latest/docs/references/sdk/task#taskcurrent_task), which always returns
the main Task.

When the script runs, it creates a task named `test torch distributed` in the `examples` project.

## Artifacts [​](https://clear.ml/docs/latest/docs/guides/distributed/distributed_pytorch_example/\#artifacts "Direct link to Artifacts")

The example uploads a dictionary as an artifact in the main Task by calling [`Task.upload_artifact()`](https://clear.ml/docs/latest/docs/references/sdk/task#upload_artifact)
on [`Task.current_task()`](https://clear.ml/docs/latest/docs/references/sdk/task#taskcurrent_task) (the main Task). The dictionary contains the [`dist.rank`](https://pytorch.org/docs/stable/distributed.html#torch.distributed.get_rank)
of the subprocess, making each unique.

```python
Task.current_task().upload_artifact(

    name='temp {:02d}'.format(dist.get_rank()),

    artifact_object={'worker_rank': dist.get_rank()}

)
```

All of these artifacts appear in the main Task under **ARTIFACTS** **>** **OTHER**.

![Task artifacts](https://clear.ml/docs/latest/assets/images/examples_pytorch_distributed_example_09-17534b819a5b7a9327da438e5767bf0f.png#light-mode-only)![Task artifacts](https://clear.ml/docs/latest/assets/images/examples_pytorch_distributed_example_09_dark-bfccacff19a0441ecf5fd92f90d37c6f.png#dark-mode-only)

## Scalars [​](https://clear.ml/docs/latest/docs/guides/distributed/distributed_pytorch_example/\#scalars "Direct link to Scalars")

Loss is reported to the main Task by calling the [`Logger.report_scalar()`](https://clear.ml/docs/latest/docs/references/sdk/logger#report_scalar)
on `Task.current_task().get_logger()`, which is the main Task's logger. Since `Logger.report_scalar` is called
with the same title (`loss`), but a different series name (containing the subprocess' `rank`), all loss scalar series are
logged together.

```python
Task.current_task().get_logger().report_scalar(

    title='loss',

    series='worker {:02d}'.format(dist.get_rank()),

    value=loss.item(),

    iteration=i

)
```

The single scalar plot for loss appears in **SCALARS**.

![Task scalars](https://clear.ml/docs/latest/assets/images/examples_pytorch_distributed_example_08-0d13ce6dd51f1d5d1a4ffc1d081d25a9.png#light-mode-only)![Task scalars](https://clear.ml/docs/latest/assets/images/examples_pytorch_distributed_example_08_dark-594535893f5a4e249fcf149aa6b7d818.png#dark-mode-only)

## Hyperparameters [​](https://clear.ml/docs/latest/docs/guides/distributed/distributed_pytorch_example/\#hyperparameters "Direct link to Hyperparameters")

ClearML automatically logs the argparse command line options. Since the [`Task.connect`](https://clear.ml/docs/latest/docs/references/sdk/task#connect)
method is called on [`Task.current_task`](https://clear.ml/docs/latest/docs/references/sdk/task#taskcurrent_task), they are logged in the main Task. A different hyperparameter key is used in each
subprocess, so they do not overwrite each other in the main Task.

```python
param = {'worker_{}_stuff'.format(dist.get_rank()): 'some stuff ' + str(randint(0, 100))}

Task.current_task().connect(param)
```

All the hyperparameters appear in **CONFIGURATION** **>** **HYPERPARAMETERS**.

![Task hyperparameters Args](https://clear.ml/docs/latest/assets/images/examples_pytorch_distributed_example_01-8e71a59a3fa37659feec9bd401666f16.png#light-mode-only)![Task hyperparameters Args](https://clear.ml/docs/latest/assets/images/examples_pytorch_distributed_example_01_dark-ea1ef7588cbc0d18509f8b3db3843e47.png#dark-mode-only)

![Task hyperparameters General ](https://clear.ml/docs/latest/assets/images/examples_pytorch_distributed_example_02-bfeae5abc190bc7fee66e643a367ed1d.png#light-mode-only)![Task hyperparameters General ](https://clear.ml/docs/latest/assets/images/examples_pytorch_distributed_example_02_dark-048e2e64afb4f56a86cbba5f0048be81.png#dark-mode-only)

## Console [​](https://clear.ml/docs/latest/docs/guides/distributed/distributed_pytorch_example/\#console "Direct link to Console")

Output to the console, including the text messages printed from the main Task object and each subprocess appear in **CONSOLE**.

![Task console log](https://clear.ml/docs/latest/assets/images/examples_pytorch_distributed_example_06-20e3c05a02a033c22b6ac4ba14edc293.png#light-mode-only)![Task console log](https://clear.ml/docs/latest/assets/images/examples_pytorch_distributed_example_06_dark-03937e39336262f42969b2f3538ae22f.png#dark-mode-only)

- [Artifacts](https://clear.ml/docs/latest/docs/guides/distributed/distributed_pytorch_example/#artifacts)
- [Scalars](https://clear.ml/docs/latest/docs/guides/distributed/distributed_pytorch_example/#scalars)
- [Hyperparameters](https://clear.ml/docs/latest/docs/guides/distributed/distributed_pytorch_example/#hyperparameters)
- [Console](https://clear.ml/docs/latest/docs/guides/distributed/distributed_pytorch_example/#console)