---
url: "https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_versioning/"
title: "Dataset Versions | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_versioning/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

Enterprise Feature

Hyper-Datasets are available under the ClearML Enterprise plan.

Use the Dataset versioning WebApp (UI) features for viewing, creating, modifying, and
deleting [Dataset versions](https://clear.ml/docs/latest/docs/hyperdatasets/dataset#dataset-versioning).

![Dataset versions page](https://clear.ml/docs/latest/assets/images/dataset_versions-611d16ad40b9b1f85f07cdba51b5e8ea.png#light-mode-only)![Dataset versions page](https://clear.ml/docs/latest/assets/images/dataset_versions_dark-a7cfd566f7f8e1f646f51be94f02811a.png#dark-mode-only)

## Dataset Version History [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_versioning/\#dataset-version-history "Direct link to Dataset Version History")

The WebApp (UI) presents your dataset version structure in tree view ![Tree view](https://clear.ml/docs/latest/icons/ico-tree-view.svg)
or list view ![List view](https://clear.ml/docs/latest/icons/ico-list-view.svg).

The tree view shows the lineage of the dataset's versions.

![Versions tree view](https://clear.ml/docs/latest/assets/images/dataset_simple_adv_02-3920f1ec8465d522dcf8809833819714.png#light-mode-only)![Versions tree view](https://clear.ml/docs/latest/assets/images/dataset_simple_adv_02_dark-ada56420ebcfc28f6ea62f3852c1312f.png#dark-mode-only)

The list view lists the dataset's versions chronologically by last update time.

![Versions list view](https://clear.ml/docs/latest/assets/images/dataset_simple_adv_01-db45162c2b350d5a84a3bc1c0b98fd79.png#light-mode-only)![Versions list view](https://clear.ml/docs/latest/assets/images/dataset_simple_adv_01_dark-907e83636452500bda760093a71d11f8.png#dark-mode-only)

Click ![Sort order](https://clear.ml/docs/latest/icons/ico-sort.svg) to order the
dataset versions in ascending or descending order based on their last update time.

Use the search bar to find specific versions. You can query by version name, version description, or version ID. The search returns
all versions that match the query.

In tree view, parent versions that do not match the query where a child version does appear in a muted color.

![Dataset version search](https://clear.ml/docs/latest/assets/images/hyperdataset_search_2-ce4b840ed65a16b94db377a8c6570ffa.png#light-mode-only)![Dataset version search](https://clear.ml/docs/latest/assets/images/hyperdataset_search_2_dark-68a443ad07c86870eca30181e087f40a.png#dark-mode-only)

### Version Actions [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_versioning/\#version-actions "Direct link to Version Actions")

Access dataset version actions, by right-clicking a version, or through the menu button ![Dot menu](https://clear.ml/docs/latest/icons/ico-dots-v-menu.svg) (available on hover).

- **Rename** \- Change the version's name
- **Create New Version** \- Creates a child version of a _Published_ dataset version. The new version is created in a _draft_
state, and inherits all the parent version's frames. The template for the default value of new dataset version names
can be set in [**Settings > Hyper-Dataset New Version Name Template**](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_ui_customization#hyper-dataset-new-version-name-template).
- **Delete** \- Delete the version. Only _Draft_ versions can be deleted.
- **Publish** \- Make a _Draft_ version read-only to preserve its contents.

Publishing versions

When publishing a version, you can create an additional working copy. The new version is created in a _draft_ state, and
inherits all the published version's frames. By default, the newly created working copy inherits the original version's
name, while the published original version is automatically renamed to reflect its published state. The template for
the default value of published version names can be set in [**Settings > Hyper-Dataset New Version Name Template**](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_ui_customization#hyper-dataset-new-version-name-template).

![Publish version modal](https://clear.ml/docs/latest/assets/images/hyperdataset_publish_version-b171adb3aa85a1e67ea91ae03a51b92a.png#light-mode-only)![Publish version modal](https://clear.ml/docs/latest/assets/images/hyperdataset_publish_version_dark-f37f0729b103a88925f8e897891db26d.png#dark-mode-only)

## Version Data [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_versioning/\#version-data "Direct link to Version Data")

A selected dataset version's information and contents are presented on the main section of the page, to the right of
the dataset's version list.

The version information is presented in the following tabs:

- [Frames](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_versioning/#frames)
- [Statistics](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_versioning/#statistics)
- [Metadata](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_versioning/#metadata)
- [Info](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_versioning/#info)

## Frames [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_versioning/\#frames "Direct link to Frames")

The **Frames** tab displays the contents of the selected dataset version.

View the version's frames as thumbnail previews or in a table. Use the view toggle to switch between thumbnail
view ![thumbnail view](https://clear.ml/docs/latest/icons/ico-grid-view.svg) and
table view ![table view](https://clear.ml/docs/latest/icons/ico-table-view.svg).

Use the thumbnail view for a visual preview of the version's frames. You can increase ![Zoom in](https://clear.ml/docs/latest/icons/ico-zoom-in.svg)
and decrease ![Zoom out](https://clear.ml/docs/latest/icons/ico-zoom-out.svg) the size of
the previews.

![Frame browser thumbnails](https://clear.ml/docs/latest/assets/images/frame_browser_thumbnails-3a57beaad76639c55aafa6e82e347e79.png#light-mode-only)![Frame browser thumbnails](https://clear.ml/docs/latest/assets/images/frame_browser_thumbnails_dark-aa33086b3c1abe6ee061236607ca8662.png#dark-mode-only)

Use the table view to list the version's frames in a customizable table. Click ![Setting Gear](https://clear.ml/docs/latest/icons/ico-settings.svg)
for column customization options.

![Frame browser list](https://clear.ml/docs/latest/assets/images/frame_browser_list-44bfb66b24176c4ac937f84d82d1bb64.png#light-mode-only)![Frame browser list](https://clear.ml/docs/latest/assets/images/frame_browser_list_dark-78a16b44b844519004bf27546abbe250.png#dark-mode-only)

The dataset version's frames can be filtered by multiple criteria. The resulting frames can be [exported as a JSON file](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_versioning/#exporting-frames).

To view the details of a specific frame, click on its preview, which will open the [Frame Viewer](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_frames#frame-viewer).

### Frame Filtering [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_versioning/\#frame-filtering "Direct link to Frame Filtering")

A combination of ROI, frame, and source rules can be specified to apply more elaborate and specific
filters.

**To apply filters:**

1. In the **FRAMES** tab, click ![Advanced filters](https://clear.ml/docs/latest/icons/ico-advanced-filters.svg) ( **Filters**).
2. In a **FRAME FILTER**, create one of the following rules:

   - ROI rule - Use "Include" and "Exclude" conditions to match frames according to an ROI label. If the "Include"
     condition is used, frames match the rule if they contain at least one annotation object (ROI) with ALL labels in the
     rule. If the "Exclude" condition is used, frames match the rule if NONE of their ROIs contain the label. Multiple ROI
     rules in the same filter are evaluated independently against all frame ROIs. Meaning, a frame will match the filter
     if it contains at least one annotation matching each rule, even if the annotations are in different ROIs. Click ![Lucene query mode](https://clear.ml/docs/latest/icons/ico-code.svg)
     to explicitly specify your rule with Lucene
   - Frame rule - Query frame metadata. Enter a Lucene query of frame metadata fields in the format `meta.<key>:<value>`
     (can use AND, OR, and NOT operators).
   - Source rule - Query frame source information. Enter a Lucene query of frame metadata fields in the format
     `sources.<key>:<value>` (can use AND, OR, and NOT operators).

A frame filter can contain a number of rules. For each frame filter, the rules are applied with a logical AND operator. For example, the dataset version in the image below has one filter. "Frame Filter 1" has two rules:

1. ROI rule - the frame must include an ROI with the `cat` label
2. Source rule - the frames must be 640 pixels wide.

The returned frames are those that match the first rule AND the second rule within the frame filter.

![Multiple rules filter](https://clear.ml/docs/latest/assets/images/multiple_rules-a26d590aa3ddf7f43a3418b54e7dec85.png#light-mode-only)![Multiple rules filter](https://clear.ml/docs/latest/assets/images/multiple_rules_dark-9e5fb2fb56b11b68e41e21190f20e9fc.png#dark-mode-only)

Create additional frame filters by clicking ![Add new](https://clear.ml/docs/latest/icons/ico-add.svg).
Multiple frame filters are applied with a logical OR operator.

For example, the dataset version in the image below has two frame filters. "Frame Filter 1" has the same two rules
described in the example above. "Frame Filter 2" specifies an ROI rule for the frame to contain an ROI with the label
`dog`. So the frames returned are those that match ALL of Frame Filter 1's rules OR ALL of Frame Filter 2's rules.

![Multiple filters](https://clear.ml/docs/latest/assets/images/multiple_filters-061868528aef81654e88b50bf86dc90f.png#light-mode-only)![Multiple filters](https://clear.ml/docs/latest/assets/images/multiple_filters_dark-132bf25e389b42808cf0863ecb082c7e.png#dark-mode-only)

To clear all filters click ![Clear filters](https://clear.ml/docs/latest/icons/ico-filter-reset.svg).

### Vector Search [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_versioning/\#vector-search "Direct link to Vector Search")

**Vector search** finds the most similar frames to a specific reference vector. Frames are evaluated based on vector
embeddings that have been registered to them through the SDK.

To find the frames most similar to one of the frames in the version:

1. Hover over the desired frame
2. Click ![Dot menu](https://clear.ml/docs/latest/icons/ico-dots-v-menu.svg)
3. Select `Find Nearest Frames By`
4. Choose the frame’s vector field that will be compared against the reference vector
5. Input the [search configuration](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_versioning/#search-configuration)

To find the frames most similar to an arbitrary vector:

1. In the **FRAMES** tab, click ![Filter](https://clear.ml/docs/latest/icons/ico-filter-off.svg) (filters)
2. Under **Vector search**, enter the vector values under **Reference vector**.
3. Input the [search configuration](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_versioning/#search-configuration)

#### Search Configuration [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_versioning/\#search-configuration "Direct link to Search Configuration")

- **Vector field** \- Select the FrameGroup's vector field that will be compared against the reference vector.
- **Number of neighbors** \- Choose how many nearest neighbors to show.
- **Search strategy**\- Either of:

  - `KNN` (K-nearest neighbors)
  - `HNSW` (Hierarchical Navigable Small World) - Available with cosine similarity only.
- **Similarity function** \- Select `Cosine similarity`, `Euclidean distance`, or `Dot product`.

After entering the search configuration, click **Apply**.

The frames are returned in order of their similarity to the reference vector. The calculated similarity is displayed on
each frame preview:

![Vector Search](https://clear.ml/docs/latest/assets/images/vector_search-f18f58dd781bf6f374e79d512e2dc8f6.png#light-mode-only)![Vector Search](https://clear.ml/docs/latest/assets/images/vector_search_dark-e32f80d1a3018d1caf921663016f4e05.png#dark-mode-only)

Vector search results adhere to configured frame filters. For example, if you filter for frames containing the ROI label
`cat`, the search will return only the nearest neighbors among frames with that ROI.

### Filtering Examples [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_versioning/\#filtering-examples "Direct link to Filtering Examples")

ROI Rules

- Create one ROI rule for the `teddy bear` label. Only frame containing at least one ROL labeled `teddy bear` match the
filter

![Adding an ROI rule](https://clear.ml/docs/latest/assets/images/frame_filtering_03-09cd7fe5c70be5ed5a0b862f7103cd1f.png#light-mode-only)![Adding an ROI rule](https://clear.ml/docs/latest/assets/images/frame_filtering_03_dark-63ee89cb7aedccfada14ed9228757a3a.png#dark-mode-only)

- In the ROI rule, add a second label. Add `partially_occluded`. Only frames containing at least one ROI labeled as both
`teddy bear` and `partially_occluded` match the filter.

![Add label to ROI rule](https://clear.ml/docs/latest/assets/images/frame_filtering_04-755c53ac87c53021e2d47327790663a8.png#light-mode-only)![Add label to ROI rule](https://clear.ml/docs/latest/assets/images/frame_filtering_04_dark-3ad451486cf7654e11c4143116dd6fb6.png#dark-mode-only)

- By opening a frame in the frame viewer, you can see an ROI labeled with both.

![Labeled ROIs in frame viewer](https://clear.ml/docs/latest/assets/images/frame_filtering_05-c99e773fff5e453133d1410bf0914bc8.png#light-mode-only)![Labeled ROIs in frame viewer](https://clear.ml/docs/latest/assets/images/frame_filtering_05_dark-5d79c4d6180022bbedaa1ada984cf492.png#dark-mode-only)

- To find frames that contain multiple ROIs, each with a different label, use separate ROI rules. Create an ROI rule for
the `teddy bear` label and, in the same filter, add another ROI rule for the `person` label. This will return all
frames that include at least one ROIs with a `person` label AND at least one (other) ROI with a `teddy bear` label.

![Add multiple ROI Rules](https://clear.ml/docs/latest/assets/images/frame_filtering_06-7e45bcc672a68d830989fef04592e62b.png#light-mode-only)![Add multiple ROI Rules](https://clear.ml/docs/latest/assets/images/frame_filtering_06_dark-b13d225b9dfa8237d499d26a7fcc527c.png#dark-mode-only)

- You can also exclude certain ROI labels. Create an ROI rule to include `teddy bear` and, in the same filter, an ROI
rule to exclude `person`. This will return all frames that include at least one ROI with the label `teddy bear` AND have
NO ROI with the `person` label

![Add Exclude ROI Rule](https://clear.ml/docs/latest/assets/images/frame_filtering_07-74a7a797aea4207c2036081fac46a781.png#light-mode-only)![Add Exclude ROI Rule](https://clear.ml/docs/latest/assets/images/frame_filtering_07_dark-088ad394e7a7bbbedd143c87a7d34925.png#dark-mode-only)

Frame Rules: Metadata

Filter by metadata using Lucene queries.

- Add a frame rule to filter by the metadata key `dangerous` for the value of `yes`.

![Filter by metadata](https://clear.ml/docs/latest/assets/images/frame_filtering_08-6d97999a1db3cd174423500b1f359e56.png#light-mode-only)![Filter by metadata](https://clear.ml/docs/latest/assets/images/frame_filtering_08_dark-0e5407bf956bc0240351a56748905e95.png#dark-mode-only)

- Open a frame in the frame viewer to see its metadata.

![Frame metadata in frame viewer](https://clear.ml/docs/latest/assets/images/frame_filtering_09-ad4156038f990aff3bb3553906432ce2.png#light-mode-only)![Frame metadata in frame viewer](https://clear.ml/docs/latest/assets/images/frame_filtering_09_dark-85e256870cdb57275f3b45b7a750b2c9.png#dark-mode-only)

Frame Rules: Date and Time Fields

If your dataset includes a metadata field that stores date and time information, you can filter
based on date ranges or specific time intervals.

Filter by date/time metadata fields using Lucene queries.

- **Data range filter**
  - Add a frame rule to filter by the metadata key `updated` for the value of `[2024-10-20 TO 2024-10-20]`. The query
    will match all frames where the `updated` value matches October 20th 2024. Use the format `meta.<field_name>.[YYYY-MM-DD TO YYYY-MM-DD]`.

    ![Filter by date](https://clear.ml/docs/latest/assets/images/frame_filtering_11-bdeadd886b73529cedd1bd30f5059564.png#light-mode-only)![Filter by date](https://clear.ml/docs/latest/assets/images/frame_filtering_11_dark-e3aa2646d8f267f0a663fcbeb0ca883d.png#dark-mode-only)

  - Open a frame in the frame viewer to see its metadata.

    ![Frame date metadata in frame viewer](https://clear.ml/docs/latest/assets/images/frame_filtering_12-5fad0bcc22766169952a03fa9ed6488a.png#light-mode-only)![Frame date metadata in frame viewer](https://clear.ml/docs/latest/assets/images/frame_filtering_12_dark-26a49454287d416b2da1b4e2885ca324.png#dark-mode-only)
- **Time interval filter**
  - Add a frame rule to filter by the metadata key `updated` for the value of `[2024-10-20T08:00:00 TO 2024-10-20T09:00:00]`.
    The query will match all frames where the updated value is between 08:00 and 09:00 on October 20th 2024.
    Use the format `meta.<field_name>.[YYYY-MM-DDThh:mm:ss TO YYYY-MM-DDThh:mm:ss]`.

    ![Filter by datetime](https://clear.ml/docs/latest/assets/images/frame_filtering_13-c5c751fc65779107163d251fb4a0c0e6.png#light-mode-only)![Filter by datetime](https://clear.ml/docs/latest/assets/images/frame_filtering_13_dark-b2180755e80106dc65bda86ffb4abd36.png#dark-mode-only)

  - Open a frame in the frame viewer to see its metadata.

    ![Frame datetime metadata in frame viewer](https://clear.ml/docs/latest/assets/images/frame_filtering_14-afe11270d7bb80086b10b998e701feed.png#light-mode-only)![Frame datetime metadata in frame viewer](https://clear.ml/docs/latest/assets/images/frame_filtering_14_dark-70274c91371fb02ed0521acaa7adf3ea.png#dark-mode-only)

Source Rules

Filter by sources using Lucene queries.

- Add a source rule to filter for source URIs with wildcards.

![Filter by source](https://clear.ml/docs/latest/assets/images/frame_filtering_10-eea4683ef98fd752d1c09b8701640637.png#light-mode-only)![Filter by source](https://clear.ml/docs/latest/assets/images/frame_filtering_10_dark-cf97a784228e26ea7b3c859697de29f8.png#dark-mode-only)

Lucene queries can also be used in ROI label filters and frame rules.

### Sorting Frames [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_versioning/\#sorting-frames "Direct link to Sorting Frames")

Sort the dataset version’s frames by any of the following attributes:

- ID
- Last update time
- Dimensions (height)
- Timestamp
- Context ID
- Metadata key - Click `+ Metadata Key` and select the desired key for sorting

Click ![Sort order](https://clear.ml/docs/latest/icons/ico-sort.svg) to toggle between ascending and descending sort orders.

![Dataset frame sorting](https://clear.ml/docs/latest/assets/images/dataset_frame_sorting-1c8a9050bb541650a9e0aa2c5e86e9ca.png#light-mode-only)![Dataset frame sorting](https://clear.ml/docs/latest/assets/images/dataset_frame_sorting_dark-0cd87a9d82f8f381e330b2bb7ae5cd51.png#dark-mode-only)

### Exporting Frames [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_versioning/\#exporting-frames "Direct link to Exporting Frames")

To export (download) the filtered frames as a JSON file, click ![Menu](https://clear.ml/docs/latest/icons/ico-bars-menu.svg) \> **EXPORT FRAMES**.

### Frame Browser Configuration [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_versioning/\#frame-browser-configuration "Direct link to Frame Browser Configuration")

Click ![Menu](https://clear.ml/docs/latest/icons/ico-bars-menu.svg) to open the
frame browser configuration settings.

![Frame browser config menu](https://clear.ml/docs/latest/assets/images/frame_browser_menu-5f8050e3886463fdfee895b008f86187.png#light-mode-only)![Frame browser config menu](https://clear.ml/docs/latest/assets/images/frame_browser_menu_dark-4f73dcb093e00ecd46f96b92bc6a2cc0.png#dark-mode-only)

#### Grouping Previews [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_versioning/\#grouping-previews "Direct link to Grouping Previews")

Use the **Grouping** menu to set how to display frames that share a common property:

- **Split Preview** \- Show a separate preview for each individual FrameGroup
- **Group by URL** \- Show a single preview for all FrameGroups with the same context ID. For example, users can set the
same `context_id` to multiple FrameGroups that represent frames in a single video.
- **Sample by Property** \- Specify a frame or ROI property whose value to group frames by and set the number of frames
to preview for each group. For example, in the image below, frames are grouped by ROI labels. Each group displays five
samples of frames that contain an ROI with the same label.

![Sample by property](https://clear.ml/docs/latest/assets/images/dataset_sample_by_roi_property-e4e2411db0f5683dd86f0b428df7441c.png#light-mode-only)![Sample by property](https://clear.ml/docs/latest/assets/images/dataset_sample_by_roi_property_dark-139a8313b5e96c992b27d7917c2e65f1.png#dark-mode-only)

**To sample by property:**

1. In the **Grouping** menu, click **Sample by Property**

2. In the **Sample by Property** modal, input the following:


   - Select the Property type:
     - ROI - Properties associated with the frame ROIs (e.g. ROI label names, IDs, confidence, etc.)
     - Frame - Properties associated with the frames (e.g. update time, metadata, timestamp, etc.)
   - Property name - Property whose value to group the frames by
   - Sample size - Number of frames to preview for each group
   - ROI match query ( _For grouping by ROI property only_) \- A Lucene query to filter which of a frame's ROIs
     to use in grouping by their properties. For example, in a Hyper-Dataset where ROIs have object labels and type labels,
     view a sample of frames with different types of the same object by grouping frames according to `label.keyword`
     with a match query for the object of interest.


![Sample by Property modal](https://clear.ml/docs/latest/assets/images/sample_by_property_modal-cc142b7a3bc608851509995b24933b29.png#light-mode-only)![Sample by Property modal](https://clear.ml/docs/latest/assets/images/sample_by_property_modal_dark-47fd99ee72b69c3ef5beb5e1d9d91a9a.png#dark-mode-only)

The image below shows a sample of 3 frames which have ROIs of each type (`pedestrian`, `rider`, `sitting`) of `person`.

![ROI Match Query](https://clear.ml/docs/latest/assets/images/roi_match_query-6fdba5674dd4c208274c01999b34bd37.png#light-mode-only)![ROI Match Query](https://clear.ml/docs/latest/assets/images/roi_match_query_dark-b58c86801a2855756a4d73ea22ac4901.png#dark-mode-only)

Property N/A group

If there are frames which have no value for the grouped by property, a sample of them will be provided as a final
group. If you sample according to an ROI property, this group will NOT include frames that have no ROIS at all.

3. Click **Save**


Once saved, whenever you select the **Sample by Property** option in the **Grouping** menu, the frame will be grouped
according to the previously configured setting.

**To modify the grouping property:**

1. Hover over **Sample by Property**
2. Click ![Edit pencil](https://clear.ml/docs/latest/icons/ico-edit.svg)
3. Modify the **Sample by Property** configuration
4. Click **Save**

#### Preview Source [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_versioning/\#preview-source "Direct link to Preview Source")

When using multi-source FrameGroups, users can choose which of the FrameGroups' sources will be displayed as the preview.

Select a source from the **Current Source** menu.
Choose the `Default preview source` option to present the first available source for each frame (sources are retrieved in ASCIIbetical order).

Choose the `All sources` option to present all the FrameGroup’s sources in a grid. In this view, the annotation panel
shows annotations grouped by their respective sources. Additionally, annotation tools (e.g. create/delete/modify
annotations) are not available in this view.

![All sources preview](https://clear.ml/docs/latest/assets/images/preview_all_sources-02fef7016df4ec865eca54166fb5daf2.png#light-mode-only)![All sources preview](https://clear.ml/docs/latest/assets/images/preview_all_sources_dark-cfaadf768b6c71283cbc82dcd1e0ad77.png#dark-mode-only)

Unavailable Source

If a FrameGroup doesn't have the selected preview source, the preview displays the "Source not available" message.

## Statistics [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_versioning/\#statistics "Direct link to Statistics")

The **Statistics** tab allows exploring frame and ROI property distribution across a Hyper-Dataset version:

1. Query the frames to include in the statistics calculations using [frame filters](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_versioning/#frame-filtering).
If no filter is applied, all frames in the dataset version will be included in the calculation.
2. Select the property whose distribution should be calculated
   - Select the property **Type**:

     - **ROI** \- Frame ROI properties (e.g. ROI label, ID, confidence, etc.). This will calculate the distribution of
       the specified property across all ROIs in the version's frames.
     - **Frame** \- Frames properties (e.g. update time, metadata keys, timestamp, etc.)
   - Input the **Property** key (e.g. `meta.location`)
   - If **ROI** property was selected, you can also limit the scope of ROIs included in the calculation with the
     **Count ROIs matching** filter: Input a Lucene query to specify which ROIs to count
3. Click **Apply** to calculate the statistics

For example, calculating the distribution for the `label` ROI property, specifying `rois.confidence: 1` for ROI matching
will show the label distribution across only ROIs with a confidence level of 1.

![Distribution by ROI property](<Base64-Image-Removed>)![Distribution by ROI property](<Base64-Image-Removed>)

By default, the ROI label distribution across the entire Hyper-Dataset version is shown.
The tab displays the following information

- Object counts:
  - Number of annotations matching specification
  - Number of annotated frames in the current frame filter selection
  - Total number of frames in the current frame filter selection
- Each property is listed along with its number of occurrences in the current frame filter selection
- The pie chart visualizes this distribution. Hover over a chart segment and its associated property and count will
appear in a tooltip and its usage percentage will appear at the center of the chart.

![Version label statistics](https://clear.ml/docs/latest/assets/images/dataset_version_statistics-73e88a7f7e57b9cba3fdbf709f933368.png#light-mode-only)![Version label statistics](https://clear.ml/docs/latest/assets/images/dataset_version_statistics_dark-89940803ab52bef053f93c6c0a24db01.png#dark-mode-only)

## Metadata [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_versioning/\#metadata "Direct link to Metadata")

The **Metadata** tab presents any additional metadata that has been attached to the dataset version.

**To edit a version's metadata,**

1. Hover over the metadata box and click **EDIT**
2. Edit the section contents (JSON format)
3. Click **OK**

![Version metadata](https://clear.ml/docs/latest/assets/images/dataset_version_metadata-d7e3837b9172e3515e4d2e45c6181820.png#light-mode-only)![Version metadata](https://clear.ml/docs/latest/assets/images/dataset_version_metadata_dark-bee8500fb436afb585de218e6c77c6d9.png#dark-mode-only)

## Info [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_versioning/\#info "Direct link to Info")

The **Info** tab presents a version's general information:

- Version ID
- Version name
- Dataset ID
- Dataset name
- Dataset description
- Dataset tags
- Status ( _Draft_ or _Published_)
- Creating user
- Version update time
- Number of frames
- Percentage of annotated frames
- Version description (editable, hover over element and click ![Edit pencil](https://clear.ml/docs/latest/icons/ico-edit.svg))

![Version info](https://clear.ml/docs/latest/assets/images/dataset_version_info_panel-c5d35d34d6debb581c5f27fbffb5e04e.png#light-mode-only)![Version info](https://clear.ml/docs/latest/assets/images/dataset_version_info_panel_dark-416a43692024685ab8637e37c9bd4433.png#dark-mode-only)

- [Dataset Version History](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_versioning/#dataset-version-history)
  - [Version Actions](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_versioning/#version-actions)
- [Version Data](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_versioning/#version-data)
- [Frames](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_versioning/#frames)
  - [Frame Filtering](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_versioning/#frame-filtering)
  - [Vector Search](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_versioning/#vector-search)
  - [Filtering Examples](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_versioning/#filtering-examples)
  - [Sorting Frames](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_versioning/#sorting-frames)
  - [Exporting Frames](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_versioning/#exporting-frames)
  - [Frame Browser Configuration](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_versioning/#frame-browser-configuration)
- [Statistics](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_versioning/#statistics)
- [Metadata](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_versioning/#metadata)
- [Info](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_versioning/#info)