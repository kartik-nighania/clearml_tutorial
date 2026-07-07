---
url: "https://clear.ml/docs/latest/docs/webapp/webapp_exp_comparing/"
title: "Comparing Tasks | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/webapp/webapp_exp_comparing/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The ClearML Web UI provides features for comparing tasks, allowing to locate, visualize, and analyze the
differences in task results and their causes. You can view the differences in:

- [Details](https://clear.ml/docs/latest/docs/webapp/webapp_exp_comparing/#side-by-side-textual-comparison) \- Compare task source code, package versions, models, configuration
objects, and other details.
- Hyperparameters
  - [Values](https://clear.ml/docs/latest/docs/webapp/webapp_exp_comparing/#side-by-side-textual-comparison) \- Compare parameters and their values
  - [Parallel coordinates](https://clear.ml/docs/latest/docs/webapp/webapp_exp_comparing/#parallel-coordinates-mode) \- View the impact of hyperparameters on selected metrics
  - [Scatter plot](https://clear.ml/docs/latest/docs/webapp/webapp_exp_comparing/#scatter-plot) \- View the correlation between a selected hyperparameter and metric
- Scalars - Compare task metrics:
  - [Values](https://clear.ml/docs/latest/docs/webapp/webapp_exp_comparing/#tabular-scalar-comparison) \- Compare minimal, maximal or last reported values in a concise comparison
    table
  - [Graphs](https://clear.ml/docs/latest/docs/webapp/webapp_exp_comparing/#plot-comparison) \- Overlay compared tasks in a single graph per metric
- [Plots](https://clear.ml/docs/latest/docs/webapp/webapp_exp_comparing/#plot-comparison) \- Compare task plots
- [Debug samples](https://clear.ml/docs/latest/docs/webapp/webapp_exp_comparing/#side-by-side-debug-sample-comparison) \- Compare debug samples by iteration

With these comparisons, you can investigate the impact of different setups on your task results, and gain insight
for crafting future tasks.

## Selecting Tasks to Compare [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_comparing/\#selecting-tasks-to-compare "Direct link to Selecting Tasks to Compare")

To select tasks to compare:

1. Go to a task table that includes the tasks to be compared.
2. Select the tasks to compare. Once multiple tasks are selected, the batch action bar appears.
3. In the batch action bar, click **COMPARE**.

The comparison page opens in the **DETAILS** tab with the tasks [compared side by side](https://clear.ml/docs/latest/docs/webapp/webapp_exp_comparing/#side-by-side-textual-comparison).

### Modifying Task Selection [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_comparing/\#modifying-task-selection "Direct link to Modifying Task Selection")

Click `TASKS` to view the tasks currently included in the comparison.

![Tasks list](https://clear.ml/docs/latest/assets/images/webapp_compare_exp_select_2-3a89fb835c6913781b628aa8e7865ff2.png#light-mode-only)![Tasks list](https://clear.ml/docs/latest/assets/images/webapp_compare_exp_select_2_dark-e83a9e09da25ce83f62e7e6b84f5e718.png#dark-mode-only)

You can add/remove tasks to your comparison:

1. Click the `+` button in any of the comparison tabs. This opens up a window with a task table with the currently
compared tasks at the top.

![Adding tasks](https://clear.ml/docs/latest/assets/images/webapp_compare_exp_select_1-9b8222c9b580f39bd49aaf6db09e8b9b.png#light-mode-only)![Adding tasks](https://clear.ml/docs/latest/assets/images/webapp_compare_exp_select_1_dark-95de68a8d941611abf5eccdba147d106.png#dark-mode-only)

2. Find the tasks to add by sorting and [filtering](https://clear.ml/docs/latest/docs/webapp/webapp_exp_table#filtering-columns) the tasks with the
appropriate column header controls. Alternatively, use the search bar to find tasks by name.

3. Select tasks to include in the comparison (and/or clear the selection of any tasks you wish to remove).

4. Click **APPLY**.


### Task Actions [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_comparing/\#task-actions "Direct link to Task Actions")

Use the task actions menu ![Menu](https://clear.ml/docs/latest/icons/ico-bars-menu.svg)
on a task in the comparison to perform actions on it:

- View task in new tab - Open the task page to view all details.
- Rename
- Archive
- Remove from Comparison

![Task actions](https://clear.ml/docs/latest/assets/images/webapp_compare_exp_actions-9fda23d5e0c2a4d742b17288a361d216.png#light-mode-only)![Task actions](https://clear.ml/docs/latest/assets/images/webapp_compare_exp_actions_dark-5c5a369c118edd792dec34f0a95450c4.png#dark-mode-only)

## Sharing Comparison Page [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_comparing/\#sharing-comparison-page "Direct link to Sharing Comparison Page")

To share a comparison page, copy the full URL from the address bar and send it to a teammate to collaborate. They will
get the exact same page (including selected tabs etc.).

## Embedding Comparison Visualization [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_comparing/\#embedding-comparison-visualization "Direct link to Embedding Comparison Visualization")

To embed plots and debug samples from the comparison pages in your [Reports](https://clear.ml/docs/latest/docs/webapp/webapp_reports), hover over the
resource and click ![Embed code](https://clear.ml/docs/latest/icons/ico-plotly-embed-code.svg),
which will copy to clipboard the embed code to put in your Reports. These visualizations are updated live as the
tasks update. The Enterprise Plan and Hosted Service support embedding resources in third-party platforms that support embedded content (e.g. Notion).

## Comparison Modes [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_comparing/\#comparison-modes "Direct link to Comparison Modes")

The comparison pages provide the following views:

- [Side-by-side textual comparison](https://clear.ml/docs/latest/docs/webapp/webapp_exp_comparing/#side-by-side-textual-comparison)
- [Tabular scalar comparison](https://clear.ml/docs/latest/docs/webapp/webapp_exp_comparing/#tabular-scalar-comparison)
- [Parallel coordinates](https://clear.ml/docs/latest/docs/webapp/webapp_exp_comparing/#parallel-coordinates-mode) for parameter impact on metric
- [Scatter plot](https://clear.ml/docs/latest/docs/webapp/webapp_exp_comparing/#scatter-plot)
- [Overlaid plot comparison](https://clear.ml/docs/latest/docs/webapp/webapp_exp_comparing/#plot-comparison)
- Side-by-side [debug sample](https://clear.ml/docs/latest/docs/webapp/webapp_exp_comparing/#side-by-side-debug-sample-comparison) and [plot](https://clear.ml/docs/latest/docs/webapp/webapp_exp_comparing/#plot-comparison) comparison

### Side-by-side Textual Comparison [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_comparing/\#side-by-side-textual-comparison "Direct link to Side-by-side Textual Comparison")

In the **Details** and **Hyperparameters** (Values view) tabs, you can view differences in the tasks' parameters' nominal
values. The **Details** tab displays the tasks' execution details (source code, uncommitted changes, Python packages),
models, artifacts, configuration objects, and additional general information. **Hyperparameters** (Values view) displays the
tasks' hyperparameter and their values.

The tasks are laid out in vertical cards, so each field is lined up side-by-side. The task on the
left is used as the base task, to which the other tasks are compared. You can set a new base task in
one of the following ways:

- Hover and click ![Switch base task](https://clear.ml/docs/latest/icons/ico-arrow-from-right.svg) on the task that will be the new base.
- Hover and click ![Pan](https://clear.ml/docs/latest/icons/ico-drag.svg) on the new base task and drag it all the way to the left

The differences between the tasks are highlighted. Easily locate
value differences by clicking click ![Up arrow](https://clear.ml/docs/latest/icons/ico-previous-diff.svg)
(previous diff) or ![Down arrow](https://clear.ml/docs/latest/icons/ico-next-diff.svg) (next diff)
in the tab header. Obscure identical fields by switching on the **Hide Identical Fields** toggle.

Use the search bar to find any field names or values. Lines that match the search query are highlighted, and you can
navigate between search results.

![Side-by-side textual comparison](https://clear.ml/docs/latest/assets/images/webapp_compare_05-d6de5f568e6123148729474905352df5.png#light-mode-only)![Side-by-side textual comparison](https://clear.ml/docs/latest/assets/images/webapp_compare_05_dark-a7a80ddc216e11b347441da57ac007ce.png#dark-mode-only)

### Tabular Scalar Comparison [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_comparing/\#tabular-scalar-comparison "Direct link to Tabular Scalar Comparison")

The **Scalars** tab **Values** view lays out the tasks' metric values in a table: a row per metric/variant and a
column for each task. Select from the dropdown menu which metric values to display:

- Last Values: The last reported values for each task
- Min Values: The minimal value reported throughout the task execution
- Max Values: The maximal value reported throughout the task execution

You can download the scalar comparison table as a CSV file by clicking ![Download](https://clear.ml/docs/latest/icons/ico-download.svg).

Switch on the **Show row extremes** toggle to highlight each variant's maximum and minimum values.

![side-by-side scalar comparison](https://clear.ml/docs/latest/assets/images/webapp_compare_exp_scalar_vals-55e4c82062a890d330a508982c5005f6.png#light-mode-only)![side-by-side scalar comparison](https://clear.ml/docs/latest/assets/images/webapp_compare_exp_scalar_vals_dark-4f1f4b273ae6171b01b7bb2e6304d553.png#dark-mode-only)

### Parallel Coordinates Mode [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_comparing/\#parallel-coordinates-mode "Direct link to Parallel Coordinates Mode")

The **Hyperparameters** tab's **Parallel Coordinates** comparison shows tasks' hyperparameter impact on specified
metrics:

1. Under **Performance Metrics**, select metrics to compare for
2. Select the values to use for each metric in the plot (can select multiple):
   - LAST - The final value, or the most recent value, for currently running tasks
   - MIN - Minimal value
   - MAX - Maximal value
3. In **Parameters**, select the hyperparameters to compare.

For example, plot the metric/variant `accuracy`/`total` against the hyperparameters
`base_lr`, `dropout`, and `number_of_epochs`.

![Parallel coordinates](https://clear.ml/docs/latest/assets/images/webapp_compare_11-ae13044997e97cdc303a6925015e3203.png#light-mode-only)![Parallel coordinates](https://clear.ml/docs/latest/assets/images/webapp_compare_11_dark-ea3f7c0fc2d1942aab1b1692663d28fb.png#dark-mode-only)

To focus on a specific task, hover over its name in the graph legend.

To hide a task, click its name in the graph legend (click again to bring back).

### Scatter Plot [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_comparing/\#scatter-plot "Direct link to Scatter Plot")

The **Hyperparameters** tab's **Scatter Plot** comparison shows tasks' correlation between a selected
hyperparameter and metric.

To show the value distribution:

- Select the **Plot Axes**:

1. Under Y-axis select the metric and the metric values to use in the plot:
     - **LAST** \- The final value, or the most recent value, for currently running tasks
     - **MIN** \- Minimal value
     - **MAX** \- Maximal value
2. Under X-axis select the hyperparameter.

Hovering over each datapoint in the resulting plot will show the task name and the metric and parameter value for that
point. You can add additional metrics and hyperparameters values to the datapoint tooltip through **ADDITIONAL DATA POINT INFORMATION**.

![Comparison scatter plot](https://clear.ml/docs/latest/assets/images/webapp_compare_scatter-02bae8089f912fd4e6b72c85e729e7be.png#light-mode-only)![Comparison scatter plot](https://clear.ml/docs/latest/assets/images/webapp_compare_scatter_dark-d6e9a0f00d968724fc73020e22dd5e68.png#dark-mode-only)

### Plot Comparison [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_comparing/\#plot-comparison "Direct link to Plot Comparison")

The **Scalars** (Graph view) and **Plots** tabs compare tasks' plots.

The **Scalars** tab displays scalar values as time series line charts. The **Plots** tab compares the last reported
iteration sample of each metric/variant combination per compared task.

Line, scatter, box, and bar graphs are compared by overlaying each metric/variant from all compared tasks' into a single
comparative plot.

For overlaid plots, use **Group by** to select how to group plots:

- **Metric** \- All variants for a metric appear on the same plot.

![Scalar plot grouped by metric](https://clear.ml/docs/latest/assets/images/webapp_compare_07-c0aef06197a4f1070b75325174c5fc90.png#light-mode-only)![Scalar plot grouped by metric](https://clear.ml/docs/latest/assets/images/webapp_compare_07_dark-a8553740a23d0a65b81479007583f628.png#dark-mode-only)

- **Metric+Variant** (default) - Every variant appears on its own plot.

![Scalar plot grouped by metric and variant](https://clear.ml/docs/latest/assets/images/webapp_compare_08-3e838b80f90086a804357c02df0de520.png#light-mode-only)![Scalar plot grouped by metric and variant](https://clear.ml/docs/latest/assets/images/webapp_compare_08_dark-3ecefac9554ea3154c4677ed0408929a.png#dark-mode-only)


Other plot types that are not overlaid are displayed separately for each task:

![non-merged comparison](https://clear.ml/docs/latest/assets/images/webapp_compare_exp_plots-2e77f6d0dd52c0d56b43d7b6e97ee70e.png#light-mode-only)![non-merged comparison](https://clear.ml/docs/latest/assets/images/webapp_compare_exp_plots_dark-312c8600920c838df0739136f7164e54.png#dark-mode-only)

All single value scalars are plotted into a single clustered bar chart under the "Summary" title, where each cluster
represents a reported metric, and each bar in the cluster represents a task.

![Single scalar comparison](https://clear.ml/docs/latest/assets/images/webapp_compare_exp_single_scalars-c54e5d6e9786ac9c45ab3ef636c3fbef.png#light-mode-only)![Single scalar comparison](https://clear.ml/docs/latest/assets/images/webapp_compare_exp_single_scalars_dark-651d6696a3f077336dad2ed45bf9ff4f.png#dark-mode-only)

Hover over plots to access plot controls (see [Scalar Plot Tools](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual#scalar-plot-tools)).

### Side-by-side Debug Sample Comparison [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_comparing/\#side-by-side-debug-sample-comparison "Direct link to Side-by-side Debug Sample Comparison")

Compare debug samples at different iterations to examine how your tasks perform throughout their execution.

You can view debug samples by metric in the reported iterations. Filter the samples by metric
by selecting a metric from the dropdown menu above the samples. The most recent iteration appears first. To navigate
between iterations, click ![Left arrow](https://clear.ml/docs/latest/icons/ico-circle-older.svg) (older images),
![Right arrow](https://clear.ml/docs/latest/icons/ico-circle-newer.svg) (newer images),
or ![right arrow, newest image](https://clear.ml/docs/latest/icons/ico-circle-newest.svg) (newest images).

Click ![Sync selection](https://clear.ml/docs/latest/icons/ico-disconnect.svg) in order
to synchronize iteration and metric selection across tasks. For example, if you select a metric for one
task's debug samples, the same metric will be automatically selected for the rest of the tasks in the
comparison.

![Debug sample comparison](https://clear.ml/docs/latest/assets/images/webapp_compare_30-55bd96cd1d1bc17c5d2160a6d1d89bcd.png#light-mode-only)![Debug sample comparison](https://clear.ml/docs/latest/assets/images/webapp_compare_30_dark-f6c3519186c44fb575f3f63e1a0d5434.png#dark-mode-only)

Open a debug sample (image, audio, or video) in the viewer or player, by clicking the thumbnail.

![Debug Sample viewer](https://clear.ml/docs/latest/assets/images/webapp_tracking_44-345319f66443cc781cb27ab4b4a84d8c.png#light-mode-only)![Debug Sample viewer](https://clear.ml/docs/latest/assets/images/webapp_tracking_44_dark-6055821ebc292a69dfccb131d3287fad.png#dark-mode-only)

To move to the same sample in another iteration, click ![Left arrow](https://clear.ml/docs/latest/icons/ico-previous.svg)
(previous), ![Right arrow](https://clear.ml/docs/latest/icons/ico-next.svg) (next), or move the slider.

- [Selecting Tasks to Compare](https://clear.ml/docs/latest/docs/webapp/webapp_exp_comparing/#selecting-tasks-to-compare)
  - [Modifying Task Selection](https://clear.ml/docs/latest/docs/webapp/webapp_exp_comparing/#modifying-task-selection)
  - [Task Actions](https://clear.ml/docs/latest/docs/webapp/webapp_exp_comparing/#task-actions)
- [Sharing Comparison Page](https://clear.ml/docs/latest/docs/webapp/webapp_exp_comparing/#sharing-comparison-page)
- [Embedding Comparison Visualization](https://clear.ml/docs/latest/docs/webapp/webapp_exp_comparing/#embedding-comparison-visualization)
- [Comparison Modes](https://clear.ml/docs/latest/docs/webapp/webapp_exp_comparing/#comparison-modes)
  - [Side-by-side Textual Comparison](https://clear.ml/docs/latest/docs/webapp/webapp_exp_comparing/#side-by-side-textual-comparison)
  - [Tabular Scalar Comparison](https://clear.ml/docs/latest/docs/webapp/webapp_exp_comparing/#tabular-scalar-comparison)
  - [Parallel Coordinates Mode](https://clear.ml/docs/latest/docs/webapp/webapp_exp_comparing/#parallel-coordinates-mode)
  - [Scatter Plot](https://clear.ml/docs/latest/docs/webapp/webapp_exp_comparing/#scatter-plot)
  - [Plot Comparison](https://clear.ml/docs/latest/docs/webapp/webapp_exp_comparing/#plot-comparison)
  - [Side-by-side Debug Sample Comparison](https://clear.ml/docs/latest/docs/webapp/webapp_exp_comparing/#side-by-side-debug-sample-comparison)