---
url: "https://clear.ml/docs/latest/docs/release_notes/clearml_serving/ver_1_0/"
title: "Version 1.0 | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/release_notes/clearml_serving/ver_1_0/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

### ClearML Serving 1.0.0 [​](https://clear.ml/docs/latest/docs/release_notes/clearml_serving/ver_1_0/\#clearml-serving-100 "Direct link to ClearML Serving 1.0.0")

Backwards Compatibility

This release is not backwards compatible.

**Breaking Changes**

- `preprocess` and `postprocess` class functions get 3 arguments
- Add support for per-request state storage, passing information between the pre/post-processing functions

**Features and Bug Fixes**

- Optimize serving latency while collecting statistics
- Fix metric statistics collecting auto-refresh issue
- Fix live update of model preprocessing code
- Add `pandas` to the default serving container
- Add per endpoint/variable statistics collection control
- Add `CLEARML_EXTRA_PYTHON_PACKAGES` for easier additional Python package support (serving inference container)
- Upgrade Nvidia Triton base container image to 22.04 (requires Nvidia drivers 510+)
- Add Kubernetes Helm chart

- [ClearML Serving 1.0.0](https://clear.ml/docs/latest/docs/release_notes/clearml_serving/ver_1_0/#clearml-serving-100)