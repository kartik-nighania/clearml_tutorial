---
url: "https://clear.ml/docs/latest/docs/guides/reporting/scatter_hist_confusion_mat_reporting/"
title: "2D Plots Reporting | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/reporting/scatter_hist_confusion_mat_reporting/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The [scatter\_hist\_confusion\_mat\_reporting.py](https://github.com/clearml/clearml/blob/master/examples/reporting/scatter_hist_confusion_mat_reporting.py)
example demonstrates reporting series data in the following 2D formats:

- [Histograms](https://clear.ml/docs/latest/docs/guides/reporting/scatter_hist_confusion_mat_reporting/#histograms)
- [Confusion matrices](https://clear.ml/docs/latest/docs/guides/reporting/scatter_hist_confusion_mat_reporting/#confusion-matrices)
- [Scatter plots](https://clear.ml/docs/latest/docs/guides/reporting/scatter_hist_confusion_mat_reporting/#2d-scatter-plots)

ClearML reports these tables in the **ClearML Web UI** **>** task's **PLOTS** tab.

When the script runs, it creates a task named `2D plots reporting` in the `examples` project.

## Histograms [​](https://clear.ml/docs/latest/docs/guides/reporting/scatter_hist_confusion_mat_reporting/\#histograms "Direct link to Histograms")

Report histograms by calling [`Logger.report_histogram()`](https://clear.ml/docs/latest/docs/references/sdk/logger#report_histogram).
To report more than one series on the same plot, use same the `title` argument. For different plots, use different
`title` arguments. Specify the type of histogram with the `mode` parameter. The `mode` values are `group` (default),
`stack`, and `relative`.

```python
# report a single histogram

histogram = np.random.randint(10, size=10)

Logger.current_logger().report_histogram(

    title="single_histogram",

    series="random histogram",

    iteration=iteration,

    values=histogram,

    xaxis="title x",

    yaxis="title y",

)



# report two histograms on the same graph (plot)

histogram1 = np.random.randint(13, size=10)

histogram2 = histogram * 0.75

Logger.current_logger().report_histogram(

    title="two_histogram",

    series="series 1",

    iteration=iteration,

    values=histogram1,

    xaxis="title x",

    yaxis="title y",

)



Logger.current_logger().report_histogram(

    "two_histogram",

    "series 2",

    iteration=iteration,

    values=histogram2,

    xaxis="title x",

    yaxis="title y",

)
```

![Single histogram](https://clear.ml/docs/latest/assets/images/examples_reporting_15-94c24db66cb3b717db06500981a3f71d.png#light-mode-only)![Single histogram](https://clear.ml/docs/latest/assets/images/examples_reporting_15_dark-cc8f428e114e13bfab189507f226f367.png#dark-mode-only)

![Double histogram](https://clear.ml/docs/latest/assets/images/examples_reporting_15a-d768ad5c398498d0d2a421b80a59d851.png#light-mode-only)![Double histogram](https://clear.ml/docs/latest/assets/images/examples_reporting_15a_dark-f3a404f5bdf2cadbd9c006ad4df6db85.png#dark-mode-only)

## Confusion Matrices [​](https://clear.ml/docs/latest/docs/guides/reporting/scatter_hist_confusion_mat_reporting/\#confusion-matrices "Direct link to Confusion Matrices")

Report confusion matrices by calling [`Logger.report_confusion_matrix()`](https://clear.ml/docs/latest/docs/references/sdk/logger#report_confusion_matrix).

```python
# report confusion matrix

confusion = np.random.randint(10, size=(10, 10))

Logger.current_logger().report_confusion_matrix(

    title="example_confusion",

    series="ignored",

    iteration=iteration,

    matrix=confusion,

    xaxis="title X",

    yaxis="title Y",

)
```

![Confusion matrix](https://clear.ml/docs/latest/assets/images/examples_reporting_16-56b0811834f1b7a7ff673fb8aa37e74d.png#light-mode-only)![Confusion matrix](https://clear.ml/docs/latest/assets/images/examples_reporting_16_dark-408359c7116883a8ef62fd3b3fe9ae7f.png#dark-mode-only)

```python
# report confusion matrix with 0,0 is at the top left

Logger.current_logger().report_confusion_matrix(

    title="example_confusion_0_0_at_top",

    series="ignored",

    iteration=iteration,

    matrix=confusion,

    xaxis="title X",

    yaxis="title Y",

    yaxis_reversed=True,

)
```

![Confusion matrix](https://clear.ml/docs/latest/assets/images/examples_reporting_16a-4d85213f035bdb245b60d665384b720c.png#light-mode-only)![Confusion matrix](https://clear.ml/docs/latest/assets/images/examples_reporting_16a_dark-6cc209f2de00ca4f18cc2265af5f7bcb.png#dark-mode-only)

## 2D Scatter Plots [​](https://clear.ml/docs/latest/docs/guides/reporting/scatter_hist_confusion_mat_reporting/\#2d-scatter-plots "Direct link to 2D Scatter Plots")

Report 2D scatter plots by calling [`Logger.report_scatter2d()`](https://clear.ml/docs/latest/docs/references/sdk/logger#report_scatter2d).
Use the `mode` parameter to plot data points with lines (by default), markers, or both lines and markers.

```python
scatter2d = np.hstack(

    (np.atleast_2d(np.arange(0, 10)).T, np.random.randint(10, size=(10, 1)))

)



# report 2d scatter plot with lines

Logger.current_logger().report_scatter2d(

    title="example_scatter",

    series="series_xy",

    iteration=iteration,

    scatter=scatter2d,

    xaxis="title x",

    yaxis="title y",

)



# report 2d scatter plot with markers

Logger.current_logger().report_scatter2d(

    title="example_scatter",

    series="series_markers",

    iteration=iteration,

    scatter=scatter2d,

    xaxis="title x",

    yaxis="title y",

    mode='markers'

)



# report 2d scatter plot with lines and markers

Logger.current_logger().report_scatter2d(

    title="example_scatter",

    series="series_lines+markers",

    iteration=iteration,

    scatter=scatter2d,

    xaxis="title x",

    yaxis="title y",

    mode='lines+markers'

)
```

![Scatter plot](https://clear.ml/docs/latest/assets/images/examples_reporting_17-b4c80ac1634b8af4c05639620dc9590e.png#light-mode-only)![Scatter plot](https://clear.ml/docs/latest/assets/images/examples_reporting_17_dark-053dbe2ca1b548ab3cb8ea7e3fcff1c3.png#dark-mode-only)

- [Histograms](https://clear.ml/docs/latest/docs/guides/reporting/scatter_hist_confusion_mat_reporting/#histograms)
- [Confusion Matrices](https://clear.ml/docs/latest/docs/guides/reporting/scatter_hist_confusion_mat_reporting/#confusion-matrices)
- [2D Scatter Plots](https://clear.ml/docs/latest/docs/guides/reporting/scatter_hist_confusion_mat_reporting/#2d-scatter-plots)