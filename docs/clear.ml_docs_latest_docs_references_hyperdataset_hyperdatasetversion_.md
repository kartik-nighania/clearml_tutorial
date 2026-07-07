---
url: "https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/"
title: "DatasetVersion | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

## _class_ datasetversion.DatasetVersion() [​](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/\#class-datasetversiondatasetversion "Direct link to class-datasetversiondatasetversion")

`DatasetVersion` represents a specific version in a dataset.

warning

Do not instantiate directly.
Use DatasetVersion.get\_version method instead.

* * *

### BulkContext [​](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/\#bulkcontext "Direct link to BulkContext")

**class BulkContext**

A context manager to modify frames (i.e. add/update/remove) in bulk.

Use `DatasetVersion.get_bulk_context` to obtain.

The bulk context allows modifying the version by adding/updating/deleting
of frames one at a time, but the actual update request will happen in bulk.
The update request (flush) will happen every
`flush_threshold` updates, or upon `__exit__`.

Create Bulk context for automatically flushing frames

- **Parameters**
  - **dv** (`DatasetVersion`) – DatasetVersion object to use

  - **flush\_threshold** (`Optional`\[`int`\]) – If provided flush every X frames

  - **log** (`Optional`\[`Logger`\]) – Optional, provide external logger

  - **refresh\_version\_stats** (`Optional`\[`bool`\]) – automatically refresh version statistics (default: True)

  - **auto\_upload\_destination** (`Optional`\[`str`\]) – If specified any local file linked by a SingleFrame/FrameGroup,
    will be automatically uploaded to the destination storage.

  - **local\_dataset\_root\_path** ( _Union_ _\[_ _str_ _,_ _Path_ _\]_ ) – Required if `auto_upload_destination` is provided.
    It should point to the common folder for all local source files

  - **allow\_update** (`bool`) – If False (default), all frame operations will use the “add” action and “update” will
    not be used (i.e. even frames collected using the BulkContext.update() call will be added, not updated).
    This is an advanced setting, please change only if you understand the limitations of using update. Note
    that when using update, provided frame data is merged with the existing indexed frame data - this means
    frame fields cannot be removed when using the update operation.

* * *

### add\_frame [​](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/\#add_frame "Direct link to add_frame")

**BulkContext.add\_frame(frame, warn\_on\_duplicate\_frames=False)**

NOTICE! If frames already contain frame.id field, they will update (overwrite) existing frames.
If not provided, frame.id is generated based on the source URI.
If a local file should be uploaded but has already been previously uploaded, the existing URI
for that file will be reused, otherwise the file will be uploaded.

info

Only available if version is still in draft (writable) mode

- **Parameters**
  - **frame** ( _DatasetVersion.Frame_ ) – The frame to add to the version.

  - **warn\_on\_duplicate\_frames** (`Optional`\[`bool`\]) – If True, issue a warning when adding a frame with an ID
    that was previously added to this instance (default False)
- **Return type**

`None`


* * *

### delete\_frame [​](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/\#delete_frame "Direct link to delete_frame")

**BulkContext.delete\_frame(frame, delete\_sources=False)**

Delete a frame from the current `DatasetVersion`.

The frame may be represented by an ID string, or a
`DatasetVersion.Frame` object. Frames are deleted by their IDs,
all other frame attributes (if exists) are ignored.

info

Only available if version is still in draft (writable) mode.

