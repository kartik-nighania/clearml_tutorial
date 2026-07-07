---
url: "https://clear.ml/docs/latest/docs/getting_started/clearml_agent_base_docker/"
title: "Building Task Execution Environments in a Container | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/getting_started/clearml_agent_base_docker/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

### Base Container [​](https://clear.ml/docs/latest/docs/getting_started/clearml_agent_base_docker/\#base-container "Direct link to Base Container")

Build a container according to the execution environment of a specific task.

```bash
clearml-agent build --id <task-id> --docker --target <new-docker-name>
```

You can add the container as the base container image to a task, using one of the following methods:

- Using the **ClearML Web UI** \- See [Default Container](https://clear.ml/docs/latest/docs/webapp/webapp_exp_tuning#default-container).
- In the ClearML configuration file - Use the ClearML configuration file [`agent.default_docker`](https://clear.ml/docs/latest/docs/configs/clearml_conf#agentdefault_docker)
options.

Check out [this tutorial](https://clear.ml/docs/latest/docs/guides/clearml_agent/exp_environment_containers) for building a Docker container
replicating the execution environment of an existing task.

- [Base Container](https://clear.ml/docs/latest/docs/getting_started/clearml_agent_base_docker/#base-container)