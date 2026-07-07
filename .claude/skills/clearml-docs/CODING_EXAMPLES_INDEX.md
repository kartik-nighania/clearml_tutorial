# ClearML Coding Examples Index

Total example scripts indexed: 128 (.py) + 18 (.ipynb)


## `coding_examples/advanced/`

- `execute_remotely_example.py` — the task.remote_execution option is used when it's needed to run part of the code locally and then move it for
- `model_embedding.py` — (no description found)
- `multiple_tasks_single_process.py` — Task: Same process, Multiple tasks, Task #{}

## `coding_examples/advanced/model_finetuning/`

- `extract.py` — (no description found)
- `finetune.py` — Task: Finetune
- `upload_local_model.py` — Task: Upload Local Model

## `coding_examples/automation/`

- `manual_random_param_search_example.py` — Task: Random Hyper-Parameter Search Example
- `programmatic_orchestration.py` — Initialize the Task Pipe's first Task used to start the Task Pipe
- `toy_base_task.py` — This Task is the base task that we will be executing as a second step (see task_piping.py)

## `coding_examples/cicd/`

- `check_remotely_runnable.py` — Get the task object
- `compare_models.py` — Task: cicd_test
- `example_task.py` — This is a dummy ClearML task. This should be replaced by your own experiment code.
- `task_stats_to_comment.py` — (no description found)

## `coding_examples/datasets/`

- `csv_dataset_creation.py` — By default, clearml data uploads to the clearml fileserver. Adding output_uri argument to the create() method
- `data_ingestion.py` — Task: Image classification with clearml-data
- `dataset_creation.py` — Download CIFAR dataset and create a dataset with ClearML's Dataset class
- `dataset_folder_syncing.py` — (no description found)
- `multi_parent_child_dataset.py` — (no description found)
- `single_parent_child_dataset.py` — (no description found)
- `urbansounds_dataset_preprocessing.py` — Task: preprocessing
- `urbansounds_get_data.py` — Task: download data

## `coding_examples/distributed/`

- `pytorch_distributed_example.py` — Gradient averaging.
- `subprocess_example.py` — ClearML - example of multiple sub-processes interacting and reporting to a single master experiment

## `coding_examples/frameworks/autokeras/`

- `autokeras_imdb_example.py` — Task: AutoKeras IMDB example with scalars

## `coding_examples/frameworks/catboost/`

- `catboost_example.py` — Task: CatBoost simple example

## `coding_examples/frameworks/click/`

- `click_multi_cmd.py` — Task: Click multi command
- `click_single_cmd.py` — Task: Click single command

## `coding_examples/frameworks/fastai/`

- `fastai_example.py` — Task: fastai v2
- `fastai_with_tensorboard_example.py` — Task: fastai v2 with tensorboard callback

## `coding_examples/frameworks/fastai/legacy/`

- `fastai_example.py` — Task: fastai v1
- `fastai_with_tensorboard_example.py` — Task: fastai with tensorboard callback

## `coding_examples/frameworks/fire/`

- `fire_class_cmd.py` — Task: Fire class command
- `fire_dict_cmd.py` — Task: Fire dict command
- `fire_grouping_cmd.py` — Task: Fire grouping command
- `fire_multi_cmd.py` — Task: Fire multi command
- `fire_object_cmd.py` — Task: Fire object command
- `fire_single_cmd.py` — Task: Fire single command
- `fire_typing.py` — Task: Fire typing command

## `coding_examples/frameworks/hydra/`

- `hydra_example.py` — Task: Hydra configuration

## `coding_examples/frameworks/ignite/`

- `cifar_ignite.py` — Task: Image classification CIFAR10

## `coding_examples/frameworks/jsonargparse/`

- `jsonargparse_command.py` — Task: jsonargparse command
- `jsonargparse_nested_namespaces.py` — Task: jsonargparse nested namespaces
- `pytorch_lightning_cli.py` — Task: pytorch_lightning_jsonargparse
- `pytorch_lightning_cli_old.py` — Task: pytorch_lightning_jsonargparse

## `coding_examples/frameworks/keras/`

- `keras_tensorboard.py` — Task: Keras with TensorBoard example
- `keras_v3.py` — Task: keras_v3

## `coding_examples/frameworks/keras/legacy/`

- `keras_tensorboard.py` — Task: Keras with TensorBoard example

## `coding_examples/frameworks/kerastuner/`

