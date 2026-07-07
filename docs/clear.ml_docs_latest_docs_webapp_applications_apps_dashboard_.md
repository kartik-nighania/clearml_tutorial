---
url: "https://clear.ml/docs/latest/docs/webapp/applications/apps_dashboard/"
title: "Project Dashboard | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/webapp/applications/apps_dashboard/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

Pro Plan Offering

The ClearML Project Dashboard App is available under the ClearML Pro plan.

The Project Dashboard Application provides an overview of a project's or workspace's progress. It presents an aggregated
view of task status and a chosen metric over time, as well as project GPU and worker usage. It also supports alerts/warnings
on completed/failed Tasks via Slack integration.

Once you have launched an app instance, you can view the following information in its dashboard:

- Task Status Summary - Percentages of Tasks by status
- Task Type Summary - Percentages of local tasks vs. agent tasks
- Task Summary - Number of tasks by status over time
- Monitoring - GPU utilization and GPU memory usage
- Metric Monitoring - An aggregated view of the values of a metric over time
- Project's Active Workers - Number of workers currently executing tasks in the monitored project
- Workers Table - List of active workers
- Task Alerts
  - Failed tasks - Failed tasks and their time of failure summary
  - Completed tasks - Completed tasks and their time of completion summary

![App dashboard](https://clear.ml/docs/latest/assets/images/apps_dashboard-3f4a24dee58b5e2a3dcca898a02a0931.png#light-mode-only)![App dashboard](https://clear.ml/docs/latest/assets/images/apps_dashboard_dark-e97e80af4ad3fa889309f86fd03ce5eb.png#dark-mode-only)

Embedding ClearML Visualization

You can embed plots from the app instance dashboard into [ClearML Reports](https://clear.ml/docs/latest/docs/webapp/webapp_reports). The Enterprise Plan and
Hosted Service also support embedding resources in third-party platforms that support embedded content (e.g. Notion). These visualizations
are updated live as the app instance(s) updates. Hover over the plot and click ![Embed code](https://clear.ml/docs/latest/icons/ico-plotly-embed-code.svg)
to copy the embed code, and navigate to a report to paste the embed code.

## Project Dashboard Instance Configuration [​](https://clear.ml/docs/latest/docs/webapp/applications/apps_dashboard/\#project-dashboard-instance-configuration "Direct link to Project Dashboard Instance Configuration")

When configuring a new Project Dashboard instance, you can fill in the required parameters or reuse the
configuration of a previously launched instance.

Launch an app instance with the configuration of a previously launched instance using one of the following options:

- Cloning a previously launched app instance will open the instance launch form with the original instance's
configuration prefilled.
- Importing an app configuration file. You can export the configuration of a previously launched instance as a JSON file
when viewing its configuration.

The prefilled configuration form can be edited before launching the new app instance.

To configure a new app instance, click `Launch New`![Add new](https://clear.ml/docs/latest/icons/ico-add.svg)
to open the app's configuration form.

### Configuration Options [​](https://clear.ml/docs/latest/docs/webapp/applications/apps_dashboard/\#configuration-options "Direct link to Configuration Options")

note

Administrators can [customize](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/app_launch_form_custom) the launch form and
modify field names and/or available options and defaults.

This section describes the default configuration provided by ClearML.

- **Import Configuration** \- Import an app instance configuration file. This will fill the instance launch form with the
values from the file, which can be modified before launching the app instance

- **Dashboard Title** \- Name of the project dashboard instance, which will appear in the instance list

- **Monitoring** \- Select what the app instance should monitor. The options are:


  - Project - Monitor a specific project. You can select an option to also monitor the specified project's subprojects
  - Entire workspace - Monitor all projects in your workspace


warning

If your workspace or specified project contains a large number of tasks, the dashboard can take a while to update.

- **Monitored Metric** \- Specify a metric for the app instance to monitor. The dashboard will present an aggregated view
of the chosen metric over time.
  - Monitored Metric - Title - Metric title to track
  - Monitored Metric - Series - Metric series (variant) to track
  - Monitored Metric - Trend - Choose whether to track the monitored metric's highest or lowest values
- **Slack Notification** (optional) - Set up Slack integration for notifications of task failure. Select the
`Alert on completed tasks` under `Additional options` to set up alerts for task completions.
  - API Token - Slack workspace access token
  - Channel Name - Slack channel to which task failure alerts will be posted
  - Alert Iteration Threshold - Minimum number of task iterations to trigger Slack alerts (tasks that fail prior to the threshold will be ignored)
- **Additional options**
  - Track manual (non agent-run) tasks as well - Select to include in the dashboard tasks that were not executed by an agent
  - Alert on completed tasks - Select to include completed tasks in alerts: in the dashboard's Task Alerts section and in Slack Alerts.
- **Export Configuration** \- Export the app instance configuration as a JSON file, which you can later import to create
a new instance with the same configuration.


![Dashboard app instance launch form](https://clear.ml/docs/latest/assets/images/apps_dashboard_wizard-60e7b62bcf47db116d32fb3d7252ab0f.png#light-mode-only)![Dashboard app instance launch form](https://clear.ml/docs/latest/assets/images/apps_dashboard_wizard_dark-40630d7c5d34d9b1ea7fb07a42e6685d.png#dark-mode-only)

- [Project Dashboard Instance Configuration](https://clear.ml/docs/latest/docs/webapp/applications/apps_dashboard/#project-dashboard-instance-configuration)
  - [Configuration Options](https://clear.ml/docs/latest/docs/webapp/applications/apps_dashboard/#configuration-options)