---
url: "https://clear.ml/docs/latest/docs/guides/advanced/execute_remotely/"
title: "Remote Execution | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/advanced/execute_remotely/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The [execute\_remotely\_example](https://github.com/clearml/clearml/blob/master/examples/advanced/execute_remotely_example.py)
script demonstrates the use of the [`Task.execute_remotely()`](https://clear.ml/docs/latest/docs/references/sdk/task#execute_remotely) method.

note

Make sure to have at least one [ClearML Agent](https://clear.ml/docs/latest/docs/clearml_agent) running and assigned to listen to the `default` queue:

```text
clearml-agent daemon --queue default
```

## Execution Flow [​](https://clear.ml/docs/latest/docs/guides/advanced/execute_remotely/\#execution-flow "Direct link to Execution Flow")

The script trains a simple deep neural network on the PyTorch built-in MNIST dataset. The following describes the code's
execution flow:

1. The training runs for one epoch.
2. The code uses [`Task.execute_remotely()`](https://clear.ml/docs/latest/docs/references/sdk/task#execute_remotely), which terminates the local execution of the code and enqueues the task
to the `default` queue, as specified in the `queue_name` parameter.
3. An agent listening to the queue fetches the task and restarts task execution remotely. When the agent executes the task,
the `execute_remotely` is considered no-op.

An execution flow that uses `execute_remotely` is especially helpful when running code on a development machine for a few iterations
to debug and to make sure the code doesn't crash, or to set up an environment. After that, the training can be
moved to be executed by a stronger machine.

During the execution of the example script, the code does the following:

- Uses ClearML's automatic and explicit logging.
- Creates a task named `Remote_execution PyTorch MNIST train` in the `examples` project.

## Scalars [​](https://clear.ml/docs/latest/docs/guides/advanced/execute_remotely/\#scalars "Direct link to Scalars")

In the example script's `train` function, the following code explicitly reports scalars to ClearML:

```python
Logger.current_logger().report_scalar(

    title="train",

    series="loss",

    iteration=(epoch * len(train_loader) + batch_idx),

    value=loss.item()

)
```

In the script's `test` function, the code explicitly reports `loss` and `accuracy` scalars.

```python
Logger.current_logger().report_scalar(

    title="test", series="loss", iteration=epoch, value=test_loss

)

Logger.current_logger().report_scalar(

    title="test", series="accuracy", iteration=epoch, value=(correct / len(test_loader.dataset))

)
```

These scalars can be visualized in plots, which appear in the ClearML web UI, in the task's **SCALARS** tab.

![Task Scalars](https://clear.ml/docs/latest/assets/images/examples_pytorch_mnist_07-7a449692f9d3feb79b8e9e5e519cc5e4.png#light-mode-only)![Task Scalars](https://clear.ml/docs/latest/assets/images/examples_pytorch_mnist_07_dark-eb096d9773c37e3cccc508159ef1d6c1.png#dark-mode-only)

## Hyperparameters [​](https://clear.ml/docs/latest/docs/guides/advanced/execute_remotely/\#hyperparameters "Direct link to Hyperparameters")

ClearML automatically logs command line options defined with `argparse`. They appear in **CONFIGURATION** **>** **HYPERPARAMETERS** **>** **Args**.

![Task hyperparameters](https://clear.ml/docs/latest/assets/images/examples_pytorch_mnist_01-3967d61d03d54b5686dd5a9d904031b4.png#light-mode-only)![Task hyperparameters](https://clear.ml/docs/latest/assets/images/examples_pytorch_mnist_01_dark-7c734374621596c90ecae6a03650f89e.png#dark-mode-only)

## Console [​](https://clear.ml/docs/latest/docs/guides/advanced/execute_remotely/\#console "Direct link to Console")

Text printed to the console for training progress, as well as all other console output, appear in **CONSOLE**.

![Task console log](https://clear.ml/docs/latest/assets/images/examples_pytorch_mnist_06-3bf370af437ddc31f0b970a31bd6986c.png#light-mode-only)![Task console log](https://clear.ml/docs/latest/assets/images/examples_pytorch_mnist_06_dark-c5b3194d24eb5a72dddbca797610b0ec.png#dark-mode-only)

## Artifacts [​](https://clear.ml/docs/latest/docs/guides/advanced/execute_remotely/\#artifacts "Direct link to Artifacts")

Models created by the task appear in the task's **ARTIFACTS** tab. ClearML automatically logs and tracks models
and any snapshots created using PyTorch.

![Task artifacts](https://clear.ml/docs/latest/assets/images/examples_remote_execution_artifacts-8ef8f3f932685ed221b08be198cb2fb3.png#light-mode-only)![Task artifacts](https://clear.ml/docs/latest/assets/images/examples_remote_execution_artifacts_dark-0a62f69994e229dc89e28ef8d29070e6.png#dark-mode-only)

- [Execution Flow](https://clear.ml/docs/latest/docs/guides/advanced/execute_remotely/#execution-flow)
- [Scalars](https://clear.ml/docs/latest/docs/guides/advanced/execute_remotely/#scalars)
- [Hyperparameters](https://clear.ml/docs/latest/docs/guides/advanced/execute_remotely/#hyperparameters)
- [Console](https://clear.ml/docs/latest/docs/guides/advanced/execute_remotely/#console)
- [Artifacts](https://clear.ml/docs/latest/docs/guides/advanced/execute_remotely/#artifacts)