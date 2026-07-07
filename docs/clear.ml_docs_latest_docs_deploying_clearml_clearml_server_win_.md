---
url: "https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_win/"
title: "Windows 10 | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_win/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

For Windows, launching the pre-built Docker image on a Linux virtual machine is recommended (see [Deploying ClearML Server: Linux or macOS](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_linux_mac)).
However, ClearML Server can be launched on Windows 10, using Docker Desktop for Windows (see the Docker [System Requirements](https://docs.docker.com/docker-for-windows/install/#system-requirements)).

For information about upgrading ClearML Server on Windows, see [here](https://clear.ml/docs/latest/docs/deploying_clearml/upgrade_server_win).

important

If ClearML Server is being reinstalled, clearing browser cookies for ClearML Server is recommended. For example,
for Firefox, go to Developer Tools > Storage > Cookies, and for Chrome, go to Developer Tools > Application > Cookies,
and delete all cookies under the ClearML Server URL.

## Deploying [​](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_win/\#deploying "Direct link to Deploying")

warning

By default, ClearML Server launches with unrestricted access. To restrict ClearML Server access, follow the instructions in the [Security](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_security) page.

Memory Requirement

Deploying the server requires a minimum of 8 GB of memory, 16 GB is recommended.

**To deploy ClearML Server on Windows 10:**

1. Install the Docker Desktop for Windows application by either:
   - Following the [Install Docker Desktop on Windows](https://docs.docker.com/docker-for-windows/install/) instructions.
   - Running the Docker installation [wizard](https://hub.docker.com/?overlay=onboarding).
2. Increase the memory allocation in Docker Desktop to `4GB`.
1. In the Windows notification area (system tray), right-click the Docker icon.

2. Click **Settings** **>** **Advanced**, and then set the memory to at least `4096`.

3. Click **Apply**.
3. Remove any previous installation of ClearML Server.

**This clears all existing ClearML SDK databases.**





```text
rmdir c:\opt\clearml /s
```

4. Create local directories for data and logs. Open PowerShell and execute the following commands:





```text
cd c:

mkdir c:\opt\clearml\data

mkdir c:\opt\clearml\logs
```

5. Save the ClearML Server `docker-compose` YAML file.





```text
curl https://raw.githubusercontent.com/clearml/clearml-server/master/docker/docker-compose-win10.yml -o c:\opt\clearml\docker-compose-win10.yml
```

6. Run `docker-compose`. In PowerShell, execute the following commands:





```text
docker-compose -f c:\opt\clearml\docker-compose-win10.yml up
```









The server is now running on [http://localhost:8080](http://localhost:8080/).


## Port Mapping [​](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_win/\#port-mapping "Direct link to Port Mapping")

After deploying ClearML Server, the services expose the following node ports:

- Web server on port `8080`
- API server on port `8008`
- File server on port `8081`

## Restarting [​](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_win/\#restarting "Direct link to Restarting")

**To restart ClearML Server Docker deployment:**

- Stop and then restart the Docker containers by executing the following commands:





```text
docker-compose -f c:\opt\clearml\docker-compose-win10.yml down

docker-compose -f c:\opt\clearml\docker-compose-win10.yml up -d
```


## Next Step [​](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_win/\#next-step "Direct link to Next Step")

To keep track of your experiments and/or data, the `clearml` package needs to communicate with your server.
For instruction to connect the ClearML SDK to the server, see [ClearML Setup](https://clear.ml/docs/latest/docs/clearml_sdk/clearml_sdk_setup).

- [Deploying](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_win/#deploying)
- [Port Mapping](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_win/#port-mapping)
- [Restarting](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_win/#restarting)
- [Next Step](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_win/#next-step)