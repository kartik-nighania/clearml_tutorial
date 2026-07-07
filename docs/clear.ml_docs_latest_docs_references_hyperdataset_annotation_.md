---
url: "https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/"
title: "Annotation | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

## _class_ dataframe.Annotation(values=None, id=None, labels=None, confidence=None, metadata=None) [​](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/\#class-dataframeannotationvaluesnone-idnone-labelsnone-confidencenone-metadatanone "Direct link to class-dataframeannotationvaluesnone-idnone-labelsnone-confidencenone-metadatanone")

Annotation object, representing general purpose annotation data.
Should be inherited and extended/specified as needed

Create a new annotation object

info

In case you need to annotate the same object with more than one annotation type, associate the
annotation objects by giving them the same ID.

- **Parameters**
  - **values** (`Union`\[`Sequence`\[`Union`\[`int`, `float`\]\], `Sequence`\[`Sequence`\[`Union`\[`int`, `float`\]\]\], `None`\]) – A sequence of numeric values or a list of sequences of numeric values

  - **id** (`Optional`\[`str`\]) – String representing the specific annotation. Useful for tracking objects. None is a valid option.

  - **labels** (`Optional`\[`Sequence`\[`str`\]\]) – List of labels (string)

  - **confidence** (`Optional`\[`float`\]) – confidence of annotation

  - **metadata** (`Optional`\[`dict`\]) – General purpose dictionary storing multiple field/values

* * *

### label\_enum [​](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/\#label_enum "Direct link to label_enum")

**property label\_enum**

Returns the enumeration value (integer) based on the DataView mapping, this is a readonly field

- **Return type**

`Optional`\[`int`\]

- **Returns**

(int)


* * *

### Annotation.get\_type [​](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/\#annotationget_type "Direct link to Annotation.get_type")

**_classmethod_ get\_type()**

- **Return type**

`str`

- **Returns**

Unique string representing the annotation type.
Optional values: “p2d”, “k2d”, “k3d”, “elp”, “b2d”, “b3d”, “im”, “mask”


* * *

### values [​](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/\#values "Direct link to values")

**property values**

- **Return type**

`Union`\[`Sequence`\[`Union`\[`int`, `float`\]\], `Sequence`\[`Sequence`\[`Union`\[`int`, `float`\]\]\], `None`\]

- **Returns**

list(float), or list(list(float)), values associated with the annotation object


* * *

### id [​](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/\#id "Direct link to id")

**property id**

Returns an ID (str) associated with the annotation object, None if not applicable.

- **Return type**

`Optional`\[`str`\]

- **Returns**

Unique ID for the annotation in within a frame context


* * *

### labels [​](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/\#labels "Direct link to labels")

**property labels**

Returns a list of labels (strings) associated with the annotation object

- **Return type**

`Optional`\[`Sequence`\[`str`\]\]

- **Returns**

list(str)


* * *

### metadata [​](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/\#metadata "Direct link to metadata")

**property metadata**

Returns General purpose dictionary storing multiple field/values

- **Return type**

`Optional`\[`dict`\]

- **Returns**

(dict)


* * *

### confidence [​](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/\#confidence "Direct link to confidence")

**property confidence**

Returns confidence level associated with the annotation

- **Return type**

`Optional`\[`float`\]

- **Returns**

(float)


* * *

### to\_dict [​](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/\#to_dict "Direct link to to_dict")

**to\_dict()**

Return REST API compliant dictionary

- **Return type**

`dict`

- **Returns**

API compliant dictionary for use directly with REST-API


* * *

### register [​](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/\#register "Direct link to register")

\* _static register(type\_names)_

A decorator to register an annotation type name for classes deriving from Annotation

- **Parameters**

**type\_names** ( _list_ _(_ _str_ _)_ ) – List of annotation types to associated with the class type.

- **Return type**

`Callable`


* * *

### copy [​](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/\#copy "Direct link to copy")

**copy()**

Returns a copy of this Annotation.
:param id: An optional ID value. if None, a new random UUID will be created.

