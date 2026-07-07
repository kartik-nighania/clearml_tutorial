---
url: "https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_services_mode/"
title: "Services Mode | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_services_mode/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

ClearML Agent supports a **Services Mode** where, as soon as a task is launched off of its queue, the agent moves on to the
next task without waiting for the previous one to complete. This mode is intended for running resource-sparse tasks that
are usually idling, such as periodic cleanup services or a [pipeline controller](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller).

To run a `clearml-agent` in services mode, run:

```bash
clearml-agent daemon --services-mode --queue services --create-queue --docker <docker_name> --cpu-only
```

To limit the number of simultaneous tasks run in services mode, pass the maximum number immediately after the
`--services-mode` option (for example: `--services-mode 5`).

Notes

- `services-mode` currently only supports Docker mode. Each service spins on its own Docker image.
- The default `clearml-server` configuration already runs a single `clearml-agent` in services mode that listens to the
`services` queue.

Launch a service task like any other task, by enqueuing it to the appropriate queue.

warning

Do not enqueue training or inference tasks into the services queue. They will put an unnecessary load on the server.

## Setting Server Credentials [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_services_mode/\#setting-server-credentials "Direct link to Setting Server Credentials")

Self-hosted [ClearML Server](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server) comes by default with a services queue.
By default, the server is open and does not require username and password, but it can be [password-protected](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_security#user-access-security).
In case it is password-protected, the services agent will need to be configured with server credentials (associated with a user).

To do that, set these environment variables on the ClearML Server machine with the appropriate credentials:

```text
CLEARML_API_ACCESS_KEY

CLEARML_API_SECRET_KEY
```

- [Setting Server Credentials](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_services_mode/#setting-server-credentials)