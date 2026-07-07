---
url: "https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdataset/"
title: "HyperDataset | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdataset/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

## _class_ hyperdatasets.core.HyperDataset(project\_name, dataset\_name, version\_name, description=None, parent\_ids=None, field\_mappings=None, raise\_if\_exists=False) [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdataset/\#class-hyperdatasetscorehyperdatasetproject_name-dataset_name-version_name-descriptionnone-parent_idsnone-field_mappingsnone-raise_if_existsfalse "Direct link to class-hyperdatasetscorehyperdatasetproject_name-dataset_name-version_name-descriptionnone-parent_idsnone-field_mappingsnone-raise_if_existsfalse")

Create a new HyperDataset version within the requested project.

- **Parameters**


  - **project\_name** (`str`) – ClearML project name that will own the dataset

  - **dataset\_name** (`str`) – HyperDataset collection name (top-level dataset)

  - **version\_name** (`str`) – Version name to create (or reuse if it already exists)

  - **description** (`Optional`\[`str`\]) – Optional dataset description string

  - **parent\_ids** (`Optional`\[`List`\[`str`\]\]) – Optional list of parent dataset version IDs to link

  - **field\_mappings** (`Optional`\[`Dict`\[`str`, `Any`\]\]) – Optional mapping that defines vector-capable metadata fields.
    Provide the fully-qualified frame metadata path (e.g. `meta.my_vector`) and
    the corresponding field settings accepted by the ClearML backend / Elasticsearch
    dense vector type. For example:


```default
field_mappings = {

    "meta.qa_vector": {

        "type": "dense_vector",

        "element_type": "float",

        "dims": 768,

    }

}
```

When supplied, ClearML Server >= 3.25 is required and vector dimensions are
validated on every frame ingest or update.
  - **raise\_if\_exists** (`bool`) – Reserved flag for compatibility (currently unused)

* * *

### add\_data\_entries [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdataset/\#add_data_entries "Direct link to add_data_entries")

**add\_data\_entries(data\_entries, upload\_local\_files\_destination=None, batch\_size=1000, max\_workers=None, show\_progress=True, upload\_retries=5, force\_upload=False, max\_request\_size\_mb=None, hash\_sources=False)**

Upload and register a collection of data entries into the HyperDataset version.
Successful registrations automatically trigger a commit to refresh the version statistics.

- **Parameters**
  - **data\_entries** – Iterable of DataEntry instances to register

  - **upload\_local\_files\_destination** (`Optional`\[`str`\]) – Optional storage URI for uploading local sources

  - **batch\_size** (`int`) – Number of entries per backend registration batch

  - **max\_workers** (`Optional`\[`int`\]) – Maximum number of threads for upload work

  - **show\_progress** (`bool`) – Reserved for API compatibility (no progress emitted currently)

  - **upload\_retries** (`int`) – Number of upload retry attempts per file

  - **force\_upload** (`bool`) – Upload even when hashes indicate the source already exists

  - **max\_request\_size\_mb** (`Optional`\[`int`\]) – Optional upper bound for registration request payload size

  - **hash\_sources** (`bool`) – Whether to hash sources for deduplication prior to upload
- **Returns**

Dictionary containing upload and registration error mappings


* * *

### add\_tags [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdataset/\#add_tags "Direct link to add_tags")

**add\_tags(tags)**

Adds the provided tags to the list of tags attached to the dataset.

- **Parameters**

**tags** (`Union`\[`Sequence`\[`str`\], `str`\]) – The list of tags to add to the dataset (before normalization; see \_normalize\_tags method).

- **Return type**

`None`


* * *

### commit\_version [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdataset/\#commit_version "Direct link to commit_version")

**commit\_version(\*, publish=False, force=False, calculate\_stats=True, override\_stats=None, publishing\_task=None)**

Commit the bound HyperDataset version to refresh backend statistics.

- **Parameters**
  - **publish** (`bool`) – Publish the version after committing (optional)

  - **force** (`bool`) – Force publish even when annotation tasks reference the version

  - **calculate\_stats** (`Optional`\[`bool`\]) – Control statistics calculation during commit

  - **override\_stats** (`Optional`\[`Any`\]) – Optional statistics payload to persist as-is

  - **publishing\_task** (`Optional`\[`str`\]) – Annotation task identifier issuing the commit