- **Return type**

`Annotation`

- **Returns**

Annotation object


## _class_ dataframe.Mask(mask\_rgb=None, id=None, labels=None, confidence=None, metadata=None, mask\_id=None) [​](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/\#class-dataframemaskmask_rgbnone-idnone-labelsnone-confidencenone-metadatanone-mask_idnone "Direct link to class-dataframemaskmask_rgbnone-idnone-labelsnone-confidencenone-metadatanone-mask_idnone")

Extending Annotation class object.

Mask object, representing a mask annotation.

Create a new annotation object

info

In case you need to annotate the same object with more than one annotation type, associate the
annotation objects by giving them the same ID.

- **Parameters**
  - **values** – A sequence of numeric values or a list of sequences of numeric values

  - **id** ( _Optional_ _\[_ _str_ _\]_ ) – String representing the specific annotation. Useful for tracking objects. None is a valid option.

  - **labels** ( _Optional_ _\[_ _Sequence_ _\[_ _str_ _\]_ _\]_ ) – List of labels (string)

  - **confidence** ( _Optional_ _\[_ _float_ _\]_ ) – confidence of annotation

  - **metadata** ( _Optional_ _\[_ _dict_ _\]_ ) – General purpose dictionary storing multiple field/values

  - **mask\_rgb** ( _Optional_ _\[_ _Sequence_ _\[_ _int_ \\*, \\* _int_ \\*, \\* _int_ _\]_ _\]_ ) –

  - **mask\_id** ( _Optional_ _\[_ _str_ _\]_ ) –
- **Return type**

()


* * *

### mask\_id [​](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/\#mask_id "Direct link to mask_id")

**property mask\_id**

- **Return type**

`str`

- **Returns**

mask ID


* * *

### mask\_rgb [​](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/\#mask_rgb "Direct link to mask_rgb")

**property mask\_rgb**

- **Return type**

Sequence\[int, int, int\]

- **Returns**

list of RGB \[int, int, int\]


## _class_ dataframe.Polygon2D(polygon\_xy=None, id=None, labels=None, confidence=None, metadata=None) [​](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/\#class-dataframepolygon2dpolygon_xynone-idnone-labelsnone-confidencenone-metadatanone "Direct link to class-dataframepolygon2dpolygon_xynone-idnone-labelsnone-confidencenone-metadatanone")

Extending Annotation class object.

Polygon2D object, representing a 2D polygon, parsing the set of float values as pairs of x,y vertices.

Create a new annotation object

info

In case you need to annotate the same object with more than one annotation type, associate the
annotation objects by giving them the same ID.

- **Parameters**
  - **values** – A sequence of numeric values or a list of sequences of numeric values

  - **id** ( _Optional_ _\[_ _str_ _\]_ ) – String representing the specific annotation. Useful for tracking objects. None is a valid option.

  - **labels** ( _Optional_ _\[_ _Sequence_ _\[_ _str_ _\]_ _\]_ ) – List of labels (string)

  - **confidence** ( _Optional_ _\[_ _float_ _\]_ ) – confidence of annotation

  - **metadata** ( _Optional_ _\[_ _dict_ _\]_ ) – General purpose dictionary storing multiple field/values

  - **polygon\_xy** ( _Optional_ _\[_ _Sequence_ _\[_ _Tuple_ _\[_ _float_ \\*, \\* _float_ _\]_ _\]_ _\]_ ) –
- **Return type**

()


* * *

### get\_bounding\_box [​](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/\#get_bounding_box "Direct link to get_bounding_box")

**get\_bounding\_box()**

Get the bounding box for this 2D polygon

- **Return type**

Sequence\[4, float\]

- **Returns**

\[left\_x top\_y width height\]


* * *

### polygon\_xy [​](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/\#polygon_xy "Direct link to polygon_xy")

**property polygon\_xy**

- **Return type**

`Sequence`\[`Tuple`\[`float`, `float`\]\]

- **Returns**

list of x,y pairs \[(float, float), \]


