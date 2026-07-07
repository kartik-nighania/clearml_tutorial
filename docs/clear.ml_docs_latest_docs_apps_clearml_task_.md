---
url: "https://clear.ml/docs/latest/docs/apps/clearml_task/"
title: "ClearML Task CLI | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/apps/clearml_task/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

Using only the command line and **zero** additional lines of code, easily track your work and integrate ClearML with your
existing code.

`clearml-task` automatically imports any script or Python repository into ClearML. `clearml-task` lets
you enqueue your code for execution by an available [ClearML Agent](https://clear.ml/docs/latest/docs/clearml_agent). You can even provide command
line arguments, Python module dependencies, and a requirements.txt file!

## What Is ClearML Task For? [​](https://clear.ml/docs/latest/docs/apps/clearml_task/\#what-is-clearml-task-for "Direct link to What Is ClearML Task For?")

- Launching off-the-shelf code on a remote machine with dedicated resources (e.g. GPU)
- Running [hyperparameter optimization](https://clear.ml/docs/latest/docs/getting_started/hpo) on a codebase that is still not in ClearML
- Creating a pipeline from an assortment of scripts, that you need to turn into ClearML tasks
- Running some code on a remote machine, either using an on-prem cluster or on the cloud

## How Does ClearML Task Work? [​](https://clear.ml/docs/latest/docs/apps/clearml_task/\#how-does-clearml-task-work "Direct link to How Does ClearML Task Work?")

1. Execute `clearml-task`, specifying the ClearML target project and task name, along with your script (and repository / commit / branch).
Optionally, specify an execution queue and container image to use.
2. `clearml-task` does its magic! It creates a new [ClearML Task](https://clear.ml/docs/latest/docs/fundamentals/task),
and, if so directed, enqueues it for execution by a ClearML Agent.
3. While the Task is running on the remote machine, all its console outputs are logged in real-time, alongside your
TensorBoard and matplotlib. You can track your script's progress and results in the [ClearML Web UI](https://clear.ml/docs/latest/docs/webapp/webapp_overview)
(a link to your task details page in the ClearML Web UI is printed as ClearML Task creates the task).

## Execution Configuration [​](https://clear.ml/docs/latest/docs/apps/clearml_task/\#execution-configuration "Direct link to Execution Configuration")

### Container [​](https://clear.ml/docs/latest/docs/apps/clearml_task/\#container "Direct link to Container")

Specify a container to run the code in with the `--docker <image>` option.
The ClearML Agent pulls it from Docker Hub or a container artifactory automatically.

### Package Dependencies [​](https://clear.ml/docs/latest/docs/apps/clearml_task/\#package-dependencies "Direct link to Package Dependencies")

`clearml-task` automatically finds the `requirements.txt` file in remote repositories.

If a local script requires certain packages, or the remote repository doesn't have a `requirements.txt` file,
manually specify the required Python packages using `--packages "<package_name>"`, for example `--packages "keras" "tensorflow>2.2"`.

### Queue [​](https://clear.ml/docs/latest/docs/apps/clearml_task/\#queue "Direct link to Queue")

Tasks are passed to ClearML Agents via [Queues](https://clear.ml/docs/latest/docs/fundamentals/agents_and_queues). Specify a queue in which to enqueue
the task. If you don't input a queue, the task is created in _draft_ status, and you can enqueue it at a later point.

### Branch and Working Directory [​](https://clear.ml/docs/latest/docs/apps/clearml_task/\#branch-and-working-directory "Direct link to Branch and Working Directory")

To specify your code's branch and commit ID, pass the `--branch <branch_name> --commit <commit_id>` options.
If unspecified, `clearml-task` will use the latest commit from the 'master' branch.

GitHub Default Branch

For GitHub repositories, it is recommended to explicitly specify your default branch (e.g. `--branch main`) to avoid
errors in identifying the correct default branch.

### Command Line Options [​](https://clear.ml/docs/latest/docs/apps/clearml_task/\#command-line-options "Direct link to Command Line Options")

| Name | Description | Mandatory |
| --- | --- | --- |
| `--args` | Arguments to pass to the remote task, list of `<argument>=<value>` strings. Currently only argparse arguments are supported. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--base-task-id` | Use a pre-existing task in the system, instead of a local repo / script. Essentially clones an existing task and overrides arguments / requirements. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--binary` | Binary executable used to launch the entry point. For example: `--binary python3`, `--binary /bin/bash`. By default, the binary will be auto-detected. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--branch` | Select repository branch / tag. By default, latest commit from the master branch. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--commit` | Select commit ID to use. By default, latest commit, or local commit ID when using local repository. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--cwd` | Working directory to launch the script from. Relative to repo root or local `--folder`. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--docker` | Select the container image to use in the remote task. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--docker_bash_setup_script` | Add a bash script to be executed inside the container before setting up the task's environment. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--docker_args` | Add Docker arguments. Pass a single string in the following format: `--docker_args "<argument_string>"`. For example: `--docker_args "-v some_dir_1:other_dir_1 -v some_dir_2:other_dir_2"`. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--folder` | Execute the code from a local folder. Notice, it assumes a git repository already exists. Current state of the repo (commit ID and uncommitted changes) is logged and replicated on the remote machine. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--force-no-requirements` | If specified, skips all package and requirements installation, and neither packages nor a requirements file need to be provided. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--import-offline-session` | Specify the path to the offline session you want to import. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--name` | Set a target name for the new task. | ![Yes](https://clear.ml/docs/latest/icons/ico-optional-yes.svg) |
| `--output-uri` | Set the task `output_uri`, upload destination for task models and artifacts. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--packages` | Manually specify a list of required packages. Example: `--packages "tqdm>=2.1" "scikit-learn"`. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--project` | Set the project name for the task (required, unless using `--base-task-id`). If the named project does not exist, it is created on-the-fly. | ![Yes](https://clear.ml/docs/latest/icons/ico-optional-yes.svg) |
| `--queue` | Select a task's execution queue. If not provided, a task is created but not launched. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--repo` | URL of remote repository. Example: `--repo https://github.com/clearml/clearml.git`. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--requirements` | Specify `requirements.txt` file to install when setting the session. By default, the` requirements.txt` from the repository will be used. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--skip-python-env-install` | If specified, agent will use the existing Python environment without installing packages. Only applies when running in Docker mode or on Kubernetes. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--script` | Entry point script for the remote execution. When used with `--repo`, input the script's relative path inside the repository. For example: `--script source/train.py`. When used with `--folder`, it supports a direct path to a file inside the local repository itself, for example: `--script ~/project/source/train.py`. | ![Yes](https://clear.ml/docs/latest/icons/ico-optional-yes.svg) |
| `--skip-repo-detection` | If specified, skip repository detection when a repository is not specified. No repository will be set in remote execution. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--skip-task-init` | If set, `Task.init()` call is not added to the entry point, and is assumed to be called within the script. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--tags` | Add tags to the newly created task. For example: `--tags "base" "job"`. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--task-type` | Set the task type. Optional values: training, testing, inference, data\_processing, application, monitor, controller, optimizer, service, qc, custom. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--version` | Display the `clearml-task` utility version. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |

## Usage [​](https://clear.ml/docs/latest/docs/apps/clearml_task/\#usage "Direct link to Usage")

These commands demonstrate a few useful use cases for `clearml-task`.

### Executing Code from a Remote Repository [​](https://clear.ml/docs/latest/docs/apps/clearml_task/\#executing-code-from-a-remote-repository "Direct link to Executing Code from a Remote Repository")

```bash
clearml-task --project examples --name remote_test --repo https://github.com/clearml/events.git --branch master --script /webinar-0620/keras_mnist.py --args batch_size=64 epochs=1 --queue default
```

The `keras_mnist.py` script from the [events](https://github.com/clearml/events) GitHub repository is imported as a
ClearML task named `remote_test` in the `examples` project. Its command line arguments `batch_size` and `epochs` values
are set, and the task is enqueued for execution on the `default` queue.

### Executing a Local Script [​](https://clear.ml/docs/latest/docs/apps/clearml_task/\#executing-a-local-script "Direct link to Executing a Local Script")

Using `clearml-task` to execute a local script is very similar to using it with a [remote repo](https://clear.ml/docs/latest/docs/apps/clearml_task/#executing-code-from-a-remote-repository).

```bash
clearml-task --project examples --name local_test --script keras_mnist.py --branch master --requirements requirements.txt --args epochs=1 --queue default
```

The `keras_mnist.py` script on the user's local machine is imported as a ClearML task named `local_test` in the `examples` project.

Its Python requirements are taken from the local `requirements.txt` file, and its `epochs` command line argument value is set.

The task is enqueued for execution on the `default` queue.

### Pushing a Script to the Server [​](https://clear.ml/docs/latest/docs/apps/clearml_task/\#pushing-a-script-to-the-server "Direct link to Pushing a Script to the Server")

```bash
clearml-task --project examples --name no_execute --script keras_mnist.py --branch master --requirements requirements.txt --args epochs=1
```

The `keras_mnist.py` script on the user's local machine is imported as a ClearML task named `no_execute` in the `examples` project.

Its Python requirements are taken from the local `requirements.txt` file, and its `epochs` command line argument value is set.
The task is created in a _draft_ status (i.e. can be modified in the [WebApp UI](https://clear.ml/docs/latest/docs/webapp/webapp_overview) and later be enqueued).

- [What Is ClearML Task For?](https://clear.ml/docs/latest/docs/apps/clearml_task/#what-is-clearml-task-for)
- [How Does ClearML Task Work?](https://clear.ml/docs/latest/docs/apps/clearml_task/#how-does-clearml-task-work)
- [Execution Configuration](https://clear.ml/docs/latest/docs/apps/clearml_task/#execution-configuration)
  - [Container](https://clear.ml/docs/latest/docs/apps/clearml_task/#container)
  - [Package Dependencies](https://clear.ml/docs/latest/docs/apps/clearml_task/#package-dependencies)
  - [Queue](https://clear.ml/docs/latest/docs/apps/clearml_task/#queue)
  - [Branch and Working Directory](https://clear.ml/docs/latest/docs/apps/clearml_task/#branch-and-working-directory)
  - [Command Line Options](https://clear.ml/docs/latest/docs/apps/clearml_task/#command-line-options)
- [Usage](https://clear.ml/docs/latest/docs/apps/clearml_task/#usage)
  - [Executing Code from a Remote Repository](https://clear.ml/docs/latest/docs/apps/clearml_task/#executing-code-from-a-remote-repository)
  - [Executing a Local Script](https://clear.ml/docs/latest/docs/apps/clearml_task/#executing-a-local-script)
  - [Pushing a Script to the Server](https://clear.ml/docs/latest/docs/apps/clearml_task/#pushing-a-script-to-the-server)