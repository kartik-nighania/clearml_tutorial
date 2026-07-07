---
url: "https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentryimage/"
title: "DataEntryImage | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentryimage/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

## _class_ hyperdatasets.data\_entry\_image.DataEntryImage(data\_entry\_id=None, metadata=None) [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentryimage/\#class-hyperdatasetsdata_entry_imagedataentryimagedata_entry_idnone-metadatanone "Direct link to class-hyperdatasetsdata_entry_imagedataentryimagedata_entry_idnone-metadatanone")

Container for a logical frame composed of one or more sub-entries.

- **Parameters**
  - **data\_entry\_id** (`Optional`\[`str`\]) – Explicit entry identifier to reuse

  - **metadata** (`Optional`\[`dict`\]) – Optional metadata dictionary stored on the frame

* * *

### add\_annotation [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentryimage/\#add_annotation "Direct link to add_annotation")

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

### add\_global\_annotation [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentryimage/\#add_global_annotation "Direct link to add_global_annotation")

**add\_global\_annotation(poly2d\_xy=None, poly3d\_xyz=None, points2d\_xy=None, points3d\_xyz=None, box2d\_xywh=None, box3d\_xyzwhxyzwh=None, ellipse2d\_xyrrt=None, mask\_rgb=None, frame\_class=None, id=None, labels=None, confidence=None, metadata=None)**

Broadcast an annotation request to all sub-entries and aggregate their indices.

- **Parameters**
  - **poly2d\_xy** (`Union`\[`Sequence`\[`float`\], `Sequence`\[`int`\], `Sequence`\[`Tuple`\[`float`, `float`\]\], `Sequence`\[`Tuple`\[`float`, `float`, `float`\]\], `Sequence`\[`Sequence`\[`Tuple`\[`float`, `float`\]\]\], `Sequence`\[`Sequence`\[`Tuple`\[`float`, `float`, `float`\]\]\], `None`\]) – 2D polygon coordinates

  - **poly3d\_xyz** (`Union`\[`Sequence`\[`float`\], `Sequence`\[`int`\], `Sequence`\[`Tuple`\[`float`, `float`\]\], `Sequence`\[`Tuple`\[`float`, `float`, `float`\]\], `Sequence`\[`Sequence`\[`Tuple`\[`float`, `float`\]\]\], `Sequence`\[`Sequence`\[`Tuple`\[`float`, `float`, `float`\]\]\], `None`\]) – 3D polygon coordinates

  - **points2d\_xy** (`Union`\[`Sequence`\[`float`\], `Sequence`\[`int`\], `Sequence`\[`Tuple`\[`float`, `float`\]\], `Sequence`\[`Tuple`\[`float`, `float`, `float`\]\], `Sequence`\[`Sequence`\[`Tuple`\[`float`, `float`\]\]\], `Sequence`\[`Sequence`\[`Tuple`\[`float`, `float`, `float`\]\]\], `None`\]) – 2D keypoint coordinates

  - **points3d\_xyz** (`Union`\[`Sequence`\[`float`\], `Sequence`\[`int`\], `Sequence`\[`Tuple`\[`float`, `float`\]\], `Sequence`\[`Tuple`\[`float`, `float`, `float`\]\], `Sequence`\[`Sequence`\[`Tuple`\[`float`, `float`\]\]\], `Sequence`\[`Sequence`\[`Tuple`\[`float`, `float`, `float`\]\]\], `None`\]) – 3D keypoint coordinates

  - **box2d\_xywh** (`Union`\[`Sequence`\[`float`\], `Sequence`\[`int`\], `Sequence`\[`Tuple`\[`float`, `float`\]\], `Sequence`\[`Tuple`\[`float`, `float`, `float`\]\], `Sequence`\[`Sequence`\[`Tuple`\[`float`, `float`\]\]\], `Sequence`\[`Sequence`\[`Tuple`\[`float`, `float`, `float`\]\]\], `None`\]) – 2D bounding box definition

  - **box3d\_xyzwhxyzwh** (`Union`\[`Sequence`\[`float`\], `Sequence`\[`int`\], `Sequence`\[`Tuple`\[`float`, `float`\]\], `Sequence`\[`Tuple`\[`float`, `float`, `float`\]\], `Sequence`\[`Sequence`\[`Tuple`\[`float`, `float`\]\]\], `Sequence`\[`Sequence`\[`Tuple`\[`float`, `float`, `float`\]\]\], `None`\]) – 3D bounding box definition

  - **ellipse2d\_xyrrt** (`Union`\[`Sequence`\[`float`\], `Sequence`\[`int`\], `Sequence`\[`Tuple`\[`float`, `float`\]\], `Sequence`\[`Tuple`\[`float`, `float`, `float`\]\], `Sequence`\[`Sequence`\[`Tuple`\[`float`, `float`\]\]\], `Sequence`\[`Sequence`\[`Tuple`\[`float`, `float`, `float`\]\]\], `None`\]) – 2D ellipse definition

  - **mask\_rgb** (`Union`\[`Sequence`\[`float`\], `Sequence`\[`int`\], `Sequence`\[`Tuple`\[`float`, `float`\]\], `Sequence`\[`Tuple`\[`float`, `float`, `float`\]\], `Sequence`\[`Sequence`\[`Tuple`\[`float`, `float`\]\]\], `Sequence`\[`Sequence`\[`Tuple`\[`float`, `float`, `float`\]\]\], `None`\]) – RGB mask values

  - **frame\_class** (`Optional`\[`Sequence`\[`str`\]\]) – Optional frame-level class labels

  - **id** (`Optional`\[`str`\]) – Annotation identifier

  - **labels** (`Optional`\[`Sequence`\[`str`\]\]) – Sequence of label names

  - **confidence** (`Optional`\[`float`\]) – Optional confidence value

  - **metadata** (`Optional`\[`dict`\]) – Extra metadata mapping to attach to the annotation