- **Returns**

Backend response payload


* * *

### create\_snapshot [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdataset/\#create_snapshot "Direct link to create_snapshot")

**create\_snapshot()**

Publish a snapshot hyperdataset with parent equal to this hyperdataset.
Leaves this hyperdataset unchanged.

- **Return type**

`HyperDataset`

- **Returns**

A new HyperDataset bound to the newly created (current) child version


* * *

### dataset\_id [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdataset/\#dataset_id "Direct link to dataset_id")

**property dataset\_id: Optional\[str\]**

- **Return type**

`Optional`\[`str`\]

- **Returns**

HyperDataset dataset ID.


* * *

### HyperDataset.delete [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdataset/\#hyperdatasetdelete "Direct link to HyperDataset.delete")

\* _classmethod delete(dataset\_name, version\_name=None, project\_name=None, , force=False)_

Delete a dataset or a specific dataset version.

- **Parameters**
  - **dataset\_name** (`str`) – Dataset name to delete (required)

  - **version\_name** (`Optional`\[`str`\]) – Version name to delete. When omitted, the entire dataset is removed

  - **project\_name** (`Optional`\[`str`\]) – Optional project context when resolving by name

  - **force** (`bool`) – Force deletion even when there are protections
- **Return type**

`bool`

- **Returns**

True when deletion completes successfully


* * *

### HyperDataset.exists [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdataset/\#hyperdatasetexists "Direct link to HyperDataset.exists")

\* _classmethod exists(dataset\_name=None, version\_name=None, project\_name=None, , dataset\_id=None, version\_id=None)_

Check whether a dataset (and optionally a specific version) exists.

- **Parameters**
  - **dataset\_name** (`Optional`\[`str`\]) – Dataset collection name. Mutually exclusive with dataset\_id

  - **version\_name** (`Optional`\[`str`\]) – Dataset version name. Mutually exclusive with version\_id

  - **project\_name** (`Optional`\[`str`\]) – Optional project filter when searching by name

  - **dataset\_id** (`Optional`\[`str`\]) – Dataset identifier to query. Mutually exclusive with dataset\_name

  - **version\_id** (`Optional`\[`str`\]) – Version identifier to query. Mutually exclusive with version\_name
- **Return type**

`bool`

- **Returns**

True when the dataset (and requested version) can be found


* * *

### HyperDataset.get [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdataset/\#hyperdatasetget "Direct link to HyperDataset.get")

\* _classmethod get(dataset\_name=None, version\_name=None, project\_name=None, , dataset\_id=None, version\_id=None)_

Return a HyperDataset handle bound to an existing dataset/version.

- **Parameters**
  - **dataset\_name** (`Optional`\[`str`\]) – Dataset collection name. Mutually exclusive with dataset\_id

  - **version\_name** (`Optional`\[`str`\]) – Version name. Mutually exclusive with version\_id

  - **project\_name** (`Optional`\[`str`\]) – Optional ClearML project filter when using dataset\_name

  - **dataset\_id** (`Optional`\[`str`\]) – Dataset identifier. Mutually exclusive with dataset\_name

  - **version\_id** (`Optional`\[`str`\]) – Version identifier. Mutually exclusive with version\_name
- **Return type**

~HD

- **Returns**

HyperDataset instance pointing at the requested dataset/version


* * *

### get\_tags [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdataset/\#get_tags "Direct link to get_tags")

**get\_tags(reload=False)**

Returns tags attached to the dataset. Allows invalidating tags cache via `dataset.get_tags(reload=True)`.

- **Parameters**

**reload** (`bool`) – If set to `True`, tags will be fetched from the backend
and the local runtime cache will be updated.

- **Return type**

`List`\[`str`\]

- **Returns**

The list of tags attached to this dataset.


* * *

### HyperDataset.list [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdataset/\#hyperdatasetlist "Direct link to HyperDataset.list")

