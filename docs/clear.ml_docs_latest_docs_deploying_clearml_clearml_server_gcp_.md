---
url: "https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_gcp/"
title: "Google Cloud Platform | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_gcp/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

Deploy ClearML Server on the Google Cloud Platform (GCP) using one of the pre-built GCP Custom Images. ClearML
provides custom images for each released version of ClearML Server. For a list of the pre-built custom images, see
[ClearML Server GCP Custom Image](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_gcp/#clearml-server-gcp-custom-image).

To keep track of your experiments and/or data, the `clearml` package needs to communicate with the server you have deployed.
For instruction to connect the ClearML SDK to the server, see [ClearML Setup](https://clear.ml/docs/latest/docs/clearml_sdk/clearml_sdk_setup).

note

In order for `clearml` to work with a ClearML Server on GCP, set `CLEARML_API_DEFAULT_REQ_METHOD=PUT` or
set `api.http.default_method` to `"PUT"` in the [`clearml.conf`](https://clear.ml/docs/latest/docs/configs/clearml_conf) file.

For information about upgrading ClearML server on GCP, see [here](https://clear.ml/docs/latest/docs/deploying_clearml/upgrade_server_gcp).

Reinstallation

If ClearML Server is being reinstalled, clearing browser cookies for ClearML Server is recommended. For example,
for Firefox, go to Developer Tools > Storage > Cookies, and for Chrome, go to Developer Tools > Application > Cookies,
and delete all cookies under the ClearML Server URL.

## Default ClearML Server Service Ports [​](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_gcp/\#default-clearml-server-service-ports "Direct link to Default ClearML Server Service Ports")

After deploying ClearML Server, the services expose the following node ports:

- Web server on `8080`
- API server on `8008`
- File Server on `8081`

## Default ClearML Server Storage Paths [​](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_gcp/\#default-clearml-server-storage-paths "Direct link to Default ClearML Server Storage Paths")

The persistent storage configuration:

- MongoDB: `/opt/clearml/data/mongo_4/`
- Elasticsearch: `/opt/clearml/data/elastic_7/`
- File Server: `/mnt/fileserver/`

## Importing the Custom Image to your GCP account [​](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_gcp/\#importing-the-custom-image-to-your-gcp-account "Direct link to Importing the Custom Image to your GCP account")

Before launching an instance using a ClearML Server GCP Custom Image, import the image to the custom images list.

note

No upload of the image file is required. Links to image files stored in Google Storage are provided.

**To import the image to your custom images list:**

1. In the Cloud Console, go to the [Images](https://console.cloud.google.com/compute/images) page.

2. At the top of the page, click **Create image**.

3. In **Name**, specify a unique name for the image.

4. Optionally, specify an image family for the new image, or configure specific encryption settings for the image.

5. In the **Source** menu, select **Cloud Storage file**.

6. Enter the ClearML Server image bucket path (see [ClearML Server GCP Custom Image](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_gcp/#clearml-server-gcp-custom-image)),
for example: `allegro-files/clearml-server/clearml-server.tar.gz`.

7. Click **Create** to import the image. The process can take several minutes depending on the size of the boot disk image.


For more information see the [Compute Engine Documentation](https://cloud.google.com/compute/docs/import/import-existing-image#import_image).

## Launching [​](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_gcp/\#launching "Direct link to Launching")

warning

By default, ClearML Server launches with unrestricted access. To restrict ClearML Server access, follow the
instructions in the [Security](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_security) page.

To launch ClearML Server using a GCP Custom Image, see the [Google Cloud Storage documentation](https://cloud.google.com/compute/docs/import/import-existing-image#overview). For more information about Custom Images, see [Custom Images](https://cloud.google.com/compute/docs/images#custom_images) in the Compute Engine documentation.

The minimum requirements for ClearML Server are:

- 2 vCPUs
- 7.5GB RAM

## Restarting [​](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_gcp/\#restarting "Direct link to Restarting")

**To restart ClearML Server Docker deployment:**

- Stop and then restart the Docker containers by executing the following commands:





```text
docker-compose -f /opt/clearml/docker-compose.yml down

docker-compose -f /opt/clearml/docker-compose.yml up -d
```


## Backing Up and Restoring Data and Configuration [​](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_gcp/\#backing-up-and-restoring-data-and-configuration "Direct link to Backing Up and Restoring Data and Configuration")

warning

Stop your server before backing up or restoring data and configuration.

The commands in this section are an example of how to back up and restore data and configuration.

If data and configuration folders are in `/opt/clearml`, then archive all data into `~/clearml_backup_data.tgz`, and
configuration into `~/clearml_backup_config.tgz`:

```text
sudo tar czvf ~/clearml_backup_data.tgz -C /opt/clearml/data .

sudo tar czvf ~/clearml_backup_config.tgz -C /opt/clearml/config .
```

If the data and the configuration need to be restored:

1. Verify you have the backup files.

2. Replace any existing data with the backup data:





```text
sudo rm -fR /opt/clearml/data/* /opt/clearml/config/*

sudo tar -xzf ~/clearml_backup_data.tgz -C /opt/clearml/data

sudo tar -xzf ~/clearml_backup_config.tgz -C /opt/clearml/config
```

3. Grant access to the data:





```text
sudo chown -R 1000:1000 /opt/clearml
```


## ClearML Server GCP Custom Image [​](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_gcp/\#clearml-server-gcp-custom-image "Direct link to ClearML Server GCP Custom Image")

The following section contains a list of Custom Image URLs (exported in different formats) for each released ClearML Server version.

### Latest Version - v1.13.0 [​](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_gcp/\#latest-version---v1130 "Direct link to Latest Version - v1.13.0")

- [https://storage.googleapis.com/allegro-files/clearml-server/clearml-server.tar.gz](https://storage.googleapis.com/allegro-files/clearml-server/clearml-server.tar.gz)

### All Release Versions [​](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_gcp/\#all-release-versions "Direct link to All Release Versions")

- v1.13.0 - [https://storage.googleapis.com/allegro-files/clearml-server/clearml-server-1-13-0.tar.gz](https://storage.googleapis.com/allegro-files/clearml-server/clearml-server-1-13-0.tar.gz)
- v1.12.1 - [https://storage.googleapis.com/allegro-files/clearml-server/clearml-server-1-12-1.tar.gz](https://storage.googleapis.com/allegro-files/clearml-server/clearml-server-1-12-1.tar.gz)
- v1.12.0 - [https://storage.googleapis.com/allegro-files/clearml-server/clearml-server-1-12-0.tar.gz](https://storage.googleapis.com/allegro-files/clearml-server/clearml-server-1-12-0.tar.gz)
- v1.11.0 - [https://storage.googleapis.com/allegro-files/clearml-server/clearml-server-1-11-0.tar.gz](https://storage.googleapis.com/allegro-files/clearml-server/clearml-server-1-11-0.tar.gz)
- v1.9.2 - [https://storage.googleapis.com/allegro-files/clearml-server/clearml-server-1-9-1.tar.gz](https://storage.googleapis.com/allegro-files/clearml-server/clearml-server-1-9-2.tar.gz)
- v1.9.1 - [https://storage.googleapis.com/allegro-files/clearml-server/clearml-server-1-9-1.tar.gz](https://storage.googleapis.com/allegro-files/clearml-server/clearml-server-1-9-1.tar.gz)
- v1.9.0 - [https://storage.googleapis.com/allegro-files/clearml-server/clearml-server-1-9-0.tar.gz](https://storage.googleapis.com/allegro-files/clearml-server/clearml-server-1-9-0.tar.gz)
- v1.8.0 - [https://storage.googleapis.com/allegro-files/clearml-server/clearml-server-1-8-0.tar.gz](https://storage.googleapis.com/allegro-files/clearml-server/clearml-server-1-8-0.tar.gz)
- v1.6.0 - [https://storage.googleapis.com/allegro-files/clearml-server/clearml-server-1-6-0.tar.gz](https://storage.googleapis.com/allegro-files/clearml-server/clearml-server-1-6-0.tar.gz)
- v1.5.0 - [https://storage.googleapis.com/allegro-files/clearml-server/clearml-server-1-5-0.tar.gz](https://storage.googleapis.com/allegro-files/clearml-server/clearml-server-1-5-0.tar.gz)
- v1.4.0 - [https://storage.googleapis.com/allegro-files/clearml-server/clearml-server-1-4-0.tar.gz](https://storage.googleapis.com/allegro-files/clearml-server/clearml-server-1-4-0.tar.gz)
- v1.3.1 - [https://storage.googleapis.com/allegro-files/clearml-server/clearml-server-1-3-1.tar.gz](https://storage.googleapis.com/allegro-files/clearml-server/clearml-server-1-3-1.tar.gz)
- v1.3.0 - [https://storage.googleapis.com/allegro-files/clearml-server/clearml-server-1-3-0.tar.gz](https://storage.googleapis.com/allegro-files/clearml-server/clearml-server-1-3-0.tar.gz)
- v1.2.0 - [https://storage.googleapis.com/allegro-files/clearml-server/clearml-server-1-2-0.tar.gz](https://storage.googleapis.com/allegro-files/clearml-server/clearml-server-1-2-0.tar.gz)
- v1.1.0 - [https://storage.googleapis.com/allegro-files/clearml-server/clearml-server-1-1-0.tar.gz](https://storage.googleapis.com/allegro-files/clearml-server/clearml-server-1-1-0.tar.gz)
- v1.0.2 - [https://storage.googleapis.com/allegro-files/clearml-server/clearml-server-1-0-2.tar.gz](https://storage.googleapis.com/allegro-files/clearml-server/clearml-server-1-0-2.tar.gz)
- v1.0.1 - [https://storage.googleapis.com/allegro-files/clearml-server/clearml-server-1-0-1.tar.gz](https://storage.googleapis.com/allegro-files/clearml-server/clearml-server-1-0-1.tar.gz)
- v1.0.0 - [https://storage.googleapis.com/allegro-files/clearml-server/clearml-server-1-0-0.tar.gz](https://storage.googleapis.com/allegro-files/clearml-server/clearml-server-1-0-0.tar.gz)
- v0.17.0 - [https://storage.googleapis.com/allegro-files/clearml-server/clearml-server-0-17-0.tar.gz](https://storage.googleapis.com/allegro-files/clearml-server/clearml-server-0-17-0.tar.gz)

## Next Step [​](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_gcp/\#next-step "Direct link to Next Step")

To keep track of your experiments and/or data, the `clearml` package needs to communicate with your server.
For instruction to connect the ClearML SDK to the server, see [ClearML Setup](https://clear.ml/docs/latest/docs/clearml_sdk/clearml_sdk_setup).

- [Default ClearML Server Service Ports](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_gcp/#default-clearml-server-service-ports)
- [Default ClearML Server Storage Paths](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_gcp/#default-clearml-server-storage-paths)
- [Importing the Custom Image to your GCP account](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_gcp/#importing-the-custom-image-to-your-gcp-account)
- [Launching](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_gcp/#launching)
- [Restarting](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_gcp/#restarting)
- [Backing Up and Restoring Data and Configuration](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_gcp/#backing-up-and-restoring-data-and-configuration)
- [ClearML Server GCP Custom Image](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_gcp/#clearml-server-gcp-custom-image)
  - [Latest Version - v1.13.0](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_gcp/#latest-version---v1130)
  - [All Release Versions](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_gcp/#all-release-versions)
- [Next Step](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_gcp/#next-step)