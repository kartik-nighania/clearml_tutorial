---
url: "https://clear.ml/docs/latest/docs/webapp/applications/apps_container_launcher/"
title: "Containerized Application Launcher | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/webapp/applications/apps_container_launcher/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

Enterprise Feature

The Containerized Application Launcher is available under the ClearML Enterprise plan.

The Containerized Application Launcher enables remote execution of application containers, while managing network routing,
data persistence, and resource monitoring.

The application features persistent workspaces, allowing you to restore previous session states when an app instance is
relaunched, ensuring continuity for long-running tasks. The launcher also enables flexible network configurations,
allowing secure access to applications over HTTPS or through raw TCP connections.

AI Application Gateway

The Containerized Application Launcher makes use of the App Gateway Router which implements a secure, authenticated
network endpoint for the application container.

If the ClearML AI Application Gateway is not available, the application container might not be accessible.
For more information, see [AI Application Gateway](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/appgw).

Once you have launched an app instance, you can view the following information in its dashboard:

- App status indicator
  - ![Loading app](https://clear.ml/docs/latest/icons/ico-containerlaunch-loading.svg) \- Remote containerized app is setting up
  - ![Active app](https://clear.ml/docs/latest/icons/ico-containerlaunch-active.svg) \- Remote containerized app is active
  - ![Idl app](https://clear.ml/docs/latest/icons/ico-containerlaunch-idle.svg) \- Remote containerized app is idle
  - ![Stopped app](https://clear.ml/docs/latest/icons/ico-containerlaunch-stopped.svg) \- Remote containerized app is stopped
- Idle time
- Restored workspace - If a previous session's workspace was restored, this will display its session ID
- Current session ID
- Network HTTPS - Links for secure access to the containerized applications over HTTPS
- Endpoint - A direct URL to the running containerized application service, intended for programmatic access. This endpoint
does not include browser-based authentication, so you must manually provide an [Application Gateway](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/appgw)
access token when sending requests. You can generate a token in the ClearML Web UI under **Settings** \> **Workspace** \> **AI Application Gateway**.
- Browser Link - Opens the containerized application directly in your web browser. This link performs user
authentication automatically through the browser.
- Total Number of Requests - Number of requests over time
- Latency - Request response time (ms) over time
- Server resources monitoring (CPU / GPU / vMem utilization)
- Console - The console log shows the instance's activity, including environment setup progress, status changes

![Containerized Application Launcher Dashboard](https://clear.ml/docs/latest/assets/images/apps_container_launcher-52064bd5ca801e8cff4818ecba80a3ff.png#light-mode-only)![Containerized Application Launcher Dashboard](https://clear.ml/docs/latest/assets/images/apps_container_launcher_dark-5ba4d35f911bcc462c88a1648721bd33.png#dark-mode-only)

Embedding ClearML Visualization

You can embed plots from the app instance dashboard into [ClearML Reports](https://clear.ml/docs/latest/docs/webapp/webapp_reports) and other third-party platforms that support embedded content
(e.g. Notion). These visualizations are updated live as the app instance(s) updates. Hover over the plot and click ![Embed code](https://clear.ml/docs/latest/icons/ico-plotly-embed-code.svg)
to copy the embed code, and navigate to a report to paste the embed code.

## Containerized Application Launcher Instance Configuration [​](https://clear.ml/docs/latest/docs/webapp/applications/apps_container_launcher/\#containerized-application-launcher-instance-configuration "Direct link to Containerized Application Launcher Instance Configuration")

When configuring a new Containerized App Launcher instance, you can fill in the required parameters or reuse the
configuration of a previously launched instance.

You can launch a new app instance using the configuration of a previously launched instance with the following options:

- Cloning a previously launched app instance will open the instance launch form with the original instance's configuration prefilled.
- Importing an app configuration file. You can export the configuration of a previously launched instance as a JSON file when viewing its configuration.

The prefilled instance launch form can be edited before starting the new app instance.

To configure a new app instance, click `Launch New` Add new to open the app's instance launch form.

### Configuration Options [​](https://clear.ml/docs/latest/docs/webapp/applications/apps_container_launcher/\#configuration-options "Direct link to Configuration Options")

note

Administrators can [customize](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/app_launch_form_custom) the launch form and
modify field names and/or available options and defaults.

This section describes the default configuration provided by ClearML.

- **Import Configuration** \- Import an app instance configuration file. This will fill the instance launch form with the values from the file, which can be modified before launching the app instance
- **Application Session Name** \- Name for the container launcher instance. This will appear in the instance list
- **Application instance project** \- ClearML Project where your app instance will be stored
- **Container Image** \- Containerized application image to use
- **Application execution command line** \- Command line to start the application inside the container, notice the container original entrypoint is ignored
- **Application execution directory** ( _optional_) \- Starting working directory for command-line inside the container.
- **Queue** \- The [ClearML Queue](https://clear.ml/docs/latest/docs/fundamentals/agents_and_queues#what-is-a-queue) to which the containerized app launcher instance task will be enqueued (make sure an agent is assigned to that queue).
- **Network routing to the container**\- Select one of the following:

  - None
  - TCP (raw)
  - HTTPS
- **Idle Time Limit** (Hours) - Maximum idle time after which the app instance will shut down
- **Created persistent internal snapshot of the application** \- Specify your workspace root directory, it will be automatically stored when the session is closed and restored into a new instance when the launcher app instance is cloned (example: `~/workspace`)
- **Environment Variables** \- Additional environment variable to set inside the container before launching the application
- **Configuration Files** \- Configuration files to inject into the container before launching the application
- **Advanced Options**
  - Container Arguments
  - Application Session Tags - Comma separated list of tags to add to your interactive session
  - Restore application state from a previous session ID - Select the ID of a previous application session to restore
  - Idle Network Threshold - Idle Network Threshold (MB/s) - Network throughput under which the session will be considered idle
  - Idle CPU Threshold (%) - CPU utilization under which the session will be considered idle
  - Idle GPU Threshold (%) - GPU utilization under which the session will be considered idle
- **Export Configuration** \- Export the app instance configuration as a JSON file, which you can later import to create a new instance with the same configuration

![Container launcher form](https://clear.ml/docs/latest/assets/images/apps_container_launcher_form-566cd2d1af2c9d2800d2e9e8089ceda3.png#light-mode-only)![Container launcher form](https://clear.ml/docs/latest/assets/images/apps_container_launcher_form_dark-da4ad3bb8e96c9d312fe8ea99b3e27b6.png#dark-mode-only)

- [Containerized Application Launcher Instance Configuration](https://clear.ml/docs/latest/docs/webapp/applications/apps_container_launcher/#containerized-application-launcher-instance-configuration)
  - [Configuration Options](https://clear.ml/docs/latest/docs/webapp/applications/apps_container_launcher/#configuration-options)