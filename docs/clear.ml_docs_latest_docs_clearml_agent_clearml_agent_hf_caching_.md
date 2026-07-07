---
url: "https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_hf_caching/"
title: "HuggingFace Cache | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_hf_caching/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

HuggingFace libraries provide their own cache mechanism for downloaded files. The HuggingFace cache location is controlled
by the `HF_HOME` environment variable.

When deploying the ClearML agent on K8s, the volume information can be set through the overrides file. For example:

```yaml
agentk8sglue:

  basePodTemplate:

    env:

      - name: HF_HOME

        value: "/root/.cache/huggingface"

    volumes:

      - name: hf-cache

        hostPath:

          path: /root/.clearml/cache/hf

          type: DirectoryOrCreate

    volumeMounts:

      - name: hf-cache

        mountPath: /root/.cache/huggingface
```