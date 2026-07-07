---
url: "https://clear.ml/docs/latest/docs/release_notes/sdk/open_source/ver_0_16/"
title: "Version 0.16 | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/release_notes/sdk/open_source/ver_0_16/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

important

**Trains** is now **ClearML**.

### Trains 0.16.4 [​](https://clear.ml/docs/latest/docs/release_notes/sdk/open_source/ver_0_16/\#trains-0164 "Direct link to Trains 0.16.4")

**Features**

- Add Hydra support ( [GitHub trains Issue 219](https://github.com/clearml/clearml/issues/219)).
- Add CIFAR ignite example ( [GitHub trains Issue 237](https://github.com/clearml/clearml/issues/237)).
- Add auto extraction of `tar.gz` files when using `StorageManager` ( [GitHub trains Issue 237](https://github.com/clearml/clearml/issues/237)).
- Add `Task.init()` argument `auto_connect_streams` controlling stdout / stderr / logging capture ( [GitHub trains Issue 181](https://github.com/clearml/clearml/issues/181)).
- Add carriage return flush support using the `sdk.development.worker.console_cr_flush_period` configuration setting ( [GitHub trains Issue 181](https://github.com/clearml/clearml/issues/181)).
- Add `Task.create_function_task()` to allow creating a new task, using a function and arguments, to be executed remotely ( [GitHub trains Issue 230](https://github.com/clearml/clearml/issues/230)).
- Allow disabling SSL certificates verification using `Task.setup_upload()` argument `verify` or AWS S3 bucket configuration `verify` property ( [GitHub trains Issue 256](https://github.com/clearml/clearml/issues/256)).
- Add `StorageManager.get_files_server()`.
- Add `Task.get_project_id()` using project name.
- Add `project_name` argument to `Task.set_project()`.
- Add `Task.connect()` support for class / instance objects.
- Add `Task get_configuration_object()` and `Task.set_configuration_object()` for easier automation.
- Improve Auto-Scaler - allow extra configurations, key name and security group are now optional, defaults using empty strings.
- Use a built-in matplotlib convertor.
- Add reporting text as debug sample example.

**Bug Fixes**

- Fix Optuna HPO parameter serializing ( [GitHub trains Issue 254](https://github.com/clearml/clearml/issues/254)).
- Fix connect dictionary `''` cast to `None` ( [GitHub trains Issue 258](https://github.com/clearml/clearml/issues/258)).
- Fix lightgbm binding keyword argument issue ( [GitHub trains Issue 251](https://github.com/clearml/clearml/issues/251)).
- Fix artifact preview if artifact body is remote URI ( [GitHub trains Issue 239](https://github.com/clearml/clearml/issues/239)).
- Fix infinite recursion in `StorageManager` upload ( [GitHub trains Issue 253](https://github.com/clearml/clearml/issues/253)).
- Fix keras reusing model object only if the filename is the same ( [GitHub trains Issue 252](https://github.com/clearml/clearml/issues/252)).
- Fix running remotely with no configuration should not crash but output a warning ( [GitHub trains Issue 243](https://github.com/clearml/clearml/issues/243)).
- Fix matplotlib 3.3.3 support:
  - Fix global figure enumeration.
  - Fix binding without a title reported a single plot (`untitled 00`) instead of increasing the counter.
- Fix Python 2.7 / 3.5 support.
- Fix quote issue when reporting debug images.
- Fix replace quote safe characters in upload file to include `;=@$`.
- Fix `at_exit` called from another process should be ignored.
- Fix `Task.set_tags()` for completed / published tasks.
- Fix `Task.add_tags()` not working when running remotely.
- Fix `Task.set_user_properties()` docstring and interface.
- Fix preview with JSON (dict) artifacts did not store the artifact.
- Fix `Logger.report_text()` on task created using `Task.create()` was not supported.
- Fix initialization for torch: only call torch `get_worker_info` if torch was loaded.
- Fix flush (wait) on auxiliary task (obtained using` Task.get_task()`) should wait on all upload events.
- Fix server was not updated with the defaults from the code when running remotely and configuration section is missing.
- Fix connect dict containing `None` default values, blocked the remote execution from passing string instead of None.
- Fix `Task.upload_artifact()` argument `delete_after_upload=True` used in conjunction with `wait_for_upload=True` was not supported.

### Trains 0.16.3 [​](https://clear.ml/docs/latest/docs/release_notes/sdk/open_source/ver_0_16/\#trains-0163 "Direct link to Trains 0.16.3")

**Features**

- Add LightGBM support.
- Add initial Hydra support ( [GitHub trains Issue 219](https://github.com/clearml/clearml/issues/219)).
- Add synchronous support for `Task.upload_artifact()` ( [GitHub trains Issue 231](https://github.com/clearml/clearml/issues/231)).
- Add `sdk.development.store_code_diff_from_remote` (default `false`) to store diff from remote HEAD instead of local HEAD ( [GitHub trains Issue 222](https://github.com/clearml/clearml/issues/222)).
- Add `sdk.development.detect_with_conda_freeze` (default `true`) for full conda freeze (requires trains-agent >= 16.2).
- Add user properties support in Task object.
- Add `Logger.report_table()` support for table as list of lists.
- Add support to split DAG and Table in pipeline DAG plot. Pipeline DAG single nodes are now round circles below the DAG graph.
- Add Pipeline / Optimization can be attached to any Task (not just the current task).
- Add `force_download` flag to `StorageManager.get_local_copy()`.
- Add control over the artifact preview using `Task.upload_artifact()``preview` argument.
- Add `Logger.report_matplotlib_figure()` with examples.
- Add `Task.set_task_type()`.
- Improve AWS auto-scaler:
  - Add key pair and security groups support.
  - Add multi-line support for both extra bash script and extra `trains.conf` data.
- Update examples.

**Bug Fixes**

- Fix `Task.update_output_model()` wrong argument order ( [GitHub trains Issue 220](https://github.com/clearml/clearml/issues/220)).
- Fix initializing task on argparse parse in remote mode. Do not call `Task.init()` to avoid auto connect, use `Task.get_task()` instead.
- Fix detected task cwd outside of repository root folder.
- Fix `Task.connect(dict)` to place non-existing entries on the section name instead of General.
- Fix `Task.clone()` support for trains-server < 0.16.
- Fix `StorageManager` cache extract zipped artifacts. Use modified time instead of access time for cached files.
- Fix diff command output was stripped.
- Make sure local packages with multi-files are marked as `package`.
- Fix `Task.set_base_docker()` should be skipped when running remotely.
- Fix ArgParser binding handling of string argument with boolean default value (affects PyTorch Lightning integration).
- When using `detect_with_pip_freeze` make sure that `package @ file://` lines are replaced with `package==x.y.z` as local file will probably not be available.
- Fix git packages to new pip standard `package @ git+`.
- Improve conda package naming `_` and `-` support.
- Do not add specific setuptools version to requirements (pip can't install it anyway).
- Fix image URL quoting when uploading from a file path.

### Trains 0.16.2 [​](https://clear.ml/docs/latest/docs/release_notes/sdk/open_source/ver_0_16/\#trains-0162 "Direct link to Trains 0.16.2")

**Features**

- Add `Task.set_resource_monitor_iteration_timeout()` to set ResourceMonitor iteration wait duration timeout ( [GitHub trains Issue 208](https://github.com/clearml/clearml/issues/208)).
- Add PyTorch Lightning save/restore model binding ( [GitHub trains Issue 212](https://github.com/clearml/clearml/issues/212)).
- Add `git diff` for repository submodule (requires git 2.14 or above).
- Add `TrainsJob.is_completed()` and `TrainsJob.is_aborted()`.
- Add `Task.logger` property.
- Add Pipeline Controller automation and example (see [here](https://github.com/clearml/clearml/blob/master/examples/pipeline/pipeline_from_tasks.py)).
- Add improved trace filtering capabilities in `trains.debugging.trace.trace_trains()`.
- Add default help per argument (if not provided) in ArgParser binding.
- Deprecate `Task.reporter`.
- Update PyTorch example.
- Remove warning on skipped auto-magic model logging ( [GitHub trains Issue 206](https://github.com/clearml/clearml/issues/206)).
- Support Keras restructuring for Network, Model and Sequential.
- Update autokeras requirements according to [https://github.com/keras-team/autokeras#installation](https://github.com/keras-team/autokeras#installation).

**Bug Fixes**

- Fix joblib auto logging models failing on compressed streams ( [GitHub trains Issue 203](https://github.com/clearml/clearml/issues/203)).
- Fix sending empty reports ( [GitHub trains Issue 205](https://github.com/clearml/clearml/issues/205)).
- Fix scatter2d sub-sampling and rounding.
- Fix plots reporting:
  - `NaN` representation (matplotlib conversion).
  - Limit the number of digits in a plot to reduce plot size (using `sdk.metrics.plot_max_num_digits` configuration value).
- Fix `Task.wait_for_status()` to reload after it ends.
- Fix thread wait Ctrl-C interrupt did not exit process.
- Improve Windows support for installed packages analysis.
- Fix auto model logging using relative path.
- Fix Hyperparameter Optimization example.
- Fix `Task.clone()` when working with TrainsServer < 0.16.0.
- Fix pandas artifact handling.
- Avoid adding `unnamed:0` column.
- Return original pandas object.
- Fix `TrainsJob` hyper-params overriding order was not guaranteed.
- Fix ArgParse auto-connect to support default function type.

### Trains 0.16.1 [​](https://clear.ml/docs/latest/docs/release_notes/sdk/open_source/ver_0_16/\#trains-0161 "Direct link to Trains 0.16.1")

**Features**

- Enhance HyperParameter optimizer.

**Bug Fixes**

- Fix typing dependency for `Python<3.5` ( [GitHub trains Issue 184](https://github.com/clearml/clearml/issues/184)).
- Fix git+https requirements handling, resolve top\_level.txt package name (kerastuner from git was not detected).
- Fix `Task.get_reported_console_output()` for new Trains Server API v2.9.
- Fix cache handling for different partitions / drives / devices.
- Disable offline mode when running remotely (i.e. executed by Trains Agent).
- Fix artifact upload to only use file stream when not uploading a locally stored file (multipart upload is not supported on stream upload) ( [GitHub trains Issue 189](https://github.com/clearml/clearml/issues/189)).
- Fix double-escaped model design text when connecting OutputModel.

### Trains 0.16.0 [​](https://clear.ml/docs/latest/docs/release_notes/sdk/open_source/ver_0_16/\#trains-0160 "Direct link to Trains 0.16.0")

**Features**

- Add continuing of previously executed experiments. Add `Task.init()` argument `continue_last_task` to continue a previously used Task ( [GitHub Issue #160](https://github.com/clearml/clearml/issues/160)).
- Allow Task editing / creation from code. `Task.export_task/import_task/update_task()` ( [GitHub Issue #128](https://github.com/clearml/clearml/issues/128)).
- Add offline mode. Use `Task.set_offline()` and `Task.import_offline_session()`:

  - Support setting offline mode via `TRAINS_OFFLINE_MODE=1` environment variable.
  - Support setting offline API version via `TRAINS_OFFLINE_MODE=2.9` environment variable.
- Automatically pickle all objects uploaded as artifacts, `task.upload_artifact()` argument `auto_pickle=True` ( [GitHub Issue #153](https://github.com/clearml/clearml/issues/153)).
- Add multiple sections / groups support for Task hyperparameters, using `Task.connect()`.
- Add multiple configurations (files) using `Task.connect_configuration()`.
- Allow enabling OS environment logging using the `sdk.development.log_os_environments` configuration parameter (complements the `TRAINS_LOG_ENVIRONMENT` environment variable).
- Add Optuna support for hyperparameter optimization controller. `OptimizerOptuna` is now the default optimizer.
- Add initial Keras-Tuner support ( [GitHub Issue keras-team/keras-tuner #334](https://github.com/keras-team/keras-tuner/issues/334)).
- Add automatic FastAI logging. It is disabled if Tensorboard is loaded (assuming TensorBoardLogger will be used).
- Support Tensorboard text logging (`add_text()`) as debug samples (`.txt` files), instead of as console output.
- Allow for more standard confusion matrix reporting. `Logger.report_confusion_matrix()` argument `yaxis_reversed` (flips the confusion matrix if `True`, default `False`) ( [GitHub Issue #165](https://github.com/clearml/clearml/issues/165)).
- Add support for Trains Server 0.16.0 (API v2.9 support).
- Allow disabling Trains update message from the log using the `TRAINS_SUPPRESS_UPDATE_MESSAGE` environment variable ( [GitHub Issue #157](https://github.com/clearml/clearml/issues/157)).
- Add AWS EC2 Auto-Scaler service wizard and Service.
- Improved and updated examples:
  - Add Keras Tuner CIFAR-10 example.
  - Add FastAI example.
  - Update PyTorch Jupyter notebook examples ( [GitHub Issue #150](https://github.com/clearml/clearml/issues/150)).
- Support global requirements detection using `pip freeze` (set `sdk.development.detect_with_pip_freeze` configuration in `trains.conf`).
- Add `Task.get_projects()` to get all projects in the system, sorted by last update time.

**Bug Fixes**

- Fix UTC to time stamp in comment ( [GitHub Issue #152](https://github.com/clearml/clearml/issues/152)).
- Fix and enhance GPU monitoring:
  - Fix GPU stats on Windows machines ( [GitHub Issue #177](https://github.com/clearml/clearml/issues/177)).
  - More robust GPU monitoring ( [GitHub Issue #170](https://github.com/clearml/clearml/issues/170)).
- Fix filename too long bug ( [GitHub trains-server Issue #49](https://github.com/clearml/clearml-server/issues/49)).
- Fix TensorFlow image logging to allow images with no width / height / color metadata ( [GitHub Issue #182](https://github.com/clearml/clearml/issues/182)).
- Fix multiprocessing Pool throw exception in pool hangs execution. Call original signal handler and re-flush `stdout`.
- Fix `plotly` support for `matplotlib` 3.3.
- Add Python 2.7 support for `get_current_thread_id()`.
- Update examples requirements.
- Fix and improve signal handling.
- Fix Tensorboard 2D convolution histogram, improve histogram accuracy on very small histograms.
- Fix auto logging multiple argparse calls before `Task.init()`.
- Limit experiment Git diff logging to 500Kb. If larger than 500Kb, diff section will contain a warning and entire diff will be uploaded as an artifact named `auxiliary_git_dif`.
- Fix requirements detection:
  - Fix Trains installed from `git+`.
  - Fix when Trains is not directly imported.
  - Fix multiple `-e` packages were not detected (only the first one).
  - Fix running with Trains in `PYTHONPATH` resulted in double entry of trains.
- Fix `Task.set_base_docker()` on main task to do nothing when running remotely.

- [Trains 0.16.4](https://clear.ml/docs/latest/docs/release_notes/sdk/open_source/ver_0_16/#trains-0164)
- [Trains 0.16.3](https://clear.ml/docs/latest/docs/release_notes/sdk/open_source/ver_0_16/#trains-0163)
- [Trains 0.16.2](https://clear.ml/docs/latest/docs/release_notes/sdk/open_source/ver_0_16/#trains-0162)
- [Trains 0.16.1](https://clear.ml/docs/latest/docs/release_notes/sdk/open_source/ver_0_16/#trains-0161)
- [Trains 0.16.0](https://clear.ml/docs/latest/docs/release_notes/sdk/open_source/ver_0_16/#trains-0160)