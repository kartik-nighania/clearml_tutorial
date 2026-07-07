---
url: "https://clear.ml/docs/latest/docs/hyperdatasets/code_examples/"
title: "Code Examples | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/hyperdatasets/code_examples/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The following examples demonstrate registering, retrieving, and ingesting your data through the Hyper-Datasets Python
interface.

## Registering your Data [​](https://clear.ml/docs/latest/docs/hyperdatasets/code_examples/\#registering-your-data "Direct link to Registering your Data")

- [register\_dataset\_with\_roi.py](https://github.com/clearml/clearml/blob/master/examples/hyperdatasets/legacy/data-registration/register_dataset_with_roi.py) \- Demonstrates
creating a new DatasetVersion and adding to it frames, supporting ROI annotations and metadata
- [register\_dataset\_masks.py](https://github.com/clearml/clearml/blob/master/examples/hyperdatasets/legacy/data-registration/register_dataset_masks.py) \- Demonstrates
creating a new DatasetVersion and adding to it frames containing masks. This example also demonstrates the
DatasetVersion-level [pixel segmentation masks](https://clear.ml/docs/latest/docs/hyperdatasets/masks#pixel-segmentation-masks).

After executing either of these scripts, you can view your DatasetVersion contents and details in the UI.

## Using your Data [​](https://clear.ml/docs/latest/docs/hyperdatasets/code_examples/\#using-your-data "Direct link to Using your Data")

### Dataviews [​](https://clear.ml/docs/latest/docs/hyperdatasets/code_examples/\#dataviews "Direct link to Dataviews")

The [dataview\_example\_framegroup.py](https://github.com/clearml/clearml/blob/master/examples/hyperdatasets/legacy/data-ingestion/dataview_example_framegroup.py)
and [dataview\_example\_singleframe.py](https://github.com/clearml/clearml/blob/master/examples/hyperdatasets/legacy/data-ingestion/dataview_example_singleframe.py)
examples demonstrate how to use a [DataView](https://clear.ml/docs/latest/docs/hyperdatasets/dataviews) to retrieve your data as SingleFrames and FrameGroups as
part of a running task. This is done by creating a DataView query and then retrieving the corresponding frames.

DataView details are displayed in the UI in a task's **DATAVIEWS** tab.

### Data Ingestion [​](https://clear.ml/docs/latest/docs/hyperdatasets/code_examples/\#data-ingestion "Direct link to Data Ingestion")

The [pytorch\_dataset\_example.py](https://github.com/clearml/clearml/blob/master/examples/hyperdatasets/legacy/data-ingestion/pytorch_dataset_example.py)
example demonstrates how to feed your DataViews to an ML framework by creating a DataView query and wrapping it as a
PyTorch Dataset.

The [pytorch\_dataset\_example\_with\_masks.py](https://github.com/clearml/clearml/blob/master/examples/hyperdatasets/legacy/data-ingestion/pytorch_dataset_example_with_masks.py)
example demonstrates the additional actions required when your frames contain masks.

- [Registering your Data](https://clear.ml/docs/latest/docs/hyperdatasets/code_examples/#registering-your-data)
- [Using your Data](https://clear.ml/docs/latest/docs/hyperdatasets/code_examples/#using-your-data)
  - [Dataviews](https://clear.ml/docs/latest/docs/hyperdatasets/code_examples/#dataviews)
  - [Data Ingestion](https://clear.ml/docs/latest/docs/hyperdatasets/code_examples/#data-ingestion)