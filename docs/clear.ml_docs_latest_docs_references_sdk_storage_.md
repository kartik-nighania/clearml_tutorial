---
url: "https://clear.ml/docs/latest/docs/references/sdk/storage/"
title: "StorageManager | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/sdk/storage/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

## _class_ StorageManager() [​](https://clear.ml/docs/latest/docs/references/sdk/storage/\#class-storagemanager "Direct link to class-storagemanager")

StorageManager provides an interface for uploading and downloading files to and from remote storage.
Supported remote servers: `http(s)`, `s3`, `gs`, `azure`, and shared filesystem.
Caching is enabled by default for all downloaded files.

* * *

### StorageManager.download\_file [​](https://clear.ml/docs/latest/docs/references/sdk/storage/\#storagemanagerdownload_file "Direct link to StorageManager.download_file")

**_classmethod_ download\_file(remote\_url, local\_folder=None, overwrite=False, skip\_zero\_size\_check=False, silence\_errors=False)**

Download a remote file to a local folder, preserving its subfolder structure.

For example, to download `s3://bucket/sub/file.ext`, calling
`StorageManager.download_file('s3://bucket/sub/file.ext', '~/folder/')` will save it locally as
`~/folder/sub/file.ext`.

- **Parameters**
  - **remote\_url** (`str`) – URL of the remote file to download. Its path structure will be recreated under the target
    `local_folder`. Supports `s3`, `gs`, `azure`, and shared filesystem.
    Example: `'s3://bucket/data/'`

  - **local\_folder** (`Optional`\[`str`\]) – Local target folder. If `None` (default), uses the cache folder.

  - **overwrite** (`bool`) – If `True`, download remote files even if they exist locally. Defaults to `False`.

  - **skip\_zero\_size\_check** (`bool`) – If `True`, no error will be raised for files with zero bytes size. Defaults to
    `False`.

  - **silence\_errors** (`bool`) – If `True`, silence errors encountered during download. Defaults to `False`.
- **Return type**

`Optional`\[`str`\]

- **Returns**

Path to downloaded file, or `None` on error.


* * *

### StorageManager.download\_folder [​](https://clear.ml/docs/latest/docs/references/sdk/storage/\#storagemanagerdownload_folder "Direct link to StorageManager.download_folder")

**_classmethod_ download\_folder(remote\_url, local\_folder=None, match\_wildcard=None, overwrite=False, skip\_zero\_size\_check=False, silence\_errors=False, max\_workers=None)**

Download a remote folder recursively to the local machine, preserving the subfolder structure.

For example, downloading `'s3://bucket/'` to `'~/folder/'` using
`StorageManager.download_folder('s3://bucket/', '~/folder/')` will copy all contents of the bucket into
`~/folder/`. If the remote contains: `s3://bucket/sub/file.ext`, it will be saved locally as:
`~/folder/sub/file.ext`.

- **Parameters**
  - **remote\_url** ( _str_ ) – Source remote storage location, tree structure of `remote_url` will
    be created under the target `local_folder`. Supports `s3`, `gs`, `azure`, and shared filesystem.
    Example: `'s3://bucket/data/'`

  - **local\_folder** (`Optional`\[`str`\]) – Local target folder to create the full tree from `remote_url`.
    If `None` (default), use the cache folder.

  - **match\_wildcard** (`Optional`\[`str`\]) – If specified, only download files matching this wildcard pattern.
    Example: `\*.json`

  - **overwrite** (`bool`) – If `True`, download remote files even if they exist locally. Defaults to `False`.

  - **skip\_zero\_size\_check** (`bool`) – If `True`, no error will be raised for files with zero bytes size. Defaults to
    `False`.

  - **silence\_errors** (`bool`) – If `True`, silence errors encountered during download. Defaults to `False`.

  - **max\_workers** (`Optional`\[`int`\]) – Number of worker threads for parallel downloads. If `None` (default), uses the number
    of logical CPU cores in the system (default Python behavior).
- **Return type**

`Optional`\[`str`\]

- **Returns**

Target local folder


* * *

