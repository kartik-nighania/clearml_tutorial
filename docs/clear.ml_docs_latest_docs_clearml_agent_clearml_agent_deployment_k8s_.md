---
url: "https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_k8s/"
title: "Kubernetes | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_k8s/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

Agents can be deployed as Docker containers in a Kubernetes cluster. ClearML Agent adds missing scheduling capabilities to Kubernetes, enabling more flexible automation from code while leveraging all of ClearML Agent's features.

ClearML Agent is deployed onto a Kubernetes cluster using **Kubernetes-Glue**, which maps ClearML jobs directly to Kubernetes jobs. This allows seamless task execution and resource allocation across your cluster.

## How It Works [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_k8s/\#how-it-works "Direct link to How It Works")

The ClearML Kubernetes-Glue performs the following:

- Pulls jobs from the ClearML execution queue.
- Prepares a Kubernetes job based on a provided YAML template.
- Inside each job pod, the `clearml-agent`:

  - Installs the required environment for the task.
  - Executes and monitors the task process.
  - Logs task data to the ClearML Server

## Deployment Options [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_k8s/\#deployment-options "Direct link to Deployment Options")

You can deploy ClearML Agent onto Kubernetes using one of the following methods:

- **K8s Glue Script**:
Run a [K8s Glue script](https://github.com/clearml/clearml-agent/blob/master/examples/k8s_glue_example.py) on a Kubernetes CPU node. This approach is less scalable and typically suited for simpler use cases.

- **ClearML Agent Helm Chart (Recommended)**:
Use the ClearML Agent Helm Chart to spin up an agent pod acting as a controller. This is the recommended and
scalable approach. ClearML provides both [open-source](https://github.com/clearml/clearml-helm-charts/tree/main/charts/clearml-agent)
and [Enterprise](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_k8s/#agent-with-an-enterprise-server) Helm charts. See more details below.


## ClearML Helm Chart [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_k8s/\#clearml-helm-chart "Direct link to ClearML Helm Chart")

The ClearML Agent is installed on Kubernetes using a Helm chart. This sets up a controller pod that listens to ClearML queues and launches jobs as needed.

### Agent with an Open Source Server [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_k8s/\#agent-with-an-open-source-server "Direct link to Agent with an Open Source Server")

1. Add the Helm Repository:





```bash
helm repo add clearml

https://clearml.github.io/clearml-helm-charts
```

2. Update to latest version of this chart:





```bash
helm repo update

helm upgrade clearml-agent clearml/clearml-agent
```

3. Change values on existing installation:





```bash
helm upgrade clearml-agent clearml/clearml-agent --version <CURRENT CHART VERSION> -f custom_values.yaml
```


### Agent with an Enterprise Server [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_k8s/\#agent-with-an-enterprise-server "Direct link to Agent with an Enterprise Server")

ClearML Enterprise adds advanced Kubernetes features, such as:

- **Multi-Queue Support**: Service multiple ClearML queues within the same Kubernetes cluster.
- **Pod-Specific Templates**: Define resource configurations per queue using pod templates.

Upgrading to Agent Chart v6.12.3 or greater

The agent image in chart v6.12.3 now runs as a non-root user. Depending on your configuration, some changes to your
`values.yaml` may be required before upgrading. See [Upgrading to Agent Chart v6.12.3 or greater](https://clear.ml/docs/latest/docs/clearml_agent/enterprise_agent_upgrade_6_12_3)
for details.

#### Prerequisites [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_k8s/\#prerequisites "Direct link to Prerequisites")

- A running [ClearML Enterprise Server](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/k8s)

- API credentials (`<ACCESS_KEY>` and `<SECRET_KEY>`) generated via
the ClearML UI ( **Settings > Workspace > API Credentials > Create new credentials**). For more information, see [ClearML API Credentials](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_profile#clearml-api-credentials).



note





Make sure these credentials belong to an admin user or a service account with admin privileges.

- The worker environment must be able to access the ClearML Server over the same network.

- A DockerHub token to access the OCI enterprise Helm charts and Docker images

- To support **GPU** queues, you must deploy the **NVIDIA GPU Operator** on your Kubernetes cluster. For more information, see [GPU Operator](https://clear.ml/docs/latest/docs/clearml_agent/fractional_gpus/gpu_operator).


#### Installation [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_k8s/\#installation "Direct link to Installation")

1. Log into the ClearML OCI Registry:





```bash
helm registry login docker.io --username allegroaienterprise --password <CLEARML_DOCKERHUB_TOKEN>
```

2. Create a `clearml-agent-values.override.yaml` file with the following content:



note





Replace the `<ACCESS_KEY>` and `<SECRET_KEY>` with the API credentials you generated earlier.
Set the `<api|file|web>ServerUrlReference` fields to match your ClearML
Server URLs.









```yaml
imageCredentials:

     password: "<CLEARML_DOCKERHUB_TOKEN>"

clearml:

     agentk8sglueKey: "<ACCESS_KEY>"

     agentk8sglueSecret: "<SECRET_KEY>"

agentk8sglue:

     apiServerUrlReference: "<CLEARML_API_SERVER_REFERENCE>"

     fileServerUrlReference: "<CLEARML_FILE_SERVER_REFERENCE>"

     webServerUrlReference: "<CLEARML_WEB_SERVER_REFERENCE>"

     createQueues: true

     queues:

       exampleQueue:

         templateOverrides: {}

         queueSettings: {}
```

3. Install the ClearML Enterprise Agent Helm chart:





```bash
helm upgrade -i -n <WORKER_NAMESPACE> clearml-enterprise-agent oci://docker.io/clearml/clearml-enterprise-agent --create-namespace -f clearml-agent-values.override.yaml
```


#### Bootstrap [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_k8s/\#bootstrap "Direct link to Bootstrap")

ClearML Agent Bootstrap can be enabled to allow tasks to run in minimal container images without pre-installed
dependencies. For details, see [ClearML Agent Bootstrap](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_bootstrap).

#### Workload Customization [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_k8s/\#workload-customization "Direct link to Workload Customization")

The ClearML Agent monitors [ClearML queues](https://clear.ml/docs/latest/docs/fundamentals/agents_and_queues) for tasks that are scheduled for execution.

ClearML supports specifying custom definitions for individual queues for fine-grained control of workload parameters; you
can set Kubernetes overrides such as pod resources and labels, as well as runtime definitions like environment variables,
container images, or ClearML worker ID formats.

For more information, see [Custom Workload Configuration](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_custom_workload).

#### Agent Configuration for Orchestration Dashboard [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_k8s/\#agent-configuration-for-orchestration-dashboard "Direct link to Agent Configuration for Orchestration Dashboard")

ClearML Agents can be configured to report resource availability and control how workers appear in the [Orchestration Dashboard](https://clear.ml/docs/latest/docs/webapp/webapp_orchestration_dash).

For configuration details, see [Orchestration Dashboard Customization](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_orch_dash_k8s).

#### Additional Configuration Options [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_k8s/\#additional-configuration-options "Direct link to Additional Configuration Options")

To view available configuration options for the Helm chart, run the following command:

```bash
helm show readme oci://docker.io/clearml/clearml-enterprise-agent

# or

helm show values oci://docker.io/clearml/clearml-enterprise-agent
```

- [How It Works](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_k8s/#how-it-works)
- [Deployment Options](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_k8s/#deployment-options)
- [ClearML Helm Chart](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_k8s/#clearml-helm-chart)
  - [Agent with an Open Source Server](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_k8s/#agent-with-an-open-source-server)
  - [Agent with an Enterprise Server](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_k8s/#agent-with-an-enterprise-server)