- **Parameters**
  - **frame** (`Union`\[ [`FrameGroup`](https://clear.ml/docs/latest/docs/references/hyperdataset/framegroup#allegroai.dataframe.FrameGroup), [`SingleFrame`](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe#allegroai.dataframe.SingleFrame), `str`, `None`\]) – The frame to delete (frame object or ID string)

  - **delete\_sources** (`bool`) – Delete sources associated with the deleted frames in the dataset.
    Supported source locations are: s3, gs and azure. In case a connection
    cannot be established with the cloud provider or a source deletion failed, the operation will abort.
- **Return type**

`None`


* * *

### flush [​](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/\#flush "Direct link to flush")

**BulkContext.flush()**

Send any outstanding version changes.

Any updates made using this `BulkContext` are
sent to the server.

- **Return type**

`None`


* * *

### update\_frame [​](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/\#update_frame "Direct link to update_frame")

**BulkContext.update\_frame(frame)**

Update an existing frame in the current `DatasetVersion`.

Find the frame by its ID, and change its properties to match that
of the frame object passed in frame. Frames exist in a version if they
were previously added (e.g. by
`update_frame`), or if they exist
in a parent version. If the frame object does not have an ID,
create a new frame.

info

Only available if version is still in draft (writable) mode.

- **Parameters**

**frame** ( _DatasetVersion.Frame_ ) – The frame to update.

- **Return type**

`None`


* * *

### version\_id [​](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/\#version_id "Direct link to version_id")

**property version\_id**

Version ID string of this specific dataset/version

- **Return type**

`str`


* * *

### version\_name [​](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/\#version_name "Direct link to version_name")

**property version\_name**

Dataset version name, not necessarily unique

- **Return type**

`str`


* * *

### dataset\_id [​](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/\#dataset_id "Direct link to dataset_id")

**property dataset\_id**

Dataset ID string of this specific dataset

- **Return type**

`str`


* * *

### dataset\_name [​](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/\#dataset_name "Direct link to dataset_name")

**property dataset\_name**

Dataset name, must be a unique name

- **Return type**

`str`


* * *

### draft [​](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/\#draft "Direct link to draft")

**property draft**

Draft flag of the dataset/version, i.e. is this version still writable
or is it locked and cannot be changed.

- **Return type**

`bool`


* * *

### last\_updated [​](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/\#last_updated "Direct link to last_updated")

**property last\_updated**

Return the timestamp of the last updated frame in the dataset version

- **Return type**

`datetime`


* * *

### comment [​](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/\#comment "Direct link to comment")

**property comment**

Return the string comment of the specific Dataset Version

- **Return type**

`str`


* * *

### DatasetVersion.create\_new\_dataset [​](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/\#datasetversioncreate_new_dataset "Direct link to DatasetVersion.create_new_dataset")

**_classmethod_ create\_new\_dataset(dataset\_name=None, description=None, tags=None, raise\_if\_exists=False, dataset\_project=None)**

Create a new dataset in the system and return a [`Dataset`](https://clear.ml/docs/latest/docs/references/hyperdataset/#allegroai.datasetversion.Dataset) object for it.

- **Parameters**
  - **dataset\_name** ( _str_ ) – The name of the new dataset.

  - **description** ( _str_ ) – A free text to describe the dataset.

  - **tags** ( _list_ ) – A list of tags (short strings) to classify the dataset.

  - **raise\_if\_exists** ( _bool_ ) – If False (the default) and there is a dataset
    with the name `dataset_name`, return the existing
    [`Dataset`](https://clear.ml/docs/latest/docs/references/hyperdataset/#allegroai.datasetversion.Dataset). If True and there is a dataset with the name
    `dataset_name`, raise `ValueError` exception.

  - **dataset\_project** ( _str_ ) – A project name for the newly created dataset.
- **Return type**

[`Dataset`](https://clear.ml/docs/latest/docs/references/hyperdataset/#allegroai.datasetversion.Dataset)

- **Returns**

A new [`Dataset`](https://clear.ml/docs/latest/docs/references/hyperdataset/#allegroai.datasetversion.Dataset) object for the newly created dataset.


* * *

### DatasetVersion.get\_current [​](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/\#datasetversionget_current "Direct link to DatasetVersion.get_current")

**_classmethod_ get\_current(dataset\_id=None, dataset\_name=None, auto\_upload\_destination=None, local\_dataset\_root\_path=None, dataset\_project=None)**

Return a `DatasetVersion` object for the current write-enabled version of the dataset

- **Parameters**
  - **dataset\_id** ( _str_ ) – The ID of the dataset of the version to retrieve.

  - **dataset\_name** ( _str_ ) – The name of the dataset of the version to retrieve.

  - **auto\_upload\_destination** ( _str_ ) – If specified any local file linked by a SingleFrame/FrameGroup,
    will be automatically uploaded to the destination storage.

  - **local\_dataset\_root\_path** ( _Union_ _\[_ _str_ _,_ _Path_ _\]_ ) – Required if `auto_upload_destination` is provided.
    It should point to the common folder for all local source files

  - **dataset\_project** (`Optional`\[`str`\]) – The project of the dataset to retrieve.
- **Return type**

`DatasetVersion`

- **Returns**

`DatasetVersion` object representing the selected version.


info

dataset\_id and dataset\_name are mutually exclusive. Setting both to non-None values will raise
a UsageError exception.

* * *

### DatasetVersion.remove\_version [​](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/\#datasetversionremove_version "Direct link to DatasetVersion.remove_version")

**_classmethod_ remove\_version(dataset\_id=None, dataset\_name=None, version\_id=None, version\_name=None, force=False, dataset\_project=None)**

Remove a dataset’s version from the system.

info

dataset\_id and dataset\_name are mutually exclusive. Setting both to non-None values will raise
a UsageError exception.

info

version\_id and version\_name are mutually exclusive. Setting both to non-None values will raise
a UsageError exception.

- **Parameters**
  - **dataset\_id** ( _str_ ) – The ID of the dataset to be removed.

  - **dataset\_name** ( _str_ ) – The name of the dataset to be removed.

  - **version\_id** ( _str_ ) – The ID of the version to be removed.

  - **version\_name** ( _str_ ) – The name of the version to be removed.

  - **force** ( _bool_ ) – If `True`, delete even if version is published.
    Default: `False`

  - **dataset\_project** ( _str_ ) – The project of the dataset to be removed.
- **Return type**

`None`


* * *

### DatasetVersion.get\_version [​](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/\#datasetversionget_version "Direct link to DatasetVersion.get_version")

**_classmethod_ get\_version(dataset\_id=None, dataset\_name=None, version\_id=None, version\_name=None, auto\_upload\_destination=None, local\_dataset\_root\_path=None, raise\_on\_multiple=False, dataset\_project=None)**

Return a `DatasetVersion` object for a specific version

info

If no version name/id is provided, the current version of the dataset is returned.

info

dataset\_id and dataset\_name are mutually exclusive. Setting both to non-None values will raise
a UsageError exception.

- **Parameters**
  - **dataset\_id** ( _str_ ) – The ID of the dataset of the version to retrieve.

  - **dataset\_name** ( _str_ ) – The name of the dataset of the version to retrieve.

  - **version\_id** ( _str_ ) – \[optional\] The ID of the version to retrieve.

  - **version\_name** ( _str_ ) – \[optional\] The name of the version to retrieve.

  - **auto\_upload\_destination** ( _str_ ) – If specified any local file linked by a SingleFrame/FrameGroup,
    will be automatically uploaded to the destination storage.

  - **local\_dataset\_root\_path** ( _Union_ _\[_ _str_ _,_ _Path_ _\]_ ) – Required if `auto_upload_destination` is provided.
    It should point to the common folder for all local source files

  - **raise\_on\_multiple** ( _bool_ ) – Raise error if multiple versions are found

  - **dataset\_project** ( _str_ ) – The project of the dataset of the version to retrieve.
- **Return type**

`DatasetVersion`

- **Returns**

`DatasetVersion` object representing the selected version.


* * *

### DatasetVersion.get\_single\_frame [​](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/\#datasetversionget_single_frame "Direct link to DatasetVersion.get_single_frame")

**_classmethod_ get\_single\_frame(frame\_id, dataset\_id=None, dataset\_name=None, version\_id=None, version\_name=None, dataset\_project=None)**

Return a `SingleFrame` / `FrameGroup`
object with the requested frame\_id (UUID) from a specific dataset version

- **Parameters**
  - **frame\_id** ( _str_ ) – The UUID of the requested frame id

  - **dataset\_id** ( _str_ ) – The ID of the dataset of the version to retrieve.

  - **dataset\_name** ( _str_ ) – The name of the dataset of the version to retrieve.

  - **version\_id** ( _str_ ) – The ID of the version to retrieve.

  - **version\_name** ( _str_ ) – The name of the version to retrieve.

  - **dataset\_project** ( _str_ ) – The project of the dataset of the version to retrieve.
- **Return type**

`Union`\[ [`FrameGroup`](https://clear.ml/docs/latest/docs/references/hyperdataset/framegroup#allegroai.dataframe.FrameGroup), [`SingleFrame`](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe#allegroai.dataframe.SingleFrame)\]

- **Returns**

SingleFrame / FrameGroup object representing the requested frame


info

dataset\_id and dataset\_name are mutually exclusive. Setting both to non-None values will raise
a UsageError exception.

* * *

### DatasetVersion.get\_frames\_by\_source [​](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/\#datasetversionget_frames_by_source "Direct link to DatasetVersion.get_frames_by_source")

**_classmethod_ get\_frames\_by\_source(source\_uri, dataset\_id=None, dataset\_name=None, version\_id=None, version\_name=None, dataset\_project=None)**

Return a list of `SingleFrame` / `FrameGroup`
objects with the requested source\_uri pattern from a specific dataset version

- **Parameters**
  - **source\_uri** ( _str_ ) – Source uri match pattern.
    Examples: ‘/home/folder/ _’ or ‘_/folder/\*’ or ‘ [https://domain.com/folder/\*’](https://domain.com/folder/*%E2%80%99) or ‘s3://bucket/folder/\*’ etc.

  - **dataset\_id** ( _str_ ) – The ID of the dataset of the version to retrieve.

  - **dataset\_name** ( _str_ ) – The name of the dataset of the version to retrieve.

  - **version\_id** ( _str_ ) – The ID of the version to retrieve.

  - **version\_name** ( _str_ ) – The name of the version to retrieve.

  - **dataset\_project** ( _str_ ) – The project of the dataset of the version to retrieve.
- **Return type**

`List`\[`Union`\[ [`SingleFrame`](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe#allegroai.dataframe.SingleFrame), [`FrameGroup`](https://clear.ml/docs/latest/docs/references/hyperdataset/framegroup#allegroai.dataframe.FrameGroup)\]\]

- **Returns**

list of SingleFrame / FrameGroup object representing the requested frame


info

dataset\_id and dataset\_name are mutually exclusive. Setting both to non-None values will raise
a UsageError exception.

* * *

### DatasetVersion.get\_frames\_by\_ids [​](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/\#datasetversionget_frames_by_ids "Direct link to DatasetVersion.get_frames_by_ids")

**_classmethod_ get\_frames\_by\_ids(frame\_ids, projection=None, dataset\_id=None, dataset\_name=None, version\_id=None, version\_name=None, dataset\_project=None)**

Return a list of `SingleFrame` / `FrameGroup`
objects with the requested frame IDs from a specific dataset version

info

Calling DatasetVersion.get\_frames\_by\_ids is deprecated starting version 3.8,
and will be removed in favor of using the instance method call dataset\_version.get\_frames\_by\_ids by 4Q 2023

- **Parameters**


  - **frame\_ids** (`Collection`\[`str`\]) – A collection of frame ID strings.

  - **projection** (`Optional`\[`Collection`\[`str`\]\]) – Used to select which parts of the frame will be returned.
    Each string represents a field or sub-field (using dot-separated notation).
    In order to specify a specific array element, use array index as a field name.
    To specify all array elements, use ‘\*’.
    To see supported fields for projection, see the schema at backend\_api.services.frames.Frame.
    If this argument is set, the values the iterator returns are dictionaries representing each frame


For example:

```python
dataview.get_iterator(projection=['id', 'dataset.id', 'sources'])

# will return an iterator that yields dictionaries with the following fields:

#  {

#    'id': '514504adbb6a91620eefa3e21ecfcc31',

#    'dataset': {

#      'id': 'df3638ec95454589bf86ba97f344f697'

#    },

#    'sources': [\
\
#      {\
\
#        'id': 'Frame',\
\
#        'uri': 'https://clearml-public.s3.amazonaws.com/datasets/food_dataset/pizza/3724187.jpg',\
\
#        'timestamp': 0,\
\
#        'preview': {\
\
#          'uri': 'https://clearml-public.s3.amazonaws.com/datasets/food_dataset/pizza/3724187.jpg',\
\
#          'timestamp': 0\
\
#        }\
\
#      }\
\
#    ]

#  }
```

  - **dataset\_id** ( _str_ ) – The ID of the dataset of the version to retrieve.

  - **dataset\_name** ( _str_ ) – The name of the dataset of the version to retrieve.

  - **version\_id** ( _str_ ) – The ID of the version to retrieve.

  - **version\_name** ( _str_ ) – The name of the version to retrieve.

  - **dataset\_project** ( _str_ ) – The project of the dataset of the version to retrieve.


info

When calling this method as an instance method, dataset\_id, dataset\_name, dataset\_project, version\_id, and version\_name are not required.

- **Return type**

`Union`\[`List`\[`Union`\[ [`SingleFrame`](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe#allegroai.dataframe.SingleFrame), [`FrameGroup`](https://clear.ml/docs/latest/docs/references/hyperdataset/framegroup#allegroai.dataframe.FrameGroup)\]\], `List`\[`dict`\]\]

- **Returns**

A list of SingleFrame / FrameGroup objects or a list of dicts representing the requested frames.



info





dataset\_id and dataset\_name are mutually exclusive. Setting both to non-None values will raise
a UsageError exception.


* * *

### DatasetVersion.create\_snapshot [​](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/\#datasetversioncreate_snapshot "Direct link to DatasetVersion.create_snapshot")

**_classmethod_ create\_snapshot(version\_name=None, version\_id=None, dataset\_name=None, dataset\_id=None, publish\_name=None, publish\_comment=None, publish\_metadata=None, child\_name=None, child\_comment=None, child\_metadata=None, dataset\_project=None)**

Publishes the specified version and creates a draft child version

- **Parameters**
  - **version\_name** ( _str_ ) – The name of the draft version for the snapshot.

  - **version\_id** ( _str_ ) – The ID of the draft version for the snapshot.

  - **dataset\_name** ( _str_ ) – The name of the dataset.

  - **dataset\_id** ( _str_ ) – The ID of the dataset to create the version in.

  - **publish\_name** ( _str_ ) – New name for the published version. The default value is ‘snapshot <date-time>’.

  - **publish\_comment** ( _str_ ) – New comment for the published version. The default value is
    ‘published at <date-time> by <user>’.

  - **publish\_metadata** ( _dict_ ) – User-specified metadata object for the published version.
    Keys can not include ‘$’ and ‘.’.

  - **child\_name** ( _str_ ) – Name for the child version. If not provided then the name of the parent version is taken.

  - **child\_comment** ( _str_ ) – Comment for the child version.

  - **child\_metadata** ( _dict_ ) – User-specified metadata object for the child version.
    Keys must not include ‘$’ and ‘.’.

  - **dataset\_project** ( _str_ ) – The project of the dataset
- **Return type**

`DatasetVersion`

- **Returns**

`DatasetVersion` object representing the new draft child version.


info

If no version\_name/id is provided, the current version of the dataset is the snapshot version.

info

dataset\_id and dataset\_name are mutually exclusive. Setting both to non-None values will raise
a UsageError exception.

info

version\_id and version\_name are mutually exclusive. Setting both to non-None values will raise
a UsageError exception.

* * *

### DatasetVersion.create\_version [​](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/\#datasetversioncreate_version "Direct link to DatasetVersion.create_version")

**_classmethod_ create\_version(version\_name, description=None, dataset\_id=None, dataset\_name=None, parent\_version\_ids=None, parent\_version\_names=None, raise\_if\_exists=False, auto\_upload\_destination=None, local\_dataset\_root\_path=None, dataset\_project=None)**

Create a new version in a dataset with a specific name.

If a version by that name already exists and in draft mode (i.e. writable), return that one,
unless `raise_if_exists` is `True`, than raise `ValueError`

- **Parameters**
  - **version\_name** ( _str_ ) – The name of the new version.

  - **description** ( _str_ ) – Description of the new dataset version

  - **dataset\_id** ( _str_ ) – The ID of the dataset to create the version in.

  - **dataset\_name** ( _str_ ) – The name of the dataset to create the version in.

  - **parent\_version\_ids** ( _list_ ) – A list of the new version parents
    IDs. All IDs must be existing version’s IDs in this dataset.
    Currently, support only a single parent for version. This is a list
    for future compatibility.

  - **parent\_version\_names** ( _list_ ) – A list of the new version parents
    names. All names must be existing version’s names in this dataset.
    Currently, support only a single parent for version. This is a list
    for future compatibility.

  - **raise\_if\_exists** ( _bool_ ) – If `True` and a version by name
    `name` already exists, raise
    `ValueError`. If `False` and a version by that name already
    exists, return it.

  - **auto\_upload\_destination** ( _str_ ) – If specified any local file linked by a SingleFrame/FrameGroup,
    will be automatically uploaded to the destination storage.

  - **local\_dataset\_root\_path** ( _Union_ _\[_ _str_ _,_ _Path_ _\]_ ) – Required if `auto_upload_destination` is provided.
    It should point to the common folder for all local source files

  - **dataset\_project** ( _str_ ) – The project of dataset to create the version in.
- **Return type**

`DatasetVersion`

- **Returns**

New `DatasetVersion` object representing the new version.


info

dataset\_id and dataset\_name are mutually exclusive. Setting both to non-None values will raise
a UsageError exception.

* * *

### DatasetVersion.get\_versions [​](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/\#datasetversionget_versions "Direct link to DatasetVersion.get_versions")

**_classmethod_ get\_versions(dataset\_name=None, dataset\_id=None, only\_published=False, only\_draft=False, dataset\_project=None)**

Return a list of all versions in a dataset.

- **Parameters**
  - **dataset\_name** ( _str_ ) – The name of the dataset. If several datasets
    with this name exist, select an arbitrary one.

  - **dataset\_id** ( _str_ ) – The ID of the dataset to list.

  - **only\_published** ( _bool_ ) – If `True`, return only published versions.
    If `False`, return all versions.

  - **only\_draft** ( _bool_ ) – If `True`, return only draft (write enabled) versions.
    If `False`, return all versions.

  - **dataset\_project** (`Optional`\[`str`\]) – The project of the dataset to list
- **Return type**

`List`\[`DatasetVersion`\]

- **Returns**

A list of `DatasetVersion`, one for each version of the dataset.
Versions are sorted by update time, from latest updated (\[0\]) to oldest


* * *

### DatasetVersion.get\_datasets [​](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/\#datasetversionget_datasets "Direct link to DatasetVersion.get_datasets")

**_classmethod_ get\_datasets(tags=None)**

Return a list of all the dataset in the system, sorted by created time.

- **Parameters**

**tags** ( _list_ ) – Filter based on the requested list of tags (strings). To exclude a tag add “-” prefix to the
tag. Example: `["best", "-debug"]`.
The default behaviour is to join all tags with a logical “OR” operator.
To join all tags with a logical “AND” operator instead, use “\_\_$all” as the first string, for example:





```py
["__$all", "best", "experiment", "ever"]
```









To join all tags with AND, but exclude a tag use “\_\_$not” before the excluded tag, for example:





```py
["__$all", "best", "experiment", "ever", "__$not", "internal", "__$not", "test"]
```









The “OR” and “AND” operators apply to all tags that follow them until another operator is specified.
The NOT operator applies only to the immediately following tag.
For example:





```py
["__$all", "a", "b", "c", "__$or", "d", "__$not", "e", "__$and", "__$or" "f", "g"]
```









This example means (“a” AND “b” AND “c” AND (“d” OR NOT “e”) AND (“f” OR “g”)).
See [https://clear.ml/docs/latest/docs/clearml\_sdk/task\_sdk/#tag-filters](https://clear.ml/docs/latest/docs/clearml_sdk/task_sdk/#tag-filters) for more information.

- **Return type**

`List`\[`None`\]

- **Returns**

A list of `datasets.Dataset`, one for each dataset.
Datasets are sorted by created time, from the oldest to the newest


* * *

### get\_iterator [​](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/\#get_iterator "Direct link to get_iterator")

**get\_iterator(projection=None)**

Get an iterator for this version.

- **Parameters**

**projection** ( _Optional_ _\[_ _Sequence_ _\[_ _str_ _\]_ _\]_ ) – Used to select which parts of the frame will be returned.
Each string represents a field or sub-field (using dot-separated notation). In
order to specify a specific array element, use array index as a field name. To
specify all array elements, use ‘\*’.
If this argument is set, the values the iterator returns are dictionaries representing each frame

For example:





```python
version.get_iterator(projection=['id', 'dataset.id', 'sources'])

# will return an iterator that yields dictionaries with the following fields:

#  {

#    'id': '514504adbb6a91620eefa3e21ecfcc31',

#    'dataset': {

#      'id': 'df3638ec95454589bf86ba97f344f697'

#    },

#    'sources': [\
\
#      {\
\
#        'id': 'Frame',\
\
#        'uri': 'https://clearml-public.s3.amazonaws.com/datasets/food_dataset/pizza/3724187.jpg',\
\
#        'timestamp': 0,\
\
#        'preview': {\
\
#          'uri': 'https://clearml-public.s3.amazonaws.com/datasets/food_dataset/pizza/3724187.jpg',\
\
#          'timestamp': 0\
\
#        }\
\
#      }\
\
#    ]

#  }
```

- **Return type**

Generator\[Union\[“DatasetVersion.Frame”, dict\]\]

- **Returns**

An iterator on all the version’s frames.


* * *

### add\_frames [​](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/\#add_frames "Direct link to add_frames")

**add\_frames(frames, warn\_on\_duplicate\_frames=False, batch\_size=1000, refresh\_version\_stats=True, auto\_upload\_destination=None, local\_dataset\_root\_path=None, force\_upload=False, progress\_report=1, register\_on\_upload\_failure=False, upload\_retries=5, src\_to\_dst\_mapping=None, unregister\_on\_upload\_fail=True, max\_request\_size\_mb=None)**

Add frames to this `DatasetVersion`.
NOTICE! If frames already contain frame.id field, they will update (overwrite) existing frames.
If not provided, frame.id is generated based on the source URI.
If a local file should be uploaded but has already been previously uploaded, the existing URI
for that file will be reused, otherwise the file will be uploaded.

info

Only available if version is still in draft (writable) mode

- **Parameters**


  - **frames** ( _list_ ) – A list of new frames to save.

  - **warn\_on\_duplicate\_frames** ( _bool_ ) – If True, issue a warning when adding a frame with an ID
    that was previously added to this instance (default False)

  - **batch\_size** (`int`) – Number of frames in a single add request (default: 1000),
    batch\_size affects the speed of the upload, versus reliability. It does not limit the
    number of frames per call and in most cases there is no need to change it.

  - **refresh\_version\_stats** (`Optional`\[`bool`\]) – Automatically call `commit_version`
    after adding frames to refresh this version’s statistics.

  - **auto\_upload\_destination** (`Optional`\[`str`\]) – If specified any local file linked by a SingleFrame/FrameGroup,
    will be automatically uploaded to the destination storage.
    Examples: ‘s3://bucket/datasets/’, ‘gs://bucket/dataset’, ‘azure://bucket/dataset’,
    ‘ [http://clearml-server/bucket/dataset’](http://clearml-server/bucket/dataset%E2%80%99)


info

Notes:

1. The uploaded files will keep the same structure inside the designation storage under
     dataset\_id/version\_name.version\_id/ folders
2. If a file content hash is already registered, it will automatically link to
     the existing remote file instead of re-uploading the local copy
3. Inside the dataset/version folder the files are stored in the same path as on the local storage,
     relative to the provided local\_root\_dataset\_folder

  - **local\_dataset\_root\_path** ( _Union_ _\[_ _str_ _,_ _Path_ _\]_ ) – Required if `auto_upload_destination` is provided.
    Mutually\_exclusive with src\_to\_dst\_mapping. It should point to the common folder for all local source files.
    This root folder is used to detect the relative path of a single source file,
    to be uploaded to the remote storage.
    Example: `'auto_upload_destination='s3://bucket/datasets/', local_dataset_root_path='/home/user/data/'`
    will make sure a file ‘/home/user/data/images/01/1.jpg’ will be uploaded to:
    ‘s3://bucket/datasets/dataset\_id/version\_id/images/01/1.jpg’

  - **force\_upload** (`Optional`\[`bool`\]) – If True and `auto_upload_destination` is provided, will force to upload the frames

  - **progress\_report** (`Optional`\[`int`\]) – Report frame uploaded every `progress_report` frames uploaded/registered,
    at `batch_size` granularity. (default: report every batch)

  - **register\_on\_upload\_failure** – If True, register the frames even when they fail uploading

  - **upload\_retries** (`int`) – The number of times the upload of a frame should be retried in case of failure,
    before marking the frame as failed on upload and continuing to upload the other frames

  - **src\_to\_dst\_mapping** (`Optional`\[`Dict`\[`str`, `str`\]\]) – A dictionary mapping the source of the frames to the upload destination.
    Each source found in the dictionary will be uploaded to the corresponding destination.
    Mutually\_exclusive with auto\_upload\_destination

  - **unregister\_on\_upload\_fail** (`bool`) – A boolean that controls whether to delete frames that failed to be uploaded.

  - **max\_request\_size\_mb** (`Optional`\[`float`\]) – The maximum request size sent to the server when adding frames, in megabytes.
    If the size of the request exceeds this, it will be broken down into multiple requests.
    If the size of one frame alone exceeds this,
    then it will not be added and an error message will be returned.
- **Return type**

`List`\[`Dict`\]

- **Returns**

A list containing the frames that failed to upload or register. Each entry in the list is





```text
    a dictionary with the following key-value pairs:
```








  - ’frame’ - the frame that failed to be added

  - ’error’ - a string that describes the error

  - ’error\_type’ - can be ‘upload’, ‘validation’ or ‘register’. Indicates where the error occurred

* * *

### update\_frames [​](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/\#update_frames "Direct link to update_frames")

**update\_frames(frames, batch\_size=1000, refresh\_version\_stats=True, without\_fields=None)**

Update existing frames in this `DatasetVersion`.

Find each frame by its ID, and change its properties to match that
of the frame object passed in frames. Frames exist in a version if they
were previously added (e.g. by `update_frames`), or
if they exist in a parent version.
If the frame object does not have an ID, create a new frame.

info

Only available if version is still in draft (writable) mode

- **Parameters**


  - **frames** ( _list_ ) – A list of frames to update.

  - **batch\_size** ( _int_ ) – Number of frames in a single update request (default: 1000)
    batch\_size affects the speed of the upload, versus reliability. It does not limit the
    number of frames per call and in most cases there is no need to change it.

  - **refresh\_version\_stats** (`Optional`\[`bool`\]) – Automatically call `commit_version`
    after updating frames to refresh this version’s statistics.

  - **without\_fields** (`Optional`\[`List`\[`str`\]\]) – A list of fields to filter out of the frame object, when sending the update call.
    These fields correspond to the fields in allegroai.backend\_api.services.datasets.Frame.
    When this list is provided, the call will generate an update operation, otherwise an add operation will
    be used (see `add_frames`). Use a non-None value (such as \[\] or False) in this
    parameter to specify an update operation without providing any fields.


info

when using an update operation, removed frame fields are ignored (e.g. update cannot be used to
remove a field from the meta structure).

For example, to avoid sending the metadata:

```python
dataset_version.update_frames(frames, without_fields=["meta"])
```

- **Return type**

`None`


* * *

### delete\_frames [​](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/\#delete_frames "Direct link to delete_frames")

**delete\_frames(frames, batch\_size=1000, refresh\_version\_stats=True, delete\_sources=False)**

Delete frames from this `DatasetVersion`.

Frames may be represented by an ID string, or a
`DatasetVersion.Frame` object. Frames are deleted by their IDs,
all other frame attributes (if exists) are ignored.

info

Only available if version is still in draft (writable) mode.

- **Parameters**
  - **frames** (`Sequence`\[`Union`\[ [`FrameGroup`](https://clear.ml/docs/latest/docs/references/hyperdataset/framegroup#allegroai.dataframe.FrameGroup), [`SingleFrame`](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe#allegroai.dataframe.SingleFrame), `dict`, `None`\]\]) – A list of a frame objects, or frame IDs (string).

  - **batch\_size** ( _int_ ) – Number of frame ids in a single delete request (default: 1000)
    batch\_size affects the speed of the upload, versus reliability. It does not limit the
    number of frames per call and in most cases there is no need to change it.

  - **refresh\_version\_stats** (`Optional`\[`bool`\]) – Automatically call `commit_version`
    after deleting frames to refresh this version’s statistics.

  - **delete\_sources** (`bool`) – Delete sources associated with the deleted frames in the dataset.
    Supported source locations are: s3, gs and azure. In case a connection
    cannot be established with the cloud provider or a source deletion failed, the operation will abort.
- **Return type**

`None`


* * *

### get\_bulk\_context [​](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/\#get_bulk_context "Direct link to get_bulk_context")

**get\_bulk\_context(flush\_threshold=None, log=None, refresh\_version\_stats=True, auto\_upload\_destination=None, local\_dataset\_root\_path=None, allow\_update=False)**

Get a context manager for bulk updates to this version.

The bulk context allows add/edit/remove data frames on this version in
bulks instead of one by one.

info

There can only be one BulkContext per
DatasetVersion. A second call to
get\_bulk\_context will return the same
object.

info

only available if version is still in draft (writable) mode.

- **Parameters**


  - **flush\_threshold** ( _int_ ) – Commit the updates to the frames every
    `flush_threshold` updates. An update
    is a call to one of `BulkContext.add_frame`,
    `BulkContext.update_frame`, or `BulkContext.delete_frame`.

  - **log** (`Optional`\[`Logger`\]) – Logger object for the context to log to.
    Defaults to the datasetversion module logger.

  - **refresh\_version\_stats** (`Optional`\[`bool`\]) – Automatically call `commit_version`
    after deleting frames to refresh this version’s statistics.

  - **auto\_upload\_destination** (`Optional`\[`str`\]) – If specified any local file linked by a SingleFrame/FrameGroup,
    will be automatically uploaded to the destination storage.
    Examples: ‘s3://bucket/datasets/’, ‘gs://bucket/dataset’, ‘azure://bucket/dataset’,
    ‘ [http://clearml-server/bucket/dataset’](http://clearml-server/bucket/dataset%E2%80%99)


info

Notes:

1. The uploaded files will keep the same structure inside the designation storage under
     dataset\_id/version\_name.version\_id/ folders
2. If a file content hash is already registered, it will automatically link to
     the existing remote file instead of re-uploading the local copy
3. Inside the dataset/version folder the files are stored in the same path as on the local storage,
     relative to the provided local\_root\_dataset\_folder

  - **local\_dataset\_root\_path** ( _Union_ _\[_ _str_ _,_ _Path_ _\]_ ) – Required if `auto_upload_destination` is provided.
    It should point to the common folder for all local source files,
    This root folder is used to detect the relative path of a single source file,
    to be uploaded to the remote storage.
    Example: `'auto_upload_destination='s3://bucket/datasets/', local_dataset_root_path='/home/user/data/'`
    will make sure a file ‘/home/user/data/images/01/1.jpg’ will be uploaded to:
    ‘s3://bucket/datasets/dataset\_id/version\_id/images/01/1.jpg’

  - **allow\_update** (`bool`) – If False (default), all frame operations will use the “add” action and “update” will
    not be used (i.e. even frames collected using the BulkContext.update() call will be added, not updated).
    This is an advanced setting, please change only if you understand the limitations of using update. Note that
    when using update, provided frame data is merged with the existing indexed frame data - this means frame
    fields cannot be removed when using the update operation.
- **Return type**

`BulkContext`

- **Returns**

A bulk update context manager for this `DatasetVersion`


* * *

### flush [​](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/\#flush-1 "Direct link to flush")

**flush(refresh\_version\_stats=True)**

Send any outstanding version changes.

If a `BulkContext` was obtained by
`get_bulk_context`, any updates made using it are
sent to the server. If not, this is a no-op.

- **Parameters**

**refresh\_version\_stats** (`Optional`\[`bool`\]) – Automatically call `commit_version`
to refresh this version’s statistics.

- **Return type**

`None`


* * *

### commit\_version [​](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/\#commit_version "Direct link to commit_version")

**commit\_version(\*\*kwargs)**

Commit this **draft**`DatasetVersion`, with all the changes made so far.

Committing a version merges changes done to it with the parent version.
Further changes to the version are still possible.
This is a must step before publishing the version.

warning

This is a blocking method and may take time to finish.

- **Return type**

`CallResult`

- **Parameters**

**kwargs** ( _Any_ ) –


* * *

### publish\_version [​](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/\#publish_version "Direct link to publish_version")

**publish\_version()**

Publish this `DatasetVersion`.

After publishing a version it is no longer a draft version and no further
changes are allowed for this version.

- **Return type**

`bool`

- **Returns**

`True` if successful, `False` otherwise.


* * *

### get\_stats [​](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/\#get_stats "Direct link to get_stats")

**get\_stats()**

Returns this version’s statistics

- **Return type**

`None`


* * *

### get\_parent [​](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/\#get_parent "Direct link to get_parent")

**get\_parent()**

Returns the ID of this version’s parent version

- **Return type**

`str`


* * *

### get\_metadata [​](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/\#get_metadata "Direct link to get_metadata")

**get\_metadata()**

- **Return type**

`dict`

- **Returns**

return metadata (dict) of user defined values stored for the specific Dataset Version


* * *

### set\_metadata [​](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/\#set_metadata "Direct link to set_metadata")

**set\_metadata(metadata)**

Store metadata (dict) of user defined values stored for the specific Dataset Version

- **Parameters**

**metadata** ( _dict_ ) – key/value dictionary (with support for nested dictionaries)

- **Return type**

`bool`

- **Returns**

True if successful (locked/published versions cannot change version metadata)


* * *

### set\_version\_name [​](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/\#set_version_name "Direct link to set_version_name")

**set\_version\_name(name)**

Set a new name for this Dataset Version

- **Parameters**

**name** (`str`) – New name for the version

- **Return type**

`bool`

- **Returns**

True if successful


* * *

### set\_masks\_labels [​](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/\#set_masks_labels "Direct link to set_masks_labels")

**set\_masks\_labels(mask\_value\_label\_mapping)**

Store a global (dataset version wide) lookup for per pixel mask values to labels.
For example:

```json
{

  (0,0,0): ["background"],

  (1,1,1): ["person", "sitting"],

  (2,2,2): ["cat"],

}
```

Pixel masks label lookup is stored as a property on the dataset version metadata.
Specifically: `dataset.get_metadata()['mask_labels'] = {...}`

- **Parameters**

**mask\_value\_label\_mapping** ( _dict_ ) – key/value dictionary.
Key is a tuple of integers, and value is a list/tuple of strings

- **Return type**

`bool`

- **Returns**

True if successful (locked/published versions cannot change version metadata)


* * *

### get\_masks\_labels [​](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/\#get_masks_labels "Direct link to get_masks_labels")

**get\_masks\_labels()**

Get the global (dataset version wide) lookup for per pixel mask values to labels.
For example:

```json
{

  (0,0,0): ["background"],

  (1,1,1): ["person", "sitting"],

  (2,2,2): ["cat"],

}
```

Pixel masks label lookup is stored as a property on the dataset version metadata.
Specifically: `dataset.get_metadata()['mask_labels'] = {...}`

- **Return type**

`Dict`\[`tuple`, `tuple`\]

- **Returns**

key/value dictionary. key is a tuple of integers, and value is a list/tuple of strings


- [_class_ datasetversion.DatasetVersion()](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/#class-datasetversiondatasetversion)
  - [BulkContext](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/#bulkcontext)
  - [add\_frame](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/#add_frame)
  - [delete\_frame](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/#delete_frame)
  - [flush](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/#flush)
  - [update\_frame](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/#update_frame)
  - [version\_id](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/#version_id)
  - [version\_name](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/#version_name)
  - [dataset\_id](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/#dataset_id)
  - [dataset\_name](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/#dataset_name)
  - [draft](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/#draft)
  - [last\_updated](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/#last_updated)
  - [comment](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/#comment)
  - [DatasetVersion.create\_new\_dataset](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/#datasetversioncreate_new_dataset)
  - [DatasetVersion.get\_current](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/#datasetversionget_current)
  - [DatasetVersion.remove\_version](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/#datasetversionremove_version)
  - [DatasetVersion.get\_version](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/#datasetversionget_version)
  - [DatasetVersion.get\_single\_frame](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/#datasetversionget_single_frame)
  - [DatasetVersion.get\_frames\_by\_source](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/#datasetversionget_frames_by_source)
  - [DatasetVersion.get\_frames\_by\_ids](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/#datasetversionget_frames_by_ids)
  - [DatasetVersion.create\_snapshot](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/#datasetversioncreate_snapshot)
  - [DatasetVersion.create\_version](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/#datasetversioncreate_version)
  - [DatasetVersion.get\_versions](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/#datasetversionget_versions)
  - [DatasetVersion.get\_datasets](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/#datasetversionget_datasets)
  - [get\_iterator](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/#get_iterator)
  - [add\_frames](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/#add_frames)
  - [update\_frames](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/#update_frames)
  - [delete\_frames](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/#delete_frames)
  - [get\_bulk\_context](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/#get_bulk_context)
  - [flush](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/#flush-1)
  - [commit\_version](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/#commit_version)
  - [publish\_version](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/#publish_version)
  - [get\_stats](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/#get_stats)
  - [get\_parent](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/#get_parent)
  - [get\_metadata](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/#get_metadata)
  - [set\_metadata](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/#set_metadata)
  - [set\_version\_name](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/#set_version_name)
  - [set\_masks\_labels](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/#set_masks_labels)
  - [get\_masks\_labels](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion/#get_masks_labels)