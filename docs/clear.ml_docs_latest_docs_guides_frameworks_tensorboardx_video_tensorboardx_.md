---
url: "https://clear.ml/docs/latest/docs/guides/frameworks/tensorboardx/video_tensorboardx/"
title: "TensorBoardX Video | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/frameworks/tensorboardx/video_tensorboardx/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The [moveiepy\_tensorboardx.py](https://github.com/clearml/clearml/blob/master/examples/frameworks/tensorboardx/moviepy_tensorboardx.py)
example demonstrates the integration of ClearML into code, which creates a TensorBoardX `SummaryWriter` object to log
video data.

When the script runs, it creates a task named `pytorch with video tensorboardX` in
the `examples` project.

## Debug Samples [​](https://clear.ml/docs/latest/docs/guides/frameworks/tensorboardx/video_tensorboardx/\#debug-samples "Direct link to Debug Samples")

ClearML automatically captures the video data that is added to the `SummaryWriter` object, using the `add_video` method.
The video appears in the task's **DEBUG SAMPLES** tab.

![Debug Samples](https://clear.ml/docs/latest/assets/images/examples_tensorboardx_debug-a01062739d871cf5225d655b94296238.png#light-mode-only)![Debug Samples](https://clear.ml/docs/latest/assets/images/examples_tensorboardx_debug_dark-d376d91be7050e93e57fb9c7860a31be.png#dark-mode-only)

- [Debug Samples](https://clear.ml/docs/latest/docs/guides/frameworks/tensorboardx/video_tensorboardx/#debug-samples)