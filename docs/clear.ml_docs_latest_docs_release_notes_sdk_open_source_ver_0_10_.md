---
url: "https://clear.ml/docs/latest/docs/release_notes/sdk/open_source/ver_0_10/"
title: "Version 0.10 | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/release_notes/sdk/open_source/ver_0_10/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

important

**Trains** is now **ClearML**.

### Trains 0.10.7 [​](https://clear.ml/docs/latest/docs/release_notes/sdk/open_source/ver_0_10/\#trains-0107 "Direct link to Trains 0.10.7")

**Features and Bug Fixes**

- Artifacts support.
- Removed apache-libcloud from requirements.
- `trains-init` now verifies credentials against the trains-server installation.

### Trains 0.10.6 [​](https://clear.ml/docs/latest/docs/release_notes/sdk/open_source/ver_0_10/\#trains-0106 "Direct link to Trains 0.10.6")

**Features and Bug Fixes**

- Fix broken (v0.10.5) Keras Binding support.

### Trains 0.10.5 [​](https://clear.ml/docs/latest/docs/release_notes/sdk/open_source/ver_0_10/\#trains-0105 "Direct link to Trains 0.10.5")

**Features and Bug Fixes**

- Add GPU monitoring support (add gpustat package to extras\_require).

- Install with GPU monitoring support:





```text
pip install trains[gpu]
```

- Move all cloud storage package requirements to extras\_require. Install with specific cloud provider support:
  - Microsoft Azure support:





    ```text
    pip install trains[azure]
    ```

  - Google Storage support:





    ```text
    pip install trains[gs]
    ```

  - Amazon S3 support:





    ```text
    pip install trains[s3]
    ```

  - Combine Cloud support with GPU monitoring. For example, install S3 and GPU using the following command:





    ```text
    pip install trains[s3,gpu]
    ```
- Improve stability with intermittent network connection.

- Support upgrading trains-server while running training jobs without losing log data.


### Trains 0.10.4 [​](https://clear.ml/docs/latest/docs/release_notes/sdk/open_source/ver_0_10/\#trains-0104 "Direct link to Trains 0.10.4")

**Features and Bug Fixes**

- Replace opencv-python with the more standard Pillow package.
- Improve matplotlib support (custom axis ticks).
- Improve Python package detection.

### Trains 0.10.3 [​](https://clear.ml/docs/latest/docs/release_notes/sdk/open_source/ver_0_10/\#trains-0103 "Direct link to Trains 0.10.3")

**Features and Bug Fixes**

- Add scikit-learn support (load/store using joblib) ( [GitHub Issue #20](https://github.com/clearml/clearml/issues/20)).
- Add xgboost support ( [GitHub Issue #10](https://github.com/clearml/clearml/issues/10)).
- Add loguru support ( [GitHub Issue #29](https://github.com/clearml/clearml/issues/29)).
- Add subdomain support [trains.conf](https://github.com/clearml/clearml/blob/master/docs/trains.conf#L3) ( [GitHub Issue #27](https://github.com/clearml/clearml/issues/27)).
- Fix sub-process support.
- Fix multiple TensorBoard writers ( [GitHub Issue #26](https://github.com/clearml/clearml/issues/26)).

### Trains 0.10.2 [​](https://clear.ml/docs/latest/docs/release_notes/sdk/open_source/ver_0_10/\#trains-0102 "Direct link to Trains 0.10.2")

**Features and Bug Fixes**

- Add Matplotlib SVG support.
- Add Seaborn support.
- Add `TRAINS_LOG_ENVIRONMENT` environment logging ( [GitHub trains Issue 17](https://github.com/clearml/clearml/issues/17#issuecomment-507398767)).
- Add Microsoft Azure notebook support.
- Add Google Colab support.
- Fix TensorBoard RGB channel order.

### Trains 0.10.1 [​](https://clear.ml/docs/latest/docs/release_notes/sdk/open_source/ver_0_10/\#trains-0101 "Direct link to Trains 0.10.1")

**Features and Bug Fixes**

- Fix Jenkins CI/CD support.

### Trains 0.10.0 [​](https://clear.ml/docs/latest/docs/release_notes/sdk/open_source/ver_0_10/\#trains-0100 "Direct link to Trains 0.10.0")

- Experiment code execution detection
- Automatically create package requirements section (including used versions).
- Automatically detect and store source code uncommitted changes.
- Improve Jupyter Notebook support
  - Automatically convert notebook to Python script (stored under uncommitted changes).
  - Automatically update used packages in Jupyter Notebook (including used versions).
- Add resource monitoring to experiment metrics
- Sample every 500ms, averaged over 30 seconds.
- CPU, network, I/O, memory, and other resources.
- For GPU support please install gpustat.
(currently not part of the requirements due to gpustat compatibility issues with Windows).





```text
pip install gpustat
```

- Automatically stop inactive tasks (default: 2 hours)
- Improve visibility
- Finer status definitions: Identify successful completion vs. user aborted.
- Experiment plot comparison: Ensure different colors for different experiments.
- Parse newline character in experiment description.
- Show experiment start time in table display.
- Add vertical guide in scalar plots.
- Move hyperparameters to the designated tab.
- "Admin" section now named "Profile".

- [Trains 0.10.7](https://clear.ml/docs/latest/docs/release_notes/sdk/open_source/ver_0_10/#trains-0107)
- [Trains 0.10.6](https://clear.ml/docs/latest/docs/release_notes/sdk/open_source/ver_0_10/#trains-0106)
- [Trains 0.10.5](https://clear.ml/docs/latest/docs/release_notes/sdk/open_source/ver_0_10/#trains-0105)
- [Trains 0.10.4](https://clear.ml/docs/latest/docs/release_notes/sdk/open_source/ver_0_10/#trains-0104)
- [Trains 0.10.3](https://clear.ml/docs/latest/docs/release_notes/sdk/open_source/ver_0_10/#trains-0103)
- [Trains 0.10.2](https://clear.ml/docs/latest/docs/release_notes/sdk/open_source/ver_0_10/#trains-0102)
- [Trains 0.10.1](https://clear.ml/docs/latest/docs/release_notes/sdk/open_source/ver_0_10/#trains-0101)
- [Trains 0.10.0](https://clear.ml/docs/latest/docs/release_notes/sdk/open_source/ver_0_10/#trains-0100)