---
url: "https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_nvcr/"
title: "NVCR Access | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_nvcr/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

To allow ClearML Agents to access NVIDIA's container registry (`nvcr.io`), the machine’s Docker infrastructure must first be configured with valid NGC credentials.
This enables Agents to pull NVIDIA-provided containers, such as those used by the [NVIDIA NIM app](https://clear.ml/docs/latest/docs/webapp/applications/apps_nvidia_nim). The setup is
required once per worker node.

Configure Docker access to the `nvcr` repository on [bare-metal/VM](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_nvcr/#on-bare-metal--vm) or [Kubernetes](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_nvcr/#on-kubernetes).

## On Bare Metal / VM [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_nvcr/\#on-bare-metal--vm "Direct link to On Bare Metal / VM")

Execute the following command where the agent that will execute the app instance will be running (replace the password with a valid NGC API key):

```text
docker login nvcr.io --username '$oauthtoken' --password 'nvapi-**'
```

Password is provided with your `nvcr` account.

## On Kubernetes [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_nvcr/\#on-kubernetes "Direct link to On Kubernetes")

To make `nvcr` available to agents running on Kubernetes:

- Create an `nvcr-registry` secret in the same namespace where the agent is running. Replace:


  - `<NAMESPACE>` with the namespace where your ClearML Agent is deployed
  - `<USERNAME>` with your NVIDIA registry username
  - `<PASSWORD>` with your valid NGC API key


```text
kubectl create secret docker-registry nvcr-registry -n <NAMESPACE> \

  --docker-server=nvcr.io \

  --docker-username=<USERNAME> \

  --docker-password=<PASSWORD> \

  --docker-email=""
```

- Configure image pull secrets for the NVIDIA registry.
In your Agent Helm values override, add:





```text
imageCredentials:

    extraImagePullSecrets:

    - name: nvcr-registry
```

- [On Bare Metal / VM](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_nvcr/#on-bare-metal--vm)
- [On Kubernetes](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_nvcr/#on-kubernetes)