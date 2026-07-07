---
url: "https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_orch_dash_k8s/"
title: "Orchestration Dashboard Customization (K8s) | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_orch_dash_k8s/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

Enterprise Feature

The Orchestration Dashboard is available under the ClearML Enterprise plan.

The ClearML [Orchestration Dashboard](https://clear.ml/docs/latest/docs/webapp/webapp_orchestration_dash) provides visibility into available and in-use compute resources across your
infrastructure. Agent configuration controls how resources are reported to the dashboard and how workers are organized
into categories and groups.

## Reporting Cluster Capacity [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_orch_dash_k8s/\#reporting-cluster-capacity "Direct link to Reporting Cluster Capacity")

### GPU Capacity [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_orch_dash_k8s/\#gpu-capacity "Direct link to GPU Capacity")

To show the GPUs available to the agent in the Orchestration Dashboard,
configure the agent in one of the following ways:

- **Fixed Value**:

Use `gpu.reportMax` to report a fixed number of GPUs. This setting overrides GPU auto-discovery if both are enabled.





```yaml
agentk8sglue:

    orchestrationDashboard:

      gpu:

        # -- Reporting to Dashboard max GPU available. This will report 2 GPUs.

        reportMax: 2
```

- **Automatic GPU Discovery**:

Enable automatic discovery to have the agent detect and report GPUs across your Kubernetes cluster.
This requires cluster-level access (`agentk8sglue.serviceAccountClusterAccess: true`), since the agent must list and evaluate all cluster nodes.

When GPU discovery is enabled, the Agent identifies which cluster nodes have GPUs and how many GPUs each node provides.
These options control how nodes are selected and how GPUs are counted:


  - `baseSelector` \- The default label selector used to identify GPU nodes.
  - `nodeSelector` \- An additional filter applied on top of `baseSelector` to narrow down which nodes are included in discovery. For
    example, to limit discovery to a specific node pool, use `"nodepool=gpu-a100"`.
  - `gpuCountSelector` \- Comma-separated list of labels used to count GPUs per node. The first matching label determines the reported GPU count.

With discovery enabled, the agent evaluates nodes matching the provided selectors and reports their GPU
capacity to the dashboard at the configured interval.

```yaml
agentk8sglue:

  # Cluster access is required for GPU discovery

  serviceAccountClusterAccess: true

  orchestrationDashboard:

    gpu:

      discovery:

        enabled: true

        baseSelector: "kubernetes.io/os=linux,nvidia.com/gpu.present=true"

        nodeSelector: ""  # Optional: further restrict discovery

        gpuCountSelector: "nvidia.com/gpu.count"
```

### CPU Capacity [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_orch_dash_k8s/\#cpu-capacity "Direct link to CPU Capacity")

To show the CPUs available to the agent in the Orchestration Dashboard,
configure the agent in one of the following ways:

- **Fixed Value**:

Use `cpu.reportMax` to report a fixed number of CPUs. This setting overrides CPU auto-discovery if both are enabled.





```yaml
agentk8sglue:

    orchestrationDashboard:

      cpu:

        # -- Reporting to Dashboard max CPU available. This will report 8 CPUs.

        reportMax: 8
```

- **Automatic CPU Discovery**:

Enable automatic discovery to have the agent detect and report CPUs across your Kubernetes cluster.
This requires cluster-level access (`agentk8sglue.serviceAccountClusterAccess: true`), since the agent must list and evaluate all cluster nodes.
  - `nodeSelector` \- Filter to narrow down which nodes are included in CPU discovery. Selector is in AND condition (comma-separated list of Label=Value).





    ```yaml
    agentk8sglue:

      # Cluster access is required for CPU discovery

      serviceAccountClusterAccess: true



      orchestrationDashboard:

        cpu:

          discovery:

            enabled: true

            nodeSelector: ""  # Optional: restrict discovery to specific nodes
    ```
- **Namespace-scoped CPU Reporting**:

To report CPUs scoped to a single namespace, enable `reportNamespaced`. By default, the agent's own namespace is used. Use `reportNamespaceOverride` to specify a different namespace.





```yaml
agentk8sglue:

    orchestrationDashboard:

      cpu:

        reportNamespaced: true

        reportNamespaceOverride: "my-namespace"  # Optional: defaults to agent's namespace
```


### Report Configuration [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_orch_dash_k8s/\#report-configuration "Direct link to Report Configuration")

You can configure how reports are sent and how often:

- `reportType`\- How the agent sends reports to the dashboard. Use one of the following options:

  - `disabled` (or no value) - Do not send any reports.
  - `global` \- Send a single category-level report that sums up all agents into the category total. Overrides individual
    agent reports. For more information about agent categorization, see [Resource Categories and Groups](https://clear.ml/docs/latest/docs/webapp/webapp_orchestration_dash#resource-categories-and-groups).
  - `aggregate` \- Send a report per agent. The dashboard aggregates all reports in the category automatically. For more information about agent categorization, see [Resource Categories and Groups](https://clear.ml/docs/latest/docs/webapp/webapp_orchestration_dash#resource-categories-and-groups).
- `reportSeconds` \- Interval in seconds between dashboard updates. Controls how frequently the agent sends capacity data.

```yaml
agentk8sglue:

  # Cluster access is required for discovery

  serviceAccountClusterAccess: true

  orchestrationDashboard:

    # Enable periodic reporting to the Orchestration Dashboard

    reportType: "global"

    reportSeconds: 600

    # GPU reporting

    gpu:

      # Overrides GPU discovery

      reportMax: 0

      # Enable GPU discovery

      discovery:

        enabled: true

        baseSelector: "kubernetes.io/os=linux,nvidia.com/gpu.present=true"

        nodeSelector: ""  # Optional: further restrict discovery

        gpuCountSelector: "nvidia.com/gpu.count"

    # CPU reporting

    cpu:

      # Overrides CPU discovery

      reportMax: 0

      # Enable CPU discovery

      discovery:

        enabled: true

        nodeSelector: ""  # Optional: restrict discovery to specific nodes

      reportNamespaced: false

      reportNamespaceOverride: ""
```

## Customizing Worker IDs [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_orch_dash_k8s/\#customizing-worker-ids "Direct link to Customizing Worker IDs")

The Orchestration Dashboard organizes agents in a 2-level hierarchy of **Categories** and **Resource Groups**.

The resource dashboard shows high-level aggregate utilization across the resource categories, with specific agent details
listed in the workload table, grouped by resource group.

![Orchestration Dashboard](https://clear.ml/docs/latest/assets/images/orchestration_dashboard_custom-df6231e81bb4201c7fb203b65bdce1da.png#light-mode-only)![Orchestration Dashboard](https://clear.ml/docs/latest/assets/images/orchestration_dashboard_custom_dark-2b96b95a0e9a54d3097f43e680d2694c.png#dark-mode-only)

Agent categorization is controlled through the ID it assigned on launch, according to the following format:

```text
<CATEGORY>:<RESOURCE_GROUP>:<WORKLOAD_ID>
```

The following defaults are used by the agent helm chart:

- Category: `k8s`

- Resource Group: `group`

- Workload ID: Makes use of the Task ID of the task executed in that node. How the agents appear in the dashboard can be
customized by chart overrides (`clearml-agent-values.override.yaml`):





```yaml
agentk8sglue:

# K8s Agent Worker ID

workerIdOverride: "k8s:my-agent"

# Default Worker ID template for nodes spawned by the K8s Agent

taskWorkerIdOverride: "k8s:my-group:{task_id}"
```


important

Make sure the **CATEGORY** portion (the first segment before `:`) is the same in both `workerIdOverride` and `taskWorkerIdOverride`
if you want the K8s Agent and its Tasks to appear in the same dashboard category box.

Worker ID templates support the following dynamic variables using the `"{variable_name}"` syntax:

- `worker_id` – The Agent's Worker ID
- `worker_id_parts` – The Agent Worker ID split by `:`. For example: `"k8s:glue-agent:my-agent"` → `["k8s", "glue-agent", "my-agent"]`.
Each part can be referenced in templates using `{worker_id_parts[n]}`.
- `task_id` – The ClearML Task ID
- `pod_name` – The Kubernetes Pod/Job name
- `namespace` – The Kubernetes namespace used to run the Task

### Configure Resource Groups Per Queue [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_orch_dash_k8s/\#configure-resource-groups-per-queue "Direct link to Configure Resource Groups Per Queue")

You can override the Worker ID template per queue.

##### Example: Split by GPU Type [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_orch_dash_k8s/\#example-split-by-gpu-type "Direct link to Example: Split by GPU Type")

This configuration creates separate resource groups for different GPU queues. Both queues will appear under the `k8s` category,
with two distinct resource groups: `H100` and `L40s`. Tasks will be listed inside each group by Task ID.

```yaml
agentk8sglue:

 queues:

   h100_queue:

     templateOverrides: {}

     queueSettings:

       customWorkerIdTemplate: "k8s:H100:{task_id}"

   l40s_queue:

     templateOverrides: {}

     queueSettings:

       customWorkerIdTemplate: "k8s:L40s:{task_id}"
```

### Hide Workers from the Orchestration Dashboard [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_orch_dash_k8s/\#hide-workers-from-the-orchestration-dashboard "Direct link to Hide Workers from the Orchestration Dashboard")

To exclude specific workers from appearing in the Orchestration Dashboard, configure regex patterns in the control plane
`clearml-values.override.yaml` file:

```yaml
clearml:

 orchestration:

   dashboard:

     hiddenWorkersPatterns:

       - "^apps-agent.*"

       - "^services-agent.*"

       - "^clearml-agent[^:]*$"

       - "^k8s:clearml-agent[^:]*$"

       # Copy the defaults above, then add your own patterns:

       - "^example.*"
```

- [Reporting Cluster Capacity](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_orch_dash_k8s/#reporting-cluster-capacity)
  - [GPU Capacity](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_orch_dash_k8s/#gpu-capacity)
  - [CPU Capacity](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_orch_dash_k8s/#cpu-capacity)
  - [Report Configuration](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_orch_dash_k8s/#report-configuration)
- [Customizing Worker IDs](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_orch_dash_k8s/#customizing-worker-ids)
  - [Configure Resource Groups Per Queue](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_orch_dash_k8s/#configure-resource-groups-per-queue)
  - [Hide Workers from the Orchestration Dashboard](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_orch_dash_k8s/#hide-workers-from-the-orchestration-dashboard)