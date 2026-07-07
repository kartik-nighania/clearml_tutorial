---
url: "https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_slurm_pyxis/"
title: "Slurm with Pyxis | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_slurm_pyxis/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

Enterprise Feature

Slurm Glue is available under the ClearML Enterprise plan.

Agents can deploy **Pyxis** containers in Linux clusters managed by Slurm.

Pyxis provides OCI-compatible container execution on Slurm clusters, typically backed by Enroot.

This integration works similarly to the [Native Slurm](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_slurm) workflow, with the following
differences:

- Container execution requires either Pyxis-specific SBATCH directives or a customized `srun` command wrapper.
- To run tasks using the `srun` wrapper approach, the agent must be launched with `--srun-delegation`.
- Tasks must specify an OCI-style container image (DockerHub, NVIDIA NGC, etc.).

## 1\. Install the Slurm Glue [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_slurm_pyxis/\#1-install-the-slurm-glue "Direct link to 1. Install the Slurm Glue")

Install the Slurm Glue on a machine where you can run Slurm commands such as `sbatch` and `squeue` (typically the login node).
One instance is sufficient for the entire cluster; there is no need to install it on every node.

```text
pip3 install -U --extra-index-url https://*****@*****.allegro.ai/repository/clearml_agent_slurm/simple clearml-agent-slurm
```

Python repository credentials

Your credentials for `--extra-index-url` are available in the WebApp under the **Help** menu ![Help menu](https://clear.ml/docs/latest/icons/ico-help-outlined.svg)**>** **ClearML Python Package setup** **>** **Install** step.

## 2\. Create a Batch Template [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_slurm_pyxis/\#2-create-a-batch-template "Direct link to 2. Create a Batch Template")

Create a batch template using either [explicit SBATCH Directives](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_slurm_pyxis/#explicit-sbatch-directives) or [Custom srun wrapper](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_slurm_pyxis/#custom-srun-wrapper).

note

Pyxis requires explicit OCI-style container URLs. For example:

- DockerHub: `docker://ubuntu:22.04`
- NVIDIA NGC: `docker://nvcr.io/nvidia/pytorch:24.01-py3`

ClearML supports this format when specifying a base container programmatically. For example:

```python
task.set_base_docker("docker://nvcr.io/nvidia/pytorch:24.01-py3")
```

### Explicit SBATCH Directives [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_slurm_pyxis/\#explicit-sbatch-directives "Direct link to Explicit SBATCH Directives")

Configure Pyxis directly using `#SBATCH --container-*` options. Use this approach for clusters where container execution is
standardized.

**Example Template:**

```text
#!/bin/bash

#SBATCH --job-name=clearml_task_${CLEARML_TASK.id}

#SBATCH --ntasks=1

# #SBATCH --mem=1mb

# #SBATCH --time=00:05:00

#SBATCH --output=task-${CLEARML_TASK.id}-%j.log

#SBATCH --partition debug

#SBATCH --cpus-per-task=1

#SBATCH --priority=5

#SBATCH --nodes=${CLEARML_TASK.hyperparams.properties.num_nodes.value:1}

# Pyxis container configuration

#SBATCH --container-image=${CLEARML_TASK.container.image}

#SBATCH --container-remap-root

#SBATCH --container-writable

${CLEARML_PRE_SETUP}

export CLEARML_MULTI_NODE_SINGLE_TASK=1

echo whoami $(whoami)

${CLEARML_AGENT_EXECUTE}

${CLEARML_POST_SETUP}
```

note

For details on available template variables, see [Slurm (Native)](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_slurm#dynamic-template-variables).

### Custom srun Wrapper [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_slurm_pyxis/\#custom-srun-wrapper "Direct link to Custom srun Wrapper")

Use this approach if your cluster does not use the SBATCH container directives, or if you need dynamic flags or custom
mounts. In this method, the template creates a custom srun wrapper which includes the required `srun --container-*` parameters.

**Example Template:**

```text
#!/bin/bash

#SBATCH --job-name=clearml_task_${CLEARML_TASK.id}

#SBATCH --ntasks=1

#SBATCH --output=task-${CLEARML_TASK.id}-%j.log

#SBATCH --partition debug

#SBATCH --cpus-per-task=1

#SBATCH --priority=5

#SBATCH --nodes=${CLEARML_TASK.hyperparams.properties.num_nodes.value:1}

${CLEARML_PRE_SETUP}

export CLEARML_MULTI_NODE_SINGLE_TASK=1

echo whoami $(whoami)

# Wrap srun to always add the container options

srun() {

    command srun \

        --container-image="${CLEARML_TASK.container.image}" \

        --container-remap-root \

        --container-writable \

        --container-mounts=$CLEARML_AGENT__AGENT__VENVS_DIR/clearml.conf:$CLEARML_AGENT__AGENT__VENVS_DIR/clearml.conf \

        "$@"

}

${CLEARML_POST_SETUP}
```

Note the srun wrapper method enables flexible mounting:

```text
--container-mounts=host_path:container_path[,host_path2:container_path2]
```

note

For details on available template variables see [Slurm (Native)](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_slurm#dynamic-template-variables).

## 3\. Launch the ClearML Agent Slurm Glue [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_slurm_pyxis/\#3-launch-the-clearml-agent-slurm-glue "Direct link to 3. Launch the ClearML Agent Slurm Glue")

Launch the ClearML Agent Slurm Glue and assign the Slurm configuration to a ClearML queue. For example, the following
associates the `default` queue to the `slurm.example_pyxis.template` script, so any jobs pushed to this queue will use the
resources set by that script.

```commandline
clearml-agent-slurm --template-files slurm.example_pyxis.template --queue default
```

If using the **srun approach** add `--srun-delegation` to the command line:

```commandline
clearml-agent-slurm --srun-delegation --template-files slurm.example_pyxis.template --queue default
```

## User Impersonation [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_slurm_pyxis/\#user-impersonation "Direct link to User Impersonation")

By default, Slurm jobs are submitted as the Linux user running the glue process.

You can configure the agent to submit jobs as different Linux users based on the ClearML user who enqueued the task.
See [Slurm User Impersonation](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_slurm_impersonation).

- [1\. Install the Slurm Glue](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_slurm_pyxis/#1-install-the-slurm-glue)
- [2\. Create a Batch Template](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_slurm_pyxis/#2-create-a-batch-template)
  - [Explicit SBATCH Directives](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_slurm_pyxis/#explicit-sbatch-directives)
  - [Custom srun Wrapper](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_slurm_pyxis/#custom-srun-wrapper)
- [3\. Launch the ClearML Agent Slurm Glue](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_slurm_pyxis/#3-launch-the-clearml-agent-slurm-glue)
- [User Impersonation](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_slurm_pyxis/#user-impersonation)