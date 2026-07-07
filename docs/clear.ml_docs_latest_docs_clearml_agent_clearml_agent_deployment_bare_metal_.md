---
url: "https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_bare_metal/"
title: "Bare Metal/Virtual Machines | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_bare_metal/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

This page explains how to install and deploy ClearML Agent on bare-metal servers or VMs.

## Installation [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_bare_metal/\#installation "Direct link to Installation")

To install [ClearML Agent](https://clear.ml/docs/latest/docs/clearml_agent), execute

```bash
pip install clearml-agent
```

important

Install ClearML Agent as a system Python package and not in a Python virtual environment.
An agent that runs in Virtual Environment Mode or Conda Environment Mode needs to create virtual environments, and
it can't do that when running from a virtual environment.

ClearML Agent Bootstrap

Bootstrap provides self-contained Python, Git, and other required binaries,
allowing tasks to run in minimal container images that do not include these tools.

It can be installed on this machine independently of agent initialization and does not require a ClearML Server connection.

For details, see [ClearML Agent Bootstrap](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_bootstrap).

## Configuration [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_bare_metal/\#configuration "Direct link to Configuration")

note

If ClearML was previously configured, follow [this](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_bare_metal/#adding-clearml-agent-to-a-configuration-file) to add
ClearML Agent specific configurations.

1. In a terminal session, execute





```bash
clearml-agent init
```









The setup wizard prompts for ClearML credentials (see [here](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_profile#clearml-api-credentials) about obtaining credentials).





```text
Please create new clearml credentials through the settings page in your `clearml-server` web app,

or create a free account at https://app.clear.ml/settings/webapp-configuration



In the settings > workspace page, press "Create new credentials", then press "Copy to clipboard".



Paste copied configuration here:
```









If the setup wizard's response indicates that a configuration file already exists, follow the instructions [here](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_bare_metal/#adding-clearml-agent-to-a-configuration-file).
The wizard does not edit or overwrite existing configuration files.

2. At the command prompt `Paste copied configuration here:`, paste the ClearML credentials and press **Enter**.
The setup wizard confirms the credentials.





```text
Detected credentials key="********************" secret="*******"
```

3. **Enter** to accept the default server URL, which is detected from the credentials or enter a ClearML web server URL.

A secure protocol, https, must be used. **Do not use http.**





```text
WEB Host configured to: [https://app.clear.ml]
```











note





If you are using a self-hosted ClearML Server, the default URL will use your domain.

4. Do as above for API, URL, and file servers.

5. The wizard responds with your configuration:





```text
CLEARML Hosts configuration:

Web App: https://app.clear.ml

API: https://api.clear.ml

File Store: https://files.clear.ml



Verifying credentials ...

Credentials verified!
```

6. Input the default output URI. Model checkpoints (snapshots) and task artifacts will be stored in this output location.





```text
Default Output URI (used to automatically store models and artifacts): (N)one/ClearML (S)erver/(C)ustom [None]
```

7. Enter your Git username and password. Leave blank for SSH key authentication or when only using public repositories.

This is needed for cloning repositories by the agent.





```text
Enter git username for repository cloning (leave blank for SSH key authentication): []

Enter password for user '<username>':
```









The setup wizard confirms your git credentials.





```text
Git repository cloning will be using user=<username> password=<password>
```

8. Enter an additional artifact repository, or press **Enter** if not required.

This is needed for installing Python packages not found in pypi.





```text
Enter additional artifact repository (extra-index-url) to use when installing python packages (leave blank if not required):
```









The setup wizard completes.





```text
New configuration stored in /home/<username>/clearml.conf

CLEARML-AGENT setup completed successfully.
```









The configuration file location depends upon the operating system:
   - Linux - `~/clearml.conf`
   - Mac - `$HOME/clearml.conf`
   - Windows - `\User\<username>\clearml.conf`
9. Optionally, configure ClearML options for **ClearML Agent** (default docker, package manager, etc.). See the [ClearML Configuration Reference](https://clear.ml/docs/latest/docs/configs/clearml_conf)
and the [ClearML Agent Environment Variables reference](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_env_var).


note

The ClearML Enterprise server provides a [configuration vault](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_profile#configuration-vault), the contents
of which are categorically applied on top of the agent-local configuration.

### Adding ClearML Agent to a Configuration File [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_bare_metal/\#adding-clearml-agent-to-a-configuration-file "Direct link to Adding ClearML Agent to a Configuration File")

In case a `clearml.conf` file already exists, add a few ClearML Agent specific configurations to it.

**Adding ClearML Agent to a ClearML configuration file:**

1. Open the ClearML configuration file for editing. Depending upon the operating system, it is:
   - Linux - `~/clearml.conf`
   - Mac - `$HOME/clearml.conf`
   - Windows - `\User\<username>\clearml.conf`
2. After the `api` section, add your `agent` section. For example:





```text
agent {

       # Set GIT user/pass credentials (if user/pass are set, GIT protocol will be set to https)

       git_user=""

       git_pass=""

       # all other domains will use public access (no user/pass). Default: always send user/pass for any VCS domain

       git_host=""



       # Force GIT protocol to use SSH regardless of the git url (Assumes GIT user/pass are blank)

       force_git_ssh_protocol: false



       # unique name of this worker, if None, created based on hostname:process_id

       # Overridden with os environment: CLEARML_WORKER_NAME

       worker_id: ""

}
```









View a complete ClearML Agent configuration file sample including an `agent` section [here](https://github.com/clearml/clearml-agent/blob/master/docs/clearml.conf).

3. Save the configuration.


### Dynamic Environment Variables [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_bare_metal/\#dynamic-environment-variables "Direct link to Dynamic Environment Variables")

Dynamic ClearML Agent environment variables can be used to override any configuration setting that appears in the [`agent`](https://clear.ml/docs/latest/docs/configs/clearml_conf#agent-section)
section of the `clearml.conf`.

The environment variable's name should be `CLEARML_AGENT__AGENT__<configuration-path>`, where `<configuration-path>`
represents the full path to the configuration field being set. Elements of the configuration path should be separated by
`__` (double underscore). For example, set the `CLEARML_AGENT__AGENT__DEFAULT_DOCKER__IMAGE` environment variable to
deploy an agent with a different value to what is specified for `agent.default_docker.image` in the clearml.conf.

Notes

- Since configuration fields may contain JSON-parsable values, make sure to always quote strings (otherwise the agent
might fail to parse them)
- To comply with environment variables standards, it is recommended to use only upper-case characters in
environment variable keys. For this reason, ClearML Agent will always convert the configuration path specified in the
dynamic environment variable's key to lower-case before overriding configuration values with the environment variable
value.

### Security Considerations [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_bare_metal/\#security-considerations "Direct link to Security Considerations")

ClearML Agent is designed for maximum flexibility in facilitating users' execution of their workloads.
For example, users can specify docker arguments that the agent will make use of as part of the `docker` invocation when setting up their task execution environment.

Where stricter controls are required, administrators can restrict the command-line options passed to Docker to, for example,
prevent users from running privileged containers.

These restrictions can be configured by:

- Configuration File: The `agent.docker_args_filters` setting in the clearml.conf file [agent](https://clear.ml/docs/latest/docs/configs/clearml_conf#agent-section) section.
- Environment Variable: The `CLEARML_AGENT_DOCKER_ARGS_FILTERS` environment variable. (See the [ClearML Agent Environment Variables reference](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_env_var)).

To completely separate the compute fabric from your workloads, it is recommended to deploy the agent onto an orchestrator such as [Kubernetes](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_k8s).

## Spinning Up an Agent [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_bare_metal/\#spinning-up-an-agent "Direct link to Spinning Up an Agent")

You can spin up an agent on any machine: on-prem and/or cloud instance. When spinning up an agent, you assign it to
service a queue(s). Utilize the machine by enqueuing tasks to the queue that the agent is servicing, and the agent will
pull and execute the tasks.

cross-platform execution

ClearML Agent is platform-agnostic. When using the ClearML Agent to execute tasks cross-platform, set platform
specific environment variables before launching the agent.

For example, to run an agent on an ARM device, set the core type environment variable before spinning up the agent:

```bash
export OPENBLAS_CORETYPE=ARMV8

clearml-agent daemon --queue <queue_name>
```

### Executing an Agent [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_bare_metal/\#executing-an-agent "Direct link to Executing an Agent")

To execute an agent, listening to a queue, run:

```bash
clearml-agent daemon --queue <queue_name>
```

### Executing in Background [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_bare_metal/\#executing-in-background "Direct link to Executing in Background")

To execute an agent in the background, run:

```bash
clearml-agent daemon --queue <execution_queue_to_pull_from> --detached
```

### Stopping Agents [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_bare_metal/\#stopping-agents "Direct link to Stopping Agents")

To stop an agent running in the background, run:

```bash
clearml-agent daemon <arguments> --stop
```

### Allocating Resources [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_bare_metal/\#allocating-resources "Direct link to Allocating Resources")

To specify GPUs associated with the agent, add the `--gpus` flag.

Docker Mode

Make sure to include the `--docker` flag, as GPU management through the agent is only supported in [Docker Mode](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_execution_env#docker-mode).

To execute multiple agents on the same machine (usually assigning GPU for the different agents), run:

```bash
clearml-agent daemon --gpus 0 --queue default --docker

clearml-agent daemon --gpus 1 --queue default --docker
```

To allocate more than one GPU, provide a list of allocated GPUs

```bash
clearml-agent daemon --gpus 0,1 --queue dual_gpu --docker
```

### Queue Prioritization [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_bare_metal/\#queue-prioritization "Direct link to Queue Prioritization")

A single agent can listen to multiple queues. The priority is set by their order.

```bash
clearml-agent daemon --queue high_q low_q
```

This ensures the agent first tries to pull a Task from the `high_q` queue, and only if it is empty, the agent will try to pull
from the `low_q` queue.

To make sure an agent pulls from all queues equally, add the `--order-fairness` flag.

```bash
clearml-agent daemon --queue group_a group_b --order-fairness
```

It will make sure the agent will pull from the `group_a` queue, then from `group_b`, then back to `group_a`, etc. This ensures
that `group_a` or `group_b` will not be able to starve one another of resources.

### SSH Access [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_bare_metal/\#ssh-access "Direct link to SSH Access")

By default, ClearML Agent maps the host's `~/.ssh` into the container's `/root/.ssh` directory (configurable,
see [clearml.conf](https://clear.ml/docs/latest/docs/configs/clearml_conf#docker_internal_mounts)).

If you want to use existing auth sockets with ssh-agent, you can verify your host ssh-agent is working correctly with:

```commandline
echo $SSH_AUTH_SOCK
```

You should see a path to a temporary file, something like this:

```console
/tmp/ssh-<random>/agent.<random>
```

Then run your `clearml-agent` in Docker mode, which will automatically detect the `SSH_AUTH_SOCK` environment variable,
and mount the socket into any container it spins.

You can also explicitly set the `SSH_AUTH_SOCK` environment variable when executing an agent. The command below will
execute an agent in Docker mode and assign it to service a queue. The agent will have access to
the SSH socket provided in the environment variable.

```text
SSH_AUTH_SOCK=<file_socket> clearml-agent daemon --gpus <your config> --queue <your queue name>  --docker
```

## Google Colab [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_bare_metal/\#google-colab "Direct link to Google Colab")

ClearML Agent can run on a [Google Colab](https://colab.research.google.com/) instance. This helps users to leverage
compute resources provided by Google Colab and send tasks for execution on it.

Check out [this tutorial](https://clear.ml/docs/latest/docs/guides/ide/google_colab) on how to run a ClearML Agent on Google Colab!

## Explicit Task Execution [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_bare_metal/\#explicit-task-execution "Direct link to Explicit Task Execution")

ClearML Agent can also execute specific tasks directly, without listening to a queue.

### Execute a Task without Queue [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_bare_metal/\#execute-a-task-without-queue "Direct link to Execute a Task without Queue")

Execute a Task with a `clearml-agent` worker without a queue.

```bash
clearml-agent execute --id <task-id>
```

### Clone a Task and Execute the Cloned Task [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_bare_metal/\#clone-a-task-and-execute-the-cloned-task "Direct link to Clone a Task and Execute the Cloned Task")

Clone the specified Task and execute the cloned Task with a `clearml-agent` worker without a queue.

```bash
clearml-agent execute --id <task-id> --clone
```

### Execute Task inside a Docker [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_bare_metal/\#execute-task-inside-a-docker "Direct link to Execute Task inside a Docker")

Execute a Task with a `clearml-agent` worker using a Docker container without a queue.

```bash
clearml-agent execute --id <task-id> --docker
```

## Debugging [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_bare_metal/\#debugging "Direct link to Debugging")

Run a `clearml-agent` daemon in foreground mode, sending all output to the console.

```bash
clearml-agent daemon --queue default --foreground
```

- [Installation](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_bare_metal/#installation)
- [Configuration](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_bare_metal/#configuration)
  - [Adding ClearML Agent to a Configuration File](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_bare_metal/#adding-clearml-agent-to-a-configuration-file)
  - [Dynamic Environment Variables](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_bare_metal/#dynamic-environment-variables)
  - [Security Considerations](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_bare_metal/#security-considerations)
- [Spinning Up an Agent](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_bare_metal/#spinning-up-an-agent)
  - [Executing an Agent](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_bare_metal/#executing-an-agent)
  - [Executing in Background](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_bare_metal/#executing-in-background)
  - [Stopping Agents](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_bare_metal/#stopping-agents)
  - [Allocating Resources](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_bare_metal/#allocating-resources)
  - [Queue Prioritization](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_bare_metal/#queue-prioritization)
  - [SSH Access](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_bare_metal/#ssh-access)
- [Google Colab](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_bare_metal/#google-colab)
- [Explicit Task Execution](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_bare_metal/#explicit-task-execution)
  - [Execute a Task without Queue](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_bare_metal/#execute-a-task-without-queue)
  - [Clone a Task and Execute the Cloned Task](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_bare_metal/#clone-a-task-and-execute-the-cloned-task)
  - [Execute Task inside a Docker](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_bare_metal/#execute-task-inside-a-docker)
- [Debugging](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_bare_metal/#debugging)