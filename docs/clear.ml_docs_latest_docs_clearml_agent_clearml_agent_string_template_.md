---
url: "https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_string_template/"
title: "Custom Pod Manifests with String Templates | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_string_template/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

Enterprise Feature

Customizing pod manifests with string templates is only supported by a ClearML Enterprise Server.

When launching a Kubernetes Pod to execute a ClearML Task, the ClearML Agent supports string templates. Templates can reference
ClearML system objects and runtime configuration values, using the following format: `${CLEARML_<variable-specifier>:<default-value>}`.

For example, `"${CLEARML_TASK.project}"` will be replaced with the Task's project ID.

## Single-value Variables [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_string_template/\#single-value-variables "Direct link to Single-value Variables")

These variables resolve to a single value. You can use them directly in a template, without specifying any path.

For example `"${CLEARML_QUEUE_NAME}"` will be replaced with the name of the queue from which the task was pulled.

Available single-value variables:

- `QUEUE_NAME` \- Name of the queue from which the task is pulled
- `QUEUE_ID` \- ID of the queue from which the task is pulled
- `WORKER_ID` \- ID of the agent running the task
- `PROJECT_NAME` \- Task's project name
- `PROJECT_ID` \- Task's project ID

## Compound Variables (Path-Based) [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_string_template/\#compound-variables-path-based "Direct link to Compound Variables (Path-Based)")

These variables represent compound objects (mappings) for which you must specify a property path. Variable specifier is
in the format `VARIABLE.path.to.property`.

The following compound variables are supported:

- `TASK` \- Represents the ClearML Task object `data` property (see [`Task.get_task()`](https://clear.ml/docs/latest/docs/references/sdk/task#taskget_task)
on how to get a task object in the SDK)
- `USER` \- Represents the user data of the task's owner. In the ClearML SDK, use the following
command to get user data:





```text
task.session.send_request("users", "get_current_user").json()['data']['user']`
```

- `CONFIG` \- Represents the task’s configuration, as loaded from local configuration and associated
user vaults. To get a section of the configuration object in the ClearML SDK, use `task.session.config.get("<section-name>")`
where `section-name` can be `sdk`, `agent`, or any other existing configuration section. You can also use custom fields
that you added to your vaults.
- `USER_VAULTS` \- Similar to `CONFIG`, but only includes configuration loaded
from vaults applied for the user who’s the task owner.
- `PROVIDERS_INFO` \- Contains user data retrieved from the identity provider (SSO), if configured on the ClearML Server.

### List Type Variables [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_string_template/\#list-type-variables "Direct link to List Type Variables")

If a variable resolves to a list of simple values (e.g. string or number), it is expanded as a comma-separated list of values.

For example, if a task has the tags `["tag1", "tag2", "tag3"]`, the variable `${CLEARML_TASK.tags}` expands to `tag1,tag2,tag3`.

### Examples [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_string_template/\#examples "Direct link to Examples")

```text
${CLEARML_TASK.name}

${CLEARML_TASK.id}

${CLEARML_TASK.project}

${CLEARML_TASK.hyperparams.properties.user_key.value}
```

## Default Fallback [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_string_template/\#default-fallback "Direct link to Default Fallback")

Use a colon (`:`) to define a default fallback string for when the variable does not have a value.

For example:

```text
${CLEARML_TASK.hyperparams.properties.user_key.value:myDefault}
```

If `user_key` is not set, the string will resolve to `myDefault`.

## Filter Operators [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_string_template/\#filter-operators "Direct link to Filter Operators")

Templates also support filter operators that can modify the resulting value strings.

Filter operators are applied using a pipe (`|`) followed by the function name, in the format
`"${CLEARML_<variable-specifier>...|op1|op2|op3(x)}"`. This is also compatible with default fallbacks.

### Available Operators [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_string_template/\#available-operators "Direct link to Available Operators")

- `strip(chars)` \- Remove the listed characters. For example, `strip(abcd)` removes `a`, `b`, `c` or `d`. Empty argument
will strip white-spaces.
- `capitalize` \- Capitalize the string
- `lower` \- Convert string to lowercase
- `remove_newlines` \- Remove newlines
- `raw` \- Keep newlines

When no filter operators are specified, `remove_newlines` operator is applied by default.

## Using Templates in ClearML Agent Helm Chart [​](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_string_template/\#using-templates-in-clearml-agent-helm-chart "Direct link to Using Templates in ClearML Agent Helm Chart")

String templates customization is supported under the `basePodTemplate` and `templateOverrides` properties of the ClearML
Agent values.

For example:

```yaml
agentk8sglue:

  basePodTemplate:

    labels:

      myTaskName: "${CLEARML_TASK.name}"

      myProjectId: "${CLEARML_TASK.project}"

  queues:

    myQueueName:

      templateOverrides:

        labels:

          team: "green"

        env:

          - name: "userKey"

            value: "${CLEARML_USER_VAULTS.my_section.userKey:undefined_user_key}"
```

- [Single-value Variables](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_string_template/#single-value-variables)
- [Compound Variables (Path-Based)](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_string_template/#compound-variables-path-based)
  - [List Type Variables](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_string_template/#list-type-variables)
  - [Examples](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_string_template/#examples)
- [Default Fallback](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_string_template/#default-fallback)
- [Filter Operators](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_string_template/#filter-operators)
  - [Available Operators](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_string_template/#available-operators)
- [Using Templates in ClearML Agent Helm Chart](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_string_template/#using-templates-in-clearml-agent-helm-chart)