## _class_ dataframe.ComplexPolygon2D(polygons\_xy=None, id=None, labels=None, confidence=None, metadata=None) [​](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/\#class-dataframecomplexpolygon2dpolygons_xynone-idnone-labelsnone-confidencenone-metadatanone "Direct link to class-dataframecomplexpolygon2dpolygons_xynone-idnone-labelsnone-confidencenone-metadatanone")

Extending Annotation class object.

ComplexPolygon2D object, representing a set of 2D polygons,
parsing the set of float values as list of polygons (with pairs of x,y vertices per polygon).

Create a new annotation object

info

In case you need to annotate the same object with more than one annotation type, associate the
annotation objects by giving them the same ID.

- **Parameters**
  - **values** – A sequence of numeric values or a list of sequences of numeric values

  - **id** ( _Optional_ _\[_ _str_ _\]_ ) – String representing the specific annotation. Useful for tracking objects. None is a valid option.

  - **labels** ( _Optional_ _\[_ _Sequence_ _\[_ _str_ _\]_ _\]_ ) – List of labels (string)

  - **confidence** ( _Optional_ _\[_ _float_ _\]_ ) – confidence of annotation

  - **metadata** ( _Optional_ _\[_ _dict_ _\]_ ) – General purpose dictionary storing multiple field/values

  - **polygons\_xy** ( _Optional_ _\[_ _Sequence_ _\[_ _Sequence_ _\[_ _Tuple_ _\[_ _float_ \\*, \\* _float_ _\]_ _\]_ _\]_ _\]_ ) –
- **Return type**

()


* * *

### get\_bounding\_box [​](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/\#get_bounding_box-1 "Direct link to get_bounding_box")

**get\_bounding\_box()**

Get the bounding box for this 2D polygon

- **Return type**

Sequence\[4, float\]

- **Returns**

\[left\_x top\_y width height\]


* * *

### polygons\_xy [​](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/\#polygons_xy "Direct link to polygons_xy")

**property polygons\_xy**

- **Return type**

`Sequence`\[`Sequence`\[`Tuple`\[`float`, `float`\]\]\]

- **Returns**

list of list of x,y pairs \[\[(float, float), \], \[(float, float), \], \]


## _class_ dataframe.Polygon3D(polygon\_xyz=None, id=None, labels=None, confidence=None, metadata=None) [​](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/\#class-dataframepolygon3dpolygon_xyznone-idnone-labelsnone-confidencenone-metadatanone "Direct link to class-dataframepolygon3dpolygon_xyznone-idnone-labelsnone-confidencenone-metadatanone")

Extending Annotation class object.

Polygon3D object, representing a 3D polygon, parsing the set of float values as triplets of x,y,z vertices.

Create a new annotation object

info

In case you need to annotate the same object with more than one annotation type, associate the
annotation objects by giving them the same ID.

- **Parameters**
  - **values** – A sequence of numeric values or a list of sequences of numeric values

  - **id** ( _Optional_ _\[_ _str_ _\]_ ) – String representing the specific annotation. Useful for tracking objects. None is a valid option.

  - **labels** ( _Optional_ _\[_ _Sequence_ _\[_ _str_ _\]_ _\]_ ) – List of labels (string)

  - **confidence** ( _Optional_ _\[_ _float_ _\]_ ) – confidence of annotation

  - **metadata** ( _Optional_ _\[_ _dict_ _\]_ ) – General purpose dictionary storing multiple field/values

  - **polygon\_xyz** ( _Optional_ _\[_ _Sequence_ _\[_ _Tuple_ _\[_ _float_ \\*, \\* _float_ \\*, \\* _float_ _\]_ _\]_ _\]_ ) –
- **Return type**

()


* * *

### polygon\_xyz [​](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/\#polygon_xyz "Direct link to polygon_xyz")

**property polygon\_xyz**

- **Return type**

`Sequence`\[`Tuple`\[`float`, `float`, `float`\]\]

- **Returns**

list of x,y,z triplets \[(float, float, float), \]


