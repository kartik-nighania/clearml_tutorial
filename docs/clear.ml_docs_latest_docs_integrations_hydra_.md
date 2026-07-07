---
url: "https://clear.ml/docs/latest/docs/integrations/hydra/"
title: "Hydra | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/integrations/hydra/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

tip

If you are not already using ClearML, see [ClearML Setup instructions](https://clear.ml/docs/latest/docs/clearml_sdk/clearml_sdk_setup).

[Hydra](https://github.com/facebookresearch/hydra) is a Python framework for managing task parameters. ClearML integrates seamlessly
with Hydra and automatically logs the `OmegaConf` which holds all the configuration files, as well as
values overridden during runtime.

All you have to do is add two lines of code:

```python
from clearml import Task

task = Task.init(task_name="<task_name>", project_name="<project_name>")
```

ClearML logs the OmegaConf as a blob and can be viewed in the
[WebApp](https://clear.ml/docs/latest/docs/webapp/webapp_overview), in the task's **CONFIGURATION > CONFIGURATION OBJECTS > OmegaConf** section.

![Hydra configuration](https://clear.ml/docs/latest/assets/images/integrations_hydra_configs-c0d369220a07e690bb23f5ddcca9de71.png#light-mode-only)![Hydra configuration](https://clear.ml/docs/latest/assets/images/integrations_hydra_configs_dark-6b227d72b7d1f36fde3d1ca534184534.png#dark-mode-only)

## Modifying Hydra Values [​](https://clear.ml/docs/latest/docs/integrations/hydra/\#modifying-hydra-values "Direct link to Modifying Hydra Values")

### Via Command Line [​](https://clear.ml/docs/latest/docs/integrations/hydra/\#via-command-line "Direct link to Via Command Line")

You can use Hydra's command line syntax to modify your OmegaConf: override, append, or remove configuration values:

- Override config value: `foo.bar=value`
- Append config value: `+foo.bar=value`
- Remove config value: `~foo.bar` or `~foo.bar=value`

See the [Hydra documentation](https://hydra.cc/docs/advanced/override_grammar/basic/#basic-override-syntax) for more information.

### Via UI [​](https://clear.ml/docs/latest/docs/integrations/hydra/\#via-ui "Direct link to Via UI")

In the UI, you can clone a task multiple times and modify it for execution by the [ClearML Agent](https://clear.ml/docs/latest/docs/clearml_agent).
The agent executes the code with the modifications you made in the UI, even overriding hardcoded values.

Clone your task, then modify your Hydra parameters via the UI in one of the following ways:

- Modify the OmegaConf directly:
1. In the task's **CONFIGURATION > HYPERPARAMETERS > HYDRA** section, set `_allow_omegaconf_edit_` to `True`
2. In the task's **CONFIGURATION > CONFIGURATION OBJECTS > OmegaConf** section, modify the OmegaConf values
- Add a task hyperparameter:


1. In the task's **CONFIGURATION > HYPERPARAMETERS > HYDRA** section, make sure `_allow_omegaconf_edit_` is set
     to `False`
2. In the same section, click `Edit`, which gives you the option to add parameters. Input parameters from the OmegaConf
     that you want to modify using dot notation. For example, if your OmegaConf looks like this:

```text
dataset:

    user: root

    main:

        number: 80
```

Specify the `number` parameter with `dataset.main.number`, then set its new value

Enqueue the customized task for execution. The task will use the new values during execution. If you use the
second option mentioned above, notice that the OmegaConf in **CONFIGURATION > CONFIGURATION OBJECTS > OmegaConf** changes
according to your added parameters.

## Code Example [​](https://clear.ml/docs/latest/docs/integrations/hydra/\#code-example "Direct link to Code Example")

See example which demonstrates integrating ClearML into script that uses Hydra [here](https://github.com/clearml/clearml/blob/master/examples/frameworks/hydra/hydra_example.py).

- [Modifying Hydra Values](https://clear.ml/docs/latest/docs/integrations/hydra/#modifying-hydra-values)
  - [Via Command Line](https://clear.ml/docs/latest/docs/integrations/hydra/#via-command-line)
  - [Via UI](https://clear.ml/docs/latest/docs/integrations/hydra/#via-ui)
- [Code Example](https://clear.ml/docs/latest/docs/integrations/hydra/#code-example)