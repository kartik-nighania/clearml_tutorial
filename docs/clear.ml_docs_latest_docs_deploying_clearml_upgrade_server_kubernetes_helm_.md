---
url: "https://clear.ml/docs/latest/docs/deploying_clearml/upgrade_server_kubernetes_helm/"
title: "Kubernetes | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/deploying_clearml/upgrade_server_kubernetes_helm/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

**To update to the latest version of the Helms chart,** execute the following:

```bash
helm repo update

helm upgrade clearml clearml/clearml
```

**To change the values in an existing installation,** execute the following:

```bash
helm upgrade clearml clearml/clearml --version <CURRENT CHART VERSION> -f custom_values.yaml
```

See the [clearml-helm-charts repository](https://github.com/clearml/clearml-helm-charts/tree/main/charts/clearml#local-environment)
to view the up-to-date charts.

tip

When changing values, make sure to set the chart version (`--version`) to avoid a chart update. Keeping separate procedures
between version and value updates is recommended to separate potential concerns.