## _class_ dataframe.ComplexPolygon3D(polygons\_xyz=None, id=None, labels=None, confidence=None, metadata=None) [​](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/\#class-dataframecomplexpolygon3dpolygons_xyznone-idnone-labelsnone-confidencenone-metadatanone "Direct link to class-dataframecomplexpolygon3dpolygons_xyznone-idnone-labelsnone-confidencenone-metadatanone")

Extending Annotation class object.

ComplexPolygon3D object, representing a set of 3D polygons,
parsing the set of float values as list of polygons (with triplets of x,y,z vertices per polygon).

Create a new annotation object

info

In case you need to annotate the same object with more than one annotation type, associate the
annotation objects by giving them the same ID.

- **Parameters**
  - **values** – A sequence of numeric values or a list of sequences of numeric values

  - **id** (`Optional`\[`str`\]) – String representing the specific annotation. Useful for tracking objects. None is a valid option.

  - **labels** (`Optional`\[`Sequence`\[`str`\]\]) – List of labels (string)

  - **confidence** (`Optional`\[`float`\]) – confidence of annotation

  - **metadata** (`Optional`\[`dict`\]) – General purpose dictionary storing multiple field/values

  - **polygons\_xyz** ( _Optional_ _\[_ _Sequence_ _\[_ _Sequence_ _\[_ _Tuple_ _\[_ _float_ \\*, \\* _float_ \\*, \\* _float_ _\]_ _\]_ _\]_ _\]_ ) –

* * *

### polygons\_xyz [​](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/\#polygons_xyz "Direct link to polygons_xyz")

**property polygons\_xyz**

- **Return type**

`Sequence`\[`Sequence`\[`Tuple`\[`float`, `float`, `float`\]\]\]

- **Returns**

list of list of x,y,z triplets \[\[(float, float, float), \], \[(float, float, float), \], \]


## _class_ dataframe.KeyPoints2D(keypoints\_xy=None, id=None, labels=None, confidence=None, metadata=None) [​](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/\#class-dataframekeypoints2dkeypoints_xynone-idnone-labelsnone-confidencenone-metadatanone "Direct link to class-dataframekeypoints2dkeypoints_xynone-idnone-labelsnone-confidencenone-metadatanone")

Extending Annotation class object.

KeyPoints2D object, representing a 2D set of key points, parsing the set of float values as pairs of x,y points.

Create a new annotation object

info

In case you need to annotate the same object with more than one annotation type, associate the
annotation objects by giving them the same ID.

- **Parameters**
  - **values** – A sequence of numeric values or a list of sequences of numeric values

  - **id** ( _Optional_ _\[_ _str_ _\]_ ) – String representing the specific annotation. Useful for tracking objects. None is a valid option.

  - **labels** ( _Optional_ _\[_ _Sequence_ _\[_ _str_ _\]_ _\]_ ) – List of labels (string)

  - **confidence** ( _Optional_ _\[_ _float_ _\]_ ) – confidence of annotation

  - **metadata** ( _Optional_ _\[_ _dict_ _\]_ ) – General purpose dictionary storing multiple field/values

  - **keypoints\_xy** ( _Optional_ _\[_ _Sequence_ _\[_ _Tuple_ _\[_ _float_ \\*, \\* _float_ _\]_ _\]_ _\]_ ) –
- **Return type**

()


* * *

### get\_bounding\_box [​](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/\#get_bounding_box-2 "Direct link to get_bounding_box")

**get\_bounding\_box()**

Get the bounding box for this 2D key points object

- **Return type**

Sequence\[4, float\]

- **Returns**

\[left\_x top\_y width height\]


* * *

### keypoints\_xy [​](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/\#keypoints_xy "Direct link to keypoints_xy")

**property keypoints\_xy**

- **Return type**

`Sequence`\[`Tuple`\[`float`, `float`\]\]

- **Returns**

list of x,y pairs \[(float, float), \]


