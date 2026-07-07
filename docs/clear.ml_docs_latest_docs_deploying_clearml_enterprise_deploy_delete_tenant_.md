---
url: "https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/delete_tenant/"
title: "Deleting Tenants from ClearML | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/delete_tenant/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The following is a step-by-step guide for deleting tenants (i.e. companies, workspaces) from ClearML.

warning

Deleting a tenant is a destructive operation that cannot be undone.

- Make sure you have the data prior to deleting the tenant.
- Backing up the system before deleting is recommended.

The tenant deletion is done from MongoDB, ElasticsSearch, and the Fileserver.

The first two are done from within the `apiserver` container, and last from within the `fileserver` container.

Any external artifacts (ex: AWS S3, GCS, minio) can be removed manually.

## Deleting Tenants from MongoDB and ElasticSearch [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/delete_tenant/\#deleting-tenants-from-mongodb-and-elasticsearch "Direct link to Deleting Tenants from MongoDB and ElasticSearch")

1. Enter the `apiserver` in one of the following ways
   - In `docker-compose`:





     ```text
     sudo docker exec -it clearml-apiserver /bin/bash
     ```

   - In Kubernetes:





     ```text
     kubectl -n <namespace> exec -it <apiserver pod name> -c clearml-apiserver -- /bin/bash
     ```
2. Set the ID and the name of the company (tenant) you wish to delete





```text
tenant_to_delete=<tenant-id>

company_name_to_delete="<company-name>"
```

3. Delete the company's data from MongoDB:





```text
PYTHONPATH=../trains-server-repo python3 \

     -m jobs.management.delete_company_data_from_mongo \

     --id $tenant_to_delete \

     --name <company-name> \

     --delete-user
```











note





This also deletes the admin users. Remove `--delete-user` to avoid this.

4. Delete the company's data from ElasticSearch:





```text
PYTHONPATH=../trains-server-repo python3 \

   -m jobs.management.cleanup_deleted_companies \

   --ids $tenant_to_delete --delete-company
```

5. Exit pod/container


## Deleting Tenants from the Fileserver [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/delete_tenant/\#deleting-tenants-from-the-fileserver "Direct link to Deleting Tenants from the Fileserver")

To remove a tenant's data from the fileserver, you can choose one of the following methods depending on your deployment setup:

- Option 1: Delete the tenant's data from within the fileserver container or pod.
- Option 2: Delete the tenant's data externally from the host system.

### Option 1 - From Within the Fileserver [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/delete_tenant/\#option-1---from-within-the-fileserver "Direct link to Option 1 - From Within the Fileserver")

1. Enter the `fileserver` in one of the following ways
   - In `docker-compose`:





     ```text
     sudo docker exec -it clearml-fileserver /bin/bash
     ```

   - In Kubernetes:





     ```text
     kubectl -n <namespace> exec -it <fileserver pod name> -c clearml-fileserver -- /bin/bash
     ```
2. Run the following:





```text
rm -rf /mnt/fileserver/<tenant-id>
```

3. Exit pod/container


### Option 2 - External Deletion [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/delete_tenant/\#option-2---external-deletion "Direct link to Option 2 - External Deletion")

#### Docker compose [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/delete_tenant/\#docker-compose "Direct link to Docker compose")

Run the following:

```text
rm -rf ${CLEARML_ROOT}/data/fileserver/<tenant-id>
```

#### Kubernetes [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/delete_tenant/\#kubernetes "Direct link to Kubernetes")

Run the following:

```text
kubectl -n <namespace> exec -it <apiserver-pod-name> -c clearml-apiserver -- /bin/bash -c "PYTHONPATH=../trains-server-repo python3 -m jobs.management.delete_company_data_from_mongo --id <tenant-id> --delete-user"

kubectl -n <namespace> exec -it <apiserver-pod-name> -c clearml-apiserver -- /bin/bash -c "PYTHONPATH=../trains-server-repo python3 -m jobs.management.cleanup_deleted_companies --ids <tenant-id> --delete-company"

kubectl -n <namespace> exec -it <fileserver-pod-name> -c clearml-fileserver -- /bin/bash -c "rm -rf /mnt/fileserver/<tenant-id>"
```

- [Deleting Tenants from MongoDB and ElasticSearch](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/delete_tenant/#deleting-tenants-from-mongodb-and-elasticsearch)
- [Deleting Tenants from the Fileserver](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/delete_tenant/#deleting-tenants-from-the-fileserver)
  - [Option 1 - From Within the Fileserver](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/delete_tenant/#option-1---from-within-the-fileserver)
  - [Option 2 - External Deletion](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/delete_tenant/#option-2---external-deletion)