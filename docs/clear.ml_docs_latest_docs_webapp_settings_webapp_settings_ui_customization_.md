---
url: "https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_ui_customization/"
title: "UI Customization | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_ui_customization/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

Enterprise Feature

The UI Customization admin settings page is available under the ClearML Enterprise plan.

## Task Clone Name Template [​](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_ui_customization/\#task-clone-name-template "Direct link to Task Clone Name Template")

Control the template used to provide default suggestions for [cloning tasks](https://clear.ml/docs/latest/docs/webapp/webapp_exp_reproducing) e.g. `"Clone Of <Original task name>"`.

The template supports dynamic variable references that are filled in when a task is cloned:

- `${name}` \- The original task’s name
- `${date}` – The time the clone was created (e.g. `21/3/2025 12:45:15`)

## Hyper-Dataset New Version Name Template [​](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_ui_customization/\#hyper-dataset-new-version-name-template "Direct link to Hyper-Dataset New Version Name Template")

Control the default name assigned to a new Hyper-Dataset version when it is created.

The template supports dynamic variables that are filled when a version is created:

- `${dataset}` \- The dataset name
- `${version}` \- The parent version name
- `${date}` \- The version creation time (e.g., `21/3/2025 12:45:15`)

- [Task Clone Name Template](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_ui_customization/#task-clone-name-template)
- [Hyper-Dataset New Version Name Template](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_ui_customization/#hyper-dataset-new-version-name-template)