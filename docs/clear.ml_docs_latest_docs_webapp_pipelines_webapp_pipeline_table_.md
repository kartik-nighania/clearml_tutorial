---
url: "https://clear.ml/docs/latest/docs/webapp/pipelines/webapp_pipeline_table/"
title: "The Pipeline Run Table | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/webapp/pipelines/webapp_pipeline_table/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The pipeline runs table is a [customizable](https://clear.ml/docs/latest/docs/webapp/pipelines/webapp_pipeline_table/#customizing-the-runs-table) list of the pipeline's runs. Use it to
view a run's details, and manage runs (create, continue, or abort). The runs table's auto-refresh allows users
to continually monitor run progress.

View the runs table in table view ![Table view](https://clear.ml/docs/latest/icons/ico-table-view.svg),
details view ![Details view](https://clear.ml/docs/latest/icons/ico-split-view.svg),
or comparison view ![Comparison view](https://clear.ml/docs/latest/icons/ico-charts-view.svg)
using the buttons on the top left of the page. Use the details view to access a selected run's details, while keeping
the run list in view. Details view can also be accessed by double-clicking a specific pipeline run in the table view to
open its details view. Use the [comparison view](https://clear.ml/docs/latest/docs/webapp/pipelines/webapp_pipeline_table/#comparing-runs) to compare your pipeline run's scalar and plot results.
This view compares the scalars/plots of currently selected pipeline runs. If no runs are selected, the first 100 visible
runs in the table are compared.

Use the search bar ![Magnifying glass](https://clear.ml/docs/latest/icons/ico-search.svg)
to find specific pipeline runs. You can query by the run name, ID, and description.
To search using regex, click the `.*` icon on the search bar.

You can archive pipeline runs so the runs table doesn't get too cluttered. Click **OPEN ARCHIVE** on the top of the
table to open the archive and view all archived runs. From the archive, you can restore
runs to remove them from the archive. You can also permanently delete runs.

You can download the pipeline runs table as a CSV file by clicking ![Download](https://clear.ml/docs/latest/icons/ico-download.svg)
and choosing one of these options:

- **Download onscreen items** \- Download the values for pipeline runs currently visible on screen
- **Download all items** \- Download the values for all runs in this pipeline that match the current active filters

The downloaded data consists of the currently displayed table columns.

![Pipeline runs table](https://clear.ml/docs/latest/assets/images/webapp_pipeline_runs_table-461c78f329502d230afe7139791114ac.png#light-mode-only)![Pipeline runs table](https://clear.ml/docs/latest/assets/images/webapp_pipeline_runs_table_dark-0870f1f303943c3684f615e1e8c386c1.png#dark-mode-only)

## Run Table Columns [​](https://clear.ml/docs/latest/docs/webapp/pipelines/webapp_pipeline_table/\#run-table-columns "Direct link to Run Table Columns")

The pipeline run table contains the following columns:

| Column | Description | Type |
| --- | --- | --- |
| **RUN** | Pipeline run identifier | String |
| **VERSION** | The pipeline version number. Corresponds to the [PipelineController](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller#class-pipelinecontroller)'s and [PipelineDecorator](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinedecorator#class-automationcontrollerpipelinedecorator)'s `version` parameter | Version string |
| **TAGS** | Descriptive, user-defined, color-coded tags assigned to run. | Tag |
| **STATUS** | Pipeline run's status. See a list of the [task states and state transitions](https://clear.ml/docs/latest/docs/fundamentals/task#task-states). For Running, Failed, and Aborted runs, you will also see a progress indicator next to the status. See [here](https://clear.ml/docs/latest/docs/pipelines/#tracking-pipeline-progress). | String |
| **USER** | User who created the run. | String |
| **STARTED** | Elapsed time since the run started. To view the date and time of start, hover over the elapsed time. | Date-time |
| **UPDATED** | Elapsed time since the last update to the run. To view the date and time of update, hover over the elapsed time. | Date-time |
| **RUN TIME** | The current / total running time of the run. | Time |
| **_Metrics_** | Add metrics column (last, minimum, and/or maximum values). Available options depend upon the runs in the table. | Varies according to runs in table |
| **_Hyperparameters_** | Add hyperparameters. Available options depend upon the runs in the table. | Varies according to runs in table |

## Customizing the Runs Table [​](https://clear.ml/docs/latest/docs/webapp/pipelines/webapp_pipeline_table/\#customizing-the-runs-table "Direct link to Customizing the Runs Table")

Customize the table using any of the following:

- Dynamic column ordering - Drag a column title to a different position.
- Show / hide columns - Click ![Setting Gear](https://clear.ml/docs/latest/icons/ico-settings.svg)
to view and select columns to show. Click **Metric** and **Hyperparameter** to add the respective custom columns
- [Filter columns](https://clear.ml/docs/latest/docs/webapp/pipelines/webapp_pipeline_table/#filtering-columns)
- Sort columns
- Resize columns - Drag the column separator to change the width of that column. Double-click the column separator for
automatic fit.

Changes are persistent (cached in the browser) and represented in the URL, so customized settings can be saved in a
browser bookmark and shared with other ClearML users.

Float Values Display

By default, the runs table displays rounded up float values. Hover over a float to view its precise value in the
tooltip that appears. To view all precise values in a column, hover over a float and click ![Expand](https://clear.ml/docs/latest/icons/ico-line-expand.svg).

### Filtering Columns [​](https://clear.ml/docs/latest/docs/webapp/pipelines/webapp_pipeline_table/\#filtering-columns "Direct link to Filtering Columns")

Filters can be applied by clicking ![Filter](https://clear.ml/docs/latest/icons/ico-filter-off.svg)
on a column, and the relevant filter appears.

There are a few types of filters:

- Value set - Choose which values to include from a list of all values in the column
- Numerical ranges - Insert minimum and/or maximum value
- Date ranges - Insert starting and/or ending date and time
- Tags - Choose which tags to filter by from a list of all tags used in the column.
  - Filter by multiple tag values using the **ANY** or **ALL** options, which correspond to the logical "AND" and "OR" respectively. These
    options appear on the top of the tag list.
  - Filter by the absence of a tag (logical "NOT") by clicking its checkbox twice. An `X` will appear in the tag's checkbox.

Once a filter is applied to a column, its filter icon will appear with a highlighted dot on its top right (![Filter on](https://clear.ml/docs/latest/icons/ico-filter-on.svg)).

To clear all active filters, click ![Clear filters](https://clear.ml/docs/latest/icons/ico-filter-reset.svg)
in the top right corner of the table.

note

The following table customizations are saved on a per-pipeline basis:

- Columns order
- Column width
- Active sort order
- Active filters
- Custom columns

## Create Run [​](https://clear.ml/docs/latest/docs/webapp/pipelines/webapp_pipeline_table/\#create-run "Direct link to Create Run")

To launch a new run for a pipeline, click **\+ NEW RUN** on the top left of the page. This opens a **NEW RUN** modal, where
you can set the run's parameters. By default, the fields are pre-filled with the last run's values.

Click **Advanced configurations** to change the run's execution queue.

![New run modal](https://clear.ml/docs/latest/assets/images/webapp_pipeline_new_run-996192c9ffcefa790849c70f87a83a1e.png#light-mode-only)![New run modal](https://clear.ml/docs/latest/assets/images/webapp_pipeline_new_run_dark-95545c517b7c808cf1618459fee46073.png#dark-mode-only)

After clicking **RUN**, the new pipeline run is enqueued in the specified queue, and the run is added to the pipeline run table.

### Create New Pipeline [​](https://clear.ml/docs/latest/docs/webapp/pipelines/webapp_pipeline_table/\#create-new-pipeline "Direct link to Create New Pipeline")

You can select to create a run in a new pipeline. This is useful, for example, when you want to use an existing pipeline
run as a starting point but develop it as a separate pipeline.

Click the dropdown arrow next to **\+ NEW RUN** and select **Run in New Pipeline**. This opens a modal where you define the new pipeline:

- Pipeline's name - Name of the new pipeline.
- Initial version - The version number for the new run
- Project - ClearML project where the new pipeline will be stored. By default, this is the same project as the original pipeline.
- Parameters – If the pipeline includes custom parameters, specify their values. The cloned run's values are pre-filled.
- Configuration
  - Pipeline controller queue - Queue to which the pipeline run will be enqueued (make sure an agent is assigned to that queue).

![New pipeline modal](https://clear.ml/docs/latest/assets/images/webapp_pipeline_clone-a3a18e1e5734ac876dd3ae7a7232bad5.png#light-mode-only)![New pipeline modal](https://clear.ml/docs/latest/assets/images/webapp_pipeline_clone_dark-fb26e76640218f082a0c7a4c5035ac5f.png#dark-mode-only)

## Run Actions [​](https://clear.ml/docs/latest/docs/webapp/pipelines/webapp_pipeline_table/\#run-actions "Direct link to Run Actions")

The following table describes the actions that can be performed from the run table, including the [states](https://clear.ml/docs/latest/docs/fundamentals/task#task-states)
that allow each operation.

Access these actions with the context menu in any of the following ways:

- In the pipeline runs table, right-click a run, or hover over a pipeline and click ![Dot menu](https://clear.ml/docs/latest/icons/ico-dots-v-menu.svg)
- In a pipeline info panel, click the menu button ![Bar menu](https://clear.ml/docs/latest/icons/ico-bars-menu.svg)

| Action | Description | States Valid for the Action | State Transition |
| --- | --- | --- | --- |
| Details | View pipeline details. Can also be accessed by double-clicking a run in the pipeline runs table. | Any state | None |
| Run | Create a pipeline run. Configure and enqueue it for execution. See [Create Run](https://clear.ml/docs/latest/docs/webapp/pipelines/webapp_pipeline_table/#create-run). | Any State | _Pending_ |
| Run in New Pipeline | Create a run in a new pipeline based on the selected run's configuration. See [Create New Pipeline](https://clear.ml/docs/latest/docs/webapp/pipelines/webapp_pipeline_table/#create-new-pipeline). | Any State | _Pending_ |
| Abort | Manually stop / cancel a run. | _Running_ / _Pending_ | _Aborted_ |
| Continue | Rerun with the same parameters. | _Aborted_ | _Pending_ |
| Add Tag | User-defined labels added to runs for grouping and organization. | Any state | None |
| Archive | Move pipeline run to the pipeline's archive. | Any state | _Pending_ to _Draft_ |
| Restore | Action available in the archive. Restore a run to the active pipeline runs table. | Any state | None |
| Delete | Action available in the archive. Delete a run and its steps, which will also remove all their logs, results, artifacts and debug samples | Any State | N/A |
| Export | Export pipeline run information (step execution details, configuration parameters etc.) as a JSON file. | Any State | None |

![pipeline run context menu](https://clear.ml/docs/latest/assets/images/webapp_pipelines_context_menu-e7e3add19244bc8662ef41ab77dc78f7.png#light-mode-only)![pipeline run context menu](https://clear.ml/docs/latest/assets/images/webapp_pipelines_context_menu_dark-cf236d27eb2f186de80f45fec07643de.png#dark-mode-only)

Most of the actions mentioned in the chart above can be performed on multiple runs at once.
[Select multiple runs](https://clear.ml/docs/latest/docs/webapp/pipelines/webapp_pipeline_table/#selecting-multiple-runs), then use either the context menu, or the bar that appears at the bottom
of the page, to perform operations on the selected runs. Actions can be performed only on the runs that match the action criteria
(for example, only _Aborted_ pipeline runs can be continued). The context menu shows the number of runs that can be
affected by each action. The same information can be found in the bottom menu, in a tooltip that appears when hovering
over an action icon.

## Selecting Multiple Runs [​](https://clear.ml/docs/latest/docs/webapp/pipelines/webapp_pipeline_table/\#selecting-multiple-runs "Direct link to Selecting Multiple Runs")

Select multiple runs by clicking the checkbox on the left of each relevant run. Clear any existing selection
by clicking the checkbox in the top left corner of the table.

Click the checkbox in the top left corner of the table to select all items currently visible.

An extended bulk selection tool is available through the down arrow next to the checkbox in the top left corner, enabling
selecting items beyond the items currently on-screen:

- **All** \- Select all runs in the pipeline
- **None** \- Clear selection
- **Filtered** \- Select all runs in the project that match the current active table filters

## Comparing Runs [​](https://clear.ml/docs/latest/docs/webapp/pipelines/webapp_pipeline_table/\#comparing-runs "Direct link to Comparing Runs")

The comparison view compares pipeline run scalar and plot results. When selected, the view presents a comparison of all
[selected runs](https://clear.ml/docs/latest/docs/webapp/pipelines/webapp_pipeline_table/#selecting-multiple-runs). If no runs are selected, the first 100 visible runs in the table are compared.

In the dropdown menu, select to view **Scalars** or **Plots**.

**Scalars** shows pipeline run scalar results as time series line graphs.

![Scalar line graphs](https://clear.ml/docs/latest/assets/images/pipelines_comparison_scalars-ba3f543c7143259934f7ae93298e15a4.png#light-mode-only)![Scalar line graphs](https://clear.ml/docs/latest/assets/images/pipelines_comparison_scalars_dark-78a2a05a2525ccabf040769e1abebcba.png#dark-mode-only)

All single value scalars are plotted into a single clustered bar chart under the "Summary" title, where each cluster
represents a reported metric, and each bar in the cluster represents a task.

![Single scalar comparison](https://clear.ml/docs/latest/assets/images/pipelines_comparison_single_scalar-da0701428f0e76bd51f5231f96ec3f02.png#light-mode-only)![Single scalar comparison](https://clear.ml/docs/latest/assets/images/pipelines_comparison_single_scalar_dark-3428ef96549f8887e3e083a31fa747f3.png#dark-mode-only)

Click ![Setting Gear](https://clear.ml/docs/latest/icons/ico-settings.svg) to customize which
metrics to view.

In the **Scalars** view, click ![Tuning](https://clear.ml/docs/latest/icons/ico-tune.svg) to access [scalar plot tools](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual#scalar-plot-tools).

**Plots** shows the last reported iteration sample of each metric/variant combination per compared run.

Line, scatter, box, and bar graphs are compared by overlaying each metric/variant from all compared runs' into a single
comparative plot.

![Merged plots](https://clear.ml/docs/latest/assets/images/pipelines_comparison_plots_merged-b9a652c56003b9c6e871853649e34838.png#light-mode-only)![Merged plots](https://clear.ml/docs/latest/assets/images/pipelines_comparison_plots_merged_dark-6d46527eb0db90a8b82f44f8714109ed.png#dark-mode-only)

Other plot types are displayed separately for each run.

![Side-by-side plots](https://clear.ml/docs/latest/assets/images/pipelines_comparison_plots-a790e91aa2d0d27033cb4f3bb6c70746.png#light-mode-only)![Side-by-side plots](https://clear.ml/docs/latest/assets/images/pipelines_comparison_plots_dark-e0b70710b83733abb0628b793e8a43be.png#dark-mode-only)

### Run Details Comparison [​](https://clear.ml/docs/latest/docs/webapp/pipelines/webapp_pipeline_table/\#run-details-comparison "Direct link to Run Details Comparison")

For a more in depth comparison of pipeline runs, select the runs to compare and click **Compare** in the batch action
bar. In the run comparison pages, you can compare details, hyperparameters, scalars, plots, and debug samples. For more
information, see [Comparing Tasks](https://clear.ml/docs/latest/docs/webapp/webapp_exp_comparing).

- [Run Table Columns](https://clear.ml/docs/latest/docs/webapp/pipelines/webapp_pipeline_table/#run-table-columns)
- [Customizing the Runs Table](https://clear.ml/docs/latest/docs/webapp/pipelines/webapp_pipeline_table/#customizing-the-runs-table)
  - [Filtering Columns](https://clear.ml/docs/latest/docs/webapp/pipelines/webapp_pipeline_table/#filtering-columns)
- [Create Run](https://clear.ml/docs/latest/docs/webapp/pipelines/webapp_pipeline_table/#create-run)
  - [Create New Pipeline](https://clear.ml/docs/latest/docs/webapp/pipelines/webapp_pipeline_table/#create-new-pipeline)
- [Run Actions](https://clear.ml/docs/latest/docs/webapp/pipelines/webapp_pipeline_table/#run-actions)
- [Selecting Multiple Runs](https://clear.ml/docs/latest/docs/webapp/pipelines/webapp_pipeline_table/#selecting-multiple-runs)
- [Comparing Runs](https://clear.ml/docs/latest/docs/webapp/pipelines/webapp_pipeline_table/#comparing-runs)
  - [Run Details Comparison](https://clear.ml/docs/latest/docs/webapp/pipelines/webapp_pipeline_table/#run-details-comparison)