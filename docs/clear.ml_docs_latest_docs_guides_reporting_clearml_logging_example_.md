---
url: "https://clear.ml/docs/latest/docs/guides/reporting/clearml_logging_example/"
title: "Using Logger - Jupyter Notebook | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/reporting/clearml_logging_example/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The [jupyter\_logging\_example.ipynb](https://github.com/clearml/clearml/blob/master/examples/reporting/jupyter_logging_example.ipynb)
script demonstrates the integration of ClearML's explicit reporting module, `Logger`, in a Jupyter Notebook. All ClearML
explicit reporting works with Jupyter Notebook.

This example includes several types of explicit reporting, including:

- Scalars
- Some plots
- Media.

note

In the `clearml` GitHub repository, this example includes a clickable icon to open the notebook in Google Colab.

## Scalars [​](https://clear.ml/docs/latest/docs/guides/reporting/clearml_logging_example/\#scalars "Direct link to Scalars")

To report scalars, call [`Logger.report_scalar()`](https://clear.ml/docs/latest/docs/references/sdk/logger#report_scalar).
The scalar plots appear in the **web UI** in **SCALARS**.

```python
# report two scalar series on two different graphs

for i in range(10):

    logger.report_scalar(title="graph A", series="series A", iteration=i, value=1./(i+1))

    logger.report_scalar(title="graph B", series="series B", iteration=i, value=10./(i+1))
```

![Separate scalar plots](https://clear.ml/docs/latest/assets/images/colab_explicit_reporting_01-26453ffbc33ca0c63c756747a8f915bd.png#light-mode-only)![Separate scalar plots](https://clear.ml/docs/latest/assets/images/colab_explicit_reporting_01_dark-b2f4bc45e0062b118b8332c58f368090.png#dark-mode-only)

```python
# report two scalar series on the same graph

for i in range(10):

    logger.report_scalar(title="unified graph", series="series A", iteration=i, value=1./(i+1))

    logger.report_scalar(title="unified graph", series="series B", iteration=i, value=10./(i+1))
```

![Unified scalar plots](https://clear.ml/docs/latest/assets/images/colab_explicit_reporting_02-9bab0c9d1d8f53c5f4286b65352efcc8.png#light-mode-only)![Unified scalar plots](https://clear.ml/docs/latest/assets/images/colab_explicit_reporting_02_dark-d6d494cd9be0d2c747d6b6bc7aac216e.png#dark-mode-only)

## Plots [​](https://clear.ml/docs/latest/docs/guides/reporting/clearml_logging_example/\#plots "Direct link to Plots")

Plots appear in **PLOTS**.

### 2D Plots [​](https://clear.ml/docs/latest/docs/guides/reporting/clearml_logging_example/\#2d-plots "Direct link to 2D Plots")

Report 2D scatter plots by calling [`Logger.report_scatter2d()`](https://clear.ml/docs/latest/docs/references/sdk/logger#report_scatter2d).
Use the `mode` parameter to plot data points as markers, or both lines and markers.

```python
scatter2d = np.hstack(

    (np.atleast_2d(np.arange(0, 10)).T, np.random.randint(10, size=(10, 1)))

)

# report 2d scatter plot with markers

logger.report_scatter2d(

    title="example_scatter",

    series="series_lines+markers",

    iteration=iteration,

    scatter=scatter2d,

    xaxis="title x",

    yaxis="title y",

    mode='lines+markers'

)
```

![2d scatter plot](https://clear.ml/docs/latest/assets/images/colab_explicit_reporting_04-ede9d8d5e82292d62b686a5111d2849c.png#light-mode-only)![2d scatter plot](https://clear.ml/docs/latest/assets/images/colab_explicit_reporting_04_dark-c7f90fed4258dbb42e91300b396859c7.png#dark-mode-only)

### 3D Plots [​](https://clear.ml/docs/latest/docs/guides/reporting/clearml_logging_example/\#3d-plots "Direct link to 3D Plots")

To plot a series as a 3D scatter plot, use [`Logger.report_scatter3d()`](https://clear.ml/docs/latest/docs/references/sdk/logger#report_scatter3d).

```python
# report 3d scatter plot

scatter3d = np.random.randint(10, size=(10, 3))

logger.report_scatter3d(

    title="example_scatter_3d",

    series="series_xyz",

    iteration=iteration,

    scatter=scatter3d,

    xaxis="title x",

    yaxis="title y",

    zaxis="title z",

)
```

![3d scatter plot](https://clear.ml/docs/latest/assets/images/colab_explicit_reporting_05-50638083a66aec7d40069c5b11c5bae5.png#light-mode-only)![3d scatter plot](https://clear.ml/docs/latest/assets/images/colab_explicit_reporting_05_dark-8d6c770e092e13937bcf08f71be5eea4.png#dark-mode-only)

To plot a series as a surface plot, use [`Logger.report_surface()`](https://clear.ml/docs/latest/docs/references/sdk/logger#report_surface).

```python
# report 3d surface

surface = np.random.randint(10, size=(10, 10))

logger.report_surface(

    title="example_surface",

    series="series1",

    iteration=iteration,

    matrix=surface,

    xaxis="title X",

    yaxis="title Y",

    zaxis="title Z",

)
```

![3d surface plot](https://clear.ml/docs/latest/assets/images/colab_explicit_reporting_06-2325fdba90666e88cb59705bc896e336.png#light-mode-only)![3d surface plot](https://clear.ml/docs/latest/assets/images/colab_explicit_reporting_06_dark-337ca96762b983d537d6b82699ace0c7.png#dark-mode-only)

### Confusion Matrices [​](https://clear.ml/docs/latest/docs/guides/reporting/clearml_logging_example/\#confusion-matrices "Direct link to Confusion Matrices")

Report confusion matrices by calling [`Logger.report_confusion_matrix()`](https://clear.ml/docs/latest/docs/references/sdk/logger#report_confusion_matrix).

```python
# report confusion matrix

confusion = np.random.randint(10, size=(10, 10))

logger.report_confusion_matrix(

    title="example_confusion",

    series="ignored",

    iteration=iteration,

    matrix=confusion,

    xaxis="title X",

    yaxis="title Y",

)
```

![Confusion matrix](https://clear.ml/docs/latest/assets/images/colab_explicit_reporting_03-d727166141837ceb47e377b53d02dd19.png#light-mode-only)![Confusion matrix](https://clear.ml/docs/latest/assets/images/colab_explicit_reporting_03_dark-4c1ab24dcdbe4460cdba267ee13f0fc1.png#dark-mode-only)

### Histograms [​](https://clear.ml/docs/latest/docs/guides/reporting/clearml_logging_example/\#histograms "Direct link to Histograms")

Report histograms by calling [`Logger.report_histogram()`](https://clear.ml/docs/latest/docs/references/sdk/logger#report_histogram).
To report more than one series on the same plot, use the same `title` argument.

```python
# report a single histogram

histogram = np.random.randint(10, size=10)

logger.report_histogram(

    title="single_histogram",

    series="random histogram",

    iteration=iteration,

    values=histogram,

    xaxis="title x",

    yaxis="title y",

)
```

![Histogram](https://clear.ml/docs/latest/assets/images/colab_explicit_reporting_12-cbe8d1c53f008908ff0d23749c5b8d4d.png#light-mode-only)![Histogram](https://clear.ml/docs/latest/assets/images/colab_explicit_reporting_12_dark-a5798215e996ec6416ea144cfaa377ae.png#dark-mode-only)

```python
# report a two histograms on the same plot

histogram1 = np.random.randint(13, size=10)

histogram2 = histogram * 0.75

logger.report_histogram(

    title="two_histogram",

    series="series 1",

    iteration=iteration,

    values=histogram1,

    xaxis="title x",

    yaxis="title y",

)

logger.report_histogram(

    title="two_histogram",

    series="series 2",

    iteration=iteration,

    values=histogram2,

    xaxis="title x",

    yaxis="title y",

)
```

![Two histograms in one plot](https://clear.ml/docs/latest/assets/images/colab_explicit_reporting_07-f5beb9d3514f4e3819b0eeac86d6669f.png#light-mode-only)![Two histograms in one plot](https://clear.ml/docs/latest/assets/images/colab_explicit_reporting_07_dark-fbc513f7ef60b570a3b8a1ec6d7b429d.png#dark-mode-only)

## Media [​](https://clear.ml/docs/latest/docs/guides/reporting/clearml_logging_example/\#media "Direct link to Media")

Report audio, HTML, image, and video by calling [`Logger.report_media()`](https://clear.ml/docs/latest/docs/references/sdk/logger#report_media)
using the `local_path` parameter. They appear in **DEBUG SAMPLES**.

The media for these examples is downloaded using [`StorageManager.get_local_copy()`](https://clear.ml/docs/latest/docs/references/sdk/storage#storagemanagerget_local_copy).

For example, to download an image:

```python
image_local_copy = StorageManager.get_local_copy(

    remote_url="https://pytorch.org/tutorials/_static/img/neural-style/picasso.jpg",

    name="picasso.jpg"

)
```

### Audio [​](https://clear.ml/docs/latest/docs/guides/reporting/clearml_logging_example/\#audio "Direct link to Audio")

```python
logger.report_media(title='audio', series='pink panther', iteration=1, local_path=audio_local_copy)
```

![Audio sample](https://clear.ml/docs/latest/assets/images/colab_explicit_reporting_08-a78357c734c25c624adb085e48aac368.png#light-mode-only)![Audio sample](https://clear.ml/docs/latest/assets/images/colab_explicit_reporting_08_dark-d97c684ace06b7709702c7a5cb55569a.png#dark-mode-only)

### HTML [​](https://clear.ml/docs/latest/docs/guides/reporting/clearml_logging_example/\#html "Direct link to HTML")

```python
logger.report_media(

    title="html",

    series="url_html",

    iteration=1,

    url="https://clear.ml/docs/latest/docs/index.html"

)
```

![HTML sample](https://clear.ml/docs/latest/assets/images/colab_explicit_reporting_09-3fdee8453298edc3b970ec10ab441b75.png#light-mode-only)![HTML sample](https://clear.ml/docs/latest/assets/images/colab_explicit_reporting_09_dark-d7e78bdf2c5ef7db0b93499dee1f3dd4.png#dark-mode-only)

### Images [​](https://clear.ml/docs/latest/docs/guides/reporting/clearml_logging_example/\#images "Direct link to Images")

```python
logger.report_image(

    title="image",

    series="image from url",

    iteration=100,

    local_path=image_local_copy

)
```

![Image sample](https://clear.ml/docs/latest/assets/images/colab_explicit_reporting_10-81908bb84cdc6413c2fa864063476e12.png#light-mode-only)![Image sample](https://clear.ml/docs/latest/assets/images/colab_explicit_reporting_10_dark-324b1906ee109c8051286994b60e1b64.png#dark-mode-only)

### Video [​](https://clear.ml/docs/latest/docs/guides/reporting/clearml_logging_example/\#video "Direct link to Video")

```python
logger.report_media(

    title='video',

    series='big bunny',

    iteration=1,

    local_path=video_local_copy

)
```

![Video sample](https://clear.ml/docs/latest/assets/images/colab_explicit_reporting_11-c03e7b617965004da24c1794496a4e24.png#light-mode-only)![Video sample](https://clear.ml/docs/latest/assets/images/colab_explicit_reporting_11_dark-7764035fc970a210f8d3f810f44183b2.png#dark-mode-only)

## Text [​](https://clear.ml/docs/latest/docs/guides/reporting/clearml_logging_example/\#text "Direct link to Text")

Report text messages by calling [`Logger.report_text()`](https://clear.ml/docs/latest/docs/references/sdk/logger#report_text).

```python
logger.report_text("hello, this is plain text")
```

![Text report to console](https://clear.ml/docs/latest/assets/images/colab_explicit_reporting_13-55fee260388c7eebbf35abc60a8fc6a2.png#light-mode-only)![Text report to console](https://clear.ml/docs/latest/assets/images/colab_explicit_reporting_13_dark-de154bf1db341b80ebffebeaa690dc88.png#dark-mode-only)

- [Scalars](https://clear.ml/docs/latest/docs/guides/reporting/clearml_logging_example/#scalars)
- [Plots](https://clear.ml/docs/latest/docs/guides/reporting/clearml_logging_example/#plots)
  - [2D Plots](https://clear.ml/docs/latest/docs/guides/reporting/clearml_logging_example/#2d-plots)
  - [3D Plots](https://clear.ml/docs/latest/docs/guides/reporting/clearml_logging_example/#3d-plots)
  - [Confusion Matrices](https://clear.ml/docs/latest/docs/guides/reporting/clearml_logging_example/#confusion-matrices)
  - [Histograms](https://clear.ml/docs/latest/docs/guides/reporting/clearml_logging_example/#histograms)
- [Media](https://clear.ml/docs/latest/docs/guides/reporting/clearml_logging_example/#media)
  - [Audio](https://clear.ml/docs/latest/docs/guides/reporting/clearml_logging_example/#audio)
  - [HTML](https://clear.ml/docs/latest/docs/guides/reporting/clearml_logging_example/#html)
  - [Images](https://clear.ml/docs/latest/docs/guides/reporting/clearml_logging_example/#images)
  - [Video](https://clear.ml/docs/latest/docs/guides/reporting/clearml_logging_example/#video)
- [Text](https://clear.ml/docs/latest/docs/guides/reporting/clearml_logging_example/#text)