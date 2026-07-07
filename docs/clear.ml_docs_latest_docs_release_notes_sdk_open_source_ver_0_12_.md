---
url: "https://clear.ml/docs/latest/docs/release_notes/sdk/open_source/ver_0_12/"
title: "Version 0.12 | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/release_notes/sdk/open_source/ver_0_12/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

important

**Trains** is now **ClearML**.

### Trains 0.12.2 [​](https://clear.ml/docs/latest/docs/release_notes/sdk/open_source/ver_0_12/\#trains-0122 "Direct link to Trains 0.12.2")

**Features and Bug Fixes**

- Add `default_output_uri` feature ( [GitHub Issue #57](https://github.com/clearml/clearml/issues/57)).
- Improve `trains-init` configuration wizard.
- Improve argparser binding.
- Fix artifact support in data pipeline ( [GitHub Issue #63](https://github.com/clearml/clearml/issues/63)).
- Fix threading issue while querying multiple experiments ( [GitHub Issue #64](https://github.com/clearml/clearml/issues/64)).
- Fix uploading large files over slow HTTP connections.
- Fix support for Git versions < 2.

Breaking Changes

Do not reuse an experiment with artifacts.

### Trains 0.12.1 [​](https://clear.ml/docs/latest/docs/release_notes/sdk/open_source/ver_0_12/\#trains-0121 "Direct link to Trains 0.12.1")

**Features and Bug Fixes**

- Add `Task.connect_configuration`, connect configuration file (or configuration dictionary including nesting support).
- Add `Task.connect_label_enumeration`, store model detection classes together with the model and experiment.
- Edit and override configuration file (or dictionary) content when executing with [trains-agent](https://github.com/clearml/clearml-agent).
- `Task.connect` automatically supports nested dictionaries (e.g. param / nested / key), including overriding values when
running with [trains-agent](https://github.com/clearml/clearml-agent).
- Add `Artifact.get`, download and load an artifact.
- Add `Task.get_tasks`, retrieve previous experiments, get metrics, rename, and other uses.
- Improve Windows support.
- Improve Minio support.
- Fix Python2 support.
- Fix Issue ( [GitHub Issue #56](https://github.com/clearml/clearml/issues/56)).

### Trains 0.12.0 [​](https://clear.ml/docs/latest/docs/release_notes/sdk/open_source/ver_0_12/\#trains-0120 "Direct link to Trains 0.12.0")

**Features and Bug Fixes**

- TRAINS Agent support (Full DevOps support).
- Add automation and orchestration ( [examples/automation](https://github.com/clearml/clearml/tree/master/examples/automation)).
Supports TRAINS-server v0.12 or above.
- Add Logger x/y/z axis title for: report\_surface / report\_confusion\_matrix / report\_scatter3d / report\_scatter2d / report\_histogram.
- Add support for TensorFlow 2.0.
- Embed pyhocon into package.
- Fix artifacts support on Windows.
- Fix example code Windows support.

- [Trains 0.12.2](https://clear.ml/docs/latest/docs/release_notes/sdk/open_source/ver_0_12/#trains-0122)
- [Trains 0.12.1](https://clear.ml/docs/latest/docs/release_notes/sdk/open_source/ver_0_12/#trains-0121)
- [Trains 0.12.0](https://clear.ml/docs/latest/docs/release_notes/sdk/open_source/ver_0_12/#trains-0120)