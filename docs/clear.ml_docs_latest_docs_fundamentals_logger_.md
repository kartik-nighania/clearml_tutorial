---
url: "https://clear.ml/docs/latest/docs/fundamentals/logger/"
title: "Logger | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/fundamentals/logger/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The ClearML Logger class is used to report task results such as metrics, graphs, and debug samples. It is provided
through the ClearML [Task](https://clear.ml/docs/latest/docs/fundamentals/task) object.

A Logger object is used to do the following:

- [Manual reporting](https://clear.ml/docs/latest/docs/fundamentals/logger/#manual-reporting), complementing ClearML's [automatic reporting](https://clear.ml/docs/latest/docs/fundamentals/logger/#automatic-reporting)
- [Logging configuration](https://clear.ml/docs/latest/docs/fundamentals/logger/#logger-configuration)
  - Set upload destination for debug sample storage
  - Control ClearML's automatic logging
  - Set default NaN and Inf values

## Types of Logged Results [​](https://clear.ml/docs/latest/docs/fundamentals/logger/\#types-of-logged-results "Direct link to Types of Logged Results")

ClearML supports four types of reports:

- Text - Mostly captured automatically from stdout and stderr but can be logged manually.
- Scalars - Time series data. X-axis is always a sequential number, usually iterations but can be epochs or others.
- Plots - General graphs and diagrams, such as histograms, confusion matrices, line plots, and custom plotly charts.
- Debug Samples - Images, audio, and videos. Can be reported per iteration.

![Logged plots](https://clear.ml/docs/latest/assets/images/report_plotly-48346b1142e5e23026b29b4105d0bf37.png#light-mode-only)![Logged plots](https://clear.ml/docs/latest/assets/images/report_plotly_dark-e87fe883a659211dca153192219b2c9b.png#dark-mode-only)

## Automatic Reporting [​](https://clear.ml/docs/latest/docs/fundamentals/logger/\#automatic-reporting "Direct link to Automatic Reporting")

ClearML automatically captures metrics reported to leading visualization libraries, such as TensorBoard and Matplotlib,
with no additional code necessary.

In addition, ClearML captures and logs everything written to standard output, from debug messages to errors to
library warning messages.

GPU, CPU, Memory, and Network information is also automatically captured.

![CPU monitoring](https://clear.ml/docs/latest/assets/images/fundamentals_logger_cpu_monitoring-3ac1cc3d483ec63c937d5ec6a2212960.png#light-mode-only)![CPU monitoring](https://clear.ml/docs/latest/assets/images/fundamentals_logger_cpu_monitoring_dark-e612ff3c54978cde822a60b72c77c875.png#dark-mode-only)

### Supported Packages [​](https://clear.ml/docs/latest/docs/fundamentals/logger/\#supported-packages "Direct link to Supported Packages")

- [TensorBoard](https://www.tensorflow.org/tensorboard)
- [TensorBoardX](https://github.com/lanpa/tensorboardX)
- [Matplotlib](https://matplotlib.org/)

### Automatic Reporting Examples [​](https://clear.ml/docs/latest/docs/fundamentals/logger/\#automatic-reporting-examples "Direct link to Automatic Reporting Examples")

Check out some of ClearML's automatic reporting examples for supported packages:

- TensorBoard
  - [TensorBoard PR Curve](https://clear.ml/docs/latest/docs/guides/frameworks/tensorflow/tensorboard_pr_curve) \- logging TensorBoard outputs and
    TensorFlow flags
  - [TensorBoard Toy](https://clear.ml/docs/latest/docs/guides/frameworks/tensorflow/tensorboard_toy) \- logging TensorBoard histograms, scalars, images, text, and
    TensorFlow flags
  - [Tensorboard with PyTorch](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/pytorch_tensorboard) \- logging TensorBoard scalars, debug samples, and text integrated into
    code that uses PyTorch
- TensorBoardX
  - [TensorBoardX with PyTorch](https://clear.ml/docs/latest/docs/guides/frameworks/tensorboardx/) \- logging TensorBoardX scalars, debug
    samples, and text in code using PyTorch
  - [MegEngine MNIST](https://clear.ml/docs/latest/docs/guides/frameworks/megengine/megengine_mnist) \- logging scalars using TensorBoardX's `SummaryWriter`
- Matplotlib
  - [Matplotlib](https://clear.ml/docs/latest/docs/guides/frameworks/matplotlib/matplotlib_example) \- logging scatter diagrams plotted with Matplotlib
  - [Matplotlib with PyTorch](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/pytorch_matplotlib) \- logging debug images shown
    by Matplotlib

## Manual Reporting [​](https://clear.ml/docs/latest/docs/fundamentals/logger/\#manual-reporting "Direct link to Manual Reporting")

ClearML also supports manually reporting multiple types of metrics and plots, such as line plots, histograms, and even plotly
charts.

The object used for reporting metrics is called **logger** and is obtained by calling [`Task.get_logger()`](https://clear.ml/docs/latest/docs/references/sdk/task#get_logger).

### Media Reporting [​](https://clear.ml/docs/latest/docs/fundamentals/logger/\#media-reporting "Direct link to Media Reporting")

ClearML also supports reporting media (such as audio, video and images) for every iteration.
This section is mostly used for debugging. It's recommended to use [artifacts](https://clear.ml/docs/latest/docs/fundamentals/task#artifacts) for storing script
outputs that would be used later on.

Only the last X results of each title / series are saved to prevent overloading the server.
See details in [`Logger.report_media`](https://clear.ml/docs/latest/docs/references/sdk/logger#report_media).

![Logger reported images](https://clear.ml/docs/latest/assets/images/webapp_tracking_43-e34d713ae3ffe8201b35e062e51e4242.png#light-mode-only)![Logger reported images](https://clear.ml/docs/latest/assets/images/webapp_tracking_43_dark-ffb10543c2b4f657aa6ef36e5db255e3.png#dark-mode-only)

### Explicit Reporting Examples [​](https://clear.ml/docs/latest/docs/fundamentals/logger/\#explicit-reporting-examples "Direct link to Explicit Reporting Examples")

Check out ClearML's explicit reporting examples for various types of results:

- [Text](https://clear.ml/docs/latest/docs/guides/reporting/text_reporting)
- [Scalars](https://clear.ml/docs/latest/docs/guides/reporting/scalar_reporting)
- Plots
  - [2d plots](https://clear.ml/docs/latest/docs/guides/reporting/scatter_hist_confusion_mat_reporting)
    - Histograms
    - Confusion matrices
    - Scatter plots
  - [3d plots](https://clear.ml/docs/latest/docs/guides/reporting/3d_plots_reporting)
    - Surface plots
    - Scatter plots
  - [Tables](https://clear.ml/docs/latest/docs/guides/reporting/pandas_reporting)
    - Pandas DataFrames
    - CSV file
  - [Matplotlib figures](https://clear.ml/docs/latest/docs/guides/reporting/manual_matplotlib_reporting)
  - [Plotly figures](https://clear.ml/docs/latest/docs/guides/reporting/plotly_reporting)
- Debug Samples
  - [Images](https://clear.ml/docs/latest/docs/guides/reporting/image_reporting)
  - [HTML](https://clear.ml/docs/latest/docs/guides/reporting/html_reporting)
  - [Media - images, audio, video](https://clear.ml/docs/latest/docs/guides/reporting/media_reporting)
- Explicit reporting in Jupyter Notebook [example](https://clear.ml/docs/latest/docs/guides/reporting/clearml_logging_example)

## Logger Configuration [​](https://clear.ml/docs/latest/docs/fundamentals/logger/\#logger-configuration "Direct link to Logger Configuration")

The Logger class provides methods to control aspects of ClearML's logging.

### Upload Destination [​](https://clear.ml/docs/latest/docs/fundamentals/logger/\#upload-destination "Direct link to Upload Destination")

Set the default storage URI for uploading debug samples using the [`Logger.set_default_upload_destination`](https://clear.ml/docs/latest/docs/references/sdk/logger#set_default_upload_destination) method.
The debug samples are uploaded separately. A link to each sample is reported.

Destination Storage Credentials

Credentials for the destination storage are specified in the [ClearML configuration file](https://clear.ml/docs/latest/docs/configs/clearml_conf#sdk-section).

### Automatic Logging Settings [​](https://clear.ml/docs/latest/docs/fundamentals/logger/\#automatic-logging-settings "Direct link to Automatic Logging Settings")

The Logger class provides methods for fine-tuning ClearML's automatic logging behavior with Matplotlib and Tensorboard.
For example, use the [`Logger.matplotlib_force_report_non_interactive`](https://clear.ml/docs/latest/docs/references/sdk/logger#loggermatplotlib_force_report_non_interactive)
class method to control how matplotlib objects are logged. See the [`Logger.tensorboard_auto_group_scalars`](https://clear.ml/docs/latest/docs/references/sdk/logger#loggertensorboard_auto_group_scalars)
class method.

### Set Default NaN and Inf Values [​](https://clear.ml/docs/latest/docs/fundamentals/logger/\#set-default-nan-and-inf-values "Direct link to Set Default NaN and Inf Values")

When you report metrics that include NaN or Inf values, ClearML logs them as `0` by default. You can specify
different default values for NaN and Inf using the [`Logger.set_reporting_nan_value`](https://clear.ml/docs/latest/docs/references/sdk/logger#loggerset_reporting_nan_value)
and the [`Logger.set_reporting_inf_value`](https://clear.ml/docs/latest/docs/references/sdk/logger#loggerset_reporting_inf_value) class methods respectively.

- [Types of Logged Results](https://clear.ml/docs/latest/docs/fundamentals/logger/#types-of-logged-results)
- [Automatic Reporting](https://clear.ml/docs/latest/docs/fundamentals/logger/#automatic-reporting)
  - [Supported Packages](https://clear.ml/docs/latest/docs/fundamentals/logger/#supported-packages)
  - [Automatic Reporting Examples](https://clear.ml/docs/latest/docs/fundamentals/logger/#automatic-reporting-examples)
- [Manual Reporting](https://clear.ml/docs/latest/docs/fundamentals/logger/#manual-reporting)
  - [Media Reporting](https://clear.ml/docs/latest/docs/fundamentals/logger/#media-reporting)
  - [Explicit Reporting Examples](https://clear.ml/docs/latest/docs/fundamentals/logger/#explicit-reporting-examples)
- [Logger Configuration](https://clear.ml/docs/latest/docs/fundamentals/logger/#logger-configuration)
  - [Upload Destination](https://clear.ml/docs/latest/docs/fundamentals/logger/#upload-destination)
  - [Automatic Logging Settings](https://clear.ml/docs/latest/docs/fundamentals/logger/#automatic-logging-settings)
  - [Set Default NaN and Inf Values](https://clear.ml/docs/latest/docs/fundamentals/logger/#set-default-nan-and-inf-values)