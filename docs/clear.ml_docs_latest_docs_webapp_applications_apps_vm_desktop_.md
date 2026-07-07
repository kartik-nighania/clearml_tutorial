---
url: "https://clear.ml/docs/latest/docs/webapp/applications/apps_vm_desktop/"
title: "Virtual Machine Remote Desktop | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/webapp/applications/apps_vm_desktop/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

Enterprise Feature

The Virtual Machine Remote Desktop application is available under the ClearML Enterprise plan.

The **Virtual Machine Remote Desktop** application allows you to launch a VM on a remote machine in your cluster complete
with an active remote access session: Select either Remote Desktop or SSH access.

The app offers workspace management features, allowing you to store, sync, and restore interactive workspaces across sessions.
This ensures that all your work is preserved and can be easily accessed in future sessions.

The remote desktop session is set up using a [ClearML Agent](https://clear.ml/docs/latest/docs/clearml_agent). When configuring an app instance,
select a queue, and the agent servicing that queue will set up the remote environment.

AI Application Gateway

The Virtual Machine Remote Desktop relies on the ClearML App Gateway Router which implements user authentication and
securely routes incoming requests to the remote desktop session.

If the ClearML AI Application Gateway is not available, the remote desktop session might not be accessible.
For more information, see [AI Application Gateway](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/appgw).

Once you have launched an app instance, you can view the following information in its dashboard:

- App status indicator
  - ![Active server](https://clear.ml/docs/latest/icons/ico-vmdesktop-active.svg) \- Remote desktop session is setting up
  - ![Loading server](https://clear.ml/docs/latest/icons/ico-vmdesktop-loading.svg) \- Remote desktop session is active
  - ![Idle server](https://clear.ml/docs/latest/icons/ico-vmdesktop-idle.svg) \- Remote desktop session is idle
  - ![Stopped server](https://clear.ml/docs/latest/icons/ico-vmdesktop-stopped.svg) \- Remote desktop session is stopped
- Idle time
- Restored workspace - If a previous session’s workspace was restored, this will display that session's ID
- Current session ID
- Shareable Browser Link - Opens the remote desktop session directly in your web browser. This link performs user
authentication automatically through the browser: it verifies your credentials, adds the necessary cookies, and then
redirects you to the active session.
- Direct Link - A direct endpoint to the running session, intended for programmatic access (e.g. connecting from an external
application or script). This link does not include browser-based authentication, so you must manually provide an [Application Gateway](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/appgw)
access token when sending requests. You can generate a token in the ClearML Web UI under **Settings** \> **Workspace** \> **AI Application Gateway**.
- Server's resources monitoring (CPU / GPU / vMem utilization)
- Console - The console log shows the instance's activity, including server setup progress, server status changes

![VM Desktop Dashboard](https://clear.ml/docs/latest/assets/images/apps_vm_desktop-fcea72c9a2b39f007d8f1a3197ecf790.png#light-mode-only)![VM Desktop Dashboard](https://clear.ml/docs/latest/assets/images/apps_vm_desktop_dark-e3c934b7bbd7f6392a72732c1f460787.png#dark-mode-only)

Embedding ClearML Visualization

You can embed plots from the app instance dashboard into [ClearML Reports](https://clear.ml/docs/latest/docs/webapp/webapp_reports) and other third-party platforms that support embedded content
(e.g. Notion). These visualizations are updated live as the app instance(s) updates. Hover over the plot and click ![Embed code](https://clear.ml/docs/latest/icons/ico-plotly-embed-code.svg)
to copy the embed code, and navigate to a report to paste the embed code.

## VM Remote Desktop Instance Configuration [​](https://clear.ml/docs/latest/docs/webapp/applications/apps_vm_desktop/\#vm-remote-desktop-instance-configuration "Direct link to VM Remote Desktop Instance Configuration")

When configuring a new Remote Desktop Session instance, you can fill in the required parameters or reuse the configuration
of a previously launched instance.

Launch an app instance with the configuration of a previously launched instance using one of the following options:

- Cloning a previously launched app instance will open the instance launch form with the original instance's configuration
prefilled.
- Importing an app configuration file. You can export the configuration of a previously launched instance as a JSON file
when viewing its configuration.

The prefilled instance launch form can be edited before starting the new app instance.

To configure a new app instance, click ![Add new](https://clear.ml/docs/latest/icons/ico-add.svg) to open the app's instance launch form.

### Configuration Options [​](https://clear.ml/docs/latest/docs/webapp/applications/apps_vm_desktop/\#configuration-options "Direct link to Configuration Options")

note

Administrators can [customize](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/app_launch_form_custom) the launch form and
modify field names and/or available options and defaults.

This section describes the default configuration provided by ClearML.

- **Import Configuration**: Import an app instance configuration file. This will fill the instance launch form with the
values from the file, which can be modified before launching the app instance

- **Application Session Name**: Name for the application instance. This will appear in the instance list

- **Type** \- Select how you want to connect:
  - `Remote Desktop` for web based remote desktop access,
  - `SSH` for SSH access to the remote machine
- **Application instance project**: The ClearML project where the app instance is created. Access is determined by
project-level permissions (i.e. users with read access can use the app).

- **Queue** \- The [ClearML Queue](https://clear.ml/docs/latest/docs/fundamentals/agents_and_queues#what-is-a-queue) to which theVM Remote Desktop
app instance task will be enqueued.







Agent requirements





Make sure the agent assigned to this queue runs in an environment with Sysbox installed



If you are using autoscaled cloud instances, whose images do not have Sysbox installed, configure the autoscaler to
install and enable Sysbox. See [Running Autoscaler Instances with Sysbox](https://clear.ml/docs/latest/docs/webapp/applications/apps_aws_autoscaler#running-autoscaler-instances-with-sysbox).

- **Idle Time Limit** (Hours): Maximum time of inactivity, after which the session will shut down. Configure idleness
definitions under Advanced Options.

- **Environment Variables**: Additional environment variable to set inside the container before launching the application

- **Advanced Options**
  - Application Session Tags: Comma separated list of tags to add to your remote session
  - Restore application state from a previous session ID: Select the ID of a previous application session to restore
  - Idle Network Threshold: Throughput under which the session will be considered idle
  - Idle CPU Threshold: CPU utilization under which the session will be considered idle
  - Idle GPU Threshold: GPU utilization under which the session will be considered idle
- **Export Configuration**: Export the app instance configuration as a JSON file, which you can later import to create
a new instance with the same configuration


- [VM Remote Desktop Instance Configuration](https://clear.ml/docs/latest/docs/webapp/applications/apps_vm_desktop/#vm-remote-desktop-instance-configuration)
  - [Configuration Options](https://clear.ml/docs/latest/docs/webapp/applications/apps_vm_desktop/#configuration-options)