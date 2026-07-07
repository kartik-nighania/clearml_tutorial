---
url: "https://clear.ml/docs/latest/docs/webapp/datasets/webapp_dataset_viewing/"
title: "Dataset Details | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/webapp/datasets/webapp_dataset_viewing/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

SDK version compatibility

The datasets page shows datasets created with `clearml` v1.6 or newer.

Datasets created with earlier versions of `clearml` are available in their original project.

The dataset page lists the dataset's versions. For a selected version, the **Dataset Version Panel** shows its lineage
in graph form.

![Dataset lineage](https://clear.ml/docs/latest/assets/images/webapp_dataset_lineage-5d9e8fa16dac8660dd100f4a63ff93c8.png#light-mode-only)![Dataset lineage](https://clear.ml/docs/latest/assets/images/webapp_dataset_lineage_dark-c82dc3525082dd2292f7db07c1c718e4.png#dark-mode-only)

Each node in the graph represents a dataset version, and shows the following details:

![Dataset node info](https://clear.ml/docs/latest/assets/images/webapp_dataset_node-0fa137190fad65a914842d5b476a70e7.png#light-mode-only)![Dataset node info](https://clear.ml/docs/latest/assets/images/webapp_dataset_node_dark-ca7e93e98a506803a4791ec8bb6330e5.png#dark-mode-only)

- Version name and number
- Version size
- Version update time
- Version details button - Hover over the version and click ![console](https://clear.ml/docs/latest/icons/ico-console.svg)
to view the version's [details panel](https://clear.ml/docs/latest/docs/webapp/datasets/webapp_dataset_viewing/#version-details-panel)

Archiving versions

You can archive dataset versions so the versions list doesn't get too cluttered. Click **OPEN ARCHIVE** on the top of
the list to open the archive and view all archived versions. From the archive, you can restore
versions to remove them from the archive. You can also permanently delete versions.

Download Version List

You can download the dataset version list as a CSV file by clicking ![Download](https://clear.ml/docs/latest/icons/ico-download.svg)
and choosing one of these options:

- **Download onscreen items** \- Download the values for versions currently visible on screen
- **Download all items** \- Download the values for all versions in this dataset that match the current active filters

The downloaded data consists of the currently displayed table columns.

## Version Details [​](https://clear.ml/docs/latest/docs/webapp/datasets/webapp_dataset_viewing/\#version-details "Direct link to Version Details")

### Version Info [​](https://clear.ml/docs/latest/docs/webapp/datasets/webapp_dataset_viewing/\#version-info "Direct link to Version Info")

On the right side of the dataset version panel, view the **VERSION INFO** which shows:

- Version name
- Dataset ID
- Parent task name (click to navigate to the parent task's page)
- Version file size (original and compressed)
- Number of files
- Number of links
- Changes from previous version
  - Number of files added
  - Number of files modified
  - Number of files removed
  - Change in size
- Version description - to modify, hover over description and click ![Edit pencil](https://clear.ml/docs/latest/icons/ico-edit.svg),
which opens the edit window

![Version info](https://clear.ml/docs/latest/assets/images/webapp_dataset_version_info-21c0a0097c1af664d5d28fec4dc20aa7.png#light-mode-only)![Version info](https://clear.ml/docs/latest/assets/images/webapp_dataset_version_info_dark-831be413db7fb5d964281e64ae20300f.png#dark-mode-only)

To view a version's detailed information, click **Full details**, which will open the dataset version's [task page](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual).

![Dataset task info](https://clear.ml/docs/latest/assets/images/webapp_dataset_task_page-0d5ed345bb5d7dc4a7b252d3b2b4e008.png#light-mode-only)![Dataset task info](https://clear.ml/docs/latest/assets/images/webapp_dataset_task_page_dark-d8fbf8ec257d8a66101d73a2fca93062.png#dark-mode-only)

To view the information for any version in the lineage graph, click its node, and the **VERSION INFO** panel displays
that version's details.

### Version Details Panel [​](https://clear.ml/docs/latest/docs/webapp/datasets/webapp_dataset_viewing/\#version-details-panel "Direct link to Version Details Panel")

Click on **DETAILS** on the top left of the info panel or hover over a version node and click ![details](https://clear.ml/docs/latest/icons/ico-console.svg)
to view the version's details panel. The panel includes three tabs:

- **CONTENT** \- Table summarizing version contents, including file names, file sizes, and hashes

![content](https://clear.ml/docs/latest/assets/images/webapp_dataset_content-502df676ac1a1b8d38d474a8910038dc.png#light-mode-only)![content](https://clear.ml/docs/latest/assets/images/webapp_dataset_content_dark-469faf3a3b6738e0e4fbe2992d0a0d3d.png#dark-mode-only)

- **PREVIEW** \- A preview of the dataset version's contents.

![preview](https://clear.ml/docs/latest/assets/images/webapp_dataset_preview-0e763c21d7fb130f169117519b3e6421.png#light-mode-only)![preview](https://clear.ml/docs/latest/assets/images/webapp_dataset_preview_dark-30fd4d6c309fa7aecf246950d84a905c.png#dark-mode-only)

- **CONSOLE** \- The dataset version's console output

![console](https://clear.ml/docs/latest/assets/images/webapp_dataset_console-525f28f2520f89e566123bc0692a8907.png#light-mode-only)![console](https://clear.ml/docs/latest/assets/images/webapp_dataset_console_dark-8b5f19a67d667f6c4fb2419a5eec4684.png#dark-mode-only)


Click ![Expand](https://clear.ml/docs/latest/icons/ico-max-panel.svg) on the content panel header to view the panel in full screen.

## Dataset Actions [​](https://clear.ml/docs/latest/docs/webapp/datasets/webapp_dataset_viewing/\#dataset-actions "Direct link to Dataset Actions")

The following table describes the actions that can be done from the dataset versions list.

Access these actions with the context menu by right-clicking a version on the dataset versions list.

| Action | Description |
| --- | --- |
| Add Tag | User-defined labels added to versions for grouping and organization. |
| Publish | Publish a version to prevent changes to it. _Published_ versions are read-only. |
| Archive | Move dataset versions to the dataset's archive. |
| Restore | Action available in the archive. Restore a version to the active dataset version table. |
| Delete | Delete an archived version and its artifacts. This action is available only from the dataset's archive. |

![Dataset actions](https://clear.ml/docs/latest/assets/images/webapp_dataset_actions-abba7e1bf38390070f12539d1071604f.png#light-mode-only)![Dataset actions](https://clear.ml/docs/latest/assets/images/webapp_dataset_actions_dark-b70dde56549d624ad8887fac583226d2.png#dark-mode-only)

The actions mentioned in the chart above can be performed on multiple versions at once. [Select multiple versions](https://clear.ml/docs/latest/docs/webapp/datasets/webapp_dataset_viewing/#selecting-multiple-versions),
then use either the context menu, or the bar that appears at the bottom of the page, to perform operations on the
selected versions.

## Selecting Multiple Versions [​](https://clear.ml/docs/latest/docs/webapp/datasets/webapp_dataset_viewing/\#selecting-multiple-versions "Direct link to Selecting Multiple Versions")

Select multiple versions by clicking the checkbox on the left of each relevant version. Clear any existing selection by
clicking the checkbox in the top left corner of the list.

Click the checkbox in the top left corner of the list to select all items currently visible.

An extended bulk selection tool is available through the down arrow next to the checkbox in the top left corner, enabling selecting items beyond the items currently on-screen:

- **All** \- Select all versions in the dataset
- **None** \- Clear selection
- **Filtered** \- Select all versions in the dataset that match the current active filters

- [Version Details](https://clear.ml/docs/latest/docs/webapp/datasets/webapp_dataset_viewing/#version-details)
  - [Version Info](https://clear.ml/docs/latest/docs/webapp/datasets/webapp_dataset_viewing/#version-info)
  - [Version Details Panel](https://clear.ml/docs/latest/docs/webapp/datasets/webapp_dataset_viewing/#version-details-panel)
- [Dataset Actions](https://clear.ml/docs/latest/docs/webapp/datasets/webapp_dataset_viewing/#dataset-actions)
- [Selecting Multiple Versions](https://clear.ml/docs/latest/docs/webapp/datasets/webapp_dataset_viewing/#selecting-multiple-versions)