---
url: "https://clear.ml/docs/latest/docs/webapp/datasets/webapp_dataset_page/"
title: "Datasets Page | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/webapp/datasets/webapp_dataset_page/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

SDK version compatibility

The datasets page shows datasets created with `clearml` v1.6 or newer.

Datasets created with earlier versions of `clearml` are available in their original project.

Use the **Datasets** Page to navigate between and manage datasets. The page shows summaries
for all datasets created using [ClearML Data](https://clear.ml/docs/latest/docs/clearml_data/).

You can view the datasets page in Project view ![Project view](https://clear.ml/docs/latest/icons/ico-project-view.svg)
or in List view ![List view](https://clear.ml/docs/latest/icons/ico-flat-view.svg). In List
view, all datasets are shown side-by-side. In Project view, datasets are organized according to their projects, and
top-level projects are displayed. Click on a project card to view the project's datasets.

Click on a dataset card to navigate to its [Version List](https://clear.ml/docs/latest/docs/webapp/datasets/webapp_dataset_viewing), where you can view the
dataset versions' lineage and contents.

Filter page contents by specific fields ![Filter](https://clear.ml/docs/latest/icons/ico-filter-off.svg)
or through free form search ![Magnifying glass](https://clear.ml/docs/latest/icons/ico-search.svg):

- My Work - Show only datasets that you created
- Tags - Choose which tags to filter by from a list of tags used in the datasets.
  - Filter by multiple tag values using the **ANY** or **ALL** options, which correspond to the logical "AND" and "OR"
    respectively. These options appear on the top of the tag list.
  - Filter by the absence of a tag (logical "NOT") by clicking its checkbox twice. An X will appear in the tag's checkbox.
- User - Filter datasets by the user who created them.

Free form search queries dataset name, ID, and description. To search using regex, click the `.*`
icon on the search bar.

![Dataset page](https://clear.ml/docs/latest/assets/images/webapp_dataset_page-dbff28c2e349ea8815ea08c2d4a28ef2.png#light-mode-only)![Dataset page](https://clear.ml/docs/latest/assets/images/webapp_dataset_page_dark-ef7faa58ecfa2a8ba304152613f38049.png#dark-mode-only)

## Project Cards [​](https://clear.ml/docs/latest/docs/webapp/datasets/webapp_dataset_page/\#project-cards "Direct link to Project Cards")

In Project view, project cards display a project's summarized dataset information:

![Project card](https://clear.ml/docs/latest/assets/images/webapp_dataset_project_card-7d8b0567f205a5288e3bdbe73136d418.png#light-mode-only)![Project card](https://clear.ml/docs/latest/assets/images/webapp_dataset_project_card_dark-2807658eed675a8133ac86f6ca65814f.png#dark-mode-only)

- Project name
- Number of datasets in project
- Tags used by datasets in project

Click on a project card to view its datasets.

## Dataset Cards [​](https://clear.ml/docs/latest/docs/webapp/datasets/webapp_dataset_page/\#dataset-cards "Direct link to Dataset Cards")

In List view, the dataset cards display summarized dataset information:

![Dataset card](https://clear.ml/docs/latest/assets/images/webapp_dataset_card-e965d270732c06b590bdf2c084ba7023.png#light-mode-only)![Dataset card](https://clear.ml/docs/latest/assets/images/webapp_dataset_card_dark-b96d52de5b3826fe45a42c991bc87ba1.png#dark-mode-only)

- Dataset name
- Time since last update
- Number of versions
- Details about latest version
  - Number of files
  - Size
- Tags

### Dataset Actions [​](https://clear.ml/docs/latest/docs/webapp/datasets/webapp_dataset_page/\#dataset-actions "Direct link to Dataset Actions")

Click ![Menu](https://clear.ml/docs/latest/icons/ico-bars-menu.svg) on the top right
of a dataset card to open its context menu and access dataset actions.

![Dataset context menu](https://clear.ml/docs/latest/assets/images/webapp_dataset_card_context_menu-2a125f85616d8efc3f446e594eece7a8.png#light-mode-only)![Dataset context menu](https://clear.ml/docs/latest/assets/images/webapp_dataset_card_context_menu_dark-a072653555498415a14f73bbe573962f.png#dark-mode-only)

- **Rename** \- Change the dataset's name
- **Add Tag** \- Add label to the dataset to help easily classify groups of dataset.
- **Delete** \- Delete the dataset and all of its versions. To delete a dataset, all its versions must first be
archived.

- [Project Cards](https://clear.ml/docs/latest/docs/webapp/datasets/webapp_dataset_page/#project-cards)
- [Dataset Cards](https://clear.ml/docs/latest/docs/webapp/datasets/webapp_dataset_page/#dataset-cards)
  - [Dataset Actions](https://clear.ml/docs/latest/docs/webapp/datasets/webapp_dataset_page/#dataset-actions)