- `keras_tuner_cifar.py` — Keras Tuner CIFAR10 example for the TensorFlow blog post.
- `keras_tuner_cifar_legacy.py` — Keras Tuner CIFAR10 example for the TensorFlow blog post.

## `coding_examples/frameworks/lightgbm/`

- `lightgbm_example.py` — Task: LightGBM

## `coding_examples/frameworks/matplotlib/`

- `matplotlib_example.py` — Task: Matplotlib example

## `coding_examples/frameworks/megengine/`

- `megengine_mnist.py` — Task: MegEngine MNIST train

## `coding_examples/frameworks/openmmlab/`

- `openmmlab_cifar10.py` — Task: OpenMMLab cifar10

## `coding_examples/frameworks/pytorch/`

- `pytorch_abseil.py` — Task: PyTorch MNIST train with abseil
- `pytorch_distributed_example.py` — Gradient averaging.
- `pytorch_matplotlib.py` — Run the style transfer.
- `pytorch_mnist.py` — Task: PyTorch MNIST train
- `pytorch_model_update.py` — Task: Model update PyTorch
- `pytorch_tensorboard.py` — Task: PyTorch with TensorBoard
- `pytorch_tensorboardx.py` — Task: PyTorch with tensorboardX
- `tensorboard_toy_pytorch.py` — Task: PyTorch TensorBoard toy example

## `coding_examples/frameworks/pytorch-lightning/`

- `pytorch_lightning_example.py` — Task: pytorch lightning MNIST

## `coding_examples/frameworks/scikit-learn/`

- `sklearn_joblib_example.py` — Task: Scikit-learn joblib example
- `sklearn_matplotlib_example.py` — (no description found)

## `coding_examples/frameworks/tensorboardx/`

- `moviepy_tensorboardx.py` — Task: pytorch with video tensorboardX
- `pytorch_tensorboardX.py` — Task: PyTorch with tensorboardX

## `coding_examples/frameworks/tensorflow/`

- `absl_flags.py` — Task: Abseil example
- `tensorboard_pr_curve.py` — Generate PR curve summaries.
- `tensorboard_toy.py` — Task: TensorbBoard toy example
- `tensorflow_mnist.py` — Task: TensorFlow v2 MNIST with summaries

## `coding_examples/frameworks/tensorflow/legacy/`

- `tensorboard_pr_curve.py` — Generate PR curve summaries.
- `tensorboard_toy.py` — Task: TensorBoard toy example
- `tensorflow_eager.py` — Train `generator` and `discriminator` models on `dataset`.
- `tensorflow_mnist_with_summaries.py` — Make a TensorFlow feed_dict: maps data onto Tensor placeholders.

## `coding_examples/frameworks/xgboost/`

- `xgboost_metrics.py` — Task: XGBoost metric auto reporting
- `xgboost_sample.py` — Task: XGBoost simple example

## `coding_examples/hyperdatasets/`

- `create_coco_hyperdataset.py` — Download a subset of COCO and convert it into a ClearML HyperDataset.
- `create_doc_entries.py` — Create a HyperDataset populated with Markdown documentation links.
- `create_image_entries.py` — Create a HyperDataset populated with local image files.
- `create_qa_entries.py` — Create a HyperDataset populated with raw Q&A pairs.
- `dataview.py` — Task: dataview_iterate
- `dataview_pytorch_dataloader.py` — ClearML utilities for resolving datasets and creating dataview iterators
- `finetune_qa_lora.py` — Fine-tune a base LLM with LoRA adapters on HyperDataset Q&A entries using Hugging Face's Trainer.
- `vector_search.py` — Search HyperDataset entries using vector similarity.

## `coding_examples/hyperdatasets/legacy/data-ingestion/`

- `dataview_example_framegroup.py` — Task: dataview example with masks
- `dataview_example_singleframe.py` — How to access and go over data
- `pytorch_dataset_example.py` — Task: PyTorch Sample Dataset
- `pytorch_dataset_example_with_masks.py` — Task: PyTorch Sample Dataset with Masks

## `coding_examples/hyperdatasets/legacy/data-registration/`

- `register_dataset_masks.py` — How to register data with masks from a json file.
- `register_dataset_with_roi.py` — How to register data with ROIs and metadata from a json file.

## `coding_examples/optimization/hyper-parameter-optimization/`

- `base_template_keras_simple.py` — Task: Keras HP optimization base
- `hyper_parameter_optimizer.py` — Task: Automatic Hyper-Parameter Optimization
- `multi_objective_hpo.py` — Task: Multi-objective HPO

## `coding_examples/pipeline/`

