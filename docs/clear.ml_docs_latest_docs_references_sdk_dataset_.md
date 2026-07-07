---
url: "https://clear.ml/docs/latest/docs/references/sdk/dataset/"
title: "Dataset | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/sdk/dataset/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

## _class_ Dataset(\_private, task=None, dataset\_project=None, dataset\_name=None, dataset\_tags=None, dataset\_version=None, description=None) [​](https://clear.ml/docs/latest/docs/references/sdk/dataset/\#class-dataset_private-tasknone-dataset_projectnone-dataset_namenone-dataset_tagsnone-dataset_versionnone-descriptionnone "Direct link to class-dataset_private-tasknone-dataset_projectnone-dataset_namenone-dataset_tagsnone-dataset_versionnone-descriptionnone")

A Dataset represents a versioned snapshot of a collection of files.

A dataset is mutable until finalized, after which it becomes immutable and can be used as a parent for new dataset
versions, enabling incremental updates and full lineage tracking.

Datasets can be stored on any storage service of your choice (`s3`,
`gs`, `azure`, Network Storage). Once uploaded, the dataset can be accessed from any
machine.

The typical lifecycle of a dataset is:
`Dataset.create()` -\> `add_files()` -\> `add_external_files()` -\> `upload()` -\> `finalize()`

warning

Do not use directly! Use `Dataset.create(...)` or `Dataset.get(...)` instead.

* * *

### add\_external\_files [​](https://clear.ml/docs/latest/docs/references/sdk/dataset/\#add_external_files "Direct link to add_external_files")

**add\_external\_files(source\_url, wildcard=None, dataset\_path=None, recursive=True, verbose=False, max\_workers=None, read\_hash=False)**

Add external files or folders to the current dataset.
External file links can be from cloud storage (`s3://`, `gs://`, `azure://`), local/network storage
(`file://`) or `http(s)//` files.
Calculates file size for each file and compares against the parent dataset to detect changes.

Examples:

- Add `file.jpg` to the dataset. When retrieving a copy of the entire dataset (see `dataset.get_local_copy()`).
This file will be located in `"./my_dataset/new_folder/file.jpg"`:
`dataset.add_external_files(source_url="s3://my_bucket/stuff/file.jpg", dataset_path="/my_dataset/new_folder/")`

- Add all `jpg` files located in an S3 bucket called `"my_bucket"` to the dataset.
`dataset.add_external_files(source_url="s3://my/bucket/", wildcard = "\*.jpg", dataset_path="/my_dataset/new_folder/")`

- Add the entire content of `"remote_folder"` to the dataset.
`dataset.add_external_files(source_url="s3://bucket/remote_folder/", dataset_path="/my_dataset/new_folder/")`

- Add the local file `"/folder/local_file.jpg"` to the dataset.
`dataset.add_external_files(source_url="file:///folder/local_file.jpg", dataset_path="/my_dataset/new_folder/")`

- **Parameters**
  - **source\_url** (`Union`\[`str`, `Sequence`\[`str`\]\]) – URL or list of URLs to add to the dataset. Examples: `s3://bucket/folder/path`,
    `[s3://bucket/folder/file.csv, http://web.com/file.txt]`.

  - **wildcard** (`Union`\[`Sequence`\[`str`\], `str`, `None`\]) – Only add files matching this wildcard pattern. Can be a single string or a list of patterns.

  - **dataset\_path** (`Union`\[`Sequence`\[`str`\], `str`, `None`\]) – The location in the dataset where the file(s) will be downloaded into, or list/tuple of
    locations (if list/tuple, it must be the same length as `source_url`).
    For example: for `source_url='s3://bucket/remote_folder/image.jpg'` and `dataset_path='s3_files'`,
    `'image.jpg'` will be downloaded to `'s3_files/image.jpg'` (relative path to the dataset).
    For `source_url=['s3://bucket/remote_folder/image.jpg', 's3://bucket/remote_folder/image2.jpg']` and
    `dataset_path=['s3_files', 's3_files_2']`, `'image.jpg'` will be downloaded to `'s3_files/image.jpg'`
    and `'image2.jpg'` will be downloaded to `'s3_files_2/image2.jpg'` (relative path to the dataset).

  - **recursive** (`bool`) – If `True`, match all wildcard files recursively

  - **verbose** (`bool`) – If `True`, print to console files added/modified

  - **max\_workers** (`Optional`\[`int`\]) – The number of threads to add the external files with. Useful when `source_url` is
    a sequence. Defaults to the number of logical cores

  - **read\_hash** (`bool`) – If `True`, read the SHA-256 hash from each object’s custom cloud metadata and store it
    on the resulting `LinkEntry`. When available, hash comparison is used for change detection instead of
    file size. Only effective for objects uploaded with `upload_hash` set in the `StorageHelper` extra dict.
    Defaults to `False`.
- **Return type**

`int`

- **Returns**

Number of file links added


* * *

### add\_files [​](https://clear.ml/docs/latest/docs/references/sdk/dataset/\#add_files "Direct link to add_files")

**add\_files(path, wildcard=None, local\_base\_folder=None, dataset\_path=None, recursive=True, verbose=False, max\_workers=None)**

Add a folder or files into the current dataset. Calculates the file hash and compares against parent, and marks
files for upload.