## _class_ dataframe.KeyPoints3D(keypoints\_xyz=None, id=None, labels=None, confidence=None, metadata=None) [​](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/\#class-dataframekeypoints3dkeypoints_xyznone-idnone-labelsnone-confidencenone-metadatanone "Direct link to class-dataframekeypoints3dkeypoints_xyznone-idnone-labelsnone-confidencenone-metadatanone")

Extending Annotation class object.

KeyPoints3D object, representing a 3D set of key points,
parsing the set of float values as triplets of x,y,z points.

Create a new annotation object

info

In case you need to annotate the same object with more than one annotation type, associate the
annotation objects by giving them the same ID.

- **Parameters**
  - **values** – A sequence of numeric values or a list of sequences of numeric values

  - **id** ( _Optional_ _\[_ _str_ _\]_ ) – String representing the specific annotation. Useful for tracking objects. None is a valid option.

  - **labels** ( _Optional_ _\[_ _Sequence_ _\[_ _str_ _\]_ _\]_ ) – List of labels (string)

  - **confidence** ( _Optional_ _\[_ _float_ _\]_ ) – confidence of annotation

  - **metadata** ( _Optional_ _\[_ _dict_ _\]_ ) – General purpose dictionary storing multiple field/values

  - **keypoints\_xyz** ( _Optional_ _\[_ _Sequence_ _\[_ _Tuple_ _\[_ _float_ \\*, \\* _float_ \\*, \\* _float_ _\]_ _\]_ _\]_ ) –
- **Return type**

()


* * *

### keypoints\_xyz [​](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/\#keypoints_xyz "Direct link to keypoints_xyz")

**property keypoints\_xyz**

- **Return type**

`Sequence`\[`Tuple`\[`float`, `float`, `float`\]\]

- **Returns**

list of x,y,z triplets \[(float, float, float), \]


## _class_ dataframe.Ellipse2D(ellipse2d\_xyrrt=None, id=None, labels=None, confidence=None, metadata=None) [​](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/\#class-dataframeellipse2dellipse2d_xyrrtnone-idnone-labelsnone-confidencenone-metadatanone "Direct link to class-dataframeellipse2dellipse2d_xyrrtnone-idnone-labelsnone-confidencenone-metadatanone")

Extending Annotation class object.

Ellipse2D object, representing an 2D Ellipse, parsing the central point with rx and ry as radii and
theta as the rotation angle (radians)

Create a new annotation object

info

In case you need to annotate the same object with more than one annotation type, associate the
annotation objects by giving them the same ID.

- **Parameters**
  - **values** – A sequence of numeric values or a list of sequences of numeric values

  - **id** ( _Optional_ _\[_ _str_ _\]_ ) – String representing the specific annotation. Useful for tracking objects. None is a valid option.

  - **labels** ( _Optional_ _\[_ _Sequence_ _\[_ _str_ _\]_ _\]_ ) – List of labels (string)

  - **confidence** ( _Optional_ _\[_ _float_ _\]_ ) – confidence of annotation

  - **metadata** ( _Optional_ _\[_ _dict_ _\]_ ) – General purpose dictionary storing multiple field/values

  - **ellipse2d\_xyrrt** ( _Optional_ _\[_ _Sequence_ _\[_ _5_ \\*, \\* _float_ _\]_ _\]_ ) –
- **Return type**

()


* * *

### angle [​](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/\#angle "Direct link to angle")

**property angle**

Return the angle (radians) of the ellipse

- **Return type**

`float`

- **Returns**

float represent the angle (radians)


* * *

### center [​](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/\#center "Direct link to center")

**property center**

Return the center of the ellipse

- **Return type**

`Tuple`\[`float`, `float`\]

- **Returns**

(float, float) represent the center x, y coordinates


* * *

### ellipse2d\_xyrrt [​](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/\#ellipse2d_xyrrt "Direct link to ellipse2d_xyrrt")

**property ellipse2d\_xyrrt**

- **Return type**

Sequence\[float, float, float, float, float\]

- **Returns**

list of x, y, rx, ry and theta as angle (radians) \[float, float, float, float, float\]


