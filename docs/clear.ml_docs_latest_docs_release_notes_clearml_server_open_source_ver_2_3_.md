---
url: "https://clear.ml/docs/latest/docs/release_notes/clearml_server/open_source/ver_2_3/"
title: "Version 2.3 | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/release_notes/clearml_server/open_source/ver_2_3/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

### ClearML Server 2.3.0 [​](https://clear.ml/docs/latest/docs/release_notes/clearml_server/open_source/ver_2_3/\#clearml-server-230 "Direct link to ClearML Server 2.3.0")

**New Features and Improvements**

- New Project Workloads dashboard: View project resource utilization by resource, user, and subproject
- New Global Search advanced mode: Direct API filter specification for more specific queries
- Improve single-value scalar Compare view: Separate plot per variant when grouping by metric
- Enable customizing the default name format of cloned tasks

**Bug Fixes**

- Fix UI GCS credentials popup continues reappearing after broken upload [#296](https://github.com/clearml/clearml-server/issues/296)
- Fix UI sometimes fails to load large task console logs [#295](https://github.com/clearml/clearml-server/issues/295)
- Fix deleting parameter in UI task configuration causes other parameters to be duplicated or incorrectly modified
- Fix deleting task in UI removes fileserver folders when "Remove all related artifacts" is not selected
- Fix UI pipeline runs sometimes do not resolve step parameters which are the outputs of previous steps
- Reports
  - Fix scalar plots embedded in UI Reports in full screen mode always grouped by metric
  - Fix embedded plots do not maintain colors specified in code
- Task Comparison
  - Fix Task Scalar Comparison page sometimes displays scalars of tasks removed from comparison
  - Fix Task Scalar Comparison does not merge subplots into single plot
- Task table
  - Fix task status is not updated in the UI Task table when resetting multiple tasks simultaneously
  - Fix UI Task table Tag filter incorrectly switches from "All" to "Any" option
- Global search
  - Fix UI Global Search “Load More” button appears unnecessarily
  - Fix selecting a project in Global Search blocks going back to All Tasks, Models, or the previous tab.
- Object table filters
  - Fix UI object table "Users" filter displays only users who reported tasks, instead of all relevant users.
  - Fix UI tables' Project column filter does not list all projects
- Fix run time of re-enqueued failed/aborted tasks includes time between failed/aborted state and running state
- Fix UI Task and Model tags are not updated when tags are deleted

- [ClearML Server 2.3.0](https://clear.ml/docs/latest/docs/release_notes/clearml_server/open_source/ver_2_3/#clearml-server-230)