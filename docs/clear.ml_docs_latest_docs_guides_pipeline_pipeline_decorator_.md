---
url: "https://clear.ml/docs/latest/docs/guides/pipeline/pipeline_decorator/"
title: "Pipeline from Decorators | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/pipeline/pipeline_decorator/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The [pipeline\_from\_decorator.py](https://github.com/clearml/clearml/blob/master/examples/pipeline/pipeline_from_decorator.py)
example demonstrates the creation of a pipeline in ClearML using the [`PipelineDecorator`](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinedecorator#class-automationcontrollerpipelinedecorator)
class.

This example creates a pipeline incorporating four tasks, each of which is created from a Python function using a custom decorator:

- `executing_pipeline`\- Implements the pipeline controller which defines the pipeline structure and execution logic.
- `step_one` \- Downloads and processes data.
- `step_two` \- Further processes the data from `step_one`.
- `step_three` \- Uses the processed data from `step_two` to train a model.
- `step_four` \- Uses data from `step_two` and the model from `step_three` to make a prediction.

The pipeline steps, defined in the `step_one`, `step_two`, `step_three`, and `step_four` functions, are each wrapped with the
[`@PipelineDecorator.component`](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinedecorator#pipelinedecoratorcomponent)
decorator, which creates a ClearML pipeline step for each one when the pipeline is executed.

The logic that executes these steps and controls the interaction between them is implemented in the `executing_pipeline`
function. This function is wrapped with the [`@PipelineDecorator.pipeline`](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinedecorator#pipelinedecoratorpipeline)
decorator which creates the ClearML pipeline task when it is executed.

The sections below describe in more detail what happens in the pipeline controller and steps.

## Pipeline Controller [​](https://clear.ml/docs/latest/docs/guides/pipeline/pipeline_decorator/\#pipeline-controller "Direct link to Pipeline Controller")

In this example, the pipeline controller is implemented by the `executing_pipeline` function.

Using the `@PipelineDecorator.pipeline` decorator creates a ClearML Controller Task from the function when it is executed.
For detailed information, see [`@PipelineDecorator.pipeline`](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinedecorator#pipelinedecoratorpipeline).

In the example script, the controller defines the interactions between the pipeline steps in the following way:

1. The controller function passes its argument, `pickle_url`, to the pipeline's first step (`step_one`)
2. The returned data from the first step, `data_frame`, is passed to `step_two`
3. Returned data from the second step's output, `X_train` and `y_train`, is passed to `step_three`
4. Returned data from the second step's output, `X_test` and `y_test`, and the output from the third step `model` is
passed to `step_four`.

Local Execution

In this example, the pipeline is set to run in local mode by using
[`PipelineDecorator.run_locally()`](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinedecorator#pipelinedecoratorrun_locally)
before calling the pipeline function. See pipeline execution options [here](https://clear.ml/docs/latest/docs/pipelines/pipelines_sdk_function_decorators#running-the-pipeline).

## Pipeline Steps [​](https://clear.ml/docs/latest/docs/guides/pipeline/pipeline_decorator/\#pipeline-steps "Direct link to Pipeline Steps")

Using the `@PipelineDecorator.component` decorator will make the function a pipeline component that can be called from the
pipeline controller, which implements the pipeline's execution logic. For detailed information, see [`@PipelineDecorator.component`](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinedecorator#pipelinedecoratorcomponent).

When the pipeline controller calls a pipeline step, a corresponding ClearML task will be created. Notice that all package
imports inside the function will be automatically logged as required packages for the pipeline execution step.

## Pipeline Execution [​](https://clear.ml/docs/latest/docs/guides/pipeline/pipeline_decorator/\#pipeline-execution "Direct link to Pipeline Execution")

```python
PipelineDecorator.set_default_execution_queue('default')

# PipelineDecorator.debug_pipeline()

executing_pipeline(

    pickle_url='https://github.com/clearml/events/raw/master/odsc20-east/generic/iris_dataset.pkl',

)
```

By default, the pipeline controller and the pipeline steps are launched through ClearML [queues](https://clear.ml/docs/latest/docs/fundamentals/agents_and_queues#what-is-a-queue).
Use the [`PipelineDecorator.set_default_execution_queue`](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinedecorator#pipelinedecoratorset_default_execution_queue)
method to specify the execution queue of all pipeline steps. The `execution_queue` parameter of the `@PipelineDecorator.component`
decorator overrides the default queue value for the specific step for which it was specified.

Execution Modes

ClearML provides different pipeline execution modes to accommodate development and production use cases. For additional
details, see [Execution Modes](https://clear.ml/docs/latest/docs/pipelines/#running-your-pipelines).

To run the pipeline, call the pipeline controller function.

## WebApp [​](https://clear.ml/docs/latest/docs/guides/pipeline/pipeline_decorator/\#webapp "Direct link to WebApp")

When the task is executed, the console output displays the task ID, and links to the pipeline controller task page and pipeline page.

```text
ClearML Task: created new task id=bc93610688f242ecbbe70f413ff2cf5f

ClearML results page: https://app.clear.ml/projects/462f48dba7b441ffb34bddb783711da7/experiments/bc93610688f242ecbbe70f413ff2cf5f/output/log

ClearML pipeline page: https://app.clear.ml/pipelines/462f48dba7b441ffb34bddb783711da7/experiments/bc93610688f242ecbbe70f413ff2cf5f
```

The pipeline run's page contains the pipeline's structure, the execution status of every step, as well as the run's
configuration parameters and output.

![Pipeline DAG](https://clear.ml/docs/latest/assets/images/examples_pipeline_from_decorator_DAG-f866a0dbf81781e51e58b1db654188ba.png#light-mode-only)![Pipeline DAG](https://clear.ml/docs/latest/assets/images/examples_pipeline_from_decorator_DAG_dark-ee215c64e202415a6dc1d8026d3b87d5.png#dark-mode-only)

To view a run's complete information, click **Full details** on the bottom of the **Run Info** panel, which will open the
pipeline's [controller task page](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual).

Click a step to see an overview of its details.

![Pipeline step info](https://clear.ml/docs/latest/assets/images/examples_pipeline_from_decorator_step_info-ab5d410dfe307e46040a5059ea6387bd.png#light-mode-only)![Pipeline step info](https://clear.ml/docs/latest/assets/images/examples_pipeline_from_decorator_step_info_dark-040b76fbaa060b8eb1942c107a1bea04.png#dark-mode-only)

## Console and Code [​](https://clear.ml/docs/latest/docs/guides/pipeline/pipeline_decorator/\#console-and-code "Direct link to Console and Code")

Click **DETAILS** to view a log of the pipeline controller's console output.

![Pipeline console](https://clear.ml/docs/latest/assets/images/examples_pipeline_from_decorator_console-9634930c3aac279aa33340d742a3037b.png#light-mode-only)![Pipeline console](https://clear.ml/docs/latest/assets/images/examples_pipeline_from_decorator_console_dark-d51d8cd51feb7d7ebb223a45cf50b620.png#dark-mode-only)

Click on a step to view its console output. You can also view the selected step's code by clicking **CODE**
on top of the console log.

![Pipeline step code](https://clear.ml/docs/latest/assets/images/examples_pipeline_from_decorator_code-ed7725798b2a285b810e5f638587cc74.png#light-mode-only)![Pipeline step code](https://clear.ml/docs/latest/assets/images/examples_pipeline_from_decorator_code_dark-d940a6abf92d9d9b02e23d99daaa7c8a.png#dark-mode-only)

- [Pipeline Controller](https://clear.ml/docs/latest/docs/guides/pipeline/pipeline_decorator/#pipeline-controller)
- [Pipeline Steps](https://clear.ml/docs/latest/docs/guides/pipeline/pipeline_decorator/#pipeline-steps)
- [Pipeline Execution](https://clear.ml/docs/latest/docs/guides/pipeline/pipeline_decorator/#pipeline-execution)
- [WebApp](https://clear.ml/docs/latest/docs/guides/pipeline/pipeline_decorator/#webapp)
- [Console and Code](https://clear.ml/docs/latest/docs/guides/pipeline/pipeline_decorator/#console-and-code)