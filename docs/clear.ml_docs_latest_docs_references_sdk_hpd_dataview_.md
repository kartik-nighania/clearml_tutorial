---
url: "https://clear.ml/docs/latest/docs/references/sdk/hpd_dataview/"
title: "DataView | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataview/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

## _class_ hyperdatasets.data\_view.DataView(name=None, description=None, tags=None, iteration\_order='sequential', iteration\_infinite=False, iteration\_random\_seed=None, iteration\_limit=None, auto\_connect\_with\_task=True, project\_name=None) [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataview/\#class-hyperdatasetsdata_viewdataviewnamenone-descriptionnone-tagsnone-iteration_ordersequential-iteration_infinitefalse-iteration_random_seednone-iteration_limitnone-auto_connect_with_tasktrue-project_namenone "Direct link to class-hyperdatasetsdata_viewdataviewnamenone-descriptionnone-tagsnone-iteration_ordersequential-iteration_infinitefalse-iteration_random_seednone-iteration_limitnone-auto_connect_with_tasktrue-project_namenone")

Instantiate a DataView wrapper around backend dataview resources.

The dataview aggregates query rules and iteration parameters. When running under a ClearML task it
can optionally auto-connect and restore previously attached definitions.

- **Parameters**
  - **name** (`Optional`\[`str`\]) – Optional dataview name

  - **description** (`Optional`\[`str`\]) – Optional descriptive text

  - **tags** (`Optional`\[`Sequence`\[`str`\]\]) – Optional list of tag strings

  - **iteration\_order** (`str`) – Iteration order (sequential or random)

  - **iteration\_infinite** (`bool`) – Whether to iterate indefinitely

  - **iteration\_random\_seed** (`Optional`\[`int`\]) – Seed used for random iteration

  - **iteration\_limit** (`Optional`\[`int`\]) – Explicit maximum number of frames to iterate (None means unlimited)

  - **auto\_connect\_with\_task** (`bool`) – Auto-attach to the current ClearML task when True

  - **project\_name** (`Optional`\[`str`\]) – Optional project name under which the DataView will be persisted
    when stored. If omitted, falls back to the current Task’s project. Required on
    servers with project-scoped RBAC for the auto-store to succeed.

* * *

### add\_queries [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataview/\#add_queries "Direct link to add_queries")

**add\_queries(queries)**

Append one or more query rules to the dataview.

If the dataview already exists on the backend the remote filter rules are updated immediately and
the attached task is re-synchronised.

- **Parameters**

