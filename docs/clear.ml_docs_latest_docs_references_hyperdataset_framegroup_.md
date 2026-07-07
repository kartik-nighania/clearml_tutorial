---
url: "https://clear.ml/docs/latest/docs/references/hyperdataset/framegroup/"
title: "FrameGroup | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/hyperdataset/framegroup/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

## _class_ dataframe.FrameGroup(id=None, metadata=None, \*args, \*\*kwargs) [​](https://clear.ml/docs/latest/docs/references/hyperdataset/framegroup/\#class-dataframeframegroupidnone-metadatanone-args-kwargs "Direct link to class-dataframeframegroupidnone-metadatanone-args-kwargs")

Represents a group of frames, in the form of a dictionary

Initialize with a list of SingleFrame and key names

- **Parameters**
  - **id** ( _str_ ) – Set the frame group’s unique ID (string representation must be alphanumeric).
    If the ID is None, a unique UUID will be generated based on the args/kwargs dictionary items
    if no args/kwargs provided, a unique UUID will be automatically generated for the frame

  - **metadata** ( _dict_ ) – General purpose dictionary (dict) stored alongside the frame group. Dict must be json-able.
    Notice: metadata keys cannot be the same as the source keys of the SingleFrames

  - **kwargs** ( [`SingleFrame`](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe#allegroai.dataframe.SingleFrame)) – key/SingleFrame collection (like dict initialization) image1=SingleFrame()

  - **args** ( _Union_ _\[_ _dict_ _, \\* [_SingleFrame_](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe#allegroai.dataframe.SingleFrame)_\]\\* ) –

* * *

### id [​](https://clear.ml/docs/latest/docs/references/hyperdataset/framegroup/\#id "Direct link to id")

**property id**

- **Return type**

`str`

- **Returns**

UUID representing the frame in the entire system


* * *

### metadata [​](https://clear.ml/docs/latest/docs/references/hyperdataset/framegroup/\#metadata "Direct link to metadata")

**property metadata**

Get the FrameGroup level metadata.

- **Return type**

`dict`

- **Returns**

General purpose dictionary (dict) stored alongside the frame group. Dict must be json-able.


* * *

### origin [​](https://clear.ml/docs/latest/docs/references/hyperdataset/framegroup/\#origin "Direct link to origin")

**property origin**

Returns the frame’s owner dataset/version information (Dataset is a collection of Versions),
including Dataset ID, Dataset Name, Version ID and Version Name.
Note: This is an auto-generated read-only property.

- **Return type**

`Dict`\[`str`, `str`\]


* * *

### dataset\_version\_metadata [​](https://clear.ml/docs/latest/docs/references/hyperdataset/framegroup/\#dataset_version_metadata "Direct link to dataset_version_metadata")

**property dataset\_version\_metadata**

Returns the frame’s owner dataset version meta-data (Read-Only).

- **Return type**

`dict`

- **Returns**

dict


* * *

### blob [​](https://clear.ml/docs/latest/docs/references/hyperdataset/framegroup/\#blob "Direct link to blob")

**property blob**

- **Return type**

`str`

- **Returns**

Non-Indexed data (string) stored alongside the frame group


* * *

### to\_dict [​](https://clear.ml/docs/latest/docs/references/hyperdataset/framegroup/\#to_dict "Direct link to to_dict")

**to\_dict()**

Return REST API compliant dictionary

- **Return type**

`dict`

- **Returns**

API compliant dictionary for use directly with REST-API


* * *

### copy [​](https://clear.ml/docs/latest/docs/references/hyperdataset/framegroup/\#copy "Direct link to copy")

**copy()**

Returns a copy of this FrameGroup, with a NEW RANDOM UUID.

- **Return type**

`FrameGroup`

- **Returns**

FrameGroup object


* * *

### get\_global\_annotations [​](https://clear.ml/docs/latest/docs/references/hyperdataset/framegroup/\#get_global_annotations "Direct link to get_global_annotations")

**get\_global\_annotations()**

Get a list of global annotations.
Since global annotations are present in all single frames of this frame group, this method will
return a list of the global annotations from one of the single frames.

- **Return type**

`List`\[ [`Annotation`](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation#allegroai.dataframe.Annotation)\]


* * *

### add\_global\_annotation [​](https://clear.ml/docs/latest/docs/references/hyperdataset/framegroup/\#add_global_annotation "Direct link to add_global_annotation")

**add\_global\_annotation(annotation)**

Add a global annotation instance. A copy of the instance will be added to every single frame.

- **Parameters**

**annotation** ( [`Annotation`](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation#allegroai.dataframe.Annotation)) – An Annotation instance

- **Return type**

`None`


* * *

### remove\_global\_annotation [​](https://clear.ml/docs/latest/docs/references/hyperdataset/framegroup/\#remove_global_annotation "Direct link to remove_global_annotation")

**remove\_global\_annotation(annotation)**

Remove a global annotation instance.
The annotation is removed from all single frames, and located using an equality test.

- **Parameters**

**annotation** ( [`Annotation`](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation#allegroai.dataframe.Annotation)) – An Annotation instance

- **Return type**

`bool`

- **Returns**

True if annotation was successfully removed from all single frames, False otherwise.


* * *

### clear [​](https://clear.ml/docs/latest/docs/references/hyperdataset/framegroup/\#clear "Direct link to clear")

**clear() -> None. Remove all items from D.**

* * *

### get [​](https://clear.ml/docs/latest/docs/references/hyperdataset/framegroup/\#get "Direct link to get")

**get(k, \[d\]) -> D\[k\] if k in D, else d. d defaults to None.**

* * *

### items [​](https://clear.ml/docs/latest/docs/references/hyperdataset/framegroup/\#items "Direct link to items")

**items() -> a set-like object providing a view on D's items**

* * *

### keys [​](https://clear.ml/docs/latest/docs/references/hyperdataset/framegroup/\#keys "Direct link to keys")

**keys() -> a set-like object providing a view on D's keys**

* * *

### pop [​](https://clear.ml/docs/latest/docs/references/hyperdataset/framegroup/\#pop "Direct link to pop")

**pop(k, \[d\]) -> v, remove specified key and return the corresponding value.**

If key is not found, d is returned if given, otherwise KeyError is raised.

* * *

### popitem [​](https://clear.ml/docs/latest/docs/references/hyperdataset/framegroup/\#popitem "Direct link to popitem")

**popitem() -> (k, v), remove and return some (key, value) pair**

as a 2-tuple; but raise KeyError if D is empty.

* * *

### setdefault [​](https://clear.ml/docs/latest/docs/references/hyperdataset/framegroup/\#setdefault "Direct link to setdefault")

**setdefault(k, \[d\]) -> D.get(k,d), also set D\[k\]=d if k not in D**

* * *

### update [​](https://clear.ml/docs/latest/docs/references/hyperdataset/framegroup/\#update "Direct link to update")

**update(\[E\], \*\*F) -> None. Update D from mapping/iterable E and F.**

If E present and has a .keys() method, does: for k in E: D\[k\] = E\[k\]
If E present and lacks .keys() method, does: for (k, v) in E: D\[k\] = v
In either case, this is followed by: for k, v in F.items(): D\[k\] = v

* * *

### values [​](https://clear.ml/docs/latest/docs/references/hyperdataset/framegroup/\#values "Direct link to values")

**values() -> an object providing a view on D's values**

* * *

### FrameGroup.from\_dict [​](https://clear.ml/docs/latest/docs/references/hyperdataset/framegroup/\#framegroupfrom_dict "Direct link to FrameGroup.from_dict")

**_classmethod_ from\_dict(framegroup\_dict)**

Build a FrameGroup from REST API compliant dictionary

- **Parameters**

**framegroup\_dict** ( _dict_ ) – a dictionary returned from FrameGroup.to\_dict()

- **Return type**

`FrameGroup`

- **Returns**

FrameGroup object built from REST API dictionary


- [_class_ dataframe.FrameGroup(id=None, metadata=None, \*args, \*\*kwargs)](https://clear.ml/docs/latest/docs/references/hyperdataset/framegroup/#class-dataframeframegroupidnone-metadatanone-args-kwargs)
  - [id](https://clear.ml/docs/latest/docs/references/hyperdataset/framegroup/#id)
  - [metadata](https://clear.ml/docs/latest/docs/references/hyperdataset/framegroup/#metadata)
  - [origin](https://clear.ml/docs/latest/docs/references/hyperdataset/framegroup/#origin)
  - [dataset\_version\_metadata](https://clear.ml/docs/latest/docs/references/hyperdataset/framegroup/#dataset_version_metadata)
  - [blob](https://clear.ml/docs/latest/docs/references/hyperdataset/framegroup/#blob)
  - [to\_dict](https://clear.ml/docs/latest/docs/references/hyperdataset/framegroup/#to_dict)
  - [copy](https://clear.ml/docs/latest/docs/references/hyperdataset/framegroup/#copy)
  - [get\_global\_annotations](https://clear.ml/docs/latest/docs/references/hyperdataset/framegroup/#get_global_annotations)
  - [add\_global\_annotation](https://clear.ml/docs/latest/docs/references/hyperdataset/framegroup/#add_global_annotation)
  - [remove\_global\_annotation](https://clear.ml/docs/latest/docs/references/hyperdataset/framegroup/#remove_global_annotation)
  - [clear](https://clear.ml/docs/latest/docs/references/hyperdataset/framegroup/#clear)
  - [get](https://clear.ml/docs/latest/docs/references/hyperdataset/framegroup/#get)
  - [items](https://clear.ml/docs/latest/docs/references/hyperdataset/framegroup/#items)
  - [keys](https://clear.ml/docs/latest/docs/references/hyperdataset/framegroup/#keys)
  - [pop](https://clear.ml/docs/latest/docs/references/hyperdataset/framegroup/#pop)
  - [popitem](https://clear.ml/docs/latest/docs/references/hyperdataset/framegroup/#popitem)
  - [setdefault](https://clear.ml/docs/latest/docs/references/hyperdataset/framegroup/#setdefault)
  - [update](https://clear.ml/docs/latest/docs/references/hyperdataset/framegroup/#update)
  - [values](https://clear.ml/docs/latest/docs/references/hyperdataset/framegroup/#values)
  - [FrameGroup.from\_dict](https://clear.ml/docs/latest/docs/references/hyperdataset/framegroup/#framegroupfrom_dict)