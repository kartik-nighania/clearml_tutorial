---
url: "https://clear.ml/docs/latest/docs/references/sdk/logger/"
title: "Logger | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/sdk/logger/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

## _class_ Logger(private\_task, connect\_stdout=True, connect\_stderr=True, connect\_logging=False) [​](https://clear.ml/docs/latest/docs/references/sdk/logger/\#class-loggerprivate_task-connect_stdouttrue-connect_stderrtrue-connect_loggingfalse "Direct link to class-loggerprivate_task-connect_stdouttrue-connect_stderrtrue-connect_loggingfalse")

The `Logger` class is the console log and metric statistics interface, providing methods for explicit reporting.

Explicit reporting extends ClearML automagical capturing of inputs and output. It supports scalar plots, line plots,
histograms, confusion matrices, 2D and 3D scatter diagrams, text logging, tables, and image uploading.

In the ClearML WebApp (UI), `Logger` output appears in the CONSOLE, SCALARS,
PLOTS, and DEBUG SAMPLES tabs.

You must get a Logger object before calling any of the other `Logger` class methods by calling
`Task.get_logger` or `Logger.current_logger`.

warning

Do not construct Logger manually!
Use `Logger.get_current`

* * *

### Logger.current\_logger [​](https://clear.ml/docs/latest/docs/references/sdk/logger/\#loggercurrent_logger "Direct link to Logger.current_logger")

**_classmethod_ current\_logger()**

Get the Logger object for the main execution Task, the current running Task, if one exists. If no Logger object
exists, this method creates one and returns it. Therefore, you can call this method from anywhere
in the code.

```py
logger = Logger.current_logger()
```

- **Return type**

`Logger`

- **Returns**

The Logger object (a singleton) for the current running Task.


* * *

### report\_text [​](https://clear.ml/docs/latest/docs/references/sdk/logger/\#report_text "Direct link to report_text")

**report\_text(msg, level=20, print\_console=True, \*args, \*\*\_)**

For explicit reporting, print text to the log. Optionally, print a log level and print to the console.

For example:

```py
logger.report_text('log some text', level=logging.DEBUG, print_console=False)
```

You can view the reported text in the **ClearML WebApp (UI)**, **RESULTS** tab, **CONSOLE** sub-tab.

- **Parameters**
  - **msg** ( _str_ ) – The text to log.

  - **level** ( _int_ ) – The log level from the Python `logging` package. The default value is `logging.INFO`.

  - **print\_console** ( _bool_ ) – In addition to the log, print to the console.

    The values are:
    - `True` \- Print to the console (default)

    - `False` \- Do not print to the console.
  - **args** ( _Any_ ) –

  - **\_** ( _Any_ ) –
- **Return type**

`None`


* * *

### report\_scalar [​](https://clear.ml/docs/latest/docs/references/sdk/logger/\#report_scalar "Direct link to report_scalar")

**report\_scalar(title, series, value, iteration)**

For explicit reporting, plot a scalar series.

For example, plot a scalar series:

```py
logger = Logger.current_logger()

scalar_series = [random.randint(0,10) for i in range(10)]

for iteration in range(10):

    logger.report_scalar(

        title='scalar metrics',

        series='series',

        value=scalar_series[iteration],

        iteration=iteration,

    )
```

You can view the scalar plots in the **ClearML WebApp (UI)**, **RESULTS** tab, **SCALARS** sub-tab.

- **Parameters**
  - **title** ( _str_ ) – The title (metric) of the plot. Plot more than one scalar series on the same plot by using
    the same `title` for each call to this method.

  - **series** ( _str_ ) – The series name (variant) of the reported scalar.

  - **value** ( _float_ ) – The value to plot per iteration.

  - **iteration** ( _int_ ) – The reported iteration / step (x-axis of the reported time series)
- **Return type**

`None`


* * *

### report\_single\_value [​](https://clear.ml/docs/latest/docs/references/sdk/logger/\#report_single_value "Direct link to report_single_value")

**report\_single\_value(name, value)**

Reports a single value metric (for example, total experiment accuracy or mAP)
You can view the metrics in the **ClearML WebApp (UI)**, **RESULTS** tab, **SCALARS** sub-tab.

- **Parameters**
  - **name** (`str`) – Metric’s name

  - **value** (`float`) – Metric’s value
- **Return type**

`None`


* * *

### report\_vector [​](https://clear.ml/docs/latest/docs/references/sdk/logger/\#report_vector "Direct link to report_vector")

**report\_vector(title, series, values, iteration=None, labels=None, xlabels=None, xaxis=None, yaxis=None, mode=None, extra\_layout=None)**

For explicit reporting, plot a vector as (default stacked) histogram.

info

This method is deprecated. Use `Logger.report_histogram` instead.

For example:

```py
vector_series = np.random.randint(10, size=10).reshape(2,5)

logger.report_vector(

    title='vector example',

    series='vector series',

    values=vector_series,

    iteration=0,

    labels=['A','B'],

    xaxis='X axis label',

    yaxis='Y axis label',

)
```

You can view the vector plot in the **ClearML WebApp (UI)**, **RESULTS** tab, **PLOTS** sub-tab.

