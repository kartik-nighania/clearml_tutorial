---
url: "https://clear.ml/docs/latest/docs/configs/clearml_conf/"
title: "Configuration File | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/configs/clearml_conf/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

This reference page provides detailed information about the configurable options for ClearML and ClearML Agent.
ClearML and ClearML Agent use the same configuration file `clearml.conf`.

This reference page is organized by configuration file section:

- [agent](https://clear.ml/docs/latest/docs/configs/clearml_conf/#agent-section) \- Contains ClearML Agent configuration options. If ClearML Agent was not installed, the configuration
file will not have an `agent` section.
- [api](https://clear.ml/docs/latest/docs/configs/clearml_conf/#api-section) \- Contains ClearML and ClearML Agent configuration options for ClearML Server.
- [sdk](https://clear.ml/docs/latest/docs/configs/clearml_conf/#sdk-section) \- Contains ClearML and ClearML Agent configuration options for ClearML Python Package and ClearML Server.
- [environment](https://clear.ml/docs/latest/docs/configs/clearml_conf/#environment-section) \- Define environment variables to apply to the OS environment
- [files](https://clear.ml/docs/latest/docs/configs/clearml_conf/#files-section) \- Define auto-generated files to apply into local file system

See an [example configuration file](https://github.com/clearml/clearml-agent/blob/master/docs/clearml.conf)
in the ClearML Agent GitHub repository.

note

The values in the ClearML configuration file can be overridden by environment variables, the [configuration vault](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_profile#configuration-vault),
and command-line arguments.

## Editing Your Configuration File [​](https://clear.ml/docs/latest/docs/configs/clearml_conf/\#editing-your-configuration-file "Direct link to Editing Your Configuration File")

To add, change, or delete options, edit your configuration file.

**To edit your ClearML configuration file:**

1. Open the configuration file for editing, depending upon your operating system:
   - Linux - `~/clearml.conf`
   - Mac - `$HOME/clearml.conf`
   - Windows - `\User\<username>\clearml.conf`
2. In the required section (sections listed on this page), add, modify, or remove required options.

3. Save configuration file.


## Environment Variables [​](https://clear.ml/docs/latest/docs/configs/clearml_conf/\#environment-variables "Direct link to Environment Variables")

ClearML's configuration file uses [HOCON](https://github.com/lightbend/config/blob/main/HOCON.md) configuration format,
which supports environment variable reference.

For example:

```editorconfig
sdk {

   google.storage {

          # # Default project and credentials file

          # # Will be used when no bucket configuration is found

          project: "clearml"

          credentials_json: ${GOOGLE_APPLICATION_CREDENTIALS}

  }

}
```

`${GOOGLE_APPLICATION_CREDENTIALS}` will automatically be substituted by the environment variable value.

See [Note on Windows](https://github.com/lightbend/config/blob/main/HOCON.md#note-on-windows-and-case-sensitivity-of-environment-variables)
for information about using environment variables with Windows in the configuration file.

## Configuration File Sections [​](https://clear.ml/docs/latest/docs/configs/clearml_conf/\#configuration-file-sections "Direct link to Configuration File Sections")

### agent section [​](https://clear.ml/docs/latest/docs/configs/clearml_conf/\#agent-section "Direct link to agent section")

**`agent`** ( _dict_)

- Dictionary of top-level ClearML Agent options to configure ClearML Agent for Git credentials, package managers, cache management, workers, and Docker for workers.

* * *

**`agent.crash_on_exception`** ( _bool_)

- By default, when encountering an exception while running a task, the agent will catch the exception, log it, and
continue running. When set to `true`, the agent crashes when encountering an exception.

* * *

**`agent.cuda_version`** ( _float_)

- The CUDA version to use.


  - If specified, this is the CUDA version used.
  - If not specified, the CUDA version is automatically detected.

Alternatively, override this option with the environment variable `CUDA_VERSION`.

* * *

**`agent.cudnn_version`** ( _float_)

- The cuDNN version to use.


  - If specified, this is the cuDNN version used.
  - If not specified, the cuDNN version is automatically detected.

Alternatively, override this option with the environment variable `CUDNN_VERSION`.

* * *

**`agent.disable_ssh_mount`** ( _bool_)

- Set to `true` to disable the auto `.ssh` mount into the docker. The environment variable `CLEARML_AGENT_DISABLE_SSH_MOUNT`
overrides this configuration option.

* * *

**`agent.disable_task_docker_override`** ( _bool_)

- If set to `true`, agent uses the default docker image and ignores any docker image and arguments specified in the
task's container section (if setup shell script is specified in task container section, it is used
in either case).

* * *

**`agent.docker_allow_host_environ`** ( _bool_)

- Set to `true` to allow passing host environments into docker container with Task's docker container arguments. For example: `"-e HOST_NAME=$HOST_NAME"`.

warning

Use with care! This might introduce security risks by allowing access to keys/secret on the host machine.

* * *

**`agent.docker_apt_cache`** ( _string_)

- The apt (Linux package tool) cache folder for mapping Ubuntu package caching into Docker.

* * *

**`agent.docker_args_extra_precedes_task`** ( _bool_)

- Allow the arguments specified in `agent.extra_docker_arguments` to override task level docker arguments, in the case that
the same argument is passed in both. If set to `False`, a task's docker arguments will override the `extra_docker_arguments`.

* * *

**`agent.docker_args_filters`** ( _list_)

- Set a whitelist of allowed Docker arguments. Only arguments matching the specified patterns can be used when running
a task. For example: `docker_args_filters: ["^--env$", "^-e$"]`.

* * *

**`agent.docker_container_name_format`** ( _string_)

Compatibility Required

Compatible with Docker versions 0.6.5 and above

- Set a name format for Docker containers created by an agent running in [Docker mode](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_execution_env#docker-mode)

- The following variables can be used:
  - `task_id`
  - `worker_id`
  - `rand_string` \- random lower-case letters string (up to 32 characters)
- The resulting name must start with an alphanumeric character, while the rest of the name may contain alphanumeric characters,
underscores (`_`), dots (`.`) and/or dashes (`-`)

- For example: `clearml-id-{task_id}-{rand_string:.8}`


* * *

**`agent.docker_force_pull`** ( _bool_)

- Always update the Docker image by forcing a Docker `pull` before running a task

The values are:
  - `true` \- Always update the Docker image.
  - `false` \- Do not always update.

* * *

**`agent.docker_install_opencv_libs`** ( _bool_)

- Install the required packages for opencv libraries (`libsm6 libxext6 libxrender-dev libglib2.0-0`), for backwards
compatibility reasons. Change to `false` to skip installation and decrease docker spin-up time.

* * *

**`agent.docker_internal_mounts`** ( _dict_)

- Set internal mount points inside the Docker. This is especially useful for non-root Docker container images.

For example:

```text
docker_internal_mounts {

     sdk_cache: "/clearml_agent_cache"

     apt_cache: "/var/cache/apt/archives"

     ssh_folder: "/root/.ssh"

     pip_cache: "/root/.cache/pip"

     poetry_cache: "/root/.cache/pypoetry"

     vcs_cache: "/root/.clearml/vcs-cache"

     venvs_cache: "/root/.clearml/venvs-cache"

     venv_build: "/root/.clearml/venvs-builds"

     pip_download: "/root/.clearml/pip-download-cache"

}
```

* * *

**`agent.docker_pip_cache`** ( _string_)

- The pip (Python package tool) cache folder for mapping Python package caching into Docker.

* * *

**`agent.docker_use_activated_venv`** ( _bool_)

- In [Docker mode](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_execution_env#docker-mode), if the container's entrypoint automatically activates a virtual environment, the activated virtual
environment is used and everything is installed in it. Set to `false` to disable, and always create a new venv inheriting
from `system_site_packages`

* * *

**`agent.enable_git_ask_pass`** ( _bool_)

note

`enable_git_ask_pass` is supported only on Linux systems.

- If enabled, uses `GIT_ASKPASS` to pass Git user/pass when cloning/fetching repositories
- It solves passing user/token to git submodules.
- This is a safer way to ensure multiple users using the same repository will not accidentally leak credentials

* * *

**`agent.enable_task_env`** ( _bool_)

- Set the OS environments based on the Task's Environment section before launching the Task process.

* * *

**`agent.extra_docker_arguments`** ( _\[string\]_)

- Optional arguments to pass to the Docker image when ClearML Agent is running in [Docker mode](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_execution_env#docker-mode). These are local for this agent, and will not be updated in the task's `docker_cmd` section. For example, `["--ipc=host", ]`.

* * *

**`agent.extra_docker_shell_script`** ( _\[string\]_)

- When ClearML Agent is running in [Docker mode](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_execution_env#docker-mode), this
optional shell script executes inside the Docker on startup, before the task starts. For example, `["apt-get install -y bindfs", ]`.

* * *

**`agent.force_git_root_python_path`** ( _bool_)

- Force the root folder of the git repository (instead of the working directory) into the `PYTHONPATH` environment variable.
`false` by default, so only the working directory will be added to `PYTHONPATH`

* * *

**`agent.force_git_ssh_protocol`** ( _bool_)

- Force Git protocol to use SSH regardless of the Git URL. This assumes the Git user/pass are blank.

The values are:
  - `true` \- Force
  - `false` \- Do not force

* * *

**`agent.force_git_ssh_port`** ( _integer_)

- Force a specific SSH port when converting HTTP to SSH links. The domain remains unchanged.

* * *

**`agent.force_git_ssh_user`** ( _string_)

- Force a specific SSH username when converting HTTP to SSH links (the default username is 'git')

* * *

**`agent.git_host`** ( _string_)

- Limit Git credentials usage to this host. The environment variable `CLEARML_AGENT_GIT_HOST` overrides this configuration option.

* * *

**`agent.git_pass`** ( _string_)

- Git repository password.
  - If using Git SSH credentials, do not specify this option.
  - If not using Git SSH credentials, use this option to specify a Git password for cloning your repositories.

* * *

**`agent.git_user`** ( _string_)

- Git repository username.
  - If using Git SSH credentials, do not specify this option.
  - If not using Git SSH credentials, use this option to specify a Git password for cloning your repositories.

* * *

**`agent.git_use_ms_entra_token`** ( _bool_)

- Enable authentication to Azure DevOps repositories using Microsoft Entra tokens.
  - Set to `true` to authenticate using a Microsoft Entra OAuth token.
  - `agent.git_use_ms_entra_token` and `agent.git_use_azure_pat` are mutually exclusive. Only one can be set to `true` at a time.
  - The token is retrieved from the configured Git password (set via `agent.git_pass` or the `CLEARML_AGENT_GIT_PASS` environment variable).
  - For more information, see the [Azure DevOps authentication guide](https://learn.microsoft.com/en-us/azure/devops/repos/git/auth-overview?view=azure-devops&tabs=Linux#microsoft-entra-oauth-tokens-recommended).

* * *

**`agent.git_use_azure_pat`** ( _bool_)

- Enable authentication to Azure DevOps repositories using a Personal Access Token (PAT).
  - Set to `true` to authenticate using an Azure DevOps PAT.
  - `agent.git_use_ms_entra_token` and `agent.git_use_azure_pat` are mutually exclusive. Only one can be set to `true` at a time.
  - The PAT is retrieved from the configured Git password (set via `agent.git_pass` or the `CLEARML_AGENT_GIT_PASS` environment variable).
  - For more information, see the [Azure DevOps authentication guide](https://learn.microsoft.com/en-us/azure/devops/repos/git/auth-overview?view=azure-devops&tabs=Linux#personal-access-tokens-alternative-option).

* * *

**`agent.hide_docker_command_env_vars`** ( _dict_)

- Hide Docker environment variables containing secrets when printing out the Docker command. When printed, the variable
values will be replaced by `********`

- Enable this feature by setting `enabled` to `true`. Doing this will hide the following environment variables values:
  - `CLEARML_API_SECRET_KEY`
  - `CLEARML_AGENT_GIT_PASS`
  - `AWS_SECRET_ACCESS_KEY`
  - `AZURE_STORAGE_KEY`
- To mask additional environment variables, add their keys to the `extra_keys` list.
For example, to hide the value of a custom environment variable named `MY_SPECIAL_PASSWORD`, set `extra_keys: ["MY_SPECIAL_PASSWORD"]`

- By default, `parse_embedded_urls` is set to `true`, so agent will also hide passwords in URLs and handle environment variables
containing docker commands


```text
hide_docker_command_env_vars {

  enabled: true

  extra_keys: ["MY_SPECIAL_PASSWORD"]

  parse_embedded_urls: true

}
```

* * *

**`agent.ignore_requested_python_version`** ( _bool_)

- Indicates whether to ignore any requested Python version

- The values are:
  - `true` \- ignore any requested Python version
  - `false` \- if a task was using a specific Python version, and the system supports multiple versions, the agent will
    use the requested Python version (default)

* * *

**`agent.protected_docker_extra_args`** ( _\[string\]_)

- Prevent listed task docker arguments from being used if they are already specified in `agent.extra_docker_arguments`.

* * *

**`agent.python_binary`** ( _string_)

- Set the Python version to use when creating the virtual environment, and when launching the task. For example, `/usr/bin/python3` or `/usr/local/bin/python3.6`.

* * *

**`agent.reload_config`** ( _bool_)

- Indicates whether to reload the configuration each time the worker daemon is executed.

* * *

**`agent.translate_ssh`** ( _bool_)

- Translate HTTPS communication to SSH

* * *

**`agent.venvs_dir`** ( _string_)

- The target folder for virtual environments builds that are created when executing a task.

* * *

**`agent.worker_id`** ( _string_)

- When creating a worker, assign the worker an ID.
  - If specified, a unique name for the worker. For example, `clearml-agent-machine1:gpu0`.

  - If not specified, the following is used: `<hostname>:<process_id>`.

    For example, `MyHost:12345`.

    Alternatively, specify the environment variable `CLEARML_WORKER_ID` to override this worker name.

* * *

**`agent.worker_name`** ( _string_)

- Use to replace the hostname when creating a worker if `agent.worker_id` is not specified. For example, if `worker_name`
is `MyMachine` and the `process_id` is `12345`, then the worker is named `MyMachine.12345`.

Alternatively, specify the environment variable `CLEARML_WORKER_NAME` to override this worker name.


#### agent.default\_docker [​](https://clear.ml/docs/latest/docs/configs/clearml_conf/\#agentdefault_docker "Direct link to agent.default_docker")

**`agent.default_docker`** ( _dict_)

- Dictionary containing the default options for workers running in [Docker mode](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_execution_env#docker-mode).
These settings define which Docker image and arguments should be used unless [explicitly overridden through the UI or an agent](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_execution_env#docker-mode).

  - **`agent.default_docker.image`** ( _str_) \- Specifies the default Docker image to use.

  - **`agent.default_docker.arguments`** (\[ _str_\]) \- Specifies the list of options to pass to the Docker container. For
    example: `arguments: ["--ipc=host", ]`.

  - **`agent.default_docker.match_rules`** ( _\[dict\]_)



    Enterprise Feature





    The `match_rules` configuration option is available under the ClearML Enterprise plan.






    - Lookup table of rules that determine the default container and arguments when running a worker in Docker mode. The
      first matched rule will be picked, according to rule order.
    - Each dictionary in the list lays out rules, and the container and container arguments to be used if the rules are
      matched.

Match rule arguments

`default_docker.match_rules.arguments` should be formatted as a single string (for example: `"-e VALUE=1 --ipc=host"`),
unlike `agent.default_docker.arguments`

note

`match_rules` are ignore if `--docker <container>` is passed in the command line.

    - The rules can be:
      - `script.requirements` \- Match all script requirements
      - `script.repostiry`, `script.branch` \- Match based on Git repository or branch where the script is stored
      - `script.binary` \- Match binary executable used to launch the entry point
      - `project` \- Match the Task project's name
    - Matching is done via regular expression. For example `"^searchme$"` will match exactly the `"searchme"` string, and `^examples`
      will match that starts with `examples` (e.g., `examples`, `examples/sub_project`).
    - Examples:
      - In the example configuration below, the rules match tasks where the Python binary is `python3.6`, `tensorflow~=2.6`
        is required, the script's Git repository is `/my_repository/`, the branch is `main`, and the task's project is
        `project/sub_project`. If all conditions are met, the `nvidia/cuda:10.1-cudnn7-runtime-ubuntu18.04` image is used
        with the argument `-e define=value`.





        ```text
        agent {

          default_docker {

            match_rules [\
\
              {\
\
                image: "nvidia/cuda:10.1-cudnn7-runtime-ubuntu18.04"\
\
                arguments: "-e define=value"\
\
                match: {\
\
                  script {\
\
                    # Optional: must match all requirements (not partial)\
\
                    requirements: {\
\
                      # version selection matching PEP-440\
\
                      pip: {\
\
                        tensorflow: "~=2.6"\
\
                      },\
\
                    }\
\
                    # Optional: matching based on regular expression, example: "^exact_match$"\
\
                    repository: "/my_repository/"\
\
                    branch: "main"\
\
                    binary: "python3.6"\
\
                  }\
\
                  # Optional: matching based on regular expression, example: "^exact_match$"\
\
                  project: "project/sub_project"\
\
                }\
\
              }\
\
            ]

          }

        }
        ```

      - In the example configuration below, two `match_rules` are used to specify different Docker images based on
        the Python binary version. The first rule applies the `python:3.6-bullseye` image with the `--ipc=host` argument
        when the task requires `python3.6`. The second rule applies the `python:3.7-bullseye` image with the same argument
        when the script requires `python3.7`. If no match is found, the default `nvidia/cuda:11.0.3-cudnn8-runtime-ubuntu20.04`
        image is used.





        ````text
        ```

        agent {

        default_docker: {

            image: "nvidia/cuda:11.0.3-cudnn8-runtime-ubuntu20.04",

            match_rules: [\
\
              {\
\
                image: "python:3.6-bullseye"\
\
                arguments": "--ipc=host"\
\
                match: {\
\
                  script {\
\
                    binary: "python3.6$"\
\
                  },\
\
                }\
\
              },\
\
              {\
\
                image: "python:3.7-bullseye"\
\
                arguments: "--ipc=host"\
\
                match: {\
\
                  script {\
\
                    binary: "python3.7$"\
\
                  },\
\
                }\
\
              },\
\
            ]

        }

        }

        ```
        ````

#### agent.package\_manager [​](https://clear.ml/docs/latest/docs/configs/clearml_conf/\#agentpackage_manager "Direct link to agent.package_manager")

**`agent.package_manager`** ( _dict_)

- Dictionary containing the options for the Python package manager.
- The currently supported package managers are
  - pip
  - conda
  - uv, if the root repository contains a `uv.lock` or `pyproject.toml` file
  - poetry, if the repository contains a `poetry.lock` or `pyproject.toml` file

* * *

**`agent.package_manager.conda_channels`** ( _\[string\]_)

- If conda is used, then this is the list of conda channels to use when installing Python packages.

* * *

**`agent.package_manager.conda_full_env_update`** ( _bool_)

- Enables update of conda environment (Conda environment does not update by default as it might break)

* * *

**`agent.package_manager.conda_env_as_base_docker`** ( _bool_)

- Uses conda environment for execution (like a docker)

* * *

**`agent.package_manager.use_conda_base_env`** ( _bool_)

- When set to `True`, installation will be performed into the base Conda environment. Use in [Docker mode](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_execution_env#docker-mode).

* * *

**`agent.package_manager.extra_index_url`** ( _\[string\]_)

- A list of URLs for additional artifact repositories when installing Python packages.

* * *

**`agent.package_manager.extra_pip_install_flags`** ( _\[string\]_)

- A list of additional flags to use when the agent install packages. For example: `["--use-deprecated=legacy-resolver", ]`

* * *

**`agent.package_manager.force_upgrade`** ( _bool_)

- Indicates whether to force an upgrade of Python packages.

The values are:
  - `true` \- Force
  - `false` \- Do not force

* * *

**`agent.package_manager.pip_version`** ( _string_)

- The `pip` version to use. For example, `"<20"`, `"==19.3.1"`, `""` (empty string will install the latest version).

* * *

**`agent.package_manager.poetry_version`** ( _string_)

- The `poetry` version to use. For example, `"<2"`, `"==1.1.1"`, `""` (empty string will install the latest version).

* * *

**`agent.package_manager.poetry_install_extra_args`** ( _list_)

- List extra command-line arguments to pass when using `poetry`

* * *

**`agent.package_manager.post_optional_packages`** ( _string_)

- A list of optional packages that will be installed after the required packages. If the installation of an optional post
package fails, the package is ignored, and the virtual environment process continues.

* * *

**`agent.package_manager.post_packages`** ( _\[string\]_)

- A list of packages that will be installed after the required packages.

* * *

**`agent.package_manager.priority_optional_packages`** ( _\[string\]_)

- A list of optional priority packages to be installed before the rest of the required packages, but in case a
package installation fails, the package will be ignored, and the virtual environment process will continue.

* * *

**`agent.package_manager.priority_packages`** ( _\[string\]_)

- A list of packages with priority to be installed before the rest of the required packages. For example: `["cython", "numpy", "setuptools", ]`

* * *

**`agent.package_manager.pytorch_resolve`** ( _str_)

- Set the PyTorch resolving mode. The options are:
  - `pip` (default) - Sets extra index based on cuda and lets pip resolve
  - `none` \- No resolving. Install PyTorch like any other package
  - `direct` \- Resolve a direct link to the PyTorch wheel by parsing the pytorch.org pip repository and matching the
    automatically detected cuda version with the required PyTorch wheel. If the exact cuda version is not found for the
    required PyTorch wheel, it will try a lower cuda version until a match is found

* * *

**`agent.package_manager.system_site_packages`** ( _bool_)

- Indicates whether Python packages for virtual environments are inherited from the system when building a virtual environment
for a task.

The values are:
  - `true` \- Inherit
  - `false` \- Do not inherit (load Python packages)

* * *

**`agent.package_manager.torch_nightly`** ( _bool_)

- Indicates whether to support installing PyTorch Nightly builds.

The values are:
  - `true` \- If a stable `torch` wheel is not found, install the nightly build.
  - `false` \- Do not install.

note

Torch Nightly builds are ephemeral and are deleted from time to time.

* * *

**`agent.package_manager.type`** ( _string_)

- Indicates the type of Python package manager to use.

The values are:
  - `pip`
  - `conda`
  - `poetry`
  - `uv`
- If `pip` or `conda` are used, the agent installs the required packages based on the "Python Packages" section of the
Task. If the "Python Packages" section is empty, it will revert to using `requirements.txt` from the repository's root
directory.

- If `poetry` is selected, and the root repository contains `poetry.lock` or `pyproject.toml`, the "Python
Packages" section is ignored, and `poetry` is used. If `poetry` is selected and no lock file is found, it reverts to
`pip` package manager behaviour.

- If `uv` is selected, and the root repository contains `uv.lock` or `pyproject.toml`, the "Python
Packages" section is ignored, and `uv` is used. If `uv` is selected and no lock file is found, it reverts to
`pip` package manager behaviour.


* * *

**`agent.package_manager.uv_files_from_repo_working_dir`** ( _bool_)

- If set to `true`, the agent will look for the `uv.lock` or `pyproject.toml` file in the provided directory path instead of
the repository's root directory.

* * *

**`agent.package_manager.uv_sync_extra_args`** ( _list_)

- List extra command-line arguments to pass when using `uv`.

* * *

**`agent.package_manager.uv_sync_locked_if_lock_file`** ( _bool_)

- If `True` (default), passes `--locked` to `uv sync` when a lockfile exists in the repository.

* * *

**`agent.package_manager.uv_version`** ( _string_)

- The `uv` version requirements. For example, `">0.4"`, `"==0.4"`, `""` (empty string will install the latest version).

#### agent.pip\_download\_cache [​](https://clear.ml/docs/latest/docs/configs/clearml_conf/\#agentpip_download_cache "Direct link to agent.pip_download_cache")

**`agent.pip_download_cache`** ( _dict_)

- Dictionary containing pip download cache options.

* * *

**`agent.pip_download_cache.enabled`** ( _bool_)

- Indicates whether to use a specific cache folder for Python package downloads.

The values are:
  - `true` \- Use a specific folder which is specified in the option `agent.pip_download_cache.path`
  - `false` \- Do not use a specific folder.

* * *

**`agent.pip_download_cache.path`** ( _string_)

- If `agent.pip_download_cache.enabled` is `true`, then this specifies the cache folder.

#### agent.vcs\_cache [​](https://clear.ml/docs/latest/docs/configs/clearml_conf/\#agentvcs_cache "Direct link to agent.vcs_cache")

**`agent.vcs_cache`** ( _dict_)

- Dictionary containing version control system clone cache folder.

* * *

**`agent.vcs_cache.enabled`** ( _bool_)

- Indicates whether the version control system cache is used.

The values are:
  - `true` \- Use cache
  - `false` \- Do not use cache

* * *

**`agent.vcs_cache.path`** ( _string_)

- The version control system cache clone folder when executing tasks.

#### agent.venvs\_cache [​](https://clear.ml/docs/latest/docs/configs/clearml_conf/\#agentvenvs_cache "Direct link to agent.venvs_cache")

**`agent.venvs_cache`** ( _dict_)

- Dictionary containing virtual environment cache options.

* * *

**`agent.venvs_cache.free_space_threshold_gb`** ( _integer_)

- Minimum required free space to allow for cache entry.
- Disable minimum by passing 0 or negative value.

* * *

**`agent.venvs_cache.max_entries`** ( _integer_)

- Maximum number of cached virtual environments.

* * *

**`agent.venvs_cache.path`** ( _string_)

- Folder of the virtual environment cache.
- Uncomment to enable virtual environment caching.

#### agent.venv\_update [​](https://clear.ml/docs/latest/docs/configs/clearml_conf/\#agentvenv_update "Direct link to agent.venv_update")

note

This option is deprecated. Use `venvs_cache` and set `venvs_cache.path` instead.

**`agent.venv_update`** ( _dict_)

- Dictionary containing virtual environment update options.

* * *

**`agent.venv_update.enabled`** ( _bool_)

- Indicates whether to use accelerated Python virtual environment building (this is a beta feature).

The values are:
  - `true` \- Accelerate
  - `false` \- Do not accelerate (default value)

### api section [​](https://clear.ml/docs/latest/docs/configs/clearml_conf/\#api-section "Direct link to api section")

**`api`** ( _dict_)

Dictionary of configuration options for the ClearML Server API, web, and file servers and credentials.

* * *

**`api.api_server`** ( _string_)

- The URL of your ClearML API server. For example, `https://api.MyDomain.com`.

* * *

**`api.web_server`** ( _string_)

- The URL of your ClearML web server. For example, `https://app.MyDomain.com`.

* * *

**`api.files_server`** ( _string_)

- The URL of your ClearML file server. For example, `https://files.MyDomain.com`.

warning

You must use a secure protocol with `api.web_server`, `api.files_server`, and `api.api_server`. Use `https`, not `http`.

* * *

**`api.http.default_method`** ( _string_)

- Set the request method for all API requests and auth login. This can be useful when `GET` requests with payloads are
blocked by a server, and `POST` requests can be used instead. The request options are: "GET", "POST", "PUT".

warning

This configuration option is experimental, and has not been vigorously tested, so it may have unintended consequences.

#### api.credentials [​](https://clear.ml/docs/latest/docs/configs/clearml_conf/\#apicredentials "Direct link to api.credentials")

**`api.credentials`** ( _dict_)

- Dictionary of API credentials.
Alternatively, specify the environment variable `CLEARML_API_ACCESS_KEY` / `CLEARML_API_SECRET_KEY` to override these keys.


* * *

**`api.credentials.access_key`** ( _string_)

- Your ClearML access key.

* * *

**`api.credentials.secret_key`** ( _string_)

- Your ClearML credentials.

* * *

**`api.verify_certificate`** ( _bool_)

- Indicates whether to verify the host SSL certificate.

The values are:
  - `true` \- Verify
  - `false` \- Do not verify.
  - `path/to/certificate` \- The certificate file to use for verification.

warning

Set to False only if required.

### sdk section [​](https://clear.ml/docs/latest/docs/configs/clearml_conf/\#sdk-section "Direct link to sdk section")

**`sdk`** ( _dict_)

- Dictionary that contains configuration options for the ClearML Python Package and related options, including storage,
metrics, network, AWS S3 buckets and credentials, Google Cloud Storage, Azure Storage, log, and development.

#### sdk.aws [​](https://clear.ml/docs/latest/docs/configs/clearml_conf/\#sdkaws "Direct link to sdk.aws")

**`sdk.aws`** ( _dict_)

- Dictionary with AWS storage options. Parameters include:
  - **`sdk.aws.boto3`** ( _dict_) \- Boto3-specific AWS storage options:
    - `max_multipart_concurrency` ( _integer_) \- Maximum number of threads making requests for a transfer.
    - `multipart_threshold` ( _integer_) \- Transfer size threshold (in bytes). For transfers above this threshold,
      Boto3 will automatically use multipart uploads/downloads/copies.
    - `multipart_chunksize` ( _integer_) \- Size of each part in a multipart transfer (in bytes).
    - `pool_connections` ( _integer_) \- Maximum number of Boto3 pool connections.
    - `connect_timeout` ( _float_ or _integer_) \- Time till a timeout exception is thrown when attempting to make a
      connection (in seconds). Default is 60 seconds.
    - `signature_version` ( _string_) \- AWS Signature version to use when signing requests.
    - `read_timeout` ( _float_ / _integer_) \- Time till a timeout exception is thrown when attempting to read from a
      connection (in seconds). The default is 60 seconds.
    - `s3` ( _dict_) \- Additional S3-specific configuration passed to Boto3 client. Configuration options include:

      - `addressing_style` ( _string_) \- Override the S3 URL addressing style. Options are: "auto", "virtual", "path".
      - `payload_signing_enabled` ( _bool_) \- Specifies whether to compute and send a checksum with every request.
      - For more information and configuration options, see the [Boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html).
  - **`sdk.aws.s3`** ( _dict_) \- AWS S3 options:
    - `credentials` ( _\[dict\]_) \- List of dictionaries specifying credentials for individual S3 buckets or hosts.See more information [below](https://clear.ml/docs/latest/docs/configs/clearml_conf/#sdkawss3credentials).
    - `key` ( _string_) \- Default access key for buckets not specified in `sdk.aws.s3.credentials`.
    - `secret` ( _string_) \- Default secret access key for buckets not specified in `sdk.aws.s3.credentials`.
    - `profile` ( _string_) \- Default AWS profile for buckets not specified in `sdk.aws.s3.credentials`.
    - `region` ( _string_) \- Default region for buckets not specified in `sdk.aws.s3.credentials`.
    - `extra_args` ( _dict_) \- Additional [ExtraArgs](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-uploading-files.html#the-extraargs-parameter)
      passed to Boto3 when uploading files. Can be set per bucket under `sdk.aws.s3.credentials`.
    - `use_credentials_chain` ( _bool_) \- Set to `true` to let Boto3 automatically locate credentials via environment
      variables, credential files, or IAM role metadata instead of using explicit parameters (key and secret). See [Boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html#configuring-credentials).

##### sdk.aws.s3.credentials [​](https://clear.ml/docs/latest/docs/configs/clearml_conf/\#sdkawss3credentials "Direct link to sdk.aws.s3.credentials")

**`sdk.aws.s3.credentials`** ( _\[dict\]_)

- List of dictionaries containing credentials for individual S3 buckets or hosts for individual buckets. Each dictionary
can override the default credentials for a specific bucket or host. Each dictionary can contain the following options:
  - `bucket` ( _string_) \- Bucket name. See the [AWS documentation](https://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html) for bucket naming restrictions.
  - `host` ( _string_) \- Optional host URL (and optionally port). When set, these credentials apply to any bucket on the host
  - `key` ( _string_):

    - If `bucket` is specified, the key applies only to that bucket.
    - If `host` is specified, the key applies to all buckets on that host.
  - `secret` ( _bool_):

    - If `bucket` is specified, the secret applies only to that bucket.
    - If `host` is specified, the secret applies to all buckets on that host.
  - `multipart` ( _bool_) \- Whether to enable multipart uploads.

    - `true` \- Enabled
    - `false` \- Disabled
  - `secure` ( _string_) \- Whether the host is secure.

    - `true` \- Secure
    - `false` \- Not secure
  - `verify` ( _string_ / _bool_) \- Whether to verify SSL certificates:

    - `true` (default) - Verify
    - `false` \- Skip SSL verification
    - Provide a path/URL to a CA bundle.
- Other keys from `sdk.aws.s3` such as `region`, `profile`, and `extra_args` are also available per bucket/host and behave
the same as the defaults under `sdk.aws.s3`.


#### sdk.azure.storage [​](https://clear.ml/docs/latest/docs/configs/clearml_conf/\#sdkazurestorage "Direct link to sdk.azure.storage")

**`sdk.azure.storage.containers`** ( _\[dict\]_)

- List of dictionaries, each dictionary contains credentials for an Azure Storage container.

* * *

**`sdk.azure.storage.containers.account_key`** ( _string_)

- For Azure Storage, this is the credentials key.

* * *

**`sdk.azure.storage.containers.account_name`** ( _string_)

- For Azure Storage, this is the account name.

* * *

**`sdk.azure.storage.containers.container_name`** ( _string_)

- For Azure Storage, this is the container name.

#### sdk.dataset [​](https://clear.ml/docs/latest/docs/configs/clearml_conf/\#sdkdataset "Direct link to sdk.dataset")

**`sdk.dataset.preview`** ( _\[dict\]_)

- Set limits for the objects that are logged as dataset previews:
  - **`sdk.dataset.preview.media`** ( _dict_) \- Set limits for media files that are logged as dataset previews. Available
    options:

    - **`sdk.dataset.preview.media.max_file_size`** ( _int_) \- Maximum file size in bytes of a preview object (e.g. image,
      video, html, etc.). Files exceeding this size will not be reported as previews.
    - **`sdk.dataset.preview.media.image_count`** ( _int_) \- The maximum number of image files reported as previews
    - **`sdk.dataset.preview.media.video_count`** ( _int_) \- The maximum number of video files reported as previews
    - **`sdk.dataset.preview.media.audio_count`** ( _int_) \- The maximum number of image files reported as previews
    - **`sdk.dataset.preview.media.html_count`** ( _int_) \- The maximum number of html files reported as previews
    - **`sdk.dataset.preview.media.json_count`** ( _int_) \- The maximum number of json files reported as previews
  - **`sdk.dataset.preview.tabular`** ( _dict_) \- Set limits for tabular files that are logged as dataset previews. Available
    options:

    - **`sdk.dataset.preview.tabular.row_count`** ( _int_) \- The maximum number of rows for each tabular file reported as a preview. By default, it will report only the first 10 rows from a file
    - **`sdk.dataset.preview.tabular.table_count`** ( _int_) \- The maximum number of tables reported as preview in a dataset

#### sdk.development [​](https://clear.ml/docs/latest/docs/configs/clearml_conf/\#sdkdevelopment "Direct link to sdk.development")

**`sdk.development`** ( _dict_)

- Dictionary of development mode options.

* * *

**`sdk.development.artifacts`** ( _dict_)

- Control default behavior when logging task artifacts:
  - **`sdk.development.artifacts.default_pandas_dataframe_extension_name`** ( _str_)

    - Set the default `extension_name` for pandas `DataFrame` objects
    - Valid values are: `.csv.gz`, `.parquet`, `.feather`, `.pickle`
    - This value can be overridden by the `extension_name` argument supplied to `Task.upload_artifact()`
  - **`sdk.development.artifacts.auto_pickle`** ( _bool_)

    - If `true` and the artifact is not of a specific type (`pathlib2.Path`, `dict`, `pandas.DataFrame`, `numpy.ndarray`,
      `PIL.Image`, url string, `local_file` string), the artifact will be
      pickled and uploaded as a pickle file artifact (with the `.pkl` file extension).
    - If `false`, the auto-pickle behavior is disabled in the artifact upload
    - This value can be overridden by the `auto_pickle` argument supplied to `Task.upload_artifact()`

* * *

**`sdk.development.default_output_uri`** ( _string_)

- The default output destination for model checkpoints (snapshots) and artifacts. If the `output_uri` parameter is not provided
when calling [`Task.init()`](https://clear.ml/docs/latest/docs/references/sdk/task#taskinit), then use the destination in `default_output_uri`.

* * *

**`sdk.development.detailed_import_report`** ( _bool_)

- If `true` (default is `false`), provide a detailed report of all Python package imports as comments inside the "Python Packages" section.

* * *

**`sdk.development.detect_with_conda_freeze`** ( _bool_)

- If `true` (default is `false`), instead of analyzing the code with Pigar, analyze with `conda freeze`

* * *

**`sdk.development.detect_with_pip_freeze`** ( _bool_)

- If `true` (default is `false`), instead of analyzing the code with Pigar, analyze with `pip freeze`

* * *

**`sdk.development.default_shell_binary`** ( _str_)

- Path to the executable binary [`Task.create()`](https://clear.ml/docs/latest/docs/references/sdk/task#taskcreate) will use as the default value
for the new task’s `script.binary`,

* * *

**`sdk.development.force_analyze_entire_repo`** ( _bool_)

- Default auto-generated requirements optimize for smaller requirements.
- The values are:
  - `true` \- Analyze the entire repository regardless of the entry point.
  - `false`\- First analyze the entry point script, if it does not contain other local files, do not analyze the entire repository.

* * *

**`sdk.development.log_os_environments`** ( _\[string\]_)

- Log specific environment variables. OS environments are listed in the UI, under a task's

**CONFIGURATION > HYPERPARAMETERS > Environment** section.
Multiple selected variables are supported including the suffix `*`. For example: `"AWS_*"` will log any OS environment
variable starting with `"AWS_"`. Example: `log_os_environments: ["AWS_*", "CUDA_VERSION"]`

- This value can be overwritten with OS environment variable `CLEARML_LOG_ENVIRONMENT=AWS_*,CUDA_VERSION`.


* * *

**`sdk.development.store_uncommitted_code_diff`** ( _bool_)

- For development mode, indicates whether to store the uncommitted `git diff` or `hg diff` in the task manifest.

The values are:
  - `true` \- Store the `diff` in the `script.requirements.diff` section
  - `false` \- Do not store the diff.

* * *

**`sdk.development.suppress_update_message`** ( _bool_)

- If `true` (default `false`), _clearml_ update messages will not be printed to the console.

- This value can be overwritten with OS environment variable `CLEARML_SUPPRESS_UPDATE_MESSAGE=1`


* * *

**`sdk.development.support_stopping`** ( _bool_)

- For development mode, indicates whether to allow stopping a task if the task was aborted externally, its status was changed, or it was reset.

The values are:
  - `true` \- Allow
  - `false` \- Do not allow

* * *

**`sdk.development.task_reuse_time_window_in_hours`** ( _float_)

- For development mode, the number of hours after which a task with the same project name and task name is reused.

* * *

**`sdk.development.vcs_repo_detect_async`** ( _bool_)

- For development mode, indicates whether to run version control repository detection asynchronously.

The values are:
  - `true` \- Run asynchronously
  - `false` \- Do not run asynchronously

##### sdk.development.worker [​](https://clear.ml/docs/latest/docs/configs/clearml_conf/\#sdkdevelopmentworker "Direct link to sdk.development.worker")

**`sdk.development.worker`** ( _dict_)

- Dictionary of development mode options for workers.

* * *

**`sdk.development.worker.log_stdout`** ( _bool_)

- For development mode workers, indicates whether all stdout and stderr messages are logged.

The values are:
  - `true` \- Log all
  - `false` \- Do not log all

* * *

**`sdk.development.worker.max_wait_for_first_iteration_to_start_sec`** ( _integer_)

- Maximum time (in seconds) for allowing the resource monitoring to switch back to reporting iterations as the x-axis
after initially starting to report "seconds from start." If the specified time limit is exceeded, the resource monitoring
will continue reporting using "seconds from start" as the x-axis.

* * *

**`sdk.development.worker.ping_period_sec`** ( _integer_)

- For development mode workers, the interval in seconds for a worker to ping the server testing connectivity.

* * *

**`sdk.development.worker.report_event_flush_threshold`** ( _integer_)

- The number of events that trigger a report

* * *

**`sdk.development.worker.report_global_mem_used`** ( _bool_)

- Compatibility feature to report memory usage for the entire machine

The values are:
  - `true` \- Report memory usage for the entire machine
  - `false` (default) - Report memory usage only on the running process and its sub-processes

* * *

**`sdk.development.worker.report_period_sec`** ( _integer_)

- For development mode workers, the interval in seconds for a development mode ClearML worker to report.

* * *

**`sdk.development.worker.report_start_sec`** ( _integer_)

- The number of seconds after which the development mode worker starts resource reporting.

* * *

**`sdk.development.worker.wait_for_first_iteration_to_start_sec`** ( _integer_)

- Controls how long (in seconds) to wait for iteration reporting to be used as x-axis for resource monitoring. If iteration
reporting is unavailable once time is exceeded, "seconds from start" will be used for the x-axis.

#### sdk.google.storage [​](https://clear.ml/docs/latest/docs/configs/clearml_conf/\#sdkgooglestorage "Direct link to sdk.google.storage")

**`sdk.google.storage`** ( _dict_)

- Dictionary of Google Cloud Storage credentials.

* * *

**`sdk.google.storage.project`** ( _string_)

- For Google Cloud Storage, the name of project.

* * *

**`sdk.google.storage.credentials_json`** ( _string_)

- For Google Cloud Storage, the file path for the default Google storage credentials JSON file.

##### sdk.google.storage.credentials [​](https://clear.ml/docs/latest/docs/configs/clearml_conf/\#sdkgooglestoragecredentials "Direct link to sdk.google.storage.credentials")

**`sdk.google.storage.credentials`** ( _\[dict\]_)

- A list of dictionaries, with specific credentials per bucket and subdirectory

* * *

**`sdk.google.storage.credentials.bucket`** ( _string_)

- For Google Cloud Storage, if specifying credentials by the individual bucket, the name of the bucket.

* * *

**`sdk.google.storage.credentials.credentials_json`** ( _string_)

- For Google Cloud Storage, if specifying credentials by the individual bucket, the file path for the default Google storage credentials JSON file.

* * *

**`sdk.google.storage.credentials.project`** ( _string_)

- For Google Cloud Storage, if specifying credentials by the individual bucket, the name of the project.

* * *

**`sdk.google.storage.credentials.subdir`** ( _string_)

- For Google Cloud Storage, if specifying credentials by the individual bucket, a subdirectory within the bucket.

#### sdk.log [​](https://clear.ml/docs/latest/docs/configs/clearml_conf/\#sdklog "Direct link to sdk.log")

**`sdk.log`** ( _dict_)

- Dictionary of log options.

* * *

**`sdk.log.disable_urllib3_info`** ( _bool_)

- Indicates whether to disable `urllib3` info messages.

The values are:
  - `true` \- Disable
  - `false` \- Do not disable

* * *

**`sdk.log.null_log_propagate`** ( _bool_)

- As debugging feature, indicates whether to allow null log messages to propagate to the root logger (so they appear as stdout).

The values are:
  - `true` \- Allow
  - `false` \- Do not allow

* * *

**`sdk.log.task_log_buffer_capacity`** ( _integer_)

- The maximum capacity of the log buffer.

#### sdk.metrics [​](https://clear.ml/docs/latest/docs/configs/clearml_conf/\#sdkmetrics "Direct link to sdk.metrics")

**`sdk.metrics`** ( _dict_)

- Dictionary of metrics options.

* * *

**`sdk.metrics.file_history_size`** ( _string_)

- The history size for debug files per metric / variant combination
- Each metric / variant combination, `file_history_size` indicates the number of files stored in the upload destination
- Files are recycled so that `file_history_size` is the maximum number of files at any time.

* * *

**`sdk.metrics.matplotlib_untitled_history_size`** ( _integer_)

- The maximum history size for `matplotlib``imshow` files per plot title.
- File names for the uploaded images are recycled so that the number of images stored in the upload destination for each matplotlib plot title
will not exceed the value of `matplotlib_untitled_history_size`

* * *

**`sdk.metrics.plot_max_num_digits`** ( _integer_)

- The maximum number of digits after the decimal point in plot reporting. This can reduce the report size.

* * *

**`sdk.metrics.plot_upload_destination`** ( _str_)

- Upload destination for plots only (e.g. `"https://files.clearml.com"`). If set to a destination other than the ClearML
file server, plots will be uploaded as debug samples instead of being reported as plots.

* * *

**`sdk.metrics.tensorboard_single_series_per_graph`** ( _bool_)

note

This option is deprecated. This plot behavior is now controlled via the UI

- Indicates whether plots appear using TensorBoard behavior where each series is plotted in its own graph (plot-per-graph).

The values are:
  - `true` \- Support TensorBoard behavior
  - `false` \- Do not

##### sdk.metrics.images [​](https://clear.ml/docs/latest/docs/configs/clearml_conf/\#sdkmetricsimages "Direct link to sdk.metrics.images")

**`sdk.metrics.images`** ( _dict_)

- Dictionary of metrics images options.

* * *

**`sdk.metrics.images.format`** ( _string_)

- The image file format for generated debug images (such as "JPEG").

* * *

**`sdk.metrics.images.quality`** ( _integer_)

- The image quality for generated debug images.

* * *

**`sdk.metrics.images.subsampling`** ( _integer_)

- The image subsampling for generated debug images.

#### sdk.network [​](https://clear.ml/docs/latest/docs/configs/clearml_conf/\#sdknetwork "Direct link to sdk.network")

**`sdk.network.file_upload_retries`** ( _int_)

- Number of retries before failing to upload a file

* * *

**`sdk.network.iteration`** ( _dict_)

- Dictionary of network iteration options.

* * *

**`sdk.network.iteration.max_retries_on_server_error`** \` ( _integer_)

- For retries when getting frames from the server, if the server returned an error (http code 500), then this is the maximum number of retries.

* * *

**`sdk.network.iteration.retry_backoff_factor_sec`** ( _integer_)

- For retries when getting frames from the server, this is backoff factor for consecutive retry attempts. This is used to
determine the number of seconds between retries. The retry backoff factor is calculated as `{backoff factor} * (2 ^ ({number of total retries} - 1))`.

##### sdk.network.metrics [​](https://clear.ml/docs/latest/docs/configs/clearml_conf/\#sdknetworkmetrics "Direct link to sdk.network.metrics")

**`sdk.network.metrics`** ( _dict_)

- Dictionary of network metrics options.

* * *

**`sdk.network.metrics.file_upload_starvation_warning_sec`** ( _integer_)

- The number of seconds before a warning is issued that file-bearing events are sent for upload, but no uploads occur.

* * *

**`sdk.network.metrics.file_upload_threads`** ( _integer_)

- The number of threads allocated to uploading files when transmitting metrics for a specific iteration.

#### sdk.storage [​](https://clear.ml/docs/latest/docs/configs/clearml_conf/\#sdkstorage "Direct link to sdk.storage")

**`sdk.storage`** ( _dict_)

- Dictionary of storage options.

##### sdk.storage.cache [​](https://clear.ml/docs/latest/docs/configs/clearml_conf/\#sdkstoragecache "Direct link to sdk.storage.cache")

**`sdk.storage.cache`** ( _dict_)

- Dictionary of storage cache options. The keys include:
  - `default_base_dir` ( _str_) \- The default base directory for caching. The default is the `<system_temp_folder>/clearml_cache`.
  - `default_cache_manager_size` ( _int_) \- Maximum number of files in the cache (default 100 files).

Enterprise features

The ClearML Enterprise plan also supports the following configuration options under `sdk.storage.cache`:

- `size.max_used_bytes` ( _str_) \- Maximum size of the local cache directory. If set to `-1`, the directory can use
the available disk space. Specified in storage units (for example: `1GB`, `2TB`, `500MB`).
- `size.min_free_bytes` ( _str_) \- Minimum amount of free disk space that should be left. If `size.max_used_bytes` is
set to `-1`, this configuration option will limit the cache directory maximum size to `free disk space - size.min_free_bytes`.
Specified in storage units (for example: `1GB`, `2TB`, `500MB`).
- `zero_file_size_check` ( _bool_)\- If set to `True`, each cache hit will also check the cached file size, making sure
it is not zero (default `False`)
- `secondary` ( _dict_) \- Set up a secondary cache (acts as an L2 cache). When a request is made, the primary cache is
queried first. If the data is not in the primary cache, the secondary cache is queried. In case of a cache
miss, the data will be pulled to the primary cache, and then copied to the secondary cache. The
`sdk.storage.cache.secondary` dictionary supports the same option as the primary cache: `default_base_dir` (required), `size.max_used_bytes`,
`size.min_free_bytes`, etc. If an option is unspecified, it defaults to the primary cache's value.

##### sdk.storage.direct\_access [​](https://clear.ml/docs/latest/docs/configs/clearml_conf/\#sdkstoragedirect_access "Direct link to sdk.storage.direct_access")

**`sdk.storage.direct_access`** ( _dict_)

- Dictionary of storage direct access options.

* * *

**`sdk.storage.direct_access.url`** ( _string_)

- Specify a list of direct access objects using glob patterns which matches sets of files using wildcards. Direct access
objects are not downloaded or cached, and any download request will return a direct reference.

##### sdk.storage.log [​](https://clear.ml/docs/latest/docs/configs/clearml_conf/\#sdkstoragelog "Direct link to sdk.storage.log")

**`sdk.storage.log.report_download_chunk_size_mb`** ( _int_)

- Specify how often in MB the `StorageManager` reports its download progress to the console. By default, it reports
every 5MB

* * *

**`sdk.storage.log.report_upload_chunk_size_mb`** ( _int_)

- Specify how often in MB the `StorageManager` reports its upload progress to the console. By default, it reports every
5MB

##### sdk.storage.path\_substitution [​](https://clear.ml/docs/latest/docs/configs/clearml_conf/\#sdkstoragepath_substitution "Direct link to sdk.storage.path_substitution")

**`sdk.storage.path_substitution`** ( _\[dict\]_)

- List of dictionaries, where each dictionary contains path substitution mapping. This is useful in
cases where data was originally logged in one location and later moved, or when different workloads access the data through different mounts.

- Each dictionary contains a `registered_prefix` and a `local_prefix`. `registered_prefix` is the URL prefix logged in ClearML. `local_prefix` is the URL prefix to be used at runtime instead of the `registered_prefix` to access the data.

For example:





```text
sdk {

     storage {

        path_substitution = [\
\
           {\
\
              registered_prefix = "s3://bucket/research"\
\
              local_prefix = "file:///mnt/shared/bucket/research"\
\
           },\
\
           {\
\
              registered_prefix = "file:///mnt/shared/folder/"\
\
              local_prefix = "file:///home/user/shared/folder"\
\
           }\
\
        ]

     }

}
```


### environment section [​](https://clear.ml/docs/latest/docs/configs/clearml_conf/\#environment-section "Direct link to environment section")

**`environment`** ( _dict_)

Dictionary of environment variables and values which are applied to the OS environment as `key=value` for each key-value
pair.

Enable by setting `agent.apply_environment` OR `sdk.apply_environment` to `true`.

Example:

```text
environment {

   key_a: value_a

   key_b: value_b

}
```

### files section [​](https://clear.ml/docs/latest/docs/configs/clearml_conf/\#files-section "Direct link to files section")

**`files`** ( _dict_)

The `files` section allows to define files which will be auto-generated at designated paths with predefined content and
target format.

Enable by setting `agent.apply_files` OR `sdk.apply_files` to `true`.

Define each file's contents in a dictionary. Files content options include:

- `contents` \- Target file's content, typically a string (or any base type int/float/list/dict etc.)
- `format` \- Custom format for the contents. Currently supports `base64` to automatically decode a
base64-encoded contents string, otherwise ignored
- `path` \- Target file's path, may include `~` and inplace env vars
- `target_format` \- Format used to encode contents before writing into the target file. Supported values are `json`, `yaml`,
`yml`, and `bytes` (in which case the file will be written in binary mode). Default is text mode.
- `mode` \- File-system mode (permissions) to apply to the file after its creation. The mode string will be parsed into an integer (for example: `"0o777"` for `-rwxrwxrwx`)
- `overwrite` \- Overwrite the target file in case it exists. Default is `true`.

Example:

```text
files {

  myfile1 {

    contents: "The quick brown fox jumped over the lazy dog"

    path: "/tmp/fox.txt"

    mode: "0o777"

  }

  myjsonfile {

    contents: {

      some {

        nested {

           value: [1, 2, 3, 4]

        }

      }

    }

    path: "/tmp/test.json"

    target_format: json

  }

}

    # Apply top-level files section from configuration into local file system

sdk {



    apply_files: true

}
```

## Configuration Vault [​](https://clear.ml/docs/latest/docs/configs/clearml_conf/\#configuration-vault "Direct link to Configuration Vault")

Enterprise Feature

Configuration vaults are available under the ClearML Enterprise plan.

The ClearML Enterprise Server includes the configuration vault. Users can add configuration sections to the vault and, once
the vault is enabled, the configurations will be merged into the ClearML and ClearML Agent configurations upon code execution and/or agent launch.

These configurations override the configurations written in the configuration file.

See [configuration vault](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_profile#configuration-vault).

- [Editing Your Configuration File](https://clear.ml/docs/latest/docs/configs/clearml_conf/#editing-your-configuration-file)
- [Environment Variables](https://clear.ml/docs/latest/docs/configs/clearml_conf/#environment-variables)
- [Configuration File Sections](https://clear.ml/docs/latest/docs/configs/clearml_conf/#configuration-file-sections)
  - [agent section](https://clear.ml/docs/latest/docs/configs/clearml_conf/#agent-section)
  - [api section](https://clear.ml/docs/latest/docs/configs/clearml_conf/#api-section)
  - [sdk section](https://clear.ml/docs/latest/docs/configs/clearml_conf/#sdk-section)
  - [environment section](https://clear.ml/docs/latest/docs/configs/clearml_conf/#environment-section)
  - [files section](https://clear.ml/docs/latest/docs/configs/clearml_conf/#files-section)
- [Configuration Vault](https://clear.ml/docs/latest/docs/configs/clearml_conf/#configuration-vault)