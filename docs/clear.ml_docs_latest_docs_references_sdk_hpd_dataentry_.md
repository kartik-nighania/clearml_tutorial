---
url: "https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentry/"
title: "DataEntry | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentry/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

## _class_ hyperdatasets.data\_entry.DataEntry(data\_entry\_id=None, metadata=None) [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentry/\#class-hyperdatasetsdata_entrydataentrydata_entry_idnone-metadatanone "Direct link to class-hyperdatasetsdata_entrydataentrydata_entry_idnone-metadatanone")

Container for a logical frame composed of one or more sub-entries.

- **Parameters**
  - **data\_entry\_id** (`Optional`\[`str`\]) – Explicit entry identifier to reuse

  - **metadata** (`Optional`\[`Dict`\[`str`, `Any`\]\]) – Optional metadata dictionary stored on the frame

* * *

### add\_annotation [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentry/\#add_annotation "Direct link to add_annotation")

**add\_annotation(id, labels, confidence, metadata)**

Attach a metadata-only annotation to this entry.

- **Parameters**
  - **id** – Identifier associated with this annotation

  - **labels** – Sequence of labels to associate with the annotation

  - **confidence** – Optional confidence value

  - **metadata** – Additional metadata to store alongside the annotation
- **Returns**

Numeric index of the appended annotation


* * *

### add\_sub\_entries [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentry/\#add_sub_entries "Direct link to add_sub_entries")

**add\_sub\_entries(sub\_entries)**

Attach the provided sub-entry objects, indexed by their name.

- **Parameters**

**sub\_entries** (`Iterable`\[ [`DataSubEntry`](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentry#clearml.hyperdatasets.data_entry.DataSubEntry)\]) – Iterable of sub-entry instances to register

- **Return type**

`None`


* * *

### DataEntry.from\_api\_object [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentry/\#dataentryfrom_api_object "Direct link to DataEntry.from_api_object")

**_classmethod_ from\_api\_object(data\_entry)**

Convert a backend frame object/dict into a generic DataEntry tree.

- **Return type**

`DataEntry`

- **Parameters**

**data\_entry** ( _Any_ ) –


* * *

### get\_all\_annotations [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentry/\#get_all_annotations "Direct link to get_all_annotations")

**get\_all\_annotations()**

Return all annotations attached to this entry.

- **Return type**

`Sequence`\[`Any`\]

- **Returns**

Sequence of annotation payloads


* * *

### get\_annotations [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentry/\#get_annotations "Direct link to get_annotations")

**get\_annotations(id=None, index=None)**

Return annotations matching the supplied identifier/index filters.

- **Parameters**
  - **id** (`Optional`\[`str`\]) – Annotation identifier to filter by

  - **index** (`Optional`\[`int`\]) – Annotation index to fetch
- **Return type**

`Sequence`\[`Any`\]

- **Returns**

Sequence of matching annotation payloads


* * *

### id [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentry/\#id "Direct link to id")

**property id: str**

Return the entry identifier used by the backend.

- **Return type**

`str`

- **Returns**

Entry identifier string


* * *

### remove\_annotation [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentry/\#remove_annotation "Direct link to remove_annotation")

**remove\_annotation(index=None, \*\*kwargs)**

Remove a single annotation by numeric index or identifier.

- **Parameters**
  - **index** (`Optional`\[`int`\]) – Annotation index to remove

  - **kwargs** (`Any`) – Alternative filters such as id=…
- **Return type**

`Any`

- **Returns**

Removed annotation payload or None when nothing matched


* * *

### remove\_annotations [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentry/\#remove_annotations "Direct link to remove_annotations")

**remove\_annotations(id=None, label=None, labels=None)**

Remove annotations that match the provided id or label filters.

- **Parameters**
  - **id** (`Optional`\[`str`\]) – Annotation identifier to match

  - **label** (`Optional`\[`str`\]) – Single label to match

  - **labels** (`Optional`\[`Sequence`\[`str`\]\]) – Sequence of labels to match
- **Return type**

`Sequence`\[`Any`\]

- **Returns**

Sequence of removed annotation payloads


* * *

### set\_vector [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentry/\#set_vector "Direct link to set_vector")

**set\_vector(vector, metadata\_field)**

Store a vector representation on the entry metadata.

- **Parameters**
  - **vector** (`Sequence`\[`Any`\]) – Sequence of scalar values describing the entry.

  - **metadata\_field** (`str`) – Metadata key to populate with the vector (for example `_vector` or
    `vectors.embedding`). The caller must supply the exact metadata path used when
    registering field mappings on the dataset.
- **Return type**

`None`


* * *

### sub\_data\_entries [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentry/\#sub_data_entries "Direct link to sub_data_entries")

**property sub\_data\_entries: List\[DataSubEntry\]**

Return the list of attached sub-entries.

- **Return type**

`List`\[ [`DataSubEntry`](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentry#clearml.hyperdatasets.data_entry.DataSubEntry)\]

- **Returns**

List of sub-entry objects


* * *

### to\_api\_object [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentry/\#to_api_object "Direct link to to_api_object")

**to\_api\_object()**

Serialize this entry to the SaveFramesRequest frame schema.

- **Return type**

`Dict`\[`str`, `Any`\]

- **Returns**

Frame dictionary ready for backend submission


- [_class_ hyperdatasets.data\_entry.DataEntry(data\_entry\_id=None, metadata=None)](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentry/#class-hyperdatasetsdata_entrydataentrydata_entry_idnone-metadatanone)
  - [add\_annotation](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentry/#add_annotation)
  - [add\_sub\_entries](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentry/#add_sub_entries)
  - [DataEntry.from\_api\_object](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentry/#dataentryfrom_api_object)
  - [get\_all\_annotations](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentry/#get_all_annotations)
  - [get\_annotations](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentry/#get_annotations)
  - [id](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentry/#id)
  - [remove\_annotation](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentry/#remove_annotation)
  - [remove\_annotations](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentry/#remove_annotations)
  - [set\_vector](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentry/#set_vector)
  - [sub\_data\_entries](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentry/#sub_data_entries)
  - [to\_api\_object](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentry/#to_api_object)