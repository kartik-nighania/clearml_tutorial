---
url: "https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/"
title: "SingleFrame | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

## _class_ dataframe.SingleFrame(id=None, source=None, width=None, height=None, timestamp=None, size=None, hash=None, preview\_uri=None, preview\_uri\_timestamp=None, metadata=None, annotations=None, mask\_source=None, context\_id=None) [​](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/\#class-dataframesingleframeidnone-sourcenone-widthnone-heightnone-timestampnone-sizenone-hashnone-preview_urinone-preview_uri_timestampnone-metadatanone-annotationsnone-mask_sourcenone-context_idnone "Direct link to class-dataframesingleframeidnone-sourcenone-widthnone-heightnone-timestampnone-sizenone-hashnone-preview_urinone-preview_uri_timestampnone-metadatanone-annotationsnone-mask_sourcenone-context_idnone")

Single frame object, representing a single file with meta-data attached

Create an empty SingleFrame and fill in the field from \*\*kwargs

- **Parameters**
  - **id** ( _str_ ) – UUID representing the frame in the entire system.
    UUID (A-z,0-9), If int/float automatically convert to string
    If None, a unique identifier will be created based on the source URI
    If source is not available, a randomly generated UUID will be used

  - **source** ( _str_ ) – URI link to the source file of the data frame.
    (if local file, [file://](file:///) prefix will be added automatically)

  - **width** ( _int_ ) – Width (integer) of the data frame. None if not applicable

  - **height** ( _int_ ) – Height (integer) of the data frame. None if not applicable

  - **timestamp** ( _int_ ) – Timestamp (integer) of the data frame. Zero/None if not applicable

  - **size** ( _int_ ) – Size (integer) in bytes of source file. None if not applicable

  - **hash** ( _str_ ) – Hash (string) of source file content. None if not applicable

  - **preview\_uri** ( _str_ ) – URI link to a visualization preview of the data frame.
    Usually browser supported format, server from a supported source, can also be direct file link.

  - **preview\_uri\_timestamp** ( _int_ ) – Timestamp (or index) (integer) valid for the URI
    link to a visualization preview of the data frame. (see also preview\_uri)

  - **metadata** ( _dict_ ) – General purpose dictionary (dict) stored alongside the data frame. Dict must be json-able.

  - **annotations** ( _list_ ) – List of annotations (Annotation object) applicable for this data frame.

  - **mask\_source** ( _str_ ) – URI link (str) to a mask file for this data frame. None if not applicable

  - **context\_id** ( _str_ ) – Context ID. Used for default frames aggregation. If not set then it is filled from
    the uri of the first source.

* * *

### preview\_uri [​](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/\#preview_uri "Direct link to preview_uri")

**property preview\_uri**

- **Return type**

`str`

- **Returns**

Interchangeable with preview\_source,
URI link to a visualization preview of the data frame. (see also preview\_uri\_timestamp)


* * *

### preview\_uri\_timestamp [​](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/\#preview_uri_timestamp "Direct link to preview_uri_timestamp")

**property preview\_uri\_timestamp**

- **Return type**

`int`

- **Returns**

Interchangeable with preview\_source\_timestamp,
Timestamp (or index) (integer) valid for the URI link to a visualization preview of the data frame.
(see also preview\_uri)


* * *

### mask\_source [​](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/\#mask_source "Direct link to mask_source")

**property mask\_source**

- **Return type**

`str`

- **Returns**

URI link (str) to a mask file for this data frame. None if not applicable


If multiple masks are registered, always return the first in the list

* * *

### masks\_source [​](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/\#masks_source "Direct link to masks_source")

**property masks\_source**

- **Return type**

`Dict`\[`str`, `str`\]

- **Returns**

Dict of Mask IDS (e.g. “00”, “01” etc.) to URI links (str) to mask files for this data frame.


* * *

### origin [​](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/\#origin "Direct link to origin")

**property origin**

Returns the frame’s owner dataset/version information (Dataset is a collection of Versions),
including Dataset ID, Dataset Name, Version ID and Version Name.
Note: This is an auto-generated read-only property.

- **Return type**

`Dict`\[`str`, `str`\]


* * *

### dataset\_version\_metadata [​](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/\#dataset_version_metadata "Direct link to dataset_version_metadata")

**property dataset\_version\_metadata**

Returns the frame’s owner dataset version meta-data (Read-Only).

- **Return type**

`dict`

- **Returns**

dict


* * *

### blob [​](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/\#blob "Direct link to blob")

**property blob**

- **Return type**

`str`

- **Returns**

Non-Indexed data (string) stored alongside the frame


* * *

### sourcedata [​](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/\#sourcedata "Direct link to sourcedata")

**property sourcedata**

- **Return type**

`dict`

- **Returns**

General purpose dictionary stored alongside the data frame.


* * *

### add\_annotation [​](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/\#add_annotation "Direct link to add_annotation")

**add\_annotation(poly2d\_xy=None, poly3d\_xyz=None, points2d\_xy=None, points3d\_xyz=None, box2d\_xywh=None, box3d\_xyzwhxyzwh=None, ellipse2d\_xyrrt=None, mask\_rgb=None, frame\_class=None, id=None, labels=None, confidence=None, metadata=None, \*\*kwargs)**

Creates an annotation instance based on the provided arguments
and adds it to the single frame’s annotations list.

info

In case more than one of:
poly2d\_xy / poly3d\_xyz / points2d\_xy / points3d\_xyz / box2d\_xywh / box3d\_xyzwhxyzwh /
ellipse2d\_xyrrt / mask\_rgb
are provided, an annotation instance will be created for each one. Created annotations will be associated
by the provided id. If an ID is not provided, one will be automatically created.

- **Parameters**
  - **poly2d\_xy** (`Union`\[`Sequence`\[`Union`\[`int`, `float`\]\], `Sequence`\[`Sequence`\[`Union`\[`int`, `float`\]\]\], `None`\]) – Floating points list (x,y) for single polygon,
    OR List of Floating points lists for complex polygon.

  - **poly3d\_xyz** (`Union`\[`Sequence`\[`Union`\[`int`, `float`\]\], `Sequence`\[`Sequence`\[`Union`\[`int`, `float`\]\]\], `None`\]) – Floating points list (x,y,z) for single polygon,
    OR List of Floating points lists for complex polygon.

  - **points2d\_xy** (`Union`\[`Sequence`\[`Union`\[`int`, `float`\]\], `Sequence`\[`Sequence`\[`Union`\[`int`, `float`\]\]\], `None`\]) – List of floating points pairs (x,y) for set of key-points,

  - **points3d\_xyz** (`Union`\[`Sequence`\[`Union`\[`int`, `float`\]\], `Sequence`\[`Sequence`\[`Union`\[`int`, `float`\]\]\], `None`\]) – List of floating points triplets (x,y,z) for set of key-points,

  - **box2d\_xywh** (`Union`\[`Sequence`\[`Union`\[`int`, `float`\]\], `Sequence`\[`Sequence`\[`Union`\[`int`, `float`\]\]\], `None`\]) – Bounding box, four or five floats for: X,Y,width,height, Optional(angle)

  - **box3d\_xyzwhxyzwh** (`Union`\[`Sequence`\[`Union`\[`int`, `float`\]\], `Sequence`\[`Sequence`\[`Union`\[`int`, `float`\]\]\], `None`\]) – Bounding box, four floats for: X,Y,width,height

  - **ellipse2d\_xyrrt** (`Union`\[`Sequence`\[`Union`\[`int`, `float`\]\], `Sequence`\[`Sequence`\[`Union`\[`int`, `float`\]\]\], `None`\]) – List of cx, cy, rx, ry, theta for the ellipse

  - **mask\_rgb** (`Union`\[`Sequence`\[`Union`\[`int`, `float`\]\], `Sequence`\[`Sequence`\[`Union`\[`int`, `float`\]\]\], `None`\]) – List of RGB (as \[r, g, b\]).

  - **frame\_class** (`Optional`\[`Sequence`\[`str`\]\]) – List of strings, frame level labels (classes).
    It is equivalent to passing `labels` without any specific annotation type.

  - **id** (`Optional`\[`str`\]) – String representing the specific annotation. Useful for tracking objects. None is a valid option.

  - **labels** (`Optional`\[`Sequence`\[`str`\]\]) – List of labels (string). If no specific annotation is passed (e.g. polygon, box, etc.)
    labels will be equivalent to frame\_class annotations

  - **confidence** (`Optional`\[`float`\]) – Labeling confidence (float). Optional

  - **metadata** (`Optional`\[`dict`\]) – General purpose dictionary storing multiple field/values

  - **kwargs** ( _In case custom annotation classes are registered_ \\*, \\* _you can use one of the registered_
    _annotation type name here to provide the values in order to create an instance of a custom annotation class._ ) –
- **Return type**

`List`\[ [`Annotation`](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation#allegroai.dataframe.Annotation)\]

- **Returns**

Annotation indexed list (int) containing a single value (in case a single instance was added) or
multiple values (in case multiple instances were added)


* * *

### remove\_annotation [​](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/\#remove_annotation "Direct link to remove_annotation")

**remove\_annotation(index=None, \*\*kwargs)**

Remove an annotation from the annotations list.
Annotations to remove are selected based on index location in the
annotation list.

- **Parameters**
  - **index** (`Optional`\[`int`\]) – (int) index of annotation to remove

  - **kwargs** ( _Dict_ ) –
- **Return type**

`Union`\[ [`Annotation`](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation#allegroai.dataframe.Annotation), `None`, `Sequence`\[ [`Annotation`](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation#allegroai.dataframe.Annotation)\]\]

- **Returns**

The removed annotation instance, or None


* * *

### remove\_annotations [​](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/\#remove_annotations "Direct link to remove_annotations")

**remove\_annotations(id=None, label=None, labels=None)**

Remove one or more annotations from the annotations list.
Annotations to remove are selected based on their ID and/or labels.

info

Providing No arguments at all will remove All annotations

info

An annotation’s ID is NOT a system ID, but a user provided value.

This means an annotation might have an ID value of None.

- **Parameters**
  - **id** (`Optional`\[`str`\]) – alphanumeric user-provided ID of the annotations to be removed

  - **label** (`Optional`\[`str`\]) – a string label. Any annotation whose labels include this label will be removed.

  - **labels** (`Optional`\[`Sequence`\[`str`\]\]) – a list of string labels. Any annotation whose labels exactly match this list will be removed.
- **Return type**

`Sequence`\[ [`Annotation`](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation#allegroai.dataframe.Annotation)\]

- **Returns**

The removed annotation instances


* * *

### get\_annotations [​](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/\#get_annotations "Direct link to get_annotations")

**get\_annotations(id=None, index=None)**

Retrieve annotation from the annotation list. Select annotation either based on index location in the
annotation list, or based on annotation ID (that can be applied to a group of annotations with the same ID)

- **Parameters**
  - **id** ( _str_ ) – alphanumeric ID of the annotations to be retrieved

  - **index** ( _int_ ) – index of annotation to remove
- **Return type**

`Sequence`\[ [`Annotation`](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation#allegroai.dataframe.Annotation)\]

- **Returns**

list of Annotations


* * *

### id [​](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/\#id "Direct link to id")

**property id**

- **Return type**

`Optional`\[`str`\]

- **Returns**

UUID representing the frame in the entire system


* * *

### source [​](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/\#source "Direct link to source")

**property source**

- **Return type**

`Optional`\[`str`\]

- **Returns**

URI link to the source file of the data frame (if local file [file://](file:///) is emitted from the source prefix)


* * *

### width [​](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/\#width "Direct link to width")

**property width**

- **Return type**

`Optional`\[`int`\]

- **Returns**

Width (integer) of the data frame. If not set, returns None


* * *

### height [​](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/\#height "Direct link to height")

**property height**

- **Return type**

`Optional`\[`int`\]

- **Returns**

Height (integer) of the data frame. If not set, returns None


* * *

### timestamp [​](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/\#timestamp "Direct link to timestamp")

**property timestamp**

- **Return type**

`int`

- **Returns**

Data frame timestamp (int), or index. Zero (0) if not applicable


* * *

### size [​](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/\#size "Direct link to size")

**property size**

- **Return type**

`Optional`\[`int`\]

- **Returns**

Size (integer) in bytes of source file.


* * *

### hash [​](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/\#hash "Direct link to hash")

**property hash**

- **Return type**

`Optional`\[`str`\]

- **Returns**

Hash (string) of source file content.


* * *

### preview\_source [​](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/\#preview_source "Direct link to preview_source")

**property preview\_source**

- **Return type**

`str`

- **Returns**

URI link to a visualization preview of the data frame. (see also preview\_uri\_timestamp)


* * *

### context\_id [​](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/\#context_id "Direct link to context_id")

**property context\_id**

- **Return type**

`str`

- **Returns**

Context ID (string) of the data frame. If not set then it is filled from the source uri


* * *

### preview\_source\_timestamp [​](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/\#preview_source_timestamp "Direct link to preview_source_timestamp")

**property preview\_source\_timestamp**

- **Return type**

`int`

- **Returns**

Timestamp (or index) (integer) valid for the URI link to a visualization preview of the data frame.
(see also preview\_uri)


* * *

### metadata [​](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/\#metadata "Direct link to metadata")

**property metadata**

- **Return type**

`dict`

- **Returns**

General purpose dictionary stored alongside the data frame.


* * *

### annotations [​](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/\#annotations "Direct link to annotations")

**property annotations**

- **Return type**

`List`\[ [`Annotation`](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation#allegroai.dataframe.Annotation)\]

- **Returns**

List of annotations (Annotation object) applicable for this data frame.
Note that you can add directly to the list returned by this property.


* * *

### copy [​](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/\#copy "Direct link to copy")

**copy()**

Returns a copy of this SingleFrame, with a NEW RANDOM UUID.

- **Return type**

`SingleFrame`

- **Returns**

SingleFrame object


* * *

### get\_local\_source [​](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/\#get_local_source "Direct link to get_local_source")

**get\_local\_source(raise\_on\_error=False, skip\_size\_check=False, force\_download=False)**

Retrieve remote file and returns a link to a local file that can be used directly.

- **Parameters**
  - **raise\_on\_error** (`bool`) – If True raise exception if accessing the file failed.
    If False (default) return None on error and print error to log.

  - **skip\_size\_check** (`bool`) – If True will return also files size zero bytes.

  - **force\_download** (`bool`) – If True will ignore local cache and download the file.
- **Return type**

`Optional`\[`str`\]

- **Returns**

Full path to file (str)


* * *

### get\_local\_mask\_source [​](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/\#get_local_mask_source "Direct link to get_local_mask_source")

**get\_local\_mask\_source(raise\_on\_error=False, mask\_id=None, skip\_size\_check=False, force\_download=False)**

Retrieve remote mask file and returns a link to a local file that can be used directly.

- **Parameters**
  - **raise\_on\_error** (`bool`) – If True raise exception if accessing the file failed.
    If False (default) return None on error and print error to log.

  - **mask\_id** (`Optional`\[`str`\]) – If provided return the specific mask\_id local file copy.

  - **skip\_size\_check** (`bool`) – If True will return also files size zero bytes.

  - **force\_download** (`bool`) – If True will ignore local cache and download the file.
- **Return type**

`Optional`\[`str`\]

- **Returns**

Full path to file (str)


* * *

### get\_local\_masks\_source [​](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/\#get_local_masks_source "Direct link to get_local_masks_source")

**get\_local\_masks\_source(raise\_on\_error=False, skip\_size\_check=False, force\_download=False)**

Retrieve remote mask files and returns a list of links to a local file that can be used directly.

- **Parameters**
  - **raise\_on\_error** (`bool`) – If True raise exception if accessing the file failed.
    If False (default) on error append None the list of local files and print error to log.

  - **skip\_size\_check** (`bool`) – If True will return also files size zero bytes.

  - **force\_download** (`bool`) – If True will ignore local cache and download the file.
- **Return type**

`Dict`\[`str`, `Optional`\[`str`\]\]

- **Returns**

Dict of mask ID (i.e. “00”, “01” etc.) to full path to file (str)


* * *

### get\_local\_preview\_source [​](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/\#get_local_preview_source "Direct link to get_local_preview_source")

**get\_local\_preview\_source(raise\_on\_error=False, skip\_size\_check=False, force\_download=False)**

Retrieve remote preview file and returns a link to a local file that can be used directly.

- **Parameters**
  - **raise\_on\_error** (`bool`) – If True raise exception if accessing the file failed.
    If False (default) return None on error and print error to log.

  - **skip\_size\_check** (`bool`) – If True will return also files size zero bytes.

  - **force\_download** (`bool`) – If True will ignore local cache and download the file.
- **Return type**

`Optional`\[`str`\]

- **Returns**

Full path to file (str)


* * *

### to\_dict [​](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/\#to_dict "Direct link to to_dict")

**to\_dict()**

Return REST API compliant dictionary

- **Return type**

`dict`

- **Returns**

API compliant dictionary for use directly with REST-API


* * *

### SingleFrame.from\_dict [​](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/\#singleframefrom_dict "Direct link to SingleFrame.from_dict")

**_classmethod_ from\_dict(singleframe\_dict)**

Build a SingleFrame from REST API compliant dictionary

- **Parameters**

**singleframe\_dict** ( _dict_ ) – a dictionary returned from SingleFrame.to\_dict()

- **Return type**

Union\[ [FrameGroup](https://clear.ml/docs/latest/docs/references/hyperdataset/framegroup#allegroai.dataframe.FrameGroup), SingleFrame\]

- **Returns**

FrameGroup object built from REST API dictionary


* * *

### update\_source\_files\_hash [​](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/\#update_source_files_hash "Direct link to update_source_files_hash")

**update\_source\_files\_hash(allow\_download=False)**

Update internal source files hash (SHA2) values
updates the self.sourcedata with:

```python
self.sourcedata['hash'] = {

    'source': sha2_hash,

    'mask_source': [sha2_hash, ...],

    'preview_source': sha2_hash,

}
```

- **Parameters**

**allow\_download** ( _bool_ ) – if False(default) only calculate hash for local URL file,
otherwise download and update the files content hash

- **Return type**

()


* * *

### get\_source\_hash [​](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/\#get_source_hash "Direct link to get_source_hash")

**get\_source\_hash()**

Return a dict of source hash.
Example:

```json
{

  'source': sha2_hash,

  'mask_source': [sha2_hash],

  'preview_source': sha2_hash,

}
```

- **Return type**

Dict\[str, (int, str)\]

- **Returns**

dict


- [_class_ dataframe.SingleFrame(id=None, source=None, width=None, height=None, timestamp=None, size=None, hash=None, preview\_uri=None, preview\_uri\_timestamp=None, metadata=None, annotations=None, mask\_source=None, context\_id=None)](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/#class-dataframesingleframeidnone-sourcenone-widthnone-heightnone-timestampnone-sizenone-hashnone-preview_urinone-preview_uri_timestampnone-metadatanone-annotationsnone-mask_sourcenone-context_idnone)
  - [preview\_uri](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/#preview_uri)
  - [preview\_uri\_timestamp](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/#preview_uri_timestamp)
  - [mask\_source](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/#mask_source)
  - [masks\_source](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/#masks_source)
  - [origin](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/#origin)
  - [dataset\_version\_metadata](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/#dataset_version_metadata)
  - [blob](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/#blob)
  - [sourcedata](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/#sourcedata)
  - [add\_annotation](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/#add_annotation)
  - [remove\_annotation](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/#remove_annotation)
  - [remove\_annotations](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/#remove_annotations)
  - [get\_annotations](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/#get_annotations)
  - [id](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/#id)
  - [source](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/#source)
  - [width](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/#width)
  - [height](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/#height)
  - [timestamp](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/#timestamp)
  - [size](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/#size)
  - [hash](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/#hash)
  - [preview\_source](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/#preview_source)
  - [context\_id](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/#context_id)
  - [preview\_source\_timestamp](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/#preview_source_timestamp)
  - [metadata](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/#metadata)
  - [annotations](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/#annotations)
  - [copy](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/#copy)
  - [get\_local\_source](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/#get_local_source)
  - [get\_local\_mask\_source](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/#get_local_mask_source)
  - [get\_local\_masks\_source](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/#get_local_masks_source)
  - [get\_local\_preview\_source](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/#get_local_preview_source)
  - [to\_dict](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/#to_dict)
  - [SingleFrame.from\_dict](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/#singleframefrom_dict)
  - [update\_source\_files\_hash](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/#update_source_files_hash)
  - [get\_source\_hash](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe/#get_source_hash)