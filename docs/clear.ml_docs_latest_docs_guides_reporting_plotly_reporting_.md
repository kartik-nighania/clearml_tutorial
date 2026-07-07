---
url: "https://clear.ml/docs/latest/docs/guides/reporting/plotly_reporting/"
title: "Plotly Reporting | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/reporting/plotly_reporting/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

The [plotly\_reporting.py](https://github.com/clearml/clearml/blob/master/examples/reporting/plotly_reporting.py) example
demonstrates ClearML's Plotly integration and reporting.

Report Plotly plots in ClearML by calling the [`Logger.report_plotly()`](https://clear.ml/docs/latest/docs/references/sdk/logger#report_plotly) method, and passing a complex
Plotly figure, using the `figure` parameter.

In this example, the Plotly figure is created using `plotly.express.scatter` (see the [Plotly documentation](https://plotly.com/python/line-and-scatter/)):

```python
# Iris dataset

df = px.data.iris()



# create complex plotly figure

fig = px.scatter(

    df,

    x="sepal_width",

    y="sepal_length",

    color="species",

    marginal_y="rug",

    marginal_x="histogram"

)



# report the plotly figure

task.get_logger().report_plotly(

    title="iris", series="sepal", iteration=0, figure=fig

)
```

When the script runs, it creates a task named `plotly reporting` in the examples project.

ClearML reports Plotly figures, and displays them in the **ClearML Web UI** **>** task's **PLOTS**
tab.

![Web UI task plots](https://clear.ml/docs/latest/assets/images/examples_reporting_13-80192f508599cf864fb5d3711a30fae2.png#light-mode-only)![Web UI task plots](https://clear.ml/docs/latest/assets/images/examples_reporting_13_dark-cf10bd4f36889975a63264b1e060cc20.png#dark-mode-only)