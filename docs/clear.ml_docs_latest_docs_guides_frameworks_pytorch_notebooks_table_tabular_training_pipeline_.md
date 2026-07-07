---
url: "https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/table/tabular_training_pipeline/"
title: "Tabular Data Pipeline with Concurrent Steps - Jupyter Notebook | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/table/tabular_training_pipeline/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

This example demonstrates an ML pipeline which preprocesses data in two concurrent steps, trains two networks, where each
network's training depends upon the completion of its own preprocessed data, and picks the best model. It is implemented
using the [PipelineController](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller)
class.

The pipeline uses four Tasks (each Task is created using a different notebook):

- The pipeline controller Task ( [tabular\_ml\_pipeline.ipynb](https://github.com/clearml/clearml/blob/master/examples/frameworks/pytorch/notebooks/table/tabular_ml_pipeline.ipynb))
- A data preprocessing Task ( [preprocessing\_and\_encoding.ipynb](https://github.com/clearml/clearml/blob/master/examples/frameworks/pytorch/notebooks/table/preprocessing_and_encoding.ipynb))
- A training Task ( [train\_tabular\_predictor.ipynb](https://github.com/clearml/clearml/blob/master/examples/frameworks/pytorch/notebooks/table/train_tabular_predictor.ipynb))
- A better model comparison Task ( [pick\_best\_model.ipynb](https://github.com/clearml/clearml/blob/master/examples/frameworks/pytorch/notebooks/table/pick_best_model.ipynb))

The `PipelineController` class includes functionality to create a pipeline controller, add steps to the pipeline, pass data from one step to another, control the dependencies of a step beginning only after other steps complete, run the pipeline, wait for it to complete, and cleanup afterwards.

In this pipeline example, the data preprocessing Task and training Task are each added to the pipeline twice (each is in two steps). When the pipeline runs, the data preprocessing Task and training Task are cloned twice, and the newly cloned Tasks execute. The Task they are cloned from, called the base Task, does not execute. The pipeline controller passes different data to each cloned Task by overriding parameters. In this way, the same Task can run more than once in the pipeline, but with different data.

Download Data

The data download Task is not a step in the pipeline, see [download\_and\_split](https://github.com/clearml/clearml/blob/master/examples/frameworks/pytorch/notebooks/table/download_and_split.ipynb).

## Pipeline Controller and Steps [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/table/tabular_training_pipeline/\#pipeline-controller-and-steps "Direct link to Pipeline Controller and Steps")

In this example, a pipeline controller object is created.

```python
pipe = PipelineController(

    project="Tabular Example",

    name="tabular training pipeline",

    add_pipeline_tags=True,

    version="0.1"

)
```

### Preprocessing Step [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/table/tabular_training_pipeline/\#preprocessing-step "Direct link to Preprocessing Step")

Two preprocessing nodes are added to the pipeline. These steps will run concurrently.

```python
pipe.add_step(

   name='preprocessing_1',

   base_task_project='Tabular Example',

   base_task_name='tabular preprocessing',

   parameter_override={

      'General/data_task_id': TABULAR_DATASET_ID,

      'General/fill_categorical_NA': 'True',

      'General/fill_numerical_NA': 'True'

   }

)

pipe.add_step(

   name='preprocessing_2',

   base_task_project='Tabular Example',

   base_task_name='tabular preprocessing',

   parameter_override={

      'General/data_task_id': TABULAR_DATASET_ID,

      'General/fill_categorical_NA': 'False',

      'General/fill_numerical_NA': 'True'

   }

)
```

The preprocessing data Task fills in values of `NaN` data based on the values of the parameters named `fill_categorical_NA`
and `fill_numerical_NA`. It will connect a parameter dictionary to the Task which contains keys with those same names.
The pipeline will override the values of those keys when the pipeline executes the cloned Tasks of the base Task. In this way,
two sets of data are created in the pipeline.

ClearML tracks and reports the preprocessing step

In the preprocessing data Task, the parameter values in `data_task_id`, `fill_categorical_NA`, and `fill_numerical_NA` are overridden.

```python
configuration_dict = {

   'data_task_id': TABULAR_DATASET_ID,

   'fill_categorical_NA': True,

   'fill_numerical_NA': True

}

configuration_dict = task.connect(configuration_dict)  # enabling configuration override by clearml
```

ClearML tracks and reports each instance of the preprocessing Task.

The raw data appears as a table in **PLOTS**.

These images are from one of the two preprocessing Tasks.

![image](https://clear.ml/docs/latest/assets/images/preprocessing_and_encoding_02-d958e78316e5f611403e0b03cad14dfe.png)

The data after filling NA values is also reported.

![image](https://clear.ml/docs/latest/assets/images/preprocessing_and_encoding_03-c7562886642a1cbcd78372c56909b002.png)

After an outcome dictionary (label enumeration) is created, it appears in **ARTIFACTS** **>** **OTHER** **>** **Outcome Dictionary**.

![image](https://clear.ml/docs/latest/assets/images/preprocessing_and_encoding_04-d9d840e73e71aadf537176860977a723.png)

The training and validation data is labeled with the encoding and reported as table.

![image](https://clear.ml/docs/latest/assets/images/preprocessing_and_encoding_05-f01fd0b8e4432c8a505ebf90cea82b94.png)

The column categories are created and uploaded as artifacts, which appear in appears in **ARTIFACTS** **>** **OTHER** **>** **Outcome Dictionary**.

![image](https://clear.ml/docs/latest/assets/images/preprocessing_and_encoding_06-4b48042dba364c8a321e0c08a92fd885.png)

Finally, the training data and validation data are stored as artifacts.

![image](https://clear.ml/docs/latest/assets/images/preprocessing_and_encoding_07-4267d243ff16d79fcc6f3ee407a88691.png)

### Training Step [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/table/tabular_training_pipeline/\#training-step "Direct link to Training Step")

Each training node depends upon the completion of one preprocessing node. The parameter `parents` is a list of step names indicating all steps that must complete before the new step starts. In this case, `preprocessing_1` must complete before `train_1` begins, and `preprocessing_2` must complete before `train_2` begins.

The ID of a Task whose artifact contains a set of preprocessed data for training will be overridden using the `data_task_id` key. Its value takes the form `${<stage-name>.<part-of-Task>}`. In this case, `${preprocessing_1.id}` is the ID of one of the preprocessing node Tasks. In this way, each training Task consumes its own set of data.

```python
pipe.add_step(

   name='train_1',

   parents=['preprocessing_1'],

   base_task_project='Tabular Example',

   base_task_name='tabular prediction',

   parameter_override={

      'General/data_task_id': '${preprocessing_1.id}'

   }

)

pipe.add_step(

   name='train_2',

   parents=['preprocessing_2'],

   base_task_project='Tabular Example',

   base_task_name='tabular prediction',

   parameter_override={

      'General/data_task_id': '${preprocessing_2.id}'

   }

)
```

ClearML tracks and reports the training step

In the training Task, the `data_task_id` parameter value is overridden. This allows the pipeline controller to pass a
different Task ID to each instance of training, where each Task has an artifact containing different data.

```python
configuration_dict = {

    'data_task_id': TABULAR_DATASET_ID,

    'number_of_epochs': 15, 'batch_size': 100, 'dropout': 0.3, 'base_lr': 0.1

}

configuration_dict = task.connect(configuration_dict)  # enabling configuration override by clearml
```

ClearML tracks and reports the training step with each instance of the newly cloned and executed training Task.

ClearML automatically logs training loss and learning. They appear in **SCALARS**.

The following images show one of the two training Tasks.

![image](https://clear.ml/docs/latest/assets/images/train_tabular_predictor_04-94fdc416bedd786b6ff85a7ca9c3803e.png)

Parameter dictionaries appear in the **General** subsection.

![image](https://clear.ml/docs/latest/assets/images/train_tabular_predictor_01-4b70aedc1c6494f73585ac347c5a2ea5.png)

The TensorFlow Definitions appear in the **TF\_DEFINE** subsection.

![image](https://clear.ml/docs/latest/assets/images/train_tabular_predictor_02-a450cd17e691dff886a06ee1c454f564.png)

### Best Model Step [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/table/tabular_training_pipeline/\#best-model-step "Direct link to Best Model Step")

The best model step depends upon both training nodes completing and takes the two training node Task IDs to override.

```python
pipe.add_step(

   name='pick_best',

   parents=['train_1', 'train_2'],

   base_task_project='Tabular Example',

   base_task_name='pick best model',

   parameter_override={

      'General/train_tasks_ids': '[${train_1.id}, ${train_2.id}]'

   }

)
```

The IDs of the training Tasks from the steps named `train_1` and `train_2` are passed to the best model Task. They take the form `${<stage-name>.<part-of-Task>}`.

ClearML tracks and reports the best model step

In the best model Task, the `train_tasks_ids` parameter is overridden with the Task IDs of the two training tasks.

```python
configuration_dict = {

   'train_tasks_ids':

      ['c9bff3d15309487a9e5aaa00358ff091', 'c9bff3d15309487a9e5aaa00358ff091']

}

configuration_dict = task.connect(configuration_dict)  # enabling configuration override by clearml
```

The logs show the Task ID and accuracy for the best model in **CONSOLE**.

![image](https://clear.ml/docs/latest/assets/images/tabular_training_pipeline_02-4e578a99490d78b83b845538661db967.png)

The link to the model details is in **ARTIFACTS** **>** **Output Model**.

![image](https://clear.ml/docs/latest/assets/images/tabular_training_pipeline_03-04f90b17fc7082b900828d8bbca2d80b.png)

The model details appear in the **MODELS** table **>** **>GENERAL**.

![image](https://clear.ml/docs/latest/assets/images/tabular_training_pipeline_04-5b9ca650a2034ca71af17550e305cb0f.png)

### Pipeline Start, Wait, and Cleanup [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/table/tabular_training_pipeline/\#pipeline-start-wait-and-cleanup "Direct link to Pipeline Start, Wait, and Cleanup")

Once all steps are added to the pipeline, start it. Wait for it to complete. Finally, cleanup the pipeline processes.

```python
# Starting the pipeline (in the background)

pipe.start()

# Wait until pipeline terminates

pipe.wait()

# cleanup everything

pipe.stop()
```

ClearML tracks and reports the pipeline's execution

ClearML reports the pipeline with its steps in **PLOTS**.

![image](https://clear.ml/docs/latest/assets/images/tabular_training_pipeline_01-8444fc6dd63590e2d7b17ca0a19aa53f.png)

By hovering over a step or path between nodes, you can view information about it.

![image](https://clear.ml/docs/latest/assets/images/tabular_training_pipeline_06-0ed745d92da7061866e7ef43e359b5f5.png)

## Running the Pipeline [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/table/tabular_training_pipeline/\#running-the-pipeline "Direct link to Running the Pipeline")

**To run the pipeline:**

1. Download the data by running the notebook [download\_and\_split.ipynb](https://github.com/clearml/clearml/blob/master/examples/frameworks/pytorch/notebooks/table/download_and_split.ipynb).

2. Run the script for each of the steps, if the script has not run once before.
   - [preprocessing\_and\_encoding.ipynb](https://github.com/clearml/clearml/blob/master/examples/frameworks/pytorch/notebooks/table/preprocessing_and_encoding.ipynb)
   - [train\_tabular\_predictor.ipynb](https://github.com/clearml/clearml/blob/master/examples/frameworks/pytorch/notebooks/table/train_tabular_predictor.ipynb)
   - [pick\_best\_model.ipynb](https://github.com/clearml/clearml/blob/master/examples/frameworks/pytorch/notebooks/table/pick_best_model.ipynb).
3. Run the pipeline controller one of the following two ways:
   - Run the notebook [tabular\_ml\_pipeline.ipynb](https://github.com/clearml/clearml/blob/master/examples/frameworks/pytorch/notebooks/table/tabular_ml_pipeline.ipynb).
   - Remotely execute the Task - If the Task `tabular training pipeline` which is associated with the project `Tabular Example` already exists in ClearML Server, clone it and enqueue it to execute.

note

If you enqueue a Task, a worker must be listening to that queue for the Task to execute.

- [Pipeline Controller and Steps](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/table/tabular_training_pipeline/#pipeline-controller-and-steps)
  - [Preprocessing Step](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/table/tabular_training_pipeline/#preprocessing-step)
  - [Training Step](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/table/tabular_training_pipeline/#training-step)
  - [Best Model Step](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/table/tabular_training_pipeline/#best-model-step)
  - [Pipeline Start, Wait, and Cleanup](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/table/tabular_training_pipeline/#pipeline-start-wait-and-cleanup)
- [Running the Pipeline](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/table/tabular_training_pipeline/#running-the-pipeline)