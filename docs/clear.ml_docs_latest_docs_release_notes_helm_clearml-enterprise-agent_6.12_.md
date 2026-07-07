---
url: "https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.12/"
title: "Version 6.12 | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.12/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

### clearml-enterprise-agent 6.12.4 [​](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.12/\#clearml-enterprise-agent-6124 "Direct link to clearml-enterprise-agent 6.12.4")

**New Features and Improvements**

- Update image version to `v1.31-3.0.0-427`

**Bug Fixes**

- Fix `update-ca-certificates` failing on hardened rootless image

### clearml-enterprise-agent 6.12.3 [​](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.12/\#clearml-enterprise-agent-6123 "Direct link to clearml-enterprise-agent 6.12.3")

Breaking Changes

The agent image in chart v6.12.3 now runs as a non-root user. Depending on your configuration, some changes to your
`values.yaml` may be required before upgrading. See [Upgrading to Agent Chart v6.12.3 or greater](https://clear.ml/docs/latest/docs/clearml_agent/enterprise_agent_upgrade_6_12_3)
for details.

**New Features and Improvements**

- Set agent image to run as non-root user

### clearml-enterprise-agent 6.12.2 [​](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.12/\#clearml-enterprise-agent-6122 "Direct link to clearml-enterprise-agent 6.12.2")

**New Features and Improvements**

- Update image version `1.30-2.0.9rc1-406`

### clearml-enterprise-agent 6.12.1 [​](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.12/\#clearml-enterprise-agent-6121 "Direct link to clearml-enterprise-agent 6.12.1")

**New Features and Improvements**

- Update image version `1.30-2.0.8rc2-405`
- Add support for Dynamic Multi-Node scheduling, allowing individual tasks to define their own GPU and node requirements via task properties

### clearml-enterprise-agent 6.12.0 [​](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.12/\#clearml-enterprise-agent-6120 "Direct link to clearml-enterprise-agent 6.12.0")

**New Features and Improvements**

- Add support for CPU reporting and automatic CPU node discovery in the Orchestration Dashboard

- [clearml-enterprise-agent 6.12.4](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.12/#clearml-enterprise-agent-6124)
- [clearml-enterprise-agent 6.12.3](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.12/#clearml-enterprise-agent-6123)
- [clearml-enterprise-agent 6.12.2](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.12/#clearml-enterprise-agent-6122)
- [clearml-enterprise-agent 6.12.1](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.12/#clearml-enterprise-agent-6121)
- [clearml-enterprise-agent 6.12.0](https://clear.ml/docs/latest/docs/release_notes/helm/clearml-enterprise-agent/6.12/#clearml-enterprise-agent-6120)