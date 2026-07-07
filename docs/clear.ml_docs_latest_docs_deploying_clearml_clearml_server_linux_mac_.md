---
url: "https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_linux_mac/"
title: "Linux and macOS | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_linux_mac/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

Deploy the ClearML Server in Linux or macOS using the pre-built Docker image.

For ClearML docker images, including previous versions, see [https://hub.docker.com/r/clearml/server](https://hub.docker.com/r/clearml/server).
However, pulling the ClearML Docker image directly is not required. ClearML provides a `docker-compose` YAML file that does this.
The `docker-compose` file is included in the instructions on this page.

For information about upgrading ClearML Server in Linux or macOS, see [here](https://clear.ml/docs/latest/docs/deploying_clearml/upgrade_server_linux_mac).

important

If ClearML Server is being reinstalled, clearing browser cookies for ClearML Server is recommended. For example,
for Firefox, go to Developer Tools > Storage > Cookies, and for Chrome, go to Developer Tools > Application > Cookies,
and delete all cookies under the ClearML Server URL.

## Prerequisites [​](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_linux_mac/\#prerequisites "Direct link to Prerequisites")

For Linux users only:

- Linux distribution must support Docker. For more information, see the [Docker documentation](https://docs.docker.com/engine/install/).
- Be logged in as a user with `sudo` privileges.
- Use `bash` for all command-line instructions in this installation.
- The ports `8080`, `8081`, and `8008` must be available for the ClearML Server services.

## Deploying [​](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_linux_mac/\#deploying "Direct link to Deploying")

warning

By default, ClearML Server launches with unrestricted access. To restrict ClearML Server access, follow the
instructions in the [Security](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_security) page.

Memory Requirement

Deploying the server requires a minimum of 8 GB of memory, 16 GB is recommended.

**To launch ClearML Server on Linux or macOS:**

01. Install Docker. The instructions depend upon the operating system:
    - Linux - see [Docker for Ubuntu](https://docs.docker.com/install/linux/docker-ce/ubuntu/).
    - macOS - see [Docker for OS X](https://docs.docker.com/docker-for-mac/install/).
02. Verify the Docker CE installation. Execute the command:





    ```text
    docker run hello-world
    ```









    The expected is output is:





    ```text
    Hello from Docker!

    This message shows that your installation appears to be working correctly.

    To generate this message, Docker took the following steps:



1. The Docker client contacted the Docker daemon.

2. The Docker daemon pulled the "hello-world" image from the Docker Hub. (amd64)

3. The Docker daemon created a new container from that image which runs the executable that produces the output you are currently reading.

4. The Docker daemon streamed that output to the Docker client, which sent it to your terminal.
```

03. For macOS only, increase the memory allocation in Docker Desktop to `8GB`.
    1. In the top status bar, click the Docker icon.
    2. Click **Preferences** **>** **Resources** **>** **Advanced**, and then set the memory to at least `8192`.
    3. Click **Apply**.
04. For Linux only, install `docker-compose`. Execute the following commands (for more information, see [Install Docker Compose](https://docs.docker.com/compose/install/) in the Docker documentation):





    ```text
    sudo curl -L "https://github.com/docker/compose/releases/download/1.24.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

    sudo chmod +x /usr/local/bin/docker-compose
    ```

05. Increase `vm.max_map_count` for Elasticsearch in Docker. Execute the following commands, depending upon the operating system:
    - Linux:





      ```text
      echo "vm.max_map_count=524288" > /tmp/99-clearml.conf

      sudo mv /tmp/99-clearml.conf /etc/sysctl.d/99-clearml.conf

      sudo sysctl -w vm.max_map_count=524288

      sudo service docker restart
      ```

    - macOS:





      ```text
      docker run --net=host --ipc=host --uts=host --pid=host --privileged --security-opt=seccomp=unconfined -it --rm -v /:/host alpine chroot /host

      sysctl -w vm.max_map_count=524288
      ```
06. Remove any previous installation of ClearML Server.

    **This clears all existing ClearML SDK databases.**





    ````text
    ```

    sudo rm -R /opt/clearml/

    ```
    ````

07. Create local directories for the databases and storage.





    ```text
    sudo mkdir -p /opt/clearml/data/elastic_7

    sudo mkdir -p /opt/clearml/data/mongo_4/db

    sudo mkdir -p /opt/clearml/data/mongo_4/configdb

    sudo mkdir -p /opt/clearml/data/redis

    sudo mkdir -p /opt/clearml/logs

    sudo mkdir -p /opt/clearml/config

    sudo mkdir -p /opt/clearml/data/fileserver
    ```

08. For macOS only do the following:
    1. Open the Docker app.

    2. Select **Preferences**.

    3. On the **File Sharing** tab, add `/opt/clearml`.
09. Grant access to the Dockers, depending upon the operating system.
    - Linux:





      ```text
      sudo chown -R 1000:1000 /opt/clearml
      ```











      note





      This assumes the container processes run as UID 1000 and GID 1000. The ownership of `/opt/clearml` must match the
      UID and GID used inside the container. If the container runs as a different user or group, update the ownership
      accordingly to ensure they can access the mounted directories.

    - macOS:





      ```text
      sudo chown -R $(whoami):staff /opt/clearml
      ```
10. Download the ClearML Server `docker-compose` YAML file:





    ```text
    sudo curl https://raw.githubusercontent.com/clearml/clearml-server/master/docker/docker-compose.yml -o /opt/clearml/docker-compose.yml
    ```

11. For Linux only, configure the **ClearML Agent Services**:


    - Set `CLEARML_AGENT_ACCESS_KEY` and `CLEARML_AGENT_SECRET_KEY` with confidential strings for the services agent to
      authenticate with the API server. Provide string values.

    - If `CLEARML_HOST_IP` is not provided, then ClearML Agent Services uses the external public address of the ClearML
      Server

    - Set `CLEARML_AGENT_GIT_USER` / `CLEARML_AGENT_GIT_PASS` so ClearML Agent Services can access
      private repositories for running service tasks


```text
export CLEARML_AGENT_ACCESS_KEY=generate_access_key_here

export CLEARML_AGENT_SECRET_KEY=generate_secret_key_here

export CLEARML_HOST_IP=server_host_ip_here

export CLEARML_AGENT_GIT_USER=git_username_here

export CLEARML_AGENT_GIT_PASS=git_password_here
```

12. Run `docker-compose` with the downloaded configuration file.





    ```text
    docker-compose -f /opt/clearml/docker-compose.yml up -d
    ```


The server is now running on [http://localhost:8080](http://localhost:8080/).

## Port Mapping [​](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_linux_mac/\#port-mapping "Direct link to Port Mapping")

After deploying ClearML Server, the services expose the following ports:

- Web server on port `8080`
- API server on port `8008`
- File server on port `8081`

## Restarting [​](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_linux_mac/\#restarting "Direct link to Restarting")

**To restart ClearML Server Docker deployment:**

- Stop and then restart the Docker containers by executing the following commands:





  ```text
  docker-compose -f /opt/clearml/docker-compose.yml down

  docker-compose -f /opt/clearml/docker-compose.yml up -d
  ```


## Backing Up and Restoring Data and Configuration [​](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_linux_mac/\#backing-up-and-restoring-data-and-configuration "Direct link to Backing Up and Restoring Data and Configuration")

warning

Stop your server before backing up or restoring data and configuration.

The commands in this section are an example of how to back up and to restore data and configuration.

If the data and configuration folders are in `/opt/clearml`, then archive all data into `~/clearml_backup_data.tgz`, and
configuration into `~/clearml_backup_config.tgz`:

```text
sudo tar czvf ~/clearml_backup_data.tgz -C /opt/clearml/data .

sudo tar czvf ~/clearml_backup_config.tgz -C /opt/clearml/config .
```

If needed, restore data and configuration by doing the following:

1. Verify the existence of backup files.

2. Replace any existing data with the backup data:





   ```text
   sudo rm -fR /opt/clearml/data/* /opt/clearml/config/*

   sudo tar -xzf ~/clearml_backup_data.tgz -C /opt/clearml/data

   sudo tar -xzf ~/clearml_backup_config.tgz -C /opt/clearml/config
   ```

3. Grant access to the data, depending upon the operating system:
   - Linux:





     ```text
     sudo chown -R 1000:1000 /opt/clearml
     ```

   - macOS:





     ```text
     sudo chown -R $(whoami):staff /opt/clearml
     ```

## Next Step [​](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_linux_mac/\#next-step "Direct link to Next Step")

To keep track of your experiments and/or data, the `clearml` package needs to communicate with your server.
For instruction to connect the ClearML SDK to the server, see [ClearML Setup](https://clear.ml/docs/latest/docs/clearml_sdk/clearml_sdk_setup).

- [Prerequisites](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_linux_mac/#prerequisites)
- [Deploying](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_linux_mac/#deploying)
- [Port Mapping](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_linux_mac/#port-mapping)
- [Restarting](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_linux_mac/#restarting)
- [Backing Up and Restoring Data and Configuration](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_linux_mac/#backing-up-and-restoring-data-and-configuration)
- [Next Step](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_linux_mac/#next-step)