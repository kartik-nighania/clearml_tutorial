---
url: "https://clear.ml/docs/latest/docs/webapp/applications/apps_overview/"
title: "ClearML Applications | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/webapp/applications/apps_overview/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

Pro Plan Offering

ClearML Applications are available under the ClearML Pro plan.

Use ClearML's GUI Applications to manage ML workloads and automatically run your recurring workflows without any coding.

![Apps page](https://clear.ml/docs/latest/assets/images/apps_overview_page-3731663709ae2268762e7c8f7e8c6307.png#light-mode-only)![Apps page](https://clear.ml/docs/latest/assets/images/apps_overview_page_dark-e26534445f1a54604bcd145944698a49.png#dark-mode-only)

Configure and launch app instances, then track their execution from the app dashboard.

ClearML provides applications in a range of categories to enhance your workflows:

### General [​](https://clear.ml/docs/latest/docs/webapp/applications/apps_overview/\#general "Direct link to General")

Applications for automating and optimizing workflows, and monitoring project performance:

- [**Hyperparameter Optimization**](https://clear.ml/docs/latest/docs/webapp/applications/apps_hpo) \- Find the parameter values that yield the best performing models
- **Nvidia Clara** \- Train models using Nvidia's Clara framework
- [**Project Dashboard**](https://clear.ml/docs/latest/docs/webapp/applications/apps_dashboard) \- High-level project monitoring with Slack alerts
- [**Task Scheduler**](https://clear.ml/docs/latest/docs/webapp/applications/apps_task_scheduler) \- Schedule tasks for one-shot and/or periodic execution at specified times (available under ClearML Enterprise Plan)
- [**Trigger Manager**](https://clear.ml/docs/latest/docs/webapp/applications/apps_trigger_manager) \- Define tasks to be run when predefined events occur (available under ClearML Enterprise Plan)

### AI Dev [​](https://clear.ml/docs/latest/docs/webapp/applications/apps_overview/\#ai-dev "Direct link to AI Dev")

Applications for deploying AI development environments on remote machines:

- [**SSH Session**](https://clear.ml/docs/latest/docs/webapp/applications/apps_ssh_session) \- Launch a full development environment on a remote machine with a
detached interactive SSH session (available under ClearML Enterprise Plan)
- [**Jupyter Lab**](https://clear.ml/docs/latest/docs/webapp/applications/apps_jupyter_lab) \- Launch a Jupyter Lab session on a remote machine (available under ClearML Enterprise Plan)
- [**VS Code**](https://clear.ml/docs/latest/docs/webapp/applications/apps_vscode) \- Launch a VS Code session on a remote machine (available under ClearML Enterprise Plan)

### Databases [​](https://clear.ml/docs/latest/docs/webapp/applications/apps_overview/\#databases "Direct link to Databases")

Applications for deploying standalone, detachable vector database sessions:

- [**Milvus DB Session**](https://clear.ml/docs/latest/docs/webapp/applications/apps_milvus) \- Launch a detachable [Milvus](https://github.com/milvus-io/milvus) database session (available under ClearML Enterprise Plan)
- [**Qdrant DB Session**](https://clear.ml/docs/latest/docs/webapp/applications/apps_qdrant) \- Launch a detachable [Qdrant](https://github.com/qdrant/qdrant) database session (available under ClearML Enterprise Plan)

### UI Dev [​](https://clear.ml/docs/latest/docs/webapp/applications/apps_overview/\#ui-dev "Direct link to UI Dev")

Applications for deploying user interfaces for models:

- [**Gradio Launcher**](https://clear.ml/docs/latest/docs/webapp/applications/apps_gradio) \- Create visual web interfaces for your models with Gradio (available under ClearML Enterprise Plan)
- [**Streamlit Launcher**](https://clear.ml/docs/latest/docs/webapp/applications/apps_streamlit) \- Create visual web interfaces for your models with Streamlit (available under ClearML Enterprise Plan)

### Deploy [​](https://clear.ml/docs/latest/docs/webapp/applications/apps_overview/\#deploy "Direct link to Deploy")

Applications for deploying machine learning models as scalable, secure services:

- [**Embedding Model Deployment**](https://clear.ml/docs/latest/docs/webapp/applications/apps_embed_model_deployment) \- Deploy embedding models as networking services over a secure endpoint (available under ClearML Enterprise Plan)
- [**vLLM Model Deployment**](https://clear.ml/docs/latest/docs/webapp/applications/apps_model_deployment) \- Deploy LLMs as networking services over a secure endpoint (available under ClearML Enterprise Plan)
- [**Llama.cpp**](https://clear.ml/docs/latest/docs/webapp/applications/apps_llama_deployment) \- Deploy LLMs in GGUF format using [`llama.cpp`](https://github.com/ggerganov/llama.cpp) as networking services over a secure endpoint (available under ClearML Enterprise Plan)
- [**SGLang Model Deployment**](https://clear.ml/docs/latest/docs/webapp/applications/apps_sglang) \- Deploy LLMs using [SGLang](https://docs.sglang.ai/) as networking services over a secure endpoint (available under ClearML Enterprise Plan)
- [**Containerized Application Launcher**](https://clear.ml/docs/latest/docs/webapp/applications/apps_container_launcher) \- Launch and application containers with persistent workspaces and flexible networking (available under ClearML Enterprise Plan)
- [**LLM UI**](https://clear.ml/docs/latest/docs/webapp/applications/apps_llm_ui) \- Launch a visual chat interface to a deployed model (available under ClearML Enterprise Plan)
- **MCP Server Deploy** \- Deploy remote MCP (Model Context Protocol) servers as containerized services over a secure network endpoint (available under ClearML Enterprise Plan).

### NVAIE [​](https://clear.ml/docs/latest/docs/webapp/applications/apps_overview/\#nvaie "Direct link to NVAIE")

Applications utilizing NVIDIA AI Enterprise's (NVAIE) suite of software tools:

- [**NIM**](https://clear.ml/docs/latest/docs/webapp/applications/apps_nvidia_nim) \- Launch [NVIDIA NIM](https://developer.nvidia.com/nim) models through their specific containers (available under ClearML Enterprise Plan)
- **NVIDIA Dynamo** \- Deploy NVIDIA Dynamo's distributed LLM inference pipeline as a multi-service stack for high-throughput model serving (available under ClearML Enterprise Plan)
- **NVIDIA NIM RAG** \- Launch an Nvidia NIM RAG session (available under ClearML Enterprise Plan)

### Cluster [​](https://clear.ml/docs/latest/docs/webapp/applications/apps_overview/\#cluster "Direct link to Cluster")

Applications for deploying and managing scalable compute clusters for distributed workloads:

- **Deploy Slurm Cluster** \- Deploy a dynamic Slurm cluster for HPC and distributed workloads (available under ClearML Enterprise Plan)
- **K3s Deployment** \- Deploy a Kubernetes cluster with a configurable number of worker nodes (available under ClearML Enterprise Plan)
- [**Multi-Node Trainer**](https://clear.ml/docs/latest/docs/webapp/applications/apps_multi_node_trainer) \- Orchestrate distributed training across multiple nodes (available under ClearML Enterprise Plan)

Autoscalers

Autoscaling ( [AWS Autoscaler](https://clear.ml/docs/latest/docs/webapp/applications/apps_aws_autoscaler) and [GCP Autoscaler](https://clear.ml/docs/latest/docs/webapp/applications/apps_gcp_autoscaler))
was previously available through the Applications page. The autoscaler functionality has been moved to the [Orchestration page](https://app.clear.ml/workers-and-queues/autoscalers)
in the WebApp.

## App Pages Layout [​](https://clear.ml/docs/latest/docs/webapp/applications/apps_overview/\#app-pages-layout "Direct link to App Pages Layout")

Each application's page is split into two sections:

- App Instance List - Launch new app instances and view previously launched instances. Click on an instance to view its
dashboard. Hover over it to access the [app instance actions](https://clear.ml/docs/latest/docs/webapp/applications/apps_overview/#app-instance-actions).
- App Instance Dashboard - The main section of the app page: displays the selected app instance's status and results.
Use the search bar ![Magnifying glass](https://clear.ml/docs/latest/icons/ico-search.svg)
to quickly find an app instance by name.

![App format](https://clear.ml/docs/latest/assets/images/apps_format_overview-79471a6d32c8e413ca593b6e7e4adf81.png#light-mode-only)![App format](https://clear.ml/docs/latest/assets/images/apps_format_overview_dark-a4341e670545794566ad535036cb4f87.png#dark-mode-only)

## Launching an App Instance [​](https://clear.ml/docs/latest/docs/webapp/applications/apps_overview/\#launching-an-app-instance "Direct link to Launching an App Instance")

1. Choose the desired app
2. Click `Launch New`![Add new](https://clear.ml/docs/latest/icons/ico-add.svg) to open the app's configuration form
3. Fill in the configuration details
4. **Launch**

Configuration shortcuts

You can also launch an app instance with the configuration of a previously launched instance:

- Cloning a previously launched app instance will open the instance launch form with the original instance's configuration
prefilled.
- Importing an app configuration file. You can export an existing app instance's configuration as a JSON file when
viewing its configuration.

The prefilled instance launch form can be edited before starting the new app instance.

## App Instance Actions [​](https://clear.ml/docs/latest/docs/webapp/applications/apps_overview/\#app-instance-actions "Direct link to App Instance Actions")

Access app instance actions, by right-clicking an instance, or through the menu button ![Dot menu](https://clear.ml/docs/latest/icons/ico-dots-v-menu.svg) (available on hover).

![App context menu](https://clear.ml/docs/latest/assets/images/app_context_menu-624f063d56a074d845bc574adc849c4a.png#light-mode-only)![App context menu](https://clear.ml/docs/latest/assets/images/app_context_menu_dark-6de0d6542ff982e4378a2ac7529ebe38.png#dark-mode-only)

- **Rename** \- Rename the instance
- **Configuration** \- View an instance's configuration
- **Export Configuration** \- Export the app instance configuration as a JSON file, which you can later import to create
a new instance with the same configuration
- **Stop** \- Shutdown the instance
- **Clone** \- Launch a new instance with same configuration prefilled
- **Delete** \- Delete the instance

## Instance List Actions [​](https://clear.ml/docs/latest/docs/webapp/applications/apps_overview/\#instance-list-actions "Direct link to Instance List Actions")

Access the instance list actions by clicking the action menu (![Dot menu](https://clear.ml/docs/latest/icons/ico-dots-v-menu.svg))
on the instance list header:

![Instance list actions](https://clear.ml/docs/latest/assets/images/apps_instance_list_actions-ca05061beb5366bc59402ca41714630c.png#light-mode-only)![Instance list actions](https://clear.ml/docs/latest/assets/images/apps_instance_list_actions_dark-4e3cdab673ed10b3fb31511feec1d9df.png#dark-mode-only)

- **Import Configuration** \- Import an app instance's configuration file. This opens the app instance launch form
prefilled according to the imported file. You can modify the configuration before launching the instance.

- **Clear Completed** \- Delete all app instances that have completed their execution. This action only
deletes instances in the current instance list view (i.e. My instances / All).


- [General](https://clear.ml/docs/latest/docs/webapp/applications/apps_overview/#general)
- [AI Dev](https://clear.ml/docs/latest/docs/webapp/applications/apps_overview/#ai-dev)
- [Databases](https://clear.ml/docs/latest/docs/webapp/applications/apps_overview/#databases)
- [UI Dev](https://clear.ml/docs/latest/docs/webapp/applications/apps_overview/#ui-dev)
- [Deploy](https://clear.ml/docs/latest/docs/webapp/applications/apps_overview/#deploy)
- [NVAIE](https://clear.ml/docs/latest/docs/webapp/applications/apps_overview/#nvaie)
- [Cluster](https://clear.ml/docs/latest/docs/webapp/applications/apps_overview/#cluster)
- [App Pages Layout](https://clear.ml/docs/latest/docs/webapp/applications/apps_overview/#app-pages-layout)
- [Launching an App Instance](https://clear.ml/docs/latest/docs/webapp/applications/apps_overview/#launching-an-app-instance)
- [App Instance Actions](https://clear.ml/docs/latest/docs/webapp/applications/apps_overview/#app-instance-actions)
- [Instance List Actions](https://clear.ml/docs/latest/docs/webapp/applications/apps_overview/#instance-list-actions)