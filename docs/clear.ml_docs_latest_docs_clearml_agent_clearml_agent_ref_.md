---
url: "https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_ref/"
title: "ClearML Agent CLI | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_ref/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The following page provides a reference to `clearml-agent`'s CLI commands:

- [build](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_ref/#build) \- Create a worker environment without executing a task.
- [config](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_ref/#config) \- List your ClearML Agent configuration data.
- [daemon](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_ref/#daemon) \- Run a worker daemon listening to a queue for tasks to execute.
- [execute](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_ref/#execute) \- Execute a task, locally without a queue.
- [list](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_ref/#list) \- List the current workers.

## build [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_ref/\#build "Direct link to build")

Use the `build` command to create worker environments without executing tasks.

You can build Docker containers according to the execution environments of specific tasks, which an agent can later
use to execute other tasks. See [tutorial](https://clear.ml/docs/latest/docs/guides/clearml_agent/exp_environment_containers).

You can also create a Docker container that executes a specific task when launched. See [tutorial](https://clear.ml/docs/latest/docs/guides/clearml_agent/executable_exp_containers).

```bash
clearml-agent build [-h] --id TASK_ID [--target TARGET]

                    [--install-globally]

                    [--docker [DOCKER [DOCKER ...]]] [--force-docker]

                    [--python-version PYTHON_VERSION]

                    [--entry-point {reuse_task,clone_task}] [-O]

                    [--git-user GIT_USER] [--git-pass GIT_PASS]

                    [--log-level {DEBUG,INFO,WARN,WARNING,ERROR,CRITICAL}]

                    [--gpus GPUS] [--cpu-only]
```

### Parameters [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_ref/\#parameters "Direct link to Parameters")

| Name | Description | Mandatory |
| --- | --- | --- |
| `--id` | Build a worker environment for this Task ID. | ![Yes](https://clear.ml/docs/latest/icons/ico-optional-yes.svg) |
| `--cpu-only` | Disable GPU access for the Docker container. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--docker` | Run agent in Docker mode. Specify a Docker container that a worker will execute at launch. To specify the image name and optional arguments, use one of the following: <br>- `--docker <image_name> <args>` on the command line<br>- `--docker` on the command line, and specify the default image name and arguments in the configuration file.<br> Environment variable settings for Docker containers: <br>- `CLEARML_DOCKER_SKIP_GPUS_FLAG` \- Ignore the `--gpus` flag inside the Docker container. This also lets you execute ClearML Agent using Docker versions earlier than 19.03.<br>- `NVIDIA_VISIBLE_DEVICES` \- Limit GPU visibility for the Docker container.<br>- `CLEARML_AGENT_GIT_USER` and `CLEARML_AGENT_GIT_PASS` \- Pass these credentials to the Docker container at execution. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--entry-point` | Used in conjunction with `--docker`, indicates how to run the Task specified by `--task-id` on Docker startup. The `--entry-point` options are: <br>- `reuse` \- Overwrite the existing Task data.<br>- `clone_task` \- Clone the Task, and execute the cloned Task. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--force-docker` | Force using the agent-specified docker image (either explicitly in the `--docker` argument or using the agent's default docker image). If provided, the agent will not use any docker container information stored in the task itself (default `False`) | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--git-pass` | Git password for repository access. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--git-user` | Git username for repository access. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--gpus` | Specify the active GPUs for the Docker containers to use. These are the same GPUs set in the `NVIDIA_VISIBLE_DEVICES` environment variable. For example: <br>- `--gpus 0`<br>- `--gpus 0,1,2`<br>- `--gpus all` | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `-h`, `--help` | Get help for this command. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--install-globally` | Install the required Python packages before creating the virtual environment. Use `agent.package_manager.system_site_packages` to control the installation of the system packages. When `--docker` is used, `--install-globally` is always true. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--log-level` | SDK log level. The values are:<br>- `DEBUG`<br>- `INFO`<br>- `WARN`<br>- `WARNING`<br>- `ERROR`<br>- `CRITICAL` | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--python-version` | Virtual environment Python version to use. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `-O` | Compile optimized pyc code (see [python documentation](https://docs.python.org/3/using/cmdline.html#cmdoption-O)). Repeat for more optimization. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--target` | The target folder for the virtual environment and source code that will be used at launch. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |

## config [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_ref/\#config "Direct link to config")

List your ClearML Agent configuration.

```text
clearml-agent config [-h]
```

## daemon [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_ref/\#daemon "Direct link to daemon")

Use the `daemon` command to spin up an agent on any machine: on-prem and/or cloud instance. When spinning up an agent,
assign it a queue(s) to service, and when tasks are added to its queues, the agent will pull and execute them.

With the `daemon` command you can configure your agent's behavior: allocate resources, prioritize queues, set it to run
in a Docker, and more.

```bash
clearml-agent daemon [-h] [--polling-interval POLLING_INTERVAL] [--foreground] [--queue QUEUES [QUEUES ...]]

                     [--order-fairness] [--standalone-mode] [--services-mode [SERVICES_MODE]]

                     [--child-report-tags CHILD_REPORT_TAGS [CHILD_REPORT_TAGS ...]] [--create-queue]

                     [--detached] [--stop [STOP ...]] [--dynamic-gpus] [--uptime [UPTIME ...]]

                     [--downtime [DOWNTIME ...]] [--status] [--check-bootstrap] [--use-owner-token] [-O]

                     [--git-user GIT_USER] [--git-pass GIT_PASS] [--log-level {DEBUG,INFO,WARN,WARNING,ERROR,CRITICAL}]

                     [--gpus GPUS] [--cpu-only] [--podman [PODMAN ...]] [--docker [DOCKER ...]] [--force-current-version]
```

### Parameters [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_ref/\#parameters-1 "Direct link to Parameters")

| Name | Description | Mandatory |
| --- | --- | --- |
| `--check-bootstrap` | On daemon startup, check whether the installed `clearml-agent-bootstrap` package is the latest released version and print a warning if not. Has no effect if `bootstrap` is not detected. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--child-report-tags` | List of tags to send with the status reports from the worker that executes a task. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--cpu-only` | If running in Docker mode (see the `--docker` option), disable GPU access for the Docker container or virtual environment. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--create-queue` | If the queue name provided with `--queue` does not exist in the server, create it on-the-fly and use it. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--detached` | Run agent in the background. The `clearml-agent` command returns immediately. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--docker` | Run in Docker mode. Execute the Task inside a Docker container. To specify the image name and optional arguments, either: <br>- Use `--docker <image_name> <args>` on the command line, or <br>- Use `--docker` on the command line, and specify the default image name and arguments in the configuration file.<br> Environment variable settings for Docker containers: <br>- `CLEARML_DOCKER_SKIP_GPUS_FLAG` \- Ignore the `--gpus` flag inside the Docker container. This also lets you execute ClearML Agent using Docker versions earlier than 19.03.<br>- `NVIDIA_VISIBLE_DEVICES` \- Limit GPU visibility for the Docker container.<br>- `CLEARML_AGENT_GIT_USER` and `CLEARML_AGENT_GIT_PASS` \- Pass these credentials to the Docker container at execution. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--downtime` | Specify downtime for `clearml-agent` in `<hours> <days>` format. For example, use `09-13 TUE` to set Tuesday's downtime to 09-13. <br>NOTES: <br>- This feature requires the agent to use a ClearML Enterprise Server<br>- Make sure to configure only `--uptime` or `--downtime`, but not both. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--dynamic-gpus` | Allow to dynamically allocate GPUs based on queue properties, configure with `--queue <queue_name>=<num_gpus>`. For example: `--dynamic-gpus --queue dual_gpus=2 single_gpu=1`<br>NOTE: **This feature requires the agent to use a ClearML Enterprise Server** | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--force-current-version` | To use your current version of ClearML Agent when running in Docker mode (the `--docker` argument is specified), instead of the latest ClearML Agent version which is automatically installed, specify `force-current-version`. <br> For example, if your current ClearML Agent version is `0.13.1`, but the latest version of ClearML Agent is `0.13.3`, use `--force-current-version` and your Task will execute in the Docker container with ClearML Agent version `0.13.1`. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--foreground` | Pipe full log to stdout/stderr. Do not use this option if running in background. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--git-pass` | Git password for repository access. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--git-user` | Git username for repository access | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--gpus` | If running in Docker mode (see the `--docker` option), specify the active GPUs for the Docker containers to use. These are the same GPUs set in the `NVIDIA_VISIBLE_DEVICES` environment variable. For example: <br>- `--gpus 0`<br>- `--gpus 0,1,2`<br>- `--gpus all` | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `-h`, `--help` | Get help for this command. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--log-level` | SDK log level. The values are:<br>- `DEBUG`<br>- `INFO`<br>- `WARN`<br>- `WARNING`<br>- `ERROR`<br>- `CRITICAL` | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `-O` | Compile optimized pyc code (see [python documentation](https://docs.python.org/3/using/cmdline.html#cmdoption-O)). Repeat for more optimization. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--order-fairness` | Pull from each queue in a round-robin order, instead of priority order. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--podman` | Run execution task inside a container using Podman. Optionally, specify `args <image> <arguments>`, or set the default docker image and arguments in `agent.default_docker.image` / `agent.default_docker.arguments` in the `clearml.conf`. Use `--gpus`/`--cpu-only` (or set `NVIDIA_VISIBLE_DEVICES`) to limit GPU visibility for docker. This behaves identically to `--docker`, except the resulting `docker run` command includes the adjustments required by Podman. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--polling-interval` | Polling interval in seconds. Minimum value is `5` (default `5`) | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--queue` | Specify the queues which the worker is listening to. The values can be any combination of:<br>- One or more queue IDs<br>- One or more queue names<br>- `default` indicating the default queue | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--services-mode` | Launch multiple long-term docker services. Spin multiple, simultaneous Tasks, each in its own Docker container, on the same machine. Each Task will be registered as a new node in the system, providing tracking and transparency capabilities. Start up and shutdown of each Docker is verified. Use in CPU mode (`--cpu-only`) only. <br> To limit the number of simultaneous tasks run in services mode, pass the maximum number immediately after the `--services-mode` option (e.g. `--services-mode 5`) | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--standalone-mode` | Do not use any network connects. This assumes all requirements are pre-installed. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--status` | Print the worker's schedule (uptime properties, server's runtime properties and listening queues) | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--stop` | Terminate a running ClearML Agent, if other arguments are the same. If no additional arguments are provided, agents are terminated in lexicographical order. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--uptime` | Specify uptime for `clearml-agent` in `<hours> <days>` format. For example, use `17-20 TUE` to set Tuesday's uptime to 17-20. <br>NOTES:<br>- This feature requires the agent to use a ClearML Enterprise Server<br>- Make sure to configure only `--uptime` or `--downtime`, but not both. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--use-owner-token` | Run tasks under the identity of each task's owner: all calls made by the task code during execution will use the owner's credentials instead of the agent's. See example use case under [Service Accounts](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_users#service-accounts). **This feature requires the agent to use a ClearML Enterprise Server**. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |

## execute [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_ref/\#execute "Direct link to execute")

Use the `execute` command to set an agent to build and execute specific tasks directly without listening to a queue.

```bash
clearml-agent execute [-h] --id TASK_ID [--log-file LOG_FILE] [--disable-monitoring]

                      [--full-monitoring] [--require-queue]

                      [--standalone-mode] [--docker [DOCKER [DOCKER ...]]] [--clone]

                      [-O] [--git-user GIT_USER] [--git-pass GIT_PASS]

                      [--log-level {DEBUG,INFO,WARN,WARNING,ERROR,CRITICAL}]

                      [--gpus GPUS] [--cpu-only]
```

### Parameters [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_ref/\#parameters-2 "Direct link to Parameters")

| Name | Description | Mandatory |
| --- | --- | --- |
| `--id` | The ID of the Task to build | ![Yes](https://clear.ml/docs/latest/icons/ico-optional-yes.svg) |
| `--clone` | Clone the Task specified by `--id`, and then execute that cloned Task. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--cpu-only` | Disable GPU access for the daemon, only use CPU in either docker or virtual environment. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--docker` | Run in Docker mode. Execute the Task inside a Docker container. To specify the image name and optional arguments, use one of the following: <br>- `--docker <image_name> <args>` on the command line<br>- `--docker` on the command line, and specify the default image name and arguments in the configuration file.<br> Environment variable settings for Dockers containers: <br>- `CLEARML_DOCKER_SKIP_GPUS_FLAG` \- Ignore the `--gpus` flag inside the Docker container. This also lets you execute ClearML Agent using Docker versions earlier than 19.03.<br>- `NVIDIA_VISIBLE_DEVICES` \- Limit GPU visibility for the Docker container.<br>- `CLEARML_AGENT_GIT_USER` and `CLEARML_AGENT_GIT_PASS` \- Pass these credentials to the Docker container at execution. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--disable-monitoring` | Disable logging and monitoring, except for stdout. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--full-monitoring` | Create a full log, including the environment setup log, Task log, and monitoring, as well as stdout. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--git-pass` | Git password for repository access. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--git-user` | Git username for repository access. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--gpus` | Specify active GPUs for the daemon to use (docker / virtual environment). Equivalent to setting `NVIDIA_VISIBLE_DEVICES`. For example: <br>- `--gpus 0`<br>- `--gpus 0,1,2`<br>- `--gpus all` | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `-h`, `--help` | Get help for this command. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--log-file` | The log file for Task execution output (stdout / stderr) to a text file. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--log-level` | SDK log level. The values are:<br>- `DEBUG`<br>- `INFO`<br>- `WARN`<br>- `WARNING`<br>- `ERROR`<br>- `CRITICAL` | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `-O` | Compile optimized pyc code (see [python documentation](https://docs.python.org/3/using/cmdline.html#cmdoption-O)). Repeat for more optimization. | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--require-queue` | If the specified task is not queued, the execution will fail (used for 3rd party scheduler integration, e.g. K8s, SLURM, etc.) | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |
| `--standalone-mode` | Do not use any network connects, assume everything is pre-installed | ![No](https://clear.ml/docs/latest/icons/ico-optional-no.svg) |

## list [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_ref/\#list "Direct link to list")

List information about all active workers.

```bash
clearml-agent list [-h]
```

- [build](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_ref/#build)
  - [Parameters](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_ref/#parameters)
- [config](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_ref/#config)
- [daemon](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_ref/#daemon)
  - [Parameters](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_ref/#parameters-1)
- [execute](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_ref/#execute)
  - [Parameters](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_ref/#parameters-2)
- [list](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_ref/#list)