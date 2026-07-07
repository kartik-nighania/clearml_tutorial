---
url: "https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_nim_caching/"
title: "NIM Cache | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_nim_caching/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

NVIDIA NIM containers use a local cache directory for downloaded models. The cache location is controlled by the
`NIM_CACHE_PATH` environment variable.

When deploying the ClearML Agent on K8s, the volume information can be set through the overrides file. For example:

```text
agentk8sglue:

  basePodTemplate:

    env:

      - name: NIM_CACHE_PATH

        value: /opt/nim/.cache

    volumeMounts:

      - name: nim-cache

        mountPath: /opt/nim/.cache

    volumes:

      - name: nim-cache

        persistentVolumeClaim:

          claimName: nim-cache-pvc
```