- **Parameters**
  - **title** (`str`) – The title (metric) of the plot.

  - **series** (`str`) – The series name (variant) of the reported histogram.

  - **values** (`Sequence`\[`Union`\[`int`, `float`\]\]) – The series values. A list of floats, or an N-dimensional Numpy array containing
    data for each histogram bar.

  - **iteration** (`Optional`\[`int`\]) – The reported iteration / step. Each `iteration` creates another plot.

  - **labels** (`Optional`\[`List`\[`str`\]\]) – Labels for each bar group, creating a plot legend labeling each series (Optional)

  - **xlabels** (`Optional`\[`List`\[`str`\]\]) – Labels per entry in each bucket in the histogram (vector), creating a set of labels
    for each histogram bar on the x-axis (Optional)

  - **xaxis** (`Optional`\[`str`\]) – The x-axis title (Optional)

  - **yaxis** (`Optional`\[`str`\]) – The y-axis title (Optional)

  - **mode** (`Optional`\[`str`\]) – Multiple histograms mode, stack / group / relative. Default is ‘group’.

  - **extra\_layout** (`Optional`\[`dict`\]) – Optional dictionary for layout configuration, passed directly to plotly.
    See full details on the supported configuration: [https://plotly.com/javascript/reference/layout/](https://plotly.com/javascript/reference/layout/).
    Example: `extra_layout={'showlegend': False, 'plot_bgcolor': 'yellow'}`
- **Return type**

`None`


* * *

### report\_histogram [​](https://clear.ml/docs/latest/docs/references/sdk/logger/\#report_histogram "Direct link to report_histogram")

**report\_histogram(title, series, values, iteration=None, labels=None, xlabels=None, xaxis=None, yaxis=None, mode=None, data\_args=None, extra\_layout=None)**

For explicit reporting, plot a (default grouped) histogram.
Notice this function will not calculate the histogram,
it assumes the histogram was already calculated in `values`

For example:

```py
vector_series = np.random.randint(10, size=10).reshape(2,5)

logger.report_histogram(

    title='histogram example',

    series='histogram series',

    values=vector_series,

    iteration=0,

    labels=['A','B'],

    xaxis='X axis label',

    yaxis='Y axis label',

)
```

You can view the reported histograms in the **ClearML WebApp (UI)**, **RESULTS** tab, **PLOTS** sub-tab.

- **Parameters**
  - **title** (`str`) – The title (metric) of the plot.

  - **series** (`str`) – The series name (variant) of the reported histogram.

  - **values** (`Sequence`\[`Union`\[`int`, `float`\]\]) – The series values. A list of floats, or an N-dimensional Numpy array containing
    data for each histogram bar.

  - **iteration** (`Optional`\[`int`\]) – The reported iteration / step. Each `iteration` creates another plot.

  - **labels** (`Optional`\[`List`\[`str`\]\]) – Labels for each bar group, creating a plot legend labeling each series (Optional)

  - **xlabels** (`Optional`\[`List`\[`str`\]\]) – Labels per entry in each bucket in the histogram (vector), creating a set of labels
    for each histogram bar on the x-axis (Optional)

  - **xaxis** (`Optional`\[`str`\]) – The x-axis title (Optional)

  - **yaxis** (`Optional`\[`str`\]) – The y-axis title (Optional)

  - **mode** (`Optional`\[`str`\]) – Multiple histograms mode, stack / group / relative. Default is ‘group’.

  - **data\_args** (`Optional`\[`dict`\]) – Optional dictionary for data configuration, passed directly to plotly.
    See full details on the supported configuration: [https://plotly.com/javascript/reference/bar/](https://plotly.com/javascript/reference/bar/).
    Example: `data_args={'orientation': 'h', 'marker': {'color': 'blue'}}`

  - **extra\_layout** (`Optional`\[`dict`\]) – Optional dictionary for layout configuration, passed directly to plotly.
    See full details on the supported configuration: [https://plotly.com/javascript/reference/bar/](https://plotly.com/javascript/reference/bar/).
    Example: `extra_layout={'xaxis': {'type': 'date', 'range': ['2020-01-01', '2020-01-31']}}`
- **Return type**

`None`


* * *

### report\_table [​](https://clear.ml/docs/latest/docs/references/sdk/logger/\#report_table "Direct link to report_table")

**report\_table(title, series, iteration=None, table\_plot=None, csv=None, url=None, extra\_layout=None, extra\_data=None)**

For explicit reporting, report a table plot.

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

         'num_specimen_seen': [10, 2, 1, 8],

     },

     index=['falcon', 'dog', 'spider', 'fish'],

 )

logger.report_table(title='table example',series='pandas DataFrame',iteration=0,table_plot=df)
```

You can view the reported tables in the **ClearML WebApp (UI)**, **RESULTS** tab, **PLOTS** sub-tab.

- **Parameters**


  - **title** (`str`) – The title (metric) of the table.

  - **series** (`str`) – The series name (variant) of the reported table.

  - **iteration** (`Optional`\[`int`\]) – The reported iteration / step.

  - **table\_plot** (`Union`\[`DataFrame`, `Sequence`\[`Sequence`\], `None`\]) – The output table plot object

  - **csv** (`Optional`\[`str`\]) – Path to local CSV file

  - **url** (`Optional`\[`str`\]) – A URL to the location of CSV file.

  - **extra\_layout** (`Optional`\[`dict`\]) – Optional dictionary for layout configuration, passed directly to plotly.
    See full details on the supported configuration: [https://plotly.com/javascript/reference/layout/](https://plotly.com/javascript/reference/layout/).
    For example:


```py
logger.report_table(

    title='table example',

    series='pandas DataFrame',

    iteration=0,

    table_plot=df,

    extra_layout={'height': 600}

)
```

  - **extra\_data** (`Optional`\[`dict`\]) – Optional dictionary for data configuration, like column width, passed directly to plotly.
    See full details on the supported configuration: [https://plotly.com/javascript/reference/table/](https://plotly.com/javascript/reference/table/).
    For example:

```py
logger.report_table(

    title='table example',

    series='pandas DataFrame',

    iteration=0,

    table_plot=df,

    extra_data={'columnwidth': [2., 1., 1., 1.]}

)
```

- **Return type**

`None`


* * *

### report\_line\_plot [​](https://clear.ml/docs/latest/docs/references/sdk/logger/\#report_line_plot "Direct link to report_line_plot")

**report\_line\_plot(title, series, xaxis, yaxis, mode='lines', iteration=None, reverse\_xaxis=False, comment=None, extra\_layout=None)**

For explicit reporting, plot one or more series as lines.

info

This method is the same as `Logger.report_scatter2d` with `mode='lines'`.
This method is deprecated, use `Logger.report_scatter2d` instead.

- **Parameters**
  - **title** ( _str_ ) – The title (metric) of the plot.

  - **series** ( _list_ ) – All the series data, one list element for each line in the plot.

  - **iteration** ( _int_ ) – The reported iteration / step.

  - **xaxis** ( _str_ ) – The x-axis title (Optional)

  - **yaxis** ( _str_ ) – The y-axis title (Optional)

  - **mode** ( _str_ ) – The type of line plot.

    The values are:
    - `lines` (default)

    - `markers`

    - `lines+markers`
  - **reverse\_xaxis** ( _bool_ ) – Reverse the x-axis.

    The values are:
    - `True` \- The x-axis is high to low (reversed).

    - `False` \- The x-axis is low to high (not reversed) (default)
  - **comment** ( _str_ ) – A comment displayed with the plot, underneath the title.

  - **extra\_layout** ( _dict_ ) – optional dictionary for layout configuration, passed directly to plotly.
    See full details on the supported configuration: [https://plotly.com/javascript/reference/scatter/](https://plotly.com/javascript/reference/scatter/).
    Example: `extra_layout={'xaxis': {'type': 'date', 'range': ['2020-01-01', '2020-01-31']}}`
- **Return type**

`None`


* * *

### report\_scatter2d [​](https://clear.ml/docs/latest/docs/references/sdk/logger/\#report_scatter2d "Direct link to report_scatter2d")

**report\_scatter2d(title, series, scatter, iteration=None, xaxis=None, yaxis=None, labels=None, mode='lines', comment=None, extra\_layout=None)**

For explicit reporting, report a 2d scatter plot.

For example:

```py
scatter2d = np.hstack((

    np.atleast_2d(np.arange(0, 10)).T,

    np.random.randint(10, size=(10, 1)),

))

logger.report_scatter2d(

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

logger.report_scatter2d(

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

logger.report_scatter2d(

    "example_scatter",

    "series_2",

    iteration=1,

    scatter=scatter2d_2,

    xaxis="title x",

    yaxis="title y",

)
```

- **Parameters**
  - **title** ( _str_ ) – The title (metric) of the plot.

  - **series** ( _str_ ) – The series name (variant) of the reported scatter plot.

  - **scatter** ( _list_ ) – The scatter data. numpy.ndarray or list of (pairs of x,y) scatter:

  - **iteration** ( _int_ ) – The reported iteration / step.

  - **xaxis** ( _str_ ) – The x-axis title (Optional)

  - **yaxis** ( _str_ ) – The y-axis title (Optional)

  - **labels** ( _list_ _(_ _str_ _)_ ) – Labels per point in the data assigned to the `scatter` parameter. The labels must be
    in the same order as the data.

  - **mode** ( _str_ ) – The type of scatter plot. The values are:
    - `lines`

    - `markers`

    - `lines+markers`
  - **comment** ( _str_ ) – A comment displayed with the plot, underneath the title.

  - **extra\_layout** ( _dict_ ) – Optional dictionary for layout configuration, passed directly to plotly.
    See full details on the supported configuration: [https://plotly.com/javascript/reference/scatter/](https://plotly.com/javascript/reference/scatter/).
    Example: `extra_layout={'xaxis': {'type': 'date', 'range': ['2020-01-01', '2020-01-31']}}`
- **Return type**

`None`


* * *

### report\_scatter3d [​](https://clear.ml/docs/latest/docs/references/sdk/logger/\#report_scatter3d "Direct link to report_scatter3d")

**report\_scatter3d(title, series, scatter, iteration=None, xaxis=None, yaxis=None, zaxis=None, labels=None, mode='markers', fill=False, comment=None, extra\_layout=None)**

For explicit reporting, plot a 3d scatter graph (with markers).

For example:

```py
scatter3d = np.random.randint(10, size=(10, 3))

logger.report_scatter3d(

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
  - **title** ( _str_ ) – The title (metric) of the plot.

  - **series** ( _str_ ) – The series name (variant) of the reported scatter plot.

  - **scatter** (`Union`\[`Sequence`\[`Tuple`\[`float`, `float`, `float`\]\], `ndarray`\]) – The scatter data.
    list of (pairs of x,y,z), list of series \[\[(x1,y1,z1)…\]\], or numpy.ndarray

  - **iteration** ( _Optional_ _\[_ _int_ _\]_ ) – The reported iteration / step.

  - **xaxis** ( _Optional_ _\[_ _str_ _\]_ ) – The x-axis title (Optional)

  - **yaxis** ( _Optional_ _\[_ _str_ _\]_ ) – The y-axis title (Optional)

  - **zaxis** ( _Optional_ _\[_ _str_ _\]_ ) – The z-axis title (Optional)

  - **labels** ( _Optional_ _\[_ _List_ _\[_ _str_ _\]_ _\]_ ) – Labels per point in the data assigned to the `scatter` parameter.
    The labels must be in the same order as the data.

  - **mode** ( _str_ ) – The type of scatter plot. The values are: `lines`, `markers`, `lines+markers`.

  - **fill** ( _bool_ ) – Fill the area under the curve. The values are:
    - `True` \- Fill

    - `False` \- Do not fill (default)
  - **comment** ( _Optional_ _\[_ _str_ _\]_ ) – A comment displayed with the plot, underneath the title.

  - **extra\_layout** ( _Optional_ _\[_ _dict_ _\]_ ) – Optional dictionary for layout configuration, passed directly to plotly.
    See full details on the supported configuration: [https://plotly.com/javascript/reference/scatter3d/](https://plotly.com/javascript/reference/scatter3d/).
    Example: `extra_layout={'xaxis': {'type': 'date', 'range': ['2020-01-01', '2020-01-31']}}`
- **Return type**

`None`


* * *

### report\_confusion\_matrix [​](https://clear.ml/docs/latest/docs/references/sdk/logger/\#report_confusion_matrix "Direct link to report_confusion_matrix")

**report\_confusion\_matrix(title, series, matrix, iteration=None, xaxis=None, yaxis=None, xlabels=None, ylabels=None, yaxis\_reversed=False, comment=None, extra\_layout=None)**

For explicit reporting, plot a heat-map matrix.

For example:

```py
confusion = np.random.randint(10, size=(10, 10))

logger.report_confusion_matrix(

    "example confusion matrix",

    "ignored",

    iteration=1,

    matrix=confusion,

    xaxis="title X",

    yaxis="title Y",

)
```

- **Parameters**
  - **title** ( _str_ ) – The title (metric) of the plot.

  - **series** ( _str_ ) – The series name (variant) of the reported confusion matrix.

  - **matrix** ( _numpy.ndarray_ ) – A heat-map matrix (example: confusion matrix)

  - **iteration** ( _Optional_ _\[_ _int_ _\]_ ) – The reported iteration / step.

  - **xaxis** ( _Optional_ _\[_ _str_ _\]_ ) – The x-axis title (Optional)

  - **yaxis** ( _Optional_ _\[_ _str_ _\]_ ) – The y-axis title (Optional)

  - **xlabels** ( _Optional_ _\[_ _list_ _(_ _str_ _)_ _\]_ ) – Labels for each column of the matrix (Optional)

  - **ylabels** ( _Optional_ _\[_ _list_ _(_ _str_ _)_ _\]_ ) – Labels for each row of the matrix (Optional)

  - **yaxis\_reversed** ( _bool_ ) – If `False`, the `(0, 0)` coordinate is at the bottom left corner.
    If `True`, the `(0, 0)` coordinate is at the top left corner.

  - **comment** ( _Optional_ _\[_ _str_ _\]_ ) – A comment displayed with the plot, underneath the title.

  - **extra\_layout** ( _Optional_ _\[_ _dict_ _\]_ ) – Optional dictionary for layout configuration, passed directly to `plotly`.
    See full details on the supported configuration: [https://plotly.com/javascript/reference/heatmap/](https://plotly.com/javascript/reference/heatmap/).
    Example: `extra_layout={'xaxis': {'type': 'date', 'range': ['2020-01-01', '2020-01-31']}}`
- **Return type**

`None`


* * *

### report\_matrix [​](https://clear.ml/docs/latest/docs/references/sdk/logger/\#report_matrix "Direct link to report_matrix")

**report\_matrix(title, series, matrix, iteration=None, xaxis=None, yaxis=None, xlabels=None, ylabels=None, yaxis\_reversed=False, extra\_layout=None)**

For explicit reporting, plot a confusion matrix.

info

This method is deprecated, use `Logger.report_confusion_matrix` instead.

- **Parameters**
  - **title** ( _str_ ) – The title (metric) of the plot.

  - **series** ( _str_ ) – The series name (variant) of the reported confusion matrix.

  - **matrix** ( _numpy.ndarray_ ) – A heat-map matrix (example: confusion matrix)

  - **iteration** ( _Optional_ _\[_ _int_ _\]_ ) – The reported iteration / step.

  - **xaxis** ( _Optional_ _\[_ _str_ _\]_ ) – The x-axis title (Optional)

  - **yaxis** ( _Optional_ _\[_ _str_ _\]_ ) – The y-axis title (Optional)

  - **xlabels** ( _Optional_ _\[_ _list_ _(_ _str_ _)_ _\]_ ) – Labels for each column of the matrix (Optional)

  - **ylabels** ( _Optional_ _\[_ _list_ _(_ _str_ _)_ _\]_ ) – Labels for each row of the matrix (Optional)

  - **yaxis\_reversed** ( _bool_ ) – If `False`, the `(0, 0)` coordinate is at the bottom left corner.
    If `True`, the `(0, 0)` coordinate is at the top left corner.

  - **extra\_layout** ( _dict_ ) – optional dictionary for layout configuration, passed directly to `plotly`.
    See full details on the supported configuration: [https://plotly.com/javascript/reference/heatmap/](https://plotly.com/javascript/reference/heatmap/).
    Example: `extra_layout={'xaxis': {'type': 'date', 'range': ['2020-01-01', '2020-01-31']}}`
- **Return type**

`None`


* * *

### report\_surface [​](https://clear.ml/docs/latest/docs/references/sdk/logger/\#report_surface "Direct link to report_surface")

**report\_surface(title, series, matrix, iteration=None, xaxis=None, yaxis=None, zaxis=None, xlabels=None, ylabels=None, camera=None, comment=None, extra\_layout=None)**

For explicit reporting, report a 3d surface plot.

info

This method plots the same data as Logger.report\_confusion\_matrix, but presents the
data as a surface diagram not a confusion matrix.

```py
surface_matrix = np.random.randint(10, size=(10, 10))

logger.report_surface(

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
  - **title** ( _str_ ) – The title (metric) of the plot.

  - **series** ( _str_ ) – The series name (variant) of the reported surface.

  - **matrix** ( _numpy.ndarray_ ) – A heat-map matrix (example: confusion matrix)

  - **iteration** ( _Optional_ _\[_ _int_ _\]_ ) – The reported iteration / step.

  - **xaxis** ( _Optional_ _\[_ _str_ _\]_ ) – The x-axis title (Optional)

  - **yaxis** ( _Optional_ _\[_ _str_ _\]_ ) – The y-axis title (Optional)

  - **zaxis** ( _Optional_ _\[_ _str_ _\]_ ) – The z-axis title (Optional)

  - **xlabels** ( _Optional_ _\[_ _List_ _\[_ _str_ _\]_ _\]_ ) – Labels for each column of the matrix (Optional)

  - **ylabels** ( _Optional_ _\[_ _List_ _\[_ _str_ _\]_ _\]_ ) – Labels for each row of the matrix (Optional)

  - **camera** ( _Optional_ _\[_ _List_ _\[_ _float_ _\]_ _\]_ ) – X,Y,Z coordinates indicating the camera position.
    The default value is `(1,1,1)`.

  - **comment** ( _Optional_ _\[_ _str_ _\]_ ) – A comment displayed with the plot, underneath the title.

  - **extra\_layout** ( _Optional_ _\[_ _dict_ _\]_ ) – Optional dictionary for layout configuration, passed directly to `plotly`.
    See full details on the supported configuration: [https://plotly.com/javascript/reference/surface/](https://plotly.com/javascript/reference/surface/).
    Example: `extra_layout={'xaxis': {'type': 'date', 'range': ['2020-01-01', '2020-01-31']}}`
- **Return type**

`None`


* * *

### report\_image [​](https://clear.ml/docs/latest/docs/references/sdk/logger/\#report_image "Direct link to report_image")

**report\_image(title, series, iteration=None, local\_path=None, image=None, matrix=None, max\_image\_history=None, delete\_after\_upload=False, url=None)**

For explicit reporting, report an image and upload its contents.

This method uploads the image to a preconfigured bucket (see `Logger.set_default_upload_destination`)
describing the task ID, title, series and iteration.

For example:

```py
matrix = np.eye(256, 256, dtype=np.uint8)*255

matrix = np.concatenate(

    (

        np.atleast_3d(matrix),

        np.zeros((256, 256, 2), dtype=np.uint8)

    ),

    axis=2,

)

logger.report_image("test case", "image color red", iteration=1, image=m)

image_open = Image.open(os.path.join("&lt;image_path&gt;", "&lt;image_filename&gt;"))

logger.report_image("test case", "image PIL", iteration=1, image=image_open)
```

One and only one of the following parameters must be provided.

- `local_path`

- `url`

- `image`

- `matrix`


- **Parameters**


  - **title** (`str`) – The title (metric) of the image.

  - **series** (`str`) – The series name (variant) of the reported image.

  - **iteration** (`Optional`\[`int`\]) – The reported iteration / step.

  - **local\_path** (`Optional`\[`str`\]) – A path to an image file.

  - **url** (`Optional`\[`str`\]) – A URL for the location of a pre-uploaded image.

  - **image** (`Union`\[`ndarray`, `Image`, `None`\]) – Image data (RGB).

  - **matrix** (`Optional`\[`ndarray`\]) – **Deprecated**, Image data (RGB).


info

The `matrix` parameter is deprecated. Use the `image` parameters.

  - **max\_image\_history** (`Optional`\[`int`\]) – The maximum number of images to store per metric/variant combination.
    For an unlimited number, use a negative value. The default value is set in global configuration
    (default=\`\`5\`\`).

  - **delete\_after\_upload** (`bool`) – After the upload, delete the local copy of the image. The values are:
    - `True` \- Delete after upload.

    - `False` \- Do not delete after upload (default)
- **Return type**

`None`


* * *

### report\_media [​](https://clear.ml/docs/latest/docs/references/sdk/logger/\#report_media "Direct link to report_media")

**report\_media(title, series, iteration=None, local\_path=None, stream=None, file\_extension=None, max\_history=None, delete\_after\_upload=False, url=None)**

Report media upload its contents, including images, audio, and video.

Media is uploaded to a preconfigured bucket (see `setup_upload()`) with a key (filename)
describing the task ID, title, series and iteration.

One and only one of the following parameters must be provided

- `local_path`

- `stream`

- `url`


If you use `stream` for a BytesIO stream to upload, `file_extension` must be provided.

- **Parameters**
  - **title** ( _str_ ) – The title (metric) of the media.

  - **series** ( _str_ ) – The series name (variant) of the reported media.

  - **iteration** ( _int_ ) – The reported iteration / step.

  - **local\_path** ( _str_ ) – A path to a media file.

  - **stream** (`Union`\[`BytesIO`, `StringIO`, `None`\]) – BytesIO stream to upload. If provided, `file_extension` must also be provided.

  - **url** ( _str_ ) – A URL to the location of a pre-uploaded media.

  - **file\_extension** (`Optional`\[`str`\]) – A file extension to use when `stream` is passed.

  - **max\_history** ( _int_ ) – The maximum number of media files to store per metric/variant combination.
    Use negative value for unlimited. Default is set in global configuration (default=5)

  - **delete\_after\_upload** ( _bool_ ) – After the file is uploaded, delete the local copy
    - `True` \- Delete

    - `False` \- Do not delete
- **Return type**

`None`


* * *

### report\_plotly [​](https://clear.ml/docs/latest/docs/references/sdk/logger/\#report_plotly "Direct link to report_plotly")

**report\_plotly(title, series, figure, iteration=None)**

Report a `Plotly` figure directly.

`Plotly` figure can be a `plotly.graph_objs._figure.Figure` or a dictionary as defined by `plotly.js`

- **Parameters**
  - **title** ( _str_ ) – The title (metric) of the plot.

  - **series** ( _str_ ) – The series name (variant) of the reported plot.

  - **iteration** ( _int_ ) – The reported iteration / step.

  - **figure** ( _dict_ ) – A `plotly` Figure object or a `plotly` dictionary
- **Return type**

`None`


* * *

### report\_matplotlib\_figure [​](https://clear.ml/docs/latest/docs/references/sdk/logger/\#report_matplotlib_figure "Direct link to report_matplotlib_figure")

**report\_matplotlib\_figure(title, series, figure, iteration=None, report\_image=False, report\_interactive=True)**

Report a `matplotlib` figure / plot directly.

`matplotlib.figure.Figure` / `matplotlib.pyplot`

- **Parameters**
  - **title** ( _str_ ) – The title (metric) of the plot.

  - **series** ( _str_ ) – The series name (variant) of the reported plot.

  - **iteration** ( _int_ ) – The reported iteration / step.

  - **figure** ( _MatplotlibFigure_ ) – A `matplotlib` Figure object

  - **report\_image** (`bool`) – Default `False`. If `True`, the plot will be uploaded as a debug sample (png image),
    and will appear under the debug samples tab (instead of the Plots tab).

  - **report\_interactive** (`bool`) – If `True` (default), it will try to convert the `matplotlib` into interactive
    plot in the UI. If `False`, the `matplotlib` is saved as is and will
    be non-interactive (except zooming in/out)
- **Return type**

`None`


* * *

### set\_default\_upload\_destination [​](https://clear.ml/docs/latest/docs/references/sdk/logger/\#set_default_upload_destination "Direct link to set_default_upload_destination")

**set\_default\_upload\_destination(uri)**

Set the destination storage URI (for example, S3, Google Cloud Storage, a file path) for uploading debug images.

The images are uploaded separately. A link to each image is reported.

info

Credentials for the destination storage are specified in the ClearML configuration file,
`~/clearml.conf`.

- **Parameters**

**uri** ( _str_ ) – Example: `'s3://bucket/directory/'` or `'file:///tmp/debug/'`

- **Return type**

`None`

- **Returns**

`True`, if the destination scheme is supported (for example, `s3://`, `file://`, or `gs://`).
`False`, if not supported.


* * *

### get\_default\_upload\_destination [​](https://clear.ml/docs/latest/docs/references/sdk/logger/\#get_default_upload_destination "Direct link to get_default_upload_destination")

**get\_default\_upload\_destination()**

Get the destination storage URI (for example, S3, Google Cloud Storage, a file path) for uploading debug images
(see `Logger.set_default_upload_destination`).

- **Return type**

`str`

- **Returns**

The default upload destination URI.

For example: `s3://bucket/directory/`, or `file:///tmp/debug/`.


* * *

### flush [​](https://clear.ml/docs/latest/docs/references/sdk/logger/\#flush "Direct link to flush")

**flush(wait=False)**

Flush cached reports and console outputs to backend.

- **Parameters**

**wait** (`bool`) – Wait for all outstanding uploads and events to be sent (default `False`)

- **Return type**

`bool`

- **Returns**

`True`, if successfully flushed the cache. `False`, if failed.


* * *

### get\_flush\_period [​](https://clear.ml/docs/latest/docs/references/sdk/logger/\#get_flush_period "Direct link to get_flush_period")

**get\_flush\_period()**

Get the Logger flush period.

- **Return type**

`Optional`\[`float`\]

- **Returns**

The logger flush period in seconds.


* * *

### set\_flush\_period [​](https://clear.ml/docs/latest/docs/references/sdk/logger/\#set_flush_period "Direct link to set_flush_period")

**set\_flush\_period(period)**

Set the logger flush period.

info

This method is deprecated. Use `sdk.development.worker.report_period_sec` to externally control the flush period.

- **Parameters**

**period** ( _float_ ) – The period to flush the logger in seconds. To set no periodic flush,
specify `None` or `0`.

- **Return type**

`None`


* * *

### set\_default\_debug\_sample\_history [​](https://clear.ml/docs/latest/docs/references/sdk/logger/\#set_default_debug_sample_history "Direct link to set_default_debug_sample_history")

**set\_default\_debug\_sample\_history(max\_history)**

Set the default maximum debug sample history when reporting media/debug samples.
Overrides the configuration file defaults.
When reporting debug samples with the same title/series combination and running iterations,
only the last X samples are stored (in other words samples are overwritten).
The default history size set with `max_history` is used when calling
`report_image`, `report_media` etc. without specifying `max_history`.

- **Parameters**

**max\_history** (`int`) – Number of samples (files) to store on a unique set of title/series being reported
with different iteration counters. This is used to make sure users do not end up exploding storage
on server storage side.

For example the following code sample will store the last 5 images even though
we are reporting 100 samples.





```py
logger.set_default_debug_sample_history(5)

for i in range(100):

      logger.report_image(title='image', series='sample', iteration=i, ...)
```

- **Return type**

`None`

- **Returns**


* * *

### get\_default\_debug\_sample\_history [​](https://clear.ml/docs/latest/docs/references/sdk/logger/\#get_default_debug_sample_history "Direct link to get_default_debug_sample_history")

**get\_default\_debug\_sample\_history()**

Return the default max debug sample history when reporting media/debug samples.
If value was not set specifically, the function returns the configuration file default value.

- **Return type**

`int`

- **Returns**

Default number of samples (files) to store on a unique set of title/series being reported
with different iteration counters. This is used to make sure users do not end up exploding storage
on server storage side.


* * *

### report\_image\_and\_upload [​](https://clear.ml/docs/latest/docs/references/sdk/logger/\#report_image_and_upload "Direct link to report_image_and_upload")

**report\_image\_and\_upload(title, series, iteration=None, path=None, matrix=None, max\_image\_history=None, delete\_after\_upload=False)**

info

This method is deprecated, use `Logger.report_image` instead.

- **Return type**

`None`

- **Parameters**
  - **title** ( _str_ ) –

  - **series** ( _str_ ) –

  - **iteration** ( _Optional_ _\[_ _int_ _\]_ ) –

  - **path** ( _Optional_ _\[_ _str_ _\]_ ) –

  - **matrix** ( _Optional_ _\[_ _Union_ _\[_ _ndarray_ \\*, \\* _Image_ _\]_ _\]_ ) –

  - **max\_image\_history** ( _Optional_ _\[_ _int_ _\]_ ) –

  - **delete\_after\_upload** ( _bool_ ) –

* * *

### capture\_logging [​](https://clear.ml/docs/latest/docs/references/sdk/logger/\#capture_logging "Direct link to capture_logging")

**capture\_logging()**

Return context capturing all the logs (via logging) reported under the context

- **Return type**

`Any`

- **Returns**

a ContextManager


* * *

### Logger.tensorboard\_auto\_group\_scalars [​](https://clear.ml/docs/latest/docs/references/sdk/logger/\#loggertensorboard_auto_group_scalars "Direct link to Logger.tensorboard_auto_group_scalars")

**_classmethod_ tensorboard\_auto\_group\_scalars(group\_scalars=False)**

Group together TensorBoard scalars that do not have a title, or assign a title/series with the same tag.

- **Parameters**

**group\_scalars** (`bool`) – Group TensorBoard scalars without a title

The values are:
  - `True` \- Groups scalars without a title together in the “Scalars” plot

  - `False` \- TensorBoard scalars without titles get a title/series with the same tag (default)
- **Return type**

`None`


* * *

### Logger.tensorboard\_single\_series\_per\_graph [​](https://clear.ml/docs/latest/docs/references/sdk/logger/\#loggertensorboard_single_series_per_graph "Direct link to Logger.tensorboard_single_series_per_graph")

**_classmethod_ tensorboard\_single\_series\_per\_graph(single\_series=False)**

info

This method is deprecated. This is now controlled from the UI!

Group TensorBoard scalar series together or in separate plots.

- **Parameters**

**single\_series** (`bool`) – Group TensorBoard scalar series together

The values are:
  - `True` \- Generate a separate plot for each TensorBoard scalar series.

  - `False` \- Group the TensorBoard scalar series together in the same plot (default)
- **Return type**

`None`


* * *

### Logger.matplotlib\_force\_report\_non\_interactive [​](https://clear.ml/docs/latest/docs/references/sdk/logger/\#loggermatplotlib_force_report_non_interactive "Direct link to Logger.matplotlib_force_report_non_interactive")

**_classmethod_ matplotlib\_force\_report\_non\_interactive(force)**

If `True`, all `matplotlib` are always converted to non-interactive static plots (images), appearing in under
the Plots section. If `False` (default), `matplotlib` figures are converted into interactive web UI plotly
figures, in case figure conversion fails, it defaults to non-interactive plots.

- **Parameters**

**force** (`bool`) – If `True`, all `matplotlib` figures are converted automatically to non-interactive plots.

- **Return type**

`None`


* * *

### Logger.set\_reporting\_nan\_value [​](https://clear.ml/docs/latest/docs/references/sdk/logger/\#loggerset_reporting_nan_value "Direct link to Logger.set_reporting_nan_value")

**_classmethod_ set\_reporting\_nan\_value(value, warn\_period=1000)**

When a NaN value is encountered, it is reported as a floating value (by default 0) and the user is warned.
This function is used to change the value NaN is converted to and the warning period.

- **Parameters**
  - **value** (`float`) – The value NaN is converted to

  - **warn\_period** (`int`) – Number of times NaN is encountered and converted until the next warning
- **Return type**

`None`


* * *

### Logger.set\_reporting\_inf\_value [​](https://clear.ml/docs/latest/docs/references/sdk/logger/\#loggerset_reporting_inf_value "Direct link to Logger.set_reporting_inf_value")

**_classmethod_ set\_reporting\_inf\_value(value, warn\_period=1000)**

When an inf value is encountered, it is reported as a floating value (by default 0) and the user is warned.
This function is used to change the value inf is converted to and the warning period.

- **Parameters**
  - **value** (`float`) – The value inf is converted to

  - **warn\_period** (`int`) – Number of times inf is encountered and converted until the next warning
- **Return type**

`None`


- [_class_ Logger(private\_task, connect\_stdout=True, connect\_stderr=True, connect\_logging=False)](https://clear.ml/docs/latest/docs/references/sdk/logger/#class-loggerprivate_task-connect_stdouttrue-connect_stderrtrue-connect_loggingfalse)
  - [Logger.current\_logger](https://clear.ml/docs/latest/docs/references/sdk/logger/#loggercurrent_logger)
  - [report\_text](https://clear.ml/docs/latest/docs/references/sdk/logger/#report_text)
  - [report\_scalar](https://clear.ml/docs/latest/docs/references/sdk/logger/#report_scalar)
  - [report\_single\_value](https://clear.ml/docs/latest/docs/references/sdk/logger/#report_single_value)
  - [report\_vector](https://clear.ml/docs/latest/docs/references/sdk/logger/#report_vector)
  - [report\_histogram](https://clear.ml/docs/latest/docs/references/sdk/logger/#report_histogram)
  - [report\_table](https://clear.ml/docs/latest/docs/references/sdk/logger/#report_table)
  - [report\_line\_plot](https://clear.ml/docs/latest/docs/references/sdk/logger/#report_line_plot)
  - [report\_scatter2d](https://clear.ml/docs/latest/docs/references/sdk/logger/#report_scatter2d)
  - [report\_scatter3d](https://clear.ml/docs/latest/docs/references/sdk/logger/#report_scatter3d)
  - [report\_confusion\_matrix](https://clear.ml/docs/latest/docs/references/sdk/logger/#report_confusion_matrix)
  - [report\_matrix](https://clear.ml/docs/latest/docs/references/sdk/logger/#report_matrix)
  - [report\_surface](https://clear.ml/docs/latest/docs/references/sdk/logger/#report_surface)
  - [report\_image](https://clear.ml/docs/latest/docs/references/sdk/logger/#report_image)
  - [report\_media](https://clear.ml/docs/latest/docs/references/sdk/logger/#report_media)
  - [report\_plotly](https://clear.ml/docs/latest/docs/references/sdk/logger/#report_plotly)
  - [report\_matplotlib\_figure](https://clear.ml/docs/latest/docs/references/sdk/logger/#report_matplotlib_figure)
  - [set\_default\_upload\_destination](https://clear.ml/docs/latest/docs/references/sdk/logger/#set_default_upload_destination)
  - [get\_default\_upload\_destination](https://clear.ml/docs/latest/docs/references/sdk/logger/#get_default_upload_destination)
  - [flush](https://clear.ml/docs/latest/docs/references/sdk/logger/#flush)
  - [get\_flush\_period](https://clear.ml/docs/latest/docs/references/sdk/logger/#get_flush_period)
  - [set\_flush\_period](https://clear.ml/docs/latest/docs/references/sdk/logger/#set_flush_period)
  - [set\_default\_debug\_sample\_history](https://clear.ml/docs/latest/docs/references/sdk/logger/#set_default_debug_sample_history)
  - [get\_default\_debug\_sample\_history](https://clear.ml/docs/latest/docs/references/sdk/logger/#get_default_debug_sample_history)
  - [report\_image\_and\_upload](https://clear.ml/docs/latest/docs/references/sdk/logger/#report_image_and_upload)
  - [capture\_logging](https://clear.ml/docs/latest/docs/references/sdk/logger/#capture_logging)
  - [Logger.tensorboard\_auto\_group\_scalars](https://clear.ml/docs/latest/docs/references/sdk/logger/#loggertensorboard_auto_group_scalars)
  - [Logger.tensorboard\_single\_series\_per\_graph](https://clear.ml/docs/latest/docs/references/sdk/logger/#loggertensorboard_single_series_per_graph)
  - [Logger.matplotlib\_force\_report\_non\_interactive](https://clear.ml/docs/latest/docs/references/sdk/logger/#loggermatplotlib_force_report_non_interactive)
  - [Logger.set\_reporting\_nan\_value](https://clear.ml/docs/latest/docs/references/sdk/logger/#loggerset_reporting_nan_value)
  - [Logger.set\_reporting\_inf\_value](https://clear.ml/docs/latest/docs/references/sdk/logger/#loggerset_reporting_inf_value)