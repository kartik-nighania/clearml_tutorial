---
url: "https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/bitnami_mongo_mitigation/"
title: "MongoDB 7 Latest Patch | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/bitnami_mongo_mitigation/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

Bitnami has discontinued updates for their open MongoDB images, which earlier ClearML charts made use of.

To update to the latest patched MongoDB version 7, you can use the official MongoDB image by modifying your `clearml-values.override.yaml` as follows:

```yaml
mongodb:

  image:

    repository: mongo

    tag: 7.0.28

  persistence:

    mountPath: /data/db
```

Deployment Mode Limitation

This configuration is only compatible with deployments that use the default `mongodb.architecture` value set to `standalone`.

You cannot apply this configuration if your chart already uses a different MongoDB architecture setting. Attempting to change the architecture after deployment may result in **DATA LOSS**.