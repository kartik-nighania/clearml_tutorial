---
url: "https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/"
title: "OutputModel | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

## _class_ OutputModel(task=None, config\_text=None, config\_dict=None, label\_enumeration=None, name=None, tags=None, comment=None, framework=None, base\_model\_id=None) [​](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/\#class-outputmodeltasknone-config_textnone-config_dictnone-label_enumerationnone-namenone-tagsnone-commentnone-frameworknone-base_model_idnone "Direct link to class-outputmodeltasknone-config_textnone-config_dictnone-label_enumerationnone-namenone-tagsnone-commentnone-frameworknone-base_model_idnone")

Create an output model for a Task (experiment) to store the training results.

The model is read-write and automatically registered as the Task’s output model.

A common use case is to reuse the OutputModel object, and override the weights after storing a model snapshot.
Another use case is to create multiple OutputModel objects for a Task, and after a new high score
is found, store a model snapshot.

If the model configuration or label enumeration is not provided, values are inherited from the Task’s input model.

info

When executing a Task remotely with a clearml-agent, you can modify the model configuration and/or model’s
label enumeration using the ClearML WebApp.

Create a new model and immediately connect it to a task.

We do not allow for Model creation without a task, so we always keep track on how we created the models.
In remote execution, Model parameters can be overridden by the Task
(such as model configuration & label enumerator).

- **Parameters**


  - **task** (`Optional`\[`ForwardRef`\]) – The Task object with which the OutputModel object is associated.

  - **config\_text** (`Optional`\[`str`\]) – The configuration as a string.
    This is usually the content of a configuration dictionary file.
    Specify `config_text` or `config_dict`, but not both.

  - **config\_dict** (`Optional`\[`dict`\]) – The configuration as a dictionary. Specify `config_dict` or `config_text`, but not both.

  - **label\_enumeration** (`Optional`\[`Mapping`\[`str`, `int`\]\]) – The label enumeration dictionary of string (label) to integer (value)
    pairs.


For example:

```javascript
{

     "background": 0,

     "person": 1

}
```

  - **name** (`Optional`\[`str`\]) – The name for the newly created model.

  - **tags** (`Optional`\[`List`\[`str`\]\]) – A list of strings which are tags for the model.

  - **comment** (`Optional`\[`str`\]) – A comment / description for the model.

  - **framework** (`Union`\[`str`, `Framework`, `None`\]) – The framework of the model or a Framework object.

  - **base\_model\_id** (`Optional`\[`str`\]) – Model ID to be reused.

* * *

### archive [​](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/\#archive "Direct link to archive")

**archive()**

Archive the model. If the model is already archived, this is a no-op

- **Return type**

`None`


* * *

### comment [​](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/\#comment "Direct link to comment")

**property comment: str**

A description of the model.

- **Return type**

`str`

- **Returns**

The model description.


* * *

### config\_dict [​](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/\#config_dict "Direct link to config_dict")

**property config\_dict: dict**

Get the configuration as a dictionary parsed from the `config_text` text. This usually represents the model
configuration. For example, from prototxt to `.ini` file or Python code to evaluate.

- **Return type**

`dict`

- **Returns**

The configuration.


* * *

### config\_text [​](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/\#config_text "Direct link to config_text")

**property config\_text: str**

Get the configuration as a string. For example, prototxt, a `.ini` file, or Python code to evaluate.

- **Return type**

`str`

- **Returns**

The configuration.


* * *

### connect [​](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/\#connect "Direct link to connect")

**connect(task, name=None, \*\*kwargs)**

Connect a preexisting model to a Task object. Preexisting models include:

- Imported models.

- Models already in the ClearML platform

- Models from external frameworks (e.g. TensorFlow)