- **Parameters**
  - **path** (`Union`\[`str`, `Path`, `Path`\]) – Path to the local folder or file to add to the dataset.

  - **wildcard** (`Union`\[`Sequence`\[`str`\], `str`, `None`\]) – Only add files matching this wildcard pattern. Can be a single string or a list of patterns.

  - **local\_base\_folder** (`Optional`\[`str`\]) – Files are placed in the dataset relative to this folder. If not provided, defaults to
    `path`.

  - **dataset\_path** (`Optional`\[`str`\]) – Target location inside the dataset where the folder/files will be placed.

  - **recursive** (`bool`) – If `True` (default), match all wildcard files recursively.

  - **verbose** (`bool`) – If `True`, print to console files added/modified. Defaults to `False`.

  - **max\_workers** (`Optional`\[`int`\]) – The number of threads to add the files with. Defaults to the number of logical cores.
- **Return type**

`int`

- **Returns**

Number of files added.


* * *

### add\_tags [​](https://clear.ml/docs/latest/docs/references/sdk/dataset/\#add_tags "Direct link to add_tags")

**add\_tags(tags)**

Add tags to this dataset. Existing tags are preserved. Has no effect when the task is executed remotely.

- **Parameters**

**tags** (`Union`\[`Sequence`\[`str`\], `str`\]) – A tag string or list of tag strings to add.

- **Return type**

`None`


* * *

### Dataset.create [​](https://clear.ml/docs/latest/docs/references/sdk/dataset/\#datasetcreate "Direct link to Dataset.create")

**_classmethod_ create(dataset\_name=None, dataset\_project=None, dataset\_tags=None, parent\_datasets=None, use\_current\_task=False, dataset\_version=None, output\_uri=None, description=None)**

Create a new dataset. Multiple dataset parents are supported.
Merging of parent datasets is done based on the order,
where each one can override overlapping files in the previous parent.

- **Parameters**
  - **dataset\_name** (`Optional`\[`str`\]) – Name of the new dataset.

  - **dataset\_project** (`Optional`\[`str`\]) – Project containing the dataset.
    If not specified, infer project name from parent datasets.

  - **dataset\_tags** (`Optional`\[`Sequence`\[`str`\]\]) – List of tags to attach to the new dataset.

  - **parent\_datasets** (`Optional`\[`Sequence`\[`Union`\[`str`, `Dataset`\]\]\]) – List of parent datasets to inherit files from. Accepts a sequence of dataset IDs
    (strings) and/or Dataset objects. Files are merged in order, with later parents overriding earlier ones.

  - **use\_current\_task** (`bool`) – If `False` (default), create a new task for the dataset.
    If `True`, the dataset is attached to the current Task.

  - **dataset\_version** (`Optional`\[`str`\]) – Version of the new dataset. If not set, try to find the latest version
    of the dataset with given `dataset_name` and `dataset_project` and auto-increment it.

  - **output\_uri** (`Optional`\[`str`\]) – Storage location for uploaded dataset files and preview samples.

    The following are examples of `output_uri` values for the supported locations:
    - A shared folder: `/mnt/share/folder`

    - S3: `s3://bucket/folder`

    - Google Cloud Storage: `gs://bucket-name/folder`

    - Azure Storage: `azure://company.blob.core.windows.net/folder/`

    - Default file server: `None`
  - **description** (`Optional`\[`str`\]) – Description of the dataset.
- **Return type**

`Dataset`

- **Returns**

Newly created Dataset object.


* * *

### Dataset.delete [​](https://clear.ml/docs/latest/docs/references/sdk/dataset/\#datasetdelete "Direct link to Dataset.delete")

**_classmethod_ delete(dataset\_id=None, dataset\_project=None, dataset\_name=None, force=False, dataset\_version=None, entire\_dataset=False, shallow\_search=False, delete\_files=True, delete\_external\_files=False)**

Delete one or more datasets. If multiple datasets match the given parameters and `entire_dataset=False`,
an exception is raised.

- **Parameters**
  - **dataset\_id** (`Optional`\[`str`\]) – The ID of the dataset(s) to be deleted.

  - **dataset\_project** (`Optional`\[`str`\]) – The project the dataset(s) to be deleted belong(s) to.

  - **dataset\_name** (`Optional`\[`str`\]) – The name of the dataset(s) to delete.

  - **force** (`bool`) – If `True`, delete the dataset(s) even if it is used. Required when `entire_dataset=True`.

  - **dataset\_version** (`Optional`\[`str`\]) – The version of the dataset(s) to delete.

  - **entire\_dataset** (`bool`) – If `True`, delete all versions matching `dataset_project`, `dataset_name`,
    `dataset_version`. Requires `force=True`.

  - **shallow\_search** (`bool`) – If `True`, search only the first 500 results (first page).

  - **delete\_files** (`bool`) – If `True`, delete all files in the dataset (from the ClearML file server), as well as
    all artifacts related to the dataset.

  - **delete\_external\_files** (`bool`) – If `True`, delete all external files in the dataset from their external storage
    locations.
- **Return type**

`None`


* * *

### file\_entries\_dict [​](https://clear.ml/docs/latest/docs/references/sdk/dataset/\#file_entries_dict "Direct link to file_entries_dict")

**property file\_entries\_dict: Mapping\[str, FileEntry\]**