* * *

### get\_bounding\_box [​](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/\#get_bounding_box-3 "Direct link to get_bounding_box")

**get\_bounding\_box()**

Get the bounding box for this 2D ellipse (angle in radians)

- **Return type**

Sequence\[5, float\]

- **Returns**

\[left\_x top\_y width height angle\]


* * *

### get\_polygon [​](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/\#get_polygon "Direct link to get_polygon")

**get\_polygon(num\_point=4)**

Get a polygon points wrapping the ellipse

- **Parameters**

**num\_point** (`int`) – the number of polygon points.

- **Return type**

`Sequence`\[`Tuple`\[`float`, `float`\]\]

- **Returns**

list of x,y pairs \[(float, float), (float, float), …\]


* * *

### radii [​](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/\#radii "Direct link to radii")

**property radii**

Return the radii of the ellipse

- **Return type**

`Tuple`\[`float`, `float`\]

- **Returns**

(float, float) represent the (rx, ry)


## _class_ dataframe.BoundingBox2D(bounding\_box\_xywh=None, id=None, labels=None, confidence=None, metadata=None) [​](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/\#class-dataframeboundingbox2dbounding_box_xywhnone-idnone-labelsnone-confidencenone-metadatanone "Direct link to class-dataframeboundingbox2dbounding_box_xywhnone-idnone-labelsnone-confidencenone-metadatanone")

Extending Annotation class object.

BoundingBox2D object, representing a 2D bounding-box, parsing the set of float values as 5 values as top, left,
width, height, angle (radians) values.

Create a new annotation object

info

In case you need to annotate the same object with more than one annotation type, associate the
annotation objects by giving them the same ID.

- **Parameters**
  - **values** – A sequence of numeric values or a list of sequences of numeric values

  - **id** ( _Optional_ _\[_ _str_ _\]_ ) – String representing the specific annotation. Useful for tracking objects. None is a valid option.

  - **labels** ( _Optional_ _\[_ _Sequence_ _\[_ _str_ _\]_ _\]_ ) – List of labels (string)

  - **confidence** ( _Optional_ _\[_ _float_ _\]_ ) – confidence of annotation

  - **metadata** ( _Optional_ _\[_ _dict_ _\]_ ) – General purpose dictionary storing multiple field/values

  - **bounding\_box\_xywh** ( _Optional_ _\[_ _Sequence_ _\[_ _5_ \\*, \\* _float_ _\]_ _\]_ ) –
- **Return type**

()


* * *

### angle [​](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/\#angle-1 "Direct link to angle")

**property angle**

- **Return type**

`float`

- **Returns**

angle (radians) of the bounding box


* * *

### bounding\_box\_xywh [​](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/\#bounding_box_xywh "Direct link to bounding_box_xywh")

**property bounding\_box\_xywh**

- **Return type**

Sequence\[4, float\]

- **Returns**

list of top x,left y, width, height of the bounding box (float, float, float, float)


* * *

### bounding\_box\_xywha [​](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/\#bounding_box_xywha "Direct link to bounding_box_xywha")

**property bounding\_box\_xywha**

- **Return type**

Sequence\[5, float\]

- **Returns**

list of top x,left y, width, height, angle (radians) of the bounding box
(float, float, float, float, float)


* * *

### get\_bounding\_box [​](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/\#get_bounding_box-4 "Direct link to get_bounding_box")

**get\_bounding\_box()**

Get the bounding box for this 2D bounding box (angle in radians)

- **Return type**

Sequence\[4, float\]

- **Returns**

\[left\_x top\_y width height\]


## _class_ dataframe.BoundingBox3D(bounding\_box\_3d\_xyzwhxyzwh=None, id=None, labels=None, confidence=None, metadata=None) [​](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/\#class-dataframeboundingbox3dbounding_box_3d_xyzwhxyzwhnone-idnone-labelsnone-confidencenone-metadatanone "Direct link to class-dataframeboundingbox3dbounding_box_3d_xyzwhxyzwhnone-idnone-labelsnone-confidencenone-metadatanone")

