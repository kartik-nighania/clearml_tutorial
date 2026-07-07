---
url: "https://clear.ml/docs/latest/docs/configs/configuring_clearml/"
title: "Configuring ClearML | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/configs/configuring_clearml/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

ClearML can be tailored to your requirements by setting configurations in a variety of methods. All ClearML and ClearML
Agent configurations can be set in the `clearml.conf` file, which serves as the baseline configuration of both packages.
For detailed information about the configurable options in ClearML and ClearML Agent, see the
[Configuration File](https://clear.ml/docs/latest/docs/configs/clearml_conf) reference page.

ClearML supports reading configuration values from environment variables. Configuration entries specified
in this manner override values specified in the `clearml.conf` file. See [Environment Variables](https://clear.ml/docs/latest/docs/configs/env_vars) for parameter
specification.

Enterprise users can insert configuration snippets into the configuration vault. When enabled, configuration entries
from the vault are applied on top of the configuration specified in `clearml.conf`. New definitions will extend the
`clearml.conf` configurations, and existing definitions will be overridden. For more information, see [Configuration Vault](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_profile#configuration-vault).

The different ClearML configuration methods take precedence as summarized in the following list (higher ordered methods
override the lower ones):

1. Command-line arguments (e.g. [clearml-task](https://clear.ml/docs/latest/docs/apps/clearml_task#command-line-options), [clearml-agent](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_ref),
[clearml-session](https://clear.ml/docs/latest/docs/apps/clearml_session#command-line-options), [clearml-data](https://clear.ml/docs/latest/docs/clearml_data/clearml_data_cli)
arguments)
2. Environment variables
3. Configuration vault
4. Configuration file