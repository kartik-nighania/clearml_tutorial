---
url: "https://clear.ml/docs/latest/docs/hyperdatasets/dataset/"
title: "Datasets and Dataset Versions | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/hyperdatasets/dataset/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

ClearML Enterprise's **Datasets** and **Dataset versions** provide the internal data structure
and functionality for the following purposes:

- Connecting source data to the ClearML Enterprise platform
- Using ClearML Enterprise's Git-like [Dataset versioning](https://clear.ml/docs/latest/docs/hyperdatasets/dataset/#dataset-versioning)
- Integrating the powerful features of [Dataviews](https://clear.ml/docs/latest/docs/hyperdatasets/dataviews) with a task
- [Annotating](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_frames#annotations) images and videos

Datasets consist of versions with SingleFrames and/or FrameGroups. Each Dataset can contain multiple versions, which
can have multiple children that inherit their parent's contents.

Mask-labels are defined at the DatasetVersion level, and are applied to all masks in a DatasetVersion.

## Example Datasets [​](https://clear.ml/docs/latest/docs/hyperdatasets/dataset/\#example-datasets "Direct link to Example Datasets")

ClearML Enterprise provides Example Datasets complete with frames,
and ready for your experimentation. Find these example Datasets in the ClearML Enterprise WebApp (UI). They appear
with an "Example" banner in the WebApp (UI).

## Usage [​](https://clear.ml/docs/latest/docs/hyperdatasets/dataset/\#usage "Direct link to Usage")

### Creating Datasets [​](https://clear.ml/docs/latest/docs/hyperdatasets/dataset/\#creating-datasets "Direct link to Creating Datasets")

Use the [`Dataset.create`](https://clear.ml/docs/latest/docs/references/hyperdataset/#datasetcreate) method to create a Dataset. It will
contain an empty version named `Current`.

```python
from allegroai import Dataset

myDataset = Dataset.create(dataset_name='myDataset')
```

Or, use the [`DatasetVersion.create_new_dataset`](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion#datasetversioncreate_new_dataset)
method.

```python
from allegroai import DatasetVersion

myDataset = DatasetVersion.create_new_dataset(dataset_name='myDataset Two')
```

When creating a dataset, you can put it into a project. In this case, the dataset will adhere to the [access rules](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_access_rules)
specified for its containing project. Use `dataset_project` parameter in `Dataset.create` or `DatasetVersion.create_new_dataset`
to specify a project name.

```python
myDataset_1 = Dataset.create(dataset_name="myDataset", dataset_project="myDataset Project")

myDataset_2 = DatasetVersion.create_new_dataset(

  dataset_name="myDataset_2", dataset_project="myDatasetProject_2"

)
```

To raise a `ValueError` exception if the Dataset exists, specify the `raise_if_exists` parameters as `True`.

- With `Dataset.create`:





```python
try:

      myDataset = Dataset.create(dataset_name='myDataset One', raise_if_exists=True)

except ValueError:

      print('Dataset exists.')
```

- Or with `DatasetVersion.create_new_dataset`:





```python
try:

      myDataset = DatasetVersion.create_new_dataset(dataset_name='myDataset Two', raise_if_exists=True)

except ValueError:

      print('Dataset exists.')
```


Additionally, create a Dataset with tags and a description.

```python
myDataset = DatasetVersion.create_new_dataset(

  dataset_name='myDataset',

  tags=['One Tag', 'Another Tag', 'And one more tag'],

  description='some description text'

)
```

### Accessing Current Dataset [​](https://clear.ml/docs/latest/docs/hyperdatasets/dataset/\#accessing-current-dataset "Direct link to Accessing Current Dataset")

To get the current Dataset, use the [`DatasetVersion.get_current`](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion#datasetversionget_current)
method.

```python
myDataset = DatasetVersion.get_current(dataset_name='myDataset')
```

### Deleting Datasets [​](https://clear.ml/docs/latest/docs/hyperdatasets/dataset/\#deleting-datasets "Direct link to Deleting Datasets")

Use the [`Dataset.delete`](https://clear.ml/docs/latest/docs/references/hyperdataset/#datasetdelete) class method to delete a Dataset:

- Delete an empty Dataset (no versions):





```python
Dataset.delete(dataset_name='MyDataset', delete_all_versions=False, force=False)
```

- Delete a Dataset containing only versions whose status is _Draft_:





```python
Dataset.delete(dataset_name='MyDataset', delete_all_versions=True, force=False)
```

- Delete a Dataset even if it contains versions whose status is _Published_:





```python
Dataset.delete(dataset_name='MyDataset', delete_all_versions=True, force=True)
```

- Delete a Dataset and the sources associated with its deleted frames:





```python
Dataset.delete(

    dataset_name='MyDataset', delete_all_versions=True, force=True, delete_sources=True

)
```









This supports deleting sources located in AWS S3, GCP, and Azure Storage (not local storage). The `delete_sources`
parameter is ignored if `delete_all_versions` is `False`. You can view the deletion process' progress by passing
`show_progress=True` (`tqdm` required).


### Tagging Datasets [​](https://clear.ml/docs/latest/docs/hyperdatasets/dataset/\#tagging-datasets "Direct link to Tagging Datasets")

Tags can be added to datasets, allowing to easily identify and group tasks.

Add tags to a dataset:

```python
MyDataset.add_tags(["coco", "dogs"])
```

Remove tags from a dataset:

```python
MyDataset.remove_tags(["dogs"])
```

## Dataset Versioning [​](https://clear.ml/docs/latest/docs/hyperdatasets/dataset/\#dataset-versioning "Direct link to Dataset Versioning")

Dataset versioning refers to the group of ClearML Enterprise SDK and WebApp (UI) features for creating,
modifying, and deleting Dataset versions.

ClearML Enterprise supports simple and advanced Dataset versioning paradigms. A **simple version structure** consists of
a single evolving version, with historic static snapshots. Continuously push your changes to your single dataset version,
and take a snapshot to record the content of your dataset at a specific point in time.

You can, alternatively, employ any **advanced structure**, where each version evolves in parallel, and you control which
versions are locked for further changes and which can be modified. See details [below](https://clear.ml/docs/latest/docs/hyperdatasets/dataset/#dataset-version-structure).

## Dataset Version State [​](https://clear.ml/docs/latest/docs/hyperdatasets/dataset/\#dataset-version-state "Direct link to Dataset Version State")

Dataset versions can have either _Draft_ or _Published_ state.

A _Draft_ version is editable, so frames can be added to and deleted and/or modified.

A _Published_ version is read-only, which ensures reproducible tasks and preserves the Dataset version contents.
Child versions can only be created from _Published_ versions, as they inherit their predecessor version contents.

## Dataset Version Structure [​](https://clear.ml/docs/latest/docs/hyperdatasets/dataset/\#dataset-version-structure "Direct link to Dataset Version Structure")

To implement a simple version structure, where the dataset is ever evolving, with a linear set of historic snapshots,
a parent version can have one and only one child, with the last child in the Dataset versions tree in _Draft_ state.
Different version structures, such as where at least one parent has more than one child, or the single last child in the
Dataset versions tree is _Published_ are considered advanced version structures.

For details about programmatically implementing simple and advanced version structures, see [Creating Snapshots](https://clear.ml/docs/latest/docs/hyperdatasets/dataset/#creating-snapshots)
and [Creating Child Versions](https://clear.ml/docs/latest/docs/hyperdatasets/dataset/#creating-child-versions) respectively below.

## DatasetVersion Usage [​](https://clear.ml/docs/latest/docs/hyperdatasets/dataset/\#datasetversion-usage "Direct link to DatasetVersion Usage")

Manage Dataset versioning using the DatasetVersion class in the ClearML Enterprise SDK.

### Creating Snapshots [​](https://clear.ml/docs/latest/docs/hyperdatasets/dataset/\#creating-snapshots "Direct link to Creating Snapshots")

If the Dataset contains only one version whose status is _Draft_, snapshots of the current version can be created.
When creating a snapshot, the current version becomes the snapshot (it keeps the same version ID),
and the newly created version (with its new version ID) becomes the current version.

To create a snapshot, use the `DatasetVersion.create_snapshot` method.

#### Snapshot Naming [​](https://clear.ml/docs/latest/docs/hyperdatasets/dataset/\#snapshot-naming "Direct link to Snapshot Naming")

In the simple version structure, ClearML Enterprise supports two methods for snapshot naming:

- **Timestamp naming** \- If only the Dataset name or ID is provided, the snapshot is named `snapshot` with a timestamp
appended.


The timestamp format is ISO 8601 (`YYYY-MM-DDTHH:mm:ss.SSSSSS`). For example, `snapshot 2020-03-26T16:55:38.441671`.

**Example:**





```python
from allegroai import DatasetVersion



myDataset = DatasetVersion.create_snapshot(dataset_name='MyDataset')
```









After the statement above runs, the previous current version keeps its existing version ID, and it becomes a
snapshot named `snapshot` with a timestamp appended. The newly created version with a new version ID becomes
the current version, and its name is `Current`.

- **User-specified snapshot naming** \- If the `publish_name` parameter is provided, it will be the name of the snapshot name.

**Example:**





```python
myDataset = DatasetVersion.create_snapshot(dataset_name='MyDataset', publish_name='NewSnapshotName')
```









After the above statement runs, the previous current version keeps its existing version ID and becomes a snapshot named
`NewSnapshotName`.
The newly created version (with a new version ID) becomes the current version, and its name is `Current`.


#### Current Version Naming [​](https://clear.ml/docs/latest/docs/hyperdatasets/dataset/\#current-version-naming "Direct link to Current Version Naming")

In the simple version structure, ClearML Enterprise supports two methods for current version naming:

- **Default naming** \- If the `child_name` parameter is not provided, `Current` is the current version name.
- **User-specified current version naming** \- If the `child_name` parameter is provided, that child name becomes the current
version name.

For example, after the following statement runs, the previous current version keeps its existing version ID and becomes
a snapshot named `snapshot` with the timestamp appended.
The newly created version (with a new version ID) is the current version, and its name is `NewCurrentVersionName`.

```python
myDataset = DatasetVersion.create_snapshot(

  dataset_name='MyDataset',

  child_name='NewCurrentVersionName'

)
```

#### Adding Metadata and Comments [​](https://clear.ml/docs/latest/docs/hyperdatasets/dataset/\#adding-metadata-and-comments "Direct link to Adding Metadata and Comments")

Add a metadata dictionary and/or comment to a snapshot.

For example:

```python
myDataset = DatasetVersion.create_snapshot(

  dataset_name='MyDataset',

  child_metadata={'abc':'1234','def':'5678'},

  child_comment='some text comment'

)
```

### Creating Child Versions [​](https://clear.ml/docs/latest/docs/hyperdatasets/dataset/\#creating-child-versions "Direct link to Creating Child Versions")

Create a new version from any version whose status is _Published_.

To create a new version, call the [`DatasetVersion.create_version`](https://clear.ml/docs/latest/docs/references/hyperdataset/#datasetversioncreate_version)
method, and provide:

- Either the Dataset name or ID
- The parent version name or ID from which the child inherits frames
- The new version's name.

For example, create a new version named `NewChildVersion` from the existing version `PublishedVersion`,
where the new version inherits the frames of the existing version. If `NewChildVersion` already exists,
it is returned.

```python
myVersion = DatasetVersion.create_version(

  dataset_name='MyDataset',

  parent_version_names=['PublishedVersion'],

  version_name='NewChildVersion'

)
```

To raise a ValueError exception if `NewChildVersion` exists, set `raise_if_exists` to `True`.

```python
myVersion = DatasetVersion.create_version(

  dataset_name='MyDataset',

  parent_version_names=['PublishedVersion'],

  version_name='NewChildVersion',

  raise_if_exists=True

)
```

### Creating Root-level Parent Versions [​](https://clear.ml/docs/latest/docs/hyperdatasets/dataset/\#creating-root-level-parent-versions "Direct link to Creating Root-level Parent Versions")

Create a new version at the root-level. This is a version without a parent, and it contains no frames.

```python
myDataset = DatasetVersion.create_version(

  dataset_name='MyDataset',

  version_name='NewRootVersion'

)
```

### Getting Versions [​](https://clear.ml/docs/latest/docs/hyperdatasets/dataset/\#getting-versions "Direct link to Getting Versions")

To get a version or versions, use the [`DatasetVersion.get_version`](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion#datasetversionget_version)
and [`DatasetVersion.get_versions`](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion#datasetversionget_versions)
methods, respectively.

**Getting a list of all versions**

```python
myDatasetversion = DatasetVersion.get_versions(dataset_name='MyDataset')
```

**Getting a list of all _published_ versions**

```python
myDatasetversion = DatasetVersion.get_versions(

  dataset_name='MyDataset',

  only_published=True

)
```

**Getting a list of all _drafts_ versions**

```python
myDatasetversion = DatasetVersion.get_versions(

  dataset_name='MyDataset',

  only_draft=True

)
```

**Getting the current version**

If more than one version exists, ClearML Enterprise outputs a warning.

```python
myDatasetversion = DatasetVersion.get_version(dataset_name='MyDataset')
```

**Getting a specific version**

```python
myDatasetversion = DatasetVersion.get_version(

  dataset_name='MyDataset',

  version_name='VersionName'

)
```

### Deleting Versions [​](https://clear.ml/docs/latest/docs/hyperdatasets/dataset/\#deleting-versions "Direct link to Deleting Versions")

Delete versions which are status _Draft_ using the [`Dataset.delete_version`](https://clear.ml/docs/latest/docs/references/hyperdataset/#delete_version)
method.

```python
from allegroai import Dataset

myDataset = Dataset.get(dataset_name='MyDataset')

myDataset.delete_version(version_name='VersionToDelete')
```

### Publishing Versions [​](https://clear.ml/docs/latest/docs/hyperdatasets/dataset/\#publishing-versions "Direct link to Publishing Versions")

Publish (make read-only) versions which are status _Draft_ using the [`DatasetVersion.publish_version`](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion#publish_version)
method. This includes the current version, if the Dataset is in the simple version structure.

```python
myVersion = DatasetVersion.get_version(

  dataset_name='MyDataset',

  version_name='VersionToPublish'

)

myVersion.publish_version()
```

### Managing Version Mask-labels [​](https://clear.ml/docs/latest/docs/hyperdatasets/dataset/\#managing-version-mask-labels "Direct link to Managing Version Mask-labels")

#### Setting Version Mask-label Mapping [​](https://clear.ml/docs/latest/docs/hyperdatasets/dataset/\#setting-version-mask-label-mapping "Direct link to Setting Version Mask-label Mapping")

In order to visualize masks in a dataset version, the mask values need to be mapped to their labels. Mask-label
mapping is stored in a version's metadata.

To define the DatasetVersion level mask-label mapping, use the [`DatasetVersion.set_masks_labels`](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion#set_masks_labels)
method, and input a dictionary of RGB-value tuple keys and label-list values.

```python
from allegroai import DatasetVersion

# Getting a version

myDatasetversion = DatasetVersion.get_version(dataset_name='MyDataset',

                                              version_name='VersionName')

# Mapping out colors and labels of masks

myDatasetversion.set_masks_labels(

    {

      (0, 0, 0): ["background"],

      (1, 1, 1): ["person", "sitting"],

      (2, 2, 2): ["cat"],

    }

)
```

#### Accessing Version Mask-label Mapping [​](https://clear.ml/docs/latest/docs/hyperdatasets/dataset/\#accessing-version-mask-label-mapping "Direct link to Accessing Version Mask-label Mapping")

The mask values and labels are stored as a property in a dataset version's metadata.

```python
mapping = myDatasetversion.get_metadata()['mask_labels']

print(mapping)
```

This should return a dictionary of the version's masks and labels, which should look something like this:

```python
{'_all_': [{'value': [0, 0, 0], 'labels': ['background']}, {'value': [1, 1, 1], 'labels': ['person', 'sitting']}, {'value': [2, 2, 2], 'labels': ['cat']}]}
```

- [Example Datasets](https://clear.ml/docs/latest/docs/hyperdatasets/dataset/#example-datasets)
- [Usage](https://clear.ml/docs/latest/docs/hyperdatasets/dataset/#usage)
  - [Creating Datasets](https://clear.ml/docs/latest/docs/hyperdatasets/dataset/#creating-datasets)
  - [Accessing Current Dataset](https://clear.ml/docs/latest/docs/hyperdatasets/dataset/#accessing-current-dataset)
  - [Deleting Datasets](https://clear.ml/docs/latest/docs/hyperdatasets/dataset/#deleting-datasets)
  - [Tagging Datasets](https://clear.ml/docs/latest/docs/hyperdatasets/dataset/#tagging-datasets)
- [Dataset Versioning](https://clear.ml/docs/latest/docs/hyperdatasets/dataset/#dataset-versioning)
- [Dataset Version State](https://clear.ml/docs/latest/docs/hyperdatasets/dataset/#dataset-version-state)
- [Dataset Version Structure](https://clear.ml/docs/latest/docs/hyperdatasets/dataset/#dataset-version-structure)
- [DatasetVersion Usage](https://clear.ml/docs/latest/docs/hyperdatasets/dataset/#datasetversion-usage)
  - [Creating Snapshots](https://clear.ml/docs/latest/docs/hyperdatasets/dataset/#creating-snapshots)
  - [Creating Child Versions](https://clear.ml/docs/latest/docs/hyperdatasets/dataset/#creating-child-versions)
  - [Creating Root-level Parent Versions](https://clear.ml/docs/latest/docs/hyperdatasets/dataset/#creating-root-level-parent-versions)
  - [Getting Versions](https://clear.ml/docs/latest/docs/hyperdatasets/dataset/#getting-versions)
  - [Deleting Versions](https://clear.ml/docs/latest/docs/hyperdatasets/dataset/#deleting-versions)
  - [Publishing Versions](https://clear.ml/docs/latest/docs/hyperdatasets/dataset/#publishing-versions)
  - [Managing Version Mask-labels](https://clear.ml/docs/latest/docs/hyperdatasets/dataset/#managing-version-mask-labels)