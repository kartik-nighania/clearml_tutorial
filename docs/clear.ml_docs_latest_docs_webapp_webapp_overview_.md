---
url: "https://clear.ml/docs/latest/docs/webapp/webapp_overview/"
title: "WebApp | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/webapp/webapp_overview/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The **ClearML Web UI** is the graphical user interface for the ClearML platform, which includes:

- ML workload automation
- Resource utilization monitoring and management
- Live model endpoint monitoring
- ML experiment management and visualization
- Model and Dataset viewing and management
- Pipeline creation and monitoring
- User and administrator settings

![WebApp screenshots gif](https://clear.ml/docs/latest/assets/images/webapp_screenshots-b21cff0556b12f91d7029aee7c291d11.gif#light-mode-only)![WebApp screenshots gif](https://clear.ml/docs/latest/assets/images/webapp_screenshots_dark-2b70c69e0b9e16fac0ca95db31e0ec57.gif#dark-mode-only)

## UI Modules [​](https://clear.ml/docs/latest/docs/webapp/webapp_overview/\#ui-modules "Direct link to UI Modules")

The WebApp's sidebar provides access to the following modules:

- ![ClearML Apps](https://clear.ml/docs/latest/icons/ico-applications.svg)[Applications](https://clear.ml/docs/latest/docs/webapp/applications/apps_overview) \- ClearML's GUI applications for no-code workflow execution (available in the ClearML Pro and Enterprise plans).

- ![Workers and Queues](https://clear.ml/docs/latest/icons/ico-workers.svg)[Orchestration](https://clear.ml/docs/latest/docs/webapp/webapp_workers_queues) \- Autoscaling, resource usage monitoring and allocation management.

- ![Model endpoints](https://clear.ml/docs/latest/icons/ico-model-endpoints.svg)[Model Endpoints](https://clear.ml/docs/latest/docs/webapp/webapp_model_endpoints) \- Monitor your live model endpoints.

- ![Datasets](https://clear.ml/docs/latest/icons/ico-side-bar-datasets.svg)[Datasets](https://clear.ml/docs/latest/docs/webapp/datasets/webapp_dataset_page) \- View and manage your datasets.

- ![Projects](https://clear.ml/docs/latest/icons/ico-projects.svg)[Projects](https://clear.ml/docs/latest/docs/webapp/webapp_projects_page) \- The main experimentation page. Access your tasks and models as they are organized into projects. The tasks and models are displayed in tables which let you:
  - Track ongoing tasks and visualize their results
  - Reproduce previous task runs
  - Tune task parameter values with no code change
  - Compare tasks and models
  - Share tasks and models with other ClearML hosted service users
  - Create and share rich content [Reports](https://clear.ml/docs/latest/docs/webapp/webapp_reports)
- ![Pipelines](https://clear.ml/docs/latest/icons/ico-pipelines.svg)[Pipelines](https://clear.ml/docs/latest/docs/webapp/pipelines/webapp_pipeline_page) \- View and manage your pipelines.


## UI Top Bar [​](https://clear.ml/docs/latest/docs/webapp/webapp_overview/\#ui-top-bar "Direct link to UI Top Bar")

### Settings Menu [​](https://clear.ml/docs/latest/docs/webapp/webapp_overview/\#settings-menu "Direct link to Settings Menu")

Click the profile menu button ![Profile button](https://clear.ml/docs/latest/icons/ico-me.svg)
to access the following:

- **Settings** \- Navigate to ClearML's [Settings](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_profile) page:

  - Set personal [WebApp preferences](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_profile)
  - Manage [workspace API credentials](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_profile#clearml-api-credentials)
  - Manage [personal configuration vault](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_profile#configuration-vault) (Enterprise offering)
  - Configure [cloud storage access credentials](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_profile#browser-cloud-storage-access) for the ClearML Web UI
  - Administrator settings
    - Manage [users and workspaces](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_users)
    - View [usage and billing](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_usage_billing) information (Free Hosted Service)
    - Manage [access rules](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_access_rules) (available in the ClearML Enterprise plan)
    - Define [configuration vaults](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_admin_vaults) to apply to designated user groups (available in the ClearML Enterprise plan)
    - Manage [server identity providers](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_id_providers) (available in the ClearML Enterprise plan)
    - Define the [resource access policies](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_resource_configs) (available in the ClearML Enterprise plan)
- Workspace Control (Free Hosted Service)
  - **Invite a User** to your workspace (supported in hosted service). Click **Invite a User** \> input user's
    email > click **ADD** \> page redirects to the [Users & Groups](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_users#user-groups) section of
    the **Settings** page
  - **Switch to Workspace** \- Hosted service users can be members of multiple workspaces. These workspaces are listed here.
    Click a workspace to switch to.
- Appearance - Select the UI color scheme:
  - Light: ClearML will be in a light theme.
  - Dark: ClearML will be in a dark theme.
  - System: ClearML will follow your device’s theme.
- **Logout** of ClearML

### Finding What You're Looking for [​](https://clear.ml/docs/latest/docs/webapp/webapp_overview/\#finding-what-youre-looking-for "Direct link to Finding What You're Looking for")

The ClearML UI provides two search options on most pages:

- **In-page search**: Each object (e.g. projects, tasks etc.) page includes its own search bar ![Magnifying glass](https://clear.ml/docs/latest/icons/ico-search.svg)
for filtering the objects shown on that page. This search focuses on attributes relevant to that object type:


  - Projects: show projects whose name or ID match the searched text
  - Tasks: show tasks whose name, ID, description, or input/output models match the searched text
  - Models: show models whose name, ID, or description match the searched text.
  - Dataviews: show dataviews whose name, ID, description, hyper-datasets, or hyper-dataset versions match the searched text.
  - Reports: show reports whose name, ID, tags, project, description, or content match the searched text.
  - Datasets: show datasets whose name, ID, or description match the searched text
  - Pipeline Runs: show reports whose name, ID, or description match the searched text


Additional filtering

ClearML's object tables (e.g. [tasks](https://clear.ml/docs/latest/docs/webapp/webapp_exp_table), [models](https://clear.ml/docs/latest/docs/webapp/webapp_model_table), [pipelines](https://clear.ml/docs/latest/docs/webapp/pipelines/webapp_pipeline_table),
and [datasets](https://clear.ml/docs/latest/docs/webapp/datasets/webapp_dataset_page)) provide column filters to easily focus your search by object properties
(e.g. status, creation/update time, metric values, etc.).

- **Global search**: The search bar ![Magnifying glass](https://clear.ml/docs/latest/icons/ico-search.svg)
in the top banner ClearML for any objects that match the queries as specified above and
returns results grouped by object type (projects, tasks, models, etc.).

Use the Advanced Search (![advanced search](https://clear.ml/docs/latest/icons/ico-code.svg))
to apply more elaborate and specific filters. Specify explicit API filters (e.g. `task_filter` in [`Task.query_tasks()`](https://clear.ml/docs/latest/docs/references/sdk/task#taskquery_tasks))
in JSON format. For example:





```text
{"status": ["stopped"], "order_by": ["-last_update"], "_all_": {"fields": ["script.repository"], "pattern": "github.com/user"}})
```


To use regular expressions, click the `.*` icon in the search bar.

![WebApp Search options](https://clear.ml/docs/latest/assets/images/webapp_search_options-56af1025844fadd8cc5ebe4ddc6f80e1.png#light-mode-only)![WebApp Search options](https://clear.ml/docs/latest/assets/images/webapp_search_options_dark-c6a1cdf0a4fcdbd8a02bfa26e4d258ca.png#dark-mode-only)

### Helpful Resources [​](https://clear.ml/docs/latest/docs/webapp/webapp_overview/\#helpful-resources "Direct link to Helpful Resources")

Click the help menu button ![Help menu](https://clear.ml/docs/latest/icons/ico-help-outlined.svg)
in the top right corner of the web UI screen to access the self-help resources including:

- ClearML Python Package setup - Instruction to get started with the `clearml` Python package
- [ClearML on YouTube](https://www.youtube.com/c/ClearML/featured)![YouTube](https://clear.ml/docs/latest/icons/ico-youtube.svg) \- Instructional videos on integrating ClearML into your workflow
- Online Documentation
- Pro Tips - Tips for working with ClearML efficiently
- [Contact Us](https://clear.ml/contact-us) \- Quick access to ClearML contact form

- [UI Modules](https://clear.ml/docs/latest/docs/webapp/webapp_overview/#ui-modules)
- [UI Top Bar](https://clear.ml/docs/latest/docs/webapp/webapp_overview/#ui-top-bar)
  - [Settings Menu](https://clear.ml/docs/latest/docs/webapp/webapp_overview/#settings-menu)
  - [Finding What You're Looking for](https://clear.ml/docs/latest/docs/webapp/webapp_overview/#finding-what-youre-looking-for)
  - [Helpful Resources](https://clear.ml/docs/latest/docs/webapp/webapp_overview/#helpful-resources)