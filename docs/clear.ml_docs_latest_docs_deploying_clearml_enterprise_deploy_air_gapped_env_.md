---
url: "https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/air_gapped_env/"
title: "Air-Gapped Environments | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/air_gapped_env/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

This guide covers how to deploy and operate ClearML in **air-gapped environments**—environments with restricted or no
internet access. It includes steps for locally hosting all required resources and configuring ClearML components accordingly.

The guide covers:

- Hosting dependencies for ClearML Applications
- Configuring application containers with offline resources
- Configuring Kubernetes deployments using private registries and image pull secrets

## Preparing ClearML Applications for Air-Gapped Use [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/air_gapped_env/\#preparing-clearml-applications-for-air-gapped-use "Direct link to Preparing ClearML Applications for Air-Gapped Use")

Some ClearML Applications require additional Python packages to be available in the container used to run the application
instance, otherwise they are downloaded and installed at instance launch.

### Hosting Required Python Packages [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/air_gapped_env/\#hosting-required-python-packages "Direct link to Hosting Required Python Packages")

Ensure the Python packages are locally hosted in your PyPI proxy or Python packages artifactory, and are accessible using
a local URL. Alternatively, use custom images that have these packages installed.

To view an application’s package requirements: Open the relevant application and hover over the `Container requirements`
button under the app description.

