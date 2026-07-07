---
url: "https://clear.ml/docs/latest/docs/hyperdatasets/previews/"
title: "Previews | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/hyperdatasets/previews/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

Previews are optional images or videos that can be used in the ClearML Enterprise
WebApp (UI) to help visualize selected content in a Hyper-Dataset.

They are useful for displaying images with formats that cannot be rendered in a web browser
(such as TIFF and 3D formats), or to provide an alternative visual representation of the data.

In a Hyper-Dataset frame, the `source` typically points to the original raw data used for training or experimentation,
while the `preview_uri` is intended for display in the UI.

Previews appear in the following WebApp pages:

- [Dataset version page](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_versioning): As thumbnails representing each frame in the dataset version.
If a `preview_uri` is provided, it will be used for the thumbnail. Otherwise, the frame's source is shown.

![Previews](https://clear.ml/docs/latest/assets/images/dataset_versions-611d16ad40b9b1f85f07cdba51b5e8ea.png#light-mode-only)![Previews](https://clear.ml/docs/latest/assets/images/dataset_versions_dark-a7cfd566f7f8e1f646f51be94f02811a.png#dark-mode-only)

If the `preview_uri` points to a video, the thumbnail includes video controls:

![Video previews](https://clear.ml/docs/latest/assets/images/video_preview-1932ab180fe96908e5730f285c1b7978.png#light-mode-only)![Video previews](https://clear.ml/docs/latest/assets/images/video_preview_dark-ac0262f2315abcfbb444ca80f7a58043.png#dark-mode-only)

- [Frame viewer](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_datasets_frames): When inspecting a single frame, the frame viewer lets you toggle between the
`source` and the `preview_uri` if both are provided and differ. If no `preview_uri` is provided, the frame's source is
shown.

![Use source toggle](https://clear.ml/docs/latest/assets/images/source_preview-b054a81f0f0dc11a301ae69e5b83ebcd.png#light-mode-only)![Use source toggle](https://clear.ml/docs/latest/assets/images/source_preview_dark-54ab5e2679b28549d114e4e705ae2ba1.png#dark-mode-only)


## Usage [​](https://clear.ml/docs/latest/docs/hyperdatasets/previews/\#usage "Direct link to Usage")

### Register Frames with a Preview [​](https://clear.ml/docs/latest/docs/hyperdatasets/previews/\#register-frames-with-a-preview "Direct link to Register Frames with a Preview")

To register a frame with a preview, set the `preview_uri` when creating the frame:

```python
# create dataset version

version = DatasetVersion.create_version(

 dataset_name="Example",

 version_name="Registering frame with preview"

)

frame = SingleFrame(

    source='https://acme-datasets.s3.amazonaws.com/tutorials/000012.jpg',

    width=512, height=512,

    preview_uri='https://acme-datasets.s3.amazonaws.com/images/000012.jpg'

)

# add frame to version

version.add_frames([frame])
```

- [Usage](https://clear.ml/docs/latest/docs/hyperdatasets/previews/#usage)
  - [Register Frames with a Preview](https://clear.ml/docs/latest/docs/hyperdatasets/previews/#register-frames-with-a-preview)