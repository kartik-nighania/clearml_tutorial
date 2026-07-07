---
url: "https://clear.ml/docs/latest/docs/hyper_datasets/"
title: "Hyper-Datasets | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/hyper_datasets/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

Enterprise Feature

Hyper-Datasets are available under the ClearML Enterprise plan.

10 - Hyperdatasets Data Versioning - YouTube

Tap to unmute

[10 - Hyperdatasets Data Versioning](https://www.youtube.com/watch?v=1VliYRexeLU) [ClearML](https://www.youtube.com/channel/UCDYdA4hjckRLRVBrCoKenCQ)

ClearML2.62K subscribers

ClearML's **Hyper-Datasets** are an MLOps-oriented abstraction of your data, which facilitates traceable, reproducible model development
through parameterized data access and metadata version control.

Hyper-Datasets is a data management system specifically tailored for handling unstructured data, like text, audio, or
visual data. You can create, manage, and version your datasets. Datasets can be set up to inherit from other datasets, so
data lineages can be created, and users can track when and how their data changes. In the ClearML Enterprise's [WebApp](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets),
you can view a dataset's version history, as well as its contents, including annotations, metadata, masks, and other
information.

![Frame viewer](https://clear.ml/docs/latest/assets/images/dataset_example_frame_editor-f21f0a5ec1a1856d17c32a12bfc52d20.png#light-mode-only)![Frame viewer](https://clear.ml/docs/latest/assets/images/dataset_example_frame_editor_dark-e37a13d3db5716f1ddc8ef0eb2d86b22.png#dark-mode-only)

The basic premise of Hyper-Datasets is that a user-formed query is a full representation of the dataset used by the ML/DL
process. Hyper-Datasets decouple metadata from raw data files, allowing you to manipulate metadata through sophisticated
queries and parameters that can be tracked through the task manager. You can clone tasks using different
data manipulations--or [**DataViews**](https://clear.ml/docs/latest/docs/hyperdatasets/dataviews)--without changing any of the hard coded values, making these manipulations part of
the task.

ClearML **Enterprise**'s Hyper-Datasets supports rapid prototyping, creating new opportunities such as:

- Hyperparameter optimization of the data itself
- QA/QC pipelining
- CD/CT (continuous training) during deployment
- Enabling complex applications like collaborative (federated) learning.

For more information, see [Hyper-Datasets](https://clear.ml/docs/latest/docs/hyperdatasets/overview).