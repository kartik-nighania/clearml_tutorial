---
url: "https://clear.ml/docs/latest/docs/webapp/webapp_model_comparing/"
title: "Comparing Models | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/webapp/webapp_model_comparing/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The ClearML Web UI provides features for comparing models, allowing to locate, visualize, and analyze model differences.
You can view the differences in model details, configuration, scalar values, and more.

## Selecting Models to Compare [​](https://clear.ml/docs/latest/docs/webapp/webapp_model_comparing/\#selecting-models-to-compare "Direct link to Selecting Models to Compare")

To select models to compare:

1. Go to a model table that includes the models to be compared.
2. Select the models to compare. Once multiple models are selected, the batch action bar appears.
3. In the batch action bar, click **COMPARE**.

The comparison page opens in the **DETAILS** tab, with the models compared [side by side](https://clear.ml/docs/latest/docs/webapp/webapp_model_comparing/#side-by-side-textual-comparison).

### Modifying Model Selection [​](https://clear.ml/docs/latest/docs/webapp/webapp_model_comparing/\#modifying-model-selection "Direct link to Modifying Model Selection")

Click `MODELS` to view the models currently included in the comparison.

![Models list](https://clear.ml/docs/latest/assets/images/webapp_compare_model_select_1-49f798fad9f53988ac4dd9b0a95a28c7.png#light-mode-only)![Models list](https://clear.ml/docs/latest/assets/images/webapp_compare_model_select_1_dark-323533700f6338037c6a4b905a5761f6.png#dark-mode-only)

You can add/remove models to your comparison:

1. Click the `+` button in any of the comparison tabs. This opens up a window with a model table with the currently
compared models at the top.

![Adding models](https://clear.ml/docs/latest/assets/images/webapp_compare_model_select_2-7a92919ab76e4a7f59b71a7d3914d92c.png#light-mode-only)![Adding models](https://clear.ml/docs/latest/assets/images/webapp_compare_model_select_2_dark-0cd1b84ce48260f4818b920427083a45.png#dark-mode-only)

2. Find the models to add by sorting and [filtering](https://clear.ml/docs/latest/docs/webapp/webapp_model_table#filtering-columns) the models with the
appropriate column header controls. Alternatively, use the search bar to find models by name.

3. Select models to include in the comparison (and/or clear the selection of any models you wish to remove).

4. Click **APPLY**.


### Model Actions [​](https://clear.ml/docs/latest/docs/webapp/webapp_model_comparing/\#model-actions "Direct link to Model Actions")

Use the model actions menu ![Menu](https://clear.ml/docs/latest/icons/ico-bars-menu.svg)
on a menu in the comparison to perform actions on it:

- View menu in new tab - Open the menu page to view all details.
- Rename
- Archive
- Remove from Comparison

![Model actions](https://clear.ml/docs/latest/assets/images/webapp_compare_model_actions-0a84b24b5fbeea1a7a54f11668e6e10e.png#light-mode-only)![Model actions](https://clear.ml/docs/latest/assets/images/webapp_compare_model_actions_dark-c5c517cb3a381557494fa30b1e585766.png#dark-mode-only)

## Sharing Comparison Page [​](https://clear.ml/docs/latest/docs/webapp/webapp_model_comparing/\#sharing-comparison-page "Direct link to Sharing Comparison Page")

To share a comparison page, copy the full URL from the address bar and send it to a teammate to collaborate. They will
get the exact same page (including selected tabs etc.).

## Embedding Comparison Visualization [​](https://clear.ml/docs/latest/docs/webapp/webapp_model_comparing/\#embedding-comparison-visualization "Direct link to Embedding Comparison Visualization")

To embed plots and debug samples from the comparison pages in your [Reports](https://clear.ml/docs/latest/docs/webapp/webapp_reports), hover over the
resource and click ![Embed code](https://clear.ml/docs/latest/icons/ico-plotly-embed-code.svg),
which will copy to clipboard the embed code to put in your Reports. These visualizations are updated live as the
models update. The Enterprise Plan and Hosted Service support embedding resources in third-party platforms that support embedded content (e.g. Notion).

## Comparison Modes [​](https://clear.ml/docs/latest/docs/webapp/webapp_model_comparing/\#comparison-modes "Direct link to Comparison Modes")

The comparison tabs provides the following views:

- [Side-by-side textual comparison](https://clear.ml/docs/latest/docs/webapp/webapp_model_comparing/#side-by-side-textual-comparison)
- [Tabular scalar comparison](https://clear.ml/docs/latest/docs/webapp/webapp_model_comparing/#tabular-scalar-comparison)
- [Plot comparison](https://clear.ml/docs/latest/docs/webapp/webapp_model_comparing/#plot-comparison)

### Side-by-side Textual Comparison [​](https://clear.ml/docs/latest/docs/webapp/webapp_model_comparing/\#side-by-side-textual-comparison "Direct link to Side-by-side Textual Comparison")

In the **Details** and **Network** tabs, you can view differences in the models' nominal
values. **Details** displays the models' general information, labels, metadata, and lineage. **Network** displays the models'
configuration. Each model's
information is displayed in a column, so each field is lined up side-by-side.

The model on the left is used as the base model, to which the other models are compared. You can set a new base model
in one of the following ways:

- Hover and click ![Switch base model](https://clear.ml/docs/latest/icons/ico-arrow-from-right.svg)
on the model that will be the new base.
- Hover and click ![Pan icon](https://clear.ml/docs/latest/icons/ico-drag.svg) on the new base model and drag it all the way to the left

The differences between the models are highlighted. You can obscure identical fields by switching on the
**Hide Identical Fields** toggle.

![Text comparison](https://clear.ml/docs/latest/assets/images/webapp_compare_models_text-eefc460e4916fc8598b835752290247f.png#light-mode-only)![Text comparison](https://clear.ml/docs/latest/assets/images/webapp_compare_models_text_dark-c5a65ed2b994d5f9a1529f5d6e209438.png#dark-mode-only)

### Tabular Scalar Comparison [​](https://clear.ml/docs/latest/docs/webapp/webapp_model_comparing/\#tabular-scalar-comparison "Direct link to Tabular Scalar Comparison")

The **Scalars** tab ( **Values** view) lays out the models' reported metric values in a table: a row per metric/variant and a
column for each model. Select from the dropdown menu which metric values to display:

- Last Values: The last reported values for each model
- Min Values: The minimal value reported
- Max Values: The maximal value reported

You can download the scalar comparison table as a CSV file by clicking ![Download](https://clear.ml/docs/latest/icons/ico-download.svg).

Switch on the **Show row extremes** toggle to highlight each variant's maximum and minimum values.

![side-by-side scalar comparison](https://clear.ml/docs/latest/assets/images/webapp_compare_models_scalar_table-b5623439508890865c5189b24f14b474.png#light-mode-only)![side-by-side scalar comparison](https://clear.ml/docs/latest/assets/images/webapp_compare_models_scalar_table_dark-a0903785711d1848978bbdfa0bc00c54.png#dark-mode-only)

### Plot Comparison [​](https://clear.ml/docs/latest/docs/webapp/webapp_model_comparing/\#plot-comparison "Direct link to Plot Comparison")

The **Scalars** (Graph view) and **Plots** tabs display plots attached to the models.

The **Scalars** tab compares scalar values as time series line charts. The **Plots** tab compares the last reported
iteration sample of each metric/variant combination per compared model.

Line, scatter, box, and bar graphs are compared by overlaying each metric/variant from all compared models' into a single
comparative plot.

For overlaid plots, use **Group by** to select how to group plots:

- **Metric** \- All variants for a metric appear on the same plot.

![Scalar plot grouped by metric](https://clear.ml/docs/latest/assets/images/webapp_compare_models_merge_plots-f6c24f644aaf637b33196f624bbe9349.png#light-mode-only)![Scalar plot grouped by metric](https://clear.ml/docs/latest/assets/images/webapp_compare_models_merge_plots_dark-cf0f9591b1b0e9c84b18c47c089064f6.png#dark-mode-only)

- **Metric+Variant** (default) - Every variant appears on its own plot.

![Scalar plot grouped by metric and variant](https://clear.ml/docs/latest/assets/images/webapp_compare_models_variant_plots-fcee86f217b2d5181e9a15ef91c79f75.png#light-mode-only)![Scalar plot grouped by metric and variant](https://clear.ml/docs/latest/assets/images/webapp_compare_models_variant_plots_dark-9f3016005c974ecc9c5bace136a086f5.png#dark-mode-only)


Other plot types are displayed separately for each model.

![Side-by-side plots](https://clear.ml/docs/latest/assets/images/webapp_compare_models_side_plots-851864e3b5827b4c319b3a84f1e23a42.png#light-mode-only)![Side-by-side plots](https://clear.ml/docs/latest/assets/images/webapp_compare_models_side_plots_dark-f3059c07ec79cd42375c18bf961cd650.png#dark-mode-only)

All single value scalars are plotted into a single clustered bar chart under the "Summary" title, where each cluster
represents a reported metric, and each bar in the cluster represents a model.

![Single scalar comparison](https://clear.ml/docs/latest/assets/images/webapp_compare_model_single_scalars-6932536d218b126591d86252cb1d8707.png#light-mode-only)![Single scalar comparison](https://clear.ml/docs/latest/assets/images/webapp_compare_model_single_scalars_dark-aa185b6c0ab7f39aea629d259d185223.png#dark-mode-only)

For better plot analysis, see [Plot Controls](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual#plot-controls).

- [Selecting Models to Compare](https://clear.ml/docs/latest/docs/webapp/webapp_model_comparing/#selecting-models-to-compare)
  - [Modifying Model Selection](https://clear.ml/docs/latest/docs/webapp/webapp_model_comparing/#modifying-model-selection)
  - [Model Actions](https://clear.ml/docs/latest/docs/webapp/webapp_model_comparing/#model-actions)
- [Sharing Comparison Page](https://clear.ml/docs/latest/docs/webapp/webapp_model_comparing/#sharing-comparison-page)
- [Embedding Comparison Visualization](https://clear.ml/docs/latest/docs/webapp/webapp_model_comparing/#embedding-comparison-visualization)
- [Comparison Modes](https://clear.ml/docs/latest/docs/webapp/webapp_model_comparing/#comparison-modes)
  - [Side-by-side Textual Comparison](https://clear.ml/docs/latest/docs/webapp/webapp_model_comparing/#side-by-side-textual-comparison)
  - [Tabular Scalar Comparison](https://clear.ml/docs/latest/docs/webapp/webapp_model_comparing/#tabular-scalar-comparison)
  - [Plot Comparison](https://clear.ml/docs/latest/docs/webapp/webapp_model_comparing/#plot-comparison)