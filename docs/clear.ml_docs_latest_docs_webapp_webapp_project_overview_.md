---
url: "https://clear.ml/docs/latest/docs/webapp/webapp_project_overview/"
title: "Project Overview | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/webapp/webapp_project_overview/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

A project's **OVERVIEW** tab provides options to present a general picture of the project. The page consists of a graph
that can show a snapshot of specified metrics' values across the project's tasks, and a space to enter and edit a
project's description. When either overview option is utilized, the **OVERVIEW** tab becomes the project's landing page,
meaning that it's the first thing that is seen when opening the project.

![Project overview](https://clear.ml/docs/latest/assets/images/webapp_project_overview-ff80e42b2f4a598228b4f6e65bf6ab57.png#light-mode-only)![Project overview](https://clear.ml/docs/latest/assets/images/webapp_project_overview_dark-c48f33871f525010fed7d51241342431.png#dark-mode-only)

## Metric Snapshot [​](https://clear.ml/docs/latest/docs/webapp/webapp_project_overview/\#metric-snapshot "Direct link to Metric Snapshot")

On the top of the **OVERVIEW** tab, you can display a **metric snapshot**. Choose metric variants, and the plot area
will present an aggregated view of the values for those metrics and the time that each task scored those values.
This way, the project's progress can be quickly deduced.

To add metric variants to the overview:

1. Click **Select Metric & Variant**
2. Select a metric **>** Expand a variant **>** Select the last reported (`LAST`), minimal (`MIN`) and/or maximal (`MAX`)
value to show
3. Click **Apply**

![Metric Snapshot selection](https://clear.ml/docs/latest/assets/images/webapp_metric_snapshot_selection-453ad5ca6c42d84270d1fae1b24fc960.png#light-mode-only)![Metric Snapshot selection](https://clear.ml/docs/latest/assets/images/webapp_metric_snapshot_selection_dark-ffde84027bbbfc1cffe17027b220515f.png#dark-mode-only)

To remove metric variants:

1. Click **\+ Metrics**
2. Remove in one of the following ways:
   - On the right panel list, hover over a variant and click `X`
   - On the left panel, uncheck metric variant
   - To remove all variants, click `Clear all`
3. Click **Apply**

When a single metric variant is selected, the plot color codes task status
(`Completed`, `Aborted`, `Published`, or `Failed`). When multiple variants are selected, each color corresponds to a
metric/variant combination.

Hover over a point in the snapshot, and a box will appear with the details of the task associated with the metric
value. Click the point to go to the task's details page.

![Project overview tab gif](https://clear.ml/docs/latest/assets/images/webapp_metric_snapshot-5f9941e23624806c1769109358d303bc.gif#light-mode-only)![Project overview tab gif](https://clear.ml/docs/latest/assets/images/webapp_metric_snapshot_dark-646aedfa1dd9611b78b787a4880b79a3.gif#dark-mode-only)

## Project Description [​](https://clear.ml/docs/latest/docs/webapp/webapp_project_overview/\#project-description "Direct link to Project Description")

Every project has a `description` field. The UI provides a Markdown editor to edit this field. For a quick reference for
the MarkDown syntax that can be used, see [Markdown Formatting Quick Guide](https://clear.ml/docs/latest/docs/webapp/webapp_reports#markdown-formatting-quick-guide).

In the Markdown document, you can write and share reports and add links to ClearML tasks
or any network resource such as issue tracker, web repository, etc.

### Editing the Description [​](https://clear.ml/docs/latest/docs/webapp/webapp_project_overview/\#editing-the-description "Direct link to Editing the Description")

To edit the description in the **OVERVIEW** tab, hover over the description section, and press the **EDIT** button that
appears on the top right of the window.

When using the Markdown editor, you can make use of features such as bullets,
numbered lists, code blocks, headings with levels, images, and italicized and bolded text.

- [Metric Snapshot](https://clear.ml/docs/latest/docs/webapp/webapp_project_overview/#metric-snapshot)
- [Project Description](https://clear.ml/docs/latest/docs/webapp/webapp_project_overview/#project-description)
  - [Editing the Description](https://clear.ml/docs/latest/docs/webapp/webapp_project_overview/#editing-the-description)