Extending Annotation class object.

BoundingBox3D object, representing a 3D bounding-box, parsing the set of float values as:
front-top-left corner (triplets x,y,z), front-width, front-height,
back-top-left corner (triplets x,y,z), back-width, back-height

Create a new annotation object

info

In case you need to annotate the same object with more than one annotation type, associate the
annotation objects by giving them the same ID.

- **Parameters**
  - **values** – A sequence of numeric values or a list of sequences of numeric values

  - **id** ( _Optional_ _\[_ _str_ _\]_ ) – String representing the specific annotation. Useful for tracking objects. None is a valid option.

  - **labels** ( _Optional_ _\[_ _Sequence_ _\[_ _str_ _\]_ _\]_ ) – List of labels (string)

  - **confidence** ( _Optional_ _\[_ _float_ _\]_ ) – confidence of annotation

  - **metadata** ( _Optional_ _\[_ _dict_ _\]_ ) – General purpose dictionary storing multiple field/values

  - **bounding\_box\_3d\_xyzwhxyzwh** ( _Optional_ _\[_ _Sequence_ _\[_ _10_ \\*, \\* _float_ _\]_ _\]_ ) –
- **Return type**

()


* * *

### bounding\_box\_3d\_xyzwhxyzwh [​](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/\#bounding_box_3d_xyzwhxyzwh "Direct link to bounding_box_3d_xyzwhxyzwh")

**property bounding\_box\_3d\_xyzwhxyzwh**

- **Return type**

Sequence\[10, float\]

- **Returns**

list of 10 floats: front-top-left corner (triplets x,y,z), front-width, front-height,
back-top-left corner (triplets x,y,z), back-width, back-height


## _class_ dataframe.ImageAnnotation(image\_classes=None, id=None, labels=None, confidence=None, metadata=None) [​](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/\#class-dataframeimageannotationimage_classesnone-idnone-labelsnone-confidencenone-metadatanone "Direct link to class-dataframeimageannotationimage_classesnone-idnone-labelsnone-confidencenone-metadatanone")

Extending Annotation class object.

ImageAnnotation annotation object, representing an image level annotation (applies for the entire image)

Create a new annotation object

info

In case you need to annotate the same object with more than one annotation type, associate the
annotation objects by giving them the same ID.

- **Parameters**
  - **values** – A sequence of numeric values or a list of sequences of numeric values

  - **id** ( _Optional_ _\[_ _str_ _\]_ ) – String representing the specific annotation. Useful for tracking objects. None is a valid option.

  - **labels** ( _Optional_ _\[_ _Sequence_ _\[_ _str_ _\]_ _\]_ ) – List of labels (string)

  - **confidence** ( _Optional_ _\[_ _float_ _\]_ ) – confidence of annotation

  - **metadata** ( _Optional_ _\[_ _dict_ _\]_ ) – General purpose dictionary storing multiple field/values

  - **image\_classes** ( _Optional_ _\[_ _Sequence_ _\[_ _str_ _\]_ _\]_ ) –
- **Return type**

()


