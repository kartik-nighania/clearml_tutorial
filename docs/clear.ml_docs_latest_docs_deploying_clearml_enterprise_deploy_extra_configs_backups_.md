---
url: "https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/backups/"
title: "Backup | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/backups/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

ClearML stores its data in multiple storage components:

- [File Server](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/backups/#file-server)
- [Elasticsearch](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/backups/#elasticsearch)
- [MongoDB](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/backups/#mongodb)

It is recommended to back these up periodically to ensure data consistency and to avoid corruption during restore operations.

The following describes recommended practices for backing up data used by ClearML deployments on Kubernetes and on-premise
Ubuntu servers. See [Backups on AWS](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/vpc_aws#backups) for best practices for AWS VPC deployments.

## File Server [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/backups/\#file-server "Direct link to File Server")

The File Server stores task artifacts, models, and other binary assets.

### Backup Recommendations [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/backups/\#backup-recommendations "Direct link to Backup Recommendations")

- Back up the entire File Server volume.
- Perform backups at least daily.
- Maintain a minimum retention period of 2 days, or longer based on operational and compliance requirements.

### Deployment Specific Notes [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/backups/\#deployment-specific-notes "Direct link to Deployment Specific Notes")

- Docker Compose - Back up the Docker volume or host directory mounted into the File Server container.
- Kubernetes - Back up the PersistentVolume (PV) used by the File Server using the cluster’s storage-level snapshot or backup solution.

Filesystem-level backups are sufficient for the File Server, as it does not maintain internal transactional state.

## Elasticsearch [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/backups/\#elasticsearch "Direct link to Elasticsearch")

Elasticsearch stores indexed metadata and task-related information that must remain internally consistent.

important

Elastic cannot be safely backed up by copying data directories or underlying disks.

Such approaches may capture partial shard states or inconsistent indices, leading to corrupted snapshots or failed restores.

### Recommended Approach [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/backups/\#recommended-approach "Direct link to Recommended Approach")

Use Elasticsearch snapshots, which are designed to safely and consistently back up indices and cluster state.

Refer to [ElasticSearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/snapshot-restore.html)
for instructions for creating snapshots.

### Deployment Specific Notes [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/backups/\#deployment-specific-notes-1 "Direct link to Deployment Specific Notes")

- Docker Compose - Configure a snapshot repository (for example, a filesystem path or S3-compatible object storage) and
trigger snapshot operations using the Elasticsearch API.
- Kubernetes - Use the same snapshot mechanisms, typically targeting external object storage. The exact setup depends on
the Elasticsearch version, deployment method, and whether an operator is used.

## MongoDB [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/backups/\#mongodb "Direct link to MongoDB")

MongoDB stores ClearML metadata and requires consistent, database-aware backups.

important

Backing up MongoDB by copying data directories or disks while the database is running is unsafe.

### Recommended Approach [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/backups/\#recommended-approach-1 "Direct link to Recommended Approach")

Use MongoDB-supported backup methods, such as:

- Filesystem snapshots coordinated with MongoDB
- Replica-set-aware or managed backup solutions

Refer to [MongoDB’s documentation](https://www.mongodb.com/docs/manual/core/backups/) for backing up and restoring instructions.

### Deployment Specific Notes [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/backups/\#deployment-specific-notes-2 "Direct link to Deployment Specific Notes")

- Docker Compose - Execute backup commands using MongoDB tools against the running service, or run backups from a
dedicated backup container or scheduled job.
- Kubernetes - Use Kubernetes Jobs, database operators, or managed database services to perform backups in accordance
with MongoDB best practices.

- [File Server](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/backups/#file-server)
  - [Backup Recommendations](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/backups/#backup-recommendations)
  - [Deployment Specific Notes](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/backups/#deployment-specific-notes)
- [Elasticsearch](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/backups/#elasticsearch)
  - [Recommended Approach](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/backups/#recommended-approach)
  - [Deployment Specific Notes](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/backups/#deployment-specific-notes-1)
- [MongoDB](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/backups/#mongodb)
  - [Recommended Approach](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/backups/#recommended-approach-1)
  - [Deployment Specific Notes](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/backups/#deployment-specific-notes-2)