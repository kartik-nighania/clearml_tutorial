---
url: "https://clear.ml/docs/latest/docs/references/hyperdataset/"
title: "Dataset | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/hyperdataset/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

## _class_ datasetversion.Dataset() [​](https://clear.ml/docs/latest/docs/references/hyperdataset/\#class-datasetversiondataset "Direct link to class-datasetversiondataset")

A dataset representation.

Used to manage a dataset and its versions

warning

Do not instantiate directly.
Use Dataset.get or Dataset.create methods instead.

* * *

### id [​](https://clear.ml/docs/latest/docs/references/hyperdataset/\#id "Direct link to id")

**property id**

The dataset’s id.

- **Return type**

`str`


* * *

### name [​](https://clear.ml/docs/latest/docs/references/hyperdataset/\#name "Direct link to name")

**property name**

The dataset’s name.

- **Return type**

`str`


* * *

### project [​](https://clear.ml/docs/latest/docs/references/hyperdataset/\#project "Direct link to project")

**property project**

The dataset’s project id. May be None if the project wasn’t specified when creating the dataset

- **Return type**

`Optional`\[`str`\]


* * *

### Dataset.create [​](https://clear.ml/docs/latest/docs/references/hyperdataset/\#datasetcreate "Direct link to Dataset.create")

**_classmethod_ create(dataset\_name, comment=None, tags=None, raise\_if\_exists=False, dataset\_project=None)**

Create a new dataset in the system and return a `Dataset` object for it.

- **Parameters**
  - **dataset\_name** ( _str_ ) – The name of the new dataset.

  - **comment** ( _str_ ) – A free text to describe the dataset

  - **tags** ( _list_ ) – A list of tags (short strings) to classify the dataset. If the
    dataset already exists, these tags will be added to its list of tags.

  - **raise\_if\_exists** ( _bool_ ) – If False (the default) and there is a dataset
    with the name `dataset_name`, return the existing
    `Dataset`. If True and there is a dataset with the name
    `dataset_name`, raise `ValueError` exception.

  - **dataset\_project** ( _str_ ) – A project name for the newly created dataset.
- **Return type**

`Dataset`

- **Returns**

A new `Dataset` object for the newly created dataset.


* * *

### Dataset.get [​](https://clear.ml/docs/latest/docs/references/hyperdataset/\#datasetget "Direct link to Dataset.get")

**_classmethod_ get(dataset\_id=None, dataset\_name=None, dataset\_project=None)**

Return a `Dataset` object for an existing dataset.

- **Parameters**


  - **dataset\_id** (`Optional`\[`str`\]) – The ID of the dataset

  - **dataset\_name** (`Optional`\[`str`\]) – The name of the dataset.

  - **dataset\_project** (`Optional`\[`str`\]) – The project of the dataset.


info

dataset\_id and dataset\_name are mutually exclusive. Setting both to non-None values will raise
a UsageError exception.

- **Return type**

`Dataset`

- **Returns**

A new `Dataset` object for the dataset.
If `dataset_name` is set and there are several
datasets with that name, return an arbitrary one.


* * *

### Dataset.delete [​](https://clear.ml/docs/latest/docs/references/hyperdataset/\#datasetdelete "Direct link to Dataset.delete")

**_classmethod_ delete(dataset\_id=None, dataset\_name=None, delete\_all\_versions=False, force=False, delete\_sources=False, show\_progress=True, dataset\_project=None)**

Delete a dataset from the system

If several datasets with the name dataset\_name exist, delete an arbitrary one.
Notice that `delete_sources` has no effect in this case.

info

dataset\_id and dataset\_name are mutually exclusive. Setting both to non-None values will raise a
UsageError exception.

- **Parameters**
  - **dataset\_id** ( _str_ ) – The ID of the dataset.

  - **dataset\_name** ( _str_ ) – The name of the dataset.

  - **delete\_all\_versions** ( _bool_ ) – If `True`, delete the dataset with
    all of its versions. If `False`, expect the dataset to have no
    versions. If there are, raise an exception. Default: `False`.

  - **force** ( _bool_ ) – If `True`, and `delete_all_versions`
    is `True`, delete also published versions. If `False`, and
    `delete_all_versions` is `True`, raise an exception
    if there is a published version in the dataset.
    If `delete_all_versions` is `False`, this has
    no effect. Default: `False`

  - **delete\_sources** ( _bool_ ) – Delete sources associated with the deleted frames in the dataset.
    Supported source locations are: s3, gs and azure. In case a connection
    cannot be established with the cloud provider or a source deletion failed, the operation will abort.
    This parameter is ignored if `delete_all_versions` is False.

  - **show\_progress** ( _bool_ ) – If True, show progress bar when deleting sources. If False,
    disable the progress bar. This parameter is ignored if `delete_sources` is False.
    Note that tqdm needs to be installed for this to work.

  - **dataset\_project** ( _str_ ) – The project name of the dataset.
