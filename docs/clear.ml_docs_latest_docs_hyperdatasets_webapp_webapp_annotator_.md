---
url: "https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_annotator/"
title: "Annotation Tasks | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_annotator/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

Enterprise Feature

Annotation tasks are available under the ClearML Enterprise plan.

Use the Annotations page to access and manage annotation Tasks.

Use annotation tasks to efficiently organize the annotation of frames in Dataset versions and manage the work of annotators
(see [Annotating Images and Videos](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_annotator/#annotating-images-and-video)).

![Annotations page](https://clear.ml/docs/latest/assets/images/annotation_page-f7d3e05d9ebcf2c2341c99e70f260d65.png#light-mode-only)![Annotations page](https://clear.ml/docs/latest/assets/images/annotation_page_dark-f1585af6211d728100424555b69a4a14.png#dark-mode-only)

Click on an annotation task card to open the frame viewer, where you can view the task's frames and annotate them.

Use the search bar ![Magnifying glass](https://clear.ml/docs/latest/icons/ico-search.svg)
to find specific annotation tasks. You can query by the task’s name, hyper-dataset version, and ID.
To search using regex, click the `.*` icon on the search bar.

## Annotation Task Actions [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_annotator/\#annotation-task-actions "Direct link to Annotation Task Actions")

Click ![Menu](https://clear.ml/docs/latest/icons/ico-bars-menu.svg) on the top right
of an annotation task card to open its context menu and access annotation task actions.

![Annotation task card](https://clear.ml/docs/latest/assets/images/annotation_task_card-0fd273ddd8a15c4c89b83ba07197ca3f.png#light-mode-only)![Annotation task card](https://clear.ml/docs/latest/assets/images/annotation_task_card_dark-bbef27c9a85f2120b70b9dfa83bbedfc.png#dark-mode-only)

- **Annotate** \- Go to annotation task frame viewer
- **Info** \- View annotation task's definitions: dataset versions, filters, and frame iteration specification
- **Complete** \- Mark annotation task as Completed
- **Delete** \- Delete annotation task

## Page View Options [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_annotator/\#page-view-options "Direct link to Page View Options")

The following are options for filtering annotation tasks:

- Active / Completed Filter - Toggle to show annotation tasks that are either Active or Completed
- Dataset Filter - Use to view only the annotation tasks for a specific Dataset
- My / Team Work - Toggle to show annotation tasks that either only you created or any team member created

Sort the annotation tasks by either using **RECENT** or **NAME** option.

## Creating Annotation Tasks [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_annotator/\#creating-annotation-tasks "Direct link to Creating Annotation Tasks")

![Annotation task creation modal](https://clear.ml/docs/latest/assets/images/annotation_task_01-87012cff04e794770c609a0c6e2fd554.png#light-mode-only)![Annotation task creation modal](https://clear.ml/docs/latest/assets/images/annotation_task_01_dark-0f0471f57dbc7673a9d662fabb1eb735.png#dark-mode-only)

**To create an annotation task:**

1. On the Annotator page, click **\+ NEW ANNOTATION**.

2. Enter a name for your new annotation task.

3. Choose a Dataset version to annotate. If the selected Dataset version's status is _Published_, then creating this
annotation task also creates a child version of the selected version. The new child version's status is _Draft_, and
its name is the same as the annotation task.

4. Set the filters for the frames this annotation task presents to the annotator.
   - In the **SET FILTERS** list, choose either:
     - **All Frames** \- Include all frames in this task.
     - **Empty Frames** \- Include only frames without any annotations in this task.
     - **Custom Filters** \- Apply any combination of ROI, frame, and source filtering rules. See [Advanced Frame Filtering](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_versioning#advanced-frame-filtering).
5. Choose the iteration parameters specifying how frames in this version are presented to the annotator.
1. In **ITERATION**, in the **ORDER** list, choose either:
      - **Sequential** \- Frames are sorted by the frame top-level `context_id` (primary sort key) and `timestamp` (secondary sort key) metadata key values, and returned by the iterator in the sorted order.
      - **Random** \- Frames are randomly returned using the value of the `random_seed` argument. The random seed is maintained with the tasks. Therefore, the random order is reproducible if the task is rerun.
2. In **REPETITION**, choose either **Use Each Frame Once** or **Limit Frames**. If you select **Limit Frames**, then in **Use Max. Frames**, type the number of frames to annotate.

3. If iterating randomly, in **RANDOM SEED** type your seed or leave blank, and the ClearML Enterprise platform generates a seed for you.

4. If annotating video, then in **CLIP LENGTH (FOR VIDEO)**, type of the number of sequential frames per iteration to annotate.
6. Click **Create**.


## Annotating Images and Video [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_annotator/\#annotating-images-and-video "Direct link to Annotating Images and Video")

Annotate images and video by labeling regions of interest in Dataset version frames. The frames presented for annotation
depend upon the settings in the annotation task (see [Creating Annotation Tasks](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_annotator/#creating-annotation-tasks)).

### Creating New Frame Objects [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_annotator/\#creating-new-frame-objects "Direct link to Creating New Frame Objects")

To draw a new annotation

1. Click one of the following modes to choose what annotation to create:


   - ![Rectangle mode icon](https://clear.ml/docs/latest/icons/ico-rectangle-icon-purple.svg) \- Rectangle mode:
     Click then drag the cursor to create a rectangle annotation on the frame.

   - ![Ellipse mode icon](https://clear.ml/docs/latest/icons/ico-ellipse-icon-purple.svg) \- Ellipse mode:
     Click then drag the cursor to create an ellipse annotation on the frame.

   - ![Polygon mode icon](https://clear.ml/docs/latest/icons/ico-polygon-icon-purple.svg) \- Polygon mode:
     Each click sets polygon vertices on the frame. Click again on the initial vertex to close the polygon.

   - ![Key points mode icon](https://clear.ml/docs/latest/icons/ico-keypoint-icon-purple.svg) \- Key points mode:
     Each click adds a keypoint to the frame. After clicking the last keypoint, click ![Check mark](https://clear.ml/docs/latest/icons/ico-save.svg)
     or `Enter` to save the annotation. Click `Esc` to cancel the annotation.


A new annotation is created.

2. In the newly created annotation, select or type-in a label(s). Click the circle in the label name to select a
different label color.


You can use the **Default ROI Label(s)** list to automatically set labels to all new annotations.

#### Copying Frame Objects [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_annotator/\#copying-frame-objects "Direct link to Copying Frame Objects")

You can copy existing annotations, and paste them to any frame of your choice:

1. Click the annotation or bounded area in the frame.
2. Click ![Copy annotation](https://clear.ml/docs/latest/icons/ico-copy-to-clipboard.svg)
(copy annotation).
3. Navigate to the frame of your choice (you can remain in the same frame).
4. Click **PASTE**. The new annotation appears in the same location as the one you copied. You can paste the annotation
multiple times.

Copy all annotations in a frame by clicking the **COPY ALL** button.

### Annotation Actions [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_annotator/\#annotation-actions "Direct link to Annotation Actions")

The following table describes the actions that can be performed on existing annotations. The frame editor automatically
saves changes when you move to another frame using the frame navigation controls
(![Next frame icon](https://clear.ml/docs/latest/icons/ico-arrow-right.svg), ![Jump to next unfiltered annotation](https://clear.ml/docs/latest/icons/ico-skip-next.svg), ![Jump forwards icon](https://clear.ml/docs/latest/icons/ico-skip-forward.svg), ![Previous frame icon](https://clear.ml/docs/latest/icons/ico-arrow-left.svg), ![Jump to previous unfiltered annotation](https://clear.ml/docs/latest/icons/ico-skip-previous.svg), ![Jump backwards icon](https://clear.ml/docs/latest/icons/ico-skip-backward.svg),
or the arrow keys on the keyboard). Closing the frame editor will prompt you to save any changes.

| Icon (when applicable) | Action | Description |
| --- | --- | --- |
|  | Move annotation | Click on a bounded area and drag it. |
|  | Resize annotation | Select an annotation, then click on a bounded area's vertex and drag it. |
| ![edit metadata](https://clear.ml/docs/latest/icons/ico-metadata.svg) | Edit metadata | Hover over an annotation in the list and click the icon to open the edit window. Input the metadata dictionary in JSON format. This metadata is specific to the selected annotation, not the entire frame. |
| ![Lock annotation](https://clear.ml/docs/latest/icons/ico-lock-open.svg) | Lock / Unlock annotation | Click the button on a specific annotation to make it uneditable. You can also click the button on top of the annotations list to lock all annotations in the frame. |
| ![Trash](https://clear.ml/docs/latest/icons/ico-trash.svg) | Delete annotation | Click the annotation or bounded area in the frame and then click the button to delete the annotation. |
| ![Eye Show All](https://clear.ml/docs/latest/icons/ico-show.svg) | Show/hide all annotations | Click the button to view the frame without annotations. When annotations are hidden, they can't be modified. |
|  | Delete label | In the relevant annotation, click **x** on the label you want to remove. |

### Frame Labels [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_annotator/\#frame-labels "Direct link to Frame Labels")

You can add labels which describe the whole frame, with no specific coordinates.

**To add frame labels:**

1. Expand the **FRAME LABELS** area (below **OBJECTS**)
2. Click **\+ Add new**
3. Enter a label(s)

## Frame Metadata [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_annotator/\#frame-metadata "Direct link to Frame Metadata")

**To edit frame metadata:**

1. Expand the **FRAMEGROUP METADATA** area
2. Click edit ![edit metadata](https://clear.ml/docs/latest/icons/ico-metadata.svg)
which will open an editing window
3. Modify the metadata dictionary in JSON format

- [Annotation Task Actions](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_annotator/#annotation-task-actions)
- [Page View Options](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_annotator/#page-view-options)
- [Creating Annotation Tasks](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_annotator/#creating-annotation-tasks)
- [Annotating Images and Video](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_annotator/#annotating-images-and-video)
  - [Creating New Frame Objects](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_annotator/#creating-new-frame-objects)
  - [Annotation Actions](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_annotator/#annotation-actions)
  - [Frame Labels](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_annotator/#frame-labels)
- [Frame Metadata](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_annotator/#frame-metadata)