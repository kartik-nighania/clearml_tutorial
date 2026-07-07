---
url: "https://clear.ml/docs/latest/docs/webapp/applications/apps_gcp_autoscaler/"
title: "GCP Autoscaler | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/webapp/applications/apps_gcp_autoscaler/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

Pro Plan Offering

The ClearML GCP Autoscaler App is available under the ClearML Pro plan.

The GCP Autoscaler Application optimizes GCP VM instance usage according to a user defined instance budget: Define your
budget by specifying the type and amount of available compute resources.

Each resource type is associated with a ClearML [queue](https://clear.ml/docs/latest/docs/fundamentals/agents_and_queues#what-is-a-queue) whose
status determines the need for instances of that resource type (i.e. spin up new instances if there are pending jobs on
the queue).

When running, the autoscaler periodically polls your GCP cluster. The autoscaler automatically deletes idle VM instances
based on a specified maximum idle time, or spins up new VM instances when there aren't enough to execute pending tasks
in a queue (until reaching the defined maximum number of instances). You can add an init script, which will be executed
when each VM instance is spun up.

For more information about how autoscalers work, see [Autoscalers Overview](https://clear.ml/docs/latest/docs/cloud_autoscaling/autoscaling_overview#autoscaler-applications).

Once an autoscaler is launched, the autoscaler's dashboard provides information about available VM instances and their
status:

- Number of idle instances
- Number of pending jobs
- Maximum idle time - The amount of time an instance can be idle before the autoscaler shuts it down
- `Shutdown idle instance now` \- Click to terminate all idle instances
- Autoscaler status and warnings
- Autoscaler Shutdown Action - Displays what the autoscaler does with instances it launched when it is shut down.
Click `Change shutdown action` to modify the behavior upon shutdown. Options include:

  - Do nothing (instances remain running)
  - Shut down all idle cloud instances
  - Shut down all cloud instances, including those running tasks
- Instance graphs
  - Available instances - Number of current running instances and their associated resources
  - Running Instances by compute resource type over time
  - Running instances by instance type over time
  - Queues and the resource type associated with them
  - Total uptime by resource type
- Instance logs - A table of instances that were spun up, including their type, associated resource, and spin-up time.

Console Debugging

To make the autoscaler console log show additional debug information, change an active app instance's log level to DEBUG:

1. Go to the app instance task's page > **CONFIGURATION** tab > **USER PROPERTIES** section
2. Hover over the section > Click `Edit` \> Click `+ADD PARAMETER`
3. Input `log_level` as the key and `DEBUG` as the value of the new parameter.

![Autoscaler debugging](https://clear.ml/docs/latest/assets/images/webapp_autoscaler_debug_log-1983e9f5a727714df0e4b4161d22de71.png)

The console's log level will update in the autoscaler's next iteration.

- Instance log files - Click to access the app instance's logs. This takes you to the app instance task's ARTIFACTS tab,
which lists the app instance's logs. In a log's `File Path` field, click ![Download](https://clear.ml/docs/latest/icons/ico-download-json.svg)
to download the complete log.

![GCP autoscaler dashboard](https://clear.ml/docs/latest/assets/images/apps_gcp_autoscaler-c6b2bc99b66ba3bd3b51e9d016c7ec3e.png#light-mode-only)![GCP autoscaler dashboard](https://clear.ml/docs/latest/assets/images/apps_gcp_autoscaler_dark-c4f8eacd7a0cbbaa8bda5fb746f0a252.png#dark-mode-only)

Embedding ClearML Visualization

You can embed plots from the app instance dashboard into [ClearML Reports](https://clear.ml/docs/latest/docs/webapp/webapp_reports). The Enterprise Plan and
Hosted Service also support embedding resources in third-party platforms that support embedded content (e.g. Notion). These visualizations
are updated live as the app instance(s) updates. Hover over the plot and click ![Embed code](https://clear.ml/docs/latest/icons/ico-plotly-embed-code.svg)
to copy the embed code, and navigate to a report to paste the embed code.

## Autoscaler Instance Configuration [​](https://clear.ml/docs/latest/docs/webapp/applications/apps_gcp_autoscaler/\#autoscaler-instance-configuration "Direct link to Autoscaler Instance Configuration")

When configuring a new GCP Autoscaler instance, you can fill in the required parameters or reuse the configuration of
a previously launched instance.

Launch an app instance with the configuration of a previously launched instance using one of the following options:

- Cloning a previously launched app instance will open the instance launch form with the original instance's
configuration prefilled.
- Importing an app configuration file. You can export the configuration of a previously launched instance as a JSON file
when viewing its configuration.

The prefilled instance launch form can be edited before starting the new app instance.

To configure a new app instance, click `Launch New`![Add new](https://clear.ml/docs/latest/icons/ico-add.svg)
to open the app's instance launch form.

### Configuration Options [​](https://clear.ml/docs/latest/docs/webapp/applications/apps_gcp_autoscaler/\#configuration-options "Direct link to Configuration Options")

note

Administrators can [customize](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/app_launch_form_custom) the launch form and
modify field names and/or available options and defaults.

This section describes the default configuration provided by ClearML.

- **Import Configuration** \- Import an app instance configuration file. This will fill the instance launch form with the
values from the file, which can be modified before launching the app instance
- **GCP Configuration**
  - GCP Project ID - Project used for spinning up VM instances
  - GCP Zone - The GCP zone where the VM instances will be spun up. See [Regions and zones](https://cloud.google.com/compute/docs/regions-zones)
  - Use full subnet path - Select to specify a full subnet path (i.e. referencing a subnet from a different project)
    - GCP Subnet Full Path - Available if `Use full subnet path` was selected. The GCP subnetwork where the instances
      will be spun up. This allows setting a custom subnet resource path, and allows setting subnets shared from other
      projects as well. See [GCP Documentation](https://cloud.google.com/dataflow/docs/guides/specifying-networks).
  - GCP Subnet Name - Available if `Use full subnet path` was not selected. The GCP subnetwork where the instances
    will be spun up. GCP setting will be `projects/{project-id}/regions/{region}/subnetworks/{subnetwork}`
  - GCP Credentials - Credentials with which the autoscaler can access your GCP account for spinning VM instances
    up/down. See [Generating GCP Credentials](https://clear.ml/docs/latest/docs/webapp/applications/apps_gcp_autoscaler/#generating-gcp-credentials).
- **Git Configuration**\- Git credentials with which the ClearML Agents running on your VM instances will access your
repositories to retrieve the code for their jobs

  - Git User
  - Git Password / Personal Access Token
- **Use docker mode** \- If selected, tasks enqueued to the autoscaler will be executed by ClearML Agents running in
[Docker mode](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_execution_env#docker-mode)
- **Base Docker Image** (optional) - Available when `Use docker mode` is selected. Default Docker image in which the ClearML Agent will run. Provide an image stored in a
Docker artifactory so VM instances can automatically fetch it
- **Compute Resources**

  - Resource Name - Assign a name to the resource type. This name will appear in the autoscaler dashboard
  - GCP Machine Type - See list of [machine types](https://cloud.google.com/compute/docs/machine-types)
  - Run in CPU mode - Select to have the autoscaler utilize only CPU VM instances
  - GPU Type - See list of [supported GPUs by instance](https://cloud.google.com/compute/docs/gpus)
  - Use Preemptible Instance - Choose whether VM instances of this type will be [preemptible](https://cloud.google.com/compute/docs/instances/preemptible)
    - Preemptible Provision Model - Select the provision model. For more information, see [Spot VMs](https://cloud.google.com/compute/docs/instances/spot)
      and [Preemptible VMs](https://cloud.google.com/compute/docs/instances/preemptible)
    - Regular Instance Rollback - When selected, if a preemptible instance is unavailable for the time specified in the
      `Regular Instance Rollback Timeout` field, a regular instance will be spun up instead
    - Preemptible Instance Blackout Period - Time (in minutes) to attempt using regular instances instead in case
      acquiring a preemptible instance fails
  - Max Number of Instances - Maximum number of concurrent running VM instances of this type allowed
  - Monitored Queue - Queue associated with this VM instance type. The tasks enqueued to this queue will be executed on VM instances of this type
  - Machine Image (optional) - The GCP machine image to launch

note

The machine image used for the autoscaler must include docker runtime and virtualenv.

  - Disc Size (in GB) (optional)
  - Use the default GCP Service Account - If selected, the default service account will be used. To use a
    different service account, clear this option and fill in the `Service Account Email` field
  - Service Account Scopes - Comma-separated scope aliases. For more information, see [GCP documentation](https://cloud.google.com/sdk/gcloud/reference/compute/instances/create#--scopes).
    Fully-qualified scope URIs are supported. If left empty, the autoscaler will use the default scopes.
  - Metadata - GCP Metadata to be applied on this resource's instances. Input comma separated key=value pairs (e.g. `"Owner=Admin,Foo=Bar"`).
  - \+ Add Item - Define another resource type
- **Global Metadata** (optional) - GCP Metadata to be applied on all instances. Input comma separated key=value pairs (e.g. `"Owner=Admin,Foo=Bar"`).
- **Autoscaler Instance Name** (optional) - Name for the Autoscaler instance. This will appear in the instance list
- **Max Idle Time** (optional) - Maximum time in minutes that a VM instance can be idle before the autoscaler spins it down
- **Workers Prefix** (optional) - A Prefix added to workers' names, associating them with this autoscaler
- **Polling Interval** (optional) - Time period in minutes at which the designated queue is polled for new tasks
- **Apply Task Owner Vault Configuration** \- Select to apply values from the task owner's [configuration vault](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_profile#configuration-vault) when executing the task (available under ClearML Enterprise Plan)
- **Warn if more than one instance is executing the same task** \- Select to print warning to console when multiple
instances are running the same task. In most cases, this indicates an issue.
- **Exclude .bashrc script** \- Select in order to skip `.bashrc` script execution
- **Ignore vault parsing errors** \- If not selected, the autoscaler will abort if encountering errors when loading vaults
on startup. This only applies to vaults loaded by the autoscaler itself, not to vaults loaded on cloud instances or by
tasks run by the autoscaler. For more information, see [Configuration Vault note](https://clear.ml/docs/latest/docs/webapp/applications/apps_gcp_autoscaler/#configuration_vault) (available under ClearML Enterprise Plan).
- **Init Script** (optional) - A bash script to execute after launching the VM instance
- **Additional ClearML Configuration** (optional) - A ClearML configuration file to use by the ClearML Agent when executing your tasks
- **Run with Service Account** \- Select to allow running the application under a [Service Account](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_users#service-accounts) identity instead of under your own identity (available under ClearML Enterprise Plan)
- **Export Configuration** \- Export the app instance configuration as a JSON file, which you can later import to create
a new instance with the same configuration

![GCP autoscaler instance launch form](https://clear.ml/docs/latest/assets/images/apps_gcp_autoscaler_wizard-3068d4d23474fe9636555625a1ce3d13.png)

Enterprise Feature

You can utilize the [configuration vault](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_profile#configuration-vault) to configure GCP
credentials for the autoscaler in the following format:

```text
auto_scaler.v1 {

    gcp {

        gcp_credentials: """

        {

          "type": "service_account",

          ...

        }

        """

    }

}
```

## Generating GCP Credentials [​](https://clear.ml/docs/latest/docs/webapp/applications/apps_gcp_autoscaler/\#generating-gcp-credentials "Direct link to Generating GCP Credentials")

The autoscaler app accesses your GCP account with the credentials you provide.

You will need to create a service account with the required access privileges. Then generate credential keys for that
account to configure the autoscaler app:

1. In your GCP account, in the project of your choice, go to **APIs & Services** \> **Credentials**

2. Click **\+ CREATE CREDENTIALS** and choose the **Service account** option

![GCP create credentials](https://clear.ml/docs/latest/assets/images/apps_gcp_autoscaler_credentials_1-53950b0007f0aa5393580ab9d7c6f0d8.png)

3. In the **Create service account** window that is opened, fill out the service account details

![GCP service account details](https://clear.ml/docs/latest/assets/images/apps_gcp_autoscaler_credentials_2-a9303a42f9fecfb36de2feeeca6e40f0.png)

4. Assign the `Service Account User` and `Compute Admin` roles to your service account

![GCP service account roles](https://clear.ml/docs/latest/assets/images/apps_gcp_autoscaler_credentials_3-8237d5f2590e8985338b0f0dde287e32.png)

5. Complete creating the account

![GCP service account creation completion](https://clear.ml/docs/latest/assets/images/apps_gcp_autoscaler_credentials_4-e9e9907da88be7f60e630eb0d3a37ad3.png)

6. In the **API & Services** \> **Credentials** page, under **Service Accounts**, click on the service account you just
created and go to its **KEYS** tab

![GCP credential keys](https://clear.ml/docs/latest/assets/images/apps_gcp_autoscaler_credentials_5-e5b9b217ab85949580febab7e73194b3.png)

7. Click **ADD KEY** and create a key in JSON format. Copy the contents of the JSON file.

![GCP credential key creation](https://clear.ml/docs/latest/assets/images/apps_gcp_autoscaler_credentials_6-5fa960abf75f49d02183d06435d9cbe5.png)

8. Go to the GCP Autoscaler instance launch form **>** open the **GCP Configuration** panel **>** click _Edit_ in the
**GCP Credentials** field.

![GCP credentials field](https://clear.ml/docs/latest/assets/images/apps_gcp_autoscaler_credentials_6a-ae7c3fb0e2b37892610e67aff3d2762f.png)

Paste the contents of the JSON file from the previous step into the **GCP Credentials** popup.

![GCP credential instance launch form input](https://clear.ml/docs/latest/assets/images/apps_gcp_autoscaler_credentials_7-ac5b644f0ef5a053edc00d75528203f7.png)


- [Autoscaler Instance Configuration](https://clear.ml/docs/latest/docs/webapp/applications/apps_gcp_autoscaler/#autoscaler-instance-configuration)
  - [Configuration Options](https://clear.ml/docs/latest/docs/webapp/applications/apps_gcp_autoscaler/#configuration-options)
- [Generating GCP Credentials](https://clear.ml/docs/latest/docs/webapp/applications/apps_gcp_autoscaler/#generating-gcp-credentials)