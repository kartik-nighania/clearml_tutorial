---
url: "https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdatasetquery/"
title: "HyperDatasetQuery | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdatasetquery/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

## _class_ hyperdatasets.data\_view.HyperDatasetQuery(project\_id='\*', dataset\_id='\*', version\_id='\*', source\_query=None, frame\_query=None, weight=1.0, filter\_by\_roi=None, label\_rules=None) [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdatasetquery/\#class-hyperdatasetsdata_viewhyperdatasetqueryproject_id-dataset_id-version_id-source_querynone-frame_querynone-weight10-filter_by_roinone-label_rulesnone "Direct link to class-hyperdatasetsdata_viewhyperdatasetqueryproject_id-dataset_id-version_id-source_querynone-frame_querynone-weight10-filter_by_roinone-label_rulesnone")

Construct a hyper-dataset query filter.

When concrete dataset/version IDs are supplied the constructor verifies their existence via
HyperDatasetManagement. Optional Lucene queries, ROI filtering, and sampling weights can be
provided to further refine the query.

- **Parameters**
  - **project\_id** (`str`) – Dataset collection identifier or wildcard

  - **dataset\_id** (`str`) – Dataset identifier or wildcard (legacy) used when version is omitted

  - **version\_id** (`str`) – Dataset version identifier; defaults to dataset\_id when empty

  - **source\_query** (`Optional`\[`str`\]) – Lucene query applied to frame source metadata

  - **frame\_query** (`Optional`\[`str`\]) – Lucene query applied to frame metadata

  - **weight** (`float`) – Relative sampling weight for this query

  - **filter\_by\_roi** (`Optional`\[`Any`\]) – Optional ROI filtering strategy

  - **label\_rules** (`Optional`\[`Any`\]) – Optional label-rule dictionaries for ROI filtering

* * *

### dataset\_id [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdatasetquery/\#dataset_id "Direct link to dataset_id")

**property dataset\_id: str**

Return the dataset identifier targeted by this query.

- **Return type**

`str`

- **Returns**

Dataset ID string or wildcard marker


* * *

### filter\_by\_roi [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdatasetquery/\#filter_by_roi "Direct link to filter_by_roi")

**property filter\_by\_roi: Optional\[Any\]**

Return the ROI filtering strategy configured for this query.

- **Return type**

`Optional`\[`Any`\]

- **Returns**

ROI filter identifier or None


* * *

### frame\_query [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdatasetquery/\#frame_query "Direct link to frame_query")

**property frame\_query: Optional\[str\]**

Return the Lucene query applied to frame-level metadata.

- **Return type**

`Optional`\[`str`\]

- **Returns**

Lucene query string or None


* * *

### label\_rules [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdatasetquery/\#label_rules "Direct link to label_rules")

**property label\_rules: Optional\[Sequence\[Any\]\]**

Return the label rule definitions used for ROI filtering.

- **Return type**

`Optional`\[`Sequence`\[`Any`\]\]

- **Returns**

Sequence of mapping of label rules, or None


* * *

### project\_id [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdatasetquery/\#project_id "Direct link to project_id")

**property project\_id: str**

Return the dataset collection identifier associated with this query.

- **Return type**

`str`

- **Returns**

Project ID string or wildcard marker


* * *

### source\_query [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdatasetquery/\#source_query "Direct link to source_query")

**property source\_query: Optional\[str\]**

Return the Lucene query applied to frame source metadata.

- **Return type**

`Optional`\[`str`\]

- **Returns**

Lucene query string or None


* * *

### version\_id [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdatasetquery/\#version_id "Direct link to version_id")

**property version\_id: str**

Return the dataset version identifier resolved for this query.

- **Return type**

`str`

- **Returns**

Version ID string or wildcard marker


* * *

### weight [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdatasetquery/\#weight "Direct link to weight")

**property weight: float**

Return the relative sampling weight assigned to this query.

- **Return type**

`float`

- **Returns**

Sampling weight as a float


- [_class_ hyperdatasets.data\_view.HyperDatasetQuery(project\_id='\*', dataset\_id='\*', version\_id='\*', source\_query=None, frame\_query=None, weight=1.0, filter\_by\_roi=None, label\_rules=None)](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdatasetquery/#class-hyperdatasetsdata_viewhyperdatasetqueryproject_id-dataset_id-version_id-source_querynone-frame_querynone-weight10-filter_by_roinone-label_rulesnone)
  - [dataset\_id](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdatasetquery/#dataset_id)
  - [filter\_by\_roi](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdatasetquery/#filter_by_roi)
  - [frame\_query](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdatasetquery/#frame_query)
  - [label\_rules](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdatasetquery/#label_rules)
  - [project\_id](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdatasetquery/#project_id)
  - [source\_query](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdatasetquery/#source_query)
  - [version\_id](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdatasetquery/#version_id)
  - [weight](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdatasetquery/#weight)