- **Return type**

`List`\[`int`\]

- **Returns**

List of annotation indices returned by the sub-entries


* * *

### add\_sub\_entries [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentryimage/\#add_sub_entries "Direct link to add_sub_entries")

**add\_sub\_entries(sub\_entries)**

Attach the provided sub-entry objects, indexed by their name.

- **Parameters**

**sub\_entries** (`Iterable`\[ [`DataSubEntry`](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentry#clearml.hyperdatasets.data_entry.DataSubEntry)\]) – Iterable of sub-entry instances to register

- **Return type**

`None`


* * *

### DataEntryImage.from\_api\_object [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentryimage/\#dataentryimagefrom_api_object "Direct link to DataEntryImage.from_api_object")

**_classmethod_ from\_api\_object(frame)**

Convert backend frame (dict/object) to DataEntryImage + DataSubEntryImage tree.

- **Return type**

`DataEntryImage`

- **Parameters**

**frame** ( _Any_ ) –


* * *

### get\_all\_annotations [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentryimage/\#get_all_annotations "Direct link to get_all_annotations")

**get\_all\_annotations()**

Return all annotations attached to this entry.

- **Return type**

`Sequence`\[`Any`\]

- **Returns**

Sequence of annotation payloads


* * *

### get\_all\_global\_annotations [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentryimage/\#get_all_global_annotations "Direct link to get_all_global_annotations")

**get\_all\_global\_annotations()**

Return every annotation collected from all sub-entries.

- **Return type**

`Sequence`\[`Any`\]

- **Returns**

Sequence of annotation payloads across all sub-entries


* * *

### get\_annotations [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentryimage/\#get_annotations "Direct link to get_annotations")

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

### get\_global\_annotations [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentryimage/\#get_global_annotations "Direct link to get_global_annotations")

**get\_global\_annotations(id=None, index=None)**

Return global annotations filtered by identifier or index.

- **Parameters**
  - **id** (`Optional`\[`str`\]) – Annotation identifier to filter by

  - **index** (`Optional`\[`int`\]) – Annotation index to fetch
- **Return type**

`Sequence`\[`Any`\]

- **Returns**

Sequence of matching annotation payloads


* * *

### id [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentryimage/\#id "Direct link to id")

**property id: str**

Return the entry identifier used by the backend.

- **Return type**

`str`

- **Returns**

Entry identifier string


* * *

### remove\_annotation [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentryimage/\#remove_annotation "Direct link to remove_annotation")

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

### remove\_annotations [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentryimage/\#remove_annotations "Direct link to remove_annotations")

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

### remove\_global\_annotation [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentryimage/\#remove_global_annotation "Direct link to remove_global_annotation")

**remove\_global\_annotation(index=None, \*\*kwargs)**

Remove the first matching annotation across sub-entries.

- **Parameters**
  - **index** (`Optional`\[`int`\]) – Annotation index to remove

  - **kwargs** (`Any`) – Alternative filters such as id=…
- **Return type**

`Any`

- **Returns**

Removed annotation payload or None when nothing matched


* * *

### remove\_global\_annotations [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentryimage/\#remove_global_annotations "Direct link to remove_global_annotations")

**remove\_global\_annotations(id=None, label=None, labels=None)**

Remove annotations across sub-entries using the provided filters.

- **Parameters**
  - **id** (`Optional`\[`str`\]) – Annotation identifier to match

  - **label** (`Optional`\[`str`\]) – Single label to match

  - **labels** (`Optional`\[`Sequence`\[`str`\]\]) – Sequence of labels to match
- **Return type**

`Sequence`\[`Any`\]

- **Returns**

Sequence of removed annotation payloads


* * *

### set\_vector [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentryimage/\#set_vector "Direct link to set_vector")

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

### sub\_data\_entries [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentryimage/\#sub_data_entries "Direct link to sub_data_entries")

**property sub\_data\_entries: List\[DataSubEntry\]**

Return the list of attached sub-entries.

- **Return type**

`List`\[ [`DataSubEntry`](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentry#clearml.hyperdatasets.data_entry.DataSubEntry)\]

- **Returns**

List of sub-entry objects


* * *

### to\_api\_object [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentryimage/\#to_api_object "Direct link to to_api_object")

**to\_api\_object()**

Serialize this entry to the SaveFramesRequest frame schema.

- **Return type**

`dict`

- **Returns**

Frame dictionary ready for backend submission


- [_class_ hyperdatasets.data\_entry\_image.DataEntryImage(data\_entry\_id=None, metadata=None)](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentryimage/#class-hyperdatasetsdata_entry_imagedataentryimagedata_entry_idnone-metadatanone)
  - [add\_annotation](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentryimage/#add_annotation)
  - [add\_global\_annotation](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentryimage/#add_global_annotation)
  - [add\_sub\_entries](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentryimage/#add_sub_entries)
  - [DataEntryImage.from\_api\_object](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentryimage/#dataentryimagefrom_api_object)
  - [get\_all\_annotations](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentryimage/#get_all_annotations)
  - [get\_all\_global\_annotations](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentryimage/#get_all_global_annotations)
  - [get\_annotations](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentryimage/#get_annotations)
  - [get\_global\_annotations](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentryimage/#get_global_annotations)
  - [id](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentryimage/#id)
  - [remove\_annotation](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentryimage/#remove_annotation)
  - [remove\_annotations](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentryimage/#remove_annotations)
  - [remove\_global\_annotation](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentryimage/#remove_global_annotation)
  - [remove\_global\_annotations](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentryimage/#remove_global_annotations)
  - [set\_vector](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentryimage/#set_vector)
  - [sub\_data\_entries](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentryimage/#sub_data_entries)
  - [to\_api\_object](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentryimage/#to_api_object)