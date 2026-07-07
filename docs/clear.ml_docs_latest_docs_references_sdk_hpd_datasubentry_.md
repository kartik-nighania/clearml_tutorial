---
url: "https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentry/"
title: "DataSubEntry | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentry/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

## _class_ hyperdatasets.data\_entry.DataSubEntry(name, source, preview\_source=None, metadata=None) [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentry/\#class-hyperdatasetsdata_entrydatasubentryname-source-preview_sourcenone-metadatanone "Direct link to class-hyperdatasetsdata_entrydatasubentryname-source-preview_sourcenone-metadatanone")

Initialise a base sub-entry that stores source URIs and optional metadata.

- **Parameters**
  - **name** (`str`) – Identifier of the sub-entry (unique per entry)

  - **source** (`Optional`\[`str`\]) – Primary source URI

  - **preview\_source** (`Optional`\[`str`\]) – Optional preview URI

  - **local\_sources\_upload\_destination** – Upload target used when auto-uploading

  - **metadata** (`Optional`\[`Dict`\[`str`, `Any`\]\]) – Optional metadata dictionary stored alongside the sub-entry

* * *

### get\_hash [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentry/\#get_hash "Direct link to get_hash")

**get\_hash(source\_field='source')**

Return the cached SHA256 hash for the requested source field.

- **Parameters**

**source\_field** (`str`) – Either “source” or “preview\_source”

- **Return type**

`Optional`\[`str`\]

- **Returns**

Hex digest string when available, otherwise None


* * *

### get\_local\_preview\_source [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentry/\#get_local_preview_source "Direct link to get_local_preview_source")

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

### get\_local\_source [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentry/\#get_local_source "Direct link to get_local_source")

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

### get\_source [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentry/\#get_source "Direct link to get_source")

**get\_source(source\_field='source')**

Return the URI associated with the requested source field.

- **Parameters**

**source\_field** (`str`) – Either “source” or “preview\_source”

- **Return type**

`Optional`\[`str`\]

- **Returns**

URI string when set, otherwise None


* * *

### name [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentry/\#name "Direct link to name")

**property name: str**

Return the sub-entry identifier (per entry unique).

- **Return type**

`str`

- **Returns**

Sub-entry name


* * *

### preview\_source [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentry/\#preview_source "Direct link to preview_source")

**property preview\_source: Optional\[str\]**

Expose the preview URI when available.

- **Return type**

`Optional`\[`str`\]

- **Returns**

Preview URI string or None


* * *

### set\_local\_sources\_upload\_destination [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentry/\#set_local_sources_upload_destination "Direct link to set_local_sources_upload_destination")

**set\_local\_sources\_upload\_destination(local\_sources\_upload\_destination)**

Set an upload destination for the local sources. This will be used when uploading the data entry

- **Parameters**

**local\_sources\_upload\_destination** – URL to the upload path


* * *

### set\_source [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentry/\#set_source "Direct link to set_source")

**set\_source(source\_field, uri)**

Update the URI linked to the requested source field.

- **Parameters**
  - **source\_field** (`str`) – Either “source” or “preview\_source”

  - **uri** (`Optional`\[`str`\]) – New URI to associate with the field
- **Return type**

`None`


* * *

### source [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentry/\#source "Direct link to source")

**property source: Optional\[str\]**

Expose the main source URI.

- **Return type**

`Optional`\[`str`\]

- **Returns**

Source URI string or None


- [_class_ hyperdatasets.data\_entry.DataSubEntry(name, source, preview\_source=None, metadata=None)](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentry/#class-hyperdatasetsdata_entrydatasubentryname-source-preview_sourcenone-metadatanone)
  - [get\_hash](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentry/#get_hash)
  - [get\_local\_preview\_source](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentry/#get_local_preview_source)
  - [get\_local\_source](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentry/#get_local_source)
  - [get\_source](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentry/#get_source)
  - [name](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentry/#name)
  - [preview\_source](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentry/#preview_source)
  - [set\_local\_sources\_upload\_destination](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentry/#set_local_sources_upload_destination)
  - [set\_source](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentry/#set_source)
  - [source](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentry/#source)