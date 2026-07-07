---
url: "https://clear.ml/docs/latest/docs/guides/clearml_agent/exp_environment_containers/"
title: "Task Environment Containers | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/clearml_agent/exp_environment_containers/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

This tutorial demonstrates using [`clearml-agent`](https://clear.ml/docs/latest/docs/clearml_agent)'s [`build`](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_ref#build)
command to build a container replicating the execution environment of an existing task. ClearML Agents can make
use of such containers to execute tasks without having to set up their environment every time.

A use case for this would be manual hyperparameter optimization, where a base task can be used to create a container to
be used when running optimization tasks.

## Prerequisites [​](https://clear.ml/docs/latest/docs/guides/clearml_agent/exp_environment_containers/\#prerequisites "Direct link to Prerequisites")

- [`clearml-agent`](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_bare_metal#installation) installed and configured
- [`clearml`](https://clear.ml/docs/latest/docs/clearml_sdk/clearml_sdk_setup#install-clearml) installed and configured
- [clearml](https://github.com/clearml/clearml) repo cloned (`git clone https://github.com/clearml/clearml.git`)

## Creating the ClearML Task [​](https://clear.ml/docs/latest/docs/guides/clearml_agent/exp_environment_containers/\#creating-the-clearml-task "Direct link to Creating the ClearML Task")

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


## Building the Container [​](https://clear.ml/docs/latest/docs/guides/clearml_agent/exp_environment_containers/\#building-the-container "Direct link to Building the Container")

Execute the following command to build the container. Input the ID of the task created above.

```console
clearml-agent build --id <TASK_ID> --docker --target new_docker
```

tip

If the container will not make use of a GPU, add the `--cpu-only` flag.

This will create a container with the specified task's execution environment in the `--target` folder.
When the Docker build completes, the console output shows:

```console
Docker build done

Committing docker container to: new_docker

sha256:460453b93ct1989fd1c6637c236e544031c4d378581433fc0b961103ce206af1
```

## Using the New Container [​](https://clear.ml/docs/latest/docs/guides/clearml_agent/exp_environment_containers/\#using-the-new-container "Direct link to Using the New Container")

Make use of the container you've just built by having a ClearML agent make use of it for executing a new task:

1. In the [ClearML Web UI](https://clear.ml/docs/latest/docs/webapp/webapp_overview), go to the "examples" project, "Keras with TensorBoard
example" task (the one executed [above](https://clear.ml/docs/latest/docs/guides/clearml_agent/exp_environment_containers/#creating-the-clearml-task)).

2. [Clone](https://clear.ml/docs/latest/docs/webapp/webapp_exp_reproducing) the task.

3. In the cloned task, go to the **EXECUTION** tab **>** **CONTAINER** section. Under **IMAGE**, insert the name
of the new Docker image, `new_docker`. See [Tuning Tasks](https://clear.ml/docs/latest/docs/webapp/webapp_exp_tuning) for more task
modification options.

4. Enqueue the cloned task to the `default` queue.

5. Launch a `clearml-agent` in [Docker Mode](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_execution_env#docker-mode) and assign it to the `default` queue:





```console
clearml-agent daemon --docker --queue default
```











tip





If the agent will not make use of a GPU, add the `--cpu-only` flag.





This agent will pull the enqueued task and run it using the `new_docker` image to create the execution environment.
In the task's **CONSOLE** tab, one of the first logs displays the following:





```console
Executing: ['docker', 'run', ..., 'CLEARML_DOCKER_IMAGE=new_docker', ...].
```


- [Prerequisites](https://clear.ml/docs/latest/docs/guides/clearml_agent/exp_environment_containers/#prerequisites)
- [Creating the ClearML Task](https://clear.ml/docs/latest/docs/guides/clearml_agent/exp_environment_containers/#creating-the-clearml-task)
- [Building the Container](https://clear.ml/docs/latest/docs/guides/clearml_agent/exp_environment_containers/#building-the-container)
- [Using the New Container](https://clear.ml/docs/latest/docs/guides/clearml_agent/exp_environment_containers/#using-the-new-container)