- `decorated_pipeline_step_decorators.py` — (no description found)
- `decorated_pipeline_step_functions.py` — (no description found)
- `full_tabular_data_process_pipeline_example.py` — (no description found)
- `pipeline_from_decorator.py` — Make the following function an independent pipeline component step
- `pipeline_from_functions.py` — We will use the following function an independent pipeline component step
- `pipeline_from_tasks.py` — Task: Pipeline step 1 dataset artifact
- `step1_dataset_artifact.py` — Task: Pipeline step 1 dataset artifact
- `step2_data_processing.py` — Task: Pipeline step 2 process dataset
- `step3_train_model.py` — Task: Pipeline step 3 train model

## `coding_examples/reporting/`

- `3d_plots_reporting.py` — reporting plots to plots section
- `artifacts.py` — Task: Artifacts example
- `artifacts_retrieval.py` — Task: Artifacts example
- `config_files.py` — Task: config_files_example
- `html_reporting.py` — reporting bokeh image (html) to debug samples section
- `hyper_parameters.py` — Task: first_trial
- `image_reporting.py` — reporting images to debug samples section
- `matplotlib_automatic_reporting.py` — Task: Matplotlib example
- `matplotlib_manual_reporting.py` — Task: Manual Matplotlib example
- `media_reporting.py` — Task: Audio and video reporting
- `model_reporting.py` — Task: Model reporting example
- `model_reporting_plots.py` — Task: Model reporting plots example
- `pandas_reporting.py` — reporting tables to the plots section
- `plotly_reporting.py` — ClearML - Example of Plotly integration and reporting
- `scalar_reporting.py` — reporting scalars to scalars section
- `scatter_hist_confusion_mat_reporting.py` — reporting plots to plots section
- `text_reporting.py` — text_to_send =
- `using_artifacts_example.py` — Upload artifacts from a Task, and then a different Task can access and utilize the data from that artifact.

## `coding_examples/router/`

- `http_router.py` — Example on how to use the ClearML HTTP router.
- `multi_endpoints.py` — Minimal example showing how to request multiple external endpoints for a Task.
- `simple_webserver.py` — A simple webserver, used as a tool to showcase the capabilities of

## `coding_examples/scheduler/`

- `cron_example.py` — Task: PyTorch MNIST train
- `trigger_example.py` — (no description found)

## `coding_examples/services/aws-autoscaler/`

- `aws_autoscaler.py` — Task: AWS Auto-Scaler

## `coding_examples/services/cleanup/`

- `cleanup_service.py` — This service will delete archived experiments and their accompanying debug samples, artifacts and models

## `coding_examples/services/monitoring/`

- `slack_alerts.py` — Create a ClearML Monitoring Service that posts alerts on Slack Channel groups based on some logic

## Jupyter notebooks

- `coding_examples/clearml_agent/clearml_colab_agent.ipynb`
- `coding_examples/frameworks/huggingface/transformers.ipynb`
- `coding_examples/frameworks/keras/jupyter.ipynb`
- `coding_examples/frameworks/keras/jupyter_keras_TB_example.ipynb`
- `coding_examples/frameworks/keras/legacy/jupyter.ipynb`
- `coding_examples/frameworks/matplotlib/jupyter_matplotlib_example.ipynb`
- `coding_examples/frameworks/pytorch/notebooks/audio/audio_classifier_UrbanSound8K.ipynb`
- `coding_examples/frameworks/pytorch/notebooks/audio/audio_preprocessing_example.ipynb`
- `coding_examples/frameworks/pytorch/notebooks/image/hyperparameter_search.ipynb`
- `coding_examples/frameworks/pytorch/notebooks/image/image_classification_CIFAR10.ipynb`
- `coding_examples/frameworks/pytorch/notebooks/table/download_and_preprocessing.ipynb`
- `coding_examples/frameworks/pytorch/notebooks/table/download_and_split.ipynb`
- `coding_examples/frameworks/pytorch/notebooks/table/pick_best_model.ipynb`
- `coding_examples/frameworks/pytorch/notebooks/table/preprocessing_and_encoding.ipynb`
- `coding_examples/frameworks/pytorch/notebooks/table/tabular_ml_pipeline.ipynb`
- `coding_examples/frameworks/pytorch/notebooks/table/train_tabular_predictor.ipynb`
- `coding_examples/frameworks/pytorch/notebooks/text/text_classification_AG_NEWS.ipynb`
- `coding_examples/reporting/jupyter_logging_example.ipynb`
