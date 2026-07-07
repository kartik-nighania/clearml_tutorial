---
url: "https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdatasetmanagement/"
title: "HyperDatasetManagement | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdatasetmanagement/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

## _class_ hyperdatasets.management.HyperDatasetManagement() [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdatasetmanagement/\#class-hyperdatasetsmanagementhyperdatasetmanagement "Direct link to class-hyperdatasetsmanagementhyperdatasetmanagement")

* * *

### commit\_version [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdatasetmanagement/\#commit_version "Direct link to commit_version")

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

### HyperDatasetManagement.delete [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdatasetmanagement/\#hyperdatasetmanagementdelete "Direct link to HyperDatasetManagement.delete")

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

### HyperDatasetManagement.exists [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdatasetmanagement/\#hyperdatasetmanagementexists "Direct link to HyperDatasetManagement.exists")

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

### HyperDatasetManagement.get [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdatasetmanagement/\#hyperdatasetmanagementget "Direct link to HyperDatasetManagement.get")

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

### HyperDatasetManagement.list [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdatasetmanagement/\#hyperdatasetmanagementlist "Direct link to HyperDatasetManagement.list")

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

### publish\_version [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdatasetmanagement/\#publish_version "Direct link to publish_version")

**publish\_version(\*, force=False, publishing\_task=None)**

Publish the bound HyperDataset version.

- **Parameters**
  - **force** (`bool`) – Force publish even with active annotation tasks

  - **publishing\_task** (`Optional`\[`str`\]) – Annotation task identifier issuing the commit
- **Returns**

Backend response payload


- [_class_ hyperdatasets.management.HyperDatasetManagement()](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdatasetmanagement/#class-hyperdatasetsmanagementhyperdatasetmanagement)
  - [commit\_version](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdatasetmanagement/#commit_version)
  - [HyperDatasetManagement.delete](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdatasetmanagement/#hyperdatasetmanagementdelete)
  - [HyperDatasetManagement.exists](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdatasetmanagement/#hyperdatasetmanagementexists)
  - [HyperDatasetManagement.get](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdatasetmanagement/#hyperdatasetmanagementget)
  - [HyperDatasetManagement.list](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdatasetmanagement/#hyperdatasetmanagementlist)
  - [publish\_version](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdatasetmanagement/#publish_version)