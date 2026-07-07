---
url: "https://clear.ml/docs/latest/docs/guides/reporting/html_reporting/"
title: "HTML Reporting | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/reporting/html_reporting/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The [html\_reporting.py](https://github.com/clearml/clearml/blob/master/examples/reporting/html_reporting.py) example
demonstrates reporting local HTML files and HTML by URL using [`Logger.report_media()`](https://clear.ml/docs/latest/docs/references/sdk/logger#report_media).

ClearML reports these HTML debug samples in the **ClearML Web UI** **>** task's **DEBUG SAMPLES** tab.

When the script runs, it creates a task named `html samples reporting` in the `examples` project.

![Debug Samples](https://clear.ml/docs/latest/assets/images/examples_reporting_05-183483e6e1bb162eb314c1ecd0912c96.png#light-mode-only)![Debug Samples](https://clear.ml/docs/latest/assets/images/examples_reporting_05_dark-f76dada1fbaebfb515af65644828127e.png#dark-mode-only)

## Reporting HTML URLs [​](https://clear.ml/docs/latest/docs/guides/reporting/html_reporting/\#reporting-html-urls "Direct link to Reporting HTML URLs")

Report HTML by URL using [`Logger.report_media()`](https://clear.ml/docs/latest/docs/references/sdk/logger#report_media)'s `url` parameter.

See the example script's [`report_html_url`](https://github.com/clearml/clearml/blob/master/examples/reporting/html_reporting.py#L16)
function, which reports the ClearML documentation's home page.

```python
Logger.current_logger().report_media(

    title="html",

    series="url_html",

    iteration=iteration,

    url="https://clear.ml/docs/latest/docs/index.html"

)
```

## Reporting HTML Local Files [​](https://clear.ml/docs/latest/docs/guides/reporting/html_reporting/\#reporting-html-local-files "Direct link to Reporting HTML Local Files")

Report the following using `Logger.report_media()`'s `local_path` parameter:

- [Interactive HTML](https://clear.ml/docs/latest/docs/guides/reporting/html_reporting/#interactive-html)
- [Bokeh GroupBy HTML](https://clear.ml/docs/latest/docs/guides/reporting/html_reporting/#bokeh-groupby-html)
- [Bokeh Graph HTML](https://clear.ml/docs/latest/docs/guides/reporting/html_reporting/#bokeh-graph-html)
- [Bokeh Image HTML](https://clear.ml/docs/latest/docs/guides/reporting/html_reporting/#bokeh-image-html)

### Interactive HTML [​](https://clear.ml/docs/latest/docs/guides/reporting/html_reporting/\#interactive-html "Direct link to Interactive HTML")

See the example script's [`report_html_periodic_table`](https://github.com/clearml/clearml/blob/master/examples/reporting/html_reporting.py#L26) function, which reports a file created from Bokeh sample data.

```python
Logger.current_logger().report_media(

    title="html",

    series="periodic_html",

    iteration=iteration,

    local_path="periodic.html"

)
```

### Bokeh GroupBy HTML [​](https://clear.ml/docs/latest/docs/guides/reporting/html_reporting/\#bokeh-groupby-html "Direct link to Bokeh GroupBy HTML")

See the example script's [`report_html_groupby`](https://github.com/clearml/clearml/blob/master/examples/reporting/html_reporting.py#L117) function, which reports a Pandas GroupBy with nested HTML, created from Bokeh sample data.

```python
Logger.current_logger().report_media(

    title="html",

    series="pandas_groupby_nested_html",

    iteration=iteration,

    local_path="bar_pandas_groupby_nested.html",

)
```

### Bokeh Graph HTML [​](https://clear.ml/docs/latest/docs/guides/reporting/html_reporting/\#bokeh-graph-html "Direct link to Bokeh Graph HTML")

See the example script's [`report_html_graph`](https://github.com/clearml/clearml/blob/master/examples/reporting/html_reporting.py#L162) function, which reports a Bokeh plot created from Bokeh sample data.

```python
Logger.current_logger().report_media(

    title="html",

    series="Graph_html",

    iteration=iteration,

    local_path="graph.html"

)
```

### Bokeh Image HTML [​](https://clear.ml/docs/latest/docs/guides/reporting/html_reporting/\#bokeh-image-html "Direct link to Bokeh Image HTML")

See the example script's [`report_html_image`](https://github.com/clearml/clearml/blob/master/examples/reporting/html_reporting.py#L195) function, which reports an image created from Bokeh sample data.

```python
Logger.current_logger().report_media(

    title="html",

    series="Spectral_html",

    iteration=iteration,

    local_path="image.html"

)
```

- [Reporting HTML URLs](https://clear.ml/docs/latest/docs/guides/reporting/html_reporting/#reporting-html-urls)
- [Reporting HTML Local Files](https://clear.ml/docs/latest/docs/guides/reporting/html_reporting/#reporting-html-local-files)
  - [Interactive HTML](https://clear.ml/docs/latest/docs/guides/reporting/html_reporting/#interactive-html)
  - [Bokeh GroupBy HTML](https://clear.ml/docs/latest/docs/guides/reporting/html_reporting/#bokeh-groupby-html)
  - [Bokeh Graph HTML](https://clear.ml/docs/latest/docs/guides/reporting/html_reporting/#bokeh-graph-html)
  - [Bokeh Image HTML](https://clear.ml/docs/latest/docs/guides/reporting/html_reporting/#bokeh-image-html)