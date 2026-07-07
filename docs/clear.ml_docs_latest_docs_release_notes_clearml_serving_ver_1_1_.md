---
url: "https://clear.ml/docs/latest/docs/release_notes/clearml_serving/ver_1_1/"
title: "Version 1.1 | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/release_notes/clearml_serving/ver_1_1/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

### ClearML Serving 1.1.0 [​](https://clear.ml/docs/latest/docs/release_notes/clearml_serving/ver_1_1/\#clearml-serving-110 "Direct link to ClearML Serving 1.1.0")

Backwards Compatibility

This release is not backwards compatible. See `Upgrading from v1.0` note below.

**Breaking Changes**

- Triton engine size supports variable request size (-1)

**Features and Bug Fixes**

- Add version number of serving session task
- Triton engine support for variable request (matrix) sizes
- Triton support, fix `--aux-config` to support more configurations elements
- Hugging Face Transformer support
- `Preprocess` class as module (see `Preprocess Class` note below)

Upgrading from v1.0

1. Take down the serving containers (docker-compose or k8s)
2. Update the `clearml-serving` CLI: `pip3 install -U clearml-serving`
3. Re-add a single existing endpoint: `clearml-serving model add ...` (press `yes` when asked). This will upgrade the
`clearml-serving` session definitions
4. Pull latest serving containers (`docker-compose pull ...` or k8s)
5. Re-spin serving containers (docker-compose or k8s)

Preprocess Class

You can now add a `Preprocess` class from a module. The entire module folder will be packaged.

```text
preprocess_folder

├── __init__.py  # from .sub.some_file import Preprocess

└── sub

    └── some_file.py
```

Pass the top-level folder path using `--preprocess`. For example:

```text
clearml-serving --id <serving_session_id> model add --preprocess /path/to/preprocess_folder ...
```

- [ClearML Serving 1.1.0](https://clear.ml/docs/latest/docs/release_notes/clearml_serving/ver_1_1/#clearml-serving-110)