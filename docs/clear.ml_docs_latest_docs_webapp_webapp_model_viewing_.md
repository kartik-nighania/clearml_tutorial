---
url: "https://clear.ml/docs/latest/docs/webapp/webapp_model_viewing/"
title: "Model Details | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/webapp/webapp_model_viewing/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

In the model table, double-click on a model to view and/or modify the following:

- General model information
- Model configuration
- Model label enumeration
- Model metadata
- Model scalars and other plots

Models in _Draft_ status are editable, so you can modify their configuration, label enumeration, and metadata.
_Published_ models are read-only, so only their metadata can be modified.

## General Model Information [​](https://clear.ml/docs/latest/docs/webapp/webapp_model_viewing/\#general-model-information "Direct link to General Model Information")

The **GENERAL** tab lists the model's General information including:

- Model URL
- ML Framework
- Creating task (ClearML task that generated the model)
- Description (click to edit)

If the model is stored in a network location, it can be downloaded by clicking the model URL. If the model was stored on
the local machine you can copy its URL to manually access it.

![Model general information](https://clear.ml/docs/latest/assets/images/webapp_model_general-246ba0e91e712c4b542325b84f63bc1c.png#light-mode-only)![Model general information](https://clear.ml/docs/latest/assets/images/webapp_model_general_dark-88986e2821136707145f01dccbeae4f6.png#dark-mode-only)

## Model Configuration [​](https://clear.ml/docs/latest/docs/webapp/webapp_model_viewing/\#model-configuration "Direct link to Model Configuration")

The **NETWORK** tab displays the model's configuration.

![Model network](https://clear.ml/docs/latest/assets/images/webapp_model_network-4b2bc74d15f6c61c718ea580d9f06147.png#light-mode-only)![Model network](https://clear.ml/docs/latest/assets/images/webapp_model_network_dark-16d65b49ff1030d872ff459823f5c306.png#dark-mode-only)

Hover over the model configuration area to access the following actions:

![Model config actions](<Base64-Image-Removed>)![Model config actions](https://clear.ml/docs/latest/assets/images/webapp_model_config_actions_dark-519f3ff5f71708d1fd8eef0caefcc73b.png#dark-mode-only)

- ![Magnifying glass](https://clear.ml/docs/latest/icons/ico-search.svg) Search
- ![Copy](https://clear.ml/docs/latest/icons/ico-copy-to-clipboard.svg) Copy configuration
- ![Trash](https://clear.ml/docs/latest/icons/ico-trash.svg)**CLEAR** (for _Draft_ models) - Delete the configuration
- **EDIT** (for _Draft_ models) - Modify / Add model configuration

## Label Enumeration [​](https://clear.ml/docs/latest/docs/webapp/webapp_model_viewing/\#label-enumeration "Direct link to Label Enumeration")

The **LABELS** tab displays for each class label (`Label`) its name and enumerated value (`ID`).

![Model label enumeration](https://clear.ml/docs/latest/assets/images/webapp_model_labels-52c723bcf38ac580434406e1e1a08cec.png#light-mode-only)![Model label enumeration](https://clear.ml/docs/latest/assets/images/webapp_model_labels_dark-71d2d4b832afbc6539cb655cdb94bed5.png#dark-mode-only)

To modify / add / delete class labels (for _Draft_ models), hover over the label table and click **EDIT**. This opens the
label editing window.

![Model label editing](https://clear.ml/docs/latest/assets/images/webapp_model_labels_edit-df02d740df98a64efa62db41186534d5.png#light-mode-only)![Model label editing](https://clear.ml/docs/latest/assets/images/webapp_model_labels_edit_dark-7df53e956fc58a3bb6ef989837c370b8.png#dark-mode-only)

## Metadata [​](https://clear.ml/docs/latest/docs/webapp/webapp_model_viewing/\#metadata "Direct link to Metadata")

The **METADATA** tab lists the model's metadata entries, which consist of a key, type, and value.

![Model metadata](https://clear.ml/docs/latest/assets/images/webapp_model_metadata-e4296f300a4e725f74fa3f6cfda3820f.png#light-mode-only)![Model metadata](https://clear.ml/docs/latest/assets/images/webapp_model_metadata_dark-8245adb0029cc52aee46e9f5be963724.png#dark-mode-only)

To modify / add / delete model metadata items, hover over the metadata table and click **EDIT**. This opens the metadata editing
window.

![Model metadata editing](https://clear.ml/docs/latest/assets/images/webapp_model_metadata_edit-f3da40ba88739c8302110bb9a87c7b9a.png#light-mode-only)![Model metadata editing](https://clear.ml/docs/latest/assets/images/webapp_model_metadata_edit_dark-36321fc47f25a46d64ad7933ac9eb7b1.png#dark-mode-only)

## Lineage [​](https://clear.ml/docs/latest/docs/webapp/webapp_model_viewing/\#lineage "Direct link to Lineage")

The **LINEAGE** tab displays the model's creating task (the ClearML task that generated the model) and lists
all the tasks where the model is used as an input model. Click a task to navigate to its page.

You can filter the task list by tags and task status.

Use the search bar to look for tasks based on their name, ID, or description.

![Model lineage](https://clear.ml/docs/latest/assets/images/webapp_model_lineage-eba2d4e63a3dc01d96009e9541811e38.png#light-mode-only)![Model lineage](https://clear.ml/docs/latest/assets/images/webapp_model_lineage_dark-194fabaae19d2f035f0ec8a7f694af15.png#dark-mode-only)

## Scalars [​](https://clear.ml/docs/latest/docs/webapp/webapp_model_viewing/\#scalars "Direct link to Scalars")

The **SCALARS** tab displays all scalar plots attached to a model. Scalar values are presented as time series line
plots. To see the series for a metric in high resolution, view it in full screen mode by hovering over the graph and
clicking ![Maximize plot icon](https://clear.ml/docs/latest/icons/ico-maximize.svg).
Reported single value scalars are aggregated into a table plot displaying scalar names and values.

To embed scalar plots in your [Reports](https://clear.ml/docs/latest/docs/webapp/webapp_reports), hover over a plot and click ![Embed code](https://clear.ml/docs/latest/icons/ico-plotly-embed-code.svg),
which will copy to clipboard the embed code to put in your Reports. In contrast to static screenshots, embedded resources
are retrieved when the report is displayed allowing your reports to show the latest up-to-date data.

For better plot analysis, see [Plot Controls](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual#plot-controls).

![Model scalars](https://clear.ml/docs/latest/assets/images/webapp_model_scalars-964545c9c5b85566146630daafb654f8.png#light-mode-only)![Model scalars](https://clear.ml/docs/latest/assets/images/webapp_model_scalars_dark-560d887e894e00e040aedea90e640f33.png#dark-mode-only)

## Plots [​](https://clear.ml/docs/latest/docs/webapp/webapp_model_viewing/\#plots "Direct link to Plots")

The **PLOTS** tab displays plots attached to a model.

To embed plots in your [Reports](https://clear.ml/docs/latest/docs/webapp/webapp_reports), hover over a plot and click ![Embed code](https://clear.ml/docs/latest/icons/ico-plotly-embed-code.svg),
which will copy to clipboard the embed code to put in your Reports. In contrast to static screenshots, embedded resources
are retrieved when the report is displayed allowing your reports to show the latest up-to-date data.

For better plot analysis, see [Plot Controls](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual#plot-controls).

![Model plots](https://clear.ml/docs/latest/assets/images/webapp_model_plots-b9075d53d7b221ed95493d73976f8dc4.png#light-mode-only)![Model plots](https://clear.ml/docs/latest/assets/images/webapp_model_plots_dark-89fbc5cd9470abaae817836a743afa76.png#dark-mode-only)

- [General Model Information](https://clear.ml/docs/latest/docs/webapp/webapp_model_viewing/#general-model-information)
- [Model Configuration](https://clear.ml/docs/latest/docs/webapp/webapp_model_viewing/#model-configuration)
- [Label Enumeration](https://clear.ml/docs/latest/docs/webapp/webapp_model_viewing/#label-enumeration)
- [Metadata](https://clear.ml/docs/latest/docs/webapp/webapp_model_viewing/#metadata)
- [Lineage](https://clear.ml/docs/latest/docs/webapp/webapp_model_viewing/#lineage)
- [Scalars](https://clear.ml/docs/latest/docs/webapp/webapp_model_viewing/#scalars)
- [Plots](https://clear.ml/docs/latest/docs/webapp/webapp_model_viewing/#plots)