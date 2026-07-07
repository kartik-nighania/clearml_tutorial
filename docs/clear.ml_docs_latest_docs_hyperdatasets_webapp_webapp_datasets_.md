---
url: "https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets/"
title: "Hyper-Datasets Page | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

Enterprise Feature

Hyper-Datasets are available under the ClearML Enterprise plan.

Use the Hyper-Datasets Page to navigate between and manage hyper-datasets.

You can view the Hyper-Datasets page in Project view ![Project view](https://clear.ml/docs/latest/icons/ico-project-view.svg)
or in List view ![List view](https://clear.ml/docs/latest/icons/ico-flat-view.svg). In List
view, all hyper-datasets are shown side-by-side. In Project view, hyper-datasets are organized according to their projects, and
top-level projects are displayed. Click on a project card to view the project's hyper-datasets.

Click on a Hyper-Dataset card to open the dataset's [version list](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_versioning), where you can view
and manage the dataset versions' lineage and contents.

Filter page contents by specific fields ![Filter](https://clear.ml/docs/latest/icons/ico-filter-off.svg)
or through free form search ![Magnifying glass](https://clear.ml/docs/latest/icons/ico-search.svg):

- My Work - Show only hyper-datasets that you created
- Tags - Choose which tags to filter by from a list of tags used in the hyper-datasets.
  - Filter by multiple tag values using the **ANY** or **ALL** options, which correspond to the logical "AND" and "OR"
    respectively. These options appear on the top of the tag list.
  - Filter by the absence of a tag (logical "NOT") by clicking its checkbox twice. An X will appear in the tag's checkbox.
- User - Filter hyper-datasets by the user who created them.

Free form search queries hyper-dataset name, ID, tags, and project. To search using regex, click the `.*`
icon on the search bar.

![Hyper-Dataset page](https://clear.ml/docs/latest/assets/images/datasets_01-8d3ad8d1da50b57f50a5f88d71e62918.png#light-mode-only)![Hyper-Dataset page](https://clear.ml/docs/latest/assets/images/datasets_01_dark-f008f0f582b603c9ef6eb53043258d3d.png#dark-mode-only)

## Project Cards [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets/\#project-cards "Direct link to Project Cards")

In Project view, project cards display a project's summarized hyper-dataset information:

![Hyper-Dataset project card](https://clear.ml/docs/latest/assets/images/hyperdataset_project_card-95bc8f11400686627b7b6f9acd093616.png#light-mode-only)![Hyper-Dataset project card](https://clear.ml/docs/latest/assets/images/hyperdataset_project_card_dark-be9888e9f7ee4bf10fc6c9726d4b5547.png#dark-mode-only)

- Project name
- Number of hyper-datasets in project
- Tags used by hyper-datasets in project

Click on a project card to view its hyper-datasets.

## Hyper-Dataset Cards [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets/\#hyper-dataset-cards "Direct link to Hyper-Dataset Cards")

In List view, the Hyper-Dataset cards display summarized dataset information:

![Hyper-Dataset card](https://clear.ml/docs/latest/assets/images/hyperdataset_card-066da450531fdaa009c925d1f1ff2205.png#light-mode-only)![Hyper-Dataset card](https://clear.ml/docs/latest/assets/images/hyperdataset_card_dark-7a4c72a61c9685fbe0dc1647cbbc1cde.png#dark-mode-only)

- Dataset name
- Time since last update. Hover over elapsed time to view date of last update
- User updating the Dataset
- If the dataset contains dataset-level metadata, the card displays the ![Check mark](https://clear.ml/docs/latest/icons/ico-status-completed.svg)`Metadata` indicator, which opens the Metadata editor on click
- The number of versions in the Dataset
- The total number of frames in all versions of the Dataset. If an asterisk (\*) appears next to **FRAMES**, then you can hover over it and see the name of the version whose frames were last updated
- The percentage of frames annotated in all versions of the Dataset. If an asterisk (\*) appears next to **ANNOTATED**, then you can hover over it and see the name of the version whose frames were last annotated
- If the Dataset version's status is _Published_, then the Dataset's top labels appear (colors are editable). If the
Dataset version is _Draft_, then no labels appear
- Tags

Change Label Color

To change the label color coding, hover over a label color, click the hand pointer, and then select a new color.

### Hyper-Dataset Actions [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets/\#hyper-dataset-actions "Direct link to Hyper-Dataset Actions")

Click ![Menu](https://clear.ml/docs/latest/icons/ico-bars-menu.svg) on the top right
of a dataset card to open its context menu and access dataset actions:

![Hyper-Dataset context menu](https://clear.ml/docs/latest/assets/images/webapp_hyperdataset_card_context_menu-35e658e2e787c04a55a92f8d796980a2.png#light-mode-only)![Hyper-Dataset context menu](https://clear.ml/docs/latest/assets/images/webapp_hyperdataset_card_context_menu_dark-3b950e78a353ce4d476fd00367836e92.png#dark-mode-only)

- **Copy Dataset ID**
- **View Dataset Schema** \- View the dataset's frame document schema. This shows the frames’ fields and their types.
- **Rename** \- Change the dataset's name
- **Add Tag** \- Add label to the dataset to help easily classify groups of datasets.
- **Edit Metadata** \- Modify dataset-level metadata. This will open the metadata edit window, where you can edit the section
- **Delete** \- Delete the dataset and all its versions.






warning





You cannot undo the deletion of a Hyper-Dataset.

- **Move to Project** \- Move the dataset to another project.

## Create New Hyper-Datasets [​](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets/\#create-new-hyper-datasets "Direct link to Create New Hyper-Datasets")

To create a Hyper-Dataset, click the **\+ NEW DATASET** button in the top right of the page, which will open a
**New Dataset** modal.

![Hyper-Dataset creation modal](https://clear.ml/docs/latest/assets/images/webapp_hyperdataset_creation-f1a6b9a077b2f31ab5cd3e8c55f16be3.png#light-mode-only)![Hyper-Dataset creation modal](https://clear.ml/docs/latest/assets/images/webapp_hyperdataset_creation_dark-a201e57eef50a5b484a0e437ff4f82e6.png#dark-mode-only)

This creates a new Hyper-Dataset that contains a single, empty draft version.

- [Project Cards](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets/#project-cards)
- [Hyper-Dataset Cards](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets/#hyper-dataset-cards)
  - [Hyper-Dataset Actions](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets/#hyper-dataset-actions)
- [Create New Hyper-Datasets](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets/#create-new-hyper-datasets)