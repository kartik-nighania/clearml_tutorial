---
url: "https://clear.ml/docs/latest/docs/getting_started/project_progress/"
title: "Monitoring Project Progress | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/getting_started/project_progress/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

ClearML provides a comprehensive set of monitoring tools to help effectively track and manage machine learning projects.
These tools offer both high-level overviews and detailed insights into task execution, resource
utilization, and project performance.

## Project Overview [​](https://clear.ml/docs/latest/docs/getting_started/project_progress/\#project-overview "Direct link to Project Overview")

A project's **OVERVIEW** tab in the UI presents a general picture of a project:

- Metric Snapshot – A graphical representation of selected metric values across project tasks, offering a quick assessment of progress.
- Task Status Tracking – When a single metric variant is selected for the snapshot, task status is color-coded (e.g.,
Completed, Aborted, Published, Failed) for better visibility.

Use the Metric Snapshot to track project progress and identify trends in task performance.

For more information, see [Project Overview](https://clear.ml/docs/latest/docs/webapp/webapp_project_overview).

![Project Overview](https://clear.ml/docs/latest/assets/images/webapp_project_overview-ff80e42b2f4a598228b4f6e65bf6ab57.png#light-mode-only)![Project Overview](https://clear.ml/docs/latest/assets/images/webapp_project_overview_dark-c48f33871f525010fed7d51241342431.png#dark-mode-only)

## Project Dashboard [​](https://clear.ml/docs/latest/docs/getting_started/project_progress/\#project-dashboard "Direct link to Project Dashboard")

Pro Plan Offering

The Project Dashboard app is available under the ClearML Pro plan.

The [**Project Dashboard**](https://clear.ml/docs/latest/docs/webapp/applications/apps_dashboard) UI application provides a centralized
view of project progress, task statuses, resource usage, and key performance metrics. It offers:

- Comprehensive insights:
  - Track task statuses and trends over time.
  - Monitor GPU utilization and worker activity.
  - Analyze performance metrics.
- Proactive alerts - By integrating with Slack, the Dashboard can notify teams of task failures
and completions.

For more information, see [Project Dashboard](https://clear.ml/docs/latest/docs/webapp/applications/apps_dashboard).

![Project Dashboard](https://clear.ml/docs/latest/assets/images/apps_dashboard-3f4a24dee58b5e2a3dcca898a02a0931.png#light-mode-only)![Project Dashboard](https://clear.ml/docs/latest/assets/images/apps_dashboard_dark-e97e80af4ad3fa889309f86fd03ce5eb.png#dark-mode-only)

## Task Monitoring [​](https://clear.ml/docs/latest/docs/getting_started/project_progress/\#task-monitoring "Direct link to Task Monitoring")

ClearML provides task monitoring capabilities through the [`clearml.automation.Monitor`](https://github.com/clearml/clearml/blob/master/clearml/automation/monitor.py)
class. With this class you can implement monitoring workflows such as:

- Send notifications via Slack or other channels
- Trigger automated responses based on specific task conditions

For a practical example, see the [Slack Alerts Example](https://clear.ml/docs/latest/docs/guides/services/slack_alerts), which demonstrates how to:

- Track task status (completion, failure, etc.)
- Send notifications to a specified Slack channel
- Retrieve task details such as status, console logs, and links to the ClearML Web UI

You can also configure filters for task types and projects to reduce unnecessary notifications.

![Slack Alerts](https://clear.ml/docs/latest/assets/images/examples_slack_alerts-c913fc137100020660bb235541b4d933.png#light-mode-only)![Slack Alerts](https://clear.ml/docs/latest/assets/images/examples_slack_alerts_dark-c262c57275b8dc2901814280d818a649.png#dark-mode-only)

- [Project Overview](https://clear.ml/docs/latest/docs/getting_started/project_progress/#project-overview)
- [Project Dashboard](https://clear.ml/docs/latest/docs/getting_started/project_progress/#project-dashboard)
- [Task Monitoring](https://clear.ml/docs/latest/docs/getting_started/project_progress/#task-monitoring)