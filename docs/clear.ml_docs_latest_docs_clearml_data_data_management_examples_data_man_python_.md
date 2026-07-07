---
url: "https://clear.ml/docs/latest/docs/clearml_data/data_management_examples/data_man_python/"
title: "Data Management with Python | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/clearml_data/data_management_examples/data_man_python/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The [dataset\_creation.py](https://github.com/clearml/clearml/blob/master/examples/datasets/dataset_creation.py) and
[data\_ingestion.py](https://github.com/clearml/clearml/blob/master/examples/datasets/data_ingestion.py) scripts
together demonstrate how to use ClearML's [`Dataset`](https://clear.ml/docs/latest/docs/references/sdk/dataset) class to create a dataset and
subsequently ingest the data.

## Dataset Creation [​](https://clear.ml/docs/latest/docs/clearml_data/data_management_examples/data_man_python/\#dataset-creation "Direct link to Dataset Creation")

The [dataset\_creation.py](https://github.com/clearml/clearml/blob/master/examples/datasets/dataset_creation.py) script
demonstrates how to do the following:

- Create a dataset and add files to it
- Upload the dataset to the ClearML Server
- Finalize the dataset

### Downloading the Data [​](https://clear.ml/docs/latest/docs/clearml_data/data_management_examples/data_man_python/\#downloading-the-data "Direct link to Downloading the Data")

You first need to obtain a local copy of the CIFAR dataset.
The code below downloads the data and `dataset_path` contains the path to the downloaded data:

```python
from clearml import StorageManager

manager = StorageManager()

dataset_path = manager.get_local_copy(

    remote_url="https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz"

)
```

### Creating the Dataset [​](https://clear.ml/docs/latest/docs/clearml_data/data_management_examples/data_man_python/\#creating-the-dataset "Direct link to Creating the Dataset")

The following code creates a data processing task called `cifar_dataset` in the `dataset examples` project, which
can be viewed in the [WebApp](https://clear.ml/docs/latest/docs/webapp/datasets/webapp_dataset_viewing).

```python
from clearml import Dataset

dataset = Dataset.create(

    dataset_name="cifar_dataset",

    dataset_project="dataset examples"

)
```

### Adding Files [​](https://clear.ml/docs/latest/docs/clearml_data/data_management_examples/data_man_python/\#adding-files "Direct link to Adding Files")

Add the downloaded files to the current dataset:

```python
dataset.add_files(path=dataset_path)
```

### Uploading the Files [​](https://clear.ml/docs/latest/docs/clearml_data/data_management_examples/data_man_python/\#uploading-the-files "Direct link to Uploading the Files")

Upload the dataset:

```python
dataset.upload()
```

By default, the dataset is uploaded to the ClearML file server. The dataset's destination can be changed by specifying the
target storage with the `output_url` parameter of the [`upload`](https://clear.ml/docs/latest/docs/references/sdk/dataset#upload) method.

### Finalizing the Dataset [​](https://clear.ml/docs/latest/docs/clearml_data/data_management_examples/data_man_python/\#finalizing-the-dataset "Direct link to Finalizing the Dataset")

Run the [`finalize`](https://clear.ml/docs/latest/docs/references/sdk/dataset#finalize) command to close the dataset and set that dataset's tasks
status to _completed_. The dataset can only be finalized if it doesn't have any pending uploads.

```python
dataset.finalize()
```

After a dataset has been closed, it can no longer be modified. This ensures future reproducibility.

Information about the dataset can be viewed in the WebApp, in the dataset's [details panel](https://clear.ml/docs/latest/docs/webapp/datasets/webapp_dataset_viewing#version-details-panel).
In the panel's **CONTENT** tab, you can see a table summarizing version contents, including file names, file sizes, and hashes.

![Dataset content tab](https://clear.ml/docs/latest/assets/images/examples_data_management_cifar_dataset-2b8f50c4abb43df312e54af5c5d28faf.png#light-mode-only)![Dataset content tab](https://clear.ml/docs/latest/assets/images/examples_data_management_cifar_dataset_dark-3a0e31c16cc2f66cb63aa4fd656d6b58.png#dark-mode-only)

## Data Ingestion [​](https://clear.ml/docs/latest/docs/clearml_data/data_management_examples/data_man_python/\#data-ingestion "Direct link to Data Ingestion")

Now that a new dataset is registered, you can consume it!

The [data\_ingestion.py](https://github.com/clearml/clearml/blob/master/examples/datasets/data_ingestion.py) script
demonstrates data ingestion using the dataset created in the first script.

The following script gets the dataset and uses [`Dataset.get_local_copy()`](https://clear.ml/docs/latest/docs/references/sdk/dataset#get_local_copy)
to return a path to the cached, read-only local dataset.

```python
dataset_name = "cifar_dataset"

dataset_project = "dataset_examples"

dataset_path = Dataset.get(

    dataset_name=dataset_name,

    dataset_project=dataset_project

).get_local_copy()
```

If you need a modifiable copy of the dataset, use the following code:

```python
Dataset.get(dataset_name, dataset_project).get_mutable_local_copy("path/to/download")
```

The script then creates a neural network to train a model to classify images from the dataset that was
created above.

- [Dataset Creation](https://clear.ml/docs/latest/docs/clearml_data/data_management_examples/data_man_python/#dataset-creation)
  - [Downloading the Data](https://clear.ml/docs/latest/docs/clearml_data/data_management_examples/data_man_python/#downloading-the-data)
  - [Creating the Dataset](https://clear.ml/docs/latest/docs/clearml_data/data_management_examples/data_man_python/#creating-the-dataset)
  - [Adding Files](https://clear.ml/docs/latest/docs/clearml_data/data_management_examples/data_man_python/#adding-files)
  - [Uploading the Files](https://clear.ml/docs/latest/docs/clearml_data/data_management_examples/data_man_python/#uploading-the-files)
  - [Finalizing the Dataset](https://clear.ml/docs/latest/docs/clearml_data/data_management_examples/data_man_python/#finalizing-the-dataset)
- [Data Ingestion](https://clear.ml/docs/latest/docs/clearml_data/data_management_examples/data_man_python/#data-ingestion)