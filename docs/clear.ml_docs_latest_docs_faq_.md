---
url: "https://clear.ml/docs/latest/docs/faq/"
title: "FAQ | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/faq/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

**General Information**

- [How do I know a new version came out?](https://clear.ml/docs/latest/docs/faq/#new-version-auto-update)
- [How do I find out ClearML version information?](https://clear.ml/docs/latest/docs/faq/#versions)

**Models**

- [How can I sort models by a certain metric?](https://clear.ml/docs/latest/docs/faq/#custom-columns)
- [Can I store more information on the models?](https://clear.ml/docs/latest/docs/faq/#store-more-model-info)
- [Can I store the model configuration file as well?](https://clear.ml/docs/latest/docs/faq/#store-model-configuration)
- [I am training multiple models at the same time, but I only see one of them. What happened?](https://clear.ml/docs/latest/docs/faq/#only-last-model-appears)
- [Can I log input and output models manually?](https://clear.ml/docs/latest/docs/faq/#manually-log-models)
- [Models are not accessible from the UI after I migrated ClearML Server to a new address. How do I fix this?](https://clear.ml/docs/latest/docs/faq/#migrate_server_models)
- [Models are not accessible from the UI after I moved them (different bucket / server). How do I fix this?](https://clear.ml/docs/latest/docs/faq/#relocate_models)

**Tasks**

- [I noticed I keep getting the message "warning: uncommitted code". What does it mean?](https://clear.ml/docs/latest/docs/faq/#uncommitted-code-warning)
- [I do not use argparse for hyperparameters. Do you have a solution?](https://clear.ml/docs/latest/docs/faq/#dont-want-argparser)
- [I noticed that all of my tasks appear as "Training". Are there other options?](https://clear.ml/docs/latest/docs/faq/#other-task-types)
- [How can I query tasks by a time range?](https://clear.ml/docs/latest/docs/faq/#time-range-query)
- [Sometimes I see tasks as running when in fact they are not. What's going on?](https://clear.ml/docs/latest/docs/faq/#task-running-but-stopped)
- [My code throws an exception, but my task status is not "Failed". What happened?](https://clear.ml/docs/latest/docs/faq/#exception-not-failed)
- [CERTIFICATE\_VERIFY\_FAILED - When I run my task, I get an SSL Connection error. Do you have a solution?](https://clear.ml/docs/latest/docs/faq/#ssl-connection-error)
- [How do I modify task names once they have been created?](https://clear.ml/docs/latest/docs/faq/#modify_exp_names)
- [Using Conda and the "typing" package, I get the error "AttributeError: type object 'Callable' has no attribute '\_abc\_registry'". How do I fix this?](https://clear.ml/docs/latest/docs/faq/#typing)
- [My ClearML Server disk space usage is too high. What can I do about this?](https://clear.ml/docs/latest/docs/faq/#delete_exp)
- [Can I change the random seed my task uses?](https://clear.ml/docs/latest/docs/faq/#random_seed)
- [In the Web UI, I can't access files that my task stored. Why not?](https://clear.ml/docs/latest/docs/faq/#access_files)
- [I get the message "ClearML Monitor: Could not detect iteration reporting, falling back to iterations as seconds-from-start". What does it mean?](https://clear.ml/docs/latest/docs/faq/#resource_monitoring)
- [Can I control what ClearML automatically logs?](https://clear.ml/docs/latest/docs/faq/#controlling_logging)
- [Can I run a ClearML Task while working offline?](https://clear.ml/docs/latest/docs/faq/#offline_mode)

**Graphs and Logs**

- [The first log lines are missing from the task console tab. Where did they go?](https://clear.ml/docs/latest/docs/faq/#first-log-lines-missing)
- [How do I create a graph comparing hyperparameters vs model accuracy?](https://clear.ml/docs/latest/docs/faq/#compare-graph-parameters)
- [I want to add more graphs, not just with TensorBoard. Is this supported?](https://clear.ml/docs/latest/docs/faq/#more-graph-types)
- [How can I report more than one scatter 2D series on the same plot?](https://clear.ml/docs/latest/docs/faq/#multiple-scatter2D)

**GIT and Storage**

- [Is there something ClearML can do about uncommitted code running?](https://clear.ml/docs/latest/docs/faq/#help-uncommitted-code)
- [I read there is a feature for centralized model storage. How do I use it?](https://clear.ml/docs/latest/docs/faq/#centralized-model-storage)
- [When using PyCharm to remotely debug a machine, the Git repo is not detected. Do you have a solution?](https://clear.ml/docs/latest/docs/faq/#pycharm-remote-debug-detect-git)
- [Debug images and/or artifacts are not loading in the UI after I migrated ClearML Server to a new address. How do I fix this?](https://clear.ml/docs/latest/docs/faq/#migrate_server_debug)

**Remote Debugging (ClearML PyCharm Plugin)**

- [I am using your ClearML PyCharm Plugin for remote debugging. I get the message "clearml.Task - INFO - Repository and package analysis timed out (10.0 sec), giving up". What should I do?](https://clear.ml/docs/latest/docs/faq/#package_thread)

**Jupyter**

- [I am using Jupyter Notebook. Is this supported?](https://clear.ml/docs/latest/docs/faq/#jupyter-notebook)

**scikit-learn**

- [Can I use ClearML with scikit-learn?](https://clear.ml/docs/latest/docs/faq/#use-scikit-learn)

**ClearML Configuration**

- [How do I explicitly specify the ClearML configuration file to be used?](https://clear.ml/docs/latest/docs/faq/#change-config-path)
- [How can I override ClearML credentials from the OS environment?](https://clear.ml/docs/latest/docs/faq/#credentials-os-env)
- [How can I track OS environment variables with tasks?](https://clear.ml/docs/latest/docs/faq/#track-env-vars)

**ClearML Hosted Service**

- [I run my script, but my task is not in the ClearML Hosted Service Web UI. How do I fix this?](https://clear.ml/docs/latest/docs/faq/#hosted-service-no-config)

**ClearML Server Deployment**

- How do I deploy ClearML Server on:
  - [Stand alone Linux Ubuntu systems?](https://clear.ml/docs/latest/docs/faq/#Ubuntu)
  - [macOS?](https://clear.ml/docs/latest/docs/faq/#Ubuntu)
  - [Windows 10?](https://clear.ml/docs/latest/docs/faq/#docker_compose_win10)
  - [AWS EC2 AMIs?](https://clear.ml/docs/latest/docs/faq/#aws_ec2_amis)
  - [Google Cloud Platform?](https://clear.ml/docs/latest/docs/faq/#google_cloud_platform)
- [How do I restart ClearML Server?](https://clear.ml/docs/latest/docs/faq/#restart)
- [Can I create a Helm Chart for ClearML Server Kubernetes deployment?](https://clear.ml/docs/latest/docs/faq/#helm)
- [My Docker cannot load a local host directory on SELinux?](https://clear.ml/docs/latest/docs/faq/#selinux)

**ClearML Server Configuration**

- [How do I configure ClearML Server for subdomains and load balancers?](https://clear.ml/docs/latest/docs/faq/#subdomains)
- [Can I add web login authentication to ClearML Server?](https://clear.ml/docs/latest/docs/faq/#web-auth)
- [Can I modify non-responsive task settings?](https://clear.ml/docs/latest/docs/faq/#watchdog)

**ClearML Server Troubleshooting**

- [After reinstalling, why can't I create credentials in the WebApp (UI)?](https://clear.ml/docs/latest/docs/faq/#clearml-server-reinstall-cookies)
- [How do I fix Docker upgrade errors?](https://clear.ml/docs/latest/docs/faq/#common-docker-upgrade-errors)
- [Why is web login authentication not working?](https://clear.ml/docs/latest/docs/faq/#port-conflict)
- [How do I bypass a proxy configuration to access my local ClearML Server?](https://clear.ml/docs/latest/docs/faq/#proxy-localhost)
- [Why am I getting a `413 Request Entity Too Large` error when uploading files?](https://clear.ml/docs/latest/docs/faq/#request-too-large)
- [The ClearML Server keeps returning HTTP 500 (or 400) errors. How do I fix this?](https://clear.ml/docs/latest/docs/faq/#elastic_watermark)
- [Why is my ClearML WebApp (UI) not showing any data?](https://clear.ml/docs/latest/docs/faq/#web-ui-empty)
- [Why can't I access my ClearML Server when I run my code in a virtual machine?](https://clear.ml/docs/latest/docs/faq/#vm_server)

**ClearML Agent**

- [How can I execute ClearML Agent without installing packages each time?](https://clear.ml/docs/latest/docs/faq/#system_site_packages)

**ClearML API**

- [How can I use the ClearML API to fetch data?](https://clear.ml/docs/latest/docs/faq/#api)

## General Information [​](https://clear.ml/docs/latest/docs/faq/\#general-information "Direct link to General Information")

#### How do I know a new version came out? [​](https://clear.ml/docs/latest/docs/faq/\#how-do-i-know-a-new-version-came-out- "Direct link to how-do-i-know-a-new-version-came-out-")

Starting with ClearML v0.9.3, ClearML issues a new version release notification, which appears in the log and is
output to the console, when a Python task script is run.

For example, when a new ClearML Python Package version is available, the notification is:

```text
CLEARML new package available: UPGRADE to vX.Y.Z is recommended!
```

When a new ClearML Server version is available, the notification is:

```text
CLEARML-SERVER new version available: upgrade to vX.Y is recommended!
```

#### How do I find out ClearML version information? [​](https://clear.ml/docs/latest/docs/faq/\#how-do-i-find-out-clearml-version-information--- "Direct link to how-do-i-find-out-clearml-version-information---")

ClearML server version information is available in the ClearML WebApp **Settings** page. On the bottom right of the page,
the following numbers are displayed:

- Web application version
- API server version
- API version

![Server version information](https://clear.ml/docs/latest/assets/images/faq_server_versions-d9877d4da0cba19675d111861a8f5c40.png#light-mode-only)![Server version information](https://clear.ml/docs/latest/assets/images/faq_server_versions_dark-44ac2491c38a6bb7e7415badbde81352.png#dark-mode-only)

ClearML Python package information can be obtained by using `pip freeze`.

For example:

```bash
pip freeze|grep clearml
```

should return something like this:

```console
clearml==1.0.3rc1

clearml-agent==1.0.0

clearml-session==0.3.2
```

## Models [​](https://clear.ml/docs/latest/docs/faq/\#models "Direct link to Models")

#### How can I sort models by a certain metric? [​](https://clear.ml/docs/latest/docs/faq/\#how-can-i-sort-models-by-a-certain-metric--- "Direct link to how-can-i-sort-models-by-a-certain-metric---")

To sort models by a metric, in the ClearML Web UI,
add a [custom column](https://clear.ml/docs/latest/docs/webapp/webapp_model_table#customizing-the-model-table) to the model table and sort by
that metric column. Available custom column options depend upon the models in the table and the metrics that have been
attached to them (see [Logging Metrics and Plots](https://clear.ml/docs/latest/docs/clearml_sdk/model_sdk#logging-metrics-and-plots)).

ClearML associates models with the tasks that created them, so you can also add a [custom column](https://clear.ml/docs/latest/docs/webapp/webapp_exp_table#customizing-the-task-table)
in a task table and sort by that metric column.

#### Can I store more information on the models? [​](https://clear.ml/docs/latest/docs/faq/\#can-i-store-more-information-on-the-models--- "Direct link to can-i-store-more-information-on-the-models---")

Yes! For example, you can use [`Task.set_model_label_enumeration()`](https://clear.ml/docs/latest/docs/references/sdk/task#set_model_label_enumeration)
to store label enumeration:

```python
Task.current_task().set_model_label_enumeration( {"label": int(0), } )
```

For more information about `Task` class methods, see the [Task Class](https://clear.ml/docs/latest/docs/fundamentals/task) reference page.

#### Can I store the model configuration file as well? [​](https://clear.ml/docs/latest/docs/faq/\#can-i-store-the-model-configuration-file-as-well---- "Direct link to can-i-store-the-model-configuration-file-as-well----")

Yes! Use [`Task.connect_configuration()`](https://clear.ml/docs/latest/docs/references/sdk/task#connect_configuration):

```python
Task.current_task().connect_configuration("a very long text with the configuration file's content")
```

#### I am training multiple models at the same time, but I only see one of them. What happened? [​](https://clear.ml/docs/latest/docs/faq/\#i-am-training-multiple-models-at-the-same-time-but-i-only-see-one-of-them-what-happened--- "Direct link to i-am-training-multiple-models-at-the-same-time-but-i-only-see-one-of-them-what-happened---")

This issue was resolved in ClearML Server v1.0.0.

See server upgrade instructions for any of the available formats:

- [AWS EC2 AMIs](https://clear.ml/docs/latest/docs/deploying_clearml/upgrade_server_aws_ec2_ami)
- [Google Cloud Platform](https://clear.ml/docs/latest/docs/deploying_clearml/upgrade_server_gcp)
- [Linux or MacOS](https://clear.ml/docs/latest/docs/deploying_clearml/upgrade_server_linux_mac)
- [Windows 10](https://clear.ml/docs/latest/docs/deploying_clearml/upgrade_server_win)
- [Kubernetes](https://clear.ml/docs/latest/docs/deploying_clearml/upgrade_server_kubernetes_helm)

#### Can I log input and output models manually? [​](https://clear.ml/docs/latest/docs/faq/\#can-i-log-input-and-output-models-manually--- "Direct link to can-i-log-input-and-output-models-manually---")

Yes! Use [`InputModel.import_model()`](https://clear.ml/docs/latest/docs/references/sdk/model_inputmodel#inputmodelimport_model)
and [`Task.connect()`](https://clear.ml/docs/latest/docs/references/sdk/task#connect) to connect an input model. Use
[`OutputModel.update_weights()`](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel#update_weights)
to connect a model weights file.

```python
input_model = InputModel.import_model(link_to_initial_model_file)

Task.current_task().connect(input_model)

OutputModel(Task.current_task()).update_weights(link_to_new_model_file_here)
```

For more information about models, see [InputModel](https://clear.ml/docs/latest/docs/references/sdk/model_inputmodel)
and [OutputModel](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel) classes.

#### Models are not accessible from the UI after I migrated ClearML Server to a new address. How do I fix this? [​](https://clear.ml/docs/latest/docs/faq/\#models-are-not-accessible-from-the-ui-after-i-migrated-clearml-server-to-a-new-address-how-do-i-fix-this--- "Direct link to models-are-not-accessible-from-the-ui-after-i-migrated-clearml-server-to-a-new-address-how-do-i-fix-this---")

This can happen if your models were uploaded to the ClearML files server, since the value registered was their full URL
at the time of registration (e.g. `https://files.<OLD_ADDRESS>/path/to/model`).

To fix this, the registered URL of each model needs to be replaced with its current URL.

To replace the URL of each model, execute the following commands:

1. Open bash in the mongo DB docker container:





```bash
sudo docker exec -it clearml-mongo /bin/bash
```

2. Create the following script inside the Docker shell (as well as the URL protocol if you aren't using `s3`).
Make sure to replace `<old-bucket-name>` and `<new-bucket-name>`.





```bash
cat <<EOT >> script.js

db.model.find({uri:{$regex:/^s3/}}).forEach(function(e,i) {

e.uri = e.uri.replace("s3://<old-bucket-name>/","s3://<new-bucket-name>/");

db.model.save(e);});

EOT
```

3. Run the script against the backend DB:





```bash
mongo backend script.js
```


#### Models are not accessible from the UI after I moved them (different bucket / server). How do I fix this? [​](https://clear.ml/docs/latest/docs/faq/\#models-are-not-accessible-from-the-ui-after-i-moved-them-different-bucket--server-how-do-i-fix-this--- "Direct link to models-are-not-accessible-from-the-ui-after-i-moved-them-different-bucket--server-how-do-i-fix-this---")

This can happen if your models were uploaded to the ClearML files server, since the value registered was their full URL
at the time of registration (e.g. `https://files.<OLD_ADDRESS>/path/to/model`).

To fix this, the registered URL of each model needs to be replaced with its current URL:

1. Open bash in the mongo DB Docker container:





```bash
sudo docker exec -it clearml-mongo /bin/bash
```

2. Create the following script inside the Docker shell (make sure to replace `<old-bucket-name>` and `<new-bucket-name>`, as well as the URL protocol prefixes if you aren't using S3):





```bash
cat <<EOT >> script.js

db.model.find({uri:{$regex:/^s3/}}).forEach(function(e,i) {

e.uri = e.uri.replace("s3://<old-bucket-name>/","s3://<new-bucket-name>/");

db.model.save(e);});

EOT
```

3. Run the script against the backend DB:





```bash
mongo backend script.js
```


## Tasks [​](https://clear.ml/docs/latest/docs/faq/\#tasks "Direct link to Tasks")

#### I noticed I keep getting the message "warning: uncommitted code". What does it mean? [​](https://clear.ml/docs/latest/docs/faq/\#i-noticed-i-keep-getting-the-message-warning-uncommitted-code-what-does-it-mean--- "Direct link to i-noticed-i-keep-getting-the-message-warning-uncommitted-code-what-does-it-mean---")

This message is only a warning. ClearML not only detects your current repository and git commit, but also warns you
if you are using uncommitted code. ClearML does this because uncommitted code means this task will be difficult
to reproduce. You can see uncommitted changes in the ClearML Web UI, in the **EXECUTION** tab of the task info panel.

#### I do not use argparse for hyperparameters. Do you have a solution? [​](https://clear.ml/docs/latest/docs/faq/\#i-do-not-use-argparse-for-hyperparameters-do-you-have-a-solution--- "Direct link to i-do-not-use-argparse-for-hyperparameters-do-you-have-a-solution---")

Yes! ClearML provides multiple ways to configure your task and track your parameters!

In addition to argparse, ClearML also automatically captures and tracks command line parameters created using:

- [click](https://clear.ml/docs/latest/docs/integrations/click)
- [Python Fire](https://clear.ml/docs/latest/docs/integrations/python_fire)
- [Hydra](https://clear.ml/docs/latest/docs/integrations/hydra)
- [LightningCLI](https://lightning.ai/docs/pytorch/stable/cli/lightning_cli.html#lightning-cli)

ClearML also supports tracking code-level configuration dictionaries using [`Task.connect()`](https://clear.ml/docs/latest/docs/references/sdk/task#connect).

For example, the code below connects hyperparameters (`learning_rate`, `batch_size`, `display_step`,
`model_path`, `n_hidden_1`, and `n_hidden_2`) to a task:

```python
# Create a dictionary of parameters

parameters_dict = { 'learning_rate': 0.001, 'batch_size': 100, 'display_step': 1,

                    'model_path': "/tmp/model.ckpt", 'n_hidden_1': 256, 'n_hidden_2': 256 }



# Connect the dictionary to your CLEARML Task

parameters_dict = Task.current_task().connect(parameters_dict)
```

For more task configuration options, see [Hyperparameters](https://clear.ml/docs/latest/docs/fundamentals/hyperparameters).

#### I noticed that all of my tasks appear as "Training". Are there other options? [​](https://clear.ml/docs/latest/docs/faq/\#i-noticed-that-all-of-my-tasks-appear-as-training-are-there-other-options--- "Direct link to i-noticed-that-all-of-my-tasks-appear-as-training-are-there-other-options---")

Yes! ClearML supports [multiple task types](https://clear.ml/docs/latest/docs/fundamentals/task#task-types). When creating tasks and
calling [`Task.init()`](https://clear.ml/docs/latest/docs/references/sdk/task#taskinit), you can provide a task type. For example:

```python
task = Task.init(project_name, task_name, Task.TaskTypes.testing)
```

#### How can I query tasks by a time range? [​](https://clear.ml/docs/latest/docs/faq/\#how-can-i-query-tasks-by-a-time-range- "Direct link to how-can-i-query-tasks-by-a-time-range-")

You can use [`Task.get_tasks()`](https://clear.ml/docs/latest/docs/references/sdk/task#taskget_tasks) and [`Task.query_tasks()`](https://clear.ml/docs/latest/docs/references/sdk/task#taskquery_tasks)
to filter tasks by time-based fields, such as `status_changed` and `started`.

Use comparison operators ( `>`, `<`, `>=`, `<=`, `=`) for specifying a desired time range. For example, to return all
tasks whose status changed after March 17, 2025, 22:00:

```python
Task.get_tasks(

    project_name='vLLM Model Deployment',

    task_filter={

        'status_changed': ">2025-03-17T22:00:00"

    }

)
```

If the SDK task object schema (`backend_api.service.v?.tasks.GetAllRequest._schema`, replace `?` with the relevant
version, e.g. [v2.23](https://github.com/clearml/clearml/blob/4a0755634bd1a1388366e66707826f122cfd5dd4/clearml/backend_api/services/v2_23/tasks.py#L7756C1-L7756C16))
is missing a field that is supported by the server, use the `_allow_extra_fields_` flag to bypass SDK schema validation
and add the query directly to the API request. API query time range specification adheres to a different syntax:

- The array `[start_time, end_time]` specifies the time range.
- Use `None` to indicate an open-ended range.

For example, assume the SDK schema is missing the `Task.started` parameter: to return all tasks started after
March 17, 2023, 22:00:

```python
Task.get_tasks(

    project_name='vLLM Model Deployment',

    task_filter={

        '_allow_extra_fields_': True,

        'started': ["2023-03-17T22:00:00", None]

    }

)
```

See all backend-supported fields in the [Task API definition](https://clear.ml/docs/latest/docs/references/api/definitions#taskstask).

#### Sometimes I see tasks as running when in fact they are not. What's going on? [​](https://clear.ml/docs/latest/docs/faq/\#sometimes-i-see-tasks-as-running-when-in-fact-they-are-not-whats-going-on--- "Direct link to sometimes-i-see-tasks-as-running-when-in-fact-they-are-not-whats-going-on---")

ClearML monitors your Python process. When the process exits properly, ClearML closes the task. When the process crashes and terminates abnormally, it sometimes misses the stop signal. In this case, you can safely right-click the task in the WebApp and abort it.

#### My code throws an exception, but my task status is not "Failed". What happened? [​](https://clear.ml/docs/latest/docs/faq/\#my-code-throws-an-exception-but-my-task-status-is-not-failed-what-happened--- "Direct link to my-code-throws-an-exception-but-my-task-status-is-not-failed-what-happened---")

This issue was resolved in Trains v0.9.2. Upgrade to ClearML by executing the following command:

```text
pip install -U clearml
```

#### When I run my task, I get an SSL Connection error CERTIFICATE\_VERIFY\_FAILED. Do you have a solution? [​](https://clear.ml/docs/latest/docs/faq/\#when-i-run-my-task-i-get-an-ssl-connection-error-certificate_verify_failed-do-you-have-a-solution "Direct link to When I run my task, I get an SSL Connection error CERTIFICATE_VERIFY_FAILED. Do you have a solution?")

Your firewall may be preventing the connection. Try one of the following solutions:

- Direct Python "requests" to use the enterprise certificate file by setting the OS environment variables `CURL_CA_BUNDLE`
or `REQUESTS_CA_BUNDLE`. For a detailed discussion of this topic, see the [Requests documentation](https://requests.readthedocs.io/en/latest/user/advanced/#ssl-cert-verification)
and this [Stack Overflow discussion](https://stackoverflow.com/questions/48391750/disable-python-requests-ssl-validation-for-an-imported-module).

- Disable certificate verification



warning





For security reasons, it is not recommended to disable certificate verification.




1. Upgrade ClearML to the current version:





     ```text
     pip install -U clearml
     ```

2. Create a new `clearml.conf` configuration file (see a [sample configuration file](https://github.com/clearml/clearml/blob/master/docs/clearml.conf)), containing:





     ```text
     api { verify_certificate = False }
     ```

3. Copy the new `clearml.conf` file to:
     - Linux - `~/clearml.conf`
     - Mac - `$HOME/clearml.conf`
     - Windows - ```\User\<username>\clearml.conf``~/clearml.conf```

#### How do I modify task names once they have been created? [​](https://clear.ml/docs/latest/docs/faq/\#how-do-i-modify-task-names-once-they-have-been-created "Direct link to How do I modify task names once they have been created?")

A task's name is a user-controlled property, which can be accessed via the `Task.name` property. This lets you use meaningful naming schemes to easily filter and compare tasks.

For example, to distinguish between different tasks, you can append the task ID to the task name:

```python
task = Task.init(project_name='examples', task_name='train')

task.name += ' {}'.format(task.id)
```

Or, append the Task ID post-execution:

```python
tasks = Task.get_tasks(project_name='examples', task_name='train')

for t in tasks:

    t.name += ' {}'.format(task.id)
```

Another example is to append a specific hyperparameter and its value to each task's name:

```python
tasks = Task.get_tasks(project_name='examples', task_name='my_automl_experiment')

for t in tasks:

    params = t.get_parameters()

    if 'my_secret_parameter' in params:

        t.name += ' my_secret_parameter={}'.format(params['my_secret_parameter'])
```

Use this task naming when creating automation pipelines with a naming convention.

#### Using Conda and the "typing" package, I get the error "AttributeError: type object 'Callable' has no attribute '\_abc\_registry'". How do I fix this? [​](https://clear.ml/docs/latest/docs/faq/\#using-conda-and-the-typing-package-i-get-the-error-attributeerror-type-object-callable-has-no-attribute-_abc_registry-how-do-i-fix-this "Direct link to Using Conda and the \"typing\" package, I get the error \"AttributeError: type object 'Callable' has no attribute '_abc_registry'\". How do I fix this?")

Conda and the [typing](https://pypi.org/project/typing/) package may have some compatibility issues.

However, [since Python 3.5](https://docs.python.org/3.5/library/typing.html), the `typing` package is part of the standard library.

To resolve the error, uninstall `typing` and rerun your script. If this does not fix the issue, create a [new ClearML issue](https://github.com/clearml/clearml/issues/new), including the full error, and your environment details.

#### My ClearML Server disk space usage is too high. What can I do about this? [​](https://clear.ml/docs/latest/docs/faq/\#my-clearml-server-disk-space-usage-is-too-high-what-can-i-do-about-this "Direct link to My ClearML Server disk space usage is too high. What can I do about this?")

To clear up space, you can delete ClearML objects (e.g. tasks, models, datasets, etc.).

To delete an object via the UI:

1. Go to the relevant object table (e.g. [Task Table](https://clear.ml/docs/latest/docs/webapp/webapp_exp_table), [Model Table](https://clear.ml/docs/latest/docs/webapp/webapp_model_table), etc.)
2. Archive the object - Right-click the object in the table **>** click **Archive**
3. Click **Open Archive** on the top of the table
4. In the archive table, right-click the object **>** click **Delete**.

To delete an object programmatically, use the relevant method:

- Tasks - [`Task.delete()`](https://clear.ml/docs/latest/docs/references/sdk/task#delete)
- Models
  - [`Model.remove()`](https://clear.ml/docs/latest/docs/references/sdk/model_model#modelremove)
  - [`InputModel.remove()`](https://clear.ml/docs/latest/docs/references/sdk/model_inputmodel#inputmodelremove)
- Datasets - [`Dataset.delete()`](https://clear.ml/docs/latest/docs/references/sdk/dataset#datasetdelete)

warning

You cannot undo the deletion of a ClearML object.

#### Can I change the random seed my task uses? [​](https://clear.ml/docs/latest/docs/faq/\#can-i-change-the-random-seed-my-task-uses "Direct link to Can I change the random seed my task uses?")

Yes! By default, ClearML initializes Tasks with an initial seed of `1337` to ensure reproducibility. To set a different
value for your task, use the [`Task.set_random_seed()`](https://clear.ml/docs/latest/docs/references/sdk/task#taskset_random_seed) class method and
provide the new seed value, **before initializing the task**.

You can disable the deterministic behavior entirely by passing `Task.set_random_seed(None)`.

#### In the Web UI, I can't access files that my task stored. Why not? [​](https://clear.ml/docs/latest/docs/faq/\#in-the-web-ui-i-cant-access-files-that-my-task-stored-why-not "Direct link to In the Web UI, I can't access files that my task stored. Why not?")

ClearML stores file locations. The machine running your browser must have access to the location where the machine
that ran the Task stored the file. This applies to debug samples and artifacts. If, for example, the machine running the browser does not have access, you may see `Unable to load image`, instead of the image.

#### I get the message "CLEARML Monitor: Could not detect iteration reporting, falling back to iterations as seconds-from-start". What does it mean? [​](https://clear.ml/docs/latest/docs/faq/\#i-get-the-message-clearml-monitor-could-not-detect-iteration-reporting-falling-back-to-iterations-as-seconds-from-start-what-does-it-mean "Direct link to I get the message \"CLEARML Monitor: Could not detect iteration reporting, falling back to iterations as seconds-from-start\". What does it mean?")

If metric reporting begins within the first three minutes, ClearML reports resource monitoring by iteration. Otherwise,
it reports resource monitoring by seconds from start, and logs a message:

```text
CLEARML Monitor: Could not detect iteration reporting, falling back to iterations as seconds-from-start.
```

However, if metric reporting begins after three minutes and anytime up to thirty minutes, resource monitoring reverts to
by iteration, and ClearML logs a message

```text
CLEARML Monitor: Reporting detected, reverting back to iteration based reporting.
```

After thirty minutes, it remains unchanged.

#### Can I control what ClearML automatically logs? [​](https://clear.ml/docs/latest/docs/faq/\#can-i-control-what-clearml-automatically-logs--- "Direct link to can-i-control-what-clearml-automatically-logs---")

Yes! ClearML lets you control automatic logging for frameworks, argument parsers, `stdout`, and `stderr` when
initializing a Task by calling [`Task.init()`](https://clear.ml/docs/latest/docs/references/sdk/task#taskinit).

##### Frameworks [​](https://clear.ml/docs/latest/docs/faq/\#frameworks "Direct link to Frameworks")

To control a Task's framework logging, use the `auto_connect_frameworks` parameter. Turn off all automatic logging by setting the
parameter to `False`. For finer grained control of logged frameworks, input a dictionary, with framework-boolean pairs.

For example:

```python
auto_connect_frameworks={

    'matplotlib': True, 'tensorflow': False, 'tensorboard': False, 'pytorch': True,

    'xgboost': False, 'scikit': True, 'fastai': True, 'lightgbm': False,

    'hydra': True, 'detect_repository': True, 'tfdefines': True, 'joblib': True,

    'megengine': True, 'catboost': True

}
```

##### Argument Parsers [​](https://clear.ml/docs/latest/docs/faq/\#argument-parsers "Direct link to Argument Parsers")

To control a task's logging of parameters from supported argument parsers, use the `auto_connect_arg_parser` parameter.
Completely disable all automatic logging by setting the parameter to `False`. For finer grained control of logged
parameters, input a dictionary with parameter-boolean pairs. The `False` value excludes the specified parameter.
Unspecified parameters default to `True`.

For example, the following code will not log the `Example_1` parameter, but will log all other arguments.

```python
auto_connect_arg_parser={"Example_1": False}
```

To exclude all unspecified parameters, set the `*` key to `False`.

For example, the following code will log **only** the `Example_2` parameter.

```python
auto_connect_arg_parser={"Example_2": True, "*": False}
```

An empty dictionary completely disables all automatic logging of parameters from argument parsers:

```python
auto_connect_arg_parser={}
```

##### stdout and stderr [​](https://clear.ml/docs/latest/docs/faq/\#stdout-and-stderr "Direct link to stdout and stderr")

To control the `stdout`, `stderr`, and standard logging, use the `auto_connect_streams` parameter.
To disable logging all three, set the parameter to `False`. For finer grained control, input a dictionary, where the keys are `stout`, `stderr`,
and `logging`, and the values are booleans. For example:

```python
auto_connect_streams={'stdout': True, 'stderr': True, 'logging': False}
```

See [`Task.init`](https://clear.ml/docs/latest/docs/references/sdk/task#taskinit).

#### Can I run ClearML Task while working offline? [​](https://clear.ml/docs/latest/docs/faq/\#can-i-run-clearml-task-while-working-offline--- "Direct link to can-i-run-clearml-task-while-working-offline---")

Yes! You can use ClearML's Offline Mode, in which all the data and logs that a task captures from the code are stored in a
local folder.

You can enable offline mode in one of the following ways:

- Before initializing a task, use the [`Task.set_offline()`](https://clear.ml/docs/latest/docs/references/sdk/task#taskset_offline) class method and set
the `offline_mode` argument to `True`
- Before running a task, set `CLEARML_OFFLINE_MODE=1`

warning

Offline mode only works with tasks created using [`Task.init()`](https://clear.ml/docs/latest/docs/references/sdk/task#taskinit) and not with those created
using [`Task.create()`](https://clear.ml/docs/latest/docs/references/sdk/task#taskcreate).

The task's console output displays the task ID and a path to the folder with the session's captured information:

```console
ClearML Task: created new task id=offline-372657bb04444c25a31bc6af86552cc9

...

...

ClearML Task: Offline session stored in /home/user/.clearml/cache/offline/b786845decb14eecadf2be24affc7418.zip
```

In order to upload to the ClearML Server the execution data that the Task captured offline, do one of the
following:

- Use the `import-offline-session <session_path>` option of the [clearml-task](https://clear.ml/docs/latest/docs/apps/clearml_task) CLI
- Use the [`Task.import_offline_session()`](https://clear.ml/docs/latest/docs/references/sdk/task#taskimport_offline_session) method.

See [Storing Task Data Offline](https://clear.ml/docs/latest/docs/guides/set_offline).

## Graphs and Logs [​](https://clear.ml/docs/latest/docs/faq/\#graphs-and-logs "Direct link to Graphs and Logs")

#### The first log lines are missing from the task console tab. Where did they go? [​](https://clear.ml/docs/latest/docs/faq/\#the-first-log-lines-are-missing-from-the-task-console-tab-where-did-they-go--- "Direct link to the-first-log-lines-are-missing-from-the-task-console-tab-where-did-they-go---")

Due to speed/optimization issues, the console displays only the last several hundred log lines.

You can always download the full log as a file using the ClearML Web UI. In the **ClearML Web UI >** task's **CONSOLE**
tab, click `Download full log`.

![Download console log](https://clear.ml/docs/latest/assets/images/faq_download_console_log-ad16c607bc209bcd9da3b02a05afff72.png#light-mode-only)![Download console log](https://clear.ml/docs/latest/assets/images/faq_download_console_log_dark-977aca300cedb2dbcd55df7937bbb5e5.png#dark-mode-only)

#### How do I create a graph comparing hyperparameters vs. model accuracy? [​](https://clear.ml/docs/latest/docs/faq/\#how-do-i-create-a-graph-comparing-hyperparameters-vs-model-accuracy--- "Direct link to how-do-i-create-a-graph-comparing-hyperparameters-vs-model-accuracy---")

You can use the UI's [task comparison features](https://clear.ml/docs/latest/docs/webapp/webapp_exp_comparing) to compare the logged hyperparameter
and accuracy values of several tasks. In the task comparison page, under the **HYPERPARAMETERS** tab
you can visualize tasks' hyperparameter values in relation to performance metrics in a scatter plot or parallel
coordinates plot:

- [Scatter plot](https://clear.ml/docs/latest/docs/webapp/webapp_exp_comparing#scatter-plot): View the correlation between a selected hyperparameter and
metric. For example, the image below shows a scatter plot that displays the values of a performance metric (`accuracy`)
and a hyperparameter (`epochs`) of a few tasks:

![Scatter plot comparison](https://clear.ml/docs/latest/assets/images/faq_compare_scatter-811ae455ac0ba273c93cb6ae74516417.png#light-mode-only)![Scatter plot comparison](https://clear.ml/docs/latest/assets/images/faq_compare_scatter_dark-88fd2a085c1e15c40e019ddf6d4ced11.png#dark-mode-only)

- [Parallel coordinates plot](https://clear.ml/docs/latest/docs/webapp/webapp_exp_comparing#parallel-coordinates-mode): View the impact of hyperparameters
on selected metric(s). For example, the image below shows
a parallel coordinates plot which displays the values of selected hyperparameters (`epochs`, `lr`, and `batch_size`)
and a performance metric (`accuracy`) of a few tasks:

![Parallel Coordinates](https://clear.ml/docs/latest/assets/images/compare_parallel_coordinates-950b07d3f41808e66bea09afd66deac8.png#light-mode-only)![Parallel Coordinates](https://clear.ml/docs/latest/assets/images/compare_parallel_coordinates_dark-67e93b302b94afa2e5e31a22cfa6f194.png#dark-mode-only)


#### I want to add more graphs, not just with TensorBoard. Is this supported? [​](https://clear.ml/docs/latest/docs/faq/\#i-want-to-add-more-graphs-not-just-with-tensorboard-is-this-supported--- "Direct link to i-want-to-add-more-graphs-not-just-with-tensorboard-is-this-supported---")

Yes! The [`Logger`](https://clear.ml/docs/latest/docs/fundamentals/logger) module includes methods for explicit reporting. For examples of explicit reporting, see the [Explicit Reporting](https://clear.ml/docs/latest/docs/guides/reporting/explicit_reporting)
tutorial.

#### How can I report more than one scatter 2D series on the same plot? [​](https://clear.ml/docs/latest/docs/faq/\#how-can-i-report-more-than-one-scatter-2d-series-on-the-same-plot---- "Direct link to how-can-i-report-more-than-one-scatter-2d-series-on-the-same-plot----")

The [`Logger.report_scatter2d()`](https://clear.ml/docs/latest/docs/references/sdk/logger#report_scatter2d)
method reports all series with the same `title` and `iteration` parameter values on the same plot.

For example, the following two scatter2D series are reported on the same plot, because both have a `title` of `example_scatter` and an `iteration` of `1`:

```python
scatter2d_1 = np.hstack((np.atleast_2d(np.arange(0, 10)).T, np.random.randint(10, size=(10, 1))))

logger.report_scatter2d(

    title="example_scatter",

    series="series_1",

    iteration=1,

    scatter=scatter2d_1,

    xaxis="title x",

    yaxis="title y"

)



scatter2d_2 = np.hstack((np.atleast_2d(np.arange(0, 10)).T, np.random.randint(10, size=(10, 1))))

logger.report_scatter2d(

    title="example_scatter",

    series="series_2",

    iteration=1,

    scatter=scatter2d_2,

    xaxis="title x",

    yaxis="title y"

)
```

## GIT and Storage [​](https://clear.ml/docs/latest/docs/faq/\#git-and-storage "Direct link to GIT and Storage")

#### Is there something ClearML can do about uncommitted code running? [​](https://clear.ml/docs/latest/docs/faq/\#is-there-something-clearml-can-do-about-uncommitted-code-running---- "Direct link to is-there-something-clearml-can-do-about-uncommitted-code-running----")

Yes! ClearML stores the git diff as part of the task's information. You can view the git diff in the **ClearML Web UI >**
task's **EXECUTION** tab.

#### I read there is a feature for centralized model storage. How do I use it? [​](https://clear.ml/docs/latest/docs/faq/\#i-read-there-is-a-feature-for-centralized-model-storage-how-do-i-use-it--- "Direct link to i-read-there-is-a-feature-for-centralized-model-storage-how-do-i-use-it---")

When calling [`Task.init`](https://clear.ml/docs/latest/docs/references/sdk/task#taskinit),
providing the `output_uri` parameter lets you specify the location in which model checkpoints (snapshots) will be stored.

For example, to store model checkpoints (snapshots) in `/mnt/shared/folder`:

```python
task = Task.init(project_name, task_name, output_uri="/mnt/shared/folder")
```

ClearML will copy all stored snapshots into a subfolder under `/mnt/shared/folder`. The subfolder's name will contain
the task's ID. For example, if the task's ID is `6ea4f0b56d994320a713aeaf13a86d9d`, the following folder will be used:

```text
/mnt/shared/folder/task.6ea4f0b56d994320a713aeaf13a86d9d/models/
```

ClearML supports other storage types for `output_uri`:

- S3: `s3://bucket/folder`
- Non-AWS S3-like services (such as MinIO): `s3://host_addr:port/bucket`. **Note that port specification is required**.
- Google Cloud Storage: `gs://bucket-name/folder`
- Azure Storage: `azure://<account name>.blob.core.windows.net/path/to/file`

For example:

```python
# AWS S3 bucket

task = Task.init(project_name, task_name, output_uri="s3://bucket-name/folder")

# Google Cloud Storage bucket

task = Task.init(project_name, task_name, output_uri="gs://bucket-name/folder")
```

To use cloud storage with ClearML, configure the storage credentials in your `~/clearml.conf`. For detailed information,
see [ClearML Configuration Reference](https://clear.ml/docs/latest/docs/configs/clearml_conf).

#### When using PyCharm to remotely debug a machine, the Git repo is not detected. Do you have a solution? [​](https://clear.ml/docs/latest/docs/faq/\#when-using-pycharm-to-remotely-debug-a-machine-the-git-repo-is-not-detected-do-you-have-a-solution "Direct link to When using PyCharm to remotely debug a machine, the Git repo is not detected. Do you have a solution?")

Yes! ClearML provides a PyCharm plugin that allows a remote debugger to grab your local
repository / commit ID. For detailed information about using the plugin, see the [ClearML PyCharm Plugin](https://clear.ml/docs/latest/docs/guides/ide/integration_pycharm).

#### Debug images and/or artifacts are not loading in the UI after I migrated ClearML Server to a new address. How do I fix this? [​](https://clear.ml/docs/latest/docs/faq/\#debug-images-andor-artifacts-are-not-loading-in-the-ui-after-i-migrated-clearml-server-to-a-new-address-how-do-i-fix-this---- "Direct link to debug-images-andor-artifacts-are-not-loading-in-the-ui-after-i-migrated-clearml-server-to-a-new-address-how-do-i-fix-this----")

This can happen if your debug images and/or artifacts were uploaded to the ClearML file server, since the value
registered was their full URL at the time of registration (e.g. `https://files.<OLD_ADDRESS>/path/to/artifact`).

To fix this, the registered URL of each debug image and/or artifact needs to be replaced with its current URL.

- For **debug images**, use the following command. Make sure to insert the old address and the new address that will replace it:



important





Note that in the following command, the `'\''` sequences end with double single quotes (`''`) and not double quotes (`"`)









```bash
curl -XPOST -H "Content-Type: application/json" "localhost:9200/events-training_debug_image-*/_update_by_query?conflicts=proceed" -d'{

      "script": {

          "source": "ctx._source.url = ctx._source.url.replace('\''https://files.<OLD_ADDRESS>'\'', '\''https://files.<NEW_ADDRESS>'\'')",

          "lang": "painless"

      },

      "query": {"prefix": {"url": {"value": "https://files.<OLD_ADDRESS>"}}}

}'
```

- For **artifacts**, you can do the following:
1. Run shell in the `apiserver` container:





     ```bash
     sudo docker exec -it clearml-apiserver /bin/bash
     ```

2. Navigate to the `apiserver` folder:





     ```bash
     cd /opt/clearml/apiserver
     ```

3. Run the `fix_mongo_urls.py` script for fixing the artifacts. Make sure to insert the old address and the new
     address that will replace it:





     ```bash
     python3 fix_mongo_urls.py --host-source http://old_address_and_port --host-target http://new_address_and_port
     ```

## Jupyter [​](https://clear.ml/docs/latest/docs/faq/\#jupyter "Direct link to Jupyter")

#### I am using Jupyter Notebook. Is this supported? [​](https://clear.ml/docs/latest/docs/faq/\#i-am-using-jupyter-notebook-is-this-supported--- "Direct link to i-am-using-jupyter-notebook-is-this-supported---")

Yes! You can run ClearML in Jupyter Notebooks using either of the following:

- [Option 1: Install ClearML on your Jupyter Notebook host machine](https://clear.ml/docs/latest/docs/faq/#opt1)
- [Option 2: Install ClearML in your Jupyter Notebook and connect using ClearML credentials](https://clear.ml/docs/latest/docs/faq/#opt2)

**Option 1: Install ClearML on your Jupyter host machine**

1. Connect to your Jupyter host machine.

2. Install the ClearML Python Package:





```text
pip install clearml
```

3. Run the ClearML setup wizard:





```text
clearml-init
```

4. In your Jupyter Notebook, you can now use ClearML.


**Option 2: Install ClearML in your Jupyter Notebook**

1. Install the ClearML Python Package:





```text
pip install clearml
```

2. Get ClearML credentials. Open the ClearML Web UI in a browser. On the **SETTINGS > WORKSPACE** page, click **Create new credentials**.
The **JUPYTER NOTEBOOK** tab shows the commands required to configure your notebook (a copy to clipboard action is available on hover)

3. Add these commands to your notebook

4. You can now use ClearML in your notebook!





```python
# create a task and start training

task = Task.init(project_name='jupyter project', task_name='my notebook')
```


## Remote Debugging (ClearML PyCharm Plugin) [​](https://clear.ml/docs/latest/docs/faq/\#remote-debugging-clearml-pycharm-plugin "Direct link to Remote Debugging (ClearML PyCharm Plugin)")

#### I am using your ClearML PyCharm Plugin for remote debugging. I get the message "clearml.Task - INFO - Repository and package analysis timed out (10.0 sec), giving up". What should I do? [​](https://clear.ml/docs/latest/docs/faq/\#i-am-using-your-clearml-pycharm-plugin-for-remote-debugging-i-get-the-message-clearmltask---info---repository-and-package-analysis-timed-out-100-sec-giving-up-what-should-i-do-- "Direct link to i-am-using-your-clearml-pycharm-plugin-for-remote-debugging-i-get-the-message-clearmltask---info---repository-and-package-analysis-timed-out-100-sec-giving-up-what-should-i-do--")

ClearML uses a background thread to analyze the script. This includes package requirements. At the end of the execution
of the script, if the background thread is still running, ClearML allows the thread another 10 seconds to complete.
If the thread does not complete, it times out.

This can occur for scripts that do not import any packages, for example short test scripts.

To fix this issue, you can import the `time` package and add a `time.sleep(20)` statement to the end of your script.

## scikit-learn [​](https://clear.ml/docs/latest/docs/faq/\#scikit-learn "Direct link to scikit-learn")

#### Can I use ClearML with scikit-learn? [​](https://clear.ml/docs/latest/docs/faq/\#can-i-use-clearml-with-scikit-learn--- "Direct link to can-i-use-clearml-with-scikit-learn---")

Yes! `scikit-learn` is supported. ClearML automatically logs models which are stored using `joblib`.
For more information, see [scikit-learn](https://clear.ml/docs/latest/docs/integrations/scikit_learn).

## ClearML Configuration [​](https://clear.ml/docs/latest/docs/faq/\#clearml-configuration "Direct link to ClearML Configuration")

#### How do I explicitly specify the ClearML configuration file to be used? [​](https://clear.ml/docs/latest/docs/faq/\#how-do-i-explicitly-specify-the-clearml-configuration-file-to-be-used--- "Direct link to how-do-i-explicitly-specify-the-clearml-configuration-file-to-be-used---")

To override the default configuration file location, set the `CLEARML_CONFIG_FILE` OS environment variable.

For example:

```text
export CLEARML_CONFIG_FILE="/home/user/myclearml.conf"
```

#### How can I override ClearML credentials from the OS environment? [​](https://clear.ml/docs/latest/docs/faq/\#how-can-i-override-clearml-credentials-from-the-os-environment--- "Direct link to how-can-i-override-clearml-credentials-from-the-os-environment---")

To override your configuration file / defaults, set the following OS environment variables:

```text
export CLEARML_API_ACCESS_KEY="key_here"

export CLEARML_API_SECRET_KEY="secret_here"

export CLEARML_API_HOST="http://localhost:8008"
```

#### How can I track OS environment variables with tasks? [​](https://clear.ml/docs/latest/docs/faq/\#how-can-i-track-os-environment-variables-with-tasks---- "Direct link to how-can-i-track-os-environment-variables-with-tasks----")

You can set environment variables to track in a task by specifying them in the `sdk.development.log_os_environments`
field of the [`clearml.conf`](https://clear.ml/docs/latest/docs/configs/clearml_conf#log_env_var) file:

```editorconfig
log_os_environments: ["AWS_*", "CUDA_VERSION"]
```

You can also use the `CLEARML_LOG_ENVIRONMENT` variable to track environment variables:

- All environment variables:





```text
export CLEARML_LOG_ENVIRONMENT=*
```

- Specific environment variables, for example, log `PWD` and `PYTHONPATH`:





```text
export CLEARML_LOG_ENVIRONMENT=PWD,PYTHONPATH
```

- No environment variables:





```text
export CLEARML_LOG_ENVIRONMENT=
```


Overriding clearml.conf

The `CLEARML_LOG_ENVIRONMENT` variable always overrides the `clearml.conf` file.

## ClearML Hosted Service [​](https://clear.ml/docs/latest/docs/faq/\#clearml-hosted-service "Direct link to ClearML Hosted Service")

#### I run my script, but my task is not in the ClearML Hosted Service Web UI. How do I fix this? [​](https://clear.ml/docs/latest/docs/faq/\#i-run-my-script-but-my-task-is-not-in-the-clearml-hosted-service-web-ui-how-do-i-fix-this--- "Direct link to i-run-my-script-but-my-task-is-not-in-the-clearml-hosted-service-web-ui-how-do-i-fix-this---")

If you joined the ClearML Hosted Service and ran a script, but your task does not appear in Web UI, you may not have configured ClearML for the hosted service. Run the ClearML setup wizard. It will request your hosted service ClearML credentials and create the ClearML configuration you need.

```text
pip install clearml



clearml-init
```

## ClearML Server Deployment [​](https://clear.ml/docs/latest/docs/faq/\#clearml-server-deployment "Direct link to ClearML Server Deployment")

#### How do I deploy ClearML Server on stand-alone Linux Ubuntu or macOS systems? [​](https://clear.ml/docs/latest/docs/faq/\#how-do-i-deploy-clearml-server-on-stand-alone-linux-ubuntu-or-macos-systems--- "Direct link to how-do-i-deploy-clearml-server-on-stand-alone-linux-ubuntu-or-macos-systems---")

For detailed instructions, see [Deploying ClearML Server: Linux or macOS](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_linux_mac).

#### How do I deploy ClearML Server on Windows 10? [​](https://clear.ml/docs/latest/docs/faq/\#how-do-i-deploy-clearml-server-on-windows-10--- "Direct link to how-do-i-deploy-clearml-server-on-windows-10---")

For detailed instructions, see [Deploying ClearML Server: Windows 10](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_win).

#### How do I deploy ClearML Server on AWS EC2 AMIs? [​](https://clear.ml/docs/latest/docs/faq/\#how-do-i-deploy-clearml-server-on-aws-ec2-amis--- "Direct link to how-do-i-deploy-clearml-server-on-aws-ec2-amis---")

For detailed instructions, see [Deploying ClearML Server: AWS EC2 AMIs](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_aws_ec2_ami).

#### How do I deploy ClearML Server on the Google Cloud Platform? [​](https://clear.ml/docs/latest/docs/faq/\#how-do-i-deploy-clearml-server-on-the-google-cloud-platform--- "Direct link to how-do-i-deploy-clearml-server-on-the-google-cloud-platform---")

For detailed instructions, see [Deploying ClearML Server: Google Cloud Platform](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_gcp).

#### How do I restart ClearML Server? [​](https://clear.ml/docs/latest/docs/faq/\#how-do-i-restart-clearml-server--- "Direct link to how-do-i-restart-clearml-server---")

For detailed instructions, see the "Restarting" section of the documentation page for your deployment format. For example,
if you deployed to Linux, see [Restarting](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_linux_mac#restarting) on the "Deploying ClearML Server: Linux or macOS" page.

#### Can I create a Helm Chart for ClearML Server Kubernetes deployment? [​](https://clear.ml/docs/latest/docs/faq/\#can-i-create-a-helm-chart-for-clearml-server-kubernetes-deployment--- "Direct link to can-i-create-a-helm-chart-for-clearml-server-kubernetes-deployment---")

Yes! You can create a Helm Chart of ClearML Server Kubernetes deployment. For detailed instructions,
see [Deploying ClearML Server: Kubernetes using Helm](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_kubernetes_helm).

#### My Docker cannot load a local host directory on SELinux? [​](https://clear.ml/docs/latest/docs/faq/\#my-docker-cannot-load-a-local-host-directory-on-selinux--- "Direct link to my-docker-cannot-load-a-local-host-directory-on-selinux---")

If you are using SELinux, run the following command (see this [discussion](https://stackoverflow.com/a/24334000)):

```text
chcon -Rt svirt_sandbox_file_t /opt/clearml
```

## ClearML Server Configuration [​](https://clear.ml/docs/latest/docs/faq/\#clearml-server-configuration "Direct link to ClearML Server Configuration")

#### How do I configure ClearML Server for subdomains and load balancers? [​](https://clear.ml/docs/latest/docs/faq/\#how-do-i-configure-clearml-server-for-subdomains-and-load-balancers--- "Direct link to how-do-i-configure-clearml-server-for-subdomains-and-load-balancers---")

For detailed instructions, see [Configuring Subdomains and load balancers](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_config#subdomains-and-load-balancers).

#### Can I add web login authentication to ClearML Server? [​](https://clear.ml/docs/latest/docs/faq/\#can-i-add-web-login-authentication-to-clearml-server--- "Direct link to can-i-add-web-login-authentication-to-clearml-server---")

By default, anyone can log in to the ClearML Server WebApp. You can configure the ClearML Server to allow only a specific set of users to access the system.

For detailed instructions, see [Web Login Authentication](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_config#web-login-authentication).

#### Can I modify non-responsive task settings? [​](https://clear.ml/docs/latest/docs/faq/\#can-i-modify-non-responsive-task-settings--- "Direct link to can-i-modify-non-responsive-task-settings---")

The non-responsive task watchdog monitors tasks that were not updated for a specified time interval, and
marks them as `aborted`. The watchdog is always active.

You can modify the following settings for the watchdog:

- The time threshold (in seconds) of task inactivity (default value is 7200 seconds which is 2 hours).
- The time interval (in seconds) between watchdog cycles.

For detailed instructions, see [Modifying non-responsive Task watchdog settings](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_config#non-responsive-task-watchdog).

## ClearML Server Troubleshooting [​](https://clear.ml/docs/latest/docs/faq/\#clearml-server-troubleshooting "Direct link to ClearML Server Troubleshooting")

#### After reinstalling, why can't I create credentials in the WebApp (UI)? [​](https://clear.ml/docs/latest/docs/faq/\#after-reinstalling-why-cant-i-create-credentials-in-the-webapp-ui--- "Direct link to after-reinstalling-why-cant-i-create-credentials-in-the-webapp-ui---")

The issue is likely your browser cookies for ClearML Server. Clearing your browser cookies for ClearML Server is recommended.
For example:

- For Firefox - go to Developer Tools > Storage > Cookies > delete all cookies under the ClearML Server URL.
- For Chrome - Developer Tools > Application > Cookies > delete all cookies under the ClearML Server URL.

#### How do I fix Docker upgrade errors? [​](https://clear.ml/docs/latest/docs/faq/\#how-do-i-fix-docker-upgrade-errors--- "Direct link to how-do-i-fix-docker-upgrade-errors---")

To resolve the Docker error:

```text
... The container name "/trains-???" is already in use by ...
```

try removing deprecated images:

```text
$ docker rm -f $(docker ps -a -q)
```

#### Why is web login authentication not working? [​](https://clear.ml/docs/latest/docs/faq/\#why-is-web-login-authentication-not-working--- "Direct link to why-is-web-login-authentication-not-working---")

A port conflict between the ClearML Server MongoDB and/or Elastic instances, and other instances running on your system may prevent web login authentication from working correctly.

ClearML Server uses the following default ports which may be in conflict with other instances:

- MongoDB port `27017`
- Elastic port `9200`

You can check for port conflicts in the logs in `/opt/clearml/log`.

If a port conflict occurs, change the MongoDB and/or Elastic ports in the `docker-compose.yml`, and then run the Docker compose commands to restart the ClearML Server instance.

To change the MongoDB and/or Elastic ports for your ClearML Server, do the following:

1. Edit the `docker-compose.yml` file.

2. Add the following environment variable(s) in the `services/trainsserver/environment` section:
   - For MongoDB:





     ```bash
     MONGODB_SERVICE_PORT: <new-mongodb-port>
     ```

   - For Elastic:





     ```bash
     ELASTIC_SERVICE_PORT: <new-elasticsearch-port>
     ```









     For example:





     ```bash
     MONGODB_SERVICE_PORT: 27018

     ELASTIC_SERVICE_PORT: 9201
     ```
3. For MongoDB, in the `services/mongo_4/ports` section, expose the new MongoDB port:





```bash
<new-mongodb-port>:27017
```









For example:





```bash
20718:27017
```

4. For Elastic, in the `services/elasticsearch/ports` section, expose the new Elastic port:





```bash
<new-elasticsearch-port>:9200
```









For example:





```bash
9201:9200
```

5. Restart ClearML Server, see [Restarting ClearML Server](https://clear.ml/docs/latest/docs/faq/#restart).


#### How do I bypass a proxy configuration to access my local ClearML Server? [​](https://clear.ml/docs/latest/docs/faq/\#how-do-i-bypass-a-proxy-configuration-to-access-my-local-clearml-server--- "Direct link to how-do-i-bypass-a-proxy-configuration-to-access-my-local-clearml-server---")

A proxy server may block access to ClearML Server configured for `localhost`.

To fix this, you may allow bypassing of your proxy server to `localhost` using a system environment variable, and configure ClearML for ClearML Server using it.

Do the following:

1. Allow bypassing of your proxy server to `localhost`
using a system environment variable, for example:





```text
NO_PROXY = localhost
```

2. If a ClearML configuration file (`clearml.conf`) exists, delete it.

3. Open a terminal session.

4. Set the system environment variable to `127.0.0.1` in the terminal session. For example:
   - Linux:





     ```bash
     no_proxy=127.0.0.1

     NO_PROXY=127.0.0.1
     ```

   - Windows:





     ```bash
     set no_proxy=127.0.0.1

     set NO_PROXY=127.0.0.1
     ```
5. Run the ClearML wizard `clearml-init` to configure ClearML for ClearML Server, which will prompt you to open the ClearML Web UI at, [http://127.0.0.1:8080/](http://127.0.0.1:8080/), and create new ClearML credentials.

The wizard completes with:





```text
Verifying credentials ...

Credentials verified!

New configuration stored in /home/<username>/clearml.conf

ClearML setup completed successfully.
```


#### Why am I getting a `413 Request Entity Too Large` error when uploading files? [​](https://clear.ml/docs/latest/docs/faq/\#why-am-i-getting-a-413-request-entity-too-large-error-when-uploading-files-- "Direct link to why-am-i-getting-a-413-request-entity-too-large-error-when-uploading-files--")

`413 Request Entity Too Large` error indicates that the request payload exceeds the maximum size allowed by the HTTP
server, reverse proxy, or load balancer fronting your ClearML server. This can occur, for example, when ClearML is
deployed on K8s behind an NGINX ingress controller, where the default request size limit is typically 1 MB.

To resolve this issue, Increase the allowed request body size in your HTTP server configuration.
For example, if you are using a K8s NGINX ingress controller, add the following configuration under both the `apiserver`
and `fileserver` sections of your Helm values override file (e.g. `clearml-values.override.yaml`).

```yaml
apiserver:

 ingress:

   enabled: true

   annotations:

     nginx.ingress.kubernetes.io/proxy-body-size: "100m"

fileserver:

 ingress:

   enabled: true

   annotations:

     nginx.ingress.kubernetes.io/proxy-body-size: "100m"
```

Adjust the value (`100m`) based on your requirements, or set it to `"0"` to remove the limit entirely.

##### Apply the changes [​](https://clear.ml/docs/latest/docs/faq/\#apply-the-changes "Direct link to Apply the changes")

Apply the configuration using `helm upgrade`.

- ClearML Enterprise:





```text
helm upgrade -i -n clearml clearml-enterprise \

    oci://docker.io/clearml/clearml-enterprise \

    --create-namespace \

    -f clearml-values.override.yaml
```

- Open Source:





```text
helm upgrade clearml clearml/clearml \

    --version <CURRENT_CHART_VERSION> \

    -f clearml-values.override.yaml
```


#### The ClearML Server keeps returning HTTP 500 (or 400) errors. How do I fix this? [​](https://clear.ml/docs/latest/docs/faq/\#the-clearml-server-keeps-returning-http-500-or-400-errors-how-do-i-fix-this--- "Direct link to the-clearml-server-keeps-returning-http-500-or-400-errors-how-do-i-fix-this---")

The ClearML Server will return HTTP error responses (5XX, or 4XX) when some of its [backend components](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server)
are failing.

A common cause for such a failure is low available disk space, as the Elasticsearch service used by your server will go
into read-only mode when it hits Elasticsearch flood watermark (by default, set to 95% disk space used).

This can be readily fixed by making more disk space available to the Elasticsearch service (either freeing up disk space
disk, or if using dynamic cloud storage, increasing the disk size).

note

A likely indication of this situation can be determined by searching your clearml logs for _"\[FORBIDDEN/12/index read-only_\
_/ allow delete (api)\]_".

#### Why is my ClearML WebApp (UI) not showing any data? [​](https://clear.ml/docs/latest/docs/faq/\#why-is-my-clearml-webapp-ui-not-showing-any-data--- "Direct link to why-is-my-clearml-webapp-ui-not-showing-any-data---")

If your ClearML WebApp (UI) does not show anything, it may be an error authenticating with the server. Try clearing the application cookies for the site in your browser's developer tools.

#### Why can't I access my ClearML Server when I run my code in a virtual machine? [​](https://clear.ml/docs/latest/docs/faq/\#why-cant-i-access-my-clearml-server-when-i-run-my-code-in-a-virtual-machine--- "Direct link to why-cant-i-access-my-clearml-server-when-i-run-my-code-in-a-virtual-machine---")

The network definitions inside a virtual machine (or container) are different from those of the host. The virtual machine's
and the server machine's IP addresses are different, so you have to make sure that the machine that is executing the
task can access the server's machine.

Make sure to have an independent configuration file for the virtual machine where you are running your tasks.
Edit the `api` section of your `clearml.conf` file and insert IP addresses of the server machine that are accessible
from the VM. It should look something like this:

```text
api {

    web_server: http://192.168.1.2:8080

    api_server: http://192.168.1.2:8008

    credentials {

        "access_key" = "KEY"

        "secret_key" = "SECRET"

    }

}
```

## ClearML Agent [​](https://clear.ml/docs/latest/docs/faq/\#clearml-agent "Direct link to ClearML Agent")

#### How can I execute ClearML Agent without installing packages each time? [​](https://clear.ml/docs/latest/docs/faq/\#how-can-i-execute-clearml-agent-without-installing-packages-each-time--- "Direct link to how-can-i-execute-clearml-agent-without-installing-packages-each-time---")

Instead of installing the Python packages in the virtual environment created by ClearML Agent, you can optimize execution
time by inheriting the packages from your global site-packages directory. In the ClearML configuration file, set the
configuration option `agent.package_manager.system_site_packages` to `true`.

## ClearML API [​](https://clear.ml/docs/latest/docs/faq/\#clearml-api "Direct link to ClearML API")

#### How can I use the ClearML API to fetch data? [​](https://clear.ml/docs/latest/docs/faq/\#how-can-i-use-the-clearml-api-to-fetch-data--- "Direct link to how-can-i-use-the-clearml-api-to-fetch-data---")

You can use the `APIClient` class, which provides a Pythonic interface to access ClearML's backend REST API. Through
an `APIClient` instance, you can access ClearML's REST API services and endpoints.

To use `APIClient`, create an instance of it, then call the method corresponding to the desired REST API endpoint, with
its respective parameters as described in the [REST API reference page](https://clear.ml/docs/latest/docs/references/api/).

For example, the [`POST/ projects.get_all`](https://clear.ml/docs/latest/docs/references/api/projects#post-projectsget_all) call returns all projects
in your workspace. The following code uses APIClient to retrieve a list of all projects whose name starts with "example."

```python
from clearml.backend_api.session.client import APIClient

# Create an instance of APIClient

client = APIClient()

project_list = client.projects.get_all(name="example*")

print(project_list)
```

For more information, see [`APIClient`](https://clear.ml/docs/latest/docs/clearml_sdk/apiclient_sdk).

- [General Information](https://clear.ml/docs/latest/docs/faq/#general-information)
- [Models](https://clear.ml/docs/latest/docs/faq/#models)
- [Tasks](https://clear.ml/docs/latest/docs/faq/#tasks)
- [Graphs and Logs](https://clear.ml/docs/latest/docs/faq/#graphs-and-logs)
- [GIT and Storage](https://clear.ml/docs/latest/docs/faq/#git-and-storage)
- [Jupyter](https://clear.ml/docs/latest/docs/faq/#jupyter)
- [Remote Debugging (ClearML PyCharm Plugin)](https://clear.ml/docs/latest/docs/faq/#remote-debugging-clearml-pycharm-plugin)
- [scikit-learn](https://clear.ml/docs/latest/docs/faq/#scikit-learn)
- [ClearML Configuration](https://clear.ml/docs/latest/docs/faq/#clearml-configuration)
- [ClearML Hosted Service](https://clear.ml/docs/latest/docs/faq/#clearml-hosted-service)
- [ClearML Server Deployment](https://clear.ml/docs/latest/docs/faq/#clearml-server-deployment)
- [ClearML Server Configuration](https://clear.ml/docs/latest/docs/faq/#clearml-server-configuration)
- [ClearML Server Troubleshooting](https://clear.ml/docs/latest/docs/faq/#clearml-server-troubleshooting)
- [ClearML Agent](https://clear.ml/docs/latest/docs/faq/#clearml-agent)
- [ClearML API](https://clear.ml/docs/latest/docs/faq/#clearml-api)