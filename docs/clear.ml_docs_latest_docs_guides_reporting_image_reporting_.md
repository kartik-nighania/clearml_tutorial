---
url: "https://clear.ml/docs/latest/docs/guides/reporting/image_reporting/"
title: "Image Reporting | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/reporting/image_reporting/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

The [image\_reporting.py](https://github.com/clearml/clearml/blob/master/examples/reporting/image_reporting.py) example
demonstrates reporting (uploading) images in several formats, including:

- NumPy arrays
- uint8
- uint8 RGB
- PIL Image objects
- Local files.

ClearML uploads images to the bucket specified in the ClearML [configuration file](https://clear.ml/docs/latest/docs/configs/clearml_conf),
or ClearML can be configured for image storage, see [`Logger.set_default_upload_destination()`](https://clear.ml/docs/latest/docs/references/sdk/logger#set_default_upload_destination)
(storage for [artifacts](https://clear.ml/docs/latest/docs/clearml_sdk/task_sdk#setting-upload-destination) is different). Set credentials for
storage in the ClearML configuration file.

When the script runs, it creates a task named `image reporting` in the `examples` project.

Report images using several formats by calling [`Logger.report_image()`](https://clear.ml/docs/latest/docs/references/sdk/logger#report_image):

```python
# report image as float image

m = np.eye(256, 256, dtype=np.float)

Logger.current_logger().report_image(title="image", series="image float", iteration=iteration, image=m)



# report image as uint8

m = np.eye(256, 256, dtype=np.uint8) * 255

Logger.current_logger().report_image(title="image", series="image uint8", iteration=iteration, image=m)



# report image as uint8 RGB

m = np.concatenate((np.atleast_3d(m), np.zeros((256, 256, 2), dtype=np.uint8)), axis=2)

Logger.current_logger().report_image(

    title="image",

    series="image color red",

    iteration=iteration,

    image=m

)



# report PIL Image object

image_open = Image.open(os.path.join("data_samples", "picasso.jpg"))

Logger.current_logger().report_image(

    title="image",

    series="image PIL",

    iteration=iteration,

    image=image_open

)
```

ClearML reports these images as debug samples in the **ClearML Web UI**, under the task's
**DEBUG SAMPLES** tab.

![Debug samples](https://clear.ml/docs/latest/assets/images/examples_reporting_07-b905e5ccb1abcfce198e4696b2821d5d.png#light-mode-only)![Debug samples](https://clear.ml/docs/latest/assets/images/examples_reporting_07_dark-a1d2cd6f72d8e38eb3adb0490284fec4.png#dark-mode-only)

Click a thumbnail to open the image viewer.

![Image viewer](https://clear.ml/docs/latest/assets/images/examples_reporting_07a-51064cdb02fcbea00b1c5cb50b45b4e6.png#light-mode-only)![Image viewer](https://clear.ml/docs/latest/assets/images/examples_reporting_07a_dark-3d45cb943c99ba29603924526f9ba6c1.png#dark-mode-only)