### StorageManager.exists\_file [​](https://clear.ml/docs/latest/docs/references/sdk/storage/\#storagemanagerexists_file "Direct link to StorageManager.exists_file")

**_classmethod_ exists\_file(remote\_url)**

Check if remote file exists. Returns `False` for directories.

- **Parameters**

**remote\_url** (`str`) – The URL where the file is stored.
For example: `'s3://bucket/some_file.txt'`, `'file://local/file'`

- **Return type**

`bool`

- **Returns**

`True` if the `remote_url` stores a file. `False` otherwise.


* * *

### StorageManager.get\_file\_size\_bytes [​](https://clear.ml/docs/latest/docs/references/sdk/storage/\#storagemanagerget_file_size_bytes "Direct link to StorageManager.get_file_size_bytes")

**_classmethod_ get\_file\_size\_bytes(remote\_url, silence\_errors=False)**

Get size of the remote file in bytes.

- **Parameters**
  - **remote\_url** (`str`) – The URL where the file is stored.
    For example: `'s3://bucket/some_file.txt'`, `'file://local/file'`

  - **silence\_errors** (`bool`) – If `True`, silence errors encountered while fetching the size of the file.
    Default: `False`
- **Return type**

`Optional`\[`int`\]

- **Returns**

The size of the file in bytes.
`None` if the file could not be found or an error occurred.


* * *

### StorageManager.get\_local\_copy [​](https://clear.ml/docs/latest/docs/references/sdk/storage/\#storagemanagerget_local_copy "Direct link to StorageManager.get_local_copy")

**_classmethod_ get\_local\_copy(remote\_url, cache\_context=None, extract\_archive=True, name=None, force\_download=False)**

Returns a local path to the given remote file.

If the remote URL points to a directly accessible local file, it is returned as-is.
Otherwise, the file is downloaded and stored in the local cache, and the cached path is returned.

Each cache context holds up to 100 files by default. When the limit is reached, the least recently accessed
files are deleted to make room. Calling this function on an already-cached file refreshes its last-accessed
timestamp, preventing its deletion.

- **Parameters**
  - **remote\_url** (`str`) – URL of the remote file to retrieve a local copy of.

  - **cache\_context** (`Optional`\[`str`\]) – Cache context identifier. Defaults to `'global'`.

  - **extract\_archive** (`bool`) – If `True`, and the file is a supported archive (currently zip files only), return the
    path to the extracted archive contents instead of the archive file itself.

  - **name** (`Optional`\[`str`\]) – Name of the target file

  - **force\_download** (`bool`) – If `True`, re-download even if a cached copy exists. Defaults to `False`.
- **Return type**

`Optional`\[`str`\]

- **Returns**

Full path to local copy of the requested URL. Return `None` on error.


* * *

### StorageManager.get\_metadata [​](https://clear.ml/docs/latest/docs/references/sdk/storage/\#storagemanagerget_metadata "Direct link to StorageManager.get_metadata")

**_classmethod_ get\_metadata(remote\_url, return\_full\_path=False, read\_hash=False)**

Get the metadata of the remote object.
The metadata is a dict containing the following keys: `name`, `size`.

- **Parameters**
  - **remote\_url** (`str`) – URL of the remote object to retrieve metadata for. Supports `s3`, `gs`, `azure`,
    shared filesystem, and `http(s)`. Example: `'s3://bucket/data/file.txt'`

  - **return\_full\_path** (`bool`) – If `True`, the `name` field in the returned dict will include the full URL
    including the base. Defaults to `False`.

  - **read\_hash** (`bool`) – If `True`, include SHA-256 hash in the returned dict when the object
    has it stored in its custom metadata.
- **Return type**

`Optional`\[`dict`\]

- **Returns**

A dict containing the metadata of the remote object. `None` in case of an error.


* * *

### StorageManager.list [​](https://clear.ml/docs/latest/docs/references/sdk/storage/\#storagemanagerlist "Direct link to StorageManager.list")

**_classmethod_ list(remote\_url, return\_full\_path=False, with\_metadata=False, read\_hash=False)**

