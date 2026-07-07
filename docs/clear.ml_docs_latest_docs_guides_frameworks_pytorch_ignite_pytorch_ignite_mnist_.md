---
url: "https://clear.ml/docs/latest/docs/guides/frameworks/pytorch_ignite/pytorch_ignite_mnist/"
title: "PyTorch Ignite ClearMLLogger | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch_ignite/pytorch_ignite_mnist/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The `ignite` repository contains the [mnist\_with\_clearml\_logger.py](https://github.com/pytorch/ignite/blob/master/examples/mnist/mnist_with_clearml_logger.py)
example script that uses [ignite](https://github.com/pytorch/ignite) and integrates **ClearMLLogger** and its [helper handlers](https://pytorch.org/ignite/v0.5.0.post2/generated/ignite.handlers.clearml_logger.html).

PyTorch Ignite supports a `ClearMLLogger` handler to log metrics, text, model / optimizer parameters, plots, and model
checkpoints during training and validation.

The example script does the following:

- Trains a model to classify images from the MNIST dataset.
- Creates a [ClearML Task](https://clear.ml/docs/latest/docs/fundamentals/task) named `ignite` in the `examples`
project. ClearMLLogger connects to ClearML so everything which is logged through it and its handlers
is automatically captured by ClearML.
- Uses the following ClearMLLogger helper handlers:
  - **ClearMLSaver** \- Saves input snapshots as ClearML artifacts.

  - **GradsHistHandler** and **WeightsHistHandler** \- Logs the model's gradients and weights respectively as histograms.

  - **GradsScalarHandler** and **WeightsScalarHandler** \- Logs gradients and weights respectively as scalars.

## ClearMLLogger [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch_ignite/pytorch_ignite_mnist/\#clearmllogger "Direct link to ClearMLLogger")

Integrate ClearML with the following steps:

1. Create a `ClearMLLogger` object. When the code runs, it connects to the ClearML backend, and creates a task in ClearML
(see ClearMLLogger's parameters [below](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch_ignite/pytorch_ignite_mnist/#parameters)).





```python
from ignite.contrib.handlers.clearml_logger import ClearMLLogger



clearml_logger = ClearMLLogger(project_name="examples", task_name="ignite")
```

2. Attach helper handlers to the `ClearMLLogger` object.

For example, attach the `OutputHandler` to log training loss at each iteration:





```python
clearml_logger.attach(

     trainer,

     log_handler=OutputHandler(tag="training",

     output_transform=lambda loss: {"loss": loss}),

     event_name=Events.ITERATION_COMPLETED

)
```


### Parameters [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch_ignite/pytorch_ignite_mnist/\#parameters "Direct link to Parameters")

The following are the `ClearMLLogger` parameters:

- `project_name` \- The name of the project in which the task will be created.
- `task_name` – The name of task.
- `task_type` – The type of task (see [task types](https://clear.ml/docs/latest/docs/fundamentals/task#task-types)).
- `report_freq` – The histogram processing frequency (handles histogram values every X calls to the handler). Affects
`GradsHistHandler` and `WeightsHistHandler`. Default value is 100.
- `histogram_update_freq_multiplier` – The histogram report frequency (report first X histograms and once every X
reports afterwards). Default value is 10.
- `histogram_granularity` \- Histogram sampling granularity. Default is 50.

### Logging [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch_ignite/pytorch_ignite_mnist/\#logging "Direct link to Logging")

To log scalars, ignite engine's output and/or metrics, use the `OutputHandler`.

- Log training loss at each iteration:

```python
clearml_logger.attach(

    trainer,

    log_handler=OutputHandler(tag="training",

    output_transform=lambda loss: {"loss": loss}),

    event_name=Events.ITERATION_COMPLETED

)
```

- Log metrics for training:

```python
clearml_logger.attach(

    train_evaluator,

    log_handler=OutputHandler(

        tag="training",

        metric_names=["nll", "accuracy"],

        global_step_transform=global_step_from_engine(trainer)

    ),

    event_name=Events.EPOCH_COMPLETED

)
```

- Log metrics for validation:

```python
clearml_logger.attach(

    evaluator,

    log_handler=OutputHandler(

        tag="validation",

        metric_names=["nll", "accuracy"],

        global_step_transform=global_step_from_engine(trainer)

    ),

    event_name=Events.EPOCH_COMPLETED

)
```

To log optimizer parameters, use the `attach_opt_params_handler` method:

```python
# Attach the logger to the trainer to log optimizer's parameters, e.g. learning rate at each iteration

clearml_logger.attach_opt_params_handler(

        trainer, event_name=Events.ITERATION_COMPLETED(every=100), optimizer=optimizer

)
```

### Model Weights [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch_ignite/pytorch_ignite_mnist/\#model-weights "Direct link to Model Weights")

To log model weights as scalars, use `WeightsScalarHandler`:

```python
from ignite.contrib.handlers.clearml_logger import WeightsScalarHandler

clearml_logger.attach(

    trainer,

    log_handler=WeightsScalarHandler(model, reduction=torch.norm),

    event_name=Events.ITERATION_COMPLETED

)
```

To log model weights as histograms, use `WeightsHistHandler`:

```python
from ignite.contrib.handlers.clearml_logger import WeightsHistHandler

clearml_logger.attach(

    trainer,

    log_handler=WeightsHistHandler(model),

    event_name=Events.ITERATION_COMPLETED

)
```

### Model Snapshots [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch_ignite/pytorch_ignite_mnist/\#model-snapshots "Direct link to Model Snapshots")

To save model checkpoints as ClearML artifacts, use `ClearMLSaver`:

```python
from ignite.handlers import Checkpoint

from ignite.contrib.handlers.clearml_logger import ClearMLSaver

handler = Checkpoint(

        {"model": model},

        ClearMLSaver(),

        n_saved=1,

        score_function=lambda e: e.state.metrics["accuracy"],

        score_name="val_acc",

        filename_prefix="best",

        global_step_transform=global_step_from_engine(trainer),

    )

validation_evaluator.add_event_handler(Events.EPOCH_COMPLETED, handler)
```

## Visualizing Task Results [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch_ignite/pytorch_ignite_mnist/\#visualizing-task-results "Direct link to Visualizing Task Results")

When the code runs, the task results can be viewed in the [ClearML Web UI](https://clear.ml/docs/latest/docs/webapp/webapp_overview).

### Scalars [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch_ignite/pytorch_ignite_mnist/\#scalars "Direct link to Scalars")

View the scalars, including training and validation metrics, in the task's page in the ClearML Web UI, under
**SCALARS**.

![Task scalars](https://clear.ml/docs/latest/assets/images/ignite_training-3452f4e221d995ef8e7f2dcfa77efc0b.png#light-mode-only)![Task scalars](https://clear.ml/docs/latest/assets/images/ignite_training_dark-fdeadf675e31d7b861c0d3f3a64bbbf9.png#dark-mode-only)

### Model Snapshots [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch_ignite/pytorch_ignite_mnist/\#model-snapshots-1 "Direct link to Model Snapshots")

View saved snapshots in the **ARTIFACTS** tab.

![Task Artifacts](https://clear.ml/docs/latest/assets/images/ignite_artifact-4b15a7b6cdaec5756e69fa2c71e1e02c.png#light-mode-only)![Task Artifacts](https://clear.ml/docs/latest/assets/images/ignite_artifact_dark-041be2350ec8793d1383e9f3a531230a.png#dark-mode-only)

To view model details, in the **ARTIFACTS** tab, click the model name (or download it).

![Model details](https://clear.ml/docs/latest/assets/images/ignite_model-a258cbbe52eb787924418d3db21fd06b.png#light-mode-only)![Model details](https://clear.ml/docs/latest/assets/images/ignite_model_dark-0249e95fbd5419b90fce7083f2fc0672.png#dark-mode-only)

- [ClearMLLogger](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch_ignite/pytorch_ignite_mnist/#clearmllogger)
  - [Parameters](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch_ignite/pytorch_ignite_mnist/#parameters)
  - [Logging](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch_ignite/pytorch_ignite_mnist/#logging)
  - [Model Weights](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch_ignite/pytorch_ignite_mnist/#model-weights)
  - [Model Snapshots](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch_ignite/pytorch_ignite_mnist/#model-snapshots)
- [Visualizing Task Results](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch_ignite/pytorch_ignite_mnist/#visualizing-task-results)
  - [Scalars](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch_ignite/pytorch_ignite_mnist/#scalars)
  - [Model Snapshots](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch_ignite/pytorch_ignite_mnist/#model-snapshots-1)