**queries** ( [`HyperDatasetQuery`](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdatasetquery#clearml.hyperdatasets.data_view.HyperDatasetQuery)) – A HyperDatasetQuery instance or iterable of instances to add


* * *

### add\_query [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataview/\#add_query "Direct link to add_query")

**add\_query( _, project\_id='_', dataset\_id=' _', version\_id='_', source\_query=None, frame\_query=None, weight=1.0, filter\_by\_roi=None, label\_rules=None)**

Construct and append a single HyperDatasetQuery without instantiating it externally.

- **Parameters**
  - **project\_id** (`str`) – Dataset collection identifier or wildcard

  - **dataset\_id** (`str`) – Dataset identifier or wildcard

  - **version\_id** (`str`) – Dataset version identifier

  - **source\_query** (`Optional`\[`str`\]) – Lucene query applied to frame sources

  - **frame\_query** (`Optional`\[`str`\]) – Lucene query applied to frame metadata

  - **weight** (`float`) – Sampling weight when combining multiple queries

  - **filter\_by\_roi** (`Optional`\[`Any`\]) – ROI filtering strategy name

  - **label\_rules** (`Optional`\[`Any`\]) – Optional label rule definitions for ROI filtering
- **Return type**

[`HyperDatasetQuery`](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdatasetquery#clearml.hyperdatasets.data_view.HyperDatasetQuery)

- **Returns**

The created HyperDatasetQuery instance


* * *

### get\_count [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataview/\#get_count "Direct link to get_count")

**get\_count()**

Fetch total frames count from backend and cache it.

Sends an inline DataView spec — no stored id required.

- **Return type**

`int`


* * *

### get\_iteration\_parameters [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataview/\#get_iteration_parameters "Direct link to get_iteration_parameters")

**get\_iteration\_parameters()**

- **Returns**

The cached iteration configuration for this dataview.


* * *

### get\_iterator [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataview/\#get_iterator "Direct link to get_iterator")

**get\_iterator(projection=None, query\_cache\_size=None, query\_queue\_depth=5, allow\_repetition=False, auto\_synthetic\_epoch\_limit=None, node\_id=None, worker\_index=None, num\_workers=None, cache\_in\_memory=False)**

Return an iterator configured to stream frames for this dataview.

- **Parameters**
  - **projection** – Optional projection list selecting frame fields

  - **query\_cache\_size** – Number of frames to request per backend batch

  - **query\_queue\_depth** – Queue depth used by the background fetcher

  - **allow\_repetition** – Enable synthetic epoch length balancing across queries

  - **auto\_synthetic\_epoch\_limit** – Legacy flag equivalent to allow\_repetition

  - **node\_id** – Explicit node identifier to send to the backend

  - **worker\_index** – Worker index when splitting frames across multiple iterators

  - **num\_workers** – Total number of cooperating workers

  - **cache\_in\_memory** – Reserved flag (currently unused)
- **Returns**

Iterator streaming DataEntry-derived objects


* * *

### get\_queries [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataview/\#get_queries "Direct link to get_queries")

**get\_queries()**

Return current HyperDatasetQuery objects attached to this dataview.

- **Return type**

`List`\[ [`HyperDatasetQuery`](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdatasetquery#clearml.hyperdatasets.data_view.HyperDatasetQuery)\]


* * *

### id [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataview/\#id "Direct link to id")

**property id**

Return the backend identifier of the materialised DataView.

- **Returns**

DataView ID string or None when not yet created


* * *

### name [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataview/\#name "Direct link to name")

**property name**

Return the human-readable name assigned to this DataView.

- **Returns**

DataView name string or None


* * *

### prefetch\_local\_sources [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataview/\#prefetch_local_sources "Direct link to prefetch_local_sources")

**prefetch\_local\_sources(num\_workers=None, wait=True, query\_cache\_size=None, get\_previews=False, get\_masks=True, force\_download=False)**

Prefetch data entry sources (and optionally previews/masks) into the local cache.

- num\_workers: number of worker threads (defaults to cpu count via ThreadPoolExecutor)

- wait: block until all prefetch tasks complete

- query\_cache\_size: data entries per backend fetch batch (defaults to iterator default)

- get\_previews: also prefetch preview URIs if available

- get\_masks: also prefetch mask URIs if available

- force\_download: bypass local cache if True


- **Parameters**
  - **num\_workers** ( _Optional_ _\[_ _int_ _\]_ ) –

  - **wait** ( _bool_ ) –

  - **query\_cache\_size** ( _Optional_ _\[_ _int_ _\]_ ) –

  - **get\_previews** ( _bool_ ) –

  - **get\_masks** ( _bool_ ) –

  - **force\_download** ( _bool_ ) –

* * *

### set\_iteration\_parameters [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataview/\#set_iteration_parameters "Direct link to set_iteration_parameters")

**set\_iteration\_parameters(\*, infinite=None, limit=)**

**Persist iteration settings both locally and on the backend if possible.**

**- **Parameters****
**- **infinite** ( _Optional_ _\[_ _bool_ _\]_ ) –**

**- **limit** ( _Union_ _\[_ _int_ \\*, \\* _None_ \\*, \\* _object_ _\]_ ) –**

*** * ***

**### set\_queries [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataview/\#set_queries "Direct link to set_queries")**

****set\_queries(queries)****

**Replace all existing queries with the supplied collection.**

**- **Parameters****

****queries** (`Optional`\[`Iterable`\[ [`HyperDatasetQuery`](https://clear.ml/docs/latest/docs/references/sdk/hpd_hyperdatasetquery#clearml.hyperdatasets.data_view.HyperDatasetQuery)\]\]) – Iterable of HyperDatasetQuery objects; pass None or an empty iterable to clear**

**- **Return type****

**`None`**


*** * ***

**### store [​](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataview/\#store "Direct link to store")**

****store(project\_name=None)****

**Persist this DataView on the server and return its id.**

**DataViews are stored automatically the first time they are iterated, unless**
**`sdk.development.store_dataviews_on_creation` is set to false in clearml.conf —**
**in which case this method is the explicit way to persist one.**

**- **Parameters****

****project\_name** (`Optional`\[`str`\]) – Optional project name to attach the DataView to. Overrides**
**the value passed at construction. If omitted, the constructor’s value**
**(or the current Task’s project as a fallback) is used.**

**- **Return type****

**`str`**

**- **Returns****

**The DataView id assigned by the server.**

**- **Raises****

**The underlying SendError when the server rejects the create call (for**
**example, when the user lacks write permission to the resolved project).**

- [_class_ hyperdatasets.data\_view.DataView(name=None, description=None, tags=None, iteration\_order='sequential', iteration\_infinite=False, iteration\_random\_seed=None, iteration\_limit=None, auto\_connect\_with\_task=True, project\_name=None)](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataview/#class-hyperdatasetsdata_viewdataviewnamenone-descriptionnone-tagsnone-iteration_ordersequential-iteration_infinitefalse-iteration_random_seednone-iteration_limitnone-auto_connect_with_tasktrue-project_namenone)
  - [add\_queries](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataview/#add_queries)
  - [add\_query](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataview/#add_query)
  - [get\_count](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataview/#get_count)
  - [get\_iteration\_parameters](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataview/#get_iteration_parameters)
  - [get\_iterator](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataview/#get_iterator)
  - [get\_queries](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataview/#get_queries)
  - [id](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataview/#id)
  - [name](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataview/#name)
  - [prefetch\_local\_sources](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataview/#prefetch_local_sources)
  - [set\_iteration\_parameters](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataview/#set_iteration_parameters)
  - [set\_queries](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataview/#set_queries)
  - [store](https://clear.ml/docs/latest/docs/references/sdk/hpd_dataview/#store)