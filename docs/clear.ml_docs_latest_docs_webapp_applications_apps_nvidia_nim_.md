---
url: "https://clear.ml/docs/latest/docs/webapp/applications/apps_nvidia_nim/"
title: "NVIDIA NIM | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/webapp/applications/apps_nvidia_nim/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

Enterprise Feature

The NIM App is available under the ClearML Enterprise plan.

The NIM application enables users to launch [NVIDIA NIM](https://developer.nvidia.com/nim) models through their specific containers. The NIM application
serves your model on a machine of your choice. Once an app instance is running, it serves your model through a secure,
publicly accessible network endpoint. The app monitors endpoint activity and shuts down if the model remains inactive
for a specified maximum idle time.

- The `NGC_API_KEY` environment variable needs to be set to a valid NGC API key. You can set the variable in one of the following ways:

  - The NIM app launch form's `Environment Variables` field
  - [Configuration vault](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_profile#configuration-vault)

AI Application Gateway

The NIM app makes use of the App Gateway Router which implements a secure, authenticated network endpoint for the model.

If the ClearML AI Application Gateway is not available, the model endpoint might not be accessible.
For more information, see [AI Application Gateway](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/appgw).

Once you start a NIM instance, you can view the following information in its dashboard:

- Status indicator
  - ![Active instance](https://clear.ml/docs/latest/icons/ico-nvidia-active.svg) \- App instance is running and is actively in use
  - ![Loading instance](https://clear.ml/docs/latest/icons/ico-nvidia-loading.svg) \- App instance is setting up
  - ![Idle instance](https://clear.ml/docs/latest/icons/ico-nvidia-idle.svg) \- App instance is idle
  - ![Stopped instance](https://clear.ml/docs/latest/icons/ico-nvidia-stopped.svg) \- App instance is stopped
- Idle time - Time elapsed since last activity
- Endpoint - The publicly accessible URL of the model endpoint. Active model endpoints are also available in the
[Model Endpoints](https://clear.ml/docs/latest/docs/webapp/webapp_model_endpoints) table, which allows you to view and compare endpoint details and
monitor status over time
- Generate Token - Link to `AI APPLICATION GATEWAY` section of the Settings page, where you can generate a token for accessing your deployed model
- Command to connect to the deployed model. The generated `curl` command includes the model's endpoint. Replace `YOUR_GENERATED_TOKEN` with a valid token generated in the `AI APPLICATION GATEWAY` section of the Settings page.
- Total Number of Requests - Number of requests over time
- Tokens per Second - Number of tokens processed over time
- Latency - Request response time (ms) over time
- Endpoint resource monitoring metrics over time
- CPU usage
  - Network throughput
  - Disk performance
  - Memory performance
  - GPU utilization
  - GPU memory usage
  - GPU temperature
- Console log - The console log shows the app instance's console output: setup progress, status changes, error messages,
etc.

![Nvidia NIM App](https://clear.ml/docs/latest/assets/images/apps_nvidia_nim-2ac7ab2399242dabd0895ef8f76cac36.png#light-mode-only)![Nvidia NIM App](https://clear.ml/docs/latest/assets/images/apps_nvidia_nim_dark-7b680525d51bcfe370f4c20daaabc9ac.png#dark-mode-only)

Embedding ClearML Visualization

You can embed plots from the app instance dashboard into [ClearML Reports](https://clear.ml/docs/latest/docs/webapp/webapp_reports) and other third-party platforms that support embedded content
(e.g. Notion). These visualizations are updated live as the app instance(s) updates. Hover over the plot and click ![Embed code](https://clear.ml/docs/latest/icons/ico-plotly-embed-code.svg)
to copy the embed code, and navigate to a report to paste the embed code.

## NIM Instance Configuration [​](https://clear.ml/docs/latest/docs/webapp/applications/apps_nvidia_nim/\#nim-instance-configuration "Direct link to NIM Instance Configuration")

When configuring a new NIM instance, you can fill in the required parameters or reuse the
configuration of a previously launched instance.

Launch an app instance with the configuration of a previously launched instance using one of the following options:

- Cloning a previously launched app instance will open the instance launch form with the original instance's
configuration prefilled.
- Importing an app configuration file. You can export the configuration of a previously launched instance as a JSON file
when viewing its configuration.

The prefilled configuration form can be edited before launching the new app instance.

To configure a new app instance, click `Launch New`![Add new](https://clear.ml/docs/latest/icons/ico-add.svg)
to open the app's configuration form.

### Configuration Options [​](https://clear.ml/docs/latest/docs/webapp/applications/apps_nvidia_nim/\#configuration-options "Direct link to Configuration Options")

note

Administrators can [customize](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/app_launch_form_custom) the launch form and
modify field names and/or available options and defaults.

This section describes the default configuration provided by ClearML.

- **Import Configuration**: Import an app instance configuration file. This will fill the instance launch form with the
values from the file, which can be modified before launching the app instance
- **Application instance project**: The ClearML project where the app instance is created. Access is determined by
project-level permissions (i.e. users with read access can use the app).
- **NIM Container Image**: Select the containerized application image to use. Note the different tags / versions of each image
- **Compute Resource (Queue)**: The [ClearML Queue](https://clear.ml/docs/latest/docs/fundamentals/agents_and_queues#what-is-a-queue) to which the NIM app instance task will be enqueued.






Agent requirements





Make sure the agent assigned to this queue:



  - Has access to NVIDIA's container registry (`nvcr.io`). See [NVCR Access](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_nvcr) for more information.
  - Runs in [Docker mode](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_execution_env#docker-mode) if it is a bare-metal agent

NIM Model Caching

See [NIM Cache](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_nim_caching) on how to configure persistent caching for NIM
models for Kubernetes.

- **AI Gateway Route**: Select an available, admin-preconfigured route to use as the service endpoint. If none is selected, an ephemeral endpoint will be created.
- **Idle Time Limit** (Hours): Maximum idle time after which the app instance will shut down
- **Environment Variables**: Additional environment variable to set inside the container before launching the application
- **Application Session Tags**: Comma separated list of tags to add to your current application session
- **Export Configuration** \- Export the app instance configuration as a JSON file, which you can later import to create a
new instance with the same configuration

![NIM app form](https://clear.ml/docs/latest/assets/images/apps_nvidia_nim_form-098978a07ea42ba3e8186269168c6433.png#light-mode-only)![NIM app form](https://clear.ml/docs/latest/assets/images/apps_nvidia_nim_form_dark-2eae4d916923992f5243d4196bbb1b4f.png#dark-mode-only)

- [NIM Instance Configuration](https://clear.ml/docs/latest/docs/webapp/applications/apps_nvidia_nim/#nim-instance-configuration)
  - [Configuration Options](https://clear.ml/docs/latest/docs/webapp/applications/apps_nvidia_nim/#configuration-options)