![Required packages](https://clear.ml/docs/latest/assets/images/app_required_packages-2c034f9df8e74a009d346ac78fb6eb44.png#light-mode-only)![Required packages](https://clear.ml/docs/latest/assets/images/app_required_packages_dark-a8db7e91ec1866509b0987f81cdc0c0a.png#dark-mode-only)

### Setting PIP Indexes [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/air_gapped_env/\#setting-pip-indexes "Direct link to Setting PIP Indexes")

Configure the Python package index for pip using one of the following environment variables:

- `PIP_EXTRA_INDEX_URL` \- Adds a custom index in addition to the default
- `PIP_INDEX_URL` \- Replaces the default index with a custom one (only a single index will be used)

The following is an example in Kubernetes using the ClearML Agent helm values override:

```yaml
agentk8sglue:

  queues:

    myQueue:

      templateOverrides:

        env:

          - name: PIP_EXTRA_INDEX_URL

            value: "<LOCAL_REPO_URL>"
```

For further pip configuration options, see the [pip documentation](https://pip.pypa.io/en/latest/cli/pip_install/#options).

#### Trusting Pip Index [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/air_gapped_env/\#trusting-pip-index "Direct link to Trusting Pip Index")

To configure pip to trust your local PyPI repository (for example, if it uses a self-signed certificate), use one of the
following methods:

- Use `PIP_TRUSTED_HOST` environment variable:





```yaml
agentk8sglue:

    queues:

      myQueue:

        templateOverrides:

          env:

          - name: PIP_EXTRA_INDEX_URL

            value: "<LOCAL_REPO_URL>"

          - name: PIP_TRUSTED_HOST

            value: "<LOCAL_REPO_HOST_NAME>"
```

- Mount a custom `pip.conf` file:





```yaml
agentk8sglue:

    queues:

      myQueue:

        templateOverrides:

          fileMounts:

          - name: "pip.conf"

            folderPath: "/home/nonroot/.pip"

            fileContent: |-

              [global]

              index-url = <LOCAL_REPO_URL>

              trusted-host = <LOCAL_REPO_HOST_NAME>
```

### Setting App Environment Variables [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/air_gapped_env/\#setting-app-environment-variables "Direct link to Setting App Environment Variables")

Application environment variables (see [below](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/air_gapped_env/#app-specific-offline-resources)) can be set using any of the following:

- [ClearML Administrator Vault](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_admin_vaults) configuration: Set `agent.extra_docker_arguments`
- Agent config on VMs or bare-metal: Set `agent.extra_docker_arguments`
- Kubernetes ClearML Agent deployments: Set the `basePodTemplate`

Ensure that:

- All containers and pods are configured to pull images from your private container registry
- Custom images include Python 3

### App-Specific Offline Resources [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/air_gapped_env/\#app-specific-offline-resources "Direct link to App-Specific Offline Resources")

#### VSCode Application [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/air_gapped_env/\#vscode-application "Direct link to VSCode Application")

For the ClearML VSCode Application to work offline, provide the following to all containers started by the ClearML Agent
running GPU workloads:

- **VSCode Server debian package**: Set `CLEARML_SESSION_VSCODE_SERVER_DEB=<PATH_TO_DEB_FILE>`. Package can be found [here](https://github.com/coder/code-server/releases/download/v4.96.2/code-server_4.96.2_amd64.deb)
(version number can be updated, see [https://github.com/coder/code-server/releases](https://github.com/coder/code-server/releases)).
- **VSCode Python extension**: Set `CLEARML_SESSION_VSCODE_PY_EXT=<PATH_TO_EXTENSION_FILE>` pointing to the Visual Studio
marketplace. Package can be found [here](https://marketplace.visualstudio.com/_apis/public/gallery/publishers/ms-python/vsextensions/python/2022.12.0/vspackage)
(version number can be updated, see the [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-python.python)).

Example in Kubernetes using the ClearML Agent helm values override:

```yaml
agentk8sglue:

queues:

    myQueue:

      templateOverrides:

        env:

          - name: CLEARML_SESSION_VSCODE_SERVER_DEB

            value: "<PATH_TO_DEB_FILE>"

          - name: CLEARML_SESSION_VSCODE_PY_EXT

            value: "<PATH_TO_EXTENSION_FILE>"
```

#### SSH Session Application [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/air_gapped_env/\#ssh-session-application "Direct link to SSH Session Application")

For air-gapped SSH applications using the DropBear server (required for non-privileged containers):

- Download and host the [DropBear executable](https://github.com/allegroai/dropbear/releases/download/DROPBEAR_CLEARML_2023.02/dropbearmulti).
- Set `CLEARML_DROPBEAR_EXEC=<PATH_TO_EXECUTABLE>` in all containers started by the ClearML Agent running GPU workloads

### Convert Image Registry [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/air_gapped_env/\#convert-image-registry "Direct link to Convert Image Registry")

[ClearML Application](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/apps_k8s) installation requires running the `convert_image_registry.py` script
included in the package. Images that need to be mirrored will be listed in the script output of the same script. Mirror these images
to your private registry before proceeding
with the upload of application packages.

## Kubernetes Environments [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/air_gapped_env/\#kubernetes-environments "Direct link to Kubernetes Environments")

### Use a Custom imagePullSecret [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/air_gapped_env/\#use-a-custom-imagepullsecret "Direct link to Use a Custom imagePullSecret")

To ensure Kubernetes workloads (ClearML Agents, Server, and App Gateway) use your private registry, configure `imagePullSecrets`
in the appropriate Helm override files.

- To use a custom defined `imagePullSecret` for a **ClearML Agent** and the tasks Pods it creates, configure the following
in your `clearml-agent-values.override.yaml` file:





```yaml
imageCredentials:

    extraImagePullSecrets:

    - name: "<IMAGE_PULL_SECRET_NAME>"
```

- To use a custom defined `imagePullSecret` for the **ClearML Server**, configure the following in your `clearml-values.override.yaml` file:





```yaml
imageCredentials:

    existingImagePullSecrets:

    - name: "<IMAGE_PULL_SECRET_NAME>"
```

- To use a custom defined `imagePullSecret` for the **ClearML App Gateway**, configure the following in your `clearml-app-gateway-values.override.yaml` file:





```yaml
imageCredentials:

    existingImagePullSecrets:

    - name: "<IMAGE_PULL_SECRET_NAME>"
```

### Create a Custom imagePullSecret [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/air_gapped_env/\#create-a-custom-imagepullsecret "Direct link to Create a Custom imagePullSecret")

To create a registry secret in Kubernetes, use the following command example. The secret needs to be created in the namespace where it will be used.

```bash
kubectl create secret docker-registry -n <NAMESPACE> <SECRET_NAME> \

  --docker-server=<REPO_URL> \

  --docker-username=<USERNAME> \

  --docker-password=<PASSWORD> \

  --docker-email=<EMAIL_OR_EMPTY_STRING>
```

### List Images Used in a ClearML Helm Chart [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/air_gapped_env/\#list-images-used-in-a-clearml-helm-chart "Direct link to List Images Used in a ClearML Helm Chart")

ClearML is deployed using several Helm charts, each with its own set of container images.

To see all container images used by each chart use the following commands:

note

This requires the `helm` and `yq` commands to be installed.

- `clearml-enterprise` (Control Plane):





```text
helm template oci://docker.io/clearml/clearml-enterprise | yq '..|.image? | select(.)' | sort -u
```

- `clearml-enterprise-agent` (ClearML k8s Agent):





```text
helm template oci://docker.io/clearml/clearml-enterprise-agent | yq '..|.image? | select(.)' | sort -u
```

- `clearml-enterprise-app-gateway` (ClearML Application Gateway):





```text
helm template oci://docker.io/clearml/clearml-enterprise-app-gateway \

    --set clearml.apiKey=dummy \

    --set clearml.apiSecret=dummy \

    --set clearml.apiServerUrlReference=dummy | yq '..|.image? | select(.)' | sort -u
```











note





The Application Gateway chart requires placeholder values for required parameters (`apiKey`, `apiSecret`,
`apiServerUrlReference`) to render successfully with helm template.


## Customize Agent Containers Start Script [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/air_gapped_env/\#customize-agent-containers-start-script "Direct link to Customize Agent Containers Start Script")

You can customize the ClearML Tasks Pod initial Bash script. This is useful in air-gapped environments, where you may
want to skip the default `apt-get` installations, and rely on prebuilt container images.

The startup script (`agentk8sglue.containerCustomBashScript`) must always end with the `clearml_agent execute` command. Otherwise,
ClearML Tasks will not run.

### Configuration Example [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/air_gapped_env/\#configuration-example "Direct link to Configuration Example")

Edit the ClearML Agent values override file with the following content. Make sure to replace the `<YOUR_IMAGE_WITH_PYTHON_3.9>`
with the name of an image that has Python 3.9 or higher pre-installed.

```yaml
agentk8sglue:

# -- Support for air-gapped systems. Skip container APT installations.

airGappedSupport: true

# -- Default container image for ClearML Task pod

defaultContainerImage: "<YOUR_IMAGE_WITH_PYTHON_3.9>"

# -- Custom Bash script for the Task Pods run by the Agent

containerCustomBashScript: |

    export HOME=/tmp

    export LOCAL_PYTHON=python3

    {extra_bash_init_cmd}

    [ ! -z $CLEARML_AGENT_NO_UPDATE ] || $LOCAL_PYTHON -m pip install clearml-agent{agent_install_args}

    {extra_docker_bash_script}

    $LOCAL_PYTHON -m clearml_agent execute {default_execution_agent_args} --id {task_id}
```

## Webserver [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/air_gapped_env/\#webserver "Direct link to Webserver")

When using a private registry, this configuration will make the Webserver reference the correct extra index URL for
Enterprise packages.

In Kubernetes:

```yaml
clearml:

extraIndexUrl: "<YOUR_REPO_URL>"
```

- [Preparing ClearML Applications for Air-Gapped Use](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/air_gapped_env/#preparing-clearml-applications-for-air-gapped-use)
  - [Hosting Required Python Packages](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/air_gapped_env/#hosting-required-python-packages)
  - [Setting PIP Indexes](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/air_gapped_env/#setting-pip-indexes)
  - [Setting App Environment Variables](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/air_gapped_env/#setting-app-environment-variables)
  - [App-Specific Offline Resources](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/air_gapped_env/#app-specific-offline-resources)
  - [Convert Image Registry](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/air_gapped_env/#convert-image-registry)
- [Kubernetes Environments](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/air_gapped_env/#kubernetes-environments)
  - [Use a Custom imagePullSecret](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/air_gapped_env/#use-a-custom-imagepullsecret)
  - [Create a Custom imagePullSecret](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/air_gapped_env/#create-a-custom-imagepullsecret)
  - [List Images Used in a ClearML Helm Chart](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/air_gapped_env/#list-images-used-in-a-clearml-helm-chart)
- [Customize Agent Containers Start Script](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/air_gapped_env/#customize-agent-containers-start-script)
  - [Configuration Example](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/air_gapped_env/#configuration-example)
- [Webserver](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/air_gapped_env/#webserver)