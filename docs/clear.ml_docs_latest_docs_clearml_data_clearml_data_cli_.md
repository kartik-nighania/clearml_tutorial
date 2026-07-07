---
url: "https://clear.ml/docs/latest/docs/clearml_data/clearml_data_cli/"
title: "ClearML Data CLI | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/clearml_data/clearml_data_cli/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

important

This page covers `clearml-data`, ClearML's file-based data management solution.
See [Hyper-Datasets](https://clear.ml/docs/latest/docs/hyperdatasets/overview) for ClearML's advanced queryable dataset management solution.

`clearml-data` is a data management CLI tool that comes as part of the `clearml` Python package. Use `clearml-data` to
create, modify, and manage your datasets. You can upload your dataset to any storage service of your choice (S3 / GS /
Azure / Network Storage) by setting the dataset's upload destination (see [`--storage`](https://clear.ml/docs/latest/docs/clearml_data/clearml_data_cli/#upload)). Once you have uploaded
your dataset, you can access it from any machine.

The following page provides a reference to `clearml-data`'s CLI commands.

## create [​](https://clear.ml/docs/latest/docs/clearml_data/clearml_data_cli/\#create "Direct link to create")

Creates a new dataset.

```bash
clearml-data create [-h] [--parents [PARENTS [PARENTS ...]]] [--project PROJECT]

                    --name NAME [--version VERSION] [--storage STORAGE]

                    [--tags [TAGS [TAGS ...]]]
```

**Parameters**

| Name | Description | Mandatory |
| --- | --- | --- |
| `--name` | Dataset's name | ![Yes](https://clear.ml/docs/latest/icons/ico-optional-yes.svg) |
| `--project` | Dataset's project | ![Yes](https://clear.ml/docs/latest/icons/ico-optional-yes.svg) |
| `--version` | Dataset version. Use the [semantic versioning](https://semver.org/) scheme. If not specified a version will automatically be assigned | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--parents` | IDs of the dataset's parents. The dataset inherits all of its parents' content. Multiple parents can be entered, but they are merged in the order they were entered | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--storage` | Network storage target to upload the dataset files and associated information (Default: files\_server). <br> For example: <br>- A shared folder: `/mnt/share/folder`<br>- S3: `s3://bucket/folder`<br>- Non-AWS S3-like services (such as MinIO): `s3://host_addr:port/bucket`. **Note that port specification is required**. <br>- Google Cloud Storage: `gs://bucket-name/folder`<br>- Azure Storage: `azure://<account name>.blob.core.windows.net/path/to/file` | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--tags` | Dataset user tags. The dataset can be labeled, which can be useful for organizing datasets | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |

Dataset ID

- For datasets created with `clearml` v1.6 or newer on ClearML Server v1.6 or newer, find the ID in the dataset version's info panel in the [Dataset UI](https://clear.ml/docs/latest/docs/webapp/datasets/webapp_dataset_viewing).


For datasets created with earlier versions of `clearml`, or if using an earlier version of ClearML Server, find the ID in the task header of the [dataset task's info panel](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual).
- `clearml-data` works in a stateful mode so once a new dataset is created, the following commands
do not require the `--id` flag.

## add [​](https://clear.ml/docs/latest/docs/clearml_data/clearml_data_cli/\#add "Direct link to add")

Add individual files or complete folders to the dataset.

```bash
clearml-data add [-h] [--id ID] [--dataset-folder DATASET_FOLDER]

                 [--files [FILES [FILES ...]]] [--wildcard [WILDCARD [WILDCARD ...]]]

                 [--links [LINKS [LINKS ...]]] [--non-recursive] [--verbose]
```

**Parameters**

| Name | Description | Mandatory |
| --- | --- | --- |
| `--id` | Dataset's ID. Default: previously created / accessed dataset | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--files` | Files / folders to add. Items will be uploaded to the dataset's designated storage. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--wildcard` | Add specific set of files, denoted by these wildcards. For example: `~/data/*.jpg ~/data/json`. Multiple wildcards can be passed. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--links` | Files / folders link to add. Supports S3, GS, Azure links. Example: `s3://bucket/data``azure://<account name>.blob.core.windows.net/path/to/file`. Items remain in their original location. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--dataset-folder` | Dataset base folder to add the files to in the dataset. Default: dataset root. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--non-recursive` | Disable recursive scan of files | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--verbose` | Verbose reporting | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |

## remove [​](https://clear.ml/docs/latest/docs/clearml_data/clearml_data_cli/\#remove "Direct link to remove")

Remove files/links from the dataset.

```bash
clearml-data remove [-h] [--id ID] [--files [FILES [FILES ...]]]

                    [--non-recursive] [--verbose]
```

**Parameters**

| Name | Description | Mandatory |
| --- | --- | --- |
| `--id` | Dataset's ID. Default: previously created / accessed dataset | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--files` | Files / folders to remove (wildcard selection is supported, for example: `~/data/*.jpg ~/data/json`). Notice: file path is the path within the dataset, not the local path. For links, you can specify their URL (for example, `s3://bucket/data`) | ![Yes](https://clear.ml/docs/latest/icons/ico-optional-yes.svg) |
| `--non-recursive` | Disable recursive scan of files | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--verbose` | Verbose reporting | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |

## upload [​](https://clear.ml/docs/latest/docs/clearml_data/clearml_data_cli/\#upload "Direct link to upload")

Upload the local dataset changes to the server. By default, it's uploaded to the ClearML file server. You can specify a different storage
medium by entering an upload destination. For example:

- A shared folder: `/mnt/shared/folder`
- S3: `s3://bucket/folder`
- Non-AWS S3-like services (such as MinIO): `s3://host_addr:port/bucket`. **Note that port specification is required**.
- Google Cloud Storage: `gs://bucket-name/folder`
- Azure Storage: `azure://<account name>.blob.core.windows.net/path/to/file`

```bash
clearml-data upload [-h] [--id ID] [--storage STORAGE] [--chunk-size CHUNK_SIZE]

                    [--verbose]
```

**Parameters**

| Name | Description | Mandatory |
| --- | --- | --- |
| `--id` | Dataset's ID. Default: previously created / accessed dataset | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--storage` | Remote storage to use for the dataset files. Default: files\_server | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--chunk-size` | Set dataset artifact upload chunk size in MB. Default 512, (pass -1 for a single chunk). Example: 512, dataset will be split and uploaded in 512 MB chunks. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--verbose` | Verbose reporting | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |

## close [​](https://clear.ml/docs/latest/docs/clearml_data/clearml_data_cli/\#close "Direct link to close")

Finalize the dataset and make it ready to be consumed. This automatically uploads all files that were not previously uploaded.
Once a dataset is finalized, it can no longer be modified.

```bash
clearml-data close [-h] [--id ID] [--storage STORAGE] [--disable-upload]

                   [--chunk-size CHUNK_SIZE] [--verbose]
```

**Parameters**

| Name | Description | Mandatory |
| --- | --- | --- |
| `--id` | Dataset's ID. Default: previously created / accessed dataset | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--storage` | Network storage target to upload the dataset files and associated information (Default: files\_server). <br> For example: <br>- A shared folder: `/mnt/share/folder`<br>- S3: `s3://bucket/folder`<br>- Non-AWS S3-like services (such as MinIO): `s3://host_addr:port/bucket`. **Note that port specification is required**. <br>- Google Cloud Storage: `gs://bucket-name/folder`<br>- Azure Storage: `azure://<account name>.blob.core.windows.net/path/to/file` | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--disable-upload` | Disable automatic upload when closing the dataset | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--chunk-size` | Set dataset artifact upload chunk size in MB. Default 512, (pass -1 for a single chunk). Example: 512, dataset will be split and uploaded in 512 MB chunks. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--verbose` | Verbose reporting | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |

## sync [​](https://clear.ml/docs/latest/docs/clearml_data/clearml_data_cli/\#sync "Direct link to sync")

Sync a folder's content with ClearML. This option is useful in case a user has a single point of truth (i.e. a folder) which
updates from time to time.

Once an update should be reflected in ClearML's system, call `clearml-data sync` and pass the folder path,
and the changes (either file addition, modification and removal) will be reflected in ClearML.

This command also uploads the data and finalizes the dataset automatically.

```bash
clearml-data sync [-h] [--id ID] [--dataset-folder DATASET_FOLDER] --folder FOLDER

                  [--parents [PARENTS [PARENTS ...]]] [--project PROJECT] [--name NAME]

                  [--version VERSION] [--storage STORAGE] [--tags [TAGS [TAGS ...]]]

                  [--storage STORAGE] [--skip-close] [--chunk-size CHUNK_SIZE] [--verbose]
```

**Parameters**

| Name | Description | Mandatory |
| --- | --- | --- |
| `--id` | Dataset's ID. Default: previously created / accessed dataset | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--dataset-folder` | Dataset base folder to add the files to (default: Dataset root) | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--folder` | Local folder to sync. Wildcard selection is supported, for example: `~/data/*.jpg ~/data/json` | ![Yes](https://clear.ml/docs/latest/icons/ico-optional-yes.svg) |
| `--storage` | Network storage target to upload the dataset files and associated information (Default: files\_server). <br> For example: <br>- A shared folder: `/mnt/share/folder`<br>- S3: `s3://bucket/folder`<br>- Non-AWS S3-like services (such as MinIO): `s3://host_addr:port/bucket`. **Note that port specification is required**. <br>- Google Cloud Storage: `gs://bucket-name/folder`<br>- Azure Storage: `azure://<account name>.blob.core.windows.net/path/to/file` | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--parents` | IDs of the dataset's parents (i.e. merge all parents). All modifications made to the folder since the parents were synced will be reflected in the dataset | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--project` | If creating a new dataset, specify the dataset's project name | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--name` | If creating a new dataset, specify the dataset's name | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--version` | Specify the dataset's version using the [semantic versioning](https://semver.org/) scheme. Default: `1.0.0` | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--tags` | Dataset user tags | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--skip-close` | Do not auto close dataset after syncing folders | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--chunk-size` | Set dataset artifact upload chunk size in MB. Default 512, (pass -1 for a single chunk). Example: 512, dataset will be split and uploaded in 512 MB chunks. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--verbose` | Verbose reporting | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |

## list [​](https://clear.ml/docs/latest/docs/clearml_data/clearml_data_cli/\#list "Direct link to list")

List a dataset's contents.

```bash
clearml-data list [-h] [--id ID] [--project PROJECT] [--name NAME] [--version VERSION]

                  [--filter [FILTER [FILTER ...]]] [--modified]
```

**Parameters**

| Name | Description | Mandatory |
| --- | --- | --- |
| `--id` | Dataset ID whose contents will be shown (alternatively, use project / name combination). Default: previously accessed dataset | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--project` | Specify dataset project name (if used instead of ID, dataset name is also required) | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--name` | Specify dataset name (if used instead of ID, dataset project is also required) | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--version` | Specify dataset version. Default: most recent version | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--filter` | Filter files based on folder / wildcard. Multiple filters are supported. Example: `folder/date_*.json folder/subfolder` | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--modified` | Only list file changes (add / remove / modify) introduced in this version | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |

## set-description [​](https://clear.ml/docs/latest/docs/clearml_data/clearml_data_cli/\#set-description "Direct link to set-description")

Sets the description of an existing dataset.

```bash
clearml-data set-description [-h] [--id ID] [--description DESCRIPTION]
```

**Parameters**

| Name | Description | Mandatory |
| --- | --- | --- |
| `--id` | Dataset's ID | ![Yes](https://clear.ml/docs/latest/icons/ico-optional-yes.svg) |
| `--description` | Description to be set | ![Yes](https://clear.ml/docs/latest/icons/ico-optional-yes.svg) |

## delete [​](https://clear.ml/docs/latest/docs/clearml_data/clearml_data_cli/\#delete "Direct link to delete")

Deletes dataset(s). Pass any of the attributes of the dataset(s) you want to delete. Multiple datasets matching the
request will raise an exception, unless you pass `--entire-dataset` and `--force`. In this case, all matching datasets
will be deleted.

If a dataset is a parent to a dataset(s), you must pass `--force` to delete it.

warning

Deleting a parent dataset may cause child datasets to lose data!

```bash
clearml-data delete [-h] [--id ID] [--project PROJECT] [--name NAME]

                    [--version VERSION] [--force] [--entire-dataset]
```

**Parameters**

| Name | Description | Mandatory |
| --- | --- | --- |
| `--id` | ID of the dataset to delete (alternatively, use project / name combination). | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--project` | Specify dataset project name (if used instead of ID, dataset name is also required) | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--name` | Specify dataset name (if used instead of ID, dataset project is also required) | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--version` | Specify dataset version | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `-–force` | Force dataset deletion even if other dataset versions depend on it. Must also be used if `--entire-dataset` flag is used | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--entire-dataset` | Delete all found datasets | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |

## rename [​](https://clear.ml/docs/latest/docs/clearml_data/clearml_data_cli/\#rename "Direct link to rename")

Rename a dataset (and all of its versions).

```bash
clearml-data rename [-h] --new-name NEW_NAME --project PROJECT --name NAME
```

**Parameters**

| Name | Description | Mandatory |
| --- | --- | --- |
| `--new-name` | The new name of the dataset | ![Yes](https://clear.ml/docs/latest/icons/ico-optional-yes.svg) |
| `--project` | The project the dataset to be renamed belongs to | ![Yes](https://clear.ml/docs/latest/icons/ico-optional-yes.svg) |
| `--name` | The current name of the dataset(s) to be renamed | ![Yes](https://clear.ml/docs/latest/icons/ico-optional-yes.svg) |

## move [​](https://clear.ml/docs/latest/docs/clearml_data/clearml_data_cli/\#move "Direct link to move")

Moves a dataset to another project

```bash
clearml-data move [-h] --new-project NEW_PROJECT --project PROJECT --name NAME
```

**Parameters**

| Name | Description | Mandatory |
| --- | --- | --- |
| `--new-project` | The new project of the dataset | ![Yes](https://clear.ml/docs/latest/icons/ico-optional-yes.svg) |
| `--project` | The current project the dataset to be move belongs to | ![Yes](https://clear.ml/docs/latest/icons/ico-optional-yes.svg) |
| `--name` | The name of the dataset to be moved | ![Yes](https://clear.ml/docs/latest/icons/ico-optional-yes.svg) |

## search [​](https://clear.ml/docs/latest/docs/clearml_data/clearml_data_cli/\#search "Direct link to search")

Search datasets in the system by project, name, ID, and/or tags.

Returns list of all datasets in the system that match the search request, sorted by creation time.

```bash
clearml-data search [-h] [--ids [IDS [IDS ...]]] [--project PROJECT]

                    [--name NAME] [--tags [TAGS [TAGS ...]]]
```

**Parameters**

| Name | Description | Mandatory |
| --- | --- | --- |
| `--ids` | A list of dataset IDs | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--project` | The project name of the datasets | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--name` | A dataset name or a partial name to filter datasets by | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--tags` | A list of dataset user tags | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |

## compare [​](https://clear.ml/docs/latest/docs/clearml_data/clearml_data_cli/\#compare "Direct link to compare")

Compare two datasets (target vs. source). The command returns a comparison summary that looks like this:
`Comparison summary: 4 files removed, 3 files modified, 0 files added`

```bash
clearml-data compare [-h] --source SOURCE --target TARGET [--verbose]
```

**Parameters**

| Name | Description | Mandatory |
| --- | --- | --- |
| `--source` | Source dataset ID (used as baseline) | ![Yes](https://clear.ml/docs/latest/icons/ico-optional-yes.svg) |
| `--target` | Target dataset ID (compare against the source baseline dataset) | ![Yes](https://clear.ml/docs/latest/icons/ico-optional-yes.svg) |
| `--verbose` | Verbose report all file changes (instead of summary) | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |

## squash [​](https://clear.ml/docs/latest/docs/clearml_data/clearml_data_cli/\#squash "Direct link to squash")

Squash multiple datasets into a single dataset version (merge down).

```bash
clearml-data squash [-h] --name NAME --ids [IDS [IDS ...]] [--storage STORAGE] [--verbose]
```

**Parameters**

| Name | Description | Mandatory |
| --- | --- | --- |
| `--name` | Squashed dataset name | ![Yes](https://clear.ml/docs/latest/icons/ico-optional-yes.svg) |
| `--ids` | Source dataset IDs to squash (merge down) | ![Yes](https://clear.ml/docs/latest/icons/ico-optional-yes.svg) |
| `--storage` | Network storage target to upload the dataset files and associated information (Default: files\_server). <br> For example: <br>- A shared folder: `/mnt/share/folder`<br>- S3: `s3://bucket/folder`<br>- Non-AWS S3-like services (such as MinIO): `s3://host_addr:port/bucket`. **Note that port specification is required**. <br>- Google Cloud Storage: `gs://bucket-name/folder`<br>- Azure Storage: `azure://<account name>.blob.core.windows.net/path/to/file` | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--verbose` | Verbose report all file changes (instead of summary) | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |

## verify [​](https://clear.ml/docs/latest/docs/clearml_data/clearml_data_cli/\#verify "Direct link to verify")

Verify that the dataset content matches the data from the local source.

```bash
clearml-data verify [-h] [--id ID] [--folder FOLDER] [--filesize] [--verbose]
```

**Parameters**

| Name | Description | Mandatory |
| --- | --- | --- |
| `--id` | Specify dataset ID. Default: previously created/accessed dataset | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--folder` | Specify dataset local copy (if not provided the local cache folder will be verified) | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--filesize` | If `True`, only verify file size and skip hash checks (default: `False`) | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--verbose` | Verbose report all file changes (instead of summary) | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |

## get [​](https://clear.ml/docs/latest/docs/clearml_data/clearml_data_cli/\#get "Direct link to get")

Get a local copy of a dataset. By default, you get a read only cached folder, but you can get a mutable copy by using the
`--copy` flag.

```bash
clearml-data get [-h] [--id ID] [--copy COPY] [--link LINK] [--part PART]

                 [--num-parts NUM_PARTS] [--overwrite] [--verbose]
```

**Parameters**

| Name | Description | Mandatory |
| --- | --- | --- |
| `--id` | Specify dataset ID. Default: previously created / accessed dataset | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--copy` | Get a writable copy of the dataset to a specific output folder | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--link` | Create a soft link (not supported on Windows) to a read-only cached folder containing the dataset | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--part` | Retrieve a partial copy of the dataset. Part number (0 to `--num-parts`-1) of total parts `--num-parts`. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--num-parts` | Total number of parts to divide the dataset into. Notice, minimum retrieved part is a single chunk in a dataset (or its parents). Example: Dataset gen4, with 3 parents, each with a single chunk, can be divided into 4 parts | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--overwrite` | If `True`, overwrite the target folder | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--verbose` | Verbose report all file changes (instead of summary) | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |

## publish [​](https://clear.ml/docs/latest/docs/clearml_data/clearml_data_cli/\#publish "Direct link to publish")

Publish the dataset for public use. The dataset must be [finalized](https://clear.ml/docs/latest/docs/clearml_data/clearml_data_cli/#close) before it is published.

```bash
clearml-data publish [-h] --id ID
```

**Parameters**

| Name | Description | Mandatory |
| --- | --- | --- |
| `--id` | The dataset task ID to be published. | ![Yes](https://clear.ml/docs/latest/icons/ico-optional-yes.svg) |

- [create](https://clear.ml/docs/latest/docs/clearml_data/clearml_data_cli/#create)
- [add](https://clear.ml/docs/latest/docs/clearml_data/clearml_data_cli/#add)
- [remove](https://clear.ml/docs/latest/docs/clearml_data/clearml_data_cli/#remove)
- [upload](https://clear.ml/docs/latest/docs/clearml_data/clearml_data_cli/#upload)
- [close](https://clear.ml/docs/latest/docs/clearml_data/clearml_data_cli/#close)
- [sync](https://clear.ml/docs/latest/docs/clearml_data/clearml_data_cli/#sync)
- [list](https://clear.ml/docs/latest/docs/clearml_data/clearml_data_cli/#list)
- [set-description](https://clear.ml/docs/latest/docs/clearml_data/clearml_data_cli/#set-description)
- [delete](https://clear.ml/docs/latest/docs/clearml_data/clearml_data_cli/#delete)
- [rename](https://clear.ml/docs/latest/docs/clearml_data/clearml_data_cli/#rename)
- [move](https://clear.ml/docs/latest/docs/clearml_data/clearml_data_cli/#move)
- [search](https://clear.ml/docs/latest/docs/clearml_data/clearml_data_cli/#search)
- [compare](https://clear.ml/docs/latest/docs/clearml_data/clearml_data_cli/#compare)
- [squash](https://clear.ml/docs/latest/docs/clearml_data/clearml_data_cli/#squash)
- [verify](https://clear.ml/docs/latest/docs/clearml_data/clearml_data_cli/#verify)
- [get](https://clear.ml/docs/latest/docs/clearml_data/clearml_data_cli/#get)
- [publish](https://clear.ml/docs/latest/docs/clearml_data/clearml_data_cli/#publish)