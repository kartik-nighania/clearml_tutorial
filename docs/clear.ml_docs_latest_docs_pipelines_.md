---
url: "https://clear.ml/docs/latest/docs/pipelines/"
title: "ClearML Pipelines | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/pipelines/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

Pipelines are a way to streamline and connect multiple processes, plugging the output of one process as the input of another.

ClearML Pipelines are implemented by a _Controller Task_ that holds the logic of the pipeline steps' interactions. The execution logic
controls which step to launch based on parent steps completing their execution. Depending on the specifications
laid out in the controller task, a step's parameters can be overridden, enabling users to leverage other steps' execution
products such as artifacts and parameters.

When run, the controller will sequentially launch the pipeline steps. The pipeline logic and steps
can be executed locally, or on any machine using the [clearml-agent](https://clear.ml/docs/latest/docs/clearml_agent).

![Pipeline UI](https://clear.ml/docs/latest/assets/images/webapp_pipeline_DAG-3ad07262e9180a4d0d90cc41abef05e8.png#light-mode-only)![Pipeline UI](https://clear.ml/docs/latest/assets/images/webapp_pipeline_DAG_dark-526b6c702058bd0daf076bea6b750458.png#dark-mode-only)

The [Pipeline Run](https://clear.ml/docs/latest/docs/webapp/pipelines/webapp_pipeline_viewing) page in the web UI displays the pipeline's structure
in terms of executed steps and their status, as well as the run's configuration parameters and output. See [pipeline UI](https://clear.ml/docs/latest/docs/webapp/pipelines/webapp_pipeline_page)
for more details.

ClearML pipelines are created from code using one of the following:

- [PipelineController](https://clear.ml/docs/latest/docs/pipelines/pipelines_sdk_tasks) class - A pythonic interface for defining and configuring the pipeline
controller and its steps. The controller and steps can be functions in your Python code, or existing [ClearML tasks](https://clear.ml/docs/latest/docs/fundamentals/task).
- [PipelineDecorator](https://clear.ml/docs/latest/docs/pipelines/pipelines_sdk_function_decorators) class - A set of Python decorators which transform your
functions into the pipeline controller and steps

When the pipeline runs, corresponding ClearML tasks are created for the controller and steps.

Since a pipeline controller is itself a [ClearML task](https://clear.ml/docs/latest/docs/fundamentals/task), it can be used as a pipeline step.
This allows to create more complicated workflows, such as pipelines running other pipelines, or pipelines running multiple
tasks concurrently. See the [Tabular training pipeline](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/table/tabular_training_pipeline)
example of a pipeline with concurrent steps.

## Running Your Pipelines [​](https://clear.ml/docs/latest/docs/pipelines/\#running-your-pipelines "Direct link to Running Your Pipelines")

ClearML supports multiple modes for pipeline execution:

- **Remote Mode** (default) - In this mode, the pipeline controller logic is executed through a designated queue, and all
the pipeline steps are launched remotely through their respective queues. Since each task is executed independently,
it can have control over its git repository (if needed), required Python packages, and the specific container to use.
- **Local Mode** \- In this mode, the pipeline is executed locally, and the steps are executed as sub-processes. Each
subprocess uses the exact same Python environment as the main pipeline logic.
- **Debugging Mode** (for PipelineDecorator) - In this mode, the entire pipeline is executed locally, with the pipeline
controller and steps called synchronously as regular Python functions providing full ability to debug each function call.

When you run your pipeline, ClearML collects and stores all the information required to reproduce the run. You can rerun
the pipeline via the ClearML Web UI. See [Pipeline Runs](https://clear.ml/docs/latest/docs/pipelines/#pipeline-runs).

## Pipeline Features [​](https://clear.ml/docs/latest/docs/pipelines/\#pipeline-features "Direct link to Pipeline Features")

### Artifacts and Metrics [​](https://clear.ml/docs/latest/docs/pipelines/\#artifacts-and-metrics "Direct link to Artifacts and Metrics")

Each pipeline step can log additional artifacts and metrics on the step task with the usual flows (TB, Matplotlib, or with
[ClearML Logger](https://clear.ml/docs/latest/docs/fundamentals/logger)). To get the instance of the step's Task during runtime, use the
[`Task.current_task()`](https://clear.ml/docs/latest/docs/references/sdk/task#taskcurrent_task) class method.

Additionally, pipeline steps can directly report metrics or upload artifacts / models to the pipeline using these
PipelineController and PipelineDecorator class methods: `get_logger`, `upload_model`, `upload_artifact`.

The pipeline controller also supports automation for logging step metrics / artifacts / models on the pipeline task itself.
Each pipeline step can specify metrics / artifacts / models to also automatically log to the pipeline Task. The idea is
that pipeline steps report metrics internally while the pipeline automatically collects them into a unified view on the
pipeline Task. To enable the automatic logging, use the `monitor_metrics`, `monitor_artifacts`, `monitor_models` arguments
when creating a pipeline step.

### Pipeline Step Caching [​](https://clear.ml/docs/latest/docs/pipelines/\#pipeline-step-caching "Direct link to Pipeline Step Caching")

The Pipeline controller supports step caching, meaning, reusing outputs of previously executed pipeline steps.

Cached pipeline steps are reused when they meet the following criteria:

- The step code is the same, including environment setup (components in the task's [Execution](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual#execution)
section, like required packages and docker image)
- The step input arguments are unchanged, including step arguments and parameters (anything logged to the task's [Configuration](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual#configuration)
section)

By default, pipeline steps are not cached. Enable caching when creating a pipeline step (for example, see [`@PipelineDecorator.component`](https://clear.ml/docs/latest/docs/pipelines/pipelines_sdk_function_decorators#pipelinedecoratorcomponent)).

When a step is cached, the step code is hashed, alongside the step's parameters (as passed in runtime), into a single
representing hash string. The pipeline first checks if a cached step exists in the system (archived Tasks will not be used
as a cached instance). If the pipeline finds an existing fully executed instance of the step, it will plug its output directly,
allowing the pipeline logic to reuse the step outputs.

### Callbacks [​](https://clear.ml/docs/latest/docs/pipelines/\#callbacks "Direct link to Callbacks")

Callbacks can be utilized to control pipeline execution flow. A callback can be defined to be called before and/or after
the execution of every task in a pipeline. Additionally, you can create customized, step-specific callbacks.

### Pipeline Runs [​](https://clear.ml/docs/latest/docs/pipelines/\#pipeline-runs "Direct link to Pipeline Runs")

When you run your pipeline, ClearML collects and stores all the information required to reproduce the run (DAG,
configuration, installed packages, uncommitted changes etc.).

You can rerun the pipeline programmatically or via the ClearML Web UI:

- To programmatically create a new run, use [`PipelineController.clone()`](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller#pipelinecontrollerclone)
which returns a copy of the original pipeline in [_draft_](https://clear.ml/docs/latest/docs/fundamentals/task#task-states) state, allowing you to
modify any configuration. Run the new pipeline using [`PipelineController.start()`](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller#start).





```python
pipeline = PipelineController.get(pipeline_id="<pipeline_ID>")

cloned_pipeline = PipelineController.clone(pipeline_controller=pipeline)



# tweak pipeline parameters



cloned_pipeline.start()
```

- To launch a new pipeline run in the UI, click **\+ NEW RUN** in the [pipeline runs](https://clear.ml/docs/latest/docs/webapp/pipelines/webapp_pipeline_table) page. This opens a **NEW RUN** modal, where you
can set the run's parameters and execution queue.


![Pipeline params UI](https://clear.ml/docs/latest/assets/images/pipelines_new_run-701921888b5ae94b185051f566b06124.png#light-mode-only)![Pipeline params UI](https://clear.ml/docs/latest/assets/images/pipelines_new_run_dark-cc3180947311dd3269d74bbfad615488.png#dark-mode-only)

The new pipeline run will be executed through the execution queue by a ClearML agent. The agent will rebuild
the pipeline according to the configuration and DAG that was captured in the original run, and override the original
parameters' value with those input in the **NEW RUN** modal.

One exception is for pipelines [created from functions](https://clear.ml/docs/latest/docs/pipelines/pipelines_sdk_tasks#steps-from-functions) (adding steps to a
pipeline controller using [`PipelineController.add_function_step()`](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller#add_function_step)):
When you rerun the pipeline through the ClearML WebApp, the pipeline is constructed again at runtime from the executed
code.

To change this behavior, pass `always_create_from_code=False` when instantiating a `PipelineController`. In this case,
when rerun, the pipeline DAG will be generated from the pipeline configuration stored in the pipeline task. This
lets you modify the pipeline configuration via the UI, without changing the original codebase.

### Pipeline Versions [​](https://clear.ml/docs/latest/docs/pipelines/\#pipeline-versions "Direct link to Pipeline Versions")

You can assign each pipeline a version number to help track the evolution of your pipeline structure and parameters.
The pipeline's version automatically bumps up if there is a change in the pipeline code. If there is no change, the
pipeline retains its version number.

### Tracking Pipeline Progress [​](https://clear.ml/docs/latest/docs/pipelines/\#tracking-pipeline-progress "Direct link to Tracking Pipeline Progress")

ClearML automatically tracks a pipeline's progress percentage: the number of pipeline steps completed out of the total
number of steps. For example, if a pipeline consists of 4 steps, after the first step completes, ClearML automatically
sets its progress value to 25. Once a pipeline has started to run but is yet to successfully finish, the WebApp will
show the pipeline's progress indication in the pipeline runs table, next to the run's status.

## Examples [​](https://clear.ml/docs/latest/docs/pipelines/\#examples "Direct link to Examples")

See examples of building ClearML pipelines:

- [PipelineDecorator](https://clear.ml/docs/latest/docs/guides/pipeline/pipeline_decorator)
- PipelineController
  - [Pipeline from tasks](https://clear.ml/docs/latest/docs/guides/pipeline/pipeline_controller)
  - [Pipeline from functions](https://clear.ml/docs/latest/docs/guides/pipeline/pipeline_functions)

- [Running Your Pipelines](https://clear.ml/docs/latest/docs/pipelines/#running-your-pipelines)
- [Pipeline Features](https://clear.ml/docs/latest/docs/pipelines/#pipeline-features)
  - [Artifacts and Metrics](https://clear.ml/docs/latest/docs/pipelines/#artifacts-and-metrics)
  - [Pipeline Step Caching](https://clear.ml/docs/latest/docs/pipelines/#pipeline-step-caching)
  - [Callbacks](https://clear.ml/docs/latest/docs/pipelines/#callbacks)
  - [Pipeline Runs](https://clear.ml/docs/latest/docs/pipelines/#pipeline-runs)
  - [Pipeline Versions](https://clear.ml/docs/latest/docs/pipelines/#pipeline-versions)
  - [Tracking Pipeline Progress](https://clear.ml/docs/latest/docs/pipelines/#tracking-pipeline-progress)
- [Examples](https://clear.ml/docs/latest/docs/pipelines/#examples)