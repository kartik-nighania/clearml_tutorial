---
url: "https://clear.ml/docs/latest/docs/getting_started/clearml_agent_docker_exec/"
title: "Building Executable Task Containers | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/getting_started/clearml_agent_docker_exec/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

## Exporting a Task into a Standalone Docker Container [​](https://clear.ml/docs/latest/docs/getting_started/clearml_agent_docker_exec/\#exporting-a-task-into-a-standalone-docker-container "Direct link to Exporting a Task into a Standalone Docker Container")

### Task Container [​](https://clear.ml/docs/latest/docs/getting_started/clearml_agent_docker_exec/\#task-container "Direct link to Task Container")

Build a Docker container that when launched executes a specific task, or a clone (copy) of that task.

- Build a Docker container that at launch will execute a specific Task:





```bash
clearml-agent build --id <task-id> --docker --target <new-docker-name> --entry-point reuse_task
```

- Build a Docker container that at launch will clone a Task specified by Task ID, and will execute the newly cloned Task:





```bash
clearml-agent build --id <task-id> --docker --target <new-docker-name> --entry-point clone_task
```

- Run built Docker by executing:





```bash
docker run <new-docker-name>
```


Check out [this tutorial](https://clear.ml/docs/latest/docs/guides/clearml_agent/executable_exp_containers) for building executable task
containers.

- [Exporting a Task into a Standalone Docker Container](https://clear.ml/docs/latest/docs/getting_started/clearml_agent_docker_exec/#exporting-a-task-into-a-standalone-docker-container)
  - [Task Container](https://clear.ml/docs/latest/docs/getting_started/clearml_agent_docker_exec/#task-container)