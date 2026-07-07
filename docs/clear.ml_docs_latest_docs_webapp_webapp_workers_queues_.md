---
url: "https://clear.ml/docs/latest/docs/webapp/webapp_workers_queues/"
title: "Orchestration | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/webapp/webapp_workers_queues/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

With the **Orchestration** page, you can:

- Use Cloud autoscaling apps to define your compute resource budget, and have the apps automatically manage your resource
consumption as needed–-with no code (available under the ClearML Pro plan)
- Monitor resources (CPU and GPU, memory, video memory, and network usage) used by the tasks that workers
execute
- View workers and the queues they listen to
- Manage worker queues
  - Create and rename queues
  - Delete empty queues
  - Monitor queue utilization
  - Reorder, move, and remove tasks from queues
- Monitor all of your available and in-use compute resources (available in the ClearML Enterprise plan. See [Orchestration Dashboard](https://clear.ml/docs/latest/docs/webapp/webapp_orchestration_dash))
- Set user group resource quotas and reservations to enable workload prioritization across available resources (available
in the ClearML Enterprise plan. See [Resource Policies](https://clear.ml/docs/latest/docs/webapp/resource_policies))

## Autoscalers [​](https://clear.ml/docs/latest/docs/webapp/webapp_workers_queues/\#autoscalers "Direct link to Autoscalers")

Pro Plan Offering

The ClearML Autoscaler apps are available under the ClearML Pro plan.

Use the **AUTOSCALERS** tab to access ClearML's cloud autoscaling applications:

- AWS Autoscaler
- GCP Autoscaler

The autoscalers automatically spin up or down cloud instances as needed and according to a budget that you set, so you
pay only for the time that you actually use the machines.

The **AWS** and **GCP** autoscaler applications will manage instances on your behalf in your cloud account. When
launching an app instance, you will provide your cloud service credentials so the autoscaler can access your account.

Once you launch an autoscaler app instance, you can monitor the autoscaler's activity and your cloud usage in the instance's
dashboard.

For more information about how autoscalers work, see the [Cloud Autoscaling Overview](https://clear.ml/docs/latest/docs/cloud_autoscaling/autoscaling_overview).
For more information about a specific autoscaler, see [AWS Autoscaler](https://clear.ml/docs/latest/docs/webapp/applications/apps_aws_autoscaler)
and/or [GCP Autoscaler](https://clear.ml/docs/latest/docs/webapp/applications/apps_gcp_autoscaler).

![Cloud autoscalers](https://clear.ml/docs/latest/assets/images/webapp_orchestration_autoscalers-d3738d8a51d5cc32a6059171379172b1.png#light-mode-only)![Cloud autoscalers](https://clear.ml/docs/latest/assets/images/webapp_orchestration_autoscalers_dark-2abac57c4bcc45411f8da0d0414e31c2.png#dark-mode-only)

## Workers [​](https://clear.ml/docs/latest/docs/webapp/webapp_workers_queues/\#workers "Direct link to Workers")

Use the **WORKERS** tab to track worker activity and monitor worker utilization.
The page shows a worker activity graph and a worker details table. The graph time span can be controlled through the menu
at its top right corner. Hover over any plot point to see its data. By default, the **WORKER UTILIZATION** graph displays the
number of active and total workers over time.

The worker table shows the currently available workers and their current execution information:

- Current running task
- Current execution time
- Training iteration.

Clicking on a worker opens the worker's details panel and replaces the graph with that worker's resource utilization
information. The resource metric being monitored can be selected through the menu at the graph's top left corner:

- CPU and GPU Usage
- Memory Usage
- Video Memory Usage
- Network Usage.

If a worker has multiple GPUs, the **CPU and GPU Usage** and **Video Memory Usage** graphs display separate usage plots
for each GPU (e.g., GPU 0, GPU 1, etc.) in addition to an overall average GPU usage plot.

The worker's details panel includes the following two tabs:

- **INFO**\- Worker information:

  - Worker Name
  - Update time - The last time the worker reported data
  - Current Task - The task currently being executed by the worker
  - Task Runtime - How long the currently executing task has been running
  - Task iteration - The last reported training iteration for the task
- **QUEUES**\- Information about the queues that the worker is assigned to:

  - Queue - The name of the Queue
  - Next task - The next task available in this queue
  - In Queue - The number of tasks currently enqueued

![Worker management](https://clear.ml/docs/latest/assets/images/agents_queues_resource_management-47fde9a54ecb95db8723a8eba0d79548.png#light-mode-only)![Worker management](https://clear.ml/docs/latest/assets/images/agents_queues_resource_management_dark-08e872544b0ac873c7605d1ff14e83f6.png#dark-mode-only)

## Queues [​](https://clear.ml/docs/latest/docs/webapp/webapp_workers_queues/\#queues "Direct link to Queues")

Use the **QUEUES** tab to manage queues and monitor their statistics. The page shows graphs of the average task
wait time and the number of queued tasks, and a queue details table. Hover over any plot point to view its data.
By default, the graphs display the overall information of all queues.

The queue table shows the following queue information:

- Queue - Queue name
- Workers - Number of workers servicing the queue
- Next Task - The next task available in this queue
- Last Updated - The last time queue contents were modified
- In Queue - Number of tasks currently enqueued in the queue

Use the search bar ![Magnifying glass](https://clear.ml/docs/latest/icons/ico-search.svg)
to find specific queues. You can query by queue name, display name, and ID.

To create a new queue - Click **\+ NEW QUEUE** (top left).

Hover over a queue and click ![Copy](https://clear.ml/docs/latest/icons/ico-copy-to-clipboard.svg)
to copy the queue's ID.

![Queues](https://clear.ml/docs/latest/assets/images/4100-da5922170a7b53e737c41ac2204ca6f1.png#light-mode-only)![Queues](https://clear.ml/docs/latest/assets/images/4100_dark-b1c090c6e97d2be7fe69be9e3bfa905f.png#dark-mode-only)

Right-click on a queue or hover and click its action button ![Dot menu](https://clear.ml/docs/latest/icons/ico-dots-v-menu.svg)
to access queue actions:

![Queue context menu](https://clear.ml/docs/latest/assets/images/webapp_workers_queues_context-29d5f61781238221cf686f1e20235e6c.png#light-mode-only)![Queue context menu](https://clear.ml/docs/latest/assets/images/webapp_workers_queues_context_dark-3f7878f38749b7cc4e1817e809f6eeb7.png#dark-mode-only)

- Delete - Delete the queue. Any pending tasks will be dequeued.
- Rename - Change the queue's name
- Clear - Remove all pending tasks from the queue

Enterprise Feature

The ClearML Enterprise Server provides a mechanism to define your own custom actions, which will
appear in the context menu. Create a custom action by defining an HTTP request to issue when clicking on the context menu
action. For more information see [Custom UI Context Menu Actions](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_config#custom-ui-context-menu-actions).

Clicking on a queue will open the queue's details panel and replace the graphs with that queue's statistics.

The queue's details panel includes the following two tabs:

- **TASKS** \- A list of tasks in the queue. You can reorder and remove enqueued tasks. See
[Controlling Queue Contents](https://clear.ml/docs/latest/docs/webapp/webapp_workers_queues/#controlling-queue-contents).
- **WORKERS**\- Information about the workers assigned to the queue:

  - Name - Worker name
  - IP - Worker's IP
  - Currently Executing - The task currently being executed by the worker

### Controlling Queue Contents [​](https://clear.ml/docs/latest/docs/webapp/webapp_workers_queues/\#controlling-queue-contents "Direct link to Controlling Queue Contents")

Click on a task's menu button ![Dot menu](https://clear.ml/docs/latest/icons/ico-dots-v-menu.svg)
in the **TASKS** tab to reorganize your queue:

![Queue task&#39;s menu](<Base64-Image-Removed>)![Queue task&#39;s menu](<Base64-Image-Removed>)

- Move a task to the top or bottom of the queue
- Move the task to a different queue
- Dequeue the task

You can also reorder tasks in a queue by dragging a task to a new position in the queue.

- [Autoscalers](https://clear.ml/docs/latest/docs/webapp/webapp_workers_queues/#autoscalers)
- [Workers](https://clear.ml/docs/latest/docs/webapp/webapp_workers_queues/#workers)
- [Queues](https://clear.ml/docs/latest/docs/webapp/webapp_workers_queues/#queues)
  - [Controlling Queue Contents](https://clear.ml/docs/latest/docs/webapp/webapp_workers_queues/#controlling-queue-contents)