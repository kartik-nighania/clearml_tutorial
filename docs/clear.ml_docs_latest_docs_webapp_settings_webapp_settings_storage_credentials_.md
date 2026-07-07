---
url: "https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_storage_credentials/"
title: "Storage Cleanup | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_storage_credentials/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

To enable ClearML to delete task artifacts stored in cloud storage when a task is deleted, configure access credentials for your storage provider:

- [Google Cloud Storage](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_storage_credentials/#google-cloud-storage)
- [AWS S3 Storage](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_storage_credentials/#aws-s3-storage)
- [Azure](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_storage_credentials/#azure)

![Storage Cleanup page](https://clear.ml/docs/latest/assets/images/webapp_settings_storage_credentials-29c980db3418f999db1e70d24960b376.png#light-mode-only)![Storage Cleanup page](https://clear.ml/docs/latest/assets/images/webapp_settings_storage_credentials_dark-4e2e8e1a4a79ceaa973d11c919218cb2.png#dark-mode-only)

## Google Cloud Storage [​](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_storage_credentials/\#google-cloud-storage "Direct link to Google Cloud Storage")

Set up credentials for Google Cloud buckets:

- Default credentials - These credentials apply to all GCS buckets unless bucket-specific credentials are set.
  - Project - Default Google Cloud Storage project
  - Credentials JSON
- Bucket specific credentials:
  - Bucket
  - Project
  - Credentials JSON

## AWS S3 Storage [​](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_storage_credentials/\#aws-s3-storage "Direct link to AWS S3 Storage")

Set up credentials for S3 protocol storage (i.e. AWS S3, MinIO, etc.):

- Default credentials - These credentials apply to all buckets unless bucket-specific credentials are set:
  - Access Key - Default access key for the storage service.
  - Secret - Default secret access key.
  - Access token - Session key for temporary credentials (if applicable).
  - Region - Default region for all unspecified buckets.
  - Credentials Chain - If selected, use boto3 default [credentials search](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html#configuring-credentials)
    (i.e. look for credentials in environment variables, credential files, and instance metadata services).
- Bucket Specific Credentials:
  - Bucket - Name of the specific bucket.
  - Region - Region for the bucket.
  - Host - For non-AWS endpoints, the host URL and port number of the specific bucket. Note that port specification
    is _always_ needed (e.g. `my-minio-host:9000`), even for standard ports like 433 for HTTPS (e.g. `my-minio-host:433`)
  - Secure Host - Select in order to enable TLS.
  - Verify SSL certificate - Select to enable SSL verification for secure hosts.
  - Access key - Access key for the bucket.
  - Secret - Secret key for the bucket.
  - Access token - The session key for your bucket. This is only needed when you are using temporary credentials.
  - Use Credentials chain - If selected, use boto3 default [credentials search](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html#configuring-credentials)
    (i.e. looks for credentials in environment variables, credential files, and instance metadata services).

## Azure [​](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_storage_credentials/\#azure "Direct link to Azure")

Set up credentials for Azure storage containers:

- Account name - Azure storage account name.
- Account key - Azure storage account key.
- Container name - Name of the specific container.

- [Google Cloud Storage](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_storage_credentials/#google-cloud-storage)
- [AWS S3 Storage](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_storage_credentials/#aws-s3-storage)
- [Azure](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_storage_credentials/#azure)