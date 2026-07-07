---
url: "https://clear.ml/docs/latest/docs/guides/reporting/artifacts/"
title: "Artifacts Reporting | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/reporting/artifacts/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The [artifacts.py](https://github.com/clearml/clearml/blob/master/examples/reporting/artifacts.py) example demonstrates
uploading objects (other than models) to storage as task artifacts.

These artifacts include:

- Pandas DataFrames
- Local files, dictionaries
- Folders
- Numpy objects
- Image files

Artifacts can be uploaded and dynamically tracked, or uploaded without tracking.

Configure ClearML for uploading artifacts to any of the supported types of storage, which include local and shared folders,
S3 buckets, Google Cloud Storage, and Azure Storage ( [debug sample storage](https://clear.ml/docs/latest/docs/references/sdk/logger#set_default_upload_destination)
is different). Configure ClearML in any of the following ways:

- In the configuration file, set [`default_output_uri`](https://clear.ml/docs/latest/docs/configs/clearml_conf#config_default_output_uri).
- In code, when [initializing a task](https://clear.ml/docs/latest/docs/references/sdk/task#taskinit), use the `output_uri` parameter.
- In the **ClearML Web UI**, when [modifying a task](https://clear.ml/docs/latest/docs/webapp/webapp_exp_tuning#output-destination).

When the script runs, it creates a task named `artifacts example` in the `examples` project.

ClearML reports artifacts in the **ClearML Web UI** **>** task details **>** **ARTIFACTS** tab.

![Task artifacts](https://clear.ml/docs/latest/assets/images/examples_reporting_03-2b730664309e3fad5742c8aee7c5ef41.png#light-mode-only)![Task artifacts](https://clear.ml/docs/latest/assets/images/examples_reporting_03_dark-efdfd0b92d67b5ea787ae159a46eecd5.png#dark-mode-only)

## Dynamically Tracked Artifacts [​](https://clear.ml/docs/latest/docs/guides/reporting/artifacts/\#dynamically-tracked-artifacts "Direct link to Dynamically Tracked Artifacts")

ClearML supports uploading and dynamically tracking Pandas DataFrames. Use [`Task.register_artifact()`](https://clear.ml/docs/latest/docs/references/sdk/task#register_artifact)
to add a DataFrame to a task. If the DataFrame is modified, ClearML will automatically update the changes.

For example:

```python
df = pd.DataFrame(

    {

        'num_legs': [2, 4, 8, 0],

        'num_wings': [2, 0, 0, 0],

        'num_specimen_seen': [10, 2, 1, 8]

    },

    index=['falcon', 'dog', 'spider', 'fish']

)

# Register Pandas object as artifact to watch

# (it will be monitored in the background and automatically synced and uploaded)

task.register_artifact(

    name='train',

    artifact=df,

    metadata={'counting': 'legs', 'max legs': 68}

)
```

By modifying the artifact, and calling [`Task.get_registered_artifacts()`](https://clear.ml/docs/latest/docs/references/sdk/task#get_registered_artifacts)
to retrieve it, you can see ClearML tracking the changes:

```python
# change the artifact object

df.sample(frac=0.5, replace=True, random_state=1)

# or access it from anywhere using the Task's get_registered_artifacts()

Task.current_task().get_registered_artifacts()['train'].sample(frac=0.5, replace=True, random_state=1)
```

## Artifacts Without Tracking [​](https://clear.ml/docs/latest/docs/guides/reporting/artifacts/\#artifacts-without-tracking "Direct link to Artifacts Without Tracking")

ClearML supports several types of objects that can be uploaded and are not tracked. Use the [Task.upload\_artifact](https://clear.ml/docs/latest/docs/references/sdk/task#upload_artifact)
method.

Artifacts without tracking include:

- Pandas DataFrames
- Local files
- Dictionaries (stored as a JSONs)
- Numpy objects (stored as NPZ files)
- Image files (stored as PNG files)
- Folders (stored as a ZIP files)
- Wildcards (stored as a ZIP files)

### Pandas DataFrames [​](https://clear.ml/docs/latest/docs/guides/reporting/artifacts/\#pandas-dataframes "Direct link to Pandas DataFrames")

```python
# add and upload pandas.DataFrame (onetime snapshot of the object)

task.upload_artifact(name='Pandas', artifact_object=df)
```

### Local Files [​](https://clear.ml/docs/latest/docs/guides/reporting/artifacts/\#local-files "Direct link to Local Files")

```python
# add and upload local file artifact

task.upload_artifact(

    name='local file',

    artifact_object=os.path.join(

        'data_samples',

        'dancing.jpg'

    )

)
```

### Dictionaries [​](https://clear.ml/docs/latest/docs/guides/reporting/artifacts/\#dictionaries "Direct link to Dictionaries")

```python
# add and upload dictionary stored as JSON

task.upload_artifact(name='dictionary', artifact_object=df.to_dict())
```

### Numpy Objects [​](https://clear.ml/docs/latest/docs/guides/reporting/artifacts/\#numpy-objects "Direct link to Numpy Objects")

```python
# add and upload Numpy Object (stored as .npz file)

task.upload_artifact(name='Numpy Eye', artifact_object=np.eye(100, 100))
```

### Image Files [​](https://clear.ml/docs/latest/docs/guides/reporting/artifacts/\#image-files "Direct link to Image Files")

```python
# add and upload Image (stored as .png file)

im = Image.open(os.path.join('data_samples', 'dancing.jpg'))

task.upload_artifact(name='pillow_image', artifact_object=im)
```

### Folders [​](https://clear.ml/docs/latest/docs/guides/reporting/artifacts/\#folders "Direct link to Folders")

```python
# add and upload a folder, artifact_object should be the folder path

task.upload_artifact(name='local folder', artifact_object=os.path.join('data_samples'))
```

### Wildcards [​](https://clear.ml/docs/latest/docs/guides/reporting/artifacts/\#wildcards "Direct link to Wildcards")

```python
# add and upload a wildcard

task.upload_artifact(name='wildcard jpegs', artifact_object=os.path.join('data_samples', '*.jpg'))
```

- [Dynamically Tracked Artifacts](https://clear.ml/docs/latest/docs/guides/reporting/artifacts/#dynamically-tracked-artifacts)
- [Artifacts Without Tracking](https://clear.ml/docs/latest/docs/guides/reporting/artifacts/#artifacts-without-tracking)
  - [Pandas DataFrames](https://clear.ml/docs/latest/docs/guides/reporting/artifacts/#pandas-dataframes)
  - [Local Files](https://clear.ml/docs/latest/docs/guides/reporting/artifacts/#local-files)
  - [Dictionaries](https://clear.ml/docs/latest/docs/guides/reporting/artifacts/#dictionaries)
  - [Numpy Objects](https://clear.ml/docs/latest/docs/guides/reporting/artifacts/#numpy-objects)
  - [Image Files](https://clear.ml/docs/latest/docs/guides/reporting/artifacts/#image-files)
  - [Folders](https://clear.ml/docs/latest/docs/guides/reporting/artifacts/#folders)
  - [Wildcards](https://clear.ml/docs/latest/docs/guides/reporting/artifacts/#wildcards)