---
url: "https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/table/download_and_preprocessing/"
title: "Tabular Data Downloading and Preprocessing - Jupyter Notebook | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/table/download_and_preprocessing/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The [download\_and\_preprocessing.ipynb](https://github.com/clearml/clearml/blob/master/examples/frameworks/pytorch/notebooks/table/download_and_preprocessing.ipynb) example demonstrates ClearML storing preprocessed tabular data as artifacts, and explicitly reporting the tabular data in the **ClearML Web UI**. When the script runs, it creates a task named `tabular preprocessing` in the `Table Example` project.

This tabular data is prepared for another script, [train\_tabular\_predictor.ipynb](https://github.com/clearml/clearml/blob/master/examples/frameworks/pytorch/notebooks/table/train_tabular_predictor.ipynb), which trains a network with it.

## Artifacts [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/table/download_and_preprocessing/\#artifacts "Direct link to Artifacts")

The example code preprocesses the downloaded data using Pandas DataFrames, and stores it as three artifacts:

- `Categories per column` \- Number of unique values per column of data.
- `Outcome dictionary` \- Label enumeration for training.
- `Processed data` \- A dictionary containing the paths of the training and validation data.

Each artifact is uploaded by calling [`Task.upload_artifact()`](https://clear.ml/docs/latest/docs/references/sdk/task#upload_artifact).
Artifacts appear in the **ARTIFACTS** tab.

![image](https://clear.ml/docs/latest/assets/images/download_and_preprocessing_02-4b20bf0c7849b0f7f696413b36294b51.png)

## Plots (tables) [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/table/download_and_preprocessing/\#plots-tables "Direct link to Plots (tables)")

The example code explicitly reports the data in Pandas DataFrames by calling [`Logger.report_table()`](https://clear.ml/docs/latest/docs/references/sdk/logger#report_table).

For example, the raw data is read into a Pandas DataFrame named `train_set`, and the `head` of the DataFrame is reported.

```python
train_set = pd.read_csv(Path(path_to_ShelterAnimal) / 'train.csv')

Logger.current_logger().report_table(

    title='ClearMLet - raw', series='pandas DataFrame', iteration=0, table_plot=train_set.head()

)
```

The tables appear in **PLOTS**.

![image](https://clear.ml/docs/latest/assets/images/download_and_preprocessing_07-b286ddfb06d4f8373267a64e0f92e25f.png)

## Hyperparameters [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/table/download_and_preprocessing/\#hyperparameters "Direct link to Hyperparameters")

A parameter dictionary is logged by connecting it to the Task using [`Task.connect()`](https://clear.ml/docs/latest/docs/references/sdk/task#connect).

```python
logger = task.get_logger()

configuration_dict = {'test_size': 0.1, 'split_random_state': 0}

configuration_dict = task.connect(configuration_dict)
```

Parameter dictionaries appear in the **General** subsection.

![image](https://clear.ml/docs/latest/assets/images/download_and_preprocessing_01-deff1c87063976dee4f612f4c5822990.png)

## Console [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/table/download_and_preprocessing/\#console "Direct link to Console")

Output to the console appears in **CONSOLE**.

![image](https://clear.ml/docs/latest/assets/images/download_and_preprocessing_06-04e2e9b7b77e869ef08c44e107df500d.png)

- [Artifacts](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/table/download_and_preprocessing/#artifacts)
- [Plots (tables)](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/table/download_and_preprocessing/#plots-tables)
- [Hyperparameters](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/table/download_and_preprocessing/#hyperparameters)
- [Console](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/table/download_and_preprocessing/#console)