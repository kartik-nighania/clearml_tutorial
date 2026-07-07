---
url: "https://clear.ml/docs/latest/docs/webapp/webapp_exp_reproducing/"
title: "Reproducing Task Runs | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/webapp/webapp_exp_reproducing/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

You can reproduce task runs on local or remote machines in one of the following ways:

- Cloning any task - Make an exact copy, while maintaining the original task
- Resetting a task whose status is not _Published_ \- Delete the previous run's logs and output

After cloning or resetting, enqueue the reset or newly cloned task for execution by a worker.

Tasks can also be modified before execution. See [Tuning Tasks](https://clear.ml/docs/latest/docs/webapp/webapp_exp_tuning).

## Cloning [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_reproducing/\#cloning "Direct link to Cloning")

To clone a task:

1. In the task table, right-click the task to reproduce and click **Clone**.
2. In the `Clone Task` modal, set the following:

   - Project - The project where the task will be saved

   - Name - The name for the new task.



     New task name template





     By default, the new task is named `Clone of <original_task_name>`.



     This default name can be customized:



     - In **ClearML Enterprise**, via UI **Settings** page **>** [**Task clone name template**](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_ui_customization#task-clone-name-template)
     - In **ClearML Open Source**, via server configuration setting. For more information, see [Default Task Clone Name](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_config#default-task-clone-name).

   - Set `<cloned_task>` as parent - Select to set this task as the new task's parent

   - Clear Dataviews (Enterprise feature) - If selected, the new task will start with no Dataviews

   - Force Original Packages - If selected, use the parent task's `original pip`/`original conda` for the new task’s [`Python Packages`](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual#python-packages).

   - Description (optional)
3. Click **Clone**

note

By default, the new task's parent task is set to the original task's parent, unless the original task does not
have a parent, in which case the original task is set as the parent. Select `Set <cloned_task> as parent` to force
the original task to become the clone's parent.

![Clone modal](https://clear.ml/docs/latest/assets/images/webapp_clone-7ed4c5b5a0223dfc9656276b61a6f727.png#light-mode-only)![Clone modal](https://clear.ml/docs/latest/assets/images/webapp_clone_dark-291dede5c34b4e9d7c0bf54a7d417b2d.png#dark-mode-only)

## Resetting [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_reproducing/\#resetting "Direct link to Resetting")

To reset a task:

1. In the task table, right-click the relevant task and click **Reset**.
2. In the `Reset Task` modal, if you want the task's artifacts and debug samples to be deleted from the
ClearML file server, click the checkbox
3. Click **Reset**

![Reset modal](https://clear.ml/docs/latest/assets/images/webapp_reset-ced5de42f02cabc09a8e6a1f6831c602.png#light-mode-only)![Reset modal](https://clear.ml/docs/latest/assets/images/webapp_reset_dark-dc9380ab8bf0901e487ffeed85afcd8b.png#dark-mode-only)

## Final Steps [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_reproducing/\#final-steps "Direct link to Final Steps")

At the end of the process you are left with a `Draft` task, meaning that it is editable.

Re-execute the new task:

1. If desired, modify the task's configuration (see [Tuning Tasks](https://clear.ml/docs/latest/docs/webapp/webapp_exp_tuning)).

2. Enqueue the task for execution. Right-click the task > Enqueue > Select a queue > **ENQUEUE**.



note





Make sure that a [ClearML Agent](https://clear.ml/docs/latest/docs/clearml_agent) has been assigned to the selected queue


A ClearML Agent will fetch the task from the queue and execute it. The task can now be tracked and its
results visualized.

- [Cloning](https://clear.ml/docs/latest/docs/webapp/webapp_exp_reproducing/#cloning)
- [Resetting](https://clear.ml/docs/latest/docs/webapp/webapp_exp_reproducing/#resetting)
- [Final Steps](https://clear.ml/docs/latest/docs/webapp/webapp_exp_reproducing/#final-steps)