- [_class_ dataframe.Annotation(values=None, id=None, labels=None, confidence=None, metadata=None)](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/#class-dataframeannotationvaluesnone-idnone-labelsnone-confidencenone-metadatanone)
  - [label\_enum](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/#label_enum)
  - [Annotation.get\_type](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/#annotationget_type)
  - [values](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/#values)
  - [id](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/#id)
  - [labels](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/#labels)
  - [metadata](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/#metadata)
  - [confidence](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/#confidence)
  - [to\_dict](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/#to_dict)
  - [register](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/#register)
  - [copy](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/#copy)
- [_class_ dataframe.Mask(mask\_rgb=None, id=None, labels=None, confidence=None, metadata=None, mask\_id=None)](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/#class-dataframemaskmask_rgbnone-idnone-labelsnone-confidencenone-metadatanone-mask_idnone)
  - [mask\_id](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/#mask_id)
  - [mask\_rgb](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/#mask_rgb)
- [_class_ dataframe.Polygon2D(polygon\_xy=None, id=None, labels=None, confidence=None, metadata=None)](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/#class-dataframepolygon2dpolygon_xynone-idnone-labelsnone-confidencenone-metadatanone)
  - [get\_bounding\_box](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/#get_bounding_box)
  - [polygon\_xy](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/#polygon_xy)
- [_class_ dataframe.ComplexPolygon2D(polygons\_xy=None, id=None, labels=None, confidence=None, metadata=None)](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/#class-dataframecomplexpolygon2dpolygons_xynone-idnone-labelsnone-confidencenone-metadatanone)
  - [get\_bounding\_box](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/#get_bounding_box-1)
  - [polygons\_xy](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/#polygons_xy)
- [_class_ dataframe.Polygon3D(polygon\_xyz=None, id=None, labels=None, confidence=None, metadata=None)](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/#class-dataframepolygon3dpolygon_xyznone-idnone-labelsnone-confidencenone-metadatanone)
  - [polygon\_xyz](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/#polygon_xyz)
- [_class_ dataframe.ComplexPolygon3D(polygons\_xyz=None, id=None, labels=None, confidence=None, metadata=None)](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/#class-dataframecomplexpolygon3dpolygons_xyznone-idnone-labelsnone-confidencenone-metadatanone)
  - [polygons\_xyz](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/#polygons_xyz)
- [_class_ dataframe.KeyPoints2D(keypoints\_xy=None, id=None, labels=None, confidence=None, metadata=None)](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/#class-dataframekeypoints2dkeypoints_xynone-idnone-labelsnone-confidencenone-metadatanone)
  - [get\_bounding\_box](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/#get_bounding_box-2)
  - [keypoints\_xy](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/#keypoints_xy)
- [_class_ dataframe.KeyPoints3D(keypoints\_xyz=None, id=None, labels=None, confidence=None, metadata=None)](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/#class-dataframekeypoints3dkeypoints_xyznone-idnone-labelsnone-confidencenone-metadatanone)
  - [keypoints\_xyz](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/#keypoints_xyz)
- [_class_ dataframe.Ellipse2D(ellipse2d\_xyrrt=None, id=None, labels=None, confidence=None, metadata=None)](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/#class-dataframeellipse2dellipse2d_xyrrtnone-idnone-labelsnone-confidencenone-metadatanone)
  - [angle](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/#angle)
  - [center](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/#center)
  - [ellipse2d\_xyrrt](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/#ellipse2d_xyrrt)
  - [get\_bounding\_box](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/#get_bounding_box-3)
  - [get\_polygon](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/#get_polygon)
  - [radii](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/#radii)
- [_class_ dataframe.BoundingBox2D(bounding\_box\_xywh=None, id=None, labels=None, confidence=None, metadata=None)](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/#class-dataframeboundingbox2dbounding_box_xywhnone-idnone-labelsnone-confidencenone-metadatanone)
  - [angle](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/#angle-1)
  - [bounding\_box\_xywh](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/#bounding_box_xywh)
  - [bounding\_box\_xywha](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/#bounding_box_xywha)
  - [get\_bounding\_box](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/#get_bounding_box-4)
- [_class_ dataframe.BoundingBox3D(bounding\_box\_3d\_xyzwhxyzwh=None, id=None, labels=None, confidence=None, metadata=None)](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/#class-dataframeboundingbox3dbounding_box_3d_xyzwhxyzwhnone-idnone-labelsnone-confidencenone-metadatanone)
  - [bounding\_box\_3d\_xyzwhxyzwh](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/#bounding_box_3d_xyzwhxyzwh)
- [_class_ dataframe.ImageAnnotation(image\_classes=None, id=None, labels=None, confidence=None, metadata=None)](https://clear.ml/docs/latest/docs/references/hyperdataset/annotation/#class-dataframeimageannotationimage_classesnone-idnone-labelsnone-confidencenone-metadatanone)