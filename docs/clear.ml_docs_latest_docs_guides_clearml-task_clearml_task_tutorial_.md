---
url: "https://clear.ml/docs/latest/docs/guides/clearml-task/clearml_task_tutorial/"
title: "ClearML Task Tutorial | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/clearml-task/clearml_task_tutorial/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

In this tutorial, you will use `clearml-task` to execute [a script](https://github.com/clearml/events/blob/master/webinar-0620/keras_mnist.py)
on a remote or local machine, from a remote repository and your local machine.

### Prerequisites [​](https://clear.ml/docs/latest/docs/guides/clearml-task/clearml_task_tutorial/\#prerequisites "Direct link to Prerequisites")

- [`clearml`](https://clear.ml/docs/latest/docs/clearml_sdk/clearml_sdk_setup) Python package installed and configured
- [`clearml-agent`](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_deployment_bare_metal#installation) running on at least one machine (to execute the task), configured to listen to `default` queue

### Executing Code from a Remote Repository [​](https://clear.ml/docs/latest/docs/guides/clearml-task/clearml_task_tutorial/\#executing-code-from-a-remote-repository "Direct link to Executing Code from a Remote Repository")

```bash
clearml-task --project keras_examples --name remote_test --repo https://github.com/clearml/events.git --branch master --script /webinar-0620/keras_mnist.py --args batch_size=64 epochs=1 --queue default
```

This sets the following arguments:

- `--project keras_examples --name remote_test` \- The project and task names
- `--repo https://github.com/clearml/events.git` \- The repository's URL. By default, `clearml-task` uses the latest
commit from the master branch
- `--branch master` \- The repository branch
- `--script /webinar-0620/keras_mnist.py` \- The script to be executed
- `--args batch_size=64 epochs=1` \- Arguments passed to the script. This uses the `argparse` object to get CLI parameters
- `--queue default` \- Selected queue to send the task to

Adding Requirements

`clearml-task` automatically finds the requirements.txt file in remote repositories.
If a remote repo does not have such a file, make sure to either add one with all the required Python packages,
or add the `--packages "<package_name>"` option to the command (for example: `--packages "tqdm>=2.1" "scikit-learn"`).

Now `clearml-task` does all the heavy-lifting!

1. It creates a new [ClearML Task](https://clear.ml/docs/latest/docs/fundamentals/task)
2. `clearml-task` enqueues the task in the selected execution queue, where a [ClearML Agent](https://clear.ml/docs/latest/docs/clearml_agent)
assigned to that queue executes the task

Your output should look something like this:

```console
New task created id=2f96ee95b05d4693b360d0fcbb26b727

Task id=2f96ee95b05d4693b360d0fcbb26b727 sent for execution on queue default

Execution log at: https://app.clear.ml/projects/552d5399112d47029c146d5248570295/experiments/2f96ee95b05d4693b360d0fcbb26b727/output/log
```

### Executing a Local Script [​](https://clear.ml/docs/latest/docs/guides/clearml-task/clearml_task_tutorial/\#executing-a-local-script "Direct link to Executing a Local Script")

For this example, use a local version of [this script](https://github.com/clearml/events/blob/master/webinar-0620/keras_mnist.py).

1. Clone the [clearml/events](https://github.com/clearml/events) repository
2. Go to the root folder of the cloned repository
3. Run the following command:

```bash
clearml-task --project keras --name local_test --script webinar-0620/keras_mnist.py --branch master --requirements webinar-0620/requirements.txt --args epochs=1 --queue default
```

This sets the following arguments:

- `--project keras --name local_test` \- The project and task names
- `--script /webinar-0620/keras_mnist.py` \- The local script to be executed
- `-requirements webinar-0620/requirements.txt` \- The local Python package requirements file
- `--args batch_size=64 epochs=1` \- Arguments passed to the script. This uses the argparse object to capture CLI parameters
- `--queue default` \- Selected queue to send the task to

`clearml-task` creates a task according to the input parameters, and sends the task to the `default` queue for execution.

- [Prerequisites](https://clear.ml/docs/latest/docs/guides/clearml-task/clearml_task_tutorial/#prerequisites)
- [Executing Code from a Remote Repository](https://clear.ml/docs/latest/docs/guides/clearml-task/clearml_task_tutorial/#executing-code-from-a-remote-repository)
- [Executing a Local Script](https://clear.ml/docs/latest/docs/guides/clearml-task/clearml_task_tutorial/#executing-a-local-script)