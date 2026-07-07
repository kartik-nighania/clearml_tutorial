---
url: "https://clear.ml/docs/latest/docs/webapp/applications/apps_jupyter_lab/"
title: "Jupyter Lab | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/webapp/applications/apps_jupyter_lab/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

Enterprise Feature

The Jupyter Lab application is available under the ClearML Enterprise plan.

The Jupyter Lab UI application allows you to launch a remote Jupyter Lab session on a machine that better meets resource needs.
This feature provides a local link to access Jupyter Lab on a remote machine over a secure and encrypted SSH connection,
letting you use the IDE as if you're running on the target machine itself.

The Jupyter Lab app offers workspace management features, allowing you to store, sync, and restore interactive workspaces
across sessions. This ensures that all your work is preserved and can be easily accessed in future sessions.

The Jupyter Lab session is set up using a [ClearML Agent](https://clear.ml/docs/latest/docs/clearml_agent). When configuring an app instance,
select a queue, and the agent servicing that queue will download and launch the IDE on its machine. When the server
setup is complete, the dashboard displays a link to access the Jupyter Lab session.

Once you have launched an app instance, you can view the following information in its dashboard:

- App status indicator
  - ![Jupyter loading](https://clear.ml/docs/latest/icons/ico-jupyter-lab-loading.svg) \- Remote IDE is setting up
  - ![Jupyter active](https://clear.ml/docs/latest/icons/ico-jupyter-lab-active.svg) \- Remote IDE is active
  - ![Jupyter idle](https://clear.ml/docs/latest/icons/ico-jupyter-lab-idle.svg) \- Remote IDE is idle
  - ![Jupyter stopped](https://clear.ml/docs/latest/icons/ico-jupyter-lab-stopped.svg) \- Remote IDE is stopped
- Idle time
- Restored workspace - If a previous session’s workspace was restored, this will display that session's ID
- Current session ID
- Open IDE - Link to the IDE session
- Server's resources monitoring (CPU / GPU / vMem utilization)
- Console - The console log shows the instance's activity, including server setup progress, server status changes

![Jupyter Lab Dashboard](https://clear.ml/docs/latest/assets/images/apps_jupyter_lab-2056391ecd036052900d83320dbe5da2.png#light-mode-only)![Jupyter Lab Dashboard](https://clear.ml/docs/latest/assets/images/apps_jupyter_lab_dark-3ed340f9bb298a84fce3f0f8b88b7f3e.png#dark-mode-only)

Embedding ClearML Visualization

You can embed plots from the app instance dashboard into [ClearML Reports](https://clear.ml/docs/latest/docs/webapp/webapp_reports) and other third-party platforms that support embedded content
(e.g. Notion). These visualizations are updated live as the app instance(s) updates. Hover over the plot and click ![Embed code](https://clear.ml/docs/latest/icons/ico-plotly-embed-code.svg)
to copy the embed code, and navigate to a report to paste the embed code.

## Jupyter Lab Instance Configuration [​](https://clear.ml/docs/latest/docs/webapp/applications/apps_jupyter_lab/\#jupyter-lab-instance-configuration "Direct link to Jupyter Lab Instance Configuration")

When configuring a new Jupyter Lab instance, you can fill in the required parameters or reuse the configuration of
a previously launched instance.

Launch an app instance with the configuration of a previously launched instance using one of the following options:

- Cloning a previously launched app instance will open the instance launch form with the original instance's
configuration prefilled.
- Importing an app configuration file. You can export the configuration of a previously launched instance as a JSON file
when viewing its configuration.

The prefilled instance launch form can be edited before starting the new app instance.

To configure a new app instance, click `Launch New`![Add new](https://clear.ml/docs/latest/icons/ico-add.svg)
to open the app's instance launch form.

### Configuration Options [​](https://clear.ml/docs/latest/docs/webapp/applications/apps_jupyter_lab/\#configuration-options "Direct link to Configuration Options")

note

Administrators can [customize](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/app_launch_form_custom) the launch form and
modify field names and/or available options and defaults.

This section describes the default configuration provided by ClearML.

- **Import Configuration** \- Import an app instance configuration file. This will fill the instance launch form with the
values from the file, which can be modified before launching the app instance

- **Git** \- To access a git repository remotely, add git information.
  - Repository
  - Branch
  - Commit
  - Store git repository as part of the snapshot - If you select to `Store git repo`, a copy of the repo will be stored
    in the workspace under `./git_repo`. Otherwise, the workspace will include a `./git_repo_not_synced` soft link to the
    expected repo path
- **Container**


  - Image - Container image used to run the IDE in
  - Docker arguments - `docker run` arguments, as a single string
  - Init script - Bash script that is executed upon container boot (comments are supported only at the beginning of the
    line)


important

The selected container image must include required Python packages for the application or allow installing them at runtime.

To view the required packages, hover over **Container requirements** in the application page under the app description.

In air-gapped environments, ensure one of the following:

  - Required packages are pre-installed in the image
  - The container can access a local PyPI proxy or package repository

- **Extra Packages** \- Extra Python packages to be installed

- **Persistent Workspace Path** \- Specify your workspace root directory. It will be automatically stored when the session
is closed and available for restoring into new sessions (example: `~/workspace`)

- **Queue** \- The queue serviced by the ClearML Agent that will execute the Jupyter Lab session

- **Maximum idle time** (hours) - Maximum time of inactivity, after which the session will shut down. Configure idleness
definitions under `Advanced Options`.

- **Interactive Session Name** \- Name for your current interactive session

- **Advanced Options**
  - Interactive Session Project - The ClearML project in which the interactive session is created. If left empty, the
    default project `Interactive Session` is used
  - Interactive Session Tags - Comma separated list of tags to add to your interactive session task.
  - Restore Interactive Workspace ID - Input a previously run interactive session ID to restore its workspace (when
    cloning a previously run app instance, this field is automatically filled with its ID)
  - Idle Network Threshold (MB/s) - Throughput under which the session will be considered idle
  - Idle CPU Threshold (%) - CPU utilization under which the session will be considered idle
  - Idle GPU Threshold (%) - GPU utilization under which the session will be considered idle
- **Export Configuration** \- Export the app instance configuration as a JSON file, which you can later import to create
a new instance with the same configuration


- [Jupyter Lab Instance Configuration](https://clear.ml/docs/latest/docs/webapp/applications/apps_jupyter_lab/#jupyter-lab-instance-configuration)
  - [Configuration Options](https://clear.ml/docs/latest/docs/webapp/applications/apps_jupyter_lab/#configuration-options)