---
url: "https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_execution_env/"
title: "Execution Environments | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_execution_env/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

ClearML Agent has two primary execution modes: [Virtual Environment Mode](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_execution_env/#virtual-environment-mode) and [Docker Mode](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_execution_env/#docker-mode).

## Virtual Environment Mode [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_execution_env/\#virtual-environment-mode "Direct link to Virtual Environment Mode")

In Virtual Environment Mode, the agent creates a virtual environment for the task, installs the required Python
packages based on the task specification, clones the code repository, applies the uncommitted changes and finally
executes the code while monitoring it. This mode uses smart caching so packages and environments can be reused over
multiple tasks (see [Virtual Environment Reuse](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_env_caching#virtual-environment-reuse)).

ClearML Agent supports working with one of the following package managers:

- [`pip`](https://en.wikipedia.org/wiki/Pip_(package_manager)) (default)
- [`conda`](https://docs.conda.io/en/latest/)
- [`uv`](https://docs.astral.sh/uv/)
- [`poetry`](https://python-poetry.org/)

To change the package manager used by the agent, edit the [`package_manager.type`](https://clear.ml/docs/latest/docs/configs/clearml_conf#agentpackage_manager)
field in the of the `clearml.conf`. If extra channels are needed for `conda`, add the missing channels in the
`package_manager.conda_channels` field in the `clearml.conf`.

Using Poetry with Pyenv

Some versions of poetry (using `install-poetry.py`) do not respect `pyenv global`.

If you are using pyenv to control the environment where you use ClearML Agent, you can:

- Use poetry v1.2 and above (which fixes [this issue](https://github.com/python-poetry/poetry/issues/5077))
- Install poetry with the deprecated `get-poetry.py` installer

## Docker Mode [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_execution_env/\#docker-mode "Direct link to Docker Mode")

Notes

- Docker Mode is only supported in Linux.
- Docker Mode requires docker service v19.03 or higher installed.
- If your machine requires root permissions to run Docker, the ClearML Agent in Docker Mode must also run with root permissions.

When executing the ClearML Agent in Docker mode, it will:

1. Run the provided Docker container
2. Install ClearML Agent in the container
3. Execute the Task in the container, and monitor the process.

ClearML Agent uses the provided default Docker container, which can be overridden from the UI.

Setting Docker Container via UI

You can set the docker container via the UI:

1. Clone the task

2. Set the Docker in the cloned task's **Execution** tab **\> Container** section

![Container section](https://clear.ml/docs/latest/assets/images/webapp_exp_container-47f6ff6f7aaa8c95bfad7721dc45290b.png#light-mode-only)![Container section](https://clear.ml/docs/latest/assets/images/webapp_exp_container_dark-1785e55dbcd64e3a35044fe8c937b96f.png#dark-mode-only)

3. Enqueue the cloned task


The task will be executed in the container specified in the UI.

All ClearML Agent flags (such as `--gpus` and `--foreground`) are applicable to Docker mode as well.

- To execute ClearML Agent in Docker mode, run:





```bash
clearml-agent daemon --queue <execution_queue_to_pull_from> --docker [optional default docker image to use]
```

- To use the current `clearml-agent` version in the Docker container, instead of the latest `clearml-agent` version that is
automatically installed, pass the `--force-current-version` flag:





```bash
clearml-agent daemon --queue default --docker --force-current-version
```

- For Kubernetes, specify a host mount on the daemon host. Do not use the host mount inside the Docker container.
Set the environment variable `CLEARML_AGENT_K8S_HOST_MOUNT`.
For example:





```text
CLEARML_AGENT_K8S_HOST_MOUNT=/mnt/host/data:/root/.clearml
```


- [Virtual Environment Mode](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_execution_env/#virtual-environment-mode)
- [Docker Mode](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_execution_env/#docker-mode)