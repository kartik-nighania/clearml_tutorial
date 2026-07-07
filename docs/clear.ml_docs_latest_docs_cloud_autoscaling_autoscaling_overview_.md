---
url: "https://clear.ml/docs/latest/docs/cloud_autoscaling/autoscaling_overview/"
title: "Cloud Autoscaling | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/cloud_autoscaling/autoscaling_overview/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

9 - The ClearML Autoscaler - YouTube

Tap to unmute

[9 - The ClearML Autoscaler](https://www.youtube.com/watch?v=j4XVMAaUt3E) [ClearML](https://www.youtube.com/channel/UCDYdA4hjckRLRVBrCoKenCQ)

ClearML2.62K subscribers

Using [ClearML Agent](https://clear.ml/docs/latest/docs/clearml_agent) and [queues](https://clear.ml/docs/latest/docs/fundamentals/agents_and_queues#what-is-a-queue), you can
easily run your code remotely on more powerful machines, including cloud instances.

Manually spinning up new virtual machines and setting up ClearML Agents on them can become a recurring task as your
workload grows, not to mention avoiding paying for running machines that aren’t being used, which can become pricey.
This is where autoscaling comes into the picture.

ClearML provides the following options to automate your resource scaling, while optimizing machine usage:

- [ClearML autoscaler applications](https://clear.ml/docs/latest/docs/cloud_autoscaling/autoscaling_overview/#autoscaler-applications) \- Use the apps to define your compute resource budget,
and have the apps automatically manage your resource consumption as needed–with no code!
- [Kubernetes integration](https://clear.ml/docs/latest/docs/cloud_autoscaling/autoscaling_overview/#kubernetes) \- Deploy agents through Kubernetes, which handles resource management and scaling

## Autoscaler Applications [​](https://clear.ml/docs/latest/docs/cloud_autoscaling/autoscaling_overview/\#autoscaler-applications "Direct link to Autoscaler Applications")

ClearML provides the following GUI autoscaler applications:

- [AWS Autoscaler](https://clear.ml/docs/latest/docs/webapp/applications/apps_aws_autoscaler)
- [GCP Autoscaler](https://clear.ml/docs/latest/docs/webapp/applications/apps_gcp_autoscaler)

The autoscalers automatically spin up or down cloud instances as needed and according to a budget that you set, so you
pay only for the time that you actually use the machines.

The **AWS** and **GCP** autoscaler applications will manage instances on your behalf in your cloud account. When
launching an app instance, you will provide your cloud service credentials so the autoscaler can access your account.

## How ClearML Autoscaler Apps Work [​](https://clear.ml/docs/latest/docs/cloud_autoscaling/autoscaling_overview/\#how-clearml-autoscaler-apps-work "Direct link to How ClearML Autoscaler Apps Work")

![Autoscaler diagram](https://clear.ml/docs/latest/assets/images/autoscaler_single_queue_diagram-e7261552107fc413de4c26d9d150e7af.png)

The diagram above demonstrates a typical flow for executing tasks through an autoscaler app:

1. [Create a queue](https://clear.ml/docs/latest/docs/webapp/webapp_workers_queues#queues) to attach the autoscaler to
2. Set up an autoscaler app instance: assign it to a queue and define a compute resource budget (see the specific
autoscaler pages for further setup details)
3. Launch the autoscaler app instance
4. Enqueue a task to the queue the autoscaler has been assigned to
5. The autoscaler attached to the queue spins up and prepares a new compute resource to execute the enqueued task
6. Enqueue additional tasks: if there are not enough machines to execute the tasks, the autoscaler spins up additional
machines to execute the tasks (until the maximum number specified in the budget is reached)
7. If a machine becomes idle since there are no tasks to execute, the autoscaler automatically spins it down

### Utilizing Multiple Compute Resource Types [​](https://clear.ml/docs/latest/docs/cloud_autoscaling/autoscaling_overview/\#utilizing-multiple-compute-resource-types "Direct link to Utilizing Multiple Compute Resource Types")

You can work with multiple compute resources through the autoscalers, where each compute resource is associated with a
different queue. When a queue detects a task, the autoscaler spins up the appropriate resource to execute the task.

![Autoscaler diagram](https://clear.ml/docs/latest/assets/images/autoscaler_diagram-ffbbbcbcee423464175dae8b83f0c4a0.png)

The diagram above demonstrates an example where an autoscaler app instance is attached to two queues. Each queue is
associated with a different resource, CPU and GPU, and each queue has two enqueued tasks. To execute the tasks,
the autoscaler spins up four machines, two CPU machines to execute the tasks in the CPU queue and two GPU machines to
execute the tasks in the GPU queue.

### Task Execution Configuration [​](https://clear.ml/docs/latest/docs/cloud_autoscaling/autoscaling_overview/\#task-execution-configuration "Direct link to Task Execution Configuration")

#### Docker [​](https://clear.ml/docs/latest/docs/cloud_autoscaling/autoscaling_overview/\#docker "Direct link to Docker")

Every task a cloud instance pulls will be run inside a docker container. When setting up an autoscaler app instance,
you can specify a default container to run the tasks inside. If the task has its own container configured, it will
override the autoscaler’s default docker image (see [Base Container](https://clear.ml/docs/latest/docs/getting_started/clearml_agent_base_docker#base-container)).

#### Git Configuration [​](https://clear.ml/docs/latest/docs/cloud_autoscaling/autoscaling_overview/\#git-configuration "Direct link to Git Configuration")

If your code is saved in a private repository, you can add your Git credentials so the ClearML Agents running on your
cloud instances will be able to retrieve the code from your repos.

#### Cloud Storage Access [​](https://clear.ml/docs/latest/docs/cloud_autoscaling/autoscaling_overview/\#cloud-storage-access "Direct link to Cloud Storage Access")

If your tasks need to access data stored in cloud storage, you can provide your cloud storage credentials, so the
executed tasks will have access to your storage service.

#### Additional Configuration [​](https://clear.ml/docs/latest/docs/cloud_autoscaling/autoscaling_overview/\#additional-configuration "Direct link to Additional Configuration")

Go to a specific app’s documentation page to view all configuration options:

- [AWS Autoscaler](https://clear.ml/docs/latest/docs/webapp/applications/apps_aws_autoscaler)
- [GCP Autoscaler](https://clear.ml/docs/latest/docs/webapp/applications/apps_gcp_autoscaler)

## Kubernetes [​](https://clear.ml/docs/latest/docs/cloud_autoscaling/autoscaling_overview/\#kubernetes "Direct link to Kubernetes")

You can install `clearml-agent` through a Helm chart.

The Clearml Agent deployment is set to service a queue(s). When tasks are added to the queues, the agent pulls the task
and creates a pod to execute the task. Kubernetes handles resource management. Your task pod will remain pending until
enough resources are available.

You can set up Kubernetes' cluster autoscaler to work with your cloud providers, which automatically adjusts the size of
your Kubernetes cluster as needed; increasing the amount of nodes when there aren't enough to execute pods and removing
underutilized nodes. See [charts](https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler/charts/cluster-autoscaler) for specific cloud providers.

Enterprise features

The ClearML Enterprise plan supports K8s servicing multiple ClearML queues, as well as providing a pod template for each
queue for describing the resources for each pod to use. See [ClearML Helm Charts](https://github.com/clearml/clearml-helm-charts/tree/main).

- [Autoscaler Applications](https://clear.ml/docs/latest/docs/cloud_autoscaling/autoscaling_overview/#autoscaler-applications)
- [How ClearML Autoscaler Apps Work](https://clear.ml/docs/latest/docs/cloud_autoscaling/autoscaling_overview/#how-clearml-autoscaler-apps-work)
  - [Utilizing Multiple Compute Resource Types](https://clear.ml/docs/latest/docs/cloud_autoscaling/autoscaling_overview/#utilizing-multiple-compute-resource-types)
  - [Task Execution Configuration](https://clear.ml/docs/latest/docs/cloud_autoscaling/autoscaling_overview/#task-execution-configuration)
- [Kubernetes](https://clear.ml/docs/latest/docs/cloud_autoscaling/autoscaling_overview/#kubernetes)