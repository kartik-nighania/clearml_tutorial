---
url: "https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentryimage/"
title: "DataSubEntryImage | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentryimage/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

## _class_ hyperdatasets.data\_entry\_image.DataSubEntryImage(name='image\_entry\_0', source=None, preview\_source=None, width=None, height=None, timestamp=None, context\_id=None, masks\_source=None, metadata=None) [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentryimage/\#class-hyperdatasetsdata_entry_imagedatasubentryimagenameimage_entry_0-sourcenone-preview_sourcenone-widthnone-heightnone-timestampnone-context_idnone-masks_sourcenone-metadatanone "Direct link to class-hyperdatasetsdata_entry_imagedatasubentryimagenameimage_entry_0-sourcenone-preview_sourcenone-widthnone-heightnone-timestampnone-context_idnone-masks_sourcenone-metadatanone")

Initialise an image sub-entry with optional dimension, context and mask metadata.

- **Parameters**
  - **name** (`str`) – Identifier of the sub-entry (defaults to image\_entry\_0)

  - **source** (`Optional`\[`str`\]) – Primary image URI

  - **preview\_source** (`Optional`\[`str`\]) – Optional preview image URI

  - **width** (`Optional`\[`int`\]) – Image width in pixels

  - **height** (`Optional`\[`int`\]) – Image height in pixels

  - **timestamp** (`Optional`\[`int`\]) – Optional timestamp associated with the frame

  - **context\_id** (`Optional`\[`str`\]) – Optional context identifier to correlate sources

  - **masks\_source** (`Union`\[`Sequence`\[`str`\], `Dict`\[`str`, `str`\], `None`\]) – Sequence or mapping of mask URIs

  - **metadata** (`Optional`\[`dict`\]) – Optional metadata dictionary stored alongside the sub-entry

* * *

### add\_annotation [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentryimage/\#add_annotation "Direct link to add_annotation")

**add\_annotation(poly2d\_xy=None, poly3d\_xyz=None, points2d\_xy=None, points3d\_xyz=None, box2d\_xywh=None, box3d\_xyzwhxyzwh=None, ellipse2d\_xyrrt=None, mask\_rgb=None, frame\_class=None, id=None, labels=None, confidence=None, metadata=None)**

Create ROI records for this sub-entry and return their indices.

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

List of annotation indices that were appended


* * *

### context\_id [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentryimage/\#context_id "Direct link to context_id")

**property context\_id: Optional\[str\]**

Return the context identifier used to correlate sub-entries.

- **Return type**

`Optional`\[`str`\]

- **Returns**

Context identifier string or None


* * *

### get\_all\_annotations [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentryimage/\#get_all_annotations "Direct link to get_all_annotations")

**get\_all\_annotations()**

Return all annotations attached to this sub-entry.

- **Return type**

`Sequence`\[`Any`\]

- **Returns**

Sequence of annotation payloads


* * *

### get\_annotations [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentryimage/\#get_annotations "Direct link to get_annotations")

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

### get\_hash [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentryimage/\#get_hash "Direct link to get_hash")

**get\_hash(source\_field='source')**

Return the cached SHA256 hash for the requested source field.

- **Parameters**

**source\_field** (`str`) – Either “source” or “preview\_source”

- **Return type**

`Optional`\[`str`\]

- **Returns**

Hex digest string when available, otherwise None


* * *

### get\_local\_mask\_source [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentryimage/\#get_local_mask_source "Direct link to get_local_mask_source")

**get\_local\_mask\_source(raise\_on\_error=False, mask\_id=None, force\_download=False)**

Retrieve a cached local copy of a specific mask source.

- **Parameters**
  - **raise\_on\_error** (`bool`) – Raise ValueError when the download fails

  - **mask\_id** (`Optional`\[`str`\]) – Mask identifier to fetch; defaults to the first mask

  - **force\_download** (`bool`) – Refresh an existing cached entry when True
- **Return type**

`Optional`\[`str`\]

- **Returns**

Absolute path to the local copy or None when unavailable


* * *

