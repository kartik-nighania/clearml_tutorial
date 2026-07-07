---
url: "https://clear.ml/docs/latest/docs/guides/clearml_agent/executable_exp_containers/"
title: "Executable Task Containers | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/clearml_agent/executable_exp_containers/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

This tutorial demonstrates using [`clearml-agent`](https://clear.ml/docs/latest/docs/clearml_agent)'s [`build`](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_ref#build)
command to package a task into an executable container. In this example, you will build a container image that, when
run, will automatically execute the [keras\_tensorboard.py](https://github.com/clearml/clearml/blob/master/examples/frameworks/keras/keras_tensorboard.py)
script.

## Prerequisites [​](https://clear.ml/docs/latest/docs/guides/clearml_agent/executable_exp_containers/\#prerequisites "Direct link to Prerequisites")

- [`clearml-agent`](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_bare_metal#installation) installed and configured
- [`clearml`](https://clear.ml/docs/latest/docs/clearml_sdk/clearml_sdk_setup#install-clearml) installed and configured
- [clearml](https://github.com/clearml/clearml) repo cloned (`git clone https://github.com/clearml/clearml.git`)

## Creating the ClearML Task [​](https://clear.ml/docs/latest/docs/guides/clearml_agent/executable_exp_containers/\#creating-the-clearml-task "Direct link to Creating the ClearML Task")

1. Set up the task's execution environment:





```console
cd clearml/examples/frameworks/keras

pip install -r requirements.txt
```

2. Run the task:





```console
python keras_tensorboard.py
```









This creates a ClearML task called "Keras with TensorBoard example" in the "examples" project.

Note the task ID in the console output when running the script above:





```console
ClearML Task: created new task id=<TASK_ID>
```









This ID will be used in the following section.


## Building and Launching a Containerized Task [​](https://clear.ml/docs/latest/docs/guides/clearml_agent/executable_exp_containers/\#building-and-launching-a-containerized-task "Direct link to Building and Launching a Containerized Task")

1. Execute the following command to build the container. Input the ID of the task created above:





```console
clearml-agent build --id <TASK_ID> --docker --target new-docker --entry-point clone_task
```











tip





If the container will not make use of a GPU, add the `--cpu-only` flag.





This command will create a container, set up with the execution environment for this task in the
specified `--target` folder. When the container is launched, it will clone the task specified with `id` and
execute the clone (as designated by the `--entry-point` parameter).

2. Run the Docker, pointing to the new container:





```console
docker run new-docker
```









The task will be executed inside the container. Task details can be viewed in the [ClearML Web UI](https://clear.ml/docs/latest/docs/webapp/webapp_overview).


For additional ClearML Agent options, see the [ClearML Agent reference page](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_ref).

- [Prerequisites](https://clear.ml/docs/latest/docs/guides/clearml_agent/executable_exp_containers/#prerequisites)
- [Creating the ClearML Task](https://clear.ml/docs/latest/docs/guides/clearml_agent/executable_exp_containers/#creating-the-clearml-task)
- [Building and Launching a Containerized Task](https://clear.ml/docs/latest/docs/guides/clearml_agent/executable_exp_containers/#building-and-launching-a-containerized-task)