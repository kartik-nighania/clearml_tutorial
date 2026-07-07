---
url: "https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_exp_comparing/"
title: "Comparing Dataviews | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_exp_comparing/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

Enterprise Feature

Dataviews are available under the ClearML Enterprise plan.

In addition to [ClearML's comparison features](https://clear.ml/docs/latest/docs/webapp/webapp_exp_comparing), the ClearML Enterprise WebApp
supports comparing input data selection criteria of task [Dataviews](https://clear.ml/docs/latest/docs/hyperdatasets/dataviews), enabling to easily locate, visualize, and analyze differences.

## Selecting Tasks [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_exp_comparing/\#selecting-tasks "Direct link to Selecting Tasks")

To select tasks to compare:

1. Go to a task table that includes the tasks to be compared.
2. Select the tasks to compare. Once multiple tasks are selected, the batch action bar appears.
3. In the batch action bar, click **COMPARE**.

The comparison page opens in the **DETAILS** tab, showing a column for each task.

## Dataviews [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_exp_comparing/\#dataviews "Direct link to Dataviews")

In the **Details** tab, you can view differences in the tasks' nominal values. Each task's information is
displayed in a column, so each field is lined up side-by-side. Expand the **DATAVIEWS**
section to view all the Dataview fields side-by-side (filters, iterations, label enumeration, etc.). The differences between the
tasks are highlighted. Obscure identical fields by switching on the `Hide Identical Fields` toggle.

The task on the left is used as the base task, to which the other tasks are compared. You can set a
new base task
in one of the following ways:

- Hover and click ![Switch base task](https://clear.ml/docs/latest/icons/ico-arrow-from-right.svg)
on the task that will be the new base.
- Hover and click ![Pan icon](https://clear.ml/docs/latest/icons/ico-drag.svg) on the new base task and drag it all the way to the left

![Dataview comparison](https://clear.ml/docs/latest/assets/images/compare_dataviews-9a966cb2f83cf8811dff44c65e4eeb77.png#light-mode-only)![Dataview comparison](https://clear.ml/docs/latest/assets/images/compare_dataviews_dark-dee2f32c0edc5203e9a373f84af0c4ca.png#dark-mode-only)

- [Selecting Tasks](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_exp_comparing/#selecting-tasks)
- [Dataviews](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_exp_comparing/#dataviews)