---
url: "https://clear.ml/docs/latest/docs/integrations/yolov8/"
title: "YOLOv8 | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/integrations/yolov8/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

YOLOv8 MLOps Integration using ClearML -- 🧠 WISDOM NUGGET - YouTube

Tap to unmute

[YOLOv8 MLOps Integration using ClearML -- 🧠 WISDOM NUGGET](https://www.youtube.com/watch?v=iLcC7m3bCes) [ClearML](https://www.youtube.com/channel/UCDYdA4hjckRLRVBrCoKenCQ)

ClearML2.62K subscribers

Ultralytics' [YOLOv8](https://github.com/ultralytics/ultralytics) is a top modeling repository for object detection,
segmentation, and classification. Get the most out of YOLOv8 with ClearML:

- Track every YOLOv8 training run in ClearML
- Remotely train and monitor your YOLOv8 training runs using [ClearML Agent](https://clear.ml/docs/latest/docs/clearml_agent)
- Turn your newly trained YOLOv8 model into an API with just a few commands using [ClearML Serving](https://clear.ml/docs/latest/docs/clearml_serving/)

## Setup [​](https://clear.ml/docs/latest/docs/integrations/yolov8/\#setup "Direct link to Setup")

1. Install the `clearml` Python package:





```commandline
pip install clearml
```

2. To keep track of your tasks and/or data, ClearML needs to communicate to a server. You have 2 server options:
   - Sign up for free to the [ClearML Hosted Service](https://app.clear.ml/)
   - Set up your own server, see [here](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server).
3. Connect the ClearML SDK to the server by creating credentials (go to the top right in the UI to **Settings > Workspace > Create new credentials**),
then execute the command below and follow the instructions:





```commandline
clearml-init
```


That's it! Now, whenever you train a model using YOLOv8, the run will be captured and tracked by ClearML – no additional
code necessary.

## Training YOLOv8 with ClearML [​](https://clear.ml/docs/latest/docs/integrations/yolov8/\#training-yolov8-with-clearml "Direct link to Training YOLOv8 with ClearML")

To enable ClearML task tracking, simply install the `clearml` pip package in your execution environment.

```commandline
pip install clearml>=1.2.0
```

This will enable integration with the YOLOv8 training script. In every training run from now on, the ClearML task
manager will capture:

- Source code and uncommitted changes
- Installed packages
- [Hyperparameters](https://clear.ml/docs/latest/docs/fundamentals/hyperparameters)
- Model files (use [`--save-period n`](https://docs.ultralytics.com/usage/cfg/#modes) to save a checkpoint every `n` epochs)
- Console output
- Scalars (e.g. mAP\_0.5, mAP\_0.5:0.95, precision, recall, losses)
- General information such as machine details, runtime, creation date etc.
- All produced plots such as label correlogram and confusion matrix
- Mosaic per epoch
- Validation images per epoch
- And more

All of this is captured into a [ClearML Task](https://clear.ml/docs/latest/docs/fundamentals/task): a task with your training script's name
created in a `YOLOv8` ClearML project. To change the task's name or project, pass the `name` and `project` arguments in one of
the following ways:

- Via the SDK:





```python
from ultralytics import YOLO



# Initialize YOLO object, load/create YOLOv8 model

model = YOLO()



# Run MODE mode using the custom arguments ARGS

model.MODE(name="<new_task_name>", project="<new_project_name>")
```

- Via the `yolo` CLI:





```commandline
yolo TASK MODE project=new_project name=new_task_name
```


project names

ClearML uses `/` as a delimiter for subprojects: using `example/sample` as a name will create the `sample`
task within the `example` project.

You can see all the captured data in the task's page of the ClearML [WebApp](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual).
Additionally, you can view all of your YOLOv8 runs tracked by ClearML in the [Task Table](https://clear.ml/docs/latest/docs/webapp/webapp_model_table).
Add custom columns to the table, such as mAP values, so you can easily sort and see what is the best performing model.
You can also select multiple tasks and directly [compare](https://clear.ml/docs/latest/docs/webapp/webapp_exp_comparing) them.

## Remote Execution [​](https://clear.ml/docs/latest/docs/integrations/yolov8/\#remote-execution "Direct link to Remote Execution")

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
cloud of your choice (AWS, GCP, Azure) and automatically deploy ClearML agents: the autoscaler automatically spins up and
shuts down instances as needed, according to a resource budget that you set.

### Reproducing Task Runs [​](https://clear.ml/docs/latest/docs/integrations/yolov8/\#reproducing-task-runs "Direct link to Reproducing Task Runs")

ClearML logs all the information required to reproduce a task run, but you may also want to change a few parameters
and task details when you re-run it, which you can do through ClearML's UI.

In order to be able to override parameters via the UI,
you have to run your code to [create a ClearML Task](https://clear.ml/docs/latest/docs/clearml_sdk/task_sdk#task-creation), which will log all the
execution parameters before using the YOLO model. When ClearML re-runs the task remotely, ClearML will override these
parameters before YOLO comes into play.

For example:

```python
from clearml import Task

from ultralytics import YOLO

# Create a ClearML Task

task = Task.init(

    project_name="my project",

    task_name="my yolo task"

)

# Load a model

model_variant = "yolov8n"

# Log "model_variant" parameter to task

task.set_parameter(name="model_variant", value=model_variant)

# Load the YOLOv8 model

model = YOLO(f'{model_variant}.pt')

# Put all YOLOv8 arguments in a dictionary and pass it to ClearML

# When the arguments are later changed in UI, they will be overridden here!

args = dict(data="coco128.yaml", epochs=16)

task.connect(args)

# Train the model

# If running remotely, the arguments may be overridden by ClearML if they were changed in the UI

results = model.train(**args)
```

tip

Notice that in the script above only the `data` and `epochs` args are passed to ClearML, so only their values can be
overridden via the UI. You can add all of YOLO's default parameters to the parameter dictionary, so you'll be able to override
any of them through the UI.

Use the UI to edit task details, then execute the task
with the new configuration on a remote machine:

- Clone the task
- Edit the hyperparameters and/or other details
- Enqueue the task

The ClearML Agent executing the task will use the new values to [override any hard coded values](https://clear.ml/docs/latest/docs/clearml_agent).

![Cloning, editing, enqueuing gif](https://clear.ml/docs/latest/assets/images/integrations_yolov5-65419387b0ce8048acf00f3b99e26a91.gif#light-mode-only)![Cloning, editing, enqueuing gif](https://clear.ml/docs/latest/assets/images/integrations_yolov5_dark-253af7b62a086b6b59ed9a8ad381cf5a.gif#dark-mode-only)

- [Setup](https://clear.ml/docs/latest/docs/integrations/yolov8/#setup)
- [Training YOLOv8 with ClearML](https://clear.ml/docs/latest/docs/integrations/yolov8/#training-yolov8-with-clearml)
- [Remote Execution](https://clear.ml/docs/latest/docs/integrations/yolov8/#remote-execution)
  - [Reproducing Task Runs](https://clear.ml/docs/latest/docs/integrations/yolov8/#reproducing-task-runs)