### get\_local\_masks\_source [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentryimage/\#get_local_masks_source "Direct link to get_local_masks_source")

**get\_local\_masks\_source(raise\_on\_error=False, force\_download=False)**

Retrieve cached local copies for all mask sources on this sub-entry.

- **Parameters**
  - **raise\_on\_error** (`bool`) – Raise ValueError when any download fails

  - **force\_download** (`bool`) – Refresh existing cached entries when True
- **Return type**

`Dict`\[`str`, `Optional`\[`str`\]\]

- **Returns**

Mapping of mask id to the local copy path (or None on failure if raise\_on\_error is False)


* * *

### get\_local\_preview\_source [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentryimage/\#get_local_preview_source "Direct link to get_local_preview_source")

**get\_local\_preview\_source(raise\_on\_error=False, force\_download=False)**

Retrieve a cached local copy of the preview source URI.

- **Parameters**
  - **raise\_on\_error** (`bool`) – Raise ValueError when the download fails

  - **force\_download** (`bool`) – Refresh the cached copy even if it already exists
- **Return type**

`Optional`\[`str`\]

- **Returns**

Absolute path to the local copy or None on failure/when preview missing


* * *

### get\_local\_source [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentryimage/\#get_local_source "Direct link to get_local_source")

**get\_local\_source(raise\_on\_error=False, force\_download=False)**

Retrieve a cached local copy of the primary source URI.

- **Parameters**
  - **raise\_on\_error** (`bool`) – Raise ValueError when the download fails

  - **force\_download** (`bool`) – Refresh the cached copy even if it already exists
- **Return type**

`Optional`\[`str`\]

- **Returns**

Absolute path to the local copy or None on failure/when source missing


* * *

### get\_mask\_source [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentryimage/\#get_mask_source "Direct link to get_mask_source")

**get\_mask\_source(mask\_id=None)**

Return the URI for the requested mask id (or the first mask if omitted).

- **Parameters**

**mask\_id** (`Optional`\[`str`\]) – Mask identifier (e.g. “00”)

- **Return type**

`Optional`\[`str`\]

- **Returns**

Mask URI string or None when unavailable


* * *

### get\_masks\_source\_dict [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentryimage/\#get_masks_source_dict "Direct link to get_masks_source_dict")

**get\_masks\_source\_dict()**

Return a copy of the mask-id to URI mapping.

- **Return type**

`Dict`\[`str`, `str`\]

- **Returns**

Dictionary mapping mask ids to URIs


* * *

### get\_source [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentryimage/\#get_source "Direct link to get_source")

**get\_source(source\_field='source')**

Return the URI associated with the requested source field.

- **Parameters**

**source\_field** (`str`) – Either “source” or “preview\_source”

- **Return type**

`Optional`\[`str`\]

- **Returns**

URI string when set, otherwise None


* * *

### height [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentryimage/\#height "Direct link to height")

**property height: Optional\[int\]**

Return cached image height if known.

- **Return type**

`Optional`\[`int`\]

- **Returns**

Height in pixels or None when unknown


* * *

### name [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentryimage/\#name "Direct link to name")

**property name: str**

Return the sub-entry identifier (per entry unique).

- **Return type**

`str`

- **Returns**

Sub-entry name


* * *

### preview\_source [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentryimage/\#preview_source "Direct link to preview_source")

**property preview\_source: Optional\[str\]**

Expose the preview URI when available.

- **Return type**

`Optional`\[`str`\]

- **Returns**

Preview URI string or None


* * *

### remove\_annotation [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentryimage/\#remove_annotation "Direct link to remove_annotation")

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

### remove\_annotations [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentryimage/\#remove_annotations "Direct link to remove_annotations")

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

### set\_local\_sources\_upload\_destination [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentryimage/\#set_local_sources_upload_destination "Direct link to set_local_sources_upload_destination")

**set\_local\_sources\_upload\_destination(local\_sources\_upload\_destination)**

Set an upload destination for the local sources. This will be used when uploading the data entry

- **Parameters**

**local\_sources\_upload\_destination** – URL to the upload path


* * *

