---
url: "https://clear.ml/docs/latest/docs/guides/reporting/text_reporting/"
title: "Text Reporting | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/reporting/text_reporting/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The [text\_reporting.py](https://github.com/clearml/clearml/blob/master/examples/reporting/text_reporting.py) script
demonstrates reporting text output and samples.

When the script runs, it creates a task named `text reporting` in the `examples` project.

## Reporting Text to Console [​](https://clear.ml/docs/latest/docs/guides/reporting/text_reporting/\#reporting-text-to-console "Direct link to Reporting Text to Console")

To report text to the task console, call [`Logger.report_text()`](https://clear.ml/docs/latest/docs/references/sdk/logger#report_text):

```python
# report text

Logger.current_logger().report_text("hello, this is plain text")
```

Text reported with `Logger.report_text()` appears in the task's **CONSOLE** tab in the ClearML Web UI.

![Text to console](https://clear.ml/docs/latest/assets/images/examples_reporting_text-861562bbc51419096984b52368b8382b.png#light-mode-only)![Text to console](https://clear.ml/docs/latest/assets/images/examples_reporting_text_dark-4cec4023f7e7c7958ab637165db53510.png#dark-mode-only)

## Reporting Text as Debug Samples [​](https://clear.ml/docs/latest/docs/guides/reporting/text_reporting/\#reporting-text-as-debug-samples "Direct link to Reporting Text as Debug Samples")

To report longer text as a debug sample (e.g., logs, large text outputs, or structured text files),
use [`Logger.report_media()`](https://clear.ml/docs/latest/docs/references/sdk/logger#report_media) with a text stream and `.txt` file extension:

```python
text_to_send = """

Lorem ipsum dolor sit amet, consectetur adipiscing elit.

Suspendisse ac justo ut dolor scelerisque posuere.

...

"""

Logger.current_logger().report_media(

    title="text title",

    series="text series",

    iteration=1,

    stream=six.StringIO(text_to_send),

    file_extension=".txt",

)
```

Text samples appear in the task's **DEBUG SAMPLES** tab in the ClearML Web UI.

![Text debug sample](https://clear.ml/docs/latest/assets/images/examples_reporting_text_debug-1c641f839184bfc5cb3fa6940466687e.png#light-mode-only)![Text debug sample](https://clear.ml/docs/latest/assets/images/examples_reporting_text_debug_dark-6961dc95223eddf624d30cfbf6f7e65f.png#dark-mode-only)

- [Reporting Text to Console](https://clear.ml/docs/latest/docs/guides/reporting/text_reporting/#reporting-text-to-console)
- [Reporting Text as Debug Samples](https://clear.ml/docs/latest/docs/guides/reporting/text_reporting/#reporting-text-as-debug-samples)