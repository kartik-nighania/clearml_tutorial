---
url: "https://clear.ml/docs/latest/docs/hyperdatasets/frames/"
title: "Frames Overview | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/hyperdatasets/frames/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

The concept of a **Frame** represents the basic building block of data in ClearML Enterprise.

Two types of frames are supported:

- [SingleFrames](https://clear.ml/docs/latest/docs/hyperdatasets/single_frames) \- A frame with one source. For example, one image.
- [FrameGroups](https://clear.ml/docs/latest/docs/hyperdatasets/frame_groups) \- A frame with multiple sources. For example, multiple images.

**SingleFrames** and **FrameGroups** contain data sources, metadata, and other data. A Frame can be added to [Datasets](https://clear.ml/docs/latest/docs/hyperdatasets/dataset)
and then modified or removed. [Versions](https://clear.ml/docs/latest/docs/hyperdatasets/dataset#dataset-versioning) of the Datasets can be created, which enables
documenting changes and reproducing data for tasks.