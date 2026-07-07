---
url: "https://clear.ml/docs/latest/docs/release_notes/sdk/enterprise/ver_3_11/"
title: "Version 3.11 | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/release_notes/sdk/enterprise/ver_3_11/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

### AllegroAI 3.11.1 [​](https://clear.ml/docs/latest/docs/release_notes/sdk/enterprise/ver_3_11/\#allegroai-3111 "Direct link to AllegroAI 3.11.1")

**Bug Fix**

- Fix updating frames in `BulkContext` sometimes causes infinite recursion.

### AllegroAI 3.11.0 [​](https://clear.ml/docs/latest/docs/release_notes/sdk/enterprise/ver_3_11/\#allegroai-3110 "Direct link to AllegroAI 3.11.0")

**New Features and Improvements**

- Add `DataView.get_current_iteration()` that returns current iteration
- Add `DataView.set_initial_iteration()` to set initial iteration, instead of zero.
- Allow dataset version filtering by tags with `tags` parameter in `DatasetVersion.get_datasets()`
- Add `Task.remove_dataviews()` to delete dataviews from a task

**Bug Fixes**

- Fix frames that failed to upload still upload their metadata
- Fix SingleFrame registration to a DatasetVersion failing
- Fix `DataView.add_query`'s `queries` parameter does not accept the returned results of `DataView.get_queries`

- [AllegroAI 3.11.1](https://clear.ml/docs/latest/docs/release_notes/sdk/enterprise/ver_3_11/#allegroai-3111)
- [AllegroAI 3.11.0](https://clear.ml/docs/latest/docs/release_notes/sdk/enterprise/ver_3_11/#allegroai-3110)