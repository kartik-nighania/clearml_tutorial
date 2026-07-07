---
url: "https://clear.ml/docs/latest/docs/deploying_models/"
title: "Model Deployment | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/deploying_models/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

Model deployment makes trained models accessible for real-world applications. ClearML provides a comprehensive suite of
tools for seamless model deployment, which supports
features including:

- Version control
- Automatic updates
- Performance monitoring

ClearML's offerings optimize the deployment process
while ensuring scalability and security. The solutions include:

- **Model Deployment UI Applications**(available under the Enterprise Plan) - The UI applications simplify deploying models
as network services through secure endpoints, providing an interface for managing deployments--no code required.
See more information about the following applications:

  - [vLLM Deployment](https://clear.ml/docs/latest/docs/webapp/applications/apps_model_deployment)
  - [Embedding Model Deployment](https://clear.ml/docs/latest/docs/webapp/applications/apps_embed_model_deployment)
  - [Llama.cpp Model Deployment](https://clear.ml/docs/latest/docs/webapp/applications/apps_llama_deployment)
  - [SGLang Model Deployment](https://clear.ml/docs/latest/docs/webapp/applications/apps_sglang)
  - [NVIDIA NIM](https://clear.ml/docs/latest/docs/webapp/applications/apps_nvidia_nim)
- **Command-line Interface** \- `clearml-serving` is a CLI for model deployment and orchestration.
It supports integration with Kubernetes clusters or custom container-based
solutions, offering flexibility for diverse infrastructure setups.
For more information, see [ClearML Serving](https://clear.ml/docs/latest/docs/clearml_serving/).

## Model Endpoint Monitoring [​](https://clear.ml/docs/latest/docs/deploying_models/\#model-endpoint-monitoring "Direct link to Model Endpoint Monitoring")

All deployed models are displayed in a unified **Model Endpoints** list in the UI. This
allows users to monitor endpoint activity and manage deployments from a single location.

For more information, see [Model Endpoints](https://clear.ml/docs/latest/docs/webapp/webapp_model_endpoints).

![Model Endpoints](https://clear.ml/docs/latest/assets/images/webapp_model_endpoints_monitor-7d3546f94f0a75e0a16771f78f2dc5a9.png#light-mode-only)![Model Endpoints](https://clear.ml/docs/latest/assets/images/webapp_model_endpoints_monitor_dark-d80b49745b836e6d6b810d476b2f4471.png#dark-mode-only)

- [Model Endpoint Monitoring](https://clear.ml/docs/latest/docs/deploying_models/#model-endpoint-monitoring)