---
url: "https://clear.ml/docs/latest/docs/guides/ui/tuning_exp/"
title: "Tuning Tasks | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/ui/tuning_exp/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

In this tutorial, learn how to tune a task. The task that will be tuned is created by the [pytorch\_mnist.py](https://github.com/clearml/clearml/blob/master/examples/frameworks/pytorch/pytorch_mnist.py)
example script.

## Prerequisites [​](https://clear.ml/docs/latest/docs/guides/ui/tuning_exp/\#prerequisites "Direct link to Prerequisites")

- Clone the [clearml](https://github.com/clearml/clearml) repository.
- Install the [requirements](https://github.com/clearml/clearml/blob/master/examples/frameworks/tensorflow/requirements.txt)
for the TensorFlow examples.
- Have **ClearML Agent** [installed and configured](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_bare_metal#installation).

## Step 1: Run the Task [​](https://clear.ml/docs/latest/docs/guides/ui/tuning_exp/\#step-1-run-the-task "Direct link to Step 1: Run the Task")

In the `examples/frameworks/pytorch` directory, run the task script:

```commandline
python pytorch_mnist.py
```

## Step 2: Clone the Task [​](https://clear.ml/docs/latest/docs/guides/ui/tuning_exp/\#step-2-clone-the-task "Direct link to Step 2: Clone the Task")

Clone the task to create an editable copy for tuning.

1. In the ClearML WebApp (UI), on the Projects page, click the `examples` project card.

2. In the task table, right-click the task `pytorch mnist train`.

3. In the context menu, click **Clone** **>** **CLONE**. The newly cloned task appears and its info panel slides open.


## Step 3: Tune the Cloned Task [​](https://clear.ml/docs/latest/docs/guides/ui/tuning_exp/\#step-3-tune-the-cloned-task "Direct link to Step 3: Tune the Cloned Task")

To demonstrate tuning, change two hyperparameter values.

1. In the info panel, **CONFIGURATION** **>** **HYPERPARAMETERS** **>** **Args** **>** Hover and click **EDIT**.

2. Change the value of `batch_size` from `64` to `32`.

3. Change the value of `lr` from `0.01` to `0.025`.

4. Click **SAVE**.


## Step 4: Run a Worker Daemon Listening to a Queue [​](https://clear.ml/docs/latest/docs/guides/ui/tuning_exp/\#step-4-run-a-worker-daemon-listening-to-a-queue "Direct link to Step 4: Run a Worker Daemon Listening to a Queue")

To execute the cloned task, use a [ClearML Agent](https://clear.ml/docs/latest/docs/fundamentals/agents_and_queues).

Run the agent on the local development machine:

1. Open a terminal session.

2. Run the following `clearml-agent` command which runs a worker daemon listening to the `default` queue:





```text
clearml-agent daemon --queue default
```









The response to this command is information about the configuration, the worker, and the queue. For example:





```text
Current configuration (clearml_agent v0.16.0, location: /home/<username>/clearml.conf):

   ----------------------

agent.worker_id =

agent.worker_name = LAPTOP-PPTKKPGK

agent.python_binary =

agent.package_manager.type = pip

.

.

.

sdk.development.worker.report_period_sec = 2

sdk.development.worker.ping_period_sec = 30

sdk.development.worker.log_stdout = true



Worker "LAPTOP-PPTKKPGK:0" - Listening to queues:

+ ---------------------------------+---------+-------+

| id                               | name    | tags  |

+ ---------------------------------+---------+-------+

| 2a03daf5ff9a4255b9915fbd5306f924 | default |       |

+ ---------------------------------+---------+-------+



Running CLEARML-AGENT daemon in background mode, writing stdout/stderr to /home/<username>/.clearml_agent_daemon_outym6lqxrz.txt
```


## Step 5: Enqueue the Tuned Task [​](https://clear.ml/docs/latest/docs/guides/ui/tuning_exp/\#step-5-enqueue-the-tuned-task "Direct link to Step 5: Enqueue the Tuned Task")

Enqueue the tuned task.

1. In the ClearML WebApp > task table, right-click the task `Clone Of pytorch mnist train`.

2. In the context menu, click **Enqueue**.

3. Select **Default** queue.

4. Click **ENQUEUE**. The task's status becomes Pending. When the worker fetches the task from the queue,
the status becomes Running. The progress of the task can be viewed in the info panel. When the status becomes
Completed, continue to the next step.


## Step 6: Compare the Tasks [​](https://clear.ml/docs/latest/docs/guides/ui/tuning_exp/\#step-6-compare-the-tasks "Direct link to Step 6: Compare the Tasks")

To compare the original and tuned tasks:

1. In the ClearML WebApp (UI), on the Projects page, click the `examples` project.

2. In the task table, select the checkboxes for the two tasks: `pytorch mnist train` and `Clone Of pytorch mnist train`.

3. On the menu bar at the bottom of the task table, click **COMPARE**. The task comparison window appears.
All differences appear with a different background color to highlight them.

The task comparison window is organized in the following tabs:
   - **DETAILS** \- The **ARTIFACTS** section, including input and output models with their network designs, and other artifacts;
     the **EXECUTION** section execution, including source code control, installed Python packages and versions,
     uncommitted changes, and the Docker image name which, in this case, is empty.
   - **HYPERPARAMETERS** \- The hyperparameters and their values.
   - **SCALARS** \- Scalar metrics with the option to view them as charts or values.
   - **PLOTS** \- Plots of any data with the option to view them as charts or values.
   - **DEBUG SAMPLES** \- Media including images, audio, and video uploaded by your task shown as thumbnails.
4. Examine the differences.
1. Compare the hyperparameters. In the **HYPERPARAMETERS** tab, expand **ARGS**. The hyperparameters `batch_size`
      and `lr` are shown with a different background color. The values are different.
2. Compare the metrics. In the **SCALARS** tab, to the right of **Add Task**, select the plot or value comparison:

      - **Graph** \- The scalar metrics plots show `pytorch mnist train` and `Clone of pytorch mnist train`.
      - **Last Values** \- Expand a metric and variant.

## Next Steps [​](https://clear.ml/docs/latest/docs/guides/ui/tuning_exp/\#next-steps "Direct link to Next Steps")

- For more information about editing tasks, see [modifying tasks](https://clear.ml/docs/latest/docs/webapp/webapp_exp_tuning#modifying-tasks).

- [Prerequisites](https://clear.ml/docs/latest/docs/guides/ui/tuning_exp/#prerequisites)
- [Step 1: Run the Task](https://clear.ml/docs/latest/docs/guides/ui/tuning_exp/#step-1-run-the-task)
- [Step 2: Clone the Task](https://clear.ml/docs/latest/docs/guides/ui/tuning_exp/#step-2-clone-the-task)
- [Step 3: Tune the Cloned Task](https://clear.ml/docs/latest/docs/guides/ui/tuning_exp/#step-3-tune-the-cloned-task)
- [Step 4: Run a Worker Daemon Listening to a Queue](https://clear.ml/docs/latest/docs/guides/ui/tuning_exp/#step-4-run-a-worker-daemon-listening-to-a-queue)
- [Step 5: Enqueue the Tuned Task](https://clear.ml/docs/latest/docs/guides/ui/tuning_exp/#step-5-enqueue-the-tuned-task)
- [Step 6: Compare the Tasks](https://clear.ml/docs/latest/docs/guides/ui/tuning_exp/#step-6-compare-the-tasks)
- [Next Steps](https://clear.ml/docs/latest/docs/guides/ui/tuning_exp/#next-steps)