**_classmethod_ list(project\_name=None, partial\_name=None, tags=None, ids=None, recursive\_project\_search=True, include\_archived=True)**

List HyperDataset collections matching the provided filters.

- **Parameters**
  - **project\_name** (`Optional`\[`str`\]) – Optional project filter (matches project hierarchy when recursive)

  - **partial\_name** (`Optional`\[`str`\]) – Optional regex / partial dataset name filter

  - **tags** (`Optional`\[`Sequence`\[`str`\]\]) – Optional list of tags to filter by

  - **ids** (`Optional`\[`Sequence`\[`str`\]\]) – Optional list of dataset identifiers

  - **recursive\_project\_search** (`bool`) – Include subprojects when filtering by project\_name

  - **include\_archived** (`bool`) – Include archived datasets when True
- **Return type**

`List`\[`Dict`\[`str`, `Any`\]\]

- **Returns**

List of dictionaries describing the matching datasets


* * *

### project\_id [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdataset/\#project_id "Direct link to project_id")

**property project\_id: Optional\[str\]**

- **Return type**

`Optional`\[`str`\]

- **Returns**

ClearML Project ID associated with this HyperDataset.


* * *

### publish\_version [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdataset/\#publish_version "Direct link to publish_version")

**publish\_version(\*, force=False, publishing\_task=None)**

Publish the bound HyperDataset version.

- **Parameters**
  - **force** (`bool`) – Force publish even with active annotation tasks

  - **publishing\_task** (`Optional`\[`str`\]) – Annotation task identifier issuing the commit
- **Returns**

Backend response payload


* * *

### remove\_tags [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdataset/\#remove_tags "Direct link to remove_tags")

**remove\_tags(tags)**

Removes the provided tags from the list of tags attached to the dataset.

- **Parameters**

**tags** (`Union`\[`Sequence`\[`str`\], `str`\]) – The list of tags to remove from the dataset (before normalization; see \_normalize\_tags method).

- **Return type**

`None`


* * *

### set\_tags [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdataset/\#set_tags "Direct link to set_tags")

**set\_tags(tags)**

Overrides the existing tags on the dataset with the provided list of tags.

- **Parameters**

**tags** (`Union`\[`Sequence`\[`str`\], `str`\]) – The list of tags that will be on the dataset (before normalization; see \_normalize\_tags method).

- **Return type**

`None`


* * *

### tags [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdataset/\#tags "Direct link to tags")

**property tags: List\[str\]**

Pythonic alternative to `dataset.get_tags()`.

- **Return type**

`List`\[`str`\]

- **Returns**

The list of tags attached to this dataset.


* * *

### version\_id [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdataset/\#version_id "Direct link to version_id")

**property version\_id: Optional\[str\]**

- **Return type**

`Optional`\[`str`\]

- **Returns**

HyperDataset version ID.


- [_class_ hyperdatasets.core.HyperDataset(project\_name, dataset\_name, version\_name, description=None, parent\_ids=None, field\_mappings=None, raise\_if\_exists=False)](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdataset/#class-hyperdatasetscorehyperdatasetproject_name-dataset_name-version_name-descriptionnone-parent_idsnone-field_mappingsnone-raise_if_existsfalse)
  - [add\_data\_entries](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdataset/#add_data_entries)
  - [add\_tags](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdataset/#add_tags)
  - [commit\_version](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdataset/#commit_version)
  - [create\_snapshot](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdataset/#create_snapshot)
  - [dataset\_id](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdataset/#dataset_id)
  - [HyperDataset.delete](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdataset/#hyperdatasetdelete)
  - [HyperDataset.exists](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdataset/#hyperdatasetexists)
  - [HyperDataset.get](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdataset/#hyperdatasetget)
  - [get\_tags](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdataset/#get_tags)
  - [HyperDataset.list](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdataset/#hyperdatasetlist)
  - [project\_id](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdataset/#project_id)
  - [publish\_version](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdataset/#publish_version)
  - [remove\_tags](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdataset/#remove_tags)
  - [set\_tags](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdataset/#set_tags)
  - [tags](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdataset/#tags)
  - [version\_id](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdataset/#version_id)