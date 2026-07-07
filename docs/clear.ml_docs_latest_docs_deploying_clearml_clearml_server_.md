---
url: "https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server/"
title: "ClearML Server | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

## What is ClearML Server? [​](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server/\#what-is-clearml-server "Direct link to What is ClearML Server?")

The ClearML Server is the backend service infrastructure for ClearML. It allows multiple users to collaborate and
manage their tasks by working seamlessly with the [ClearML Python package](https://clear.ml/docs/latest/docs/clearml_sdk/clearml_sdk_setup) and [ClearML Agent](https://clear.ml/docs/latest/docs/clearml_agent).

ClearML Server is composed of the following:

- Web server including the [ClearML Web UI](https://clear.ml/docs/latest/docs/webapp/webapp_overview), which is the user interface for tracking, comparing, and managing tasks.

- API server which is a RESTful API for:
  - Documenting and logging tasks, including information, statistics, and results.
  - Querying task history, logs, and results.
- File server which stores media and models making them easily accessible using the ClearML Web UI.


The [**ClearML Hosted Service**](https://app.clear.ml/) is essentially the ClearML Server maintained for you.

![image](https://clear.ml/docs/latest/assets/images/ClearML_Server_Diagram-7ea19db8e22a7737f062cce207befe38.png)

The ClearML Web UI is the ClearML user interface and is part of ClearML Server.

Use the ClearML Web UI to:

- Track tasks
- Compare tasks
- Manage tasks

For detailed information about the ClearML Web UI, see [User Interface](https://clear.ml/docs/latest/docs/webapp/webapp_overview).

ClearML Server also comes with a [services agent](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_services_mode) preinstalled.

## Deployment [​](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server/\#deployment "Direct link to Deployment")

The ClearML Server can be deployed in any of the formats listed below. Once deployed, configure the server for web login
authentication, subdomains, and load balancers, and use any of its many configuration settings.

**To deploy your own ClearML Server:**

1. Deploy `clearml-server` using any of the available formats, which include:
   - Pre-built [AWS EC2 AMIs](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_aws_ec2_ami)
   - Pre-built [Google Cloud Platform custom images](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_gcp)
   - Pre-built Docker images for [Linux](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_linux_mac), [macOS](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_linux_mac), and
     [Windows 10](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_win)
   - [Kubernetes using Helm](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_kubernetes_helm)
2. Optionally, [configure ClearML Server](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_config) for additional features, including subdomains and load balancers,
web login authentication, and the non-responsive task watchdog.

3. [Connect the ClearML SDK to the ClearML Server](https://clear.ml/docs/latest/docs/clearml_sdk/clearml_sdk_setup)


## Updating [​](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server/\#updating "Direct link to Updating")

When necessary, upgrade your ClearML Server on any of the available formats:

- [AWS EC2 AMIs](https://clear.ml/docs/latest/docs/deploying_clearml/upgrade_server_aws_ec2_ami)
- [Google Cloud Platform](https://clear.ml/docs/latest/docs/deploying_clearml/upgrade_server_gcp)
- [Linux or MacOS](https://clear.ml/docs/latest/docs/deploying_clearml/upgrade_server_linux_mac)
- [Windows 10](https://clear.ml/docs/latest/docs/deploying_clearml/upgrade_server_win)
- [Kubernetes](https://clear.ml/docs/latest/docs/deploying_clearml/upgrade_server_kubernetes_helm)

If you are using v0.15 or Older, [upgrade to ClearML Server](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_es7_migration).

- [What is ClearML Server?](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server/#what-is-clearml-server)
- [Deployment](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server/#deployment)
- [Updating](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server/#updating)