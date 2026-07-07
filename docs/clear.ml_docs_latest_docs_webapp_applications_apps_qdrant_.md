---
url: "https://clear.ml/docs/latest/docs/webapp/applications/apps_qdrant/"
title: "Qdrant DB Session | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/webapp/applications/apps_qdrant/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

Enterprise Feature

The Qdrant DB Session App is available under the ClearML Enterprise plan.

[Qdrant](https://github.com/qdrant/qdrant) is an open source vector database and similarity search engine.

The Qdrant DB Session application allows you to launch and manage standalone, detachable Qdrant database sessions.

The app serves DB sessions through secure, publicly accessible network endpoints. The database is automatically
serialized and stored, ensuring data persistence. You can clone previous application instances, and easily restore their
workspaces.

The app monitors endpoint activity and shuts down if the database session remains inactive for a specified maximum idle time.

AI Application Gateway

The Qdrant DB Session app makes use of the App Gateway Router which implements a secure, authenticated network endpoint
for the database session.

If the ClearML AI Application Gateway is not available, the database endpoint might not be accessible. For more information,
see [AI Application Gateway](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/appgw).

Once you start a Qdrant DB Session instance, you can view the following information in its dashboard:

- Status indicator
  - ![Active app](https://clear.ml/docs/latest/icons/ico-qdrant-active.svg) \- App instance is running and is actively in use
  - ![Loading app](https://clear.ml/docs/latest/icons/ico-qdrant-loading.svg) \- App instance is setting up
  - ![Idle app](https://clear.ml/docs/latest/icons/ico-qdrant-idle.svg) \- App instance is idle
  - ![Stopped app](https://clear.ml/docs/latest/icons/ico-qdrant-stopped.svg) \- App instance is stopped
- Idle time - Time elapsed since last activity
- Restored workspace - If another app instance’s workspace was restored, this will display that session’s ID
- Current database session ID
- Database Interface - The publicly accessible URL of the database session endpoint.
- RestAPI Endpoint - The publicly accessible URL of the database session’s Rest API endpoint.
- Web Interface - The publicly accessible URL of the DB session's web interface.
- Authentication Token - Link to your workspace settings page, where you can generate an access token for accessing your DB session (under `AI APPLICATION GATEWAY`).
- DB connect command - An example Python script to connect to the DB session
- Performance metrics
  - CPU usage
  - Network throughput
  - Disk performance
  - Memory performance
  - GPU utilization
  - GPU memory usage
  - GPU temperature
- Console log - The console log shows the app instance's console output: setup progress, status changes, error messages, etc.

![Qdrant Dashboard](https://clear.ml/docs/latest/assets/images/apps_qdrant-7b44a86db25aff561abc800f77a458e1.png#light-mode-only)![Qdrant Dashboard](https://clear.ml/docs/latest/assets/images/apps_qdrant_dark-a09665ac4076c9cb41adcc5c5328380d.png#dark-mode-only)

Embedding ClearML Visualization

You can embed plots from the app instance dashboard into [ClearML Reports](https://clear.ml/docs/latest/docs/webapp/webapp_reports) and other third-party platforms that support embedded content
(e.g. Notion). These visualizations are updated live as the app instance(s) updates. Hover over the plot and click ![Embed code](https://clear.ml/docs/latest/icons/ico-plotly-embed-code.svg)
to copy the embed code, and navigate to a report to paste the embed code.

## Qdrant DB Session Instance Configuration [​](https://clear.ml/docs/latest/docs/webapp/applications/apps_qdrant/\#qdrant-db-session-instance-configuration "Direct link to Qdrant DB Session Instance Configuration")

When configuring a new Qdrant DB Session instance, you can fill in the required parameters or reuse the configuration of a
previously launched instance.

Launch an app instance with the configuration of a previously launched instance using one of the following options:

- Cloning a previously launched app instance will open the instance launch form with the original instance's configuration prefilled.
- Importing an app configuration file. You can export the configuration of a previously launched instance as a JSON file when viewing its configuration.

The prefilled configuration form can be edited before launching the new app instance.

To configure a new app instance, click `Launch New`![Add new](https://clear.ml/docs/latest/icons/ico-add.svg)
to open the app's configuration form.

### Configuration Options [​](https://clear.ml/docs/latest/docs/webapp/applications/apps_qdrant/\#configuration-options "Direct link to Configuration Options")

note

Administrators can [customize](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/app_launch_form_custom) the launch form and
modify field names and/or available options and defaults.

This section describes the default configuration provided by ClearML.

- **Import Configuration** \- Import an app instance configuration file. This will fill the instance launch form with the
values from the file, which can be modified before launching the app instance

- **Container**


  - Image - Qdrant container image to use. For example: `qdrant/qdrant:v1.12.5`. Note that different database versions
    can be specified by selecting the relevant container image
  - Container Arguments - Override container environment variables using the format `--env key=value`


important

The selected container image must include required Python packages for the application or allow installing them at runtime.

To view the required packages, hover over **Container requirements** in the application page under the app description.

In air-gapped environments, ensure one of the following:

  - Required packages are pre-installed in the image
  - The container can access a local PyPI proxy or package repository

- **Queue** \- The [ClearML Queue](https://clear.ml/docs/latest/docs/fundamentals/agents_and_queues#what-is-a-queue) to which the Qdrant DB session
app instance task will be enqueued. Make sure an agent is assigned to that queue.

- **Database Session Name** \- An optional name for the database session for better visibility

- **Idle Time Limit (Hours**) \- Maximum idle time after which the app instance will shut down

- **Advanced Options**
  - Database Session Project - The ClearML project where the app instance is created. Access is determined by project-level
    permissions (i.e. users with read access can use the database session)
  - Database Session Tags - Optional comma-separated list of tags to attach to your current database session for improved
    organization
  - Restore Database state from a previous session ID - Select the ID of a previous database session app instance to restore
  - Custom Qdrant Configuration - Override the default Qdrant configuration (`user.yaml`). See [Qdrant](https://qdrant.tech/documentation/guides/configuration/)
    documentation for further details
  - Idle Network Threshold (MB/s) - Throughput under which the app instance will be considered idle
  - Idle CPU Threshold (percentage) - CPU utilization under which the app instance will be considered idle
  - Idle GPU Threshold (percentage) - GPU utilization under which the app instance will be considered idle
- **Export Configuration** \- Export the app instance configuration as a JSON file, which you can later import to create
a new instance with the same configuration


- [Qdrant DB Session Instance Configuration](https://clear.ml/docs/latest/docs/webapp/applications/apps_qdrant/#qdrant-db-session-instance-configuration)
  - [Configuration Options](https://clear.ml/docs/latest/docs/webapp/applications/apps_qdrant/#configuration-options)