---
url: "https://clear.ml/docs/latest/docs/webapp/applications/apps_milvus/"
title: "Milvus DB Session | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/webapp/applications/apps_milvus/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

Enterprise Feature

The Milvus DB Session App is available under the ClearML Enterprise plan.

[Milvus](https://github.com/milvus-io/milvus) is an open source high performance vector database.

The app serves DB sessions through secure, publicly accessible network endpoints. The database is automatically serialized
and stored, ensuring data persistence. You can clone previous application instances, and easily restore their workspaces.

The app monitors endpoint activity and shuts down if the database session remains inactive for a specified maximum idle time.

AI Application Gateway

The Milvus DB Session app makes use of the App Gateway Router which implements a secure, authenticated network endpoint
for the database session.

If the ClearML AI Application Gateway is not available, the database endpoint might not be accessible. For more information,
see [AI Application Gateway](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/appgw).

Once you start a Milvus DB Session instance, you can view the following information in its dashboard:

- Status indicator
  - ![Active app](https://clear.ml/docs/latest/icons/ico-milvus-active.svg) \- App instance is running and is actively in use
  - ![Loading app](https://clear.ml/docs/latest/icons/ico-milvus-loading.svg) \- App instance is setting up
  - ![Idle app](https://clear.ml/docs/latest/icons/ico-milvus-idle.svg) \- App instance is idle
  - ![Stopped app](https://clear.ml/docs/latest/icons/ico-milvus-stopped.svg) \- App instance is stopped
- Idle time - Time elapsed since last activity
- Restored workspace - If another app instance’s workspace was restored, this will display that session’s ID
- Current database session ID
- Database gRPC IP:PORT - network address for the database’s gRPC endpoint
- Database Username and password
- Connect Command - An example Python script to connect to the DB session
- Performance metrics
  - CPU usage
  - Network throughput
  - Disk performance
  - Memory performance
  - GPU utilization
  - GPU memory usage
  - GPU temperature
- Console log - The console log shows the app instance's console output: setup progress, status changes, error messages, etc.

![Milvus Dashboard](https://clear.ml/docs/latest/assets/images/apps_milvus-aa3385d3bdb842f62ace49af726cee85.png#light-mode-only)![Milvus Dashboard](https://clear.ml/docs/latest/assets/images/apps_milvus_dark-bfa2b57f764dfaddfd6d3a918d177d47.png#dark-mode-only)

Embedding ClearML Visualization

You can embed plots from the app instance dashboard into [ClearML Reports](https://clear.ml/docs/latest/docs/webapp/webapp_reports) and other third-party platforms that support embedded content
(e.g. Notion). These visualizations are updated live as the app instance(s) updates. Hover over the plot and click ![Embed code](https://clear.ml/docs/latest/icons/ico-plotly-embed-code.svg)
to copy the embed code, and navigate to a report to paste the embed code.

## Milvus DB Session Instance Configuration [​](https://clear.ml/docs/latest/docs/webapp/applications/apps_milvus/\#milvus-db-session-instance-configuration "Direct link to Milvus DB Session Instance Configuration")

When configuring a new Milvus DB Session instance, you can fill in the required parameters or reuse the configuration of
a previously launched instance.

Launch an app instance with the configuration of a previously launched instance using one of the following options:

- Cloning a previously launched app instance will open the instance launch form with the original instance's configuration prefilled.
- Importing an app configuration file. You can export the configuration of a previously launched instance as a JSON file when viewing its configuration.

The prefilled configuration form can be edited before launching the new app instance.

To configure a new app instance, click `Launch New`![Add new](https://clear.ml/docs/latest/icons/ico-add.svg)
to open the app's configuration form.

### Configuration Options [​](https://clear.ml/docs/latest/docs/webapp/applications/apps_milvus/\#configuration-options "Direct link to Configuration Options")

note

Administrators can [customize](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/app_launch_form_custom) the launch form and
modify field names and/or available options and defaults.

This section describes the default configuration provided by ClearML.

- **Import Configuration** \- Import an app instance configuration file. This will fill the instance launch form with the values
from the file, which can be modified before launching the app instance

- **Container**


  - Image - Milvus container image to use. For example: `milvus/milvus:v1.12.5`. Note that different database versions
    can be specified by selecting the relevant container image.
  - Container Arguments - Override container environment variables using the format `--env key=value`


important

The selected container image must include required Python packages for the application or allow installing them at runtime.

To view the required packages, hover over **Container requirements** in the application page under the app description.

In air-gapped environments, ensure one of the following:

  - Required packages are pre-installed in the image
  - The container can access a local PyPI proxy or package repository

- **Queue** \- The [ClearML Queue](https://clear.ml/docs/latest/docs/fundamentals/agents_and_queues#what-is-a-queue) to which the Milvus DB session
app instance task will be enqueued. Make sure an agent is assigned to that queue.

- **Database Session Name** \- An optional name for the database session for better visibility

- **Database Root Password** \- Provide root user password for DB management

- **Idle Time Limit (Hours)** \- Maximum idle time after which the app instance will shut down

- **Advanced Options**
  - Database Session Project - The ClearML project where the app instance is created. Access is determined by project-level permissions (i.e. users with read access can use the database session)
  - Database Session Tags - Optional comma-separated list of tags to attach to your current database session for improved organization
  - Restore Database state from a previous session ID - Select the ID of a previous database session to restore
  - Custom Milvus User Configuration - Override the default Milvus configuration (`user.yaml`). See [Milvus documentation](https://milvus.io/docs/system_configuration.md) for further details
  - Custom Milvus EtcD Configuration - Milvus `embedEtcd.yaml` configuration section. See [Milvus repository](https://github.com/milvus-io/milvus/blob/master/configs/advanced/etcd.yaml) for further details
  - Idle Network Threshold (MB/s) - Throughput under which the app instance will be considered idle
  - Idle CPU Threshold (percentage) - CPU utilization under which the app instance will be considered idle
  - Idle GPU Threshold (percentage) - GPU utilization under which the app instance will be considered idle
- **Export Configuration** \- Export the app instance configuration as a JSON file, which you can later import to create
a new instance with the same configuration


- [Milvus DB Session Instance Configuration](https://clear.ml/docs/latest/docs/webapp/applications/apps_milvus/#milvus-db-session-instance-configuration)
  - [Configuration Options](https://clear.ml/docs/latest/docs/webapp/applications/apps_milvus/#configuration-options)