Notice this call returns an internal representation, do not modify!

- **Return type**

`Mapping`\[`str`, `FileEntry`\]

- **Returns**

dict with relative file path as key, and `FileEntry` as value.


* * *

### finalize [​](https://clear.ml/docs/latest/docs/references/sdk/dataset/\#finalize "Direct link to finalize")

**finalize(verbose=False, raise\_on\_error=True, auto\_upload=False)**

Finalize the dataset, preventing further modification.

Finalization requires that all pending file uploads have been completed. If `upload()` has not been called
and `auto_upload=False`, this method raises a `ValueError` (or returns `False` when
`raise_on_error=False`).

- **Parameters**
  - **verbose** (`bool`) – If `True`, print verbose progress report. Defaults to `False`.

  - **raise\_on\_error** (`bool`) – If `True` (default), raise exception if finalization fails.

  - **auto\_upload** (`bool`) – If `True`, automatically upload any pending files to the default storage location
    before finalizing.
- **Return type**

`bool`

- **Returns**

`True` if finalization succeeded.


* * *

### Dataset.get [​](https://clear.ml/docs/latest/docs/references/sdk/dataset/\#datasetget "Direct link to Dataset.get")

**_classmethod_ get(dataset\_id=None, dataset\_project=None, dataset\_name=None, dataset\_tags=None, only\_completed=False, only\_published=False, include\_archived=False, auto\_create=False, writable\_copy=False, dataset\_version=None, alias=None, overridable=False, shallow\_search=False, silence\_alias\_warnings=False, \*\*kwargs)**

Get a specific Dataset. If multiple datasets are found, the dataset with the
highest semantic version is returned. If no semantic version is found, the most recently
updated dataset is returned. This function raises an Exception in case no dataset
can be found and the `auto_create=True` flag is not set.

- **Parameters**
  - **dataset\_id** (`Optional`\[`str`\]) – Requested dataset ID.

  - **dataset\_project** (`Optional`\[`str`\]) – Requested dataset project name.

  - **dataset\_name** (`Optional`\[`str`\]) – Requested dataset name.

  - **dataset\_tags** (`Optional`\[`Sequence`\[`str`\]\]) – Requested dataset tags (list of tag strings).

  - **only\_completed** (`bool`) – Return only if the requested dataset is completed or published.

  - **only\_published** (`bool`) – Return only if the requested dataset is published.

  - **include\_archived** (`bool`) – Include archived tasks and datasets also.

  - **auto\_create** (`bool`) – Create a new dataset if it does not exist yet.

  - **writable\_copy** (`bool`) – Get a newly created mutable dataset with the current one as its parent,
    so new files can be added to the instance.

  - **dataset\_version** (`Optional`\[`str`\]) – Requested version of the dataset.

  - **alias** (`Optional`\[`str`\]) – Alias of the dataset. If set, the alias-to-dataset-ID mapping will be set under the `Datasets`
    hyperparameters section.

  - **overridable** (`bool`) – If `True`, allow overriding the dataset ID with a given alias in the
    hyperparameters section. Useful when one wants to change the dataset used when running
    a task remotely. If the alias parameter is not set, this parameter has no effect.

  - **shallow\_search** (`bool`) – If `True`, search only the first 500 results (first page).

  - **silence\_alias\_warnings** (`bool`) – If `True`, suppress the warning logged when no `alias` is provided.

  - **kwargs** ( _Any_ ) –
- **Return type**

`Dataset`

- **Returns**

Dataset object


* * *

### get\_default\_storage [​](https://clear.ml/docs/latest/docs/references/sdk/dataset/\#get_default_storage "Direct link to get_default_storage")

**get\_default\_storage()**

Return the default storage location of the dataset.

- **Return type**

`Optional`\[`str`\]

- **Returns**

URL for the default storage location.


* * *

### get\_dependency\_graph [​](https://clear.ml/docs/latest/docs/references/sdk/dataset/\#get_dependency_graph "Direct link to get_dependency_graph")

**get\_dependency\_graph()**

Return the DAG of the dataset dependencies (all previous dataset version and their parents).

Example:

```py
{

    'current_dataset_id': ['parent_1_id', 'parent_2_id'],

    'parent_2_id': ['parent_1_id'],

    'parent_1_id': [],

}
```

- **Return type**

`Dict`\[`str`, `List`\[`str`\]\]

- **Returns**

dict representing the genealogy dag graph of the current dataset.


* * *

### get\_local\_copy [​](https://clear.ml/docs/latest/docs/references/sdk/dataset/\#get_local_copy "Direct link to get_local_copy")

**get\_local\_copy(use\_soft\_links=None, part=None, num\_parts=None, raise\_on\_error=True, max\_workers=None, files=None)**

Download and return a read-only local copy of the entire dataset by merging files from all parent versions.
The dataset must be finalized before calling this method.

