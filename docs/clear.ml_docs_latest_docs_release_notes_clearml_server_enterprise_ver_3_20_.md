---
url: "https://clear.ml/docs/latest/docs/release_notes/clearml_server/enterprise/ver_3_20/"
title: "Version 3.20 | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/release_notes/clearml_server/enterprise/ver_3_20/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

### Enterprise Server 3.20.4 [​](https://clear.ml/docs/latest/docs/release_notes/clearml_server/enterprise/ver_3_20/\#enterprise-server-3204 "Direct link to Enterprise Server 3.20.4")

**Bug Fix**

- Fix access cannot be granted to UI Application projects through access rules

### Enterprise Server 3.20.3 [​](https://clear.ml/docs/latest/docs/release_notes/clearml_server/enterprise/ver_3_20/\#enterprise-server-3203 "Direct link to Enterprise Server 3.20.3")

**Bug Fix**

- Fix batch deletes from files server sometimes does not work

### Enterprise Server 3.20.2 [​](https://clear.ml/docs/latest/docs/release_notes/clearml_server/enterprise/ver_3_20/\#enterprise-server-3202 "Direct link to Enterprise Server 3.20.2")

**Bug Fixes**

- Fix clicking on UI Metric Snapshot datapoint does not navigate to experiment
- Fix missing experiment labels in UI experiment plot comparison
- Fix starting time not updating for some tasks
- Fix S3/Minio file deletion broken in non-default region

### Enterprise Server 3.20.1 [​](https://clear.ml/docs/latest/docs/release_notes/clearml_server/enterprise/ver_3_20/\#enterprise-server-3201 "Direct link to Enterprise Server 3.20.1")

**New Feature**

- Add support for serving UI from a subpath

**Bug Fixes**

- Fix UI experiment plot comparison displays duplicates of image plots
- Fix downloading UI experiment console log sometimes returns an older file

### Enterprise Server 3.20.0 [​](https://clear.ml/docs/latest/docs/release_notes/clearml_server/enterprise/ver_3_20/\#enterprise-server-3200 "Direct link to Enterprise Server 3.20.0")

**New Features and Improvements**

- Add Administrator identity provider management UI: administrators can add and manage multiple identity providers
- New UI experiment table comparative view: compare plots and scalars of all selected experiments
- Add UI project metric snapshot support for multiple metrics
- Add UI experiment display of original Python requirements along with actual packages used.
- Add compressed UI experiment table info panel mode displaying only experiment name and status
- Add "x unified" hover mode to UI plots
- Add option to view metadata of published dataset versions in UI Hyper-Dataset list view
- Add experiment hyperparameter UI section dataset IDs link to datasets page
- Make all URLs clickable in UI experiment artifacts
- Redesign WebApp tabs: Tabs now appear in UI header
- Add option to force setting original task as clone's parent when cloning a task

**Bug Fixes**

- Fix CVE-2023-45133 Web App vulnerability
- Fix "select all" in UI dataset archive counts also unarchived datasets
- Fix hyperparameter keys with dots in their names displayed incorrectly in UI experiment table and task info
- Fix UI experiment scalar comparison raising error
- Fix “Project” column redundantly appears inside a specific project's model table
- Fix UI models with many labels slowing down web app
- Fix Hyper-Dataset version list collapsed by default in UI DataView preview
- Fix when invalid source query filter is applied to UI Hyper-Dataset version, navigating to frame raises an error
- Fix can't select root project in UI report creation modal when workspace has no projects
- Fix UI plot "Show/hide" legend button sometimes disappears
- Fix "load more" button displayed unnecessarily in UI object tables

- [Enterprise Server 3.20.4](https://clear.ml/docs/latest/docs/release_notes/clearml_server/enterprise/ver_3_20/#enterprise-server-3204)
- [Enterprise Server 3.20.3](https://clear.ml/docs/latest/docs/release_notes/clearml_server/enterprise/ver_3_20/#enterprise-server-3203)
- [Enterprise Server 3.20.2](https://clear.ml/docs/latest/docs/release_notes/clearml_server/enterprise/ver_3_20/#enterprise-server-3202)
- [Enterprise Server 3.20.1](https://clear.ml/docs/latest/docs/release_notes/clearml_server/enterprise/ver_3_20/#enterprise-server-3201)
- [Enterprise Server 3.20.0](https://clear.ml/docs/latest/docs/release_notes/clearml_server/enterprise/ver_3_20/#enterprise-server-3200)