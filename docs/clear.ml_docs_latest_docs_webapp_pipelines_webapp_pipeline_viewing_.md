---
url: "https://clear.ml/docs/latest/docs/webapp/pipelines/webapp_pipeline_viewing/"
title: "Pipeline Run Details | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/webapp/pipelines/webapp_pipeline_viewing/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The run details panel shows the pipeline's structure and the execution status of every step, as well as the run's
configuration parameters and output.

![Pipeline structure](https://clear.ml/docs/latest/assets/images/webapp_pipeline_DAG-3ad07262e9180a4d0d90cc41abef05e8.png#light-mode-only)![Pipeline structure](https://clear.ml/docs/latest/assets/images/webapp_pipeline_DAG_dark-526b6c702058bd0daf076bea6b750458.png#dark-mode-only)

Each step shows:

![Pipeline step info](<Base64-Image-Removed>)![Pipeline step info](<Base64-Image-Removed>)

- Step name
- Step status
- Step execution time
- Step log button - Hover over the step and click ![console](https://clear.ml/docs/latest/icons/ico-console.svg)
to view the step's [details panel](https://clear.ml/docs/latest/docs/webapp/pipelines/webapp_pipeline_viewing/#run-and-step-details-panel)

While the pipeline is running, the steps' details and colors are updated.

## Run Stages [​](https://clear.ml/docs/latest/docs/webapp/pipelines/webapp_pipeline_viewing/\#run-stages "Direct link to Run Stages")

Steps that were set into the same stage when created, are grouped into stages in the Run Details panel.

In stages view, click `Expand Stages` to view the complete pipeline DAG with all steps visible.
In the detailed view, click `Collapse Stages` to view the pipeline DAG outline with the same stage steps grouped into a single stage.

![Pipeline structure in stages](https://clear.ml/docs/latest/assets/images/webapp_pipeline_DAG_collapsed-e3f0737a89f2457510f7f98950b18795.png#light-mode-only)![Pipeline structure in stages](https://clear.ml/docs/latest/assets/images/webapp_pipeline_DAG_collapsed_dark-b40249dd33726a7b4712af60b54f70ea.png#dark-mode-only)

In the collapsed view, each stage displays:

![Pipeline stage card](<Base64-Image-Removed>)![Pipeline stage card](<Base64-Image-Removed>)

- Stage name
- Number of steps in stage

Click ![Expand](https://clear.ml/docs/latest/icons/ico-zoom-to-fit.svg) to view the
steps that comprise the stage. Select a step to view its [Step Info](https://clear.ml/docs/latest/docs/webapp/pipelines/webapp_pipeline_viewing/#run-and-step-info).

Click on a stage to view its **STAGE INFO**:

![Pipeline stage info](https://clear.ml/docs/latest/assets/images/webapp_pipeline_stage_info-0c634b02e594424e1f21a18b401973b4.png#light-mode-only)![Pipeline stage info](https://clear.ml/docs/latest/assets/images/webapp_pipeline_stage_info_dark-d36e5f63ada1f758ba3112bfe2a88816.png#dark-mode-only)

- Stage name
- Step count by status - The number of steps in each status category (e.g. completed, running, pending)

## Run and Step Details [​](https://clear.ml/docs/latest/docs/webapp/pipelines/webapp_pipeline_viewing/\#run-and-step-details "Direct link to Run and Step Details")

### Run and Step Info [​](https://clear.ml/docs/latest/docs/webapp/pipelines/webapp_pipeline_viewing/\#run-and-step-info "Direct link to Run and Step Info")

On the pipeline run panel, view the **RUN INFO** which shows:

- Run Parameters
- Reported Metrics
- Produced Artifacts
- Output Models

![Run info](https://clear.ml/docs/latest/assets/images/webapp_pipeline_run_info-f5c55dacf8ee3d68a6dec46463fc35c6.png#light-mode-only)![Run info](https://clear.ml/docs/latest/assets/images/webapp_pipeline_run_info_dark-3d54d352dff24fc6c5220ec6909b0d50.png#dark-mode-only)

To view a run's complete information, click **Full details**, which will open the pipeline's controller [task page](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual).
View each list's complete details in the pipeline task's corresponding tabs:

- **PARAMETERS** list > **CONFIGURATION** tab
- **METRICS** list > **SCALARS** tab
- **ARTIFACTS** and **MODELS** lists > **ARTIFACTS** tab

![Pipeline task info](https://clear.ml/docs/latest/assets/images/webapp_pipeline_task_info-652e425dc0ff39ad6fca2f93e261f5b3.png#light-mode-only)![Pipeline task info](https://clear.ml/docs/latest/assets/images/webapp_pipeline_task_info_dark-6871931ea08163896b3d00f9e9703aa2.png#dark-mode-only)

To view a specific step's information, click the step on the execution graph, and the info panel displays its **STEP INFO**.
The panel displays the step's name, task type, and status, as well as its parameters, metrics, artifacts, and models.

![Step info](https://clear.ml/docs/latest/assets/images/webapp_pipeline_step_info-6a13e8cea5d7276fb709a590e3f8699a.png#light-mode-only)![Step info](https://clear.ml/docs/latest/assets/images/webapp_pipeline_step_info_dark-e25368d59ebb9d223700496009484809.png#dark-mode-only)

To return to viewing the run's information, click the pipeline graph, outside any of the steps.

### Run and Step Details Panel [​](https://clear.ml/docs/latest/docs/webapp/pipelines/webapp_pipeline_viewing/\#run-and-step-details-panel "Direct link to Run and Step Details Panel")

Click on **DETAILS** on the top left of the info panel to view the pipeline controller's details panel. To view a step's
details panel, click **DETAILS** and then click on a step node, or hover over a step node and click ![details](https://clear.ml/docs/latest/icons/ico-console.svg).

The details panel includes three tabs:

- **Preview** \- View debug samples and plots attached to the pipeline controller or step

![preview](https://clear.ml/docs/latest/assets/images/webapp_pipeline_step_debug-8cc2cb12f9c2e8a71162507799396daa.png#light-mode-only)![preview](https://clear.ml/docs/latest/assets/images/webapp_pipeline_step_debug_dark-c0bc787db3755b3bd6f3dc97364e4c3c.png#dark-mode-only)

- **Console** \- The console log for the pipeline controller or steps: contains everything printed to stdout and stderr.

![console](https://clear.ml/docs/latest/assets/images/webapp_pipeline_step_console-a2bcba95700a11cee5abfff08bcc7ace.png#light-mode-only)![console](https://clear.ml/docs/latest/assets/images/webapp_pipeline_step_console_dark-d542d302b9e400213993e66981f20c0a.png#dark-mode-only)

- **Code** \- For pipeline steps generated from functions using either [`PipelineController.add_function_step`](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller#add_function_step)
or [`PipelineDecorator.component`](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinedecorator#pipelinedecoratorcomponent),
you can view the selected step's code.

![code](https://clear.ml/docs/latest/assets/images/webapp_pipeline_step_code-051a29efb0261bfc1d052b3c27e25510.png#light-mode-only)![code](https://clear.ml/docs/latest/assets/images/webapp_pipeline_step_code_dark-22f14f3ce9201135b56326676fd3b78e.png#dark-mode-only)


Click ![Expand](https://clear.ml/docs/latest/icons/ico-max-panel.svg) on the details panel header to view the panel in full screen.

- [Run Stages](https://clear.ml/docs/latest/docs/webapp/pipelines/webapp_pipeline_viewing/#run-stages)
- [Run and Step Details](https://clear.ml/docs/latest/docs/webapp/pipelines/webapp_pipeline_viewing/#run-and-step-details)
  - [Run and Step Info](https://clear.ml/docs/latest/docs/webapp/pipelines/webapp_pipeline_viewing/#run-and-step-info)
  - [Run and Step Details Panel](https://clear.ml/docs/latest/docs/webapp/pipelines/webapp_pipeline_viewing/#run-and-step-details-panel)