### set\_mask\_source [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentryimage/\#set_mask_source "Direct link to set_mask_source")

**set\_mask\_source(uri)**

Add a single mask URI and auto-number it (00, 01, 02, …).

Returns the assigned mask id, or None if uri is falsy.

- **Return type**

`Optional`\[`str`\]

- **Parameters**

**uri** ( _Optional_ _\[_ _str_ _\]_ ) –


* * *

### set\_masks\_source [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentryimage/\#set_masks_source "Direct link to set_masks_source")

**set\_masks\_source(masks\_source=None)**

Set multiple mask URIs and auto-number them (00, 01, 02, …).

For dict input, the values’ iteration order is used and keys are ignored.
For list/sequence input, order is preserved.

- **Return type**

`None`

- **Parameters**

**masks\_source** ( _Optional_ _\[_ _Union_ _\[_ _Sequence_ _\[_ _str_ _\]_ \\*, \\* _Dict_ _\[_ _str_ \\*, \\* _str_ _\]_ _\]_ _\]_ ) –


* * *

### set\_source [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentryimage/\#set_source "Direct link to set_source")

**set\_source(source\_field, uri)**

Update the URI linked to the requested source field.

- **Parameters**
  - **source\_field** (`str`) – Either “source” or “preview\_source”

  - **uri** (`Optional`\[`str`\]) – New URI to associate with the field
- **Return type**

`None`


* * *

### source [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentryimage/\#source "Direct link to source")

**property source: Optional\[str\]**

Expose the main source URI.

- **Return type**

`Optional`\[`str`\]

- **Returns**

Source URI string or None


* * *

### timestamp [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentryimage/\#timestamp "Direct link to timestamp")

**property timestamp: Optional\[int\]**

Return the timestamp associated with this frame, if any.

- **Return type**

`Optional`\[`int`\]

- **Returns**

Timestamp value or None


* * *

### width [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentryimage/\#width "Direct link to width")

**property width: Optional\[int\]**

Return cached image width if known.

- **Return type**

`Optional`\[`int`\]

- **Returns**

Width in pixels or None when unknown


- [_class_ hyperdatasets.data\_entry\_image.DataSubEntryImage(name='image\_entry\_0', source=None, preview\_source=None, width=None, height=None, timestamp=None, context\_id=None, masks\_source=None, metadata=None)](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentryimage/#class-hyperdatasetsdata_entry_imagedatasubentryimagenameimage_entry_0-sourcenone-preview_sourcenone-widthnone-heightnone-timestampnone-context_idnone-masks_sourcenone-metadatanone)
  - [add\_annotation](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentryimage/#add_annotation)
  - [context\_id](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentryimage/#context_id)
  - [get\_all\_annotations](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentryimage/#get_all_annotations)
  - [get\_annotations](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentryimage/#get_annotations)
  - [get\_hash](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentryimage/#get_hash)
  - [get\_local\_mask\_source](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentryimage/#get_local_mask_source)
  - [get\_local\_masks\_source](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentryimage/#get_local_masks_source)
  - [get\_local\_preview\_source](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentryimage/#get_local_preview_source)
  - [get\_local\_source](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentryimage/#get_local_source)
  - [get\_mask\_source](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentryimage/#get_mask_source)
  - [get\_masks\_source\_dict](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentryimage/#get_masks_source_dict)
  - [get\_source](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentryimage/#get_source)
  - [height](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentryimage/#height)
  - [name](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentryimage/#name)
  - [preview\_source](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentryimage/#preview_source)
  - [remove\_annotation](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentryimage/#remove_annotation)
  - [remove\_annotations](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentryimage/#remove_annotations)
  - [set\_local\_sources\_upload\_destination](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentryimage/#set_local_sources_upload_destination)
  - [set\_mask\_source](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentryimage/#set_mask_source)
  - [set\_masks\_source](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentryimage/#set_masks_source)
  - [set\_source](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentryimage/#set_source)
  - [source](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentryimage/#source)
  - [timestamp](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentryimage/#timestamp)
  - [width](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentryimage/#width)