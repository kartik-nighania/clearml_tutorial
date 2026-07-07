---
url: "https://clear.ml/docs/latest/docs/hyperdatasets/custom_metadata/"
title: "Custom Metadata | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/hyperdatasets/custom_metadata/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

Metadata can be customized as needed using: **meta** dictionaries:

- As a top-level key for metadata applying to entire frame
- In `rois` dictionaries, for metadata applying to individual ROIs.

## Usage [​](https://clear.ml/docs/latest/docs/hyperdatasets/custom_metadata/\#usage "Direct link to Usage")

### Adding Frame Metadata [​](https://clear.ml/docs/latest/docs/hyperdatasets/custom_metadata/\#adding-frame-metadata "Direct link to Adding Frame Metadata")

When instantiating a `SingleFrame`, metadata that applies to the entire frame can be
added as an argument:

```python
from allegroai import SingleFrame

# create a frame with metadata

frame = SingleFrame(

    source='https://allegro-datasets.s3.amazonaws.com/tutorials/000012.jpg',

    preview_uri='https://allegro-datasets.s3.amazonaws.com/tutorials/000012.jpg',

    # insert metadata dictionary

    metadata={'alive':'yes'},

)

# add metadata to the frame

frame.metadata['dangerous'] = 'no'
```

### Adding ROI Metadata [​](https://clear.ml/docs/latest/docs/hyperdatasets/custom_metadata/\#adding-roi-metadata "Direct link to Adding ROI Metadata")

Metadata can be added to individual ROIs when adding an annotation to a `frame`, using [`SingleFrame.add_annotation()`](https://clear.ml/docs/latest/docs/references/hyperdataset/singleframe#add_annotation):

```python
frame.add_annotation(

    box2d_xywh=(10, 10, 30, 20),

    labels=['tiger'],

    # insert metadata dictionary

    metadata={'dangerous':'yes'}

)
```

- [Usage](https://clear.ml/docs/latest/docs/hyperdatasets/custom_metadata/#usage)
  - [Adding Frame Metadata](https://clear.ml/docs/latest/docs/hyperdatasets/custom_metadata/#adding-frame-metadata)
  - [Adding ROI Metadata](https://clear.ml/docs/latest/docs/hyperdatasets/custom_metadata/#adding-roi-metadata)