---
url: "https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/apps_k8s/"
title: "Application Installation on Kubernetes | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/apps_k8s/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

Enterprise Feature

UI application deployment is available under the ClearML Enterprise plan.

ClearML Applications are plugins that extend the functionality of the ClearML Enterprise Server. They enable users
to:

- Manage ML workloads
- Automate recurring workflows--no code required

Applications are installed on top of the ClearML Server and are provided by the ClearML team.

## Requirements [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/apps_k8s/\#requirements "Direct link to Requirements")

- Python 3 installed on your local machine to run the provided installation scripts
- A ClearML Enterprise Server is up and running with `clearmlApplications.enabled` set to `"true"` in the server's `overrides.yaml` file.
- Applications package provided by ClearML, including the following scripts:
  - `convert_image_registry.py`
  - `upload_apps.py`
- API credentials (`<ACCESS_KEY>` and `<SECRET_KEY>`) generated via
the ClearML UI ( **Settings > Workspace > API Credentials > Create new credentials**). Make sure these credentials
belong to an admin user or a service user with admin privileges. For more information, see [ClearML API Credentials](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_profile#clearml-api-credentials).

## Installation [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/apps_k8s/\#installation "Direct link to Installation")

To install the ClearML Applications on a newly installed ClearML Enterprise Server:

### Download and Extract [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/apps_k8s/\#download-and-extract "Direct link to Download and Extract")

Download the applications package using the URL provided by ClearML:

```bash
wget -O apps.zip "<ClearML enterprise applications configuration download url>"

unzip apps.zip
```

### Adjust Application Docker Images Location (Air-Gapped Systems) [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/apps_k8s/\#adjust-application-docker-images-location-air-gapped-systems "Direct link to Adjust Application Docker Images Location (Air-Gapped Systems)")

ClearML Applications use pre-built Docker images from the ClearML DockerHub repository. If you are
installing in an air-gapped system, these images must be available in your internal docker registry. You must specify
the docker images location before installing the applications.

Use the provided script to modify the application zip files to reference your internal registry:

```bash
python convert_image_registry.py \

--apps-dir "<PATH_TO_APPS_DIR>" \

--artifactory <LOCAL_REGISTRY>/clearml_apps
```

The script will:

- Update the application zip files to point to the new registry

- Output the list of images that need to be copied to the local registry. For example:





```text
> make sure `allegroai/clearml-apps:hpo-1.10.0-1062` was added to `local_registry/clearml-apps`
```


### Upload Applications to ClearML Server [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/apps_k8s/\#upload-applications-to-clearml-server "Direct link to Upload Applications to ClearML Server")

Use `upload_apps.py` to upload the application packages to the ClearML Server.

To see available options, run `python3 upload_apps.py --help`.

**Upload a Single application:**

```bash
python3 upload_apps.py --host <APISERVER_URL> --key <ACCESS_KEY> --secret <SECRET_KEY> --command upload --files "YOUR_APP.zip"
```

**Upload Multiple applications:**

```bash
python3 upload_apps.py --host <APISERVER_URL> --key <ACCESS_KEY> --secret <SECRET_KEY> --command upload --dir "<PATH_TO_APPS_DIR>" -ml
```

## Application Instance Visibility [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/apps_k8s/\#application-instance-visibility "Direct link to Application Instance Visibility")

By default, all users can view all application instances in the ClearML UI. You can configure different visibility
policies globally or for specific applications, for example to restrict access to the application owner or allow sharing
only with selected user groups.

For more information, see [Application Instance Visibility Policy](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/app_visibility_policy).

- [Requirements](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/apps_k8s/#requirements)
- [Installation](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/apps_k8s/#installation)
  - [Download and Extract](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/apps_k8s/#download-and-extract)
  - [Adjust Application Docker Images Location (Air-Gapped Systems)](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/apps_k8s/#adjust-application-docker-images-location-air-gapped-systems)
  - [Upload Applications to ClearML Server](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/apps_k8s/#upload-applications-to-clearml-server)
- [Application Instance Visibility](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/apps_k8s/#application-instance-visibility)