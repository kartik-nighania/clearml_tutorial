---
url: "https://clear.ml/docs/latest/docs/guides/reporting/media_reporting/"
title: "Media Reporting | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/reporting/media_reporting/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The [media\_reporting.py](https://github.com/clearml/clearml/blob/master/examples/reporting/media_reporting.py) example
demonstrates reporting (uploading) images, audio, and video. Use [`Logger.report_media()`](https://clear.ml/docs/latest/docs/references/sdk/logger#report_media)
to upload from:

- Local path
- BytesIO stream
- URL of media already uploaded to some storage

ClearML uploads media to the bucket specified in the ClearML configuration file. You can configure ClearML for image
storage using [`Logger.set_default_upload_destination()`](https://clear.ml/docs/latest/docs/references/sdk/logger#set_default_upload_destination)
(note that [artifact storage](https://clear.ml/docs/latest/docs/clearml_sdk/task_sdk#setting-upload-destination) is handled differently).
Set the storage credentials in the [clearml.conf file](https://clear.ml/docs/latest/docs/configs/clearml_conf#sdk-section).

ClearML reports media in the **ClearML Web UI** **>** task details **>** **DEBUG SAMPLES**
tab.

When the script runs, it creates a task named `audio and video reporting` in the `examples`
project.

## Reporting (Uploading) Media from a Source by URL [​](https://clear.ml/docs/latest/docs/guides/reporting/media_reporting/\#reporting-uploading-media-from-a-source-by-url "Direct link to Reporting (Uploading) Media from a Source by URL")

Report by using the `url` parameter of [`Logger.report_media()`](https://clear.ml/docs/latest/docs/references/sdk/logger#report_media):

```python
# report video, an already uploaded video media (url)

Logger.current_logger().report_media(

    'video', 'big bunny', iteration=1,

    url='https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/720/Big_Buck_Bunny_720_10s_1MB.mp4'

)



#  report audio, report an already uploaded audio media (url)

Logger.current_logger().report_media(

    'audio', 'pink panther', iteration=1,

    url='https://www2.cs.uic.edu/~i101/SoundFiles/PinkPanther30.wav'

)
```

The reported audio can be viewed in the **DEBUG SAMPLES** tab. Click a thumbnail to open the audio player.

![Audio debug samples](https://clear.ml/docs/latest/assets/images/examples_reporting_08-7d7412296f63d78976c17e1a1356bae6.png#light-mode-only)![Audio debug samples](https://clear.ml/docs/latest/assets/images/examples_reporting_08_dark-0bdfc7956516b12b04d2eb6a353afe5e.png#dark-mode-only)

## Reporting (Uploading) Media from a Local File [​](https://clear.ml/docs/latest/docs/guides/reporting/media_reporting/\#reporting-uploading-media-from-a-local-file "Direct link to Reporting (Uploading) Media from a Local File")

Report by using the `local_path` parameter of [`Logger.report_media()`](https://clear.ml/docs/latest/docs/references/sdk/logger#report_media):

```python
#  report audio, report local media audio file

Logger.current_logger().report_media(

    title='audio',

    series='tada',

    iteration=1,

    local_path=os.path.join('data_samples', 'sample.mp3')

)
```

The reported video can be viewed in the **DEBUG SAMPLES** tab. Click a thumbnail to open the video player.

![Video debug samples](https://clear.ml/docs/latest/assets/images/examples_reporting_09-19466952e385068ae0fa572d97f84bf3.png#light-mode-only)![Video debug samples](https://clear.ml/docs/latest/assets/images/examples_reporting_09_dark-c301c99a8f5e00f687c1235bd9bc3829.png#dark-mode-only)

- [Reporting (Uploading) Media from a Source by URL](https://clear.ml/docs/latest/docs/guides/reporting/media_reporting/#reporting-uploading-media-from-a-source-by-url)
- [Reporting (Uploading) Media from a Local File](https://clear.ml/docs/latest/docs/guides/reporting/media_reporting/#reporting-uploading-media-from-a-local-file)