Return a list of object names inside the base path or dictionaries containing the corresponding
objects’ metadata (in case `with_metadata` is `True`).

- **Parameters**
  - **remote\_url** (`str`) – The base path.
    For Google Storage, Azure and S3 it is the bucket of the path, for local files it is the root directory.
    For example: AWS S3: `s3://bucket/folder_` will list all the files you have in
    `s3://bucket-name/folder_\*/\*`. The same behavior with Google Storage: `gs://bucket/folder_`,
    Azure blob storage: `azure://bucket/folder_` and also file system listing: `/mnt/share/folder_`

  - **return\_full\_path** (`bool`) – If `True`, return a list of full object paths instead of relative paths.
    Defaults to
    `False`.

  - **with\_metadata** (`bool`) – If `True`, return a list of dicts containing name and size instead of just names.
    Defaults to `False`.

  - **read\_hash** (`bool`) – If `True` and `with_metadata=True`, include SHA-256 hash in each metadata dict
    when the object has it stored in its custom metadata.
- **Return type**

`Optional`\[`List`\[`Union`\[`str`, `dict`\]\]\]

- **Returns**

A list of object paths relative to the base path, or a list of the objects’ metadata dicts if
`with_metadata=True`. Returns `None` if the list operation is not supported (e.g. HTTP/HTTPS protocols).


* * *

### StorageManager.set\_cache\_file\_limit [​](https://clear.ml/docs/latest/docs/references/sdk/storage/\#storagemanagerset_cache_file_limit "Direct link to StorageManager.set_cache_file_limit")

**_classmethod_ set\_cache\_file\_limit(cache\_file\_limit, cache\_context=None)**

Set the maximum number of files the cache context can hold. Note: the limit applies to file count only, not
total storage size.

- **Parameters**
  - **cache\_file\_limit** (`int`) – Maximum number of cached files.

  - **cache\_context** (`Optional`\[`str`\]) – Optional cache context identifier, default global context.
- **Return type**

`int`

- **Returns**

The new cache context file limit.


* * *

### StorageManager.set\_report\_download\_chunk\_size [​](https://clear.ml/docs/latest/docs/references/sdk/storage/\#storagemanagerset_report_download_chunk_size "Direct link to StorageManager.set_report_download_chunk_size")

**_classmethod_ set\_report\_download\_chunk\_size(chunk\_size\_mb)**

Set the download progress report chunk size (in MB). The chunk size
determines how often the progress reports are logged:
every time a chunk of data with a size greater than `chunk_size_mb`
is downloaded, log the report.
This function overwrites the `sdk.storage.log.report_download_chunk_size_mb`
config entry

- **Parameters**

**chunk\_size\_mb** (`int`) – The chunk size in megabytes

- **Return type**

`None`


* * *

### StorageManager.set\_report\_upload\_chunk\_size [​](https://clear.ml/docs/latest/docs/references/sdk/storage/\#storagemanagerset_report_upload_chunk_size "Direct link to StorageManager.set_report_upload_chunk_size")

**_classmethod_ set\_report\_upload\_chunk\_size(chunk\_size\_mb)**

Set the upload progress report chunk size (in MB). The chunk size
determines how often the progress reports are logged:
every time a chunk of data with a size greater than `chunk_size_mb`
is uploaded, log the report.
This function overrides the `sdk.storage.log.report_upload_chunk_size_mb`
configuration value.

- **Parameters**

**chunk\_size\_mb** (`int`) – The chunk size in megabytes

- **Return type**

`None`


* * *

### StorageManager.upload\_file [​](https://clear.ml/docs/latest/docs/references/sdk/storage/\#storagemanagerupload_file "Direct link to StorageManager.upload_file")

**_classmethod_ upload\_file(local\_file, remote\_url, wait\_for\_upload=True, retries=None)**

Upload a local file to a remote location. Supports `http(s)`, `s3`, `gs`, `azure`, and shared
filesystem.

Examples:

