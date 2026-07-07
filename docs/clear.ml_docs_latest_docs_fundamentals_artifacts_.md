---
url: "https://clear.ml/docs/latest/docs/fundamentals/artifacts/"
title: "Artifacts | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/fundamentals/artifacts/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

**Artifacts** are objects associated with ClearML [tasks](https://clear.ml/docs/latest/docs/fundamentals/task) that are logged to ClearML, so they can later be
easily accessed, modified, and used.

Task artifacts support built-in serialization for a wide range of object types, such as:

- Numpy arrays (`.npz`)
- Pandas DataFrames
- PIL images (converted to `.jpg`)
- Files and folders
- Python objects
- and more

ClearML also logs your tasks' input and output models as well as interim model checkpoints. Model artifacts also have
unique ClearML Model IDs (see [Models](https://clear.ml/docs/latest/docs/fundamentals/models)).

Artifacts allow you to:

- **Track Task Inputs**: Record non source-controlled data to reproduce your workflows.
- **Compare Outputs**: Easily access model snapshots.
- **Build Elaborate Workflows**: Implement pipelines by using the outputs of one task as inputs to another (e.g. a data
cleaning task logs its clean dataset for use by a subsequent training task).

## Logging Artifacts [​](https://clear.ml/docs/latest/docs/fundamentals/artifacts/\#logging-artifacts "Direct link to Logging Artifacts")

ClearML automatically logs artifacts created by popular frameworks, including TensorFlow and PyTorch. See [supported frameworks](https://clear.ml/docs/latest/docs/clearml_sdk/task_sdk#automatic-logging).

You can also log any other object using [`Task.upload_artifact()`](https://clear.ml/docs/latest/docs/references/sdk/task#upload_artifact). See
the [Artifacts Reporting](https://clear.ml/docs/latest/docs/guides/reporting/artifacts) example for details.

ClearML can be configured to upload artifacts to any supported types of storage, which include local and shared folders,
AWS S3 buckets, Google Cloud Storage, and Azure Storage (see [Storage](https://clear.ml/docs/latest/docs/integrations/storage)).

## Updating Artifacts Dynamically [​](https://clear.ml/docs/latest/docs/fundamentals/artifacts/\#updating-artifacts-dynamically "Direct link to Updating Artifacts Dynamically")

Clearml can automatically update artifacts as their contents change while your task is running through the use of
[`register_artifact()`](https://clear.ml/docs/latest/docs/references/sdk/task#register_artifact).

## Accessing Artifacts [​](https://clear.ml/docs/latest/docs/fundamentals/artifacts/\#accessing-artifacts "Direct link to Accessing Artifacts")

Task artifacts can be accessed by other tasks. To use an artifact, first retrieve the `Task` that created it. Then use
one of the following methods:

- `get_local_copy()`: Caches the file for later use and returns its path.
- `get()`: Directly retrieves the Python object associated with the artifact.

For more information, see [Using Artifacts](https://clear.ml/docs/latest/docs/clearml_sdk/task_sdk#using-artifacts).

## WebApp Interface [​](https://clear.ml/docs/latest/docs/fundamentals/artifacts/\#webapp-interface "Direct link to WebApp Interface")

Artifacts appear under the **ARTIFACTS** tab of a Task. Each artifact's location is displayed in the **FILE PATH** field:

- **Locally stored artifacts**: Include an option to copy the artifact’s location for accessibility (since web
applications are prohibited from accessing the local disk for security reasons)
- **Network stored artifacts**: Display a download action to retrieve files from URLs (e.g., `https://`, `s3://`).

![WebApp Artifacts section](https://clear.ml/docs/latest/assets/images/webapp_tracking_30-768137fdcb284d1b88464da5d487e2db.png#light-mode-only)![WebApp Artifacts section](https://clear.ml/docs/latest/assets/images/webapp_tracking_30_dark-6173f2824ef1c8269535afd7ca3c291a.png#dark-mode-only)

## SDK Interface [​](https://clear.ml/docs/latest/docs/fundamentals/artifacts/\#sdk-interface "Direct link to SDK Interface")

See the [Artifacts](https://clear.ml/docs/latest/docs/clearml_sdk/task_sdk#artifacts) section in the Task SDK page for an overview of how to work
with ClearML Artifacts using Pythonic methods.

- [Logging Artifacts](https://clear.ml/docs/latest/docs/fundamentals/artifacts/#logging-artifacts)
- [Updating Artifacts Dynamically](https://clear.ml/docs/latest/docs/fundamentals/artifacts/#updating-artifacts-dynamically)
- [Accessing Artifacts](https://clear.ml/docs/latest/docs/fundamentals/artifacts/#accessing-artifacts)
- [WebApp Interface](https://clear.ml/docs/latest/docs/fundamentals/artifacts/#webapp-interface)
- [SDK Interface](https://clear.ml/docs/latest/docs/fundamentals/artifacts/#sdk-interface)