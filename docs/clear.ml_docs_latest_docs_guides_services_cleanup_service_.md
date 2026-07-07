---
url: "https://clear.ml/docs/latest/docs/guides/services/cleanup_service/"
title: "Cleanup Service | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/services/cleanup_service/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The [cleanup service](https://github.com/clearml/clearml/blob/master/examples/services/cleanup/cleanup_service.py)
demonstrates how to use the `clearml.backend_api.session.client.APIClient` class to implement a service that deletes old
archived tasks and their associated files: model checkpoints, other artifacts, and debug samples.

Modify the cleanup service's parameters to specify which archived tasks to delete and when to delete them.

### Running the Cleanup Service [​](https://clear.ml/docs/latest/docs/guides/services/cleanup_service/\#running-the-cleanup-service "Direct link to Running the Cleanup Service")

Self-deployed ClearML server

A template `Cleanup Service` task is available in the `DevOps Services` project. You can clone it, adapt its [configuration](https://clear.ml/docs/latest/docs/guides/services/cleanup_service/#configuration)
to your needs, and enqueue it for execution directly from the ClearML UI.

Configure the task execution by modifying the `args` dictionary:

- `delete_threshold_days` \- Tasks older than this number of days will be deleted. The default value is 30 days.
- `cleanup_period_in_days` \- Repeat the cleanup service at this interval, in days. The default value is 1.0 (run once a day).
- `force_delete` \- If `False` (default), delete only Draft tasks. If `True`, allows deletion of tasks in any status.
- `run_as_service` \- If `True` (default), the task will be enqueued for remote execution (default queue: "services"). Otherwise, the script will execute locally.

Remote Execution

If `run_as_service` is set to `True`, make sure a `clearml-agent` is assigned to the `services` queue.

Now that the script is configured, execute it:

```bash
python cleanup_service.py
```

A new task called `Cleanup Service` is created in the `DevOps` project on your ClearML server. The script output should
look similar to:

```console
ClearML Task: created new task id=8126c0af800f4903be07421aa344d7b3

ClearML results page: https://app.clear.ml/projects/608e9039/experiments/81261aa34d7b3/output/log

Cleanup service started

Starting cleanup

Deleting 100 tasks
```

This is followed by details from the cleanup.

## The Cleanup Service Code [​](https://clear.ml/docs/latest/docs/guides/services/cleanup_service/\#the-cleanup-service-code "Direct link to The Cleanup Service Code")

[cleanup\_service.py](https://github.com/clearml/clearml/blob/master/examples/services/cleanup/cleanup_service.py) creates
an `APIClient` object that establishes a session with the ClearML Server, and accomplishes the cleanup by calling:

- [`Tasks.get_all`](https://clear.ml/docs/latest/docs/references/api/tasks#post-tasksget_all)to get a list of Tasks to delete, providing the following parameters:

  - `system_tags` \- Get only Tasks tagged as `archived`.
  - `status_changed` \- Get Tasks whose last status change is older than the delete threshold (in seconds).
- [`Task.delete`](https://clear.ml/docs/latest/docs/references/sdk/task#delete) \- Delete a Task.

## Configuration [​](https://clear.ml/docs/latest/docs/guides/services/cleanup_service/\#configuration "Direct link to Configuration")

The task's hyperparameters are explicitly logged to ClearML using the [`Task.connect()`](https://clear.ml/docs/latest/docs/references/sdk/task#connect)
method. View them in the WebApp, in the task's **CONFIGURATION** tab under **HYPERPARAMETERS > General**.

The task can be reused. Clone the task, edit its parameters, and enqueue the task to run in ClearML Agent [services mode](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_services_mode).

![Cleanup service configuration](https://clear.ml/docs/latest/assets/images/example_cleanup_configuration-d07af6272eccd1c9ddce80ddccb825a1.png)

## Console [​](https://clear.ml/docs/latest/docs/guides/services/cleanup_service/\#console "Direct link to Console")

All console output appears in the task's **CONSOLE** tab.

![Cleanup service console](https://clear.ml/docs/latest/assets/images/examples_cleanup_console-b6d5ec57b9aa37441c38728a3dadb2c5.png)

- [Running the Cleanup Service](https://clear.ml/docs/latest/docs/guides/services/cleanup_service/#running-the-cleanup-service)
- [The Cleanup Service Code](https://clear.ml/docs/latest/docs/guides/services/cleanup_service/#the-cleanup-service-code)
- [Configuration](https://clear.ml/docs/latest/docs/guides/services/cleanup_service/#configuration)
- [Console](https://clear.ml/docs/latest/docs/guides/services/cleanup_service/#console)