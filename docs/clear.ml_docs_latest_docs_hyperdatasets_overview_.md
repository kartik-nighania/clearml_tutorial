---
url: "https://clear.ml/docs/latest/docs/hyperdatasets/overview/"
title: "Hyper-Datasets | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/hyperdatasets/overview/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

Enterprise Feature

Hyper-Datasets are available under the ClearML Enterprise plan.

ClearML's Hyper-Datasets are an MLOps-oriented abstraction of your data, which facilitates traceable, reproducible model development
through parameterized data access and meta-data version control.

The basic premise is that a user-formed query is a full representation of the dataset used by the ML/DL process.

ClearML **Enterprise**'s Hyper-Datasets supports rapid prototyping, creating new opportunities such as:

- Hyperparameter optimization of the data itself
- QA/QC pipelining
- CD/CT (continuous training) during deployment
- Enabling complex applications like collaborative (federated) learning.

## Hyper-Dataset Components [​](https://clear.ml/docs/latest/docs/hyperdatasets/overview/\#hyper-dataset-components "Direct link to Hyper-Dataset Components")

A Hyper-Dataset is composed of the following components:

- [Frames](https://clear.ml/docs/latest/docs/hyperdatasets/frames)
  - [SingleFrames](https://clear.ml/docs/latest/docs/hyperdatasets/single_frames)
  - [FrameGroups](https://clear.ml/docs/latest/docs/hyperdatasets/frame_groups)
- [Datasets and Dataset Versions](https://clear.ml/docs/latest/docs/hyperdatasets/dataset)
- [Dataviews](https://clear.ml/docs/latest/docs/hyperdatasets/dataviews)

These components interact in a way that enables revising data and tracking and accessing all of its versions.

Frames are the basic units of data in ClearML Enterprise. SingleFrames and FrameGroups make up a Dataset version.
Dataset versions can be created, modified, and removed. The different versions are recorded and available,
so tasks, and their data are reproducible and traceable.

Lastly, Dataviews manage views of the dataset with queries, so a task's input data can be defined from a
subset of a Dataset or combinations of Datasets.

- [Hyper-Dataset Components](https://clear.ml/docs/latest/docs/hyperdatasets/overview/#hyper-dataset-components)