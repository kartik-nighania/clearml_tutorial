---
url: "https://clear.ml/docs/latest/docs/integrations/tao/"
title: "Nvidia TAO | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/integrations/tao/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The [NVIDIA TAO Toolkit](https://docs.nvidia.com/tao/tao-toolkit/index.html) is a low-code version of the NVIDIA TAO
framework that accelerates the model training process. ClearML integrates seamlessly with TAO Toolkit, automatically
logging metrics, model files, plots, debug samples, and more, so you can gain more insight into the training process.

## Setup [​](https://clear.ml/docs/latest/docs/integrations/tao/\#setup "Direct link to Setup")

1. Install the `clearml` Python package:





```commandline
pip install clearml
```

2. To keep track of your tasks and/or data, ClearML needs to communicate to a server. You have 2 server options:
   - Sign up for free to the [ClearML Hosted Service](https://app.clear.ml/)
   - Set up your own server, see [here](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server)
3. Connect the ClearML SDK to the server by creating credentials (go to the top right in the UI to **Settings > Workspace > Create new credentials**),
then execute the command below and follow the instructions:





```commandline
clearml-init
```











Jupyter Notebook





If you're using Jupyter Notebook, in the **New Credential** modal, click "Jupyter Notebook", and copy the credential and paste
them in your notebook







Set Credentials in TAO Toolkit Launcher





You can set environment variables with your ClearML credentials via the TAO Toolkit launcher. Add your credentials
to the `Envs` element of the `~/.tao_mounts.json` file as shown below:







```json
{

       "Mounts": [\
\
\
\
       ],

       "Envs": [\
\
           {\
\
               "variable": "CLEARML_WEB_HOST",\
\
               "value": "https://app.clear.ml"\
\
           },\
\
           {\
\
               "variable": "CLEARML_API_HOST",\
\
               "value": "https://api.clear.ml"\
\
            },\
\
            {\
\
                "variable": "CLEARML_FILES_HOST",\
\
                "value": "https://files.clear.ml"\
\
            },\
\
            {\
\
                "variable": "CLEARML_API_ACCESS_KEY",\
\
                "value": "<API_ACCESS_KEY>"\
\
            },\
\
            {\
\
                "variable": "CLEARML_API_SECRET_KEY",\
\
                "value": "<API_SECRET_KEY>"\
\
            }\
\
        ],

        "DockerOptions": {



        }

}
```

4. Customize the ClearML Task through TAO Toolkit. Under `visualizer.clearml_config` of your training configuration file,
you can set the following:


   - `task` \- Name of the ClearML Task. In order to maintain a unique name per run, TAO Toolkit appends to the name
     string a timestamp of the task creation time.
   - `project` \- Project where the task will be stored
   - `tags` \- Tags to label the task.

For example:

```text
clearml_config{

    project: "TAO Toolkit ClearML Demo"

    task: "detectnet_v2_resnet18_clearml"

    tags: "detectnet_v2"

    tags: "training"

    tags: "resnet18"

    tags: "unpruned"

}
```

This configuration may vary depending on the schema the network follows. For more information, see the [NVIDIA documentation](https://docs.nvidia.com/tao/tao-toolkit/text/mlops/clearml.html#configuring-the-clearml-element-in-the-training-spec).

And that's it! Whenever you train a model using TAO Toolkit, a [ClearML Task](https://clear.ml/docs/latest/docs/fundamentals/task) will be created,
which will capture your model files, training configuration, scalars, debug samples, plots, console output, and more.
You can view all of this captured information in the [ClearML Web UI](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual).

![TAO UI plots](https://clear.ml/docs/latest/assets/images/integrations_nvidia_tao_plots-2d080d1b08429d536be3a07a74db2f39.png)

## Remote Execution [​](https://clear.ml/docs/latest/docs/integrations/tao/\#remote-execution "Direct link to Remote Execution")

ClearML logs all the information required to reproduce a task run on a different machine (installed packages,
uncommitted changes etc.). The [ClearML Agent](https://clear.ml/docs/latest/docs/clearml_agent) listens to designated queues and when a task is
enqueued, the agent pulls it, recreates its execution environment, and runs it, reporting its scalars, plots, etc. to the
task manager.

Deploy a ClearML Agent onto any machine (e.g. a cloud VM, a local GPU machine, your own laptop) by simply running
the following command on it:

```commandline
clearml-agent daemon --queue <queues_to_listen_to> [--docker]
```

Use the ClearML [Autoscalers](https://clear.ml/docs/latest/docs/cloud_autoscaling/autoscaling_overview) to help you manage cloud workloads in the
cloud of your choice (AWS, GCP, Azure) and automatically deploy ClearML agents: the autoscaler automatically spins up
and shuts down instances as needed, according to a resource budget that you set.

### Reproducing Task Runs [​](https://clear.ml/docs/latest/docs/integrations/tao/\#reproducing-task-runs "Direct link to Reproducing Task Runs")

![Cloning, editing, enqueuing gif](https://clear.ml/docs/latest/assets/images/integrations_yolov5-65419387b0ce8048acf00f3b99e26a91.gif#light-mode-only)![Cloning, editing, enqueuing gif](https://clear.ml/docs/latest/assets/images/integrations_yolov5_dark-253af7b62a086b6b59ed9a8ad381cf5a.gif#dark-mode-only)

Use ClearML's web interface to edit task details, like configuration parameters or input models, then execute the task
with the new configuration on a remote machine:

- Clone the task
- Edit the hyperparameters and/or other details
- Enqueue the task

The ClearML Agent executing the task will use the new values to [override any hard coded values](https://clear.ml/docs/latest/docs/clearml_agent).

- [Setup](https://clear.ml/docs/latest/docs/integrations/tao/#setup)
- [Remote Execution](https://clear.ml/docs/latest/docs/integrations/tao/#remote-execution)
  - [Reproducing Task Runs](https://clear.ml/docs/latest/docs/integrations/tao/#reproducing-task-runs)