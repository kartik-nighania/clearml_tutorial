---
url: "https://clear.ml/docs/latest/docs/clearml_data/"
title: "ClearML Data | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/clearml_data/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

important

This page covers `clearml-data`, ClearML's file-based data management solution.
See [Hyper-Datasets](https://clear.ml/docs/latest/docs/hyperdatasets/overview) for ClearML's advanced queryable dataset management solution.

In Machine Learning, you are very likely dealing with a gargantuan amount of data that you need to put in a dataset,
which you then need to be able to share, reproduce, and track.

ClearML Data Management solves two important challenges:

- Accessibility - Making data easily accessible from every machine
- Versioning - Linking data and tasks for better **traceability**.

![Dataset preview](https://clear.ml/docs/latest/assets/images/webapp_dataset_preview-0e763c21d7fb130f169117519b3e6421.png#light-mode-only)![Dataset preview](https://clear.ml/docs/latest/assets/images/webapp_dataset_preview_dark-30fd4d6c309fa7aecf246950d84a905c.png#dark-mode-only)

**We believe Data is not code**. It should not be stored in a git tree, because progress on datasets is not always linear.
Moreover, it can be difficult and inefficient to find on a git tree the commit associated with a certain version of a dataset.

Use ClearML Data to create, manage, and version your datasets. Store your files in any storage location of your choice
(S3 / GS / Azure / Network Storage) by setting the dataset's upload destination (see [`--storage`](https://clear.ml/docs/latest/docs/clearml_data/clearml_data_cli#upload)
CLI option or [`output_url`](https://clear.ml/docs/latest/docs/clearml_data/clearml_data_sdk#uploading-files) parameter).

Datasets can be set up to inherit from other datasets, so data lineages can be created, and users can track when and how
their data changes. Dataset changes are stored using differentiable storage, meaning a version will store the change-set
from its previous dataset parents.

You can get a local copy of your dataset on any machine. Local copies of datasets are always cached, so the same data
never needs to be downloaded twice. When a dataset is pulled it will automatically pull all parent datasets and merge
them into one output folder for you to work with.

The [Dataset Versions](https://clear.ml/docs/latest/docs/webapp/datasets/webapp_dataset_viewing) page in the web UI displays dataset versions'
lineage and content information. See [dataset UI](https://clear.ml/docs/latest/docs/webapp/datasets/webapp_dataset_page) for more details.

## Setup [​](https://clear.ml/docs/latest/docs/clearml_data/\#setup "Direct link to Setup")

`clearml-data` comes built-in with the `clearml` Python package! Check out the [ClearML Setup](https://clear.ml/docs/latest/docs/clearml_sdk/clearml_sdk_setup)
guide for more info!

## Using ClearML Data [​](https://clear.ml/docs/latest/docs/clearml_data/\#using-clearml-data "Direct link to Using ClearML Data")

ClearML Data supports two interfaces:

- `clearml-data` \- A CLI utility for creating, uploading, and managing datasets. See [CLI](https://clear.ml/docs/latest/docs/clearml_data/clearml_data_cli) for a reference of `clearml-data` commands.
- `clearml.Dataset` \- A Python interface for creating, retrieving, managing, and using datasets. See [SDK](https://clear.ml/docs/latest/docs/clearml_data/clearml_data_sdk) for an overview of the basic methods of the `Dataset` module.

For an overview of recommendations for ClearML Data workflows and practices, see [Best Practices](https://clear.ml/docs/latest/docs/best_practices/data_best_practices).

## Dataset Version States [​](https://clear.ml/docs/latest/docs/clearml_data/\#dataset-version-states "Direct link to Dataset Version States")

The following table displays the possible states for a dataset version.

| State | Description |
| --- | --- |
| _Uploading_ | Dataset creation is in progress |
| _Failed_ | Dataset creation was terminated with an error |
| _Aborted_ | Dataset creation was aborted by user before it was finalization |
| _Final_ | A dataset was created and finalized successfully |
| _Published_ | The dataset is read-only. Publish a dataset to prevent changes to it |

- [Setup](https://clear.ml/docs/latest/docs/clearml_data/#setup)
- [Using ClearML Data](https://clear.ml/docs/latest/docs/clearml_data/#using-clearml-data)
- [Dataset Version States](https://clear.ml/docs/latest/docs/clearml_data/#dataset-version-states)