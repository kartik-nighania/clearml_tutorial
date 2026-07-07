---
url: "https://clear.ml/docs/latest/docs/webapp/applications/apps_task_scheduler/"
title: "Task Scheduler | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/webapp/applications/apps_task_scheduler/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

Enterprise Feature

The Task Scheduler application is available under the ClearML Enterprise plan.

ClearML's Task Scheduler Application lets you schedule tasks for one-shot and/or periodic execution at specified times.
The Scheduler is useful for scheduling routine operations, such as backups, generating reports, as well
as periodically running pipelines for updating data and models.

Each scheduling job is configured with ClearML tasks and a scheduling specification for each task: the time
for execution and recurrence type. The Scheduler app will then launch copies of the specified tasks at their specified
times.

Once you have launched an app instance, you can view the following information in its dashboard:

- Scheduled Tasks - Table of tasks scheduled for execution. The table displays the ID of the task scheduled for execution,
the queue where it will be enqueued, and when it is scheduled to be executed. Each row presents a specific time that
the task is scheduled to be executed (both recurring and not). In the image below, the task in the first row is
scheduled to be launched daily (`day=1`) at 06:20 UTC (`minute=20, hour=6`).
The task in the third row is scheduled to be launched every month (`month=1`) on the 15th at 12:00 UTC (`day=15, hour=12`).

![TaskScheduler scheduler tasks](https://clear.ml/docs/latest/assets/images/apps_taskscheduler_scheduled_tasks-800f00686cf0c871b88e397f7b566168.png#light-mode-only)![TaskScheduler scheduler tasks](https://clear.ml/docs/latest/assets/images/apps_taskscheduler_scheduled_tasks_dark-048a097748b80fb603f91db71ecbc0af.png#dark-mode-only)

- Executed Tasks - Table of tasks that have been executed. The table displays the `started` time, which is the time
the task was enqueued, and its `finished` time, which is the time the task's execution was completed. If it says `None`,
under the `finished` column, the task has not yet completed its execution.

![TaskScheduler executed tasks](https://clear.ml/docs/latest/assets/images/apps_taskscheduler_executed_tasks-a0f467be9cd34a249c5886da9cdfed2e.png#light-mode-only)![TaskScheduler executed tasks](https://clear.ml/docs/latest/assets/images/apps_taskscheduler_executed_tasks_dark-3cfcc0e2f6044fcf188f0afd9fc512f1.png#dark-mode-only)

- Scheduler Log - Application console log containing everything printed to stdout and stderr. The log
includes when the scheduler syncs, and when it launches tasks for execution.


![TaskScheduler dashboard](https://clear.ml/docs/latest/assets/images/apps_taskscheduler_dashboard-53566ff432c65a69dcf46adf05e83f15.png#light-mode-only)![TaskScheduler dashboard](https://clear.ml/docs/latest/assets/images/apps_taskscheduler_dashboard_dark-8186060d9c3cfc15b5af2aec3d460375.png#dark-mode-only)

Embedding ClearML Visualization

You can embed plots from the app instance dashboard into [ClearML Reports](https://clear.ml/docs/latest/docs/webapp/webapp_reports) and other third-party platforms that support embedded content
(e.g. Notion). These visualizations are updated live as the app instance(s) updates. Hover over the plot and click ![Embed code](https://clear.ml/docs/latest/icons/ico-plotly-embed-code.svg)
to copy the embed code, and navigate to a report to paste the embed code.

## Scheduler Instance Configuration [​](https://clear.ml/docs/latest/docs/webapp/applications/apps_task_scheduler/\#scheduler-instance-configuration "Direct link to Scheduler Instance Configuration")

When configuring a new Task Scheduler instance, you can fill in the required parameters or reuse the
configuration of a previously launched instance.

Launch an app instance with the configuration of a previously launched instance using one of the following options:

- Cloning a previously launched app instance will open the instance launch form with the original instance's
configuration prefilled.
- Importing an app configuration file. You can export the configuration of a previously launched instance as a JSON file
when viewing its configuration.

The prefilled configuration form can be edited before launching the new app instance.

To configure a new app instance, click `Launch New`![Add new](https://clear.ml/docs/latest/icons/ico-add.svg)
to open the app's configuration form.

### Configuration Options [​](https://clear.ml/docs/latest/docs/webapp/applications/apps_task_scheduler/\#configuration-options "Direct link to Configuration Options")

note

Administrators can [customize](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/app_launch_form_custom) the launch form and
modify field names and/or available options and defaults.

This section describes the default configuration provided by ClearML.

- **Import Configuration** \- Import an app instance configuration file. This will fill the instance launch form with the
values from the file, which can be modified before launching the app instance
- **Scheduled Tasks**
  - **Base Task ID** \- Select a task or enter its ID. This task will be cloned and enqueued for execution at the specified
    time. Click **Select** to open the task selection modal, where you can browse and search for a task, then apply it.
  - **Destination Project** \- The project where the task will be cloned to.
  - **Queue** \- The [ClearML Queue](https://clear.ml/docs/latest/docs/fundamentals/agents_and_queues#what-is-a-queue) to which scheduled tasks are enqueued (make sure an agent is assigned to that queue)
  - **Recurrence**\- Recurrence type, select one of the following options:

    - **None** \- The task will run once at the specified time.
    - **Daily** \- Task will run every day at the times specified in the `Time of the Day` field
    - **Weekly** \- Task will run every week on the specified day, at the times specified in the `Time of the Day` field
    - **Monthly** \- Task will run every month on the specified days, and at the times specified in the `Time of the Day` field
    - **Time of the Day** \- The time(s) (UTC) at which the task should run
    - **Add item** \- Add another task to schedule
- **Scheduling Job Name** \- Name for the Scheduler instance. This will appear in the instance list
- **Export Configuration** \- Export the app instance configuration as a JSON file, which you can later import to create
a new instance with the same configuration

![TaskScheduler instance launch form](https://clear.ml/docs/latest/assets/images/apps_taskscheduler_wizard-b02eb7b22aafcd464fcb151dde8b8b63.png#light-mode-only)![TaskScheduler instance launch form](https://clear.ml/docs/latest/assets/images/apps_taskscheduler_wizard_dark-29e14061160fc20b18df606ec7a6796c.png#dark-mode-only)

- [Scheduler Instance Configuration](https://clear.ml/docs/latest/docs/webapp/applications/apps_task_scheduler/#scheduler-instance-configuration)
  - [Configuration Options](https://clear.ml/docs/latest/docs/webapp/applications/apps_task_scheduler/#configuration-options)