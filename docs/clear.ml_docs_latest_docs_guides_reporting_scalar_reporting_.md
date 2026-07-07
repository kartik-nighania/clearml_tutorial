---
url: "https://clear.ml/docs/latest/docs/guides/reporting/scalar_reporting/"
title: "Scalars Reporting | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/reporting/scalar_reporting/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The [scalar\_reporting.py](https://github.com/clearml/clearml/blob/master/examples/reporting/scalar_reporting.py) script
demonstrates explicit scalar reporting. ClearML reports scalars in the **ClearML Web UI** **>** task's **SCALARS** tab.

When the script runs, it creates a task named `scalar reporting` in the `examples` project.

## Reporting Scalar Series [​](https://clear.ml/docs/latest/docs/guides/reporting/scalar_reporting/\#reporting-scalar-series "Direct link to Reporting Scalar Series")

To report scalar series, call [`Logger.report_scalar()`](https://clear.ml/docs/latest/docs/references/sdk/logger#report_scalar).
To report more than one series on the same plot, use the same `title` argument. For different plots, use different
`title` arguments.

```python
# report two scalar series on the same graph

for i in range(100):

    Logger.current_logger().report_scalar(

        title="unified graph", series="series A", iteration=i, value=1./(i+1)

    )

    Logger.current_logger().report_scalar(

        title="unified graph", series="series B", iteration=i, value=10./(i+1)

    )



# report two scalar series on two different graphs

for i in range(100):

    Logger.current_logger().report_scalar(

        title="graph A", series="series A", iteration=i, value=1./(i+1)

    )

    Logger.current_logger().report_scalar(

        title="graph B", series="series B", iteration=i, value=10./(i+1)

    )
```

![Scalars series](https://clear.ml/docs/latest/assets/images/examples_reporting_14-4d613a04ea966775c887ae975f746e31.png#light-mode-only)![Scalars series](https://clear.ml/docs/latest/assets/images/examples_reporting_14_dark-93b31ef13a45c018f70c331555379c99.png#dark-mode-only)

## Reporting Single Scalar Values [​](https://clear.ml/docs/latest/docs/guides/reporting/scalar_reporting/\#reporting-single-scalar-values "Direct link to Reporting Single Scalar Values")

To report single scalar values (individual metrics, not part of a series), use [`Logger.report_single_value()`](https://clear.ml/docs/latest/docs/references/sdk/logger#report_single_value).

```python
# Report individual scalar values

Logger.current_logger().report_single_value(name="metric A", value=486)

Logger.current_logger().report_single_value(name="metric B", value=305.95)
```

Single value scalars are shown in the UI in the task's **SCALARS** tab under the `Summary` table.

![Single scalars](https://clear.ml/docs/latest/assets/images/examples_reporting_14a-56de0c803681be4989cf3baf30c34705.png#light-mode-only)![Single scalars](https://clear.ml/docs/latest/assets/images/examples_reporting_14a_dark-ca8c2a83dbcf4cc561624b67fd4ee143.png#dark-mode-only)

- [Reporting Scalar Series](https://clear.ml/docs/latest/docs/guides/reporting/scalar_reporting/#reporting-scalar-series)
- [Reporting Single Scalar Values](https://clear.ml/docs/latest/docs/guides/reporting/scalar_reporting/#reporting-single-scalar-values)