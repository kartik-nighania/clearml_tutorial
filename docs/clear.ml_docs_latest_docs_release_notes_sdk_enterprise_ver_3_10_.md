---
url: "https://clear.ml/docs/latest/docs/release_notes/sdk/enterprise/ver_3_10/"
title: "Version 3.10 | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/release_notes/sdk/enterprise/ver_3_10/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

### AllegroAI 3.10.2 [​](https://clear.ml/docs/latest/docs/release_notes/sdk/enterprise/ver_3_10/\#allegroai-3102 "Direct link to AllegroAI 3.10.2")

**Bug Fixes**

- Fix duplicate frame registration changes the source URI for HyperDatasets
- Fix incorrect mask ID is provided when creating an annotation with an RoiMask
- Fix passing Iterable objects raises a subscript exception when being used in `_to_api_object`
- Fix SingleFrame annotation of type mask\_rgb does not contain the correct mask ID

### AllegroAI 3.10.1 [​](https://clear.ml/docs/latest/docs/release_notes/sdk/enterprise/ver_3_10/\#allegroai-3101 "Direct link to AllegroAI 3.10.1")

**New Features**

- Use ClearML 1.13.0 SDK

**Bug Fixes**

- Fix requirements conflict with ClearML SDK requirements (upper limit constraints removed)
- Fix deprecated login service support causes exception when loading `APIClient()`

### AllegroAI 3.10.0 [​](https://clear.ml/docs/latest/docs/release_notes/sdk/enterprise/ver_3_10/\#allegroai-3100 "Direct link to AllegroAI 3.10.0")

**New Feature**

- `Dataset.project` property for Hyperdataset project ID.

**Bug Fixes**

- Fix `allegroai.CachedStorageHelper` and `clearml.StorageHelper` compatibility
- Fix `DatasetVersion.update_frames()` doesn't update metadata when keys are removed
- Fix `DataView.Store()` raises errors
- Fix UI DataView frame query values are not applied at runtime.

- [AllegroAI 3.10.2](https://clear.ml/docs/latest/docs/release_notes/sdk/enterprise/ver_3_10/#allegroai-3102)
- [AllegroAI 3.10.1](https://clear.ml/docs/latest/docs/release_notes/sdk/enterprise/ver_3_10/#allegroai-3101)
- [AllegroAI 3.10.0](https://clear.ml/docs/latest/docs/release_notes/sdk/enterprise/ver_3_10/#allegroai-3100)