- **Return type**

`None`


* * *

### create\_version [​](https://clear.ml/docs/latest/docs/references/hyperdataset/\#create_version "Direct link to create_version")

**create\_version(version\_name, description=None, parent\_version\_ids=None, parent\_version\_names=None, raise\_if\_exists=False, auto\_upload\_destination=None, local\_dataset\_root\_path=None)**

Create and return a new [`DatasetVersion`](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion#allegroai.datasetversion.DatasetVersion) for this Dataset.

info

parent\_version\_ids and parent\_version\_names are mutually
exclusive. Setting both to non-None values will raise a
UsageError exception.

- **Parameters**
  - **version\_name** ( _str_ ) – The new version name.

  - **description** ( _str_ ) – A free text to describe the version.

  - **parent\_version\_ids** ( _list_ ) – A list of the new version parents
    IDs. All IDs must be existing version’s IDs in this dataset.
    Currently support only a single parent for version. This is a list
    for future compatibility.

  - **parent\_version\_names** ( _list_ ) – A list of the new version parents
    names. All names must be existing version’s names in this dataset.
    Currently support only a single parent for version. This is a list
    for future compatibility.

  - **raise\_if\_exists** ( _bool_ ) – If `False` (the default) and a version
    with the name `version_name` exists in this dataset, return that version.
    If `True`, raise a `ValueError` exception.

  - **auto\_upload\_destination** ( _str_ ) – If specified any local file linked by a SingleFrame/FrameGroup,
    will be automatically uploaded to the destination storage.

  - **local\_dataset\_root\_path** ( _Union_ _\[_ _str_ _,_ _Path_ _\]_ ) – Required if `auto_upload_destination` is provided.
    It should point to the common folder for all local source files
- **Return type**

[`DatasetVersion`](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion#allegroai.datasetversion.DatasetVersion)

- **Returns**

A new [`DatasetVersion`](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion#allegroai.datasetversion.DatasetVersion) object with the name
`version_name` in this Dataset.


* * *

### get\_version [​](https://clear.ml/docs/latest/docs/references/hyperdataset/\#get_version "Direct link to get_version")

**get\_version(version\_id=None, version\_name=None, auto\_upload\_destination=None, local\_dataset\_root\_path=None, raise\_on\_multiple=False)**

Return a [`DatasetVersion`](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion#allegroai.datasetversion.DatasetVersion) object of a version in this dataset.

info

version\_id and version\_name are mutually exclusive. setting both to non-None values will raise
a UsageError exception.

- **Parameters**
  - **version\_id** ( _str_ ) – The ID of the version to get.

  - **version\_name** ( _str_ ) – The name of the version to get.
    If several versions exist with that name, return an arbitrary one.

  - **auto\_upload\_destination** ( _str_ ) – If specified any local file linked by a SingleFrame/FrameGroup,
    will be automatically uploaded to the destination storage.

  - **local\_dataset\_root\_path** ( _Union_ _\[_ _str_ _,_ _Path_ _\]_ ) – Required if `auto_upload_destination` is provided.
    It should point to the common folder for all local source files

  - **raise\_on\_multiple** ( _bool_ ) – Raise error if multiple versions are found
- **Return type**

[`DatasetVersion`](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion#allegroai.datasetversion.DatasetVersion)

- **Returns**

A [`DatasetVersion`](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion#allegroai.datasetversion.DatasetVersion) object of the desired version from
this dataset.


* * *

### get\_versions [​](https://clear.ml/docs/latest/docs/references/hyperdataset/\#get_versions "Direct link to get_versions")

**get\_versions(only\_published=False)**

Return a list of all the versions of a Dataset

- **Parameters**

**only\_published** ( _bool_ ) – If `True`, return only published versions.
If `False`, return all versions.

- **Return type**

`List`\[ [`DatasetVersion`](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion#allegroai.datasetversion.DatasetVersion)\]

- **Returns**

A list of [`DatasetVersion`](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion#allegroai.datasetversion.DatasetVersion) objects for all the
versions in this dataset.


* * *

### delete\_version [​](https://clear.ml/docs/latest/docs/references/hyperdataset/\#delete_version "Direct link to delete_version")

**delete\_version(version\_id=None, version\_name=None, force=False, delete\_sources=False, show\_progress=True)**

Delete a version from this dataset.

info

version\_id and version\_name are mutually exclusive. Setting both to non-None values will raise
a UsageError exception.

- **Parameters**
  - **version\_id** ( _str_ ) – The ID of the version to delete.

  - **version\_name** ( _str_ ) – The name of the version to delete. If several
    versions with this name exist in this dataset, delete an arbitrary one.

  - **force** ( _bool_ ) – If `True`, delete even if version is published.
    Default: `False`.

  - **delete\_sources** ( _bool_ ) – Delete sources associated with the deleted frames in the dataset.
    Supported source locations are: s3, gs and azure. In case a connection
    cannot be established with the cloud provider or a source deletion failed, the operation will abort.
    If multiple versions with the same `version_name` are found, this parameter is ignored

  - **show\_progress** ( _bool_ ) – If True, show progress bar when deleting sources. If False,
    disable the progress bar. This parameter is ignored if `delete_sources` is False.
    Note that tqdm needs to be installed for this to work.
- **Return type**

`None`


* * *

### add\_tags [​](https://clear.ml/docs/latest/docs/references/hyperdataset/\#add_tags "Direct link to add_tags")

**add\_tags(tags)**

Add tags (short string) to classify the dataset. Old tags are not deleted

- **Parameters**

**tags** (`Union`\[`str`, `Sequence`\[`str`\]\]) – The tags to add to the dataset

- **Return type**

`None`


* * *

### remove\_tags [​](https://clear.ml/docs/latest/docs/references/hyperdataset/\#remove_tags "Direct link to remove_tags")

**remove\_tags(tags=None)**

Remove tags from the dataset

- **Parameters**

**tags** (`Union`\[`str`, `List`\[`str`\], `None`\]) – The tags to remove from the dataset. If None (default),
remove all tags

- **Return type**

`None`


* * *

### get\_dataset\_webpage [​](https://clear.ml/docs/latest/docs/references/hyperdataset/\#get_dataset_webpage "Direct link to get_dataset_webpage")

**get\_dataset\_webpage()**

Return the Hyper Dataset’s web page address.
For example: `https://your_web_server/datasets/73757bd349634b86ae4b66ef5ed412df`

- **Return type**

`str`

- **Returns**

http/s URL link


- [_class_ datasetversion.Dataset()](https://clear.ml/docs/latest/docs/references/hyperdataset/#class-datasetversiondataset)
  - [id](https://clear.ml/docs/latest/docs/references/hyperdataset/#id)
  - [name](https://clear.ml/docs/latest/docs/references/hyperdataset/#name)
  - [project](https://clear.ml/docs/latest/docs/references/hyperdataset/#project)
  - [Dataset.create](https://clear.ml/docs/latest/docs/references/hyperdataset/#datasetcreate)
  - [Dataset.get](https://clear.ml/docs/latest/docs/references/hyperdataset/#datasetget)
  - [Dataset.delete](https://clear.ml/docs/latest/docs/references/hyperdataset/#datasetdelete)
  - [create\_version](https://clear.ml/docs/latest/docs/references/hyperdataset/#create_version)
  - [get\_version](https://clear.ml/docs/latest/docs/references/hyperdataset/#get_version)
  - [get\_versions](https://clear.ml/docs/latest/docs/references/hyperdataset/#get_versions)
  - [delete\_version](https://clear.ml/docs/latest/docs/references/hyperdataset/#delete_version)
  - [add\_tags](https://clear.ml/docs/latest/docs/references/hyperdataset/#add_tags)
  - [remove\_tags](https://clear.ml/docs/latest/docs/references/hyperdataset/#remove_tags)
  - [get\_dataset\_webpage](https://clear.ml/docs/latest/docs/references/hyperdataset/#get_dataset_webpage)