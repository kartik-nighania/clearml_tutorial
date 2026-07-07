---
url: "https://clear.ml/docs/latest/docs/guides/reporting/3d_plots_reporting/"
title: "3D Plot Reporting | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/reporting/3d_plots_reporting/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The [3d\_plots\_reporting.py](https://github.com/clearml/clearml/blob/master/examples/reporting/3d_plots_reporting.py)
example demonstrates reporting a series as a surface plot and as a 3D scatter plot.

When the script runs, it creates a task named `3D plot reporting` in the `examples` project.

ClearML reports these plots in the task's **PLOTS** tab.

## Surface Plot [​](https://clear.ml/docs/latest/docs/guides/reporting/3d_plots_reporting/\#surface-plot "Direct link to Surface Plot")

To plot a series as a surface plot, use [`Logger.report_surface()`](https://clear.ml/docs/latest/docs/references/sdk/logger#report_surface):

```python
# report 3d surface

surface = np.random.randint(10, size=(10, 10))

Logger.current_logger().report_surface(

    title="example_surface",

    series="series1",

    iteration=iteration,

    matrix=surface,

    xaxis="title X",

    yaxis="title Y",

    zaxis="title Z",

)
```

View the reported surface plot in **PLOTS**.

![Surface plot](https://clear.ml/docs/latest/assets/images/examples_reporting_02-150b441d8426918120460672d57a594f.png#light-mode-only)![Surface plot](https://clear.ml/docs/latest/assets/images/examples_reporting_02_dark-85d628645c99f3ee081a91c31cdf299d.png#dark-mode-only)

## 3D Scatter Plot [​](https://clear.ml/docs/latest/docs/guides/reporting/3d_plots_reporting/\#3d-scatter-plot "Direct link to 3D Scatter Plot")

To plot a series as a 3D scatter plot, use [`Logger.report_scatter3d()`](https://clear.ml/docs/latest/docs/references/sdk/logger#report_scatter3d):

```python
# report 3d scatter plot

scatter3d = np.random.randint(10, size=(10, 3))

Logger.current_logger().report_scatter3d(

    title="example_scatter_3d",

    series="series_xyz",

    iteration=iteration,

    scatter=scatter3d,

    xaxis="title x",

    yaxis="title y",

    zaxis="title z",

)
```

View the reported 3D scatter plot in **PLOTS**.
![3d scatter plot](https://clear.ml/docs/latest/assets/images/examples_reporting_01-3083da885fe7059341fad017867f850b.png#light-mode-only)![3d scatter plot](https://clear.ml/docs/latest/assets/images/examples_reporting_01_dark-1c27965fc57b2a6d38620e8a579f7998.png#dark-mode-only)

- [Surface Plot](https://clear.ml/docs/latest/docs/guides/reporting/3d_plots_reporting/#surface-plot)
- [3D Scatter Plot](https://clear.ml/docs/latest/docs/guides/reporting/3d_plots_reporting/#3d-scatter-plot)