- **Parameters**
  - **task** ( [_Task_](https://clear.ml/docs/latest/docs/references/sdk/task#clearml.Task)) – A Task object.

  - **name** (`Optional`\[`str`\]) – The model name as it would appear on the Task object.
    The model’s own name can differ, which is useful when a single Task uses multiple models.

  - **kwargs** ( _Any_ ) –
- **Return type**

`None`


* * *

### framework [​](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/\#framework "Direct link to framework")

**property framework: str**

The ML framework of the model (for example: PyTorch, TensorFlow, XGBoost, etc.).

- **Return type**

`str`

- **Returns**

The model’s framework


* * *

### get\_all\_metadata [​](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/\#get_all_metadata "Direct link to get_all_metadata")

**get\_all\_metadata()**

Returns all metadata as a `Dict[key, Dict[value, type]]`,
where `key`, `value`, and `type` are all strings.
To get values cast to their original types (if possible), use `Model.get_all_metadata_casted`.

- **Return type**

`Dict`\[`str`, `Dict`\[`str`, `str`\]\]

- **Returns**

All metadata in `Dict[key, Dict[value, type]]` format.


* * *

### get\_all\_metadata\_casted [​](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/\#get_all_metadata_casted "Direct link to get_all_metadata_casted")

**get\_all\_metadata\_casted()**

Returns all metadata as a `Dict[key, Dict[value, type]]`,
where `key` and `type` are strings, and `value` is cast to its original type where possible.
To get all values as strings, use `Model.get_all_metadata`.

- **Return type**

`Dict`\[`str`, `Dict`\[`str`, `Any`\]\]

- **Returns**

All metadata in `Dict[key, Dict[value, type]]` format.


* * *

### get\_metadata [​](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/\#get_metadata "Direct link to get_metadata")

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

### get\_metadata\_casted [​](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/\#get_metadata_casted "Direct link to get_metadata_casted")

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

### get\_weights [​](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/\#get_weights "Direct link to get_weights")

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

### get\_weights\_package [​](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/\#get_weights_package "Direct link to get_weights_package")

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

### id [​](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/\#id "Direct link to id")

**property id: str**

The ID (system UUID) of the model.

- **Return type**

`str`

- **Returns**

The model ID.


* * *

### labels [​](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/\#labels "Direct link to labels")

**property labels: Dict\[str, int\]**

Get the label enumeration as a dictionary of string (label) to integer (value) pairs.

For example:

```javascript
{

     "background": 0,

     "person": 1

}
```

- **Return type**

`Dict`\[`str`, `int`\]

- **Returns**

The label enumeration.


* * *

### name [​](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/\#name "Direct link to name")

**property name: str**

The name of the model.

- **Return type**

`str`

- **Returns**

The model name.


* * *

### original\_task [​](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/\#original_task "Direct link to original_task")

**property original\_task: str**

Return the ID of the Task that created this model.

- **Return type**

`str`

- **Returns**

The Task ID


* * *

### project [​](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/\#project "Direct link to project")

**property project: str**

Project ID of the model.

- **Return type**

`str`

- **Returns**

Project ID


* * *

### publish [​](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/\#publish "Direct link to publish")

**publish()**

Set the model to the status `published` and for public use. If the model’s status is already `published`,
then this method is a no-op.

- **Return type**

`None`


* * *

### published [​](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/\#published "Direct link to published")

**property published: bool**

Get the published state of this model.

- **Return type**

`bool`

- **Returns**

`True` if the model is published, `False` otherwise.


* * *

### report\_confusion\_matrix [​](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/\#report_confusion_matrix "Direct link to report_confusion_matrix")

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

### report\_histogram [​](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/\#report_histogram "Direct link to report_histogram")

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

### report\_line\_plot [​](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/\#report_line_plot "Direct link to report_line_plot")

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

### report\_matrix [​](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/\#report_matrix "Direct link to report_matrix")

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

### report\_scalar [​](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/\#report_scalar "Direct link to report_scalar")

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

### report\_scatter2d [​](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/\#report_scatter2d "Direct link to report_scatter2d")

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

### report\_scatter3d [​](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/\#report_scatter3d "Direct link to report_scatter3d")

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

### report\_single\_value [​](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/\#report_single_value "Direct link to report_single_value")

**report\_single\_value(name, value)**

Reports a single value metric (for example, total experiment accuracy or mAP)

- **Parameters**
  - **name** (`str`) – Metric’s name

  - **value** (`float`) – Metric’s value
- **Return type**

`None`


* * *

### report\_surface [​](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/\#report_surface "Direct link to report_surface")

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

### report\_table [​](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/\#report_table "Direct link to report_table")

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

### report\_vector [​](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/\#report_vector "Direct link to report_vector")

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

### set\_all\_metadata [​](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/\#set_all_metadata "Direct link to set_all_metadata")

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

### OutputModel.set\_default\_upload\_uri [​](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/\#outputmodelset_default_upload_uri "Direct link to OutputModel.set_default_upload_uri")

**_classmethod_ set\_default\_upload\_uri(output\_uri)**

Set the default upload URI for all OutputModels.

- **Parameters**

**output\_uri** (`Optional`\[`str`\]) – URL for uploading models. Examples:
  - `https://demofiles.demo.clear.ml`

  - `s3://bucket/`

  - `gs://bucket/`

  - `azure://bucket/`

  - `file:///mnt/shared/nfs`
- **Return type**

`None`


* * *

### set\_metadata [​](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/\#set_metadata "Direct link to set_metadata")

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

### set\_upload\_destination [​](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/\#set_upload_destination "Direct link to set_upload_destination")

**set\_upload\_destination(uri)**

Set the URI of the storage destination for uploaded model weight files.
Supported storage destinations include S3, Google Cloud Storage, and file locations.

Using this method, file uploads are separate and then a link to each is stored in the model object.

info

For storage requiring credentials, the credentials are stored in the ClearML configuration file,
`~/clearml.conf`.

- **Parameters**

**uri** (`str`) – The URI of the upload storage destination.

For example:
  - `s3://bucket/directory/`

  - `file:///tmp/debug/`
- **Return type**

`None`


* * *

### system\_tags [​](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/\#system_tags "Direct link to system_tags")

**property system\_tags: List\[str\]**

A list of system tags describing the model.

- **Return type**

`List`\[`str`\]

- **Returns**

The list of tags.


* * *

### tags [​](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/\#tags "Direct link to tags")

**property tags: List\[str\]**

A list of tags describing the model.

- **Return type**

`List`\[`str`\]

- **Returns**

The list of tags.


* * *

### task [​](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/\#task "Direct link to task")

**property task: str**

The ID of the task connected to this model. If no task is connected, returns the ID of the task that originally
created it.

- **Return type**

`str`

- **Returns**

The Task ID


* * *

### unarchive [​](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/\#unarchive "Direct link to unarchive")

**unarchive()**

Unarchive the model. If the model is not archived, this is a no-op

- **Return type**

`None`


* * *

### update\_design [​](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/\#update_design "Direct link to update_design")

**update\_design(config\_text=None, config\_dict=None)**

Update the model configuration. Store a blob of text for custom usage.

info

This method’s behavior is lazy. The design update is only forced when the weights
are updated.

- **Parameters**
  - **config\_text** (`Optional`\[`str`\]) – The configuration as a string.
    This is usually the content of a configuration dictionary file.
    Specify `config_text` or `config_dict`, but not both.

  - **config\_dict** (`Optional`\[`dict`\]) – The configuration as a dictionary. Specify `config_text` or `config_dict`, but not both.
- **Return type**

`bool`

- **Returns**

`True` if the update was successful, `False` if it was not.


* * *

### update\_labels [​](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/\#update_labels "Direct link to update_labels")

**update\_labels(labels)**

Update the label enumeration.

- **Parameters**

**labels** (`Mapping`\[`str`, `int`\]) – The label enumeration dictionary of string (label) to integer (value) pairs.

For example:





```javascript
{

       "background": 0,

       "person": 1

}
```

- **Return type**

`Any`


* * *

### update\_weights [​](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/\#update_weights "Direct link to update_weights")

**update\_weights(weights\_filename=None, upload\_uri=None, target\_filename=None, auto\_delete\_file=True, register\_uri=None, iteration=None, update\_comment=True, is\_package=False, async\_enable=True)**

Update the model weights from a local file.

info

Uploading the model is a background process. This method returns immediately.

- **Parameters**
  - **weights\_filename** (`Optional`\[`str`\]) – The name of the locally stored weights file to upload.
    Specify `weights_filename` or `register_uri`, but not both.

  - **upload\_uri** (`Optional`\[`str`\]) – The URI of the storage destination for model weights upload. The default value
    is the previously used URI.

  - **target\_filename** (`Optional`\[`str`\]) – The newly created filename in the storage destination location. The default value
    is the `weights_filename` value.

  - **auto\_delete\_file** (`bool`) – If `True` (default), delete the temporary file after uploading.

  - **register\_uri** (`Optional`\[`str`\]) – The URI of an already uploaded weights file. The URI must be valid. Specify
    `register_uri` or `weights_filename`, but not both.

  - **iteration** (`Optional`\[`int`\]) – The iteration number.

  - **update\_comment** (`bool`) – If `True` (default), append the local weights filename to the model comment
    (to maintain provenance).

  - **is\_package** (`bool`) – If `True`, mark the weights file as a compressed package, usually a zip file. Defaults to `False`.

  - **async\_enable** (`bool`) – If `True` (default), upload in the background and return immediately. If `False`, block
    until the upload completes. Raises an error if the upload fails.
- **Return type**

`str`

- **Returns**

The uploaded URI.


* * *

### update\_weights\_package [​](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/\#update_weights_package "Direct link to update_weights_package")

**update\_weights\_package(weights\_filenames=None, weights\_path=None, upload\_uri=None, target\_filename=None, auto\_delete\_file=True, iteration=None, async\_enable=True)**

Update the model weights from a local file, or from directory containing multiple files.

info

Uploading the model is a background process. This method returns immediately.

- **Parameters**
  - **weights\_filenames** (`Optional`\[`Sequence`\[`str`\]\]) – The file names of the locally stored model files. Specify `weights_filenames`,
    or `weights_path`, but not both.

  - **weights\_path** (`Optional`\[`str`\]) – The directory path to a package. All the files in the directory will be uploaded.
    Specify `weights_path` or `weights_filenames`, but not both.

  - **upload\_uri** (`Optional`\[`str`\]) – The URI of the storage destination for the model weights upload. The default
    is the previously used URI.

  - **target\_filename** (`Optional`\[`str`\]) – The newly created filename in the storage destination URI location. The default
    is the value specified in the `weights_filename` parameter.

  - **auto\_delete\_file** (`bool`) – If `True` (default), delete temporary file after uploading.

  - **iteration** (`Optional`\[`int`\]) – The iteration number.

  - **async\_enable** (`bool`) – Whether to upload model in background or to block.
    Will raise an error in the main thread if the weights failed to be uploaded or not.
- **Return type**

`str`

- **Returns**

The uploaded URI for the weights package.


* * *

### upload\_storage\_uri [​](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/\#upload_storage_uri "Direct link to upload_storage_uri")

**property upload\_storage\_uri: str**

The URI of the storage destination for uploaded model weight files.

- **Return type**

`str`

- **Returns**

The URI string


* * *

### url [​](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/\#url "Direct link to url")

**property url: str**

Return the URL of the model file (or archived files)

- **Return type**

`str`

- **Returns**

The model file URL.


* * *

### OutputModel.wait\_for\_uploads [​](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/\#outputmodelwait_for_uploads "Direct link to OutputModel.wait_for_uploads")

**_classmethod_ wait\_for\_uploads(timeout=None, max\_num\_uploads=None)**

Wait for any pending or in-progress model uploads to complete. If no uploads are pending or in-progress,
then the `wait_for_uploads` returns immediately.

- **Parameters**
  - **timeout** (`Optional`\[`float`\]) – The timeout interval to wait for uploads (seconds).

  - **max\_num\_uploads** (`Optional`\[`int`\]) – The maximum number of uploads to wait for.
- **Return type**

`None`


- [_class_ OutputModel(task=None, config\_text=None, config\_dict=None, label\_enumeration=None, name=None, tags=None, comment=None, framework=None, base\_model\_id=None)](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/#class-outputmodeltasknone-config_textnone-config_dictnone-label_enumerationnone-namenone-tagsnone-commentnone-frameworknone-base_model_idnone)
  - [archive](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/#archive)
  - [comment](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/#comment)
  - [config\_dict](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/#config_dict)
  - [config\_text](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/#config_text)
  - [connect](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/#connect)
  - [framework](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/#framework)
  - [get\_all\_metadata](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/#get_all_metadata)
  - [get\_all\_metadata\_casted](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/#get_all_metadata_casted)
  - [get\_metadata](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/#get_metadata)
  - [get\_metadata\_casted](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/#get_metadata_casted)
  - [get\_weights](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/#get_weights)
  - [get\_weights\_package](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/#get_weights_package)
  - [id](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/#id)
  - [labels](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/#labels)
  - [name](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/#name)
  - [original\_task](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/#original_task)
  - [project](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/#project)
  - [publish](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/#publish)
  - [published](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/#published)
  - [report\_confusion\_matrix](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/#report_confusion_matrix)
  - [report\_histogram](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/#report_histogram)
  - [report\_line\_plot](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/#report_line_plot)
  - [report\_matrix](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/#report_matrix)
  - [report\_scalar](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/#report_scalar)
  - [report\_scatter2d](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/#report_scatter2d)
  - [report\_scatter3d](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/#report_scatter3d)
  - [report\_single\_value](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/#report_single_value)
  - [report\_surface](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/#report_surface)
  - [report\_table](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/#report_table)
  - [report\_vector](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/#report_vector)
  - [set\_all\_metadata](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/#set_all_metadata)
  - [OutputModel.set\_default\_upload\_uri](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/#outputmodelset_default_upload_uri)
  - [set\_metadata](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/#set_metadata)
  - [set\_upload\_destination](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/#set_upload_destination)
  - [system\_tags](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/#system_tags)
  - [tags](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/#tags)
  - [task](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/#task)
  - [unarchive](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/#unarchive)
  - [update\_design](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/#update_design)
  - [update\_labels](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/#update_labels)
  - [update\_weights](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/#update_weights)
  - [update\_weights\_package](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/#update_weights_package)
  - [upload\_storage\_uri](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/#upload_storage_uri)
  - [url](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/#url)
  - [OutputModel.wait\_for\_uploads](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel/#outputmodelwait_for_uploads)