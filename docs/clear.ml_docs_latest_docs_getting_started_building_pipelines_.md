---
url: "https://clear.ml/docs/latest/docs/getting_started/building_pipelines/"
title: "Building Pipelines | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/getting_started/building_pipelines/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

Pipelines are a way to streamline and connect multiple processes, plugging the output of one process as the input of another.

ClearML Pipelines are implemented by a Controller Task that holds the logic of the pipeline steps' interactions. The
execution logic controls which step to launch based on parent steps completing their execution. Depending on the
specifications laid out in the controller task, a step's parameters can be overridden, enabling users to leverage other
steps' execution products such as artifacts and parameters.

When run, the controller will sequentially launch the pipeline steps. Pipelines can be executed locally or
on any machine using the [clearml-agent](https://clear.ml/docs/latest/docs/clearml_agent).

ClearML pipelines are created from code using one of the following:

- [PipelineController class](https://clear.ml/docs/latest/docs/pipelines/pipelines_sdk_tasks) \- A pythonic interface for defining and configuring the
pipeline controller and its steps. The controller and steps can be functions in your Python code or existing ClearML tasks.
- [PipelineDecorator class](https://clear.ml/docs/latest/docs/pipelines/pipelines_sdk_function_decorators) \- A set of Python decorators which transform
your functions into the pipeline controller and steps

For more information, see [ClearML Pipelines](https://clear.ml/docs/latest/docs/pipelines/).

![Pipeline DAG](https://clear.ml/docs/latest/assets/images/webapp_pipeline_DAG-3ad07262e9180a4d0d90cc41abef05e8.png#light-mode-only)![Pipeline DAG](https://clear.ml/docs/latest/assets/images/webapp_pipeline_DAG_dark-526b6c702058bd0daf076bea6b750458.png#dark-mode-only)