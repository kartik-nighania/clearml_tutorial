---
url: "https://clear.ml/docs/latest/docs/references/hpd_overview/"
title: "Hyper-Datasets | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/hpd_overview/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

Enterprise Feature

Hyper-Datasets are available under the ClearML Enterprise plan.

The ClearML Hyper-Datasets SDK interface is provided through:

- Main interface: `clearml` Python package (as of v2.1.0)
- Legacy interface: `allegroai` Python package

Both packages provide a programmatic interface for ClearML's Hyper-Datasets, albeit through a slightly different class hierarchy.

## clearml ≥ 2.1 [​](https://clear.ml/docs/latest/docs/references/hpd_overview/\#clearml--21 "Direct link to clearml ≥ 2.1")

Starting with version 2.1, the `clearml` Python package provides the following interface for Hyper-Datasets:

- [**HyperDataset**](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdataset) \- Handle to a specific Dataset version, used for adding new data and performing queries like vector search
- [**HyperDatasetManagement**](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdatasetmanagement) \- Management operations for Hyper-Datasets (e.g. listing, fetching, and deleting)
- [**DataEntry**](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentry) \- Logical unit of data. It contains one or more DataSubEntry objects
- [**DataSubEntry**](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentry) \- Represents a source file within a `DataEntry`
- [**DataEntryImage**](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataentryimage) \- Image-specific `DataEntry` implementation, providing image-oriented metadata and access patterns.
- [**DataSubEntryImage**](https://clear.ml/docs/latest/docs/references/sdk/hpd_datasubentryimage) \- Image-specific sub-entry associated with a `DataEntryImage`
- [**DataView**](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataview) \- Defines how data is consumed and iterated over without modifying the underlying dataset
- [**HyperDatasetQuery**](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdatasetquery) \- Represents a single query or filter rule used to construct DataView objects across one or more dataset versions

## allegroai [​](https://clear.ml/docs/latest/docs/references/hpd_overview/\#allegroai "Direct link to allegroai")

Legacy Interface

The `allegroai` Python package is a legacy SDK that is maintained for backwards compatibility.
Users are urged to move to newer versions of the `clearml` Python package.

The `allegroai` Python package provides the following interface for Hyper-Datasets:

- [**Dataset**](https://clear.ml/docs/latest/docs/references/hyperdataset/) \- Represents a Hyper-Dataset and provides access to its versions and metadata
- [**DatasetVersion**](https://clear.ml/docs/latest/docs/references/hyperdataset/hyperdatasetversion) \- A specific version of a Hyper-Dataset, containing frames and annotations
- [**SingleFrame**](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe) \- The basic units of data within a dataset version. For example, one image
- [**FrameGroup**](https://clear.ml/docs/latest/docs/references/hyperdataset/framegroup) \- A collection of multiple frames such as multiple image sources at the same point in time
- [**Annotation**](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation) \- Annotation data associated with frames, such as ROIs or frame labels
- [**DataView**](https://clear.ml/docs/latest/docs/references/hyperdataset/dataview) \- Filtered view over dataset frames, enabling iteration over a subset of the data

- [clearml ≥ 2.1](https://clear.ml/docs/latest/docs/references/hpd_overview/#clearml--21)
- [allegroai](https://clear.ml/docs/latest/docs/references/hpd_overview/#allegroai)