---
url: "https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/appgw/"
title: "AI Application Gateway | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/appgw/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

Enterprise Feature

The AI Application Gateway is available under the ClearML Enterprise plan.

Services running through a cluster orchestrator such as Kubernetes or cloud hyperscaler require meticulous configuration
to make them available as these environments do not expose their networks to external users.

The ClearML AI Application Gateway facilitates setting up secure, authenticated access to jobs running on your compute
nodes from external networks.

Using the AI Application Gateway, services are allocated externally accessible, SSL secure network routes which provide
access in adherence to ClearML RBAC privileges. The AI Application Gateway supports HTTP/S as well as raw TCP routing.

The following ClearML UI applications make use of the AI Application Gateway to provide authenticated HTTPS access to
their instances:

- GPUaaS
  - [JupyterLab](https://clear.ml/docs/latest/docs/webapp/applications/apps_jupyter_lab)
  - [VScode](https://clear.ml/docs/latest/docs/webapp/applications/apps_vscode)
  - [SSH Session](https://clear.ml/docs/latest/docs/webapp/applications/apps_ssh_session)
- UI Dev
  - [Gradio launcher](https://clear.ml/docs/latest/docs/webapp/applications/apps_gradio)
  - [Streamlit launcher](https://clear.ml/docs/latest/docs/webapp/applications/apps_streamlit)
- Deploy
  - [vLLM Deployment](https://clear.ml/docs/latest/docs/webapp/applications/apps_model_deployment)
  - [Embedding Model Deployment](https://clear.ml/docs/latest/docs/webapp/applications/apps_embed_model_deployment)
  - [Llama.cpp Model Deployment](https://clear.ml/docs/latest/docs/webapp/applications/apps_llama_deployment)
  - [Containerized Application Launcher](https://clear.ml/docs/latest/docs/webapp/applications/apps_container_launcher)
  - [LLM UI](https://clear.ml/docs/latest/docs/webapp/applications/apps_llm_ui)

The AI Application Gateway requires an additional component to the ClearML Server deployment: the **ClearML App Gateway Router**.
If your ClearML Deployment does not have the App Gateway Router properly installed, these application instances may not be accessible.

#### Installation [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/appgw/\#installation "Direct link to Installation")

The App Gateway Router supports the following deployment options:

- [Docker Compose](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/appgw_install_compose)
- [Docker Compose for hosted servers](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/appgw_install_compose_hosted)
- [Kubernetes](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/appgw_install_k8s)

The deployment configuration specifies the external and internal address and port mappings for routing requests.