```py
upload_file('/tmp/artifact.yaml', 'http://localhost:8081/manual_artifacts/my_artifact.yaml')

upload_file('/tmp/artifact.yaml', 's3://a_bucket/artifacts/my_artifact.yaml')

upload_file('/tmp/artifact.yaml', '/mnt/share/folder/artifacts/my_artifact.yaml')
```

- **Parameters**
  - **local\_file** (`str`) – Full path of a local file to be uploaded.

  - **remote\_url** (`str`) – Full path or remote URL to upload to (including file name).

  - **wait\_for\_upload** (`bool`) – If `False`, upload in the background and return immediately. Defaults to `True`.

  - **retries** (`Optional`\[`int`\]) – Number of retries before failing to upload file.
- **Return type**

`str`

- **Returns**

Newly uploaded remote URL.


* * *

### StorageManager.upload\_folder [​](https://clear.ml/docs/latest/docs/references/sdk/storage/\#storagemanagerupload_folder "Direct link to StorageManager.upload_folder")

**_classmethod_ upload\_folder(local\_folder, remote\_url, match\_wildcard=None, retries=None)**

Upload a local folder recursively to remote storage, preserving the subfolder structure.

For example, uploading `'~/folder/'` to `'s3://bucket/'` using
`StorageManager.upload_folder('~/folder/', 's3://bucket/')` will copy all contents of the local folder to the
bucket. If the local folder contains `~/folder/sub/file.ext`, it will be saved remotely as
`s3://bucket/sub/file.ext`.

- **Parameters**
  - **local\_folder** (`str`) – Local folder to recursively upload

  - **remote\_url** (`str`) – Target remote storage location. The folder structure of `local_folder` will
    be recreated under `remote_url`. Supports `http(s)`, `s3`, `gs`, `azure`, and shared filesystem.
    Example: `'s3://bucket/data/'`.

  - **match\_wildcard** (`Optional`\[`str`\]) – If specified, only upload files matching this wildcard pattern.
    Example: `\*.json`.

  - **retries** (`Optional`\[`int`\]) – Number of retries before failing to upload a file in the folder.
- **Return type**

`Optional`\[`str`\]

- **Returns**

Newly uploaded remote URL or `None` on error.


- [_class_ StorageManager()](https://clear.ml/docs/latest/docs/references/sdk/storage/#class-storagemanager)
  - [StorageManager.download\_file](https://clear.ml/docs/latest/docs/references/sdk/storage/#storagemanagerdownload_file)
  - [StorageManager.download\_folder](https://clear.ml/docs/latest/docs/references/sdk/storage/#storagemanagerdownload_folder)
  - [StorageManager.exists\_file](https://clear.ml/docs/latest/docs/references/sdk/storage/#storagemanagerexists_file)
  - [StorageManager.get\_file\_size\_bytes](https://clear.ml/docs/latest/docs/references/sdk/storage/#storagemanagerget_file_size_bytes)
  - [StorageManager.get\_local\_copy](https://clear.ml/docs/latest/docs/references/sdk/storage/#storagemanagerget_local_copy)
  - [StorageManager.get\_metadata](https://clear.ml/docs/latest/docs/references/sdk/storage/#storagemanagerget_metadata)
  - [StorageManager.list](https://clear.ml/docs/latest/docs/references/sdk/storage/#storagemanagerlist)
  - [StorageManager.set\_cache\_file\_limit](https://clear.ml/docs/latest/docs/references/sdk/storage/#storagemanagerset_cache_file_limit)
  - [StorageManager.set\_report\_download\_chunk\_size](https://clear.ml/docs/latest/docs/references/sdk/storage/#storagemanagerset_report_download_chunk_size)
  - [StorageManager.set\_report\_upload\_chunk\_size](https://clear.ml/docs/latest/docs/references/sdk/storage/#storagemanagerset_report_upload_chunk_size)
  - [StorageManager.upload\_file](https://clear.ml/docs/latest/docs/references/sdk/storage/#storagemanagerupload_file)
  - [StorageManager.upload\_folder](https://clear.ml/docs/latest/docs/references/sdk/storage/#storagemanagerupload_folder)