---
url: "https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/monitoring_k8s/"
title: "Monitoring (K8s) | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/monitoring_k8s/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The following are general recommendations for monitoring your ClearML deployment on Kubernetes. These practices help
identify performance bottlenecks and maintain the system's reliability.

## API Server Logging and Analysis [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/monitoring_k8s/\#api-server-logging-and-analysis "Direct link to API Server Logging and Analysis")

Collect ClearML API Server logs using your preferred log aggregation solution. These logs can provide operational
insights, including:

- HTTP activity - Status codes, errors, and warning messages.
- API call details - Request ID, duration, version, and associated task for each endpoint.
- Usage tracking - API activity by caller
- Database performance - Latency measurements for APIs, including time spent per database call.

For more details on configuring API auditing, log adapters, and customizing which API endpoints and fields are logged,
see [Setting up API Auditing](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/api_audit).

## Kubernetes Metrics and Infrastructure Monitoring [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/monitoring_k8s/\#kubernetes-metrics-and-infrastructure-monitoring "Direct link to Kubernetes Metrics and Infrastructure Monitoring")

Monitor ClearML components at the Kubernetes level using standard metrics exporters and dashboards, such as Prometheus
and Grafana, to ensure all components are performing reliably under load.

Commonly tracked metrics include:

- Pod-level CPU, memory, and network utilization for:
  - API Server
  - File Server
  - ClearML Agents
  - Application Gateways
- Storage utilization of the File Server or external object storage.
- Task pod metrics for pods prefixed with `clearml-id-*`.
- Ingress performance - Track Ingress Controller metrics using common exporters and dashboards (e.g., NGINX).
- Database performance - Track database performance using community-supported exporters and dashboards.

- [API Server Logging and Analysis](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/monitoring_k8s/#api-server-logging-and-analysis)
- [Kubernetes Metrics and Infrastructure Monitoring](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/monitoring_k8s/#kubernetes-metrics-and-infrastructure-monitoring)