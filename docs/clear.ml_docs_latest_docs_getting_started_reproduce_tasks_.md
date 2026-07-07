---
url: "https://clear.ml/docs/latest/docs/getting_started/reproduce_tasks/"
title: "Reproducing Task Runs | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/getting_started/reproduce_tasks/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

note

This tutorial assumes that you've already set up [ClearML](https://clear.ml/docs/latest/docs/clearml_sdk/clearml_sdk_setup) and [ClearML Agent](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_bare_metal).

Tasks can be reproduced--or **Cloned**--for validation or as a baseline for further experimentation. When you initialize a task in your
code, ClearML logs everything needed to reproduce your task and its environment:

- Uncommitted changes
- Used packages and their versions
- Parameters
- and more

Cloning a task duplicates the task's configuration, but not its outputs.

ClearML offers two ways to clone your task:

- [Via the WebApp](https://clear.ml/docs/latest/docs/getting_started/reproduce_tasks/#via-the-webapp)--no further code required
- [Via programmatic interface](https://clear.ml/docs/latest/docs/getting_started/reproduce_tasks/#via-programmatic-interface) using the `clearml` Python package

Once you have cloned your task, you can modify its setup, and then execute it remotely on a machine of your choice using a ClearML Agent.

## Via the WebApp [​](https://clear.ml/docs/latest/docs/getting_started/reproduce_tasks/\#via-the-webapp "Direct link to Via the WebApp")

**To clone a task in the ClearML WebApp:**

1. Click on any project card to open its [task table](https://clear.ml/docs/latest/docs/webapp/webapp_exp_table).
2. Right-click the task you want to reproduce.
3. Click **Clone** in the context menu, which will open a **CLONE TASK** window.
4. Click **CLONE** in the window.

The newly cloned task's details page will open up. The cloned task is in _draft_ mode, which means
it can be modified. You can edit any of the Task's setup details, including:

- Git and/or code references
- Python packages to be installed
- Container image to be used

You can adjust the values of the task's hyperparameters and configuration files. See [Modifying Tasks](https://clear.ml/docs/latest/docs/webapp/webapp_exp_tuning#modifying-tasks) for more
information about editing tasks in the UI.

### Enqueue a Task [​](https://clear.ml/docs/latest/docs/getting_started/reproduce_tasks/\#enqueue-a-task "Direct link to Enqueue a Task")

Once you have set up a task, it is now time to execute it.

**To execute a task through the ClearML WebApp:**

1. In the task's details page, click "Menu" ![Menu](https://clear.ml/docs/latest/icons/ico-bars-menu.svg)
2. Click **ENQUEUE** to open the **ENQUEUE TASK** window
3. In the window, select `default` in the `Queue` menu
4. Click **ENQUEUE**

This action pushes the task into the `default` queue. The task's status becomes _Pending_ until an agent
assigned to the queue fetches it, at which time the task's status becomes _Running_. The agent executes the
task, and the task can be [tracked and its results visualized](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual).

## Via Programmatic Interface [​](https://clear.ml/docs/latest/docs/getting_started/reproduce_tasks/\#via-programmatic-interface "Direct link to Via Programmatic Interface")

The cloning, modifying, and enqueuing actions described above can also be performed programmatically using `clearml`.

### Clone the Task [​](https://clear.ml/docs/latest/docs/getting_started/reproduce_tasks/\#clone-the-task "Direct link to Clone the Task")

To duplicate the task, use [`Task.clone()`](https://clear.ml/docs/latest/docs/references/sdk/task#taskclone), and input either a
Task object or the Task's ID as the `source_task` argument.

```python
cloned_task = Task.clone(source_task='qw03485je3hap903ere54')
```

The cloned task is in _draft_ mode, which means it can be modified. For modification options, such as setting new parameter
values, see [Task SDK](https://clear.ml/docs/latest/docs/clearml_sdk/task_sdk).

### Enqueue the Task [​](https://clear.ml/docs/latest/docs/getting_started/reproduce_tasks/\#enqueue-the-task "Direct link to Enqueue the Task")

To enqueue the task, use [`Task.enqueue()`](https://clear.ml/docs/latest/docs/references/sdk/task#taskenqueue), and input the Task object
with the `task` argument, and the queue to push the task into with `queue_name`.

```python
Task.enqueue(task=cloned_task, queue_name='default')
```

This action pushes the task into the `default` queue. The task's status becomes _Pending_ until an agent
assigned to the queue fetches it, at which time the task's status becomes _Running_. The agent executes the
task, and the task can be [tracked and its results visualized](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual).

- [Via the WebApp](https://clear.ml/docs/latest/docs/getting_started/reproduce_tasks/#via-the-webapp)
  - [Enqueue a Task](https://clear.ml/docs/latest/docs/getting_started/reproduce_tasks/#enqueue-a-task)
- [Via Programmatic Interface](https://clear.ml/docs/latest/docs/getting_started/reproduce_tasks/#via-programmatic-interface)
  - [Clone the Task](https://clear.ml/docs/latest/docs/getting_started/reproduce_tasks/#clone-the-task)
  - [Enqueue the Task](https://clear.ml/docs/latest/docs/getting_started/reproduce_tasks/#enqueue-the-task)