---
url: "https://clear.ml/docs/latest/docs/references/sdk/model_model/"
title: "Model | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/sdk/model_model/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

## _class_ Model(model\_id) [​](https://clear.ml/docs/latest/docs/references/sdk/model_model/\#class-modelmodel_id "Direct link to class-modelmodel_id")

A read-only representation of an existing model, looked up by ID.
Can be connected to a Task to pre-initialize a network.
When running remotely, the model can be overridden via the UI.

- **Parameters**

**model\_id** (`str`) – The ID (system UUID) of the model.


* * *

### archive [​](https://clear.ml/docs/latest/docs/references/sdk/model_model/\#archive "Direct link to archive")

**archive()**

Archive the model. If the model is already archived, this is a no-op

- **Return type**

`None`


* * *

### comment [​](https://clear.ml/docs/latest/docs/references/sdk/model_model/\#comment "Direct link to comment")

**property comment: str**

A description of the model.

- **Return type**

`str`

- **Returns**

The model description.


* * *

### config\_dict [​](https://clear.ml/docs/latest/docs/references/sdk/model_model/\#config_dict "Direct link to config_dict")

**property config\_dict: dict**

The configuration as a dictionary, parsed from the design text. This usually represents the model configuration.
For example, prototxt, a `.ini` file, or Python code to evaluate.

- **Return type**

`dict`

- **Returns**

The configuration.


* * *

### config\_text [​](https://clear.ml/docs/latest/docs/references/sdk/model_model/\#config_text "Direct link to config_text")

**property config\_text: str**

The configuration as a string. For example, prototxt, a `.ini` file, or Python code to evaluate.

- **Return type**

`str`

- **Returns**

The configuration.


* * *

### framework [​](https://clear.ml/docs/latest/docs/references/sdk/model_model/\#framework "Direct link to framework")

**property framework: str**

The ML framework of the model (for example: PyTorch, TensorFlow, XGBoost, etc.).

- **Return type**

`str`

- **Returns**

The model’s framework


* * *

### get\_all\_metadata [​](https://clear.ml/docs/latest/docs/references/sdk/model_model/\#get_all_metadata "Direct link to get_all_metadata")

**get\_all\_metadata()**

Returns all metadata as a `Dict[key, Dict[value, type]]`,
where `key`, `value`, and `type` are all strings.
To get values cast to their original types (if possible), use `Model.get_all_metadata_casted`.

- **Return type**

`Dict`\[`str`, `Dict`\[`str`, `str`\]\]

- **Returns**

All metadata in `Dict[key, Dict[value, type]]` format.


* * *

### get\_all\_metadata\_casted [​](https://clear.ml/docs/latest/docs/references/sdk/model_model/\#get_all_metadata_casted "Direct link to get_all_metadata_casted")

**get\_all\_metadata\_casted()**

Returns all metadata as a `Dict[key, Dict[value, type]]`,
where `key` and `type` are strings, and `value` is cast to its original type where possible.
To get all values as strings, use `Model.get_all_metadata`.

- **Return type**

`Dict`\[`str`, `Dict`\[`str`, `Any`\]\]

- **Returns**

All metadata in `Dict[key, Dict[value, type]]` format.


* * *

### get\_local\_copy [​](https://clear.ml/docs/latest/docs/references/sdk/model_model/\#get_local_copy "Direct link to get_local_copy")

**get\_local\_copy(extract\_archive=None, raise\_on\_error=False, force\_download=False)**

Retrieve a valid link to the model file(s).
If the model URL is a file system link, it will be returned directly.
If the model URL points to a remote location (`http`, `s3`, `gs`, etc.),
it will download the file(s) and return the temporary location of the downloaded model.

- **Parameters**
  - **extract\_archive** (`Optional`\[`bool`\]) – If `True`, extract the local copy if possible.
    If `None` (default), then extract the downloaded file only if the model is a package.

  - **raise\_on\_error** (`bool`) – If `True`, raise `ValueError` if the artifact download fails.

  - **force\_download** (`bool`) – If `True`, re-download model artifact even if a cached copy exists.
- **Return type**

`str`

- **Returns**

A local path to the model (or a downloaded copy of it).


* * *

### get\_metadata [​](https://clear.ml/docs/latest/docs/references/sdk/model_model/\#get_metadata "Direct link to get_metadata")

**get\_metadata(key)**

Get one metadata entry value (as a string) based on its key. See `Model.get_metadata_casted`
if you wish to cast the value to its type (if possible).

- **Parameters**

**key** (`str`) – Key of the metadata entry you want to get.

- **Return type**

`Optional`\[`str`\]

- **Returns**

String representation of the value of the metadata entry or `None` if the entry was not found


* * *

### get\_metadata\_casted [​](https://clear.ml/docs/latest/docs/references/sdk/model_model/\#get_metadata_casted "Direct link to get_metadata_casted")

