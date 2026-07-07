---
url: "https://clear.ml/docs/latest/docs/webapp/applications/apps_llm_ui/"
title: "LLM UI | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/webapp/applications/apps_llm_ui/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

Enterprise Feature

The LLM UI application is available under the ClearML Enterprise plan.

Use the ClearML LLM UI application to launch a visual chat interface to a deployed model.

The app instance uses endpoints of models deployed through the ClearML [vLLM Model Deployment](https://clear.ml/docs/latest/docs/webapp/applications/apps_model_deployment),
[Llama.cpp Model Deployment](https://clear.ml/docs/latest/docs/webapp/applications/apps_llama_deployment), and [SGLang Model Deployment](https://clear.ml/docs/latest/docs/webapp/applications/apps_sglang) apps. In the interface, you must
first select the model to query. The interface provides controls for adjusting generation parameters such as temperature,
max tokens, and stop sequences. For detailed usage and customization options, see the
[Open WebUI documentation](https://docs.openwebui.com/).

AI Application Gateway

The LLM UI app makes use of the App Gateway Router which implements a secure, authenticated network endpoint for the
model. If the ClearML AI Application Gateway is not available, the model endpoint might not be accessible. For more
information, see [AI Application Gateway](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/appgw).

After launching an LLM UI instance, its dashboard displays the following:

- Status indicator
  - ![Active instance](https://clear.ml/docs/latest/icons/ico-llm-ui-active.svg) \- App instance is running and is actively in use
  - ![Loading instance](https://clear.ml/docs/latest/icons/ico-llm-ui-loading.svg) \- App instance is setting up
  - ![Idle instance](https://clear.ml/docs/latest/icons/ico-llm-ui-idle.svg) \- App instance is idle
  - ![Stopped instance](https://clear.ml/docs/latest/icons/ico-llm-ui-stopped.svg) \- App instance is stopped
- Idle time – Time since the last user activity
- Restored workspace - If the session was restored, the previous session's ID is shown
- Current session ID
- Sharable Link – Publicly accessible URL to access the model’s chat interface (available only when the instance is running)
- Chat window (available only when the instance is running) - For detailed usage and customization options, see the
[Open WebUI documentation](https://docs.openwebui.com/).
- Console log – Displays setup progress, status changes, error messages, etc.

![LLM UI dashboard](https://clear.ml/docs/latest/assets/images/apps_llm_ui-2d6bde2ef19c5841fac35f1fd7bd037f.png#light-mode-only)![LLM UI dashboard](https://clear.ml/docs/latest/assets/images/apps_llm_ui_dark-a6b1a27b75ca162a9540608f934bb57a.png#dark-mode-only)

## LLM UI Instance Configuration [​](https://clear.ml/docs/latest/docs/webapp/applications/apps_llm_ui/\#llm-ui-instance-configuration "Direct link to LLM UI Instance Configuration")

When configuring a new LLM UI instance, you can fill in the required parameters or reuse the
configuration of a previously launched instance.

Launch an app instance with the configuration of a previously launched instance using one of the following options:

- Cloning a previously launched app instance will open the instance launch form with the original instance's
configuration prefilled.
- Importing an app configuration file. You can export the configuration of a previously launched instance as a JSON file
when viewing its configuration.

The prefilled configuration form can be edited before launching the new app instance.

To configure a new app instance, click `Launch New`![Add new](https://clear.ml/docs/latest/icons/ico-add.svg)
to open the app's configuration form.

### Configuration Options [​](https://clear.ml/docs/latest/docs/webapp/applications/apps_llm_ui/\#configuration-options "Direct link to Configuration Options")

note

Administrators can [customize](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/app_launch_form_custom) the launch form and
modify field names and/or available options and defaults.

This section describes the default configuration provided by ClearML.

- Instance Name – Name for the LLM UI app instance. This will appear in the instance list
- Service Project (Access Control) – The ClearML project where the app instance is created. Access is determined by
project-level permissions (i.e. users with read access can use the app).
- Queue: The queue serviced by the ClearML
Agent which will execute the application instance.
- RAG Embedding Model: The embedding model is used by the application to create embeddings to facilitate RAG for documents
you add to your workspace (See [Knowledge Bases](https://clear.ml/docs/latest/docs/webapp/applications/apps_llm_ui/#using-knowledge-bases-for-rag)). These entries can be edited in the running instance UI.

  - Embedding Model Endpoint URL: The embedding model endpoint URL (See [Embedding Model Deployment app](https://clear.ml/docs/latest/docs/webapp/applications/apps_embed_model_deployment)).
  - Model Name: The embedding model's name
- Restore LLM UI ID - Specify a LLM UI ID to be restored
- Idle options:
  - Idle Time Limit (Hours) - Maximum idle time after which the app instance will shut down
  - Last Action Report Interval (Seconds) - Frequency at which last activity is reported. Prevents idle shutdown while still active.

![LLM UI launch form](https://clear.ml/docs/latest/assets/images/apps_llm_ui_wizard-854e993396854b4385f54e9c9109a29c.png#light-mode-only)![LLM UI launch form](https://clear.ml/docs/latest/assets/images/apps_llm_ui_wizard_dark-098126c8332baa82a8338f6036c695a3.png#dark-mode-only)

## Using Knowledge Bases for RAG [​](https://clear.ml/docs/latest/docs/webapp/applications/apps_llm_ui/\#using-knowledge-bases-for-rag "Direct link to Using Knowledge Bases for RAG")

You can improve your model’s responses by providing context through **Knowledge Bases**. This allows the LLM to consider
your uploaded documents as part of the queries.

1. In the model UI, click **Menu > Workspace > Knowledge > + (Create Knowledge Base)**
2. In the `Create Knowledge Base` window:

   - Name and describe the knowledge base.
   - Click **Create Knowledge**
3. Drag and drop `.pdf` or `.txt` files
4. Click **New Chat**
5. In the chat, reference a Knowledge Base by typing `#<YourKnowledgeBaseName>`.

The LLM leverages the referenced knowledge base to retrieve relevant information, then uses that information to generate more accurate and contextually appropriate responses.

- [LLM UI Instance Configuration](https://clear.ml/docs/latest/docs/webapp/applications/apps_llm_ui/#llm-ui-instance-configuration)
  - [Configuration Options](https://clear.ml/docs/latest/docs/webapp/applications/apps_llm_ui/#configuration-options)
- [Using Knowledge Bases for RAG](https://clear.ml/docs/latest/docs/webapp/applications/apps_llm_ui/#using-knowledge-bases-for-rag)