- **Parameters**
  - **use\_soft\_links** (`Optional`\[`bool`\]) – If `True`, use soft links. Defaults to `False` on windows, `True` on Posix systems.

  - **part** (`Optional`\[`int`\]) – If provided, download only the selected part (index) of the Dataset.
    First part number is `0` and last part is `num_parts-1`.
    Notice, if `num_parts` is not provided, the number of parts equals the total number of chunks
    (i.e. sum over all chunks from the specified Dataset including all parent Datasets).
    This argument is passed to parent datasets, as well as the implicit `num_parts`,
    allowing users to get a partial copy of the entire dataset, for multi node/step processing.

  - **num\_parts** (`Optional`\[`int`\]) – If specified, normalize the number of chunks stored to the
    requested number of parts. Notice that the actual chunks used per part are rounded down.
    Example: Assuming total 8 chunks for this dataset (including parent datasets),
    and `num_parts=5`, the chunk index used per parts would be: `part=0` -\> `chunks[0,5]`,
    `part=1` -\> `chunks[1,6]`, `part=2` -\> `chunks[2,7]`, `part=3` -\> `chunks[3, ]`

  - **raise\_on\_error** (`bool`) – If `True` (default), raise exception if any file fails to merge.

  - **max\_workers** (`Optional`\[`int`\]) – Number of threads for downloading the dataset copy. Defaults
    to the number of logical cores.

  - **files** (`Optional`\[`List`\[`str`\]\]) – List of relative file paths to download. When provided, only the chunks containing those files are
    fetched, and the result is cached separately from the full dataset copy. If `None` (default), the full
    dataset is downloaded.
- **Return type**

`str`

- **Returns**

A base folder for the entire dataset


* * *

### get\_logger [​](https://clear.ml/docs/latest/docs/references/sdk/dataset/\#get_logger "Direct link to get_logger")

**get\_logger()**

Return a `Logger` object for the Dataset, allowing users to report metrics
and debug samples on the Dataset itself.

- **Return type**

