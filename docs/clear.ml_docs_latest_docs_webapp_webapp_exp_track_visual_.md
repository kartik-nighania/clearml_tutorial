---
url: "https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/"
title: "Tracking Tasks and Visualizing Results | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

While a task is running, and any time after it finishes, track it and visualize the results in the ClearML Web UI,
including:

- [Execution details](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/#execution) \- Code, the container image used for [ClearML Agent](https://clear.ml/docs/latest/docs/clearml_agent), output destination for artifacts, and the logging level.
- [Configuration](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/#configuration) \- Hyperparameters, user properties, and configuration objects.
- [Artifacts](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/#artifacts) \- Input model, output model, model snapshot locations, other artifacts.
- [Info](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/#info) \- Extended task information, such as the start, create, and last update times and dates, user creating the task, and its description.
- [Console](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/#console) \- stdout, stderr, output to the console from libraries, and ClearML explicit reporting.
- [Scalars](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/#scalars) \- Metric plots.
- [Plots](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/#plots) \- Other plots and data, for example: Matplotlib, Plotly, and ClearML explicit reporting.
- [Debug samples](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/#debug-samples) \- Images, audio, video, and HTML.

You can download the task information (execution details, configuration parameters etc.) as a JSON file by clicking ![Profile button](https://clear.ml/docs/latest/icons/ico-export.svg).

## Viewing Modes [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/\#viewing-modes "Direct link to Viewing Modes")

The ClearML Web UI provides two viewing modes for task details:

- [Info panel](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/#info-panel)
- [Full screen details mode](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/#full-screen-details-view)

Both modes contain all task details. When either view is open, switch to the other mode by clicking ![Table/Full screen view](https://clear.ml/docs/latest/icons/ico-info-min.svg)
( **View in task table / full screen**), or clicking ![Bars menu](https://clear.ml/docs/latest/icons/ico-bars-menu.svg) ( **menu**) \> **View in tasks**
**table / full screen**.

### Info Panel [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/\#info-panel "Direct link to Info Panel")

The info panel keeps the task table in view so that [task actions](https://clear.ml/docs/latest/docs/webapp/webapp_exp_table#task-actions)
can be performed from the table (as well as the menu in the info panel).

![Info panel](https://clear.ml/docs/latest/assets/images/webapp_tracking_40-3609b1a01adf34e7a13961511832226e.png#light-mode-only)![Info panel](https://clear.ml/docs/latest/assets/images/webapp_tracking_40_dark-f333647114477ed86eaea994a5b95081.png#dark-mode-only)

Click ![Compressed view](https://clear.ml/docs/latest/icons/ico-compact-view.svg) to
hide details in the task table, so only the task names and statuses are displayed

![Compressed info panel](https://clear.ml/docs/latest/assets/images/webapp_tracking_41-a4f6c3d85718ae2d716ab221b01b3097.png#light-mode-only)![Compressed info panel](https://clear.ml/docs/latest/assets/images/webapp_tracking_41_dark-9da3637f2d17883d532b39a43c0cb750.png#dark-mode-only)

### Full Screen Details View [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/\#full-screen-details-view "Direct link to Full Screen Details View")

The full screen details view allows for easier viewing and working with task tracking and results. The task
table is not visible when the full screen details view is open. Perform task actions from the menu.

![Full screen view](https://clear.ml/docs/latest/assets/images/webapp_tracking_33-88be7968dda63d307955303da3aaaa83.png#light-mode-only)![Full screen view](https://clear.ml/docs/latest/assets/images/webapp_tracking_33_dark-eea393d7f4c04f61432a7074de2ae791.png#dark-mode-only)

## Execution [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/\#execution "Direct link to Execution")

A task's **EXECUTION** tab of lists the following:

- Source code
- Uncommitted changes
- Installed Python packages
- Container details
- Output details

In full-screen mode, the source code and output details are grouped in the **DETAILS** section.

### Source Code [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/\#source-code "Direct link to Source Code")

The Source Code section of a task's **EXECUTION** tab includes:

- The task's repository - Click link to open the repository at the specified revision
- Commit ID
- Script path
- Working directory
- Binary (Python executable)

![Source code section](https://clear.ml/docs/latest/assets/images/webapp_exp_source_code-3b979a9752a01debd4796a6f328ec178.png#light-mode-only)![Source code section](https://clear.ml/docs/latest/assets/images/webapp_exp_source_code_dark-ba9c0ac293af84fb76beeb5decda6d84.png#dark-mode-only)

### Uncommitted Changes [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/\#uncommitted-changes "Direct link to Uncommitted Changes")

ClearML displays the git diff of the task in the Uncommitted Changes section.

![Uncommitted changes section](https://clear.ml/docs/latest/assets/images/webapp_exp_uncommitted_changes-09a31fce93ab60183c8d243b58a3b735.png#light-mode-only)![Uncommitted changes section](https://clear.ml/docs/latest/assets/images/webapp_exp_uncommitted_changes_dark-b7c783067da74392fb387dbbdf8c5916.png#dark-mode-only)

### Python Packages [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/\#python-packages "Direct link to Python Packages")

The Python Packages section lists the task's installed Python packages and their versions.

![Python packages section](https://clear.ml/docs/latest/assets/images/webapp_exp_installed_packages-ad6649019c408839d134b1df1a0dbc12.png#light-mode-only)![Python packages section](https://clear.ml/docs/latest/assets/images/webapp_exp_installed_packages_dark-a01b05830d52f0e68113d2f353a72f2c.png#dark-mode-only)

When a ClearML agent executing a task ends up using a different set of Python packages than was originally
specified, both the original specification (`original pip` or `original conda`), and the packages the agent ended up
using to set up an environment (`pip` or `conda`) are available. Select which requirements to view in the dropdown menu.

![Packages used by agent](https://clear.ml/docs/latest/assets/images/webapp_exp_installed_packages_2-02e1a8566721ead4ea1582b68f98609c.png#light-mode-only)![Packages used by agent](https://clear.ml/docs/latest/assets/images/webapp_exp_installed_packages_2_dark-245afccccec916f33a52953263905b8e.png#dark-mode-only)

### Container [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/\#container "Direct link to Container")

The Container section list the following information:

- Image - a pre-configured container that ClearML Agent will use to remotely execute this task (see [Building Task Execution Environments in a Container](https://clear.ml/docs/latest/docs/getting_started/clearml_agent_base_docker))
- Arguments - add container arguments
- Setup shell script - a bash script to be executed inside the container before setting up the task's environment

important

To [rerun](https://clear.ml/docs/latest/docs/webapp/webapp_exp_tuning) a task through the UI in the listed container, the ClearML Agent executing the task must be running in
Docker mode:

```bash
clearml-agent daemon --queue <execution_queue_to_pull_from> --docker [optional default docker image to use]
```

For more information, see [Docker Mode](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_execution_env#docker-mode).

![Container section](https://clear.ml/docs/latest/assets/images/webapp_exp_container-47f6ff6f7aaa8c95bfad7721dc45290b.png#light-mode-only)![Container section](https://clear.ml/docs/latest/assets/images/webapp_exp_container_dark-1785e55dbcd64e3a35044fe8c937b96f.png#dark-mode-only)

### Output [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/\#output "Direct link to Output")

The Output details include:

- The output destination used for storing model checkpoints (snapshots) and artifacts (see also, [default\_output\_uri](https://clear.ml/docs/latest/docs/configs/clearml_conf#config_default_output_uri)
in the configuration file, and `output_uri` in [`Task.init`](https://clear.ml/docs/latest/docs/references/sdk/task#taskinit) parameters).

![Execution details section](https://clear.ml/docs/latest/assets/images/webapp_exp_output-276d0a67e0474d226b8ef28b4629bebf.png#light-mode-only)![Execution details section](https://clear.ml/docs/latest/assets/images/webapp_exp_output_dark-a855120653b4946ec42b9ff1f2c65d3c.png#dark-mode-only)

## Configuration [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/\#configuration "Direct link to Configuration")

All parameters and configuration objects appear in the **CONFIGURATION** tab.

### Hyperparameters [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/\#hyperparameters "Direct link to Hyperparameters")

Hyperparameters are grouped by their type and appear in **CONFIGURATION** **>** **HYPERPARAMETERS**. Once a task
is run and stored in ClearML Server, any of these hyperparameters can be [modified](https://clear.ml/docs/latest/docs/webapp/webapp_exp_tuning#modifying-tasks).

#### Command Line Arguments [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/\#command-line-arguments "Direct link to Command Line Arguments")

The **Args** group shows automatically logged argument parser parameters (e.g. `argparse`, `click`, `hydra`).
Hover over ![Description](https://clear.ml/docs/latest/icons/ico-description.svg) (menu) on a
parameter's line, and the type, description, and default value appear, if they were provided.

![Command line arguments configuration group](https://clear.ml/docs/latest/assets/images/webapp_tracking_22-2c9e34154ed2c57557a3ecdb0e66193f.png#light-mode-only)![Command line arguments configuration group](https://clear.ml/docs/latest/assets/images/webapp_tracking_22_dark-a312b68d66bfcf16526997ad015e30f0.png#dark-mode-only)

#### Environment Variables [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/\#environment-variables "Direct link to Environment Variables")

If environment variables were listed in the `CLEARML_LOG_ENVIRONMENT` environment variable or the [`sdk.development.log_os_environments`](https://clear.ml/docs/latest/docs/configs/clearml_conf#log_env_var)
field of the `clearml.conf` file, the **Environment** group displays the listed environment variables (see [this FAQ](https://clear.ml/docs/latest/docs/faq#track-env-vars)).

note

The `CLEARML_LOG_ENVIRONMENT` variable always overrides the `clearml.conf` file.

![Environment variables configuration group](https://clear.ml/docs/latest/assets/images/webapp_tracking_23-19aa3b06ae64ea9fc798f1cf761a6ec9.png#light-mode-only)![Environment variables configuration group](https://clear.ml/docs/latest/assets/images/webapp_tracking_23_dark-5a11bdc297d6605d676384f9d2fc5bca.png#dark-mode-only)

#### Custom Parameter Groups [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/\#custom-parameter-groups "Direct link to Custom Parameter Groups")

Custom parameter groups show parameter dictionaries if the parameters were connected to the Task, using
[`Task.connect()`](https://clear.ml/docs/latest/docs/references/sdk/task#connect) with a `name` argument provided. `General` is the default section
if a name is not provided.

![Custom parameters group](https://clear.ml/docs/latest/assets/images/webapp_tracking_25-17b8fe27b27f9e6a22452550c2e5e6f1.png#light-mode-only)![Custom parameters group](https://clear.ml/docs/latest/assets/images/webapp_tracking_25_dark-8a8a7ee6f2a8beb5512617680fbb452d.png#dark-mode-only)

#### TensorFlow Definitions [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/\#tensorflow-definitions "Direct link to TensorFlow Definitions")

The **TF\_DEFINE** parameter group shows automatic TensorFlow logging.

![TF_DEFINE parameter group](https://clear.ml/docs/latest/assets/images/webapp_tracking_26-6eb798de6b204a73f1babfa0cfa9dc14.png#light-mode-only)![TF_DEFINE parameter group](https://clear.ml/docs/latest/assets/images/webapp_tracking_26_dark-02ffac0c1156adca3cda093e46b58f6c.png#dark-mode-only)

### User Properties [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/\#user-properties "Direct link to User Properties")

User properties allow to store any descriptive information in a key-value pair format. They are editable in any task,
except _Published_ ones (read-only).

![User properties section](https://clear.ml/docs/latest/assets/images/webapp_tracking_21-77b6d0370d5729794b3dab581dd27081.png#light-mode-only)![User properties section](https://clear.ml/docs/latest/assets/images/webapp_tracking_21_dark-7d0e5b8450d158338eb6e6860fd489a0.png#dark-mode-only)

### Configuration Objects [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/\#configuration-objects "Direct link to Configuration Objects")

ClearML tracks a task's model configuration objects, which appear in **Configuration Objects** **>** **General**.
These objects include those that are automatically tracked, and those connected to a Task in code (see [`Task.connect_configuration`](https://clear.ml/docs/latest/docs/references/sdk/task#connect_configuration)).

![Configuration objects](https://clear.ml/docs/latest/assets/images/webapp_tracking_24-44e8a2b08f71c5e6785b13619ff9df32.png#light-mode-only)![Configuration objects](https://clear.ml/docs/latest/assets/images/webapp_tracking_24_dark-2c3d261097bd3e06d9218caed1e65683.png#dark-mode-only)

ClearML supports providing a name for a Task model configuration object (see the `name`
parameter in [`Task.connect_configuration`](https://clear.ml/docs/latest/docs/references/sdk/task#connect_configuration)).

![Custom configuration objects](https://clear.ml/docs/latest/assets/images/webapp_tracking_28-3e2d4e724d71eadee4a6ec113b5ba64f.png#light-mode-only)![Custom configuration objects](https://clear.ml/docs/latest/assets/images/webapp_tracking_28_dark-dc9d59e4ce75d1f32410be021a4cb4c7.png#dark-mode-only)

## Artifacts [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/\#artifacts "Direct link to Artifacts")

Task artifacts, including models, appear in the **ARTIFACTS** tab.

Each non-model artifact entry displays:

- File path
- File size
- Hash
- Metadata (if set)

Artifact location is displayed in the `FILE PATH` field. To access model and other artifact files:

- **Local Files**: Use the 'copy to clipboard' action (![Clipboard](https://clear.ml/docs/latest/icons/ico-copy-to-clipboard.svg))
to obtain the file path to facilitate local storage access since web applications are prohibited from accessing the local disk for security reasons.
- **Remote Files** (e.g. network-hosted artifacts with `https://`, `s3://`, etc. URIs): Use the download action (![Download](https://clear.ml/docs/latest/icons/ico-download-json.svg))
to retrieve the file.

![Other artifacts section](https://clear.ml/docs/latest/assets/images/webapp_tracking_30-768137fdcb284d1b88464da5d487e2db.png#light-mode-only)![Other artifacts section](https://clear.ml/docs/latest/assets/images/webapp_tracking_30_dark-6173f2824ef1c8269535afd7ca3c291a.png#dark-mode-only)

### Models [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/\#models "Direct link to Models")

The task's input and output models appear in the **ARTIFACTS** tab. Each model entry shows:

- Model name
- ID
- Configuration.

Input models also display their creating task, which on-click navigates you to the task's page.

![Models in Artifacts tab](https://clear.ml/docs/latest/assets/images/webapp_exp_artifacts_01-bff3c9a27c1ad89d820c141cb1c49bb8.png#light-mode-only)![Models in Artifacts tab](https://clear.ml/docs/latest/assets/images/webapp_exp_artifacts_01_dark-ddffb0ddc11ca3ec570833c939f271d8.png#dark-mode-only)

To view more model details, including design, label enumeration, and general information, click the model name
to navigate to its page in the **MODELS** tab (see [Model Details](https://clear.ml/docs/latest/docs/webapp/webapp_model_viewing)).

## Info [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/\#info "Direct link to Info")

The **INFO** tab shows extended task information:

- [Latest task events log](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/#latest-events-log)
- [Task description](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/#description)
- [Task details](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/#task-details)

### Latest Events Log [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/\#latest-events-log "Direct link to Latest Events Log")

Hosted Service and Enterprise Feature

The latest events log is available only on the ClearML Hosted Service and under the ClearML Enterprise plan.

The **INFO** tab includes a detailed history of task activity:

- Task action (e.g. status changes, project move, etc.)
- Action time
- Acting user
- Action source (i.e. ClearML Agent, SDK, or UI)
- Action source version

To download the task history as a CSV file, hover over the log and click ![Download](https://clear.ml/docs/latest/icons/ico-download.svg).

![Task audit log](https://clear.ml/docs/latest/assets/images/webapp_info_audit_log-1aacc2c51e2615ec8c1a68a0418ced0b.png#light-mode-only)![Task audit log](https://clear.ml/docs/latest/assets/images/webapp_info_audit_log_dark-390a53c19ac3e5fcb8262bb43964fbeb.png#dark-mode-only)

Limited persistency

ClearML maintains a system-wide, large but strict limit for task history items. Once the limit is reached, the oldest entries are purged to make room for fresh entries.

### Description [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/\#description "Direct link to Description")

Add descriptive text to the task in the **Description** section. To modify the description, hover over the
description box and click **Edit**.

### Task Details [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/\#task-details "Direct link to Task Details")

The **Task Details** section lists information describing the task:

- The parent task
- Project name
- Creation, start, and last update dates and times
- User who created the task
- Task state (status)
- Whether the task is archived
- Runtime properties - Information about the machine running the task:
  - Operating system
  - CUDA driver version
  - Number of CPU cores
  - Number of GPUs
  - CPU / GPU type
  - Memory size
  - Host name
  - Processor
  - Python version
- Task Progress

![Info tab](https://clear.ml/docs/latest/assets/images/webapp_tracking_31-3d0c0572c42a93351e9924f137e9507f.png#light-mode-only)![Info tab](https://clear.ml/docs/latest/assets/images/webapp_tracking_31_dark-bd613d34a897de9457ea241e09e91836.png#dark-mode-only)

## Task Results [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/\#task-results "Direct link to Task Results")

Embedding ClearML Visualization

You can embed task plots and debug samples into ClearML [Reports](https://clear.ml/docs/latest/docs/webapp/webapp_reports). These visualizations are
updated live as the task(s) updates. The Enterprise Plan and Hosted Service support embedding resources in external
tools (e.g. Notion). See [Plot Controls](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/#plot-controls).

### Console [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/\#console "Direct link to Console")

The complete task log containing everything printed to stdout and stderr appears in the **CONSOLE** tab. The full log
is downloadable. To view the end of the log, click **Jump to end**.

![Console tab](https://clear.ml/docs/latest/assets/images/webapp_tracking_32-5f124a23edb4accb3ab4eb5567dfaf6a.png#light-mode-only)![Console tab](https://clear.ml/docs/latest/assets/images/webapp_tracking_32_dark-c5769dcbf1d032fa1a0233c84af40427.png#dark-mode-only)

### Scalars [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/\#scalars "Direct link to Scalars")

All scalars that ClearML automatically logs, as well as those explicitly reported in code, appear in
**SCALARS**.

Scalar series can be displayed in [graph view](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/#graph-view) (default) or in [metric values view](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/#metric-values-view):

#### Graph View [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/\#graph-view "Direct link to Graph View")

Scalar graph view (![Graph view](https://clear.ml/docs/latest/icons/ico-charts-view.svg))
shows scalar series plotted as a time series line chart. By default, a single plot is shown for each scalar metric,
with all variants overlaid within.

The series are subsampled for
display efficiency. For high resolution, view a series in full screen mode by hovering over the graph and clicking ![Maximize plot icon](https://clear.ml/docs/latest/icons/ico-maximize.svg).

Full Screen Refresh

Scalar graphs in full screen mode do not auto-refresh. Click ![Refresh](https://clear.ml/docs/latest/icons/ico-reset.svg)
to update the graph.

Single value scalars (see [`Logger.report_single_value`](https://clear.ml/docs/latest/docs/references/sdk/logger#report_single_value)) are shown in
a `Summary` table.

![Single value scalar plot](https://clear.ml/docs/latest/assets/images/webapp_single_scalar_plot-49f4806c76ba62aad0d5d9ddddb11232.png#light-mode-only)![Single value scalar plot](https://clear.ml/docs/latest/assets/images/webapp_single_scalar_plot_dark-398a2bbf229d31b303cd57cde22ca7ed.png#dark-mode-only)

##### Scalar Plot Tools [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/\#scalar-plot-tools "Direct link to Scalar Plot Tools")

Use the scalar tools to improve analysis of scalar metrics. In the info panel, click ![Tuning](https://clear.ml/docs/latest/icons/ico-tune.svg) to access the tools. In the full-screen details view, the tools
are on the left side of the window. The tools include:

- **Group by** \- Select one of the following:
  - **Metric** \- Displays all variants for a metric on the same plot. For example, if you have a "Test" metric with
    "loss" and "accuracy" variants, both variants will appear on the same plot that is titled "Test".

    ![Plots grouped by metric](https://clear.ml/docs/latest/assets/images/webapp_tracking_33-88be7968dda63d307955303da3aaaa83.png#light-mode-only)![Plots grouped by metric](https://clear.ml/docs/latest/assets/images/webapp_tracking_33_dark-eea393d7f4c04f61432a7074de2ae791.png#dark-mode-only)

  - **None** \- Displays individual plots for each metric-variant combination, grouped into sections by metric. For
    example, a "Test" metric with "loss" and "accuracy" variants will have a separate plot for each variant under the
    "Test" group.

    ![Plots groups my metric and variant](https://clear.ml/docs/latest/assets/images/webapp_tracking_34-99a25857d423475e11204da6d9090449.png#light-mode-only)![Plots groups my metric and variant](https://clear.ml/docs/latest/assets/images/webapp_tracking_34_dark-509d59d540ac9fb3a4adc4b41c2ba6e9.png#dark-mode-only)
- Horizontal axis - Select the x-axis units:
  - Iterations
  - Time from start - Time since task began
  - Wall time - Local clock time
- Curve smoothing - Choose which smoothing algorithm to use from the dropdown menu: Exponential moving average, Gaussian,
or Running Average. Use the sliders to configure smoothing factors or specify a value manually. Use the `Show Originals`
toggle control to show both original and smoothed plots, or smoothed plots only.

- Show / hide plots - Click ![Eye Show](https://clear.ml/docs/latest/icons/ico-show.svg) to control which
plots to display. For example, to display specific plots, click **HIDE ALL**, and then click ![Eye Show](https://clear.ml/docs/latest/icons/ico-show.svg)
on each plot you want to view.


Default scalar display

After adjusting the scalar display (e.g. grouping, axis, smoothing), click **Set as default** to save the current
configuration as the default view for the project’s task and model scalars.

See additional [plot controls](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/#plot-controls) below.

##### Embedding Plots [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/\#embedding-plots "Direct link to Embedding Plots")

To embed scalar plots in your [Reports](https://clear.ml/docs/latest/docs/webapp/webapp_reports), hover over a plot and click Embed ![Embed code](https://clear.ml/docs/latest/icons/ico-plotly-embed-code.svg),
which will copy to clipboard the embed code to put in your Reports. To quickly get the embed codes for all plots of a
specific metric, click Embed ![Embed code](https://clear.ml/docs/latest/icons/ico-plotly-embed-code.svg)
on the group section header (available when plots are [grouped by](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/#group_by)`None`).

![Embed metric group](https://clear.ml/docs/latest/assets/images/webapp_tracking_34b-ed382213ff42780eaa3fb1b1eb383c29.png#light-mode-only)![Embed metric group](https://clear.ml/docs/latest/assets/images/webapp_tracking_34b_dark-182b1bf1c9a41c8b8706d95f6e76e17b.png#dark-mode-only)

In contrast to static screenshots, embedded resources
are retrieved when the report is displayed allowing your reports to show the latest up-to-date data.

#### Metric Values View [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/\#metric-values-view "Direct link to Metric Values View")

The metric values view (![Table view](https://clear.ml/docs/latest/icons/ico-table-view.svg))
shows a table summary of your metrics with a row per metric/variant:

- First - The metric/variant series' initial value
- Last - The metric/variant series' last value
- Min - The metric/variant series' minimum value
- Max - The metric/variant series' maximum value
- Mean - The metric/variant series' mean value

If all the values of a specific metric/variant are the same, the row will display a ![Same values](https://clear.ml/docs/latest/icons/ico-equal-outline.svg) sign.

![Plots tab](https://clear.ml/docs/latest/assets/images/webapp_tracking_34a-225e5626e40241d438fb40fa0b95c552.png#light-mode-only)![Plots tab](https://clear.ml/docs/latest/assets/images/webapp_tracking_34a_dark-6f6caee7155a75068c0b55910773b3df.png#dark-mode-only)

#### Select Metrics and Variants to View [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/\#select-metrics-and-variants-to-view "Direct link to Select Metrics and Variants to View")

Choose which metrics to view using one of the following options:

- Quick filter bar (![Magnifying glass](https://clear.ml/docs/latest/icons/ico-search.svg)) \- Show
metrics/variants whose name fit a partial-string match
- Filter menu (![Eye Show](https://clear.ml/docs/latest/icons/ico-show.svg) in Graph View, ![Filter](https://clear.ml/docs/latest/icons/ico-filter-off.svg) in Metric
Values View) - Select which metrics to view by clicking their show/hide button (![Eye Show](https://clear.ml/docs/latest/icons/ico-show.svg)).
Click **Hide/Show all** to quickly hide/show all metrics (when the selection is focused through search, the Hide/Show action applies to the matching metrics only).

### Plots [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/\#plots "Direct link to Plots")

Non-time-series plots appear in **PLOTS**. These include data generated by libraries, visualization tools, and
explicitly reported using the ClearML Logger. These may include 2D and 3D plots, tables (Pandas and CSV files), and
Plotly plots. Individual plots can be shown / hidden or filtered by title.

![Plots tab](https://clear.ml/docs/latest/assets/images/webapp_tracking_35-13d7c291a697fa16002d4ce2d440fcef.png#light-mode-only)![Plots tab](https://clear.ml/docs/latest/assets/images/webapp_tracking_35_dark-b2f7459fa084113574210d171aab7960.png#dark-mode-only)

Plots are grouped into sections by metric. To quickly get the embed codes for all plots of a specific metric, click Embed ![Embed code](https://clear.ml/docs/latest/icons/ico-plotly-embed-code.svg)
on the group section header.

For each metric/variant combination, the latest reported plot is displayed.

When viewing a plot in full screen (![Maximize plot icon](https://clear.ml/docs/latest/icons/ico-maximize.svg)),
older iterations are available through the iteration slider (or using the up/down arrow keyboard shortcut). Go to the
previous/next plot in the current iteration using the ![Previous](https://clear.ml/docs/latest/icons/ico-previous.svg) / ![Next](https://clear.ml/docs/latest/icons/ico-next.svg)
buttons (or using the left/right arrow keyboard shortcut).

![Plots maximize tab](https://clear.ml/docs/latest/assets/images/webapp_tracking_35a-95ab7f03ba5afb37a9b71a22c4f8f003.png#light-mode-only)![Plots maximize tab](https://clear.ml/docs/latest/assets/images/webapp_tracking_35a_dark-2d42debfdc2d0d462058567f1e3acaab.png#dark-mode-only)

Choose which plots to display using the following options:

- Quick filter bar (![Magnifying glass](https://clear.ml/docs/latest/icons/ico-search.svg)) \- Show
metrics/variants whose name fit a partial-string match
- Filter menu - Select which metrics to view by clicking their show/hide button (![Eye Show](https://clear.ml/docs/latest/icons/ico-show.svg)).
Click **Hide/Show all** to quickly hide/show all metrics (when the selection is focused through search, the Hide/Show
action applies to the matching metrics only).

#### Plot Controls [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/\#plot-controls "Direct link to Plot Controls")

The table below lists the plot controls which may be available for any plot (in the **SCALARS** and **PLOTS** tabs).
These controls allow you to better analyze the results. Hover over a plot, and the controls appear.

| Icon | Description |
| --- | --- |
| ![Download PNG icon](https://clear.ml/docs/latest/icons/ico-download-pic.svg) | Download plots as PNG files. |
| ![Pan icon](https://clear.ml/docs/latest/icons/ico-pan.svg) | Pan around plot. Click ![Pan icon](https://clear.ml/docs/latest/icons/ico-pan.svg), click the plot, and then drag. |
| ![Dotted box icon](https://clear.ml/docs/latest/icons/ico-dotted-box.svg) | To examine an area, draw a dotted box around it. Click ![Dotted box icon](https://clear.ml/docs/latest/icons/ico-dotted-box.svg) and then drag. |
| ![Dotted lasso icon](https://clear.ml/docs/latest/icons/ico-dotted-lasso.svg) | To examine an area, draw a dotted lasso around it. Click ![Dotted lasso icon](https://clear.ml/docs/latest/icons/ico-dotted-lasso.svg) and then drag. |
| ![Zoom icon](https://clear.ml/docs/latest/icons/ico-zoom.svg) | Zoom into a section of a plot. Zoom in - Click ![Zoom icon](https://clear.ml/docs/latest/icons/ico-zoom.svg) and drag over a section of the plot. Reset to original scale - Click ![Reset autoscale icon](https://clear.ml/docs/latest/icons/ico-reset-autoscale.svg). |
| ![Zoom-in icon](https://clear.ml/docs/latest/icons/ico-zoom-in-square.svg) | Zoom in. |
| ![Zoom-out icon](https://clear.ml/docs/latest/icons/ico-zoom-out-square.svg) | Zoom out. |
| ![Reset autoscale icon](https://clear.ml/docs/latest/icons/ico-reset-autoscale.svg) | Reset to autoscale after zooming (![Zoom icon](https://clear.ml/docs/latest/icons/ico-zoom.svg), ![Zoom-in icon](https://clear.ml/docs/latest/icons/ico-zoom-in-square.svg), or ![Zoom-out icon](https://clear.ml/docs/latest/icons/ico-zoom-out-square.svg)). |
| ![Reset axes icon](https://clear.ml/docs/latest/icons/ico-reset-axes.svg) | Reset axes after a zoom. |
| ![Spike lines icon](https://clear.ml/docs/latest/icons/ico-spike-lines.svg) | Show / hide spike lines. |
| ![Show closest icon](https://clear.ml/docs/latest/icons/ico-show-closest.svg)<br>![Compare data icon](https://clear.ml/docs/latest/icons/ico-compare-data.svg)<br>![X-united mode](https://clear.ml/docs/latest/icons/ico-x-unified.svg) | Set data hover mode:<br>- ![Show closest icon](https://clear.ml/docs/latest/icons/ico-show-closest.svg) Closest - Show the (X, Y) data point closest to the cursor, including horizontal and vertical axes values<br>- ![Compare data icon](https://clear.ml/docs/latest/icons/ico-compare-data.svg) X - Show labels for points with the same x value as the cursor <br>- ![X-united mode](https://clear.ml/docs/latest/icons/ico-x-unified.svg) X unified - Show a single label for the points with the same x value as the cursor |
| ![Logarithmic view icon](https://clear.ml/docs/latest/icons/ico-logarithmic-view.svg) | Switch to logarithmic view. |
| ![Graph legend icon](https://clear.ml/docs/latest/icons/ico-graph-legend.svg) | Hide / show the legend. |
| ![Plot layout setting](https://clear.ml/docs/latest/icons/ico-reset_1.svg) | Switch between original and auto-fitted plot dimensions. The original layout is the plot's user-defined dimensions. |
| ![Download JSON icon](https://clear.ml/docs/latest/icons/ico-download-json-plot.svg) | Download plot data as a JSON file. |
| ![Download CSV icon](https://clear.ml/docs/latest/icons/ico-download-csv.svg) | Download **table** plot data as a CSV file. |
| ![Maximize plot icon](https://clear.ml/docs/latest/icons/ico-maximize.svg) | Expand plot to entire window. When used with scalar graphs, full screen mode displays plots with all data points, as opposed to an averaged plot |
| ![Refresh](https://clear.ml/docs/latest/icons/ico-reset.svg) | Refresh scalar graphs in full screen mode to update it. |
| ![Embed code](https://clear.ml/docs/latest/icons/ico-plotly-embed-code.svg) | Copy to clipboard the resource embed code. This opens the following options: <br>- **Embed in External tool** (available in the ClearML Enterprise plan and Hosted Service) - Copy code to add to third-party platforms that support embedded content (e.g. Notion). <br>- **Embed in ClearML report** \- Copy code to add to a [report](https://clear.ml/docs/latest/docs/webapp/webapp_reports)<br> In contrast to static screenshots, embedded resources are retrieved when the tool/report is displayed allowing your tools/reports to show the latest up-to-date data. |

#### 3D Plot Controls [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/\#3d-plot-controls "Direct link to 3D Plot Controls")

| Icon | Description |
| --- | --- |
| ![Orbital rotation mode icon](https://clear.ml/docs/latest/icons/ico-orbital-rotation.svg) | Switch to orbital rotation mode - rotate the plot around its middle point. |
| ![Turntable rotation mode icon](https://clear.ml/docs/latest/icons/ico-turntable-rotation.svg) | Switch to turntable rotation mode - rotate the plot around its middle point while constraining one axis |
| ![reset axes icon](https://clear.ml/docs/latest/icons/ico-reset-axes.svg) | Reset axes to default position. |

### Debug Samples [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/\#debug-samples "Direct link to Debug Samples")

Task outputs such as images, audio, and videos appear in **DEBUG SAMPLES**. These include data generated by
libraries and visualization tools, and explicitly reported using the [ClearML Logger](https://clear.ml/docs/latest/docs/fundamentals/logger).

You can view debug samples by metric in the reported iterations. Filter the samples by metric by selecting a metric from the
dropdown menu above the samples. The most recent iteration appears first.

![Debug Samples tab](https://clear.ml/docs/latest/assets/images/webapp_tracking_43-e34d713ae3ffe8201b35e062e51e4242.png#light-mode-only)![Debug Samples tab](https://clear.ml/docs/latest/assets/images/webapp_tracking_43_dark-ffb10543c2b4f657aa6ef36e5db255e3.png#dark-mode-only)

For each metric, the latest reported debug sample is displayed.

Click a sample to view it in full screen. If the sample is video or audio, the full screen mode includes a player.

When viewing a sample in full screen, older iterations are available through the iteration slider (or using the up/down
arrow keyboard shortcut). Go to the previous/next sample in the current iteration using the ![Previous](https://clear.ml/docs/latest/icons/ico-previous.svg) / ![Next](https://clear.ml/docs/latest/icons/ico-next.svg)
buttons (or using the left/right arrow keyboard shortcut).

![Debug Samples image viewer](https://clear.ml/docs/latest/assets/images/webapp_tracking_44-345319f66443cc781cb27ab4b4a84d8c.png#light-mode-only)![Debug Samples image viewer](https://clear.ml/docs/latest/assets/images/webapp_tracking_44_dark-6055821ebc292a69dfccb131d3287fad.png#dark-mode-only)

## Tagging Tasks [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/\#tagging-tasks "Direct link to Tagging Tasks")

Tags can do more than you think! -- 🧠 WISDOM NUGGET - YouTube

Tap to unmute

[Tags can do more than you think! -- 🧠 WISDOM NUGGET](https://www.youtube.com/watch?v=uqik38jlBsQ) [ClearML](https://www.youtube.com/channel/UCDYdA4hjckRLRVBrCoKenCQ)

![thumbnail-image](https://yt3.ggpht.com/ytc/AIdro_kEljxxvNzLP5hB1Bv03O_F-CooCUhLk76T2A-B2sM9_w=s68-c-k-c0x00ffffff-no-rj)

ClearML2.62K subscribers

Tags are user-defined, color-coded labels that can be added to tasks (and pipelines, datasets, and models),
allowing to easily identify and group tasks. Tags can help in organizing, querying, and automating tasks.
For example, tag tasks by the machine type used to execute them, label versions, team names, or any other
category.

You can use tags to filter the tasks in your task table (see [Filtering Columns](https://clear.ml/docs/latest/docs/webapp/webapp_exp_table#filtering-columns))
or when querying tasks in your code (see [Tag Filters](https://clear.ml/docs/latest/docs/clearml_sdk/task_sdk#tag-filters)). You can trigger
task execution according to their tags (see [TriggerScheduler](https://clear.ml/docs/latest/docs/references/sdk/trigger)) or automatically
deploy models according to their tags (see [ClearML Serving](https://clear.ml/docs/latest/docs/clearml_serving/clearml_serving_extra#automatic-model-deployment)).

**To add tags:**

1. Click the task **>** Hover over the tag area **>** **+ADD TAG** or ![Bars menu](https://clear.ml/docs/latest/icons/ico-bars-menu.svg) (menu)
2. Do one of the following:
   - Add a new tag - Type the new tag name **>** **(Create New)**.
   - Add an existing tag - Click a tag.
   - Customize a tag's colors - Click **Tag Colors** **>** Click the tag icon **>** **Background** or **Foreground** **>** Pick a color **>** **OK** **>** **CLOSE**.

**To remove a tag** \- Hover over the tag and click **X**.

## Locating the Task ID [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/\#locating-the-task-id "Direct link to Locating the Task ID")

The task ID appears in the task page's header.

- [Viewing Modes](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/#viewing-modes)
  - [Info Panel](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/#info-panel)
  - [Full Screen Details View](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/#full-screen-details-view)
- [Execution](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/#execution)
  - [Source Code](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/#source-code)
  - [Uncommitted Changes](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/#uncommitted-changes)
  - [Python Packages](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/#python-packages)
  - [Container](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/#container)
  - [Output](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/#output)
- [Configuration](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/#configuration)
  - [Hyperparameters](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/#hyperparameters)
  - [User Properties](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/#user-properties)
  - [Configuration Objects](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/#configuration-objects)
- [Artifacts](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/#artifacts)
  - [Models](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/#models)
- [Info](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/#info)
  - [Latest Events Log](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/#latest-events-log)
  - [Description](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/#description)
  - [Task Details](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/#task-details)
- [Task Results](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/#task-results)
  - [Console](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/#console)
  - [Scalars](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/#scalars)
  - [Plots](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/#plots)
  - [Debug Samples](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/#debug-samples)
- [Tagging Tasks](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/#tagging-tasks)
- [Locating the Task ID](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual/#locating-the-task-id)