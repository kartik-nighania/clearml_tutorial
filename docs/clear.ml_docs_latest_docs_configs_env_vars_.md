---
url: "https://clear.ml/docs/latest/docs/configs/env_vars/"
title: "Environment Variables | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/configs/env_vars/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

This page lists the available environment variables for configuring ClearML.

note

ClearML's environment variables override the clearml.conf file, SDK, and [configuration vault](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_profile#configuration-vault),
but can be overridden by command-line arguments.

## ClearML SDK Variables [​](https://clear.ml/docs/latest/docs/configs/env_vars/\#clearml-sdk-variables "Direct link to ClearML SDK Variables")

### General [​](https://clear.ml/docs/latest/docs/configs/env_vars/\#general "Direct link to General")

| Name | Description |
| --- | --- |
| **CLEARML\_CACHE\_DIR** | Set the path for the ClearML cache directory, where ClearML stores all downloaded content. |
| **CLEARML\_DEFERRED\_TASK\_INIT** | When set to `1`, sets `Task.init(deferred_init)`: `Task.init()` returns immediately, and server communication runs in a background thread. For more information, see [`deferred_init`](https://clear.ml/docs/latest/docs/references/sdk/task#taskinit). |
| **CLEARML\_DEFAULT\_OUTPUT\_URI** | The default output destination for model checkpoints (snapshots) and artifacts. |
| **CLEARML\_DISABLE\_VAULT\_SUPPORT** | When set to `0`, disable vault support. The SDK will not attempt to load [configuration vaults](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_profile#configuration-vault). Configuration vaults are available under the ClearML Enterprise plan. |
| **CLEARML\_DOCKER\_IMAGE** | Sets the default docker image to use when running an agent in [Docker mode](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_execution_env#docker-mode). |
| **CLEARML\_ENABLE\_ENV\_CONFIG\_SECTION** | When set to `1`, applies the [`environment`](https://clear.ml/docs/latest/docs/configs/clearml_conf#environment-section) section from the `clearml.conf`, which defines key-value pairs that will be set as environment variables at runtime. |
| **CLEARML\_ENABLE\_FILES\_CONFIG\_SECTION** | When set to `1`, applies the [`files`](https://clear.ml/docs/latest/docs/configs/clearml_conf#files-section) section from the `clearml.conf`, which defines files that will be auto-generated with specified content and target paths. |
| **CLEARML\_IGNORE\_MISSING\_CONFIG** | When set to `1`, suppresses errors if a configuration file is not found |
| **CLEARML\_LOG\_ENVIRONMENT** | List of Environment variable names. These environment variables will be logged in the ClearML task's configuration hyperparameters `Environment` section. When executed by a ClearML agent, these values will be set in the task's execution environment. The list should be specified in the following format: `CLEARML_LOG_ENVIRONMENT=VAR_1,VAR_2`. |
| **CLEARML\_LOG\_LEVEL** | Sets the ClearML package's log verbosity. Log levels adhere to [Python log levels](https://docs.python.org/3/library/logging.config.html#configuration-file-format): CRITICAL, ERROR, WARNING, INFO, DEBUG, NOTSET |
| **CLEARML\_SET\_ITERATION\_OFFSET** | Set initial iteration value for the executed task. The task will report its iterations starting with the specified value +1. Specify `0` to force resetting the iteration count. |
| **CLEARML\_SUPPRESS\_UPDATE\_MESSAGE** | Boolean. <br> When set to `1`, suppresses new ClearML package version availability message. |
| **CLEARML\_TASK\_NO\_REUSE** | Boolean. <br> When set to `1`, a new task is created for every execution (see Task [reuse](https://clear.ml/docs/latest/docs/clearml_sdk/task_sdk#task-reuse)). |

### VCS [​](https://clear.ml/docs/latest/docs/configs/env_vars/\#vcs "Direct link to VCS")

Overrides Repository Auto-logging

| Name | Description |
| --- | --- |
| **CLEARML\_VCS\_REPO\_URL** | Repository's URL |
| **CLEARML\_VCS\_COMMIT\_ID** | Repository's Commit ID |
| **CLEARML\_VCS\_BRANCH** | Repository's Branch |
| **CLEARML\_VCS\_ROOT** | Repository's Root directory |
| **CLEARML\_VCS\_WORK\_DIR** | Repository's working directory |
| **CLEARML\_VCS\_STATUS** | Repository status |
| **CLEARML\_VCS\_DIFF** | Base64 encoded string. Holds repo diff logged to a task. If set to an empty string, uncommitted changes are not logged. Note: Overriding CLEARML\_VCS\_DIFF may change the results of a task when executed remotely |
| **CLEARML\_VCS\_ENTRY\_POINT** | Entry point script |

### Server Connection [​](https://clear.ml/docs/latest/docs/configs/env_vars/\#server-connection "Direct link to Server Connection")

| Name | Description |
| --- | --- |
| **CLEARML\_API\_HOST** | Sets the API Server URL |
| **CLEARML\_CONFIG\_FILE** | Sets the ClearML configuration file. Overrides the default configuration file location |
| **CLEARML\_WEB\_HOST** | Sets the Web UI Server URL |
| **CLEARML\_FILES\_HOST** | Sets the File Server URL |
| **CLEARML\_API\_ACCESS\_KEY** | Sets the Server's Public Access Key |
| **CLEARML\_API\_SECRET\_KEY** | Sets the Server's Private Access Key |
| **CLEARML\_API\_HOST\_VERIFY\_CERT** | Enables / Disables server certificate verification (if behind a firewall) |
| **CLEARML\_API\_DEFAULT\_REQ\_METHOD** | _Experimental - this option has not been vigorously tested._ Set the request method for all API requests and auth login. This can be useful when GET requests with payloads are blocked by a server, so POST/PUT requests can be used instead. |
| **CLEARML\_OFFLINE\_MODE** | Sets Offline mode |
| **CLEARML\_NO\_DEFAULT\_SERVER** | Disables sending information to demo server when no HOST server is set |

## Agent Specific Variables [​](https://clear.ml/docs/latest/docs/configs/env_vars/\#agent-specific-variables "Direct link to Agent Specific Variables")

See [here](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_env_var) for environment variables to configure how the ClearML Agent works
with the SDK.

- [ClearML SDK Variables](https://clear.ml/docs/latest/docs/configs/env_vars/#clearml-sdk-variables)
  - [General](https://clear.ml/docs/latest/docs/configs/env_vars/#general)
  - [VCS](https://clear.ml/docs/latest/docs/configs/env_vars/#vcs)
  - [Server Connection](https://clear.ml/docs/latest/docs/configs/env_vars/#server-connection)
- [Agent Specific Variables](https://clear.ml/docs/latest/docs/configs/env_vars/#agent-specific-variables)