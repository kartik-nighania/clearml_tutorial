---
url: "https://clear.ml/docs/latest/docs/webapp/webapp_exp_tuning/"
title: "Tuning Tasks | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/webapp/webapp_exp_tuning/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

Tune task parameters and edit their execution details, then execute the tuned tasks on local or remote machines.

## To Tune a Task and Execute it Remotely: [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_tuning/\#to-tune-a-task-and-execute-it-remotely "Direct link to To Tune a Task and Execute it Remotely:")

1. Locate the task.
   - On the Project Dashboard:
     - Click on a task in **RECENT TASKS**
     - In RECENT PROJECTS **>** click on a project card **>** click task
     - In RECENT PROJECTS **\> VIEW ALL** **>** click the project card **>** click task
     - In RECENT PROJECTS **>** click **VIEW ALL** **>** click project card or **All Tasks** card **>** click task
2. Clone the task. In the task table:


1. Click **Clone**, which opens the **Clone task** modal.
2. Provide new task's details:
      - Project: Select the ClearML project in which the new task will be created, or create a new one. To search for a
        project, start typing the project name. To create a new project, type a new name and click **Create New**.
      - Name: New task's name
      - Description (Optional): Brief description of the task.
3. Click **CLONE**.

The new task is created and has a _Draft_ status.

