---
url: "https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.9/"
title: "Version 6.9 | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.9/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

### clearml-enterprise-agent 6.9.13 [​](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.9/\#clearml-enterprise-agent-6913 "Direct link to clearml-enterprise-agent 6.9.13")

**New Features and Improvements**

- Set default Agent Worker ID to use the same cluster name prefix as the default Task Worker ID

### clearml-enterprise-agent 6.9.12 [​](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.9/\#clearml-enterprise-agent-6912 "Direct link to clearml-enterprise-agent 6.9.12")

**Bug Fixes**

- Fix init container not mounting custom secret credentials

### clearml-enterprise-agent 6.9.11 [​](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.9/\#clearml-enterprise-agent-6911 "Direct link to clearml-enterprise-agent 6.9.11")

**New Features and Improvements**

- Add option to override `serviceAccountName` for the agent

### clearml-enterprise-agent 6.9.10 [​](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.9/\#clearml-enterprise-agent-6910 "Direct link to clearml-enterprise-agent 6.9.10")

**New Features and Improvements**

- Add option to override `imagePullPolicy` for the agent

### clearml-enterprise-agent 6.9.9 [​](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.9/\#clearml-enterprise-agent-699 "Direct link to clearml-enterprise-agent 6.9.9")

**Bug Fixes**

- Fix default `taskWorkerIdOverride` value not correctly applying three-part format (`k8s:group:{task_id}`)

### clearml-enterprise-agent 6.9.8 [​](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.9/\#clearml-enterprise-agent-698 "Direct link to clearml-enterprise-agent 6.9.8")

**Bug Fixes**

- Fix default `taskWorkerIdOverride` value to `k8s:{task_id}`

### clearml-enterprise-agent 6.9.7 [​](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.9/\#clearml-enterprise-agent-697 "Direct link to clearml-enterprise-agent 6.9.7")

**New Features and Improvements**

- Set default value for `taskWorkerIdOverride` to `k8s:{worker_id}:{task_id}`

### clearml-enterprise-agent 6.9.6 [​](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.9/\#clearml-enterprise-agent-696 "Direct link to clearml-enterprise-agent 6.9.6")

**New Features and Improvements**

- Add default service account for task pods, created automatically by the Helm chart

### clearml-enterprise-agent 6.9.5 [​](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.9/\#clearml-enterprise-agent-695 "Direct link to clearml-enterprise-agent 6.9.5")

**New Features and Improvements**

- Remove Kubernetes maximum compatible version constraint

### clearml-enterprise-agent 6.9.4 [​](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.9/\#clearml-enterprise-agent-694 "Direct link to clearml-enterprise-agent 6.9.4")

**New Features and Improvements**

- Add support for `appsQueue` configuration
- Update image version to `1.30-2.0.0rc2-243`
- Move image repository from `allegroai` to `clearml`

### clearml-enterprise-agent 6.9.3 [​](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.9/\#clearml-enterprise-agent-693 "Direct link to clearml-enterprise-agent 6.9.3")

**New Features and Improvements**

- Update Helm repository to OCI registry

- [clearml-enterprise-agent 6.9.13](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.9/#clearml-enterprise-agent-6913)
- [clearml-enterprise-agent 6.9.12](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.9/#clearml-enterprise-agent-6912)
- [clearml-enterprise-agent 6.9.11](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.9/#clearml-enterprise-agent-6911)
- [clearml-enterprise-agent 6.9.10](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.9/#clearml-enterprise-agent-6910)
- [clearml-enterprise-agent 6.9.9](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.9/#clearml-enterprise-agent-699)
- [clearml-enterprise-agent 6.9.8](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.9/#clearml-enterprise-agent-698)
- [clearml-enterprise-agent 6.9.7](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.9/#clearml-enterprise-agent-697)
- [clearml-enterprise-agent 6.9.6](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.9/#clearml-enterprise-agent-696)
- [clearml-enterprise-agent 6.9.5](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.9/#clearml-enterprise-agent-695)
- [clearml-enterprise-agent 6.9.4](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.9/#clearml-enterprise-agent-694)
- [clearml-enterprise-agent 6.9.3](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.9/#clearml-enterprise-agent-693)