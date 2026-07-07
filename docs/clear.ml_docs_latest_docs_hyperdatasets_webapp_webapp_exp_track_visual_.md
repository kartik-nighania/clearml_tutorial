---
url: "https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_exp_track_visual/"
title: "Task Dataviews | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_exp_track_visual/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

Enterprise Feature

Dataviews are available under the ClearML Enterprise plan.

While a task is running, and any time after it finishes, results are tracked and can be visualized in the ClearML
Enterprise WebApp (UI).

In addition to all of ClearML's offerings, ClearML Enterprise keeps track of the Dataviews associated with a
task, which can be viewed and [modified](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_exp_modifying) in the WebApp.

## Viewing a Task's Dataviews [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_exp_track_visual/\#viewing-a-tasks-dataviews "Direct link to Viewing a Task's Dataviews")

In a task's page, go to the **DATAVIEWS** tab to view all the task's Dataview details, including:

- Input data [selection](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_exp_track_visual/#input) and [filtering](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_exp_track_visual/#filtering)
- ROI [mapping](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_exp_track_visual/#mapping) (label translation)
- [Label enumeration](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_exp_track_visual/#label-enumeration)
- [Iteration controls](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_exp_track_visual/#iteration-control)

![Dataview tab](https://clear.ml/docs/latest/assets/images/dataview_tab-50cd12db08b8d91147732848c04e1ed6.png#light-mode-only)![Dataview tab](https://clear.ml/docs/latest/assets/images/dataview_tab_dark-ee17731f5b024b22011b58f6ec24c677.png#dark-mode-only)

### Input [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_exp_track_visual/\#input "Direct link to Input")

SingleFrames are iterated from the Dataset versions specified in the **INPUT** area, in the **SELECTED DATAVIEW** drop-down
menu.

### Filtering [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_exp_track_visual/\#filtering "Direct link to Filtering")

The **FILTERING** section lists the SingleFrame filters iterated by a Dataview, applied to the task data.

Each frame filter is composed of:

- A Dataset version to input from
- ROI Rules for SingleFrames to include and/or exclude certain criteria.
- Weights for debiasing input data.

Combinations of frame filters can implement complex querying.

For more detailed information, see [Filtering](https://clear.ml/docs/latest/docs/hyperdatasets/dataviews#filtering).

### Mapping [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_exp_track_visual/\#mapping "Direct link to Mapping")

ROI label mapping (label translation) applies to the new model. For example, use ROI label mapping to accomplish the following:

- Combine several labels under another more generic label.
- Consolidate disparate datasets containing different names for the ROI.
- Hide labeled objects from the training process.

For detailed information, see [Mapping ROI labels](https://clear.ml/docs/latest/docs/hyperdatasets/dataviews#mapping-roi-labels).

### Label Enumeration [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_exp_track_visual/\#label-enumeration "Direct link to Label Enumeration")

Assign label enumeration in the **LABELS ENUMERATION** area.

### Iteration Control [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_exp_track_visual/\#iteration-control "Direct link to Iteration Control")

The input data iteration control settings determine the order, number, timing, and reproducibility of the Dataview iterating
SingleFrames. Depending upon the combination of iteration control settings, all SingleFrames may not be iterated, and some may repeat.

For detailed information, see [Iteration control](https://clear.ml/docs/latest/docs/hyperdatasets/dataviews#iteration-control).

- [Viewing a Task's Dataviews](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_exp_track_visual/#viewing-a-tasks-dataviews)
  - [Input](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_exp_track_visual/#input)
  - [Filtering](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_exp_track_visual/#filtering)
  - [Mapping](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_exp_track_visual/#mapping)
  - [Label Enumeration](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_exp_track_visual/#label-enumeration)
  - [Iteration Control](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_exp_track_visual/#iteration-control)