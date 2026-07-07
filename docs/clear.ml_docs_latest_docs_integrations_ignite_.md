---
url: "https://clear.ml/docs/latest/docs/integrations/ignite/"
title: "PyTorch Ignite | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/integrations/ignite/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

tip

If you are not already using ClearML, see [ClearML Setup instructions](https://clear.ml/docs/latest/docs/clearml_sdk/clearml_sdk_setup).

[PyTorch Ignite](https://pytorch.org/ignite/index.html) is a library for training and evaluating neural networks in
PyTorch. You can integrate ClearML into your code using Ignite's built-in loggers: [TensorboardLogger](https://clear.ml/docs/latest/docs/integrations/ignite/#tensorboardlogger)
and [ClearMLLogger](https://clear.ml/docs/latest/docs/integrations/ignite/#clearmllogger).

## TensorboardLogger [​](https://clear.ml/docs/latest/docs/integrations/ignite/\#tensorboardlogger "Direct link to TensorboardLogger")

ClearML integrates seamlessly with TensorboardLogger, and automatically captures all information logged through the
handler: metrics, parameters, images, and gradients.

All you have to do is add two lines of code to your script:

```python
from clearml import Task

task = Task.init(task_name="<task_name>", project_name="<project_name>")
```

This will create a [ClearML Task](https://clear.ml/docs/latest/docs/fundamentals/task) that captures your script's information, including Git details,
uncommitted code, Python environment, all information logged through `TensorboardLogger`, and more.

Visualize all the captured information in the task's page in ClearML's [WebApp](https://clear.ml/docs/latest/docs/integrations/ignite/#webapp).

See a code example [here](https://github.com/clearml/clearml/blob/master/examples/frameworks/ignite/cifar_ignite.py).

## ClearMLLogger [​](https://clear.ml/docs/latest/docs/integrations/ignite/\#clearmllogger "Direct link to ClearMLLogger")

PyTorch Ignite supports a ClearML Logger to log metrics, text, model/optimizer parameters, plots, and model checkpoints
during training and validation.

Integrate ClearML with the following steps:

1. Create a `ClearMLLogger` object:





```python
from ignite.contrib.handlers.clearml_logger import *



clearml_logger = ClearMLLogger(task_name="ignite", project_name="examples")
```









This creates a [ClearML Task](https://clear.ml/docs/latest/docs/fundamentals/task) called `ignite` in the `examples` project, which captures your
script's information, including Git details, uncommitted code, Python environment.

You can also pass the following parameters to the `ClearMLLogger` object:
   - `task_type` – The type of task (see [task types](https://clear.ml/docs/latest/docs/fundamentals/task#task-types)).
   - `report_freq` – The histogram processing frequency (handles histogram values every X calls to the handler). Affects
     `GradsHistHandler` and `WeightsHistHandler` (default: 100).
   - `histogram_update_freq_multiplier` – The histogram report frequency (report first X histograms and once every X
     reports afterwards) (default: 10).
   - `histogram_granularity` \- Histogram sampling granularity (default: 50).
2. Attach the `ClearMLLogger` to output handlers to log metrics:





```python
# Attach the logger to the trainer to log training loss

clearml_logger.attach_output_handler(

       trainer,

       event_name=Events.ITERATION_COMPLETED(every=100),

       tag="training",

       output_transform=lambda loss: {"batchloss": loss},

)



# Attach the logger to log loss and accuracy for both training and validation

for tag, evaluator in [("training metrics", train_evaluator), ("validation metrics", validation_evaluator)]:

       clearml_logger.attach_output_handler(

           evaluator,

           event_name=Events.EPOCH_COMPLETED,

           tag=tag,

           metric_names=["loss", "accuracy"],

           global_step_transform=global_step_from_engine(trainer),

       )
```

3. Attach the `ClearMLLogger` object to helper handlers to log task outputs. Ignite supports the following helper handlers for ClearML:


   - **ClearMLSaver** \- Saves input snapshots as ClearML artifacts.
   - **GradsHistHandler** and **WeightsHistHandler** \- Logs the model's gradients and weights respectively as histograms.
   - **GradsScalarHandler** and **WeightsScalarHandler** \- Logs gradients and weights respectively as scalars.
   - **OptimizerParamsHandler** \- Logs optimizer parameters

```python
# Attach the logger to the trainer to log model's weights norm

clearml_logger.attach(

    trainer, log_handler=WeightsScalarHandler(model), event_name=Events.ITERATION_COMPLETED(every=100)

)

# Attach the logger to the trainer to log model's weights as a histogram

clearml_logger.attach(trainer, log_handler=WeightsHistHandler(model), event_name=Events.EPOCH_COMPLETED(every=100))

# Attach the logger to the trainer to log model's gradients as scalars

clearml_logger.attach(

    trainer, log_handler=GradsScalarHandler(model), event_name=Events.ITERATION_COMPLETED(every=100)

)

#Attach the logger to the trainer to log model's gradients as a histogram

clearml_logger.attach(trainer, log_handler=GradsHistHandler(model), event_name=Events.EPOCH_COMPLETED(every=100))

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

# Attach the logger to the trainer to log optimizer's parameters, e.g. learning rate at each iteration

clearml_logger.attach(

   trainer,

   log_handler=OptimizerParamsHandler(optimizer),

   event_name=Events.ITERATION_STARTED

)
```

Visualize all the captured information in the task's page in ClearML's [WebApp](https://clear.ml/docs/latest/docs/integrations/ignite/#webapp).

For more information, see the [ignite documentation](https://pytorch.org/ignite/v0.5.0.post2/generated/ignite.handlers.clearml_logger.html).

See code example [here](https://github.com/pytorch/ignite/blob/master/examples/mnist/mnist_with_clearml_logger.py).

## WebApp [​](https://clear.ml/docs/latest/docs/integrations/ignite/\#webapp "Direct link to WebApp")

All the task information that ClearML captures can be viewed in the [WebApp](https://clear.ml/docs/latest/docs/webapp/webapp_overview):

### Models [​](https://clear.ml/docs/latest/docs/integrations/ignite/\#models "Direct link to Models")

View saved model snapshots in the **ARTIFACTS** tab.

![Model snapshots](https://clear.ml/docs/latest/assets/images/ignite_artifact-4b15a7b6cdaec5756e69fa2c71e1e02c.png#light-mode-only)![Model snapshots](https://clear.ml/docs/latest/assets/images/ignite_artifact_dark-041be2350ec8793d1383e9f3a531230a.png#dark-mode-only)

### Scalars [​](https://clear.ml/docs/latest/docs/integrations/ignite/\#scalars "Direct link to Scalars")

View the scalars in the task's **SCALARS** tab.

![Scalars](https://clear.ml/docs/latest/assets/images/examples_cifar_scalars-4df44ac28557bec117e421cd376c41e0.png#light-mode-only)![Scalars](https://clear.ml/docs/latest/assets/images/examples_cifar_scalars_dark-645e91a598a1dad6b9f26df46503fbcb.png#dark-mode-only)

### Debug Samples [​](https://clear.ml/docs/latest/docs/integrations/ignite/\#debug-samples "Direct link to Debug Samples")

ClearML automatically tracks images logged to `TensorboardLogger`. They appear in the task's **DEBUG SAMPLES**.

![Debug Samples](https://clear.ml/docs/latest/assets/images/examples_integration_pytorch_ignite_debug-6bcf86ff36ee2f8a0f54ecbc487575b3.png#light-mode-only)![Debug Samples](https://clear.ml/docs/latest/assets/images/examples_integration_pytorch_ignite_debug_dark-23e79575e805126ab0dcb2c4e11f5497.png#dark-mode-only)

- [TensorboardLogger](https://clear.ml/docs/latest/docs/integrations/ignite/#tensorboardlogger)
- [ClearMLLogger](https://clear.ml/docs/latest/docs/integrations/ignite/#clearmllogger)
- [WebApp](https://clear.ml/docs/latest/docs/integrations/ignite/#webapp)
  - [Models](https://clear.ml/docs/latest/docs/integrations/ignite/#models)
  - [Scalars](https://clear.ml/docs/latest/docs/integrations/ignite/#scalars)
  - [Debug Samples](https://clear.ml/docs/latest/docs/integrations/ignite/#debug-samples)