[`Logger`](https://clear.ml/docs/latest/docs/references/sdk/logger#clearml.Logger)

- **Returns**

`Logger` object


* * *

### get\_metadata [​](https://clear.ml/docs/latest/docs/references/sdk/dataset/\#get_metadata "Direct link to get_metadata")

**get\_metadata(metadata\_name='metadata')**

Get attached metadata in its original format. Returns `None` if no metadata is found .

- **Return type**

`Union`\[`array`, `DataFrame`, `dict`, `str`, `bool`, `None`\]

- **Parameters**

**metadata\_name** ( _str_ ) –


* * *

### get\_mutable\_local\_copy [​](https://clear.ml/docs/latest/docs/references/sdk/dataset/\#get_mutable_local_copy "Direct link to get_mutable_local_copy")

**get\_mutable\_local\_copy(target\_folder, overwrite=False, part=None, num\_parts=None, raise\_on\_error=True, max\_workers=None)**

Returns a base folder with a writable (mutable) local copy of the entire dataset.
Download and copy / soft-link, files from all the parent dataset versions. Note that the method initially
downloads the local copy into a cache directory before moving it to the `target_folder`. Make sure the default
cache directory has sufficient disk space.

- **Parameters**
  - **target\_folder** (`Union`\[`Path`, `Path`, `str`\]) – Target folder for the writable copy

  - **overwrite** (`bool`) – If `True`, recursively delete the target folder before creating a copy.
    If `False` (default) and target folder contains files, raise exception or return `None`.

  - **part** (`Optional`\[`int`\]) – If provided only download the selected part (index) of the Dataset.
    First part number is `0` and last part is `num_parts-1`.
    Notice, if `num_parts` is not provided, number of parts will be equal to the total number of chunks
    (i.e. sum over all chunks from the specified Dataset including all parent Datasets).
    This argument is passed to parent datasets, as well as the implicit `num_parts`,
    allowing users to get a partial copy of the entire dataset, for multi node/step processing.

  - **num\_parts** (`Optional`\[`int`\]) – If specified, normalize the number of chunks stored to the
    requested number of parts. Notice that the actual chunks used per part are rounded down.
    Example: Assuming total 8 chunks for this dataset (including parent datasets),
    and `num_parts=5`, the chunk index used per parts would be: `part=0` -\> `chunks[0,5]`,
    `part=1` -\> `chunks[1,6]`, `part=2` -\> `chunks[2,7]`, `part=3` -\> `chunks[3, ]`

  - **raise\_on\_error** (`bool`) – If `True`, raise exception if dataset merging failed on any file

  - **max\_workers** (`Optional`\[`int`\]) – Number of threads for downloading. Defaults
    to the number of logical cores.
- **Return type**

`Optional`\[`str`\]

- **Returns**

The target folder containing the entire dataset


* * *

### get\_num\_chunks [​](https://clear.ml/docs/latest/docs/references/sdk/dataset/\#get_num_chunks "Direct link to get_num_chunks")

**get\_num\_chunks(include\_parents=True)**

Return the number of chunks stored on this dataset.

- **Parameters**

**include\_parents** (`bool`) – If `True` (default),
return the total number of chunks from this version and all parent versions.
If `False`, only return the number of chunks stored on this specific version.

- **Return type**

`int`

- **Returns**

Number of stored chunks.


* * *

### get\_offline\_mode\_folder [​](https://clear.ml/docs/latest/docs/references/sdk/dataset/\#get_offline_mode_folder "Direct link to get_offline_mode_folder")

**get\_offline\_mode\_folder()**

Return the folder where all the dataset data is stored in the offline session.

- **Return type**

`Optional`\[`Path`\]

- **Returns**

Path object, local folder


* * *

### Dataset.import\_offline\_session [​](https://clear.ml/docs/latest/docs/references/sdk/dataset/\#datasetimport_offline_session "Direct link to Dataset.import_offline_session")

**_classmethod_ import\_offline\_session(session\_folder\_zip, upload=True, finalize=False)**

Import an offline session of a dataset.
Includes repository details, installed packages, artifacts, logs, metric and debug samples.

- **Parameters**
  - **session\_folder\_zip** (`str`) – Path to a folder containing the session, or zip-file of the session folder.

  - **upload** (`bool`) – If `True`, upload the dataset’s data.

  - **finalize** (`bool`) – If `True`, finalize the dataset.
- **Return type**

`str`

- **Returns**

The ID of the imported dataset.


* * *

### is\_dirty [​](https://clear.ml/docs/latest/docs/references/sdk/dataset/\#is_dirty "Direct link to is_dirty")

**is\_dirty()**

Return `True` if the dataset has pending uploads that would prevent finalization.

- **Return type**

`bool`

- **Returns**

`True` if the dataset has pending uploads. Call `upload()` before finalizing.


* * *

### is\_final [​](https://clear.ml/docs/latest/docs/references/sdk/dataset/\#is_final "Direct link to is_final")

**is\_final()**

Return `True` if the dataset was finalized and cannot be changed anymore.

- **Return type**

`bool`

- **Returns**

`True` if dataset is finalized.


* * *

### Dataset.is\_offline [​](https://clear.ml/docs/latest/docs/references/sdk/dataset/\#datasetis_offline "Direct link to Dataset.is_offline")

**_classmethod_ is\_offline()**

Return offline-mode state, If in offline-mode, no communication to the backend is enabled.

- **Return type**

`bool`

- **Returns**

boolean offline-mode state


* * *

### link\_entries\_dict [​](https://clear.ml/docs/latest/docs/references/sdk/dataset/\#link_entries_dict "Direct link to link_entries_dict")

**property link\_entries\_dict: Mapping\[str, LinkEntry\]**

Notice this call returns an internal representation, do not modify!

- **Return type**

`Mapping`\[`str`, `LinkEntry`\]

- **Returns**

dict with relative file path as key, and `LinkEntry` as value.


* * *

### list\_added\_files [​](https://clear.ml/docs/latest/docs/references/sdk/dataset/\#list_added_files "Direct link to list_added_files")

**list\_added\_files(dataset\_id=None)**

Return a list of files that were added in this dataset version relative to the specified `dataset_id`.

- **Parameters**

**dataset\_id** (`Optional`\[`str`\]) – Dataset ID to compare against. If `None` (default), compare against the parent datasets.

- **Return type**

`List`\[`str`\]

- **Returns**

Sorted list of relative file paths (files might not be available locally until `get_local_copy()` is
called)


* * *

### Dataset.list\_datasets [​](https://clear.ml/docs/latest/docs/references/sdk/dataset/\#datasetlist_datasets "Direct link to Dataset.list_datasets")

**_classmethod_ list\_datasets(dataset\_project=None, partial\_name=None, tags=None, ids=None, only\_completed=True, recursive\_project\_search=True, include\_archived=True)**

Query list of dataset in the system.

- **Parameters**
  - **dataset\_project** (`Optional`\[`str`\]) – Specify dataset project name.

  - **partial\_name** (`Optional`\[`str`\]) – Filter datasets by partial name match. Supports regular expressions. To match special
    characters literally, wrap the name with `re.escape()`.

  - **tags** (`Optional`\[`Sequence`\[`str`\]\]) – Specify user tags.

  - **ids** (`Optional`\[`Sequence`\[`str`\]\]) – List specific dataset based on IDs list.

  - **only\_completed** (`bool`) – If `False`, return datasets that are still in progress (uploading/edited etc.).
    Defaults to `True`.

  - **recursive\_project\_search** (`bool`) – If `True` (default) and the `dataset_project` argument is set,
    search inside subprojects as well.
    If `False`, don’t search inside subprojects (except for the special `.datasets` subproject)

  - **include\_archived** (`bool`) – If `True`, include archived datasets as well.
- **Return type**

`List`\[`dict`\]

- **Returns**

List of dictionaries with dataset information.
Example: `[{'name': name, 'project': project name, 'id': dataset_id, 'created': date_created},]`


* * *

### list\_files [​](https://clear.ml/docs/latest/docs/references/sdk/dataset/\#list_files "Direct link to list_files")

**list\_files(dataset\_path=None, recursive=True, dataset\_id=None)**

Return a list of files in the current dataset.

- **Parameters**
  - **dataset\_path** (`Optional`\[`str`\]) – Only match files matching the `dataset_path` (including wildcards).
    Example: `'folder/sub/\*.json'`

  - **recursive** (`bool`) – If `True` (default), match `dataset_path` recursively

  - **dataset\_id** (`Optional`\[`str`\]) – If provided, return a list of files that remained unchanged since the specified
    `dataset_id`. Defaults to `None`.
- **Return type**

`List`\[`str`\]

- **Returns**

List of files with relative path
(files might not be available locally until `get_local_copy()` is called)


* * *

### list\_modified\_files [​](https://clear.ml/docs/latest/docs/references/sdk/dataset/\#list_modified_files "Direct link to list_modified_files")

**list\_modified\_files(dataset\_id=None)**

Return a list of files modified when comparing to a specific `dataset_id`.

- **Parameters**

**dataset\_id** (`Optional`\[`str`\]) – Dataset ID (`str`) to compare against, if `None` is given compare against the parent
datasets

- **Return type**

`List`\[`str`\]

- **Returns**

List of files with relative path (files might not be available locally until `get_local_copy()` is
called)


* * *

### list\_removed\_files [​](https://clear.ml/docs/latest/docs/references/sdk/dataset/\#list_removed_files "Direct link to list_removed_files")

**list\_removed\_files(dataset\_id=None)**

Return a list of files removed when comparing to a specific `dataset_id`.

- **Parameters**

**dataset\_id** (`Optional`\[`str`\]) – Dataset ID to compare against, if `None` is given compare against the parent datasets.

- **Return type**

`List`\[`str`\]

- **Returns**

List of files with relative path (files might not be available locally until `get_local_copy()` is
called)


* * *

### Dataset.move\_to\_project [​](https://clear.ml/docs/latest/docs/references/sdk/dataset/\#datasetmove_to_project "Direct link to Dataset.move_to_project")

**_classmethod_ move\_to\_project(new\_dataset\_project, dataset\_project, dataset\_name)**

Move the dataset to another project.

- **Parameters**
  - **new\_dataset\_project** (`str`) – New project to move the dataset to

  - **dataset\_project** (`str`) – Project of the dataset to move to new project

  - **dataset\_name** (`str`) – Name of the dataset to move to new project
- **Return type**

`None`


* * *

### publish [​](https://clear.ml/docs/latest/docs/references/sdk/dataset/\#publish "Direct link to publish")

**publish(raise\_on\_error=True)**

Publish the dataset. If dataset is not finalized, raises an exception.

- **Parameters**

**raise\_on\_error** (`bool`) – If `True`, raise exception if dataset publishing failed.

- **Return type**

`bool`


* * *

### remove\_files [​](https://clear.ml/docs/latest/docs/references/sdk/dataset/\#remove_files "Direct link to remove_files")

**remove\_files(dataset\_path=None, recursive=True, verbose=False)**

Remove files from the current dataset.

- **Parameters**
  - **dataset\_path** (`Optional`\[`str`\]) – Remove files from the dataset.
    The path is always relative to the dataset (e.g `'folder/file.bin'`).
    External files can also be removed by their links (e.g. `'s3://bucket/file'`)

  - **recursive** (`bool`) – If `True`, match all wildcard files recursively

  - **verbose** (`bool`) – If `True`, print to console files removed
- **Return type**

`int`

- **Returns**

Number of files removed


* * *

### Dataset.rename [​](https://clear.ml/docs/latest/docs/references/sdk/dataset/\#datasetrename "Direct link to Dataset.rename")

**_classmethod_ rename(new\_dataset\_name, dataset\_project, dataset\_name)**

Rename a dataset.

- **Parameters**
  - **new\_dataset\_name** (`str`) – New name to assign to the dataset.

  - **dataset\_project** (`str`) – Project containing the dataset.

  - **dataset\_name** (`str`) – Current name of the dataset (before renaming).
- **Return type**

`None`


* * *

### set\_description [​](https://clear.ml/docs/latest/docs/references/sdk/dataset/\#set_description "Direct link to set_description")

**set\_description(description)**

Set description of the dataset.

- **Parameters**

**description** (`str`) – Description to be set.

- **Return type**

`None`


* * *

### set\_metadata [​](https://clear.ml/docs/latest/docs/references/sdk/dataset/\#set_metadata "Direct link to set_metadata")

**set\_metadata(metadata, metadata\_name='metadata', ui\_visible=True)**

Attach user-defined metadata to the dataset. See `Task.upload_artifact` for supported types.
If type is Pandas DataFrames, optionally make it visible as a table in the UI.

- **Return type**

`None`

- **Parameters**
  - **metadata** ( _Union_ _\[_ _array_ \\*, \\* _DataFrame_ \\*, \\* _Dict_ _\[_ _str_ \\*, \\* _Any_ _\]_ _\]_ ) –

  - **metadata\_name** ( _str_ ) –

  - **ui\_visible** ( _bool_ ) –

* * *

### Dataset.set\_offline [​](https://clear.ml/docs/latest/docs/references/sdk/dataset/\#datasetset_offline "Direct link to Dataset.set_offline")

**_classmethod_ set\_offline(offline\_mode=False)**

Set offline mode, where all data and logs are stored into local folder, for later transmission.

- **Parameters**

**offline\_mode** (`bool`) – If `True`, offline-mode is turned on, and no communication to the backend is enabled.

- **Return type**

`None`


* * *

### Dataset.squash [​](https://clear.ml/docs/latest/docs/references/sdk/dataset/\#datasetsquash "Direct link to Dataset.squash")

**_classmethod_ squash(dataset\_name, dataset\_ids=None, dataset\_project\_name\_pairs=None, output\_url=None, close\_squashed\_dataset=True)**

Generate a new dataset from the squashed set of dataset versions.
If a single version is given it will squash to the root (i.e. create single standalone version)
If a set of versions are given it will squash the versions diff into a single version.

- **Parameters**
  - **dataset\_name** (`str`) – Name for the new squashed dataset.

  - **dataset\_ids** (`Optional`\[`Sequence`\[`Union`\[`str`, `Dataset`\]\]\]) – List of dataset IDs or `Dataset` objects to squash. Notice order does matter.
    The versions are merged from first to last.

  - **dataset\_project\_name\_pairs** (`Optional`\[`Sequence`\[`str`\]\]) – List of pairs (`project_name`, `dataset_name`) to squash.
    Notice order does matter. The versions are merged from first to last.

  - **output\_url** (`Optional`\[`str`\]) – Target storage for the compressed dataset (default: file server).
    Examples: `s3://bucket/data`, `gs://bucket/data` , `azure://bucket/data` , `/mnt/share/data`

  - **close\_squashed\_dataset** (`Optional`\[`bool`\]) – If `True`, upload and finalize the newly created dataset.
- **Return type**

`Dataset`

- **Returns**

Newly created dataset object.


* * *

### sync\_folder [​](https://clear.ml/docs/latest/docs/references/sdk/dataset/\#sync_folder "Direct link to sync_folder")

**sync\_folder(local\_path, dataset\_path=None, verbose=False)**

Synchronize the dataset with a local folder. The dataset is synchronized from the
`relative_base_folder` (default: dataset root) and deeper with the specified local path.
Note that if a remote file is identified as being modified when syncing, it will
be added as a `FileEntry`, ready to be uploaded to the ClearML server. This version of the
file is considered “newer” and it will be downloaded instead of the one stored at its
remote address when calling `Dataset.get_local_copy()`.

- **Parameters**
  - **local\_path** (`Union`\[`Path`, `Path`, `str`\]) – Local folder to sync (assumes all files and recursive).

  - **dataset\_path** (`Union`\[`Path`, `Path`, `str`, `None`\]) – Target dataset path to sync with (default the root of the dataset).

  - **verbose** (`bool`) – If `True`, print to console files added/modified/removed.
- **Return type**

(<class ‘int’>, <class ‘int’>, <class ‘int’>)

- **Returns**

Number of files removed, number of files modified/added.


* * *

### update\_changed\_files [​](https://clear.ml/docs/latest/docs/references/sdk/dataset/\#update_changed_files "Direct link to update_changed_files")

**update\_changed\_files(num\_files\_added=None, num\_files\_modified=None, num\_files\_removed=None)**

Update the internal state keeping track of added, modified and removed files.

- **Parameters**
  - **num\_files\_added** (`Optional`\[`int`\]) – Amount of files added when compared to the parent dataset

  - **num\_files\_modified** (`Optional`\[`int`\]) – Amount of files with the same name but a different hash when
    compared to the parent dataset

  - **num\_files\_removed** (`Optional`\[`int`\]) – Amount of files removed when compared to the parent dataset
- **Return type**

`None`


* * *

### upload [​](https://clear.ml/docs/latest/docs/references/sdk/dataset/\#upload "Direct link to upload")

**upload(show\_progress=True, verbose=False, output\_url=None, compression=None, chunk\_size=None, max\_workers=None, retries=3, preview=True, upload\_as\_external\_links=False)**

Start file uploading, the function returns when all files are uploaded.

- **Parameters**
  - **show\_progress** (`bool`) – If `True`, show upload progress bar

  - **verbose** (`bool`) – If `True`, print verbose progress report

  - **output\_url** (`Optional`\[`str`\]) – Target storage location for the compressed dataset. Defaults to the file server.
    Examples: `s3://bucket/data`, `gs://bucket/data` , `azure://bucket/data` , `/mnt/share/data`

  - **compression** (`Optional`\[`str`\]) – Compression algorithm for the Zipped dataset file (default: `ZIP_DEFLATED`)

  - **chunk\_size** (`Optional`\[`int`\]) – Artifact chunk size (MB) for the compressed dataset.
    If `None` (default), uses 512 MB. Pass `-1` to store the entire dataset changeset in a single zip.

  - **max\_workers** (`Optional`\[`int`\]) – Numbers of threads to be spawned when zipping and uploading the files.

    If `None` (default) it will be set to:
    - `1`: if the upload destination is a cloud provider (`s3`, `gs`, `azure`)

    - Number of logical cores: otherwise
  - **retries** ( _int_ ) – Number of retries before failing to upload each zip. If 0, the upload is not retried.

  - **preview** (`bool`) – If `True` (default) the dataset preview is uploaded and shown in the UI.

  - **upload\_as\_external\_links** (`bool`) – If `True`, upload each local file entry directly to storage
    as an individual object (instead of bundling into a zip artifact) and register it as an
    external link entry. The destination path is `&lt;output_url&gt;/external_links/&lt;dataset_id&gt;/`.
    Requires `output_url` to be set (either as argument or as the task’s output URI).
- **Raise**

If the upload failed (i.e. at least one zip failed to upload), raises a `ValueError`.

- **Return type**

`Optional`\[`bool`\]


* * *

### verify\_dataset\_hash [​](https://clear.ml/docs/latest/docs/references/sdk/dataset/\#verify_dataset_hash "Direct link to verify_dataset_hash")

**verify\_dataset\_hash(local\_copy\_path=None, skip\_hash=False, verbose=False)**

Verify the current copy of the dataset against the stored hash.

- **Parameters**
  - **local\_copy\_path** (`Optional`\[`str`\]) – Specify local path containing a copy of the dataset.
    If not provided use the cached folder.

  - **skip\_hash** (`bool`) – If `True`, verify file size only instead of computing the SHA-256 hash.

  - **verbose** (`bool`) – If `True`, print errors while testing dataset files hash.
- **Return type**

`List`\[`str`\]

- **Returns**

List of files with unmatched hashes.


- [_class_ Dataset(\_private, task=None, dataset\_project=None, dataset\_name=None, dataset\_tags=None, dataset\_version=None, description=None)](https://clear.ml/docs/latest/docs/references/sdk/dataset/#class-dataset_private-tasknone-dataset_projectnone-dataset_namenone-dataset_tagsnone-dataset_versionnone-descriptionnone)
  - [add\_external\_files](https://clear.ml/docs/latest/docs/references/sdk/dataset/#add_external_files)
  - [add\_files](https://clear.ml/docs/latest/docs/references/sdk/dataset/#add_files)
  - [add\_tags](https://clear.ml/docs/latest/docs/references/sdk/dataset/#add_tags)
  - [Dataset.create](https://clear.ml/docs/latest/docs/references/sdk/dataset/#datasetcreate)
  - [Dataset.delete](https://clear.ml/docs/latest/docs/references/sdk/dataset/#datasetdelete)
  - [file\_entries\_dict](https://clear.ml/docs/latest/docs/references/sdk/dataset/#file_entries_dict)
  - [finalize](https://clear.ml/docs/latest/docs/references/sdk/dataset/#finalize)
  - [Dataset.get](https://clear.ml/docs/latest/docs/references/sdk/dataset/#datasetget)
  - [get\_default\_storage](https://clear.ml/docs/latest/docs/references/sdk/dataset/#get_default_storage)
  - [get\_dependency\_graph](https://clear.ml/docs/latest/docs/references/sdk/dataset/#get_dependency_graph)
  - [get\_local\_copy](https://clear.ml/docs/latest/docs/references/sdk/dataset/#get_local_copy)
  - [get\_logger](https://clear.ml/docs/latest/docs/references/sdk/dataset/#get_logger)
  - [get\_metadata](https://clear.ml/docs/latest/docs/references/sdk/dataset/#get_metadata)
  - [get\_mutable\_local\_copy](https://clear.ml/docs/latest/docs/references/sdk/dataset/#get_mutable_local_copy)
  - [get\_num\_chunks](https://clear.ml/docs/latest/docs/references/sdk/dataset/#get_num_chunks)
  - [get\_offline\_mode\_folder](https://clear.ml/docs/latest/docs/references/sdk/dataset/#get_offline_mode_folder)
  - [Dataset.import\_offline\_session](https://clear.ml/docs/latest/docs/references/sdk/dataset/#datasetimport_offline_session)
  - [is\_dirty](https://clear.ml/docs/latest/docs/references/sdk/dataset/#is_dirty)
  - [is\_final](https://clear.ml/docs/latest/docs/references/sdk/dataset/#is_final)
  - [Dataset.is\_offline](https://clear.ml/docs/latest/docs/references/sdk/dataset/#datasetis_offline)
  - [link\_entries\_dict](https://clear.ml/docs/latest/docs/references/sdk/dataset/#link_entries_dict)
  - [list\_added\_files](https://clear.ml/docs/latest/docs/references/sdk/dataset/#list_added_files)
  - [Dataset.list\_datasets](https://clear.ml/docs/latest/docs/references/sdk/dataset/#datasetlist_datasets)
  - [list\_files](https://clear.ml/docs/latest/docs/references/sdk/dataset/#list_files)
  - [list\_modified\_files](https://clear.ml/docs/latest/docs/references/sdk/dataset/#list_modified_files)
  - [list\_removed\_files](https://clear.ml/docs/latest/docs/references/sdk/dataset/#list_removed_files)
  - [Dataset.move\_to\_project](https://clear.ml/docs/latest/docs/references/sdk/dataset/#datasetmove_to_project)
  - [publish](https://clear.ml/docs/latest/docs/references/sdk/dataset/#publish)
  - [remove\_files](https://clear.ml/docs/latest/docs/references/sdk/dataset/#remove_files)
  - [Dataset.rename](https://clear.ml/docs/latest/docs/references/sdk/dataset/#datasetrename)
  - [set\_description](https://clear.ml/docs/latest/docs/references/sdk/dataset/#set_description)
  - [set\_metadata](https://clear.ml/docs/latest/docs/references/sdk/dataset/#set_metadata)
  - [Dataset.set\_offline](https://clear.ml/docs/latest/docs/references/sdk/dataset/#datasetset_offline)
  - [Dataset.squash](https://clear.ml/docs/latest/docs/references/sdk/dataset/#datasetsquash)
  - [sync\_folder](https://clear.ml/docs/latest/docs/references/sdk/dataset/#sync_folder)
  - [update\_changed\_files](https://clear.ml/docs/latest/docs/references/sdk/dataset/#update_changed_files)
  - [upload](https://clear.ml/docs/latest/docs/references/sdk/dataset/#upload)
  - [verify\_dataset\_hash](https://clear.ml/docs/latest/docs/references/sdk/dataset/#verify_dataset_hash)