---
url: "https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.13/"
title: "Version 6.13 | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.13/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

### clearml-enterprise-agent 6.13.9 [​](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.13/\#clearml-enterprise-agent-6139 "Direct link to clearml-enterprise-agent 6.13.9")

**Bug Fixes**

- Fix `ClusterRole` and `ClusterRoleBinding` name collisions in clusters with multiple agent deployments.
Resource names now include the release namespace to ensure uniqueness

### clearml-enterprise-agent 6.13.8 [​](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.13/\#clearml-enterprise-agent-6138 "Direct link to clearml-enterprise-agent 6.13.8")

**New Features and Improvements**

- Report tasks as Aborted when a pending pod is evicted in the Kubernetes backend

**Bug Fixes**

- Fix Multi-Node task scheduling not counting GPUs from pods across all namespaces

### clearml-enterprise-agent 6.13.7 [​](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.13/\#clearml-enterprise-agent-6137 "Direct link to clearml-enterprise-agent 6.13.7")

**Bug Fixes**

- Fix experiment log rendering issues with Kubernetes events:
  - Fix Kubernetes events being concatenated instead of rendered on separate lines
  - Fix Kubernetes events that occur within the same millisecond not preserving their original arrival order
  - Fix duplicate Kubernetes pod status entries in logs

### clearml-enterprise-agent 6.13.6 [​](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.13/\#clearml-enterprise-agent-6136 "Direct link to clearml-enterprise-agent 6.13.6")

**New Features and Improvements**

- Improve `nodeSelector` description for CPU discovery

### clearml-enterprise-agent 6.13.5 [​](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.13/\#clearml-enterprise-agent-6135 "Direct link to clearml-enterprise-agent 6.13.5")

**New Features and Improvements**

- Add option to configure delay before deleting completed task pods/jobs via `agentk8sglue.completedPodDeletionDelayMinutes`
- Add support for GPU fraction usage reporting via pod annotation

### clearml-enterprise-agent 6.13.4 [​](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.13/\#clearml-enterprise-agent-6134 "Direct link to clearml-enterprise-agent 6.13.4")

**New Features and Improvements**

- Make fileserver reference optional for the agent
- Update default URLs in Helm values to use `nip.io`

### clearml-enterprise-agent 6.13.3 [​](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.13/\#clearml-enterprise-agent-6133 "Direct link to clearml-enterprise-agent 6.13.3")

**New Features and Improvements**

- Update image version to `1.31-3.0.2rc0-440`

### clearml-enterprise-agent 6.13.2 [​](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.13/\#clearml-enterprise-agent-6132 "Direct link to clearml-enterprise-agent 6.13.2")

**New Features and Improvements**

- Update image version to `1.31-3.0.1-439`
- Update bootstrap image version to `1.0.1-34`

### clearml-enterprise-agent 6.13.1 [​](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.13/\#clearml-enterprise-agent-6131 "Direct link to clearml-enterprise-agent 6.13.1")

**Bug Fixes**

- Improve internal chart CI

### clearml-enterprise-agent 6.13.0 [​](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.13/\#clearml-enterprise-agent-6130 "Direct link to clearml-enterprise-agent 6.13.0")

**New Features and Improvements**

- Add `bootstrap` support: when enabled, agent pre-packages compiled Python and Git binaries on
the host and mounts them directly into containers at launch, reducing boot time

- [clearml-enterprise-agent 6.13.9](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.13/#clearml-enterprise-agent-6139)
- [clearml-enterprise-agent 6.13.8](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.13/#clearml-enterprise-agent-6138)
- [clearml-enterprise-agent 6.13.7](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.13/#clearml-enterprise-agent-6137)
- [clearml-enterprise-agent 6.13.6](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.13/#clearml-enterprise-agent-6136)
- [clearml-enterprise-agent 6.13.5](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.13/#clearml-enterprise-agent-6135)
- [clearml-enterprise-agent 6.13.4](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.13/#clearml-enterprise-agent-6134)
- [clearml-enterprise-agent 6.13.3](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.13/#clearml-enterprise-agent-6133)
- [clearml-enterprise-agent 6.13.2](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.13/#clearml-enterprise-agent-6132)
- [clearml-enterprise-agent 6.13.1](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.13/#clearml-enterprise-agent-6131)
- [clearml-enterprise-agent 6.13.0](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.13/#clearml-enterprise-agent-6130)