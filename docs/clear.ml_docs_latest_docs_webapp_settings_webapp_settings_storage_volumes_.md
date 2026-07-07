---
url: "https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_storage_volumes/"
title: "Volumes | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_storage_volumes/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

Enterprise Feature

Volume templates and managed volumes are available under the ClearML Enterprise plan.

Volumes are storage configurations that can be assigned to projects to be applied by users to the workloads running in
those projects.

Tenant administrators create volumes using templates assigned to the tenant by platform administrators. These templates
can provide custom variables for the tenant administrators to further customize the storage configuration.

The **Volumes** table lists all currently defined storage volumes:

- Name
- Description
- Volume template
- Projects - The projects the volume can be applied to

The table also includes columns for the custom template variables in use by the existing volumes.

Hover over a volume in the table to **Edit** or **Delete** a volume.

Deleting a volume will remove all project storage configurations making use of the volume

## Create a Volume [​](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_storage_volumes/\#create-a-volume "Direct link to Create a Volume")

1. Click `+ Add Volume`

2. Input following information:
   - Name

   - Description

   - Availability - Define which projects can use this volume:
     - All Projects - Available across all projects
     - Selected Projects - Specify one or more projects. The volume will also be available to all subprojects of the selected projects
   - Volume template - Select a volume template.



     note





     Available templates are predefined by the platform administrator

   - Template Parameters - Additional parameters may be available depending on the selected template. Click **Available System Variables**
     for available built-in variables which can be used in volume configuration.
3. Click **Add**



![Volume settings](https://clear.ml/docs/latest/assets/images/settings_volume-1049c4804958f68da51b9ae8c75b47cc.png#light-mode-only)![Volume settings](https://clear.ml/docs/latest/assets/images/settings_volume_dark-c32dd4594f1b4b382c175060606efd41.png#dark-mode-only)


- [Create a Volume](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_storage_volumes/#create-a-volume)