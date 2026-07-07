---
url: "https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/app_install_ex_server/"
title: "External Applications Server Installation | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/app_install_ex_server/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

Enterprise Feature

UI application deployment is available under the ClearML Enterprise plan.

ClearML supports applications, which are extensions that allow additional capabilities, such as cloud auto-scaling,
Hyperparameter Optimizations, etc. For more information, see [ClearML Applications](https://clear.ml/docs/latest/docs/webapp/applications/apps_overview).

Applications run inside Docker containers, which can either reside on the ClearML Server side, or on an external server.
The `clearml-apps-agent` polls an internal applications queue, and spawns additional Docker containers for application
instances that are launched using the ClearML web UI.

This guide provides instructions on how to configure an external applications server.

## Requirements [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/app_install_ex_server/\#requirements "Direct link to Requirements")

- A server, as described in [Server Requirements](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/app_install_ex_server/#server-requirements)
- `docker-compose.yml` file provided by ClearML
- `constants.env` \- Environment file with required credentials
- Credentials to access ClearML’s enterprise Dockerhub registry

### Server Requirements [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/app_install_ex_server/\#server-requirements "Direct link to Server Requirements")

- Operating system: Linux-based
- CPU: Since applications do not produce a high CPU load, we recommend 2-4 virtual CPUs, assuming around 10 concurrent
applications are required
- Memory: Around 1 GiB of RAM is required per each concurrent application instance
- Storage: About 100 GB of storage is recommended for the system volume, with an additional 100 GB of storage for
application caching. In AWS, `m6a.xlarge` can be used for running up to 10 applications in parallel.

## Installation [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/app_install_ex_server/\#installation "Direct link to Installation")

note

Installing an external server requires removing the applications’ agent from the ClearML Enterprise Server. This
is done by ClearML in hosted environments, or by removing the `apps-agent` service from the `docker-compose` override
file in VPC and on-premises installations. For K8s environments, please consult the ClearML team.

1. Install Docker. See [Docker documentation](https://docs.docker.com/engine/install/ubuntu/)

2. Copy the `docker-compose.yml` and `constants.env` files to `/opt/allegro`. The
`constants.env` file should contain following definitions:
   - `APISERVER_URL_FOR_EXTERNAL_WORKERS` \- URL of the ClearML API server
   - `WEBSERVER_URL_FOR_EXTERNAL_WORKERS` \- URL of the ClearML WebApp
   - `FILESERVER_URL_FOR_EXTERNAL_WORKERS` \- URL of the ClearML files server
   - `APPS_AGENT_USER_KEY` \- Provided by ClearML
   - `APPS_AGENT_USER_SECRET` \- Provided by ClearML
   - `APPS_AGENT_GIT_USER` \- Provided by ClearML (required up to ClearML Server 1.8)
   - `APPS_AGENT_GIT_PASSWORD` \- Provided by ClearML (required up to ClearML Server 1.8)
   - `APPS_WORKER_DOCKER_IMAGE` \- Provided by ClearML (required up to ClearML Server 1.8)
   - `APPS_DAEMON_DOCKER_IMAGE` \- Provided by ClearML
3. Log in to the Docker registry:





```text
sudo docker login -username allegroaienterprise
```

4. Pull the container:





```text
docker compose -env-file constants.env pull
```

5. Start the service:





```text
docker compose -env-file constants.env up -d
```


## Clearing Stopped Containers [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/app_install_ex_server/\#clearing-stopped-containers "Direct link to Clearing Stopped Containers")

Containers of running applications that are stopped are not automatically deleted. Therefore, it is recommended to
periodically delete stopped containers. This can be done by adding the following to the cron file:

```text
0 0 * * * root docker container prune --force --filter "until=96h" --filter "label=allegro-type=application"
```

## Monitoring [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/app_install_ex_server/\#monitoring "Direct link to Monitoring")

We recommend monitoring the following:

- Available memory
- CPU usage
- Remaining Storage

For more information contact ClearML's support team.

- [Requirements](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/app_install_ex_server/#requirements)
  - [Server Requirements](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/app_install_ex_server/#server-requirements)
- [Installation](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/app_install_ex_server/#installation)
- [Clearing Stopped Containers](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/app_install_ex_server/#clearing-stopped-containers)
- [Monitoring](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/app_install_ex_server/#monitoring)