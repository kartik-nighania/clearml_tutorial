---
url: "https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_exp_modifying/"
title: "Modifying Dataviews | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_exp_modifying/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

Enterprise Feature

Dataviews are available under the ClearML Enterprise plan.

A task that has been executed can be [cloned](https://clear.ml/docs/latest/docs/webapp/webapp_exp_reproducing), then the cloned task's
execution details can be modified, and the modified task can be executed.

In addition to all the [ClearML tuning capabilities](https://clear.ml/docs/latest/docs/webapp/webapp_exp_tuning), the **ClearML Enterprise WebApp** (UI)
enables modifying [Dataviews](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_dataviews), including:

- [Selected Dataview](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_exp_modifying/#selecting-dataviews)
- [Dataset versions](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_exp_modifying/#selecting-dataset-versions)
- [Frame filtering](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_exp_modifying/#filtering-frames)
- [Label mapping](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_exp_modifying/#mapping-labels-label-translation)
- [Class label enumeration](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_exp_modifying/#label-enumeration)
- [Input frame iteration controls](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_exp_modifying/#iteration-controls)

## Selecting Dataviews [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_exp_modifying/\#selecting-dataviews "Direct link to Selecting Dataviews")

**To choose a Dataview**, do any of the following:

- Create a new Dataview
  - Click **+** and then follow the instructions below to select Hyper-Dataset versions, filter frames, map labels (label translation),
    and set label enumeration and iteration controls.
- Select a different Dataview already associated with the task.
  - In the **SELECTED DATAVIEW** list, choose a Dataview.
- Import a different Dataview associated with the same or another project.
  - Click ![Import](https://clear.ml/docs/latest/icons/ico-import.svg) ( **Import dataview**) and then
    select **Import to current dataview** or **Import as aux dataview**.

note

After importing a Dataview, it can be renamed and/or removed.

### Selecting Dataset Versions [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_exp_modifying/\#selecting-dataset-versions "Direct link to Selecting Dataset Versions")

To input data from a different data source or different version of a data source, select a different Dataset version used
by the Dataview.

**To select Dataset versions for input data:**

1. In the **INPUT** area, click **EDIT**.

2. Do any of the following:


   - Add a Dataset version - Input frames from another version of another Dataset.
     - Click **+**

     - Select a Dataset and a Dataset version
   - Remove a Dataset version - Do not input frames from a Dataset version.


Select frames from as many Dataset versions as are needed.

3. Click **SAVE**.


## Filtering Frames [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_exp_modifying/\#filtering-frames "Direct link to Filtering Frames")

Filtering of SingleFrames iterated by a Dataview for input to the task is accomplished by frame filters.
For more detailed information, see [Filtering](https://clear.ml/docs/latest/docs/hyperdatasets/dataviews#filtering).

**To modify frame filtering:**

1. In the **FILTERING** area, click **EDIT**.

2. For each frame filter:
1. Select the Hyper-Dataset version to which the frame filter applies.

2. Add, change, or remove any combination of the following rules:
      - ROI rule - Include or exclude frames containing any single ROI with any combination of labels in the Dataset
        version. Specify a range of the number of matching ROI (instances) per frame, and a range of confidence levels.
      - Frame rule - Filter by frame metadata key-value pairs, or ROI labels.
      - Source rule - Filter by frame `source` dictionary key-value pairs.
3. Optionally, debias input data by setting ratios for frames returned by the Dataview for each frame filter. These
      ratios allow adjusting an imbalance in input data.
3. Click **SAVE**.


## Mapping Labels (Label Translation) [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_exp_modifying/\#mapping-labels-label-translation "Direct link to Mapping Labels (Label Translation)")

Modify the ROI label mapping rules, which translate one or more input labels to another label for the output model. Labels
that are not mapped are ignored.

**To modify label mapping:**

1. In the **MAPPING** section, click **EDIT**
   - Add ( **+**) or edit a mapping:
     1. Select the Hyper-Dataset and version whose labels will be mapped.

     2. Select one or more labels to map.

     3. Select or enter the label to map to in the output model.
   - Remove (![Trash](https://clear.ml/docs/latest/icons/ico-trash.svg)) a mapping.
2. Click **SAVE**


## Label Enumeration [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_exp_modifying/\#label-enumeration "Direct link to Label Enumeration")

Modify the label enumeration assigned to output models.

**To modify label enumeration:**

1. In the **LABELS ENUMERATION** section, click **EDIT**.
   - Add ( **+**) or edit an enumeration:
     - Select a label and then enter an integer for it.
   - Remove (![Trash](https://clear.ml/docs/latest/icons/ico-trash.svg)) an enumeration.
2. Click **SAVE**.


## Iteration Controls [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_exp_modifying/\#iteration-controls "Direct link to Iteration Controls")

Modify the frame iteration performed by the Dataview to control the order, number, timing, and reproducibility of frames
for training.

For more detailed information, see [Iteration Control](https://clear.ml/docs/latest/docs/hyperdatasets/dataviews#iteration-control).

**To modify iteration controls:**

1. In the **ITERATION** sections, click **EDIT**.

2. Select the **ORDER** of the SingleFrames returned by the iteration, either:
   - **Sequential** \- Iterate SingleFrames in sorted order by context ID and timestamp.
   - **Random** \- Iterate SingleFrames randomly using the random seed you can set (see Random Seed below).
3. Select the frame **REPETITION** option, either:
   - **Use Each Frame Once**

   - **Limit Frames**

   - **Infinite Iterations**
4. Select the **RANDOM SEED** \- If the task is rerun and the seed remains unchanged, the frame iteration is the same.

5. For video, enter a **CLIP LENGTH** \- For video data sources, in the number of sequential frames from a clip to iterate.

6. Click **SAVE**.


- [Selecting Dataviews](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_exp_modifying/#selecting-dataviews)
  - [Selecting Dataset Versions](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_exp_modifying/#selecting-dataset-versions)
- [Filtering Frames](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_exp_modifying/#filtering-frames)
- [Mapping Labels (Label Translation)](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_exp_modifying/#mapping-labels-label-translation)
- [Label Enumeration](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_exp_modifying/#label-enumeration)
- [Iteration Controls](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_exp_modifying/#iteration-controls)