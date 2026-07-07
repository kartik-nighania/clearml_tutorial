---
url: "https://clear.ml/docs/latest/docs/clearml_agent/"
title: "ClearML Agent | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/clearml_agent/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

4 - Agent Remote Execution and Automation - YouTube

Tap to unmute

[4 - Agent Remote Execution and Automation](https://www.youtube.com/watch?v=MX3BrXnaULs) [ClearML](https://www.youtube.com/channel/UCDYdA4hjckRLRVBrCoKenCQ)

![thumbnail-image](https://yt3.ggpht.com/ytc/AIdro_kEljxxvNzLP5hB1Bv03O_F-CooCUhLk76T2A-B2sM9_w=s68-c-k-c0x00ffffff-no-rj)

ClearML2.62K subscribers

**ClearML Agent** is a virtual environment and execution manager for DL / ML solutions on GPU machines. It integrates with the **ClearML Python Package** and ClearML Server to provide a full AI cluster solution.

Its main focus is around:

- Reproducing task runs, including their complete environments.
- Scaling workflows on multiple target machines.

ClearML Agent executes a task or other workflow by reproducing the state of the code from the original machine
to a remote machine.

![ClearML Agent flow diagram](https://clear.ml/docs/latest/assets/images/clearml_agent_flow_diagram-303e55229e7d733c5c73af2695c4fc1b.png#light-mode-only)![ClearML Agent flow diagram](https://clear.ml/docs/latest/assets/images/clearml_agent_flow_diagram_dark-01169384c43eced0b7a983b59b12f514.png#dark-mode-only)

The preceding diagram demonstrates a typical flow where an agent executes a task:

1. Enqueue a task for execution on the queue.
2. The agent pulls the task from the queue.
3. The agent launches a container in which to run the task's code.
4. The task's execution environment is set up:
1. Execute any custom setup script configured.
2. Install any required system packages.
3. Clone the code from a git repository.
4. Apply any uncommitted changes recorded.
5. Set up the Python environment and required packages.
5. The task's script/code is executed.

Python Version

ClearML Agent uses the Python version available in the environment or container in which it executes the code. It does not
install Python, so make sure to use a container or environment with the version you need.

While the agent is running, it continuously reports system metrics to the ClearML Server (these can be monitored in the
[**Orchestration**](https://clear.ml/docs/latest/docs/webapp/webapp_workers_queues) page).

Continue using ClearML Agent once it is running on a target machine. Reproducing task runs and execute
automated workflows in one (or both) of the following ways:

- Programmatically (using [`Task.enqueue()`](https://clear.ml/docs/latest/docs/references/sdk/task#taskenqueue) or [`Task.execute_remotely()`](https://clear.ml/docs/latest/docs/references/sdk/task#execute_remotely))
- Through the ClearML Web UI (without working directly with code), by cloning tasks and enqueuing them to the
queue that a ClearML Agent is servicing.

The agent facilitates [overriding task execution detail](https://clear.ml/docs/latest/docs/webapp/webapp_exp_tuning) values through the UI without
code modification. When you modify a cloned task’s configuration, the ClearML agent will override the original values
during execution:

- Modified package requirements will have the task script run with updated packages
- Modified recorded command line arguments will have the ClearML agent inject the new values in their stead
- Code-level configuration instrumented with [`Task.connect()`](https://clear.ml/docs/latest/docs/references/sdk/task#connect) will be overridden by modified hyperparameters

ClearML Agent can be deployed in various setups to suit different workflows and infrastructure needs:

- [Bare Metal / VM](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_bare_metal#spinning-up-an-agent)
- [Kubernetes](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_k8s)
- [Slurm](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_slurm)
- [Google Colab](https://clear.ml/docs/latest/docs/guides/ide/google_colab)

## References [​](https://clear.ml/docs/latest/docs/clearml_agent/\#references "Direct link to References")

For more information, see the following:

- [ClearML Agent CLI](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_ref) for a reference for `clearml-agent`'s CLI commands.
- [ClearML Agent Environment Variables](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_env_var) for a list of environment variables
to configure ClearML Agent
- [Agent Section](https://clear.ml/docs/latest/docs/configs/clearml_conf#agent-section) for a list of options to configure the ClearML Agent in the
`clearml.conf`

- [References](https://clear.ml/docs/latest/docs/clearml_agent/#references)