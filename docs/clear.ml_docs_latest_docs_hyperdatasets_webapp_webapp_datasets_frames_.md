---
url: "https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_frames/"
title: "Working with Frames | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_frames/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

Enterprise Feature

Hyper-Datasets are available under the ClearML Enterprise plan.

View and edit SingleFrames in the Dataset page. After selecting a Hyper-Dataset version, the **Version Browser** shows a sample
of frames and enables viewing SingleFrames and FramesGroups, and editing SingleFrames, in the [frame viewer](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_frames/#frame-viewer).
Before opening the frame viewer, you can apply [frame filters](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_versioning#frame-filtering).

![Dataset page](https://clear.ml/docs/latest/assets/images/dataset_versions-611d16ad40b9b1f85f07cdba51b5e8ea.png#light-mode-only)![Dataset page](https://clear.ml/docs/latest/assets/images/dataset_versions_dark-a7cfd566f7f8e1f646f51be94f02811a.png#dark-mode-only)

## Frame Viewer [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_frames/\#frame-viewer "Direct link to Frame Viewer")

Use the frame viewer to view and edit annotations (ROIs and frame labels), frame details (see [frames](https://clear.ml/docs/latest/docs/hyperdatasets/frames)),
and frame metadata, as well as view frame masks of your dataset version frames.

![Frame viewer](https://clear.ml/docs/latest/assets/images/dataset_example_frame_editor-f21f0a5ec1a1856d17c32a12bfc52d20.png#light-mode-only)![Frame viewer](https://clear.ml/docs/latest/assets/images/dataset_example_frame_editor_dark-e37a13d3db5716f1ddc8ef0eb2d86b22.png#dark-mode-only)

### Viewing FrameGroup Data [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_frames/\#viewing-framegroup-data "Direct link to Viewing FrameGroup Data")

FrameGroup information is organized across several panels in the Frame Viewer:

- **FrameGroup Details** – Displays all FrameGroup details except metadata. The details include: general fields (e.g.
`context_id`, dataset ID and version, timestamp, etc.) as well as annotation (e.g. `rois`, their `labels`, `confidence`, etc.)

  - Click ![edit metadata](https://clear.ml/docs/latest/icons/ico-metadata.svg) to view the details in a larger window.
  - Click ![view schema](https://clear.ml/docs/latest/icons/ico-code-file.svg) to view the dataset's frame document schema. This covers all possible fields in the dataset
- **FrameGroup Metadata** – Displays FrameGroup-level metadata. Displays only the contents of the `frame.meta` field—typically used for structured metadata or custom key-value data.

  - Click ![edit metadata](https://clear.ml/docs/latest/icons/ico-metadata.svg) to modify the metadata field.
- **Annotations** \- Review and modify frame annotations. For more information, see [Masks](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_frames/#masks) and [Annotations](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_frames/#annotations).

### Frame Viewer Controls [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_frames/\#frame-viewer-controls "Direct link to Frame Viewer Controls")

Use frame viewer controls to navigate between frames in a Hyper-Dataset Version, and control frame changes and viewing.

| Control Icon | Actions | Shortcut |
| --- | --- | --- |
| ![Jump backwards icon](https://clear.ml/docs/latest/icons/ico-skip-backward.svg) | Jumps backwards ten frames | CTRL + Left arrow |
| ![Jump to previous unfiltered annotation](https://clear.ml/docs/latest/icons/ico-skip-previous.svg) | Go to the previous frame containing a non-filtered annotation. The filter is the minimum confidence level setting. If the confidence level filter is set to zero, any frame containing annotations matches the filter. | ![Not applicable](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| ![Previous frame icon](https://clear.ml/docs/latest/icons/ico-arrow-left.svg) | Go to the previous frame | Left arrow |
| ![Next frame icon](https://clear.ml/docs/latest/icons/ico-arrow-right.svg) | Go to the next frame | Right arrow |
| ![Jump to next unfiltered annotation](https://clear.ml/docs/latest/icons/ico-skip-next.svg) | Go to the next frame containing a non-filtered annotation (same filter as ![Jump to previous unfiltered annotation](https://clear.ml/docs/latest/icons/ico-skip-previous.svg)). | ![Not applicable](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| ![Jump forwards icon](https://clear.ml/docs/latest/icons/ico-skip-forward.svg) | Jump forwards ten frames | CTRL + Right arrow |
| `Use Source Data` | Show the frame's `source` rather than its `preview` | ![Not applicable](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| ![Reload frame icon](https://clear.ml/docs/latest/icons/ico-revert.svg) | Reload the frame. | ![Not applicable](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| ![Undo icon](https://clear.ml/docs/latest/icons/ico-undo.svg) | Undo changes. | Ctrl + Z |
| ![Redo icon](https://clear.ml/docs/latest/icons/ico-redo.svg) | Redo changes. | Ctrl + Y |
| ![Autofit icon](https://clear.ml/docs/latest/icons/ico-zoom-to-fit.svg) | Autofit | ![Not applicable](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| ![Return to original size](https://clear.ml/docs/latest/icons/ico-zoom-1-to-1.svg) | View image in original size | ![Not applicable](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| ![Zoom in icon](https://clear.ml/docs/latest/icons/ico-zoom-in.svg) | Zoom in | **+** or Ctrl + Mouse wheel |
| ![Zoom out icon](https://clear.ml/docs/latest/icons/ico-zoom-out.svg) | Zoom out | **-** or Ctrl + Mouse wheel |
| Percentage textbox | Zoom percentage | ![Not applicable](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `Current Source` | When viewing multi-source FrameGroups, select which of the FrameGroups' sources to display: <br>- `Default preview source`: present the first available source for each frame (sources are retrieved in ASCIIbetical order)<br>- `All sources`: Present all the FrameGroup’s sources in a grid<br>- Specific source: Select an individual source by name from the list of available sources | ![Not applicable](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| ![Copy URL](https://clear.ml/docs/latest/icons/ico-shared-item.svg) | Copy frame URL. A direct link to view the current frame | ![Not applicable](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |

#### Additional Keyboard Shortcuts [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_frames/\#additional-keyboard-shortcuts "Direct link to Additional Keyboard Shortcuts")

**General Controls**

| Control | Action |
| --- | --- |
| Hold Spacebar + Press and hold image + Drag | Move around image. NOTE: If using a touchpad, this only works if the _Disable touchpad while typing_ setting is turned off |
| Esc | Escape frame viewer and return to dataset page |

**General Annotation Controls**

| Control | Action |
| --- | --- |
| Delete | Remove annotation |
| Alt + \] / \[ | Choose a default ROI label by navigating between previous / next labels |\
| Shift + M | Edit metadata |\
| Shift + N | Add a new [frame label](https://clear.ml/docs/latest/docs/hyperdatasets/annotations#frame-labels) |\
| Shift + Tab | Previous annotation (use after clicking an annotation) |\
\
**Mode-specific annotation controls**\
\
| Control | Mode | Action |\
| --- | --- | --- |\
| Hold Shift | Key points (![Key points mode](https://clear.ml/docs/latest/icons/ico-keypoint-icon-purple.svg)) | While holding Shift, add new points to the ROI by left clicking, and move a single point by dragging it with your mouse |\
| Enter | Key points (![Key points mode](https://clear.ml/docs/latest/icons/ico-keypoint-icon-purple.svg)) | Complete annotation |\
| Esc | Key points (![Key points mode](https://clear.ml/docs/latest/icons/ico-keypoint-icon-purple.svg)), Polygon (![Polygon mode](https://clear.ml/docs/latest/icons/ico-polygon-icon-purple.svg)) | Cancel annotation process |\
\
### Viewing and Editing Frames [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_frames/\#viewing-and-editing-frames "Direct link to Viewing and Editing Frames")\
\
**To view / edit a frame in the frame editor**\
\
1. Locate your frame by applying [frame filters](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_versioning#frame-filtering).\
2. Click the frame thumbnail. The frame editor appears.\
3. Do any of the following:\
   - View frame details, including:\
     - Frame file path\
     - Dimensions of the image or video\
     - Frame details\
     - Frame metadata\
     - Annotations\
       - Frame objects - Labeled Regions of Interest, with confidence levels and custom metadata per frame object.\
       - Frame labels - Labels applied to the entire frame, not a region in the frame.\
   - Optionally, filter annotations by confidence level using the **Minimum confidence** slider.\
   - Add, change, and delete [annotations](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_frames/#annotations) and [frame metadata](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_frames/#frame-metadata).\
\
Saving Frame Changes\
\
To save frames changes at any time, click **SAVE** (below the annotation list area).\
\
### Viewing FrameGroups [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_frames/\#viewing-framegroups "Direct link to Viewing FrameGroups")\
\
Viewing and editing frames in a FrameGroup is similar to viewing and editing SingleFrames.\
Click the FrameGroup in the Hyper-Dataset. In the frame viewer, select SingleFrame to view / modify from\
a dropdown list in the **Current Source** section.\
\
![Frame dropdown menu in FrameGroup](https://clear.ml/docs/latest/assets/images/framegroup_01-5a72588e76445be80f58260844e32956.png#light-mode-only)![Frame dropdown menu in FrameGroup](https://clear.ml/docs/latest/assets/images/framegroup_01_dark-f45abc1c6df68ab2796d9e44619b2193.png#dark-mode-only)\
\
If an annotation applies to all frames in a FrameGroup, it is displayed with a `Multi Source` indicator:\
\
![Multi-source ROI](https://clear.ml/docs/latest/assets/images/multi_source_annotation-21ba1e577cf65009728c0a17c4b01720.png#light-mode-only)![Multi-source ROI](https://clear.ml/docs/latest/assets/images/multi_source_annotation_dark-674eab33a2dbe4a68e71d6de25e1858f.png#dark-mode-only)\
\
## Masks [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_frames/\#masks "Direct link to Masks")\
\
Use the **MASKS** panel to select which masks to apply over the frame.\
\
To view / hide a specific mask, click ![Eye Show](https://clear.ml/docs/latest/icons/ico-show.svg).\
In order to view / hide all masks, click **Show all** / **Hide all**.\
\
Masks are applied over the image either by pixel segmentation or as an alpha channel:\
\
- ![Pixel segmentation mode](https://clear.ml/docs/latest/icons/ico-segmentation.svg) Pixel\
segmentation - Class labels are mapped onto the mask according to their pixel value definitions, and each\
class is assigned a unique color.\
- ![Alpha channel mode](https://clear.ml/docs/latest/icons/ico-alpha-mask.svg) Alpha\
channel - Mask pixel values are translated to transparency. Additionally, a color can be applied to the mask to help\
distinguish multiple masks. Click ![Alpha color](https://clear.ml/docs/latest/icons/ico-mask-color-preview.svg) to select\
a color.\
\
To adjust the transparency of a mask, use its opacity slider.\
\
### Labels [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_frames/\#labels "Direct link to Labels")\
\
The **Active mask labels** section displays the color mapping of the mask labels.\
The panel presents labels only from masks that are currently displayed.\
\
**To modify a label's color and opacity:**\
\
1. Click the colored circle next to the label\
2. Select a new color\
3. Adjust the opacity slider\
4. Click **OK**\
\
## Annotations [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_frames/\#annotations "Direct link to Annotations")\
\
### Adding Frame Objects (Regions of Interest) [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_frames/\#adding-frame-objects-regions-of-interest "Direct link to Adding Frame Objects (Regions of Interest)")\
\
Annotate images and video by labeling regions of interest in Dataset version frames. You can create new annotations\
and copy existing annotations.\
\
#### Creating New Frame Objects [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_frames/\#creating-new-frame-objects "Direct link to Creating New Frame Objects")\
\
To draw a new annotation:\
\
1. Click one of the following modes to choose what annotation to create:\
\
\
   - ![Rectangle mode icon](https://clear.ml/docs/latest/icons/ico-rectangle-icon-purple.svg) \- Rectangle mode:\
     Click then drag the cursor to create a rectangle annotation on the frame.\
\
   - ![Ellipse mode icon](https://clear.ml/docs/latest/icons/ico-ellipse-icon-purple.svg) \- Ellipse mode:\
     Click then drag the cursor to create an ellipse annotation on the frame.\
\
   - ![Polygon mode icon](https://clear.ml/docs/latest/icons/ico-polygon-icon-purple.svg) \- Polygon mode:\
     Each click sets polygon vertices on the frame. Click again on the initial vertex to close the polygon.\
\
   - ![Key points mode icon](https://clear.ml/docs/latest/icons/ico-keypoint-icon-purple.svg) \- Key points mode:\
     Each click adds a keypoint to the frame. After clicking the last keypoint, click ![Check mark](https://clear.ml/docs/latest/icons/ico-save.svg)\
     or `Enter` to save the annotation. Click `Esc` to cancel the annotation.\
\
\
A new annotation is created.\
\
2. In the newly created annotation, select or type-in the labels for this annotation.\
\
\
You can use the **Default ROI Label(s)** list to automatically set labels to all new annotations.\
\
Annotation color\
\
Each annotation label is automatically assigned a color based on its value. The annotation color is automatically\
calculated based on the colors of its labels.\
\
Click the color circle in the label name to manually set the label's color.\
\
![Set label color](https://clear.ml/docs/latest/assets/images/annotation_label_color-0227abfe6bffb3b95eb43665741d0321.png#light-mode-only)![Set label color](https://clear.ml/docs/latest/assets/images/annotation_label_color_dark-013d2fe58f0e374b96940483d209d7f5.png#dark-mode-only)\
\
Click the color circle in the annotation header to manually set the annotation’s color and its opacity.\
\
![Set annotation color and opacity](https://clear.ml/docs/latest/assets/images/annotation_label_opacity-c63c03383def033b34b49bd3eeffd1a5.png#light-mode-only)![Set annotation color and opacity](https://clear.ml/docs/latest/assets/images/annotation_label_opacity_dark-1e661a6f5ac284226277588b4fdefd1d.png#dark-mode-only)\
\
#### Copying Frame Objects [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_frames/\#copying-frame-objects "Direct link to Copying Frame Objects")\
\
You can copy existing annotations, and paste them to any frame of your choice:\
\
1. Click the annotation or bounded area in the frame.\
2. Click ![Copy annotation](https://clear.ml/docs/latest/icons/ico-copy-to-clipboard.svg)\
(copy annotation).\
3. Navigate to the frame of your choice (you can remain in the same frame).\
4. Click **PASTE**. The new annotation appears in the same location as the one you copied. You can paste the annotation\
multiple times.\
\
Copy all annotations in a frame by clicking the **COPY ALL** button.\
\
### Annotation Actions [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_frames/\#annotation-actions "Direct link to Annotation Actions")\
\
The following table describes the actions that can be performed on existing annotations. The frame editor automatically\
saves changes when you move to another frame using the frame navigation controls\
(![Next frame icon](https://clear.ml/docs/latest/icons/ico-arrow-right.svg), ![Jump to next unfiltered annotation](https://clear.ml/docs/latest/icons/ico-skip-next.svg), ![Jump forwards icon](https://clear.ml/docs/latest/icons/ico-skip-forward.svg), ![Previous frame icon](https://clear.ml/docs/latest/icons/ico-arrow-left.svg), ![Jump to previous unfiltered annotation](https://clear.ml/docs/latest/icons/ico-skip-previous.svg), ![Jump backwards icon](https://clear.ml/docs/latest/icons/ico-skip-backward.svg),\
or the arrow keys on the keyboard). Closing the frame editor will prompt you to save any changes.\
\
| Icon (when applicable) | Action | Description |\
| --- | --- | --- |\
|  | Move annotation | Click on a bounded area and drag it. |\
|  | Resize annotation | Select an annotation, then click on a bounded area's vertex and drag it. |\
| ![edit metadata](https://clear.ml/docs/latest/icons/ico-metadata.svg) | Edit metadata | Hover over an annotation in the list and click the icon to open the edit window. Input the metadata dictionary in JSON format. This metadata is specific to the selected annotation, not the entire frame. |\
| ![Lock annotation](https://clear.ml/docs/latest/icons/ico-lock-open.svg) | Lock / Unlock annotation | Click the button on a specific annotation to make it uneditable. You can also click the button on top of the annotations list to lock all annotations in the frame. |\
| ![Trash](https://clear.ml/docs/latest/icons/ico-trash.svg) | Delete annotation | Click the annotation or bounded area in the frame and then click the button to delete the annotation. |\
| ![Eye Show All](https://clear.ml/docs/latest/icons/ico-show.svg) | Show/hide annotations | Click the button on a specific annotation to hide it. You can also click the button on top of the annotations list to hide all annotations. Hidden annotations can't be modified. |\
|  | Delete label | In the relevant annotation, click **x** on the label you want to remove. |\
\
### Frame Labels [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_frames/\#frame-labels "Direct link to Frame Labels")\
\
You can add labels which describe the whole frame, with no specific coordinates.\
\
**To add frame labels:**\
\
1. Expand the **FRAME LABELS** area (below **OBJECTS**)\
2. Click **\+ Add new**\
3. Enter a label(s)\
\
## Frame Metadata [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_frames/\#frame-metadata "Direct link to Frame Metadata")\
\
**To edit frame metadata:**\
\
1. Expand the **FRAMEGROUP METADATA** area\
2. Click edit ![edit metadata](https://clear.ml/docs/latest/icons/ico-metadata.svg)\
which will open an editing window\
3. Modify the metadata dictionary in JSON format\
\
- [Frame Viewer](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_frames/#frame-viewer)\
  - [Viewing FrameGroup Data](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_frames/#viewing-framegroup-data)\
  - [Frame Viewer Controls](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_frames/#frame-viewer-controls)\
  - [Viewing and Editing Frames](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_frames/#viewing-and-editing-frames)\
  - [Viewing FrameGroups](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_frames/#viewing-framegroups)\
- [Masks](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_frames/#masks)\
  - [Labels](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_frames/#labels)\
- [Annotations](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_frames/#annotations)\
  - [Adding Frame Objects (Regions of Interest)](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_frames/#adding-frame-objects-regions-of-interest)\
  - [Annotation Actions](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_frames/#annotation-actions)\
  - [Frame Labels](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_frames/#frame-labels)\
- [Frame Metadata](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_frames/#frame-metadata)