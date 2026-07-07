---
url: "https://clear.ml/docs/latest/docs/release_notes/clearml_agent/ver_0_13/"
title: "Version 0.13 | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/release_notes/clearml_agent/ver_0_13/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

important

**Trains** is now **ClearML**.

### Trains Agent 0.13.3 [​](https://clear.ml/docs/latest/docs/release_notes/clearml_agent/ver_0_13/\#trains-agent-0133 "Direct link to Trains Agent 0.13.3")

**Features and Bug Fixes**

- Allow providing queue names instead of queue IDs in daemon mode.
- Improve Docker mode:
  - Support running as a specific user inside a docker using the `TRAINS_AGENT_EXEC_USER` environment flag.
  - Pass the correct GPU limit when skipping gpus flag.
  - Add the `--force-current-version` daemon command-line flag.
- Add K8s/trains glue service example.
- Add K8s support in daemon mode.
  - Running inside a K8s pod.
  - Mounting dockerized experiment folders to host.
  - Allow a specific network for the docker.
- Add default storage environment vars (for AWS, GS and Azure) to generated agent configuration.
- Improve Unicode/UTF stdout handling.

### Trains Agent 0.13.0 [​](https://clear.ml/docs/latest/docs/release_notes/clearml_agent/ver_0_13/\#trains-agent-0130 "Direct link to Trains Agent 0.13.0")

**Features**

- Add support for Docker pre-installed pytorch versions that do not exist on PyPI/PyTorch.org.
- Add AWS dynamic cluster management service.
- Add support for various event query endpoints in APIClient.
- Improve the configuration wizard.

- [Trains Agent 0.13.3](https://clear.ml/docs/latest/docs/release_notes/clearml_agent/ver_0_13/#trains-agent-0133)
- [Trains Agent 0.13.0](https://clear.ml/docs/latest/docs/release_notes/clearml_agent/ver_0_13/#trains-agent-0130)