3. Edit the task. See [modifying tasks](https://clear.ml/docs/latest/docs/webapp/webapp_exp_tuning/#modifying-tasks).

4. Enqueue the task for execution. Right-click the task **>** **Enqueue** **>** Select a queue **>** **ENQUEUE**.

The task's status becomes _Pending_. When the worker assigned to the queue fetches the task, its
status becomes _Running_. The task can now be tracked and its results visualized.


## Modifying Tasks [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_tuning/\#modifying-tasks "Direct link to Modifying Tasks")

Tasks whose status is _Draft_ are editable (see the [user properties](https://clear.ml/docs/latest/docs/webapp/webapp_exp_tuning/#user-properties) exception). In the **ClearML**
**Web UI**, edit any of the following

- [Source code](https://clear.ml/docs/latest/docs/webapp/webapp_exp_tuning/#source-code)
- [Output destination for artifacts](https://clear.ml/docs/latest/docs/webapp/webapp_exp_tuning/#output-destination)
- [Default container](https://clear.ml/docs/latest/docs/webapp/webapp_exp_tuning/#default-container)
- [Hyperparameters](https://clear.ml/docs/latest/docs/webapp/webapp_exp_tuning/#hyperparameters) \- Parameters, TensorFlow Definitions, command line options, environment variables, and user-defined properties

note

User parameters are editable in any task, except those whose status is _Published_ (read-only).

- [Configuration objects](https://clear.ml/docs/latest/docs/webapp/webapp_exp_tuning/#configuration-objects) \- Task model description
- [Initial weight input model](https://clear.ml/docs/latest/docs/webapp/webapp_exp_tuning/#initial-weights-input-model)
- [Output destination for artifacts storage](https://clear.ml/docs/latest/docs/webapp/webapp_exp_tuning/#output-destination)

### Execution Details [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_tuning/\#execution-details "Direct link to Execution Details")

#### Source Code [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_tuning/\#source-code "Direct link to Source Code")

Modify code execution by changing any of the following:

- Repository, commit (select by ID, tag name, or choose the last commit in the branch), script, working directory,
and/or binary.
- The Python packages to be installed and/or their versions - Edit the package list, or clear it to have the ClearML
Agent either not install any packages or use an existing repo `requirements.txt` file. If the task is based on a
run in which the packages used were eventually different to the ones originally specified, you can easily or reset the
packages to originally recorded values ("Original Pip").
- Uncommitted changes - Edit or clear all.

**To modify the source code**, hover over the relevant sections in the **EXECUTION** tab to access Edit, Clear/Discard,
and/or Reset functions.

#### Default Container [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_tuning/\#default-container "Direct link to Default Container")

Select a pre-configured container that the [ClearML Agent](https://clear.ml/docs/latest/docs/clearml_agent) will use to remotely execute this task (see [Building Task Execution Environments in a Container](https://clear.ml/docs/latest/docs/getting_started/clearml_agent_base_docker)).

**To add, change, or delete a default container:**

- In **EXECUTION** **>** **CONTAINER** **>** hover **>** **EDIT** **>**
Enter the default container image.

important

For a ClearML Agent to execute the task in a container, the agent must be running in
[Docker Mode](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_execution_env#docker-mode):

```bash
clearml-agent daemon --queue <execution_queue_to_pull_from> --docker [optional default container image to use]
```

#### Output Destination [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_tuning/\#output-destination "Direct link to Output Destination")

Set an output destination for model checkpoints (snapshots) and other artifacts. Examples of supported types of destinations
and formats for specifying locations include:

- A shared folder: `/mnt/share/folder`
- S3: `s3://bucket/folder`
- Non-AWS S3-like services (e.g. MinIO): `s3://host_addr:port/bucket`. **Note that port specification is required**.
- Google Cloud Storage: `gs://bucket-name/folder`
- Azure Storage: `azure://<account name>.blob.core.windows.net/path/to/file`

**To add, change, or delete an artifact output destination:**

- In **EXECUTION** **>** **OUTPUT** \> **DESTINATION** **>** hover **>** **EDIT** **>** edit **>** **SAVE**.

Set Output Destination for Artifacts

Also set the output destination for artifacts in code (see the `output_uri` parameter of the
[`Task.init`](https://clear.ml/docs/latest/docs/references/sdk/task#taskinit)
method), and in the ClearML configuration file
for all tasks (see [`default_output_uri`](https://clear.ml/docs/latest/docs/configs/clearml_conf#config_default_output_uri)
on the ClearML Configuration Reference page).

### Configuration [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_tuning/\#configuration "Direct link to Configuration")

#### Hyperparameters [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_tuning/\#hyperparameters "Direct link to Hyperparameters")

Add, change, or delete hyperparameters, which are organized in the **ClearML Web UI** in the following sections:

- **Args** \- Automatically logged argument parser parameters (e.g. `argparse`, `click`, `hydra`).

- **TF\_DEFINE** \- TensorFlow definitions (from code, TF\_DEFINEs automatic logging).

- **General** \- Parameter dictionaries (from code, connected to the Task by calling [`Task.connect()`](https://clear.ml/docs/latest/docs/references/sdk/task#connect)).

- Environment variables - Tracked if variables were listed in the `CLEARML_LOG_ENVIRONMENT` environment variable
or the [`sdk.development.log_os_environments`](https://clear.ml/docs/latest/docs/configs/clearml_conf#log_env_var) field of the `clearml.conf` file (see this [FAQ](https://clear.ml/docs/latest/docs/faq#track-env-vars)).

- Custom named parameter groups (see the `name` parameter in [`Task.connect`](https://clear.ml/docs/latest/docs/references/sdk/task#connect)).


**To add, change, or delete hyperparameters:**

- In the **CONFIGURATION** tab **>** **HYPERPARAMETERS** **>** parameter group **>** hover **>** click **EDIT** **>** add, change,
or delete keys and/or values **>** click **SAVE**.

#### User Properties [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_tuning/\#user-properties "Direct link to User Properties")

User properties allow storing any descriptive information in key-value pair format. They are editable in any task,
except those whose status is _Published_ (read-only).

**To add, change, or delete user properties:**

- In **CONFIGURATION** **>** **USER PROPERTIES** **>** **Properties** **>** hover **>** click **EDIT** **>** add, change, or delete
keys and/or values **>** click **SAVE**.

#### Configuration Objects [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_tuning/\#configuration-objects "Direct link to Configuration Objects")

**To add, change, or delete the Task model configurations:**

- In **CONFIGURATION** **>** **CONFIGURATION OBJECTS** **>** object name **>** hover **>** **EDIT** or **CLEAR** (if the
configuration is not empty).

### Artifacts [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_tuning/\#artifacts "Direct link to Artifacts")

#### Initial Weights Input Model [​](https://clear.ml/docs/latest/docs/webapp/webapp_exp_tuning/\#initial-weights-input-model "Direct link to Initial Weights Input Model")

Edit model configuration and label enumeration, choose a different initial input weight model for the same project or any
other project, or remove the model.

note

The models are editable in the **MODELS** tab, not the **TASKS** tab. Clicking the model name hyperlink shows the
model in the **MODELS** tab.

**To select a different model:**

1. In **ARTIFACTS** **>** **Input Model** **>** Hover and click **EDIT**.
2. If a model is associated with the task, click ![Edit Pencil](https://clear.ml/docs/latest/icons/ico-edit.svg).
3. In the **SELECT MODEL** dialog, select a model from the current project or any other project.

**To edit a model's configuration or label enumeration:**

1. Click the model name hyperlink. The model details appear in the **MODELS** tab.

2. Edit the model configuration or label enumeration:
   - Model configuration - In the **NETWORK** tab **>** Hover and click **EDIT**. **>** CLick **EDIT** or **CLEAR** (to
     remove the configuration).

     Users can also search for the configuration (hover over the configuration textbox, the search box appears) and copy the
     configuration to the clipboard (hover and click ![Copy Clipboard](https://clear.ml/docs/latest/icons/ico-copy-to-clipboard.svg)).

   - Label enumeration - In the **LABELS** tab **>** Hover and click **EDIT** **>** Add, change, or delete label
     enumeration key-value pairs.

**To remove a model from a task:**

- Hover and click **EDIT** **>** Click ![Trash](https://clear.ml/docs/latest/icons/ico-trash.svg)

- [To Tune a Task and Execute it Remotely:](https://clear.ml/docs/latest/docs/webapp/webapp_exp_tuning/#to-tune-a-task-and-execute-it-remotely)
- [Modifying Tasks](https://clear.ml/docs/latest/docs/webapp/webapp_exp_tuning/#modifying-tasks)
  - [Execution Details](https://clear.ml/docs/latest/docs/webapp/webapp_exp_tuning/#execution-details)
  - [Configuration](https://clear.ml/docs/latest/docs/webapp/webapp_exp_tuning/#configuration)
  - [Artifacts](https://clear.ml/docs/latest/docs/webapp/webapp_exp_tuning/#artifacts)