---
url: "https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_dataviews/"
title: "The Dataview Table | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_dataviews/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

Enterprise Feature

Dataviews are available under the ClearML Enterprise plan.

The **Dataview table** is a [customizable](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_dataviews/#customizing-the-dataview-table) list of Dataviews associated with a project.
Use it to view and create Dataviews, and access their info panels.

The table lists independent Dataview objects. To see Dataviews logged by a task, go
to the specific task's **DATAVIEWS** tab (see [Task Dataviews](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_exp_track_visual)).

View the Dataview table in table view ![Table view](https://clear.ml/docs/latest/icons/ico-table-view.svg)
or in details view ![Details view](https://clear.ml/docs/latest/icons/ico-split-view.svg),
using the buttons on the top left of the page. Use the table view for a comparative view of your Dataviews according to
columns of interest. Use the details view to access a selected Dataview's details, while keeping the Dataview list in view.
Details view can also be accessed by double-clicking a specific Dataview in the table view to open its details view.

Use the search bar ![Magnifying glass](https://clear.ml/docs/latest/icons/ico-search.svg)
to find specific dataviews. You can query by the dataview name, ID, description, hyper-datasets, and versions.
To search using regex, click the `.*` icon on the search bar.

You can archive Dataviews so the Dataview table doesn't get too cluttered. Click **OPEN ARCHIVE** on the top of the
table to open the archive and view all archived Dataviews. From the archive, you can restore
Dataviews to remove them from the archive. You can also permanently delete Dataviews.

You can download the Dataview table as a CSV file by clicking ![Download](https://clear.ml/docs/latest/icons/ico-download.svg)
and choosing one of these options:

- **Download onscreen items** \- Download the values for Dataviews currently visible on screen
- **Download all items** \- Download the values for all Dataviews in this project that match the current active filters

The downloaded data consists of the currently displayed table columns.

![Dataview table](https://clear.ml/docs/latest/assets/images/webapp_dataviews_table-81398c718df07080c71ce428c7e8bcff.png#light-mode-only)![Dataview table](https://clear.ml/docs/latest/assets/images/webapp_dataviews_table_dark-f0287b357d3efe9a8e01a4c98fd9ba18.png#dark-mode-only)

The Dataview table includes the following columns:

| Column | Description | Type |
| --- | --- | --- |
| **DATAVIEW** | Dataview name | String |
| **USER** | User who created the Dataview | String |
| **STATUS** | The status of the Dataview, which can be _Draft_ (editable) or _Published_ (read-only) | String |
| **PROJECT** | Name of the Dataview's project | String |
| **CREATED** | Elapsed time since the Dataview was created | Date-time |
| **DESCRIPTION** | A description of the Dataview | String |

Dynamically order the columns by dragging a column heading
to a new position.

## Customizing the Dataview Table [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_dataviews/\#customizing-the-dataview-table "Direct link to Customizing the Dataview Table")

The Dataview table can be customized. Changes are persistent (cached in the browser), and represented in the URL.
Save customized settings in a browser bookmark, and share the URL with teammates.

Customize the table using any of the following:

- Dynamic column order - Drag a column title to a different position.
- Resize columns - Drag the column separator to change the width of that column. Double-click the column separator for automatic fit.
- Filter by user and/or status - When a filter is applied to a column, its filter icon will appear with a highlighted
dot on its top right (![Filter on](https://clear.ml/docs/latest/icons/ico-filter-on.svg)). To
clear all active filters, click ![Clear filters](https://clear.ml/docs/latest/icons/ico-filter-reset.svg)
in the top right corner of the table.
- Sort columns - By task name and/or elapsed time since creation.

note

The following Dataviews-table customizations are saved on a **per-project** basis:

- Column order
- Column width
- Active sort order
- Active filters

If a project has subprojects, the Dataviews can be viewed by their subproject groupings or together with
all the Dataviews in the project. The customizations of these two views are saved separately.

## Dataview Actions [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_dataviews/\#dataview-actions "Direct link to Dataview Actions")

The following table describes the actions that can be performed from the Dataview table.

Access these actions with the context menu in any of the following ways:

- In the Dataview table, right-click a Dataview, or hover over a Dataview and click ![Dot menu](https://clear.ml/docs/latest/icons/ico-dots-v-menu.svg)
- In a Dataview info panel, click the menu button ![Bar menu](https://clear.ml/docs/latest/icons/ico-bars-menu.svg)

| ClearML Action | Description |
| --- | --- |
| Details | View Dataview details, including input datasets, label mapping, and iteration control. Can also be accessed by double-clicking a Dataview in the Dataview table. |
| Archive | Move Dataview to the Dataview's archive. |
| Restore | Action available in the archive. Restore a Dataview to the active Dataview table. |
| Delete | Action available in the archive. Permanently delete a Dataview. |
| Clone | Make an exact copy of a Dataview that is editable. |
| Move to Project | Move a Dataview to another project. |
| Publish | Publish a Dataview to prevent changes to it. _Published_ Dataviews are read-only. |

Enterprise Feature

The ClearML Enterprise Server provides a mechanism to define your own custom actions, which will
appear in the context menu. Create a custom action by defining an HTTP request to issue when clicking on the context menu
action. For more information see [Custom UI Context Menu Actions](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_config#custom-ui-context-menu-actions).

Some of the actions mentioned in the chart above can be performed on multiple Dataviews at once.
Select multiple Dataviews, then use either the context menu, or the batch action bar that appears at the bottom of the page, to perform
operations on the selected Dataviews. The context menu shows the number of Dataviews that can be affected by each action.
The same information can be found in the batch action bar, in a tooltip that appears when hovering over an action icon.

![Dataview table batch operations](https://clear.ml/docs/latest/assets/images/webapp_dataviews_context_menu-c409067026e99b5c3fb5ff68a0e4a501.png#light-mode-only)![Dataview table batch operations](https://clear.ml/docs/latest/assets/images/webapp_dataviews_context_menu_dark-423d2d6d398910fe6cf54e3b5ce62ab0.png#dark-mode-only)

## Creating a Dataview [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_dataviews/\#creating-a-dataview "Direct link to Creating a Dataview")

Create a Dataview by clicking **\+ NEW DATAVIEW**, which opens a
**NEW DATAVIEW** window.

![New Dataview window](https://clear.ml/docs/latest/assets/images/webapp_dataview_new-e6b69e104268a8267f9ff9478d3f9b53.png#light-mode-only)![New Dataview window](https://clear.ml/docs/latest/assets/images/webapp_dataview_new_dark-c61c9fb041432ad5996809569a0b84b7.png#dark-mode-only)

- [Customizing the Dataview Table](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_dataviews/#customizing-the-dataview-table)
- [Dataview Actions](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_dataviews/#dataview-actions)
- [Creating a Dataview](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_dataviews/#creating-a-dataview)