**get\_metadata\_casted(key)**

Get one metadata entry based on its key, casted to its type if possible.

- **Parameters**

**key** (`str`) – Key of the metadata entry you want to get.

- **Return type**

`Optional`\[`str`\]

- **Returns**

The value of the metadata entry, casted to its type (if not possible,
the string representation will be returned) or `None` if the entry was not found


* * *

### get\_weights [​](https://clear.ml/docs/latest/docs/references/sdk/model_model/\#get_weights "Direct link to get_weights")

**get\_weights(raise\_on\_error=False, force\_download=False, extract\_archive=False)**

Download the base model and return the locally stored filename.

- **Parameters**
  - **raise\_on\_error** (`bool`) – If `True`, raise `ValueError` if the artifact download fails.

  - **force\_download** (`bool`) – If `True`, re-download base model even if a cached copy exists.

  - **extract\_archive** (`bool`) – If `True`, extract the downloaded weights file if possible.
- **Return type**

`str`

- **Returns**

The locally stored file.


* * *

### get\_weights\_package [​](https://clear.ml/docs/latest/docs/references/sdk/model_model/\#get_weights_package "Direct link to get_weights_package")

**get\_weights\_package(return\_path=False, raise\_on\_error=False, force\_download=False, extract\_archive=True)**

Download the base model package into a temporary directory (extract the files), or return a list of the
locally stored filenames.

- **Parameters**
  - **return\_path** (`bool`) – If `True`, extract weights to a temp directory and return its path.
    If `False` (default), return a list of local file paths.

  - **raise\_on\_error** (`bool`) – If `True`, raise `ValueError` if the artifact download fails.
    If `False`, returns `None` and logs a warning.

  - **force\_download** (`bool`) – If `True`, re-download the base artifact even if a cached copy exists.

  - **extract\_archive** (`bool`) – If `True`, extract the downloaded weights file if possible.
- **Return type**

`Union`\[`str`, `List`\[`Path`\], `None`\]

- **Returns**

The model weights, or a list of the locally stored filenames.
If `raise_on_error=False`, returns `None` on error.


* * *

### id [​](https://clear.ml/docs/latest/docs/references/sdk/model_model/\#id "Direct link to id")

**property id: str**

The ID (system UUID) of the model.

- **Return type**

`str`

- **Returns**

The model ID.


* * *

### labels [​](https://clear.ml/docs/latest/docs/references/sdk/model_model/\#labels "Direct link to labels")

**property labels: Dict\[str, int\]**

The label enumeration of string (label) to integer (value) pairs.

- **Return type**

`Dict`\[`str`, `int`\]

- **Returns**

A dictionary containing label enumeration, where the keys are labels and the values are integers.


* * *

### name [​](https://clear.ml/docs/latest/docs/references/sdk/model_model/\#name "Direct link to name")

**property name: str**

The name of the model.

- **Return type**

`str`

- **Returns**

The model name.


* * *

### original\_task [​](https://clear.ml/docs/latest/docs/references/sdk/model_model/\#original_task "Direct link to original_task")

**property original\_task: str**

Return the ID of the Task that created this model.

- **Return type**

`str`

- **Returns**

The Task ID


* * *

### project [​](https://clear.ml/docs/latest/docs/references/sdk/model_model/\#project "Direct link to project")

**property project: str**

Project ID of the model.

- **Return type**

`str`

- **Returns**

Project ID


* * *

### publish [​](https://clear.ml/docs/latest/docs/references/sdk/model_model/\#publish "Direct link to publish")

**publish()**

Set the model to the status `published` and for public use. If the model’s status is already `published`,
then this method is a no-op.

- **Return type**

`None`


* * *

### published [​](https://clear.ml/docs/latest/docs/references/sdk/model_model/\#published "Direct link to published")

**property published: bool**

Get the published state of this model.

- **Return type**

`bool`

- **Returns**

`True` if the model is published, `False` otherwise.


* * *

### Model.query\_models [​](https://clear.ml/docs/latest/docs/references/sdk/model_model/\#modelquery_models "Direct link to Model.query_models")

**_classmethod_ query\_models(project\_name=None, model\_name=None, tags=None, only\_published=False, include\_archived=False, max\_results=None, metadata=None)**

Query the model artifactory based on project name / model name / tags.
Results are sorted by last updated, most recent first.

- **Parameters**


  - **project\_name** (`Optional`\[`str`\]) – Filter by project name string. If not provided, queries across all projects.

  - **model\_name** (`Optional`\[`str`\]) – Filter by model name as shown in the artifactory.

  - **tags** (`Optional`\[`Sequence`\[`str`\]\]) – Filter by a list of tags (strings).
    To exclude a tag add “-” prefix to the tag. Example: `["production", "verified", "-qa"]`.
    The default behaviour is to join all tags with a logical “OR” operator.
    To join all tags with a logical “AND” operator instead, use “\_\_$all” as the first string, for example:


```py
["__$all", "best", "model", "ever"]
```

To join all tags with AND, but exclude a tag use “\_\_$not” before the excluded tag, for example:

```py
["__$all", "best", "model", "ever", "__$not", "internal", "__$not", "test"]
```

The “OR” and “AND” operators apply to all tags that follow them until another operator is specified.
The NOT operator applies only to the immediately following tag.
For example:

```py
["__$all", "a", "b", "c", "__$or", "d", "__$not", "e", "__$and", "__$or", "f", "g"]
```

This example means (“a” AND “b” AND “c” AND (“d” OR NOT “e”) AND (“f” OR “g”)).
See [https://clear.ml/docs/latest/docs/clearml\_sdk/model\_sdk#tag-filters](https://clear.ml/docs/latest/docs/clearml_sdk/model_sdk#tag-filters) for details.
  - **only\_published** (`bool`) – If `True`, return only published models. Defaults to `False`.

  - **include\_archived** (`bool`) – If `True`, include archived models in results. Defaults to `False`.

  - **max\_results** (`Optional`\[`int`\]) – Maximum number of models to return.

  - **metadata** (`Optional`\[`Dict`\[`str`, `str`\]\]) – Filter by metadata key-value pairs.
- **Return type**

`List`\[`Model`\]

- **Returns**

List of Model objects


* * *

### Model.remove [​](https://clear.ml/docs/latest/docs/references/sdk/model_model/\#modelremove "Direct link to Model.remove")

**_classmethod_ remove(model, delete\_weights\_file=True, force=False, raise\_on\_errors=False)**

Remove a model from the model artifactory, and optionally delete its weights file from remote storage.

- **Parameters**
  - **model** (`Union`\[`str`, `Model`\]) – Model ID or Model object to remove.

  - **delete\_weights\_file** (`bool`) – If `True` (default), delete the weights file from the remote storage.

  - **force** (`bool`) – If `True`, remove model even if other Tasks are using this model. Defaults to `False`.

  - **raise\_on\_errors** (`bool`) – If `True`, raise `ValueError` if something went wrong. Defaults to `False`.
- **Return type**

`bool`

- **Returns**

`True` if model was removed successfully.
Partial removal returns `False`, i.e. model was deleted but weights file deletion failed.


* * *

### report\_confusion\_matrix [​](https://clear.ml/docs/latest/docs/references/sdk/model_model/\#report_confusion_matrix "Direct link to report_confusion_matrix")

**report\_confusion\_matrix(title, series, matrix, iteration=None, xaxis=None, yaxis=None, xlabels=None, ylabels=None, yaxis\_reversed=False, comment=None, extra\_layout=None)**

Plot a heat-map matrix.

For example:

```py
confusion = np.random.randint(10, size=(10, 10))

model.report_confusion_matrix(

    "example confusion matrix",

    "ignored",

    iteration=1,

    matrix=confusion,

    xaxis="title X",

    yaxis="title Y",

)
```

- **Parameters**
  - **title** (`str`) – Plot title (metric).

  - **series** (`str`) – Series name (variant).

  - **matrix** (`ndarray`) – A heat-map matrix (example: confusion matrix).

  - **iteration** (`Optional`\[`int`\]) – The reported iteration / step.

  - **xaxis** (`Optional`\[`str`\]) – The x-axis title.

  - **yaxis** (`Optional`\[`str`\]) – The y-axis title.

  - **xlabels** (`Optional`\[`List`\[`str`\]\]) – Labels for each column of the matrix.

  - **ylabels** (`Optional`\[`List`\[`str`\]\]) – Labels for each row of the matrix.

  - **yaxis\_reversed** (`bool`) – If set to `False`, the `(0, 0)` coordinate is at the bottom left corner.
    If set to `True`, the `(0, 0)` coordinate is at the top left corner.

  - **comment** (`Optional`\[`str`\]) – A comment displayed with the plot, underneath the title.

  - **extra\_layout** (`Optional`\[`dict`\]) – Optional dictionary for layout configuration, passed directly to `plotly`.
    See full details on the supported configuration: [https://plotly.com/javascript/reference/heatmap/](https://plotly.com/javascript/reference/heatmap/).
    Example: `extra_layout={'xaxis': {'type': 'date', 'range': ['2020-01-01', '2020-01-31']}}`
- **Return type**

`None`


* * *

### report\_histogram [​](https://clear.ml/docs/latest/docs/references/sdk/model_model/\#report_histogram "Direct link to report_histogram")

**report\_histogram(title, series, values, iteration=None, labels=None, xlabels=None, xaxis=None, yaxis=None, mode=None, data\_args=None, extra\_layout=None)**

Plot a (default grouped) histogram.
Notice this function will not calculate the histogram,
it assumes the histogram was already calculated in `values`.

For example:

```py
vector_series = np.random.randint(10, size=10).reshape(2,5)

model.report_histogram(

    title='histogram example',

    series='histogram series',

    values=vector_series,

    iteration=0,

    labels=['A','B'],

    xaxis='X axis label',

    yaxis='Y axis label',

)
```

- **Parameters**
  - **title** (`str`) – Plot title (metric).

  - **series** (`str`) – Series name (variant).

  - **values** (`Sequence`\[`Union`\[`int`, `float`\]\]) – The series values. A list of floats, or an `N`-dimensional Numpy array containing
    data for each histogram bar.

  - **iteration** (`Optional`\[`int`\]) – The reported iteration / step. Each `iteration` creates another plot.

  - **labels** (`Optional`\[`List`\[`str`\]\]) – Labels for each bar group, creating a plot legend labeling each series.

  - **xlabels** (`Optional`\[`List`\[`str`\]\]) – Labels per entry in each bucket in the histogram (vector), creating a set of labels
    for each histogram bar on the x-axis.

  - **xaxis** (`Optional`\[`str`\]) – The x-axis title.

  - **yaxis** (`Optional`\[`str`\]) – The y-axis title.

  - **mode** (`Optional`\[`str`\]) – Display mode for multiple histograms. The options are:
    - `group` (default)

    - `stack`

    - `relative`
  - **data\_args** (`Optional`\[`dict`\]) – Optional dictionary for data configuration passed directly to `plotly`.
    See full details on the supported configuration: [https://plotly.com/javascript/reference/bar/](https://plotly.com/javascript/reference/bar/).
    Example: `data_args={'orientation': 'h', 'marker': {'color': 'blue'}}`

  - **extra\_layout** (`Optional`\[`dict`\]) – Optional dictionary for layout configuration, passed directly to `plotly`.
    See full details on the supported configuration: [https://plotly.com/javascript/reference/bar/](https://plotly.com/javascript/reference/bar/).
    Example: `extra_layout={'xaxis': {'type': 'date', 'range': ['2020-01-01', '2020-01-31']}}`
- **Return type**

`None`


* * *

### report\_line\_plot [​](https://clear.ml/docs/latest/docs/references/sdk/model_model/\#report_line_plot "Direct link to report_line_plot")

**report\_line\_plot(title, series, xaxis, yaxis, mode='lines', iteration=None, reverse\_xaxis=False, comment=None, extra\_layout=None)**

Plot one or more series as lines.

- **Parameters**
  - **title** (`str`) – Plot title (metric).

  - **series** (`Sequence`\[`SeriesInfo`\]) – All the series data, one list element for each line in the plot.

  - **iteration** (`Optional`\[`int`\]) – The reported iteration / step.

  - **xaxis** (`str`) – The x-axis title.

  - **yaxis** (`str`) – The y-axis title.

  - **mode** (`str`) – The type of line plot. The options are: `lines` (default), `markers`, `lines+markers`.

  - **reverse\_xaxis** (`bool`) – If `True`, reverse the x-axis (high to low). Defaults to `False`.

  - **comment** (`Optional`\[`str`\]) – A comment displayed underneath the plot title.

  - **extra\_layout** (`Optional`\[`dict`\]) – Dictionary for layout configuration, passed directly to `plotly`.
    See full details on the supported configuration: [https://plotly.com/javascript/reference/scatter/](https://plotly.com/javascript/reference/scatter/).
    Example: `extra_layout={'xaxis': {'type': 'date', 'range': ['2020-01-01', '2020-01-31']}}`
- **Return type**

`None`


* * *

### report\_matrix [​](https://clear.ml/docs/latest/docs/references/sdk/model_model/\#report_matrix "Direct link to report_matrix")

**report\_matrix(title, series, matrix, iteration=None, xaxis=None, yaxis=None, xlabels=None, ylabels=None, yaxis\_reversed=False, extra\_layout=None)**

Plot a confusion matrix.

info

This method is the same as `Model.report_confusion_matrix`.

- **Parameters**
  - **title** (`str`) – Plot title (metric).

  - **series** (`str`) – Series name (variant).

  - **matrix** (`ndarray`) – A heat-map matrix (example: confusion matrix).

  - **iteration** (`Optional`\[`int`\]) – The reported iteration / step.

  - **xaxis** (`Optional`\[`str`\]) – The x-axis title.

  - **yaxis** (`Optional`\[`str`\]) – The y-axis title.

  - **xlabels** (`Optional`\[`List`\[`str`\]\]) – Labels for each column of the matrix.

  - **ylabels** (`Optional`\[`List`\[`str`\]\]) – Labels for each row of the matrix.

  - **yaxis\_reversed** (`bool`) – If set to `False`, the `(0, 0)` coordinate is at the bottom left corner.
    If set to `True`, the `(0, 0)` coordinate is at the top left corner.

  - **extra\_layout** (`Optional`\[`dict`\]) – Dictionary for layout configuration, passed directly to `plotly`.
    See full details on the supported configuration: [https://plotly.com/javascript/reference/heatmap/](https://plotly.com/javascript/reference/heatmap/).
    Example: `extra_layout={'xaxis': {'type': 'date', 'range': ['2020-01-01', '2020-01-31']}}`
- **Return type**

`None`


* * *

### report\_scalar [​](https://clear.ml/docs/latest/docs/references/sdk/model_model/\#report_scalar "Direct link to report_scalar")

**report\_scalar(title, series, value, iteration)**

Plot a scalar series.

- **Parameters**
  - **title** (`str`) – Plot title (metric). Plot more than one scalar series on the same plot by using
    the same `title` for each call to this method.

  - **series** (`str`) – Series name (variant).

  - **value** (`float`) – The value to plot per iteration.

  - **iteration** (`int`) – The reported iteration / step (x-axis of the reported time series)
- **Return type**

`None`


* * *

### report\_scatter2d [​](https://clear.ml/docs/latest/docs/references/sdk/model_model/\#report_scatter2d "Direct link to report_scatter2d")

**report\_scatter2d(title, series, scatter, iteration=None, xaxis=None, yaxis=None, labels=None, mode='line', comment=None, extra\_layout=None)**

Report a 2D scatter plot.

For example:

```py
scatter2d = np.hstack((

    np.atleast_2d(np.arange(0, 10)).T,

    np.random.randint(10, size=(10, 1))

))

model.report_scatter2d(

    title="example_scatter",

    series="series",

    iteration=0,

    scatter=scatter2d,

    xaxis="title x",

    yaxis="title y",

)
```

Plot multiple 2D scatter series on the same plot by passing the same `title` and `iteration` values
to this method:

```py
scatter2d_1 = np.hstack((

    np.atleast_2d(np.arange(0, 10)).T,

    np.random.randint(10, size=(10, 1))

))

model.report_scatter2d(

    title="example_scatter",

    series="series_1",

    iteration=1,

    scatter=scatter2d_1,

    xaxis="title x",

    yaxis="title y",

)

scatter2d_2 = np.hstack((

    np.atleast_2d(np.arange(0, 10)).T,

    np.random.randint(10, size=(10, 1)),

))

model.report_scatter2d(

    "example_scatter",

    "series_2",

    iteration=1,

    scatter=scatter2d_2,

    xaxis="title x",

    yaxis="title y",

)
```

- **Parameters**
  - **title** (`str`) – Plot title (metric).

  - **series** (`str`) – Series name (variant) of the reported scatter plot.

  - **scatter** (`Union`\[`Sequence`\[`Tuple`\[`float`, `float`\]\], `ndarray`\]) – The scatter data. `numpy.ndarray` or list of (pairs of x,y) scatter.

  - **iteration** (`Optional`\[`int`\]) – The reported iteration / step.

  - **xaxis** (`Optional`\[`str`\]) – The x-axis title.

  - **yaxis** (`Optional`\[`str`\]) – The y-axis title.

  - **labels** (`Optional`\[`List`\[`str`\]\]) – Labels per point in the data assigned to the `scatter` parameter. The labels must be
    in the same order as the data.

  - **mode** (`str`) – The type of scatter plot. The options are: `lines` (default), `markers`, `lines+markers`.

  - **comment** (`Optional`\[`str`\]) – A comment displayed with the plot, underneath the title.

  - **extra\_layout** (`Optional`\[`dict`\]) – Dictionary for layout configuration, passed directly to `plotly`.
    See full details on the supported configuration: [https://plotly.com/javascript/reference/scatter/](https://plotly.com/javascript/reference/scatter/).
    Example: `extra_layout={'xaxis': {'type': 'date', 'range': ['2020-01-01', '2020-01-31']}}`
- **Return type**

`None`


* * *

### report\_scatter3d [​](https://clear.ml/docs/latest/docs/references/sdk/model_model/\#report_scatter3d "Direct link to report_scatter3d")

**report\_scatter3d(title, series, scatter, iteration=None, xaxis=None, yaxis=None, zaxis=None, labels=None, mode='markers', fill=False, comment=None, extra\_layout=None)**

Plot a 3D scatter graph. For example:

```py
scatter3d = np.random.randint(10, size=(10, 3))

model.report_scatter3d(

    title="example_scatter_3d",

    series="series_xyz",

    iteration=1,

    scatter=scatter3d,

    xaxis="title x",

    yaxis="title y",

    zaxis="title z",

)
```

- **Parameters**
  - **title** (`str`) – Plot title (metric)

  - **series** (`str`) – Series name (variant)

  - **scatter** (`Union`\[`Sequence`\[`Tuple`\[`float`, `float`, `float`\]\], `ndarray`\]) – The scatter data as
    - a list of `(x,y,z)` tuples

    - a nested list `[[(x1,y1,z1)...]]`, or

    - a `numpy.ndarray`.
  - **iteration** (`Optional`\[`int`\]) – The reported iteration / step.

  - **xaxis** (`Optional`\[`str`\]) – The x-axis title.

  - **yaxis** (`Optional`\[`str`\]) – The y-axis title.

  - **zaxis** (`Optional`\[`str`\]) – The z-axis title.

  - **labels** (`Optional`\[`List`\[`str`\]\]) – Labels per point in the data assigned to the `scatter` parameter. The labels must be
    in the same order as the data.

  - **mode** (`str`) – The type of scatter plot. The options are: `markers` (default), `lines`, `lines+markers`.

  - **fill** (`bool`) – If `True`, fill the area under the curve. Defaults to `False`.

  - **comment** (`Optional`\[`str`\]) – A comment displayed underneath the plot title.

  - **extra\_layout** (`Optional`\[`dict`\]) – Dictionary for layout configuration passed directly to `plotly`.
    See full details on the supported configuration: [https://plotly.com/javascript/reference/scatter3d/](https://plotly.com/javascript/reference/scatter3d/).
    Example: `extra_layout={'xaxis': {'type': 'date', 'range': ['2020-01-01', '2020-01-31']}}`
- **Return type**

`None`


* * *

### report\_single\_value [​](https://clear.ml/docs/latest/docs/references/sdk/model_model/\#report_single_value "Direct link to report_single_value")

**report\_single\_value(name, value)**

Reports a single value metric (for example, total experiment accuracy or mAP)

- **Parameters**
  - **name** (`str`) – Metric’s name

  - **value** (`float`) – Metric’s value
- **Return type**

`None`


* * *

### report\_surface [​](https://clear.ml/docs/latest/docs/references/sdk/model_model/\#report_surface "Direct link to report_surface")

**report\_surface(title, series, matrix, iteration=None, xaxis=None, yaxis=None, zaxis=None, xlabels=None, ylabels=None, camera=None, comment=None, extra\_layout=None)**

Report a 3D surface plot.

info

This method plots the same data as `Model.report_confusion_matrix`, but presents the
data as a surface diagram not a confusion matrix.

```py
surface_matrix = np.random.randint(10, size=(10, 10))

model.report_surface(

    "example surface",

    "series",

    iteration=0,

    matrix=surface_matrix,

    xaxis="title X",

    yaxis="title Y",

    zaxis="title Z",

)
```

- **Parameters**
  - **title** (`str`) – Plot title (metric).

  - **series** (`str`) – Series name (variant).

  - **matrix** (`ndarray`) – A heat-map matrix (example: confusion matrix).

  - **iteration** (`Optional`\[`int`\]) – The reported iteration / step.

  - **xaxis** (`Optional`\[`str`\]) – The x-axis title.

  - **yaxis** (`Optional`\[`str`\]) – The y-axis title.

  - **zaxis** (`Optional`\[`str`\]) – The z-axis title.

  - **xlabels** (`Optional`\[`List`\[`str`\]\]) – Labels for each column of the matrix (optional).

  - **ylabels** (`Optional`\[`List`\[`str`\]\]) – Labels for each row of the matrix (optional).

  - **camera** (`Optional`\[`Sequence`\[`float`\]\]) – `(X,Y,Z)` coordinates indicating the camera position. The default value is `(1,1,1)`.

  - **comment** (`Optional`\[`str`\]) – A comment displayed underneath the plot title.

  - **extra\_layout** (`Optional`\[`dict`\]) – Dictionary for layout configuration passed directly to `plotly`.
    See full details on the supported configuration: [https://plotly.com/javascript/reference/surface/](https://plotly.com/javascript/reference/surface/).
    Example: `extra_layout={'xaxis': {'type': 'date', 'range': ['2020-01-01', '2020-01-31']}}`
- **Return type**

`None`


* * *

### report\_table [​](https://clear.ml/docs/latest/docs/references/sdk/model_model/\#report_table "Direct link to report_table")

**report\_table(title, series, iteration=None, table\_plot=None, csv=None, url=None, extra\_layout=None)**

Report a table plot.

One and only one of the following parameters must be provided.

- `table_plot` \- Pandas DataFrame or Table as list of rows (list)

- `csv` \- CSV file

- `url` \- URL to CSV file


For example:

```py
 df = pd.DataFrame(

     {

         'num_legs': [2, 4, 8, 0],

         'num_wings': [2, 0, 0, 0],

         'num_specimen_seen': [10, 2, 1, 8]

     },

     index=['falcon', 'dog', 'spider', 'fish'],

 )

model.report_table(title='table example', series='pandas DataFrame', iteration=0, table_plot=df)
```

- **Parameters**
  - **title** (`str`) – Table title (metric).

  - **series** (`str`) – Series name (variant).

  - **iteration** (`Optional`\[`int`\]) – The reported iteration / step.

  - **table\_plot** (`Union`\[`DataFrame`, `Sequence`\[`Sequence`\], `None`\]) – The output table plot object.

  - **csv** (`Optional`\[`str`\]) – Path to local CSV file.

  - **url** (`Optional`\[`str`\]) – A URL to the location of CSV file.

  - **extra\_layout** (`Optional`\[`Dict`\]) – Optional dictionary for layout configuration passed directly to `plotly`.
    See full details on the supported configuration: [https://plotly.com/javascript/reference/layout/](https://plotly.com/javascript/reference/layout/).
    Example: `extra_layout={'height': 600}`
- **Return type**

`None`


* * *

### report\_vector [​](https://clear.ml/docs/latest/docs/references/sdk/model_model/\#report_vector "Direct link to report_vector")

**report\_vector(title, series, values, iteration=None, labels=None, xlabels=None, xaxis=None, yaxis=None, mode=None, extra\_layout=None)**

Plot a vector as a (default stacked) histogram.

For example:

```py
vector_series = np.random.randint(10, size=10).reshape(2,5)

model.report_vector(

    title='vector example',

    series='vector series',

    values=vector_series,

    iteration=0,

    labels=['A','B'],

    xaxis='X axis label',

    yaxis='Y axis label',

)
```

- **Parameters**
  - **title** (`str`) – Plot title (metric).

  - **series** (`str`) – Series name (variant).

  - **values** (`Sequence`\[`Union`\[`int`, `float`\]\]) – Vector data as a list of floats or an N-dimensional Numpy array containing data
    for each histogram bar.

  - **iteration** (`Optional`\[`int`\]) – The reported iteration / step. Each `iteration` creates another plot.

  - **labels** (`Optional`\[`List`\[`str`\]\]) – Labels for each bar group, creating a plot legend labeling each series.

  - **xlabels** (`Optional`\[`List`\[`str`\]\]) – Labels per entry in each bucket in the histogram (vector), creating a set of labels
    for each histogram bar on the x-axis.

  - **xaxis** (`Optional`\[`str`\]) – The x-axis title.

  - **yaxis** (`Optional`\[`str`\]) – The y-axis title.

  - **mode** (`Optional`\[`str`\]) – Display mode for multiple histograms. The options are:
    - `group` (default)

    - `stack`

    - `relative`
  - **extra\_layout** (`Optional`\[`dict`\]) – Optional dictionary for layout configuration, passed directly to `plotly`.
    See full details on the supported configuration: [https://plotly.com/javascript/reference/layout/](https://plotly.com/javascript/reference/layout/).
    Example: `extra_layout={'showlegend': False, 'plot_bgcolor': 'yellow'}`
- **Return type**

`None`


* * *

### set\_all\_metadata [​](https://clear.ml/docs/latest/docs/references/sdk/model_model/\#set_all_metadata "Direct link to set_all_metadata")

**set\_all\_metadata(metadata, replace=True)**

Set metadata based on the given parameters. Allows replacing all entries or updating the current entries.

- **Parameters**
  - **metadata** (`Dict`\[`str`, `Dict`\[`str`, `str`\]\]) – A dictionary of format `Dict[key, Dict[value, type]]`
    representing the metadata you want to set.

  - **replace** (`bool`) – If `True`, replace all metadata with the entries in the `metadata` parameter.
    If `False`, keep the old metadata and update it with the entries in the `metadata` parameter
    (add or change it).
- **Return type**

`bool`

- **Returns**

`True` if the metadata was set and `False` otherwise


* * *

### set\_metadata [​](https://clear.ml/docs/latest/docs/references/sdk/model_model/\#set_metadata "Direct link to set_metadata")

**set\_metadata(key, value, v\_type=None)**

Set one metadata entry. All parameters must be strings or castable to strings.

- **Parameters**
  - **key** (`str`) – Key of the metadata entry.

  - **value** (`str`) – Value of the metadata entry.

  - **v\_type** (`Optional`\[`str`\]) – Type of the metadata entry.
- **Return type**

`bool`

- **Returns**

`True` if the metadata was set, `False` otherwise.


* * *

### system\_tags [​](https://clear.ml/docs/latest/docs/references/sdk/model_model/\#system_tags "Direct link to system_tags")

**property system\_tags: List\[str\]**

A list of system tags describing the model.

- **Return type**

`List`\[`str`\]

- **Returns**

The list of tags.


* * *

### tags [​](https://clear.ml/docs/latest/docs/references/sdk/model_model/\#tags "Direct link to tags")

**property tags: List\[str\]**

A list of tags describing the model.

- **Return type**

`List`\[`str`\]

- **Returns**

The list of tags.


* * *

### task [​](https://clear.ml/docs/latest/docs/references/sdk/model_model/\#task "Direct link to task")

**property task: str**

The ID of the task connected to this model. If no task is connected, returns the ID of the task that originally
created it.

- **Return type**

`str`

- **Returns**

The Task ID


* * *

### unarchive [​](https://clear.ml/docs/latest/docs/references/sdk/model_model/\#unarchive "Direct link to unarchive")

**unarchive()**

Unarchive the model. If the model is not archived, this is a no-op

- **Return type**

`None`


* * *

### url [​](https://clear.ml/docs/latest/docs/references/sdk/model_model/\#url "Direct link to url")

**property url: str**

Return the URL of the model file (or archived files)

- **Return type**

`str`

- **Returns**

The model file URL.


- [_class_ Model(model\_id)](https://clear.ml/docs/latest/docs/references/sdk/model_model/#class-modelmodel_id)
  - [archive](https://clear.ml/docs/latest/docs/references/sdk/model_model/#archive)
  - [comment](https://clear.ml/docs/latest/docs/references/sdk/model_model/#comment)
  - [config\_dict](https://clear.ml/docs/latest/docs/references/sdk/model_model/#config_dict)
  - [config\_text](https://clear.ml/docs/latest/docs/references/sdk/model_model/#config_text)
  - [framework](https://clear.ml/docs/latest/docs/references/sdk/model_model/#framework)
  - [get\_all\_metadata](https://clear.ml/docs/latest/docs/references/sdk/model_model/#get_all_metadata)
  - [get\_all\_metadata\_casted](https://clear.ml/docs/latest/docs/references/sdk/model_model/#get_all_metadata_casted)
  - [get\_local\_copy](https://clear.ml/docs/latest/docs/references/sdk/model_model/#get_local_copy)
  - [get\_metadata](https://clear.ml/docs/latest/docs/references/sdk/model_model/#get_metadata)
  - [get\_metadata\_casted](https://clear.ml/docs/latest/docs/references/sdk/model_model/#get_metadata_casted)
  - [get\_weights](https://clear.ml/docs/latest/docs/references/sdk/model_model/#get_weights)
  - [get\_weights\_package](https://clear.ml/docs/latest/docs/references/sdk/model_model/#get_weights_package)
  - [id](https://clear.ml/docs/latest/docs/references/sdk/model_model/#id)
  - [labels](https://clear.ml/docs/latest/docs/references/sdk/model_model/#labels)
  - [name](https://clear.ml/docs/latest/docs/references/sdk/model_model/#name)
  - [original\_task](https://clear.ml/docs/latest/docs/references/sdk/model_model/#original_task)
  - [project](https://clear.ml/docs/latest/docs/references/sdk/model_model/#project)
  - [publish](https://clear.ml/docs/latest/docs/references/sdk/model_model/#publish)
  - [published](https://clear.ml/docs/latest/docs/references/sdk/model_model/#published)
  - [Model.query\_models](https://clear.ml/docs/latest/docs/references/sdk/model_model/#modelquery_models)
  - [Model.remove](https://clear.ml/docs/latest/docs/references/sdk/model_model/#modelremove)
  - [report\_confusion\_matrix](https://clear.ml/docs/latest/docs/references/sdk/model_model/#report_confusion_matrix)
  - [report\_histogram](https://clear.ml/docs/latest/docs/references/sdk/model_model/#report_histogram)
  - [report\_line\_plot](https://clear.ml/docs/latest/docs/references/sdk/model_model/#report_line_plot)
  - [report\_matrix](https://clear.ml/docs/latest/docs/references/sdk/model_model/#report_matrix)
  - [report\_scalar](https://clear.ml/docs/latest/docs/references/sdk/model_model/#report_scalar)
  - [report\_scatter2d](https://clear.ml/docs/latest/docs/references/sdk/model_model/#report_scatter2d)
  - [report\_scatter3d](https://clear.ml/docs/latest/docs/references/sdk/model_model/#report_scatter3d)
  - [report\_single\_value](https://clear.ml/docs/latest/docs/references/sdk/model_model/#report_single_value)
  - [report\_surface](https://clear.ml/docs/latest/docs/references/sdk/model_model/#report_surface)
  - [report\_table](https://clear.ml/docs/latest/docs/references/sdk/model_model/#report_table)
  - [report\_vector](https://clear.ml/docs/latest/docs/references/sdk/model_model/#report_vector)
  - [set\_all\_metadata](https://clear.ml/docs/latest/docs/references/sdk/model_model/#set_all_metadata)
  - [set\_metadata](https://clear.ml/docs/latest/docs/references/sdk/model_model/#set_metadata)
  - [system\_tags](https://clear.ml/docs/latest/docs/references/sdk/model_model/#system_tags)
  - [tags](https://clear.ml/docs/latest/docs/references/sdk/model_model/#tags)
  - [task](https://clear.ml/docs/latest/docs/references/sdk/model_model/#task)
  - [unarchive](https://clear.ml/docs/latest/docs/references/sdk/model_model/#unarchive)
  - [url](https://clear.ml/docs/latest/docs/references/sdk/model_model/#url)