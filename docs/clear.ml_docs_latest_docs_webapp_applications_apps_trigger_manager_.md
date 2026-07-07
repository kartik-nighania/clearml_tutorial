---
url: "https://clear.ml/docs/latest/docs/webapp/applications/apps_trigger_manager/"
title: "Trigger Manager | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/webapp/applications/apps_trigger_manager/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

Enterprise Feature

The Trigger Manager application is available under the ClearML Enterprise plan.

ClearML's Trigger Manager Application lets you define tasks to be run when predefined events occur. The Trigger Manager
is useful for automating your workflows: trigger training a model whenever a new dataset is tagged with a specific tag,
or running a pipeline when a new model is published.

Each trigger is configured to run a ClearML task when its specifications are met.

The events which can activate a trigger include:

- Status change of an object (task, dataset, or model)
- Tagging of an object
- For task triggers, crossing a specified metric threshold

The app monitors your workspace for trigger events and will launch copies of the specified task when the trigger is activated.

Once you have launched an app instance, you can view the console log in the instance's dashboard. The log shows the
instance's activity: periodic polling and triggered events.

![Trigger dashboard](https://clear.ml/docs/latest/assets/images/apps_trigger_manager_dashboard-21b2ced1a966e531a1d027c1b79a356c.png#light-mode-only)![Trigger dashboard](https://clear.ml/docs/latest/assets/images/apps_trigger_manager_dashboard_dark-57cb57eed4d3514d81aefb3a6191d8fc.png#dark-mode-only)

## Trigger Manager Instance Configuration [​](https://clear.ml/docs/latest/docs/webapp/applications/apps_trigger_manager/\#trigger-manager-instance-configuration "Direct link to Trigger Manager Instance Configuration")

When configuring a new Trigger Manager instance, you can fill in the required parameters or reuse the
configuration of a previously launched instance.

Launch an app instance with the configuration of a previously launched instance using one of the following options:

- Cloning a previously launched app instance will open the instance launch form with the original instance's
configuration prefilled.
- Importing an app configuration file. You can export the configuration of a previously launched instance as a JSON file
when viewing its configuration.

The prefilled configuration form can be edited before launching the new app instance.

To configure a new app instance, click `Launch New`![Add new](https://clear.ml/docs/latest/icons/ico-add.svg)
to open the app's configuration form.

### Configuration Options [​](https://clear.ml/docs/latest/docs/webapp/applications/apps_trigger_manager/\#configuration-options "Direct link to Configuration Options")

note

Administrators can [customize](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/app_launch_form_custom) the launch form and
modify field names and/or available options and defaults.

This section describes the default configuration provided by ClearML.

- **Import Configuration** \- Import an app instance configuration file. This will fill the instance launch form with the
values from the file, which can be modified before launching the app instance
- **Name** \- Name for the app instance. This will appear in the instance list
- **Triggers**\- Events whose occurrence will cause a task to be executed

  - Task ID - Select a task or enter its ID. This task will be cloned and enqueued for execution when the trigger is activated.
    Click **Select** to open the task selection modal, where you can browse and search for a task, then apply it.
  - Target Project - The project where the task will be cloned to
  - Queue - The ClearML Queue to which cloned tasks are enqueued (make sure an agent is assigned to that queue)
  - Override Task Hyperparameters - Override parameters in the cloned task. Input the original task's configuration
    parameter name (including section name e.g. Args/lr). Use UNIX shell-like syntax (splits on whitespace)
  - Trigger Type - Triggers can be activated by model, dataset, and/or task activity. Choose which object type to monitor.
    - Object selection criteria:
      - Match Project - Monitor objects in projects that match this name only
      - Match Name - Monitor objects that match this name. Supports both string and Python regex match
      - Trigger on Any Tags - Trigger if the object is tagged with _ANY_ of the specified tags (comma separated list)
      - Trigger on All Tags - Trigger if the object is tagged with _ALL_ of the specified tags (comma separated list)
    - Trigger events for Datasets and Models:
      - Trigger on Publish - Activate trigger when a Dataset/Model is published
      - Trigger on Archive - Activate trigger when a Dataset/Model is archived
    - Trigger events for Tasks:
      - Trigger on Status Change - Activate trigger when a task's status changes to the selected state.
      - Trigger on scalar - Activate trigger when a task's specific metric crosses a threshold:
        - Metric - Title of metric
        - Variant - Metric's variant (series)
        - Condition - Activate trigger if the value goes over/under the specified threshold
        - Threshold - The metric threshold to monitor
  - Add item - Add another trigger
- **Polling frequency** \- Time period in minutes at which the workspace is polled for trigger events
- **Export Configuration** \- Export the app instance configuration as a JSON file, which you can later import to create
a new instance with the same configuration

![Trigger manager instance launch form](https://clear.ml/docs/latest/assets/images/apps_trigger_manager_wizard-96fbd80bf1a394a3fbac6463d2ef5e6d.png#light-mode-only)![Trigger manager instance launch form](https://clear.ml/docs/latest/assets/images/apps_trigger_manager_wizard_dark-acd71015cb01c54e991bf7ac260084d5.png#dark-mode-only)

- [Trigger Manager Instance Configuration](https://clear.ml/docs/latest/docs/webapp/applications/apps_trigger_manager/#trigger-manager-instance-configuration)
  - [Configuration Options](https://clear.ml/docs/latest/docs/webapp/applications/apps_trigger_manager/#configuration-options)