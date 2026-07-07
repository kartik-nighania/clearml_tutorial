---
url: "https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_env_var/"
title: "ClearML Agent Environment Variables | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_env_var/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

This page lists the available environment variables for configuring ClearML Agent.

In addition to the environment variables listed below, ClearML also supports **dynamic environment variables** to override
any configuration option that appears in the [`agent`](https://clear.ml/docs/latest/docs/configs/clearml_conf#agent-section) section of the `clearml.conf`.
For more information, see [Dynamic Environment Variables](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_bare_metal#dynamic-environment-variables).

note

ClearML's environment variables override the [clearml.conf file](https://clear.ml/docs/latest/docs/configs/clearml_conf), SDK, and
[configuration vault](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_profile#configuration-vault),
but can be overridden by command-line arguments.

List Formatting

Some environment variables accept lists (multiple arguments, labels, flags, or patterns).
When setting a list value, separate each item with a space. For example: `VAR="item1 item2 item3"`

| Name | Description |
| --- | --- |
| **CLEARML\_DOCKER\_IMAGE** | Sets the default Docker image to use when running an agent in [Docker mode](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_execution_env#docker-mode) |
| **CLEARML\_WORKER\_ID** | Sets the agent's ID. This ID appears in the output of `clearml-agent list` and in the worker list in the UI's **Workers & Queues** page. <br> If not specified, it defaults to: `<hostname>:<process_id>`. <br> Use `CLEARML_WORKER_NAME` to set a custom name instead of `<hostname>`. |
| **CLEARML\_WORKER\_NAME** | Sets a custom agent name.<br> If `CLEARML_WORKER_ID` is not set, this value replaces the machine's hostname when the worker name is generated.<br> For example, if `CLEARML_WORKER_NAME` is `MyMachine` and the agent's `process_id` is `12345`, then the worker is named `MyMachine.12345`.<br> When `CLEARML_WORKER_ID` is not set, this name appears in the output of `clearml-agent list` and in the worker list in the UI's **Workers & Queues** page. |
| **CLEARML\_CUDA\_VERSION** | Sets the CUDA version to be used by the agent. When unspecified, the CUDA version is automatically detected. |
| **CLEARML\_CUDNN\_VERSION** | Sets the cuDNN version to be used by the agent. When unspecified, the cuDNN version is automatically detected. |
| **CLEARML\_CPU\_ONLY** | Boolean. If set to `1`, forces CPU-only mode. When running an agent in [Docker mode](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_execution_env#docker-mode), this disables GPU access for the container. |
| **CLEARML\_DOCKER\_SKIP\_GPUS\_FLAG** | Boolean. If set to `1`, the agent will not add the `--gpus` flag when launching Docker containers. This allows you to execute ClearML Agent using Docker versions earlier than 19.03. |
| **CLEARML\_AGENT\_ABORT\_CALLBACK\_CMD** | Path to a callback script to execute when a Task is aborted. The script may run up to the maximum time set with `CLEARML_AGENT_ABORT_CALLBACK_TIMEOUT`. Set task callback script using `-e CLEARML_AGENT_ABORT_CALLBACK_CMD=path/script.sh`. |
| **CLEARML\_AGENT\_ABORT\_CALLBACK\_TIMEOUT** | Maximum time (in seconds) the abort callback script (set with `CLEARML_AGENT_ABORT_CALLBACK_CMD`) is allowed to run. Set abort callback timeout using `-e CLEARML_AGENT_ABORT_CALLBACK_TIMEOUT=30`. |
| **CLEARML\_AGENT\_DOCKER\_ARGS\_FILTERS** | A list of allowed Docker arguments (regex patterns). Only arguments matching these patterns can be used when running a task. Use `shlex.split` formatting, separating multiple patterns with spaces. For example: `CLEARML_AGENT_DOCKER_ARGS_FILTERS="^--env$ ^-e$"` |
| **CLEARML\_AGENT\_DOCKER\_ARGS\_HIDE\_ENV** | Specify Docker environment variable values the console log should obfuscate. When printed, the variable values will be replaced by `********`. By default, `CLEARML_API_SECRET_KEY`, `CLEARML_AGENT_GIT_PASS`, `AWS_SECRET_ACCESS_KEY`, and `AZURE_STORAGE_KEY` values are redacted. **Separate multiple variables with spaces**. |
| **CLEARML\_AGENT\_DISABLE\_SSH\_MOUNT** | Boolean. If set to `1`, disables automatic mounting of the `.ssh` directory into the container. |
| **CLEARML\_AGENT\_FORCE\_CODE\_DIR** | Skip repository cloning and/or applying any changes to the code. The agent will execute the entry point from the provided path. |
| **CLEARML\_AGENT\_FORCE\_UV** | If set to `1`, force the agent to use UV as the package manager. Overrides the default manager set in the [clearml.conf](https://clear.ml/docs/latest/docs/configs/clearml_conf) under `agent.package_manager.type` |
| **CLEARML\_AGENT\_FORCE\_EXEC\_SCRIPT** | Overrides the remote execution script to bypass repository cloning and execute code already available where the remote agent is running. Use `module:file.py` format to specify a module and a script to execute (e.g. `.:main.py` to run `main.py` from the working dir) |
| **CLEARML\_AGENT\_FORCE\_TASK\_INIT** | If set to `1`, the agent adds `Task.init()` to scripts that do not include it, creating a Task to capture code execution information and output, which is then sent to the ClearML Server. If set to `0`, scripts without `Task.init()` will still run, but the agent will capture only the output streams and console output, not code execution details, metrics, or models. |
| **CLEARML\_AGENT\_FORCE\_SYSTEM\_SITE\_PACKAGES** | Boolean. If set to `1`, overrides default [`agent.package_manager.system_site_packages: true`](https://clear.ml/docs/latest/docs/configs/clearml_conf#system_site_packages) behavior when running tasks in containers (docker mode and k8s-glue) |
| **CLEARML\_AGENT\_GIT\_CLONE\_VERBOSE** | Boolean. If set to `1`, `git clone` calls will report progress verbosely |
| **CLEARML\_AGENT\_GIT\_USER** | Git username so the agent can access and clone task repositories. Do not set when using SSH authentication or public repositories. |
| **CLEARML\_AGENT\_GIT\_PASS** | Git password so the agent can access and clone task repositories. Do not set when using SSH authentication or public repositories. |
| **CLEARML\_AGENT\_GIT\_HOST** | Limits Git credentials usage to the specified host. |
| **CLEARML\_AGENT\_GIT\_USE\_MS\_ENTRA\_TOKEN** | Boolean. If set to `1`, enables authentication to Azure DevOps repositories using a Microsoft Entra token. The Azure token will be taken from the git password setting (`CLEARML_AGENT_GIT_PASS` or `agent.git_host`). `CLEARML_AGENT_GIT_USE_MS_ENTRA_TOKEN` and `CLEARML_AGENT_GIT_USE_AZURE_PAT` are mutually exclusive, only one can be set to `1`. For more information, see the [Azure DevOps authentication guide](https://learn.microsoft.com/en-us/azure/devops/repos/git/auth-overview?view=azure-devops&tabs=Linux#microsoft-entra-oauth-tokens-recommended). |
| **CLEARML\_AGENT\_GIT\_USE\_AZURE\_PAT** | Boolean. If set to `1`, enables authentication to Azure DevOps repositories using a Personal Access Token (PAT). The PAT will be taken from the git password setting (`CLEARML_AGENT_GIT_PASS` or `agent.git_host`). `CLEARML_AGENT_GIT_USE_MS_ENTRA_TOKEN` and `CLEARML_AGENT_GIT_USE_AZURE_PAT` are mutually exclusive, only one can be set to `1`. For more information, see the [Azure DevOps authentication guide](https://learn.microsoft.com/en-us/azure/devops/repos/git/auth-overview?view=azure-devops&tabs=Linux#personal-access-tokens-alternative-option) |
| **CLEARML\_AGENT\_EXEC\_USER** | Sets the user for an agent executing tasks (`root` by default). Only for Linux. |
| **CLEARML\_AGENT\_EXTRA\_DOCKER\_ARGS** | Optional Docker arguments to pass when ClearML Agent is running in [Docker mode](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_execution_env#docker-mode). Applies only to this agent and does not modify the task’s `docker_cmd` section. **Separate multiple arguments with spaces**. |
| **CLEARML\_AGENT\_EXTRA\_DOCKER\_LABELS** | List of labels to add to Docker container. **Separate multiple labels with spaces**. See [Docker documentation](https://docs.docker.com/config/labels-custom-metadata/). |
| **CLEARML\_EXTRA\_PIP\_INSTALL\_FLAGS** | List of additional flags to use when the agent installs packages. **Separate multiple flags with spaces**. For example: `CLEARML_EXTRA_PIP_INSTALL_FLAGS=--use-deprecated=legacy-resolver` for a single flag or `CLEARML_EXTRA_PIP_INSTALL_FLAGS="--use-deprecated=legacy-resolver --no-warn-conflicts"` for multiple flags |
| **CLEARML\_AGENT\_EXTRA\_PYTHON\_PATH** | Sets extra Python path |
| **CLEARML\_AGENT\_INITIAL\_CONNECT\_RETRY\_OVERRIDE** | Number of retries the agent should attempt when initially connecting to the ClearML Server. |
| **CLEARML\_AGENT\_NO\_UPDATE** | Boolean. If set to 1, skip agent update inside K8s pod before the agent executes the task |
| **CLEARML\_AGENT\_K8S\_HOST\_MOUNT** / **CLEARML\_AGENT\_DOCKER\_HOST\_MOUNT** | Sets the host path to mount inside Docker/Kubernetes task environments |
| **CLEARML\_AGENT\_TEMP\_STDOUT\_FILE\_DIR** | Overrides the default `/tmp` location for storing agent temporary output files |
| **CLEARML\_K8S\_GLUE\_START\_AGENT\_SCRIPT\_PATH** | Sets an alternate path for the agent startup script generated inside a k8s task pod (instead of the default `~/~/__start_agent__.sh`) |
| **CLEARML\_AGENT\_PACKAGE\_PYTORCH\_RESOLVE** | Sets the PyTorch resolving mode. The options are: <br>- `none` \- No resolving. Install PyTorch like any other package<br>- `pip` (default) - Sets extra index based on cuda and lets pip resolve<br>- `direct` \- Resolve a direct link to the PyTorch wheel by parsing the pytorch.org pip repository, and matching the automatically detected cuda version with the required PyTorch wheel. If the exact cuda version is not found for the required PyTorch wheel, it will try a lower cuda version until a match is found |
| **CLEARML\_AGENT\_DEBUG\_INFO** | Enables additional debug information for specific contexts (currently only `docker` is supported) |
| **CLEARML\_AGENT\_CHILD\_AGENTS\_COUNT\_CMD** | Custom command to list child agents when running in services mode. Default command: `'docker ps --filter label={parent_worker_label} --format {{{{.ID}}}}'` |
| **CLEARML\_AGENT\_SKIP\_PIP\_VENV\_INSTALL** | Instead of creating a new virtual environment inheriting from the system packages, use an existing virtual environment and install missing packages directly to it. Specify the Python binary of the existing virtual environment. For example: `CLEARML_AGENT_SKIP_PIP_VENV_INSTALL=/home/venv/bin/python`. <br>**Note:** By default, ClearML Agent will still install any missing packages into the specified virtual environment. To ensure no additional packages will be installed, also set `CLEARML_AGENT_SKIP_PYTHON_ENV_INSTALL=1`. |
| **CLEARML\_AGENT\_SKIP\_PYTHON\_ENV\_INSTALL** | Boolean. Skips entire Python virtual environment installation and assumes Python and dependencies are already installed. |
| **CLEARML\_AGENT\_VENV\_CACHE\_PATH** | Sets directory for virtual environment caching. Enables virtual environment caching |
| **CLEARML\_MULTI\_NODE\_SINGLE\_TASK** | Control how multi-node resource monitoring is reported. The options are: <br>- `-1` \- Only master node's (rank zero) console/resources are reported<br>- `1` \- Graph per node i.e. machine/GPU graph for every node (console output prefixed with RANK)<br>- `2` \- Series per node under a unified machine resource graph, graph per type of resource e.g. CPU/GPU utilization (console output prefixed with RANK) |