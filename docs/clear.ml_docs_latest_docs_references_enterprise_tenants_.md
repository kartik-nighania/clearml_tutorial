---
url: "https://clear.ml/docs/latest/docs/references/enterprise/tenants/"
title: "tenants | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

### POST /tenants.add\_or\_update\_global\_template\_variable [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#post-tenantsadd_or_update_global_template_variable "Direct link to POST /tenants.add_or_update_global_template_variable")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#description "Direct link to Description")

Create or update a global template variable

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#parameters "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-add_or_update_global_template_variable-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_optional_ | Variable ID (for updating an existing variable) | string |
| **name**<br>_required_ | Variable name | string |
| **value**<br>_required_ | Variable value | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#responses "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-add_or_update_global_template_variable-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_optional_ | Variable ID | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#security "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | root,system |

### POST /tenants.add\_or\_update\_volume\_template [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#post-tenantsadd_or_update_volume_template "Direct link to POST /tenants.add_or_update_volume_template")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#description-1 "Direct link to Description")

Internal. Update existing volume template (if ID provided). Or add a new one

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#parameters-1 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-add_or_update_volume_template-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **description**<br>_optional_ | Volume template description | string |
| **global\_template\_variables**<br>_optional_ | List of global template variable IDs used in this template | < string > array |
| **id**<br>_optional_ | Volume template ID (for update of the existing volume template) | string |
| **name**<br>_required_ | Volume Name | string |
| **spec**<br>_required_ | Volume spec | string |
| **tenants**<br>_optional_ | The list of tenant IDs that have access to this volume template | < string > array |
| **type**<br>_optional_ | Volume type | string |
| **variables**<br>_optional_ | The list of variable definitions | < [variables](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-add_or_update_volume_template-post-variables) \> array |

**variables**

| Name | Description | Schema |
| --- | --- | --- |
| **access**<br>_required_ | Who should set the environment variable | enum (tenant\_admin, user) |
| **default\_value**<br>_optional_ | The default value for the mandatory environment variable | string |
| **description**<br>_optional_ | Variable description | string |
| **display\_name**<br>_optional_ | Variable display name | string |
| **mandatory**<br>_optional_ | Whether environment variable is mandatory on not | boolean |
| **name**<br>_required_ | Variable name | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#responses-1 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-add_or_update_volume_template-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_optional_ | Volume ID | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#security-1 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | root,system |

### POST /tenants.add\_tenant\_admin\_credentials [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#post-tenantsadd_tenant_admin_credentials "Direct link to POST /tenants.add_tenant_admin_credentials")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#description-2 "Direct link to Description")

Generate new admin credentials for an existing tenant

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#parameters-2 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-add_tenant_admin_credentials-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **tenant**<br>_required_ | Tenant (company) ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#responses-2 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-add_tenant_admin_credentials-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **credentials**<br>_optional_ | Newly generated admin credentials | [credentials](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-add_tenant_admin_credentials-post-credentials) |

**credentials**

| Name | Schema |
| --- | --- |
| **access\_key**<br>_optional_ | string |
| **secret\_key**<br>_optional_ | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#security-2 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | root,system |

### POST /tenants.create\_tenant [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#post-tenantscreate_tenant "Direct link to POST /tenants.create_tenant")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#description-3 "Direct link to Description")

Create a new tenant with an admin user and return the admin credentials

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#parameters-3 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-create_tenant-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **admin\_emails**<br>_optional_ | Email addresses to pre-register as admins in this tenant | < string > array |
| **domain**<br>_optional_ | Email domain whose users will be routed to this tenant on login | string |
| **max\_service\_users**<br>_optional_ | Maximum number of service users allowed (omit for unlimited) | integer |
| **max\_users**<br>_optional_ | Maximum number of regular users allowed (omit for unlimited) | integer |
| **name**<br>_required_ | Tenant name <br>**Minimum length** : `3` | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#responses-3 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-create_tenant-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **credentials**<br>_optional_ | Admin credentials for the new tenant | [credentials](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-create_tenant-post-credentials) |
| **id**<br>_optional_ | Newly created tenant ID | string |

**credentials**

| Name | Schema |
| --- | --- |
| **access\_key**<br>_optional_ | string |
| **secret\_key**<br>_optional_ | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#security-3 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | root,system |

### POST /tenants.custom\_events [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#post-tenantscustom_events "Direct link to POST /tenants.custom_events")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#description-4 "Direct link to Description")

Report custom events to usage aggregator

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#parameters-4 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-custom_events-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **events**<br>_optional_ | Events data | < object > array |
| **template\_key**<br>_optional_ | Event template name | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#responses-4 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-custom_events-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **errors**<br>_optional_ | Errors | < string > array |
| **succeeded**<br>_optional_ | The amount of successfully sent events | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#security-4 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /tenants.delete\_global\_template\_variables [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#post-tenantsdelete_global_template_variables "Direct link to POST /tenants.delete_global_template_variables")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#description-5 "Direct link to Description")

Delete global template variables

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#parameters-5 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-delete_global_template_variables-request) |

**request**

| Name | Schema |
| --- | --- |
| **ids**<br>_required_ | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#responses-5 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-delete_global_template_variables-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **deleted**<br>_optional_ | The amount of deleted variables | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#security-5 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | root,system |

### POST /tenants.delete\_tenant [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#post-tenantsdelete_tenant "Direct link to POST /tenants.delete_tenant")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#description-6 "Direct link to Description")

Internal. Soft-delete a tenant. Requires the provided name to match the stored

tenant name. Rejects when the tenant has running resources unless force=true.

Returns the resource snapshot taken at deletion time.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#parameters-6 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-delete_tenant-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **force**<br>_optional_ | If true, delete even when running resources exist <br>**Default** : `false` | boolean |
| **name**<br>_required_ | Tenant name. Must match the stored Company.name as a safety check. | string |
| **tenant**<br>_required_ | Tenant ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#responses-6 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-delete_tenant-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **running**<br>_optional_ | Live entities currently using compute | [running](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-delete_tenant-post-running) |
| **totals**<br>_optional_ | All entities of each type, regardless of state | [totals](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-delete_tenant-post-totals) |

**running**

| Name | Description | Schema |
| --- | --- | --- |
| **active\_routes**<br>_optional_ | Number of enabled routes currently in use by running tasks | integer |
| **app\_tasks**<br>_optional_ | Number of running application instance tasks plus tasks they spawned | integer |
| **connected\_workers**<br>_optional_ | Number of workers that reported within the connected-worker timeout | integer |
| **pipeline\_tasks**<br>_optional_ | Number of running pipeline controller tasks | integer |
| **tasks**<br>_optional_ | Number of running tasks that are neither application nor pipeline tasks | integer |

**totals**

| Name | Description | Schema |
| --- | --- | --- |
| **datasets**<br>_optional_ | Total number of datasets (projects tagged as datasets) | integer |
| **dataviews**<br>_optional_ | Total number of dataviews | integer |
| **hyper\_datasets**<br>_optional_ | Total number of hyper datasets | integer |
| **reports**<br>_optional_ | Total number of reports | integer |
| **tasks**<br>_optional_ | Total number of tasks excluding reports and dataset-tagged tasks | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#security-6 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | root,system |

### POST /tenants.delete\_tenant\_variable\_override [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#post-tenantsdelete_tenant_variable_override "Direct link to POST /tenants.delete_tenant_variable_override")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#description-7 "Direct link to Description")

Delete a tenant-level override for a global template variable

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#parameters-7 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-delete_tenant_variable_override-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **tenant\_id**<br>_required_ | Tenant (company) ID | string |
| **variable\_id**<br>_required_ | Global template variable ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#responses-7 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#security-7 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | root,system |

### POST /tenants.delete\_volume\_templates [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#post-tenantsdelete_volume_templates "Direct link to POST /tenants.delete_volume_templates")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#description-8 "Direct link to Description")

Internal. Delete volume templates

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#parameters-8 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-delete_volume_templates-request) |

**request**

| Name | Schema |
| --- | --- |
| **ids**<br>_required_ | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#responses-8 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-delete_volume_templates-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **deleted**<br>_optional_ | The amount of deleted templates | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#security-8 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | root,system |

### POST /tenants.download\_events\_log [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#post-tenantsdownload_events_log "Direct link to POST /tenants.download_events_log")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#description-9 "Direct link to Description")

Internal. Downloads a plain-text log of all platform-wide worker events. Same

format as workers.download\_events\_log.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#parameters-9 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-download_events_log-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **max\_age\_days**<br>_optional_ | Maximum age in days for retrieving events. Default is 30. | integer |
| **tenant**<br>_optional_ | Optional tenant ID. If omitted, returns events for all tenants. | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#responses-9 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#security-9 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | root,system |

### POST /tenants.edit\_usage\_configuration [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#post-tenantsedit_usage_configuration "Direct link to POST /tenants.edit_usage_configuration")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#description-10 "Direct link to Description")

Internal. Edit the global usage aggregator configuration. The configuration

must be complete (every category has a count\_strategy). Returns the updated

configuration.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#parameters-10 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-edit_usage_configuration-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **events**<br>_optional_ | Categories keyed by category name | < string, [events](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-edit_usage_configuration-post-events) \> map |
| **pricing**<br>_optional_ |  | [pricing](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-edit_usage_configuration-post-pricing) |

**events**

| Name | Description | Schema |
| --- | --- | --- |
| **count\_strategy**<br>_optional_ | The algorithm used for calculating total usage per day (sum - all usage reports <br>are summed, max - the max value is taken) | enum (sum, max) |
| **display\_name**<br>_optional_ |  | string |
| **labels**<br>_optional_ | Category labels keyed by label name | < string, [labels](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-edit_usage_configuration-post-events-labels) \> map |
| **read\_only**<br>_optional_ | If set the category originates from the global configuration and cannot be <br>edited by the tenant | boolean |
| **type**<br>_optional_ |  | enum (compute, storage, model\_tokens, users, service\_accounts) |
| **unit\_name**<br>_optional_ |  | string |

**labels**

| Name | Description | Schema |
| --- | --- | --- |
| **display\_name**<br>_optional_ |  | string |
| **enabled**<br>_optional_ | If set to Falsethe label data is neither collected nor returned | boolean |
| **pricing**<br>_optional_ |  | [pricing](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-edit_usage_configuration-post-events-labels-pricing) |
| **read\_only**<br>_optional_ | If set the label originates from the global configuration and cannot be edited <br>by the tenant | boolean |

**pricing**

| Name | Schema |
| --- | --- |
| **price**<br>_optional_ | number |
| **units**<br>_optional_ | number |

**pricing**

| Name | Schema |
| --- | --- |
| **currency**<br>_optional_ | string |
| **read\_only**<br>_optional_ | boolean |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#responses-10 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-edit_usage_configuration-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **events**<br>_optional_ | Categories keyed by category name | < string, [events](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-edit_usage_configuration-post-events) \> map |
| **pricing**<br>_optional_ |  | [pricing](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-edit_usage_configuration-post-pricing) |

**events**

| Name | Description | Schema |
| --- | --- | --- |
| **count\_strategy**<br>_optional_ | The algorithm used for calculating total usage per day (sum - all usage reports <br>are summed, max - the max value is taken) | enum (sum, max) |
| **display\_name**<br>_optional_ |  | string |
| **labels**<br>_optional_ | Category labels keyed by label name | < string, [labels](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-edit_usage_configuration-post-events-labels) \> map |
| **read\_only**<br>_optional_ | If set the category originates from the global configuration and cannot be <br>edited by the tenant | boolean |
| **type**<br>_optional_ |  | enum (compute, storage, model\_tokens, users, service\_accounts) |
| **unit\_name**<br>_optional_ |  | string |

**labels**

| Name | Description | Schema |
| --- | --- | --- |
| **display\_name**<br>_optional_ |  | string |
| **enabled**<br>_optional_ | If set to Falsethe label data is neither collected nor returned | boolean |
| **pricing**<br>_optional_ |  | [pricing](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-edit_usage_configuration-post-events-labels-pricing) |
| **read\_only**<br>_optional_ | If set the label originates from the global configuration and cannot be edited <br>by the tenant | boolean |

**pricing**

| Name | Schema |
| --- | --- |
| **price**<br>_optional_ | number |
| **units**<br>_optional_ | number |

**pricing**

| Name | Schema |
| --- | --- |
| **currency**<br>_optional_ | string |
| **read\_only**<br>_optional_ | boolean |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#security-10 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | root,system |

### POST /tenants.get\_global\_template\_variables [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#post-tenantsget_global_template_variables "Direct link to POST /tenants.get_global_template_variables")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#description-11 "Direct link to Description")

Get all global template variables with all their tenant overrides.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#parameters-11 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-get_global_template_variables-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **ids**<br>_optional_ | Optional list of variable IDs to filter by | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#responses-11 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-get_global_template_variables-response-200) |

**Response 200**

| Name | Schema |
| --- | --- |
| **variables**<br>_optional_ | < [variables](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-get_global_template_variables-post-variables) \> array |

**variables**

| Name | Description | Schema |
| --- | --- | --- |
| **created**<br>_optional_ |  | string (date-time) |
| **id**<br>_optional_ |  | string |
| **last\_update**<br>_optional_ |  | string (date-time) |
| **name**<br>_optional_ |  | string |
| **tenant\_overrides**<br>_optional_ | Map of tenant ID to override value | < string, string > map |
| **value**<br>_optional_ |  | string |
| **volume\_templates**<br>_optional_ |  | < [volume\_templates](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-get_global_template_variables-post-variables-volume_templates) \> array |

**volume\_templates**

| Name | Schema |
| --- | --- |
| **id**<br>_optional_ | string |
| **name**<br>_optional_ | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#security-11 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | root,system |

### POST /tenants.get\_multitenant\_usages [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#post-tenantsget_multitenant_usages "Direct link to POST /tenants.get_multitenant_usages")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#description-12 "Direct link to Description")

Internal. Get aggregated usages across all tenants. Returns platform-wide

totals with an optional per-tenant breakdown when tenants\_breakdown is true.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#parameters-12 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-get_multitenant_usages-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **categories**<br>_optional_ | Selected categories | < string > array |
| **from\_date**<br>_required_ | Start date in the form YYYY-MM-DD | string (date) |
| **include\_labels**<br>_optional_ | If set the individual labels data is returned under the components <br>**Default** : `true` | boolean |
| **tenants**<br>_optional_ | Optional list of tenant IDs to limit the results to. If omitted, all tenants <br>are included. | < string > array |
| **tenants\_breakdown**<br>_optional_ | If true, return per-tenant time series instead of platform-wide totals <br>**Default** : `false` | boolean |
| **tenants\_sub\_category\_label**<br>_optional_ | Sub-category label key to scope the results by (e.g. 'a100') | string |
| **to\_date**<br>_required_ | End date in the form YYYY-MM-DD | string (date) |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#responses-12 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-get_multitenant_usages-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **categories**<br>_optional_ |  | < string, [categories](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-get_multitenant_usages-post-categories) \> map |
| **currency**<br>_optional_ |  | string |
| **dates**<br>_optional_ | Date strings for the breakdown period, index-aligned with per-tenant <br>usages/costs arrays. Present only when tenants\_breakdown is true. | < string (date) > array |
| **tenants**<br>_optional_ | Per-tenant time series entries, present only when tenants\_breakdown was <br>requested | < [tenants](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-get_multitenant_usages-post-tenants) \> array |
| **total\_cost**<br>_optional_ |  | number |

**categories**

| Name | Description | Schema |
| --- | --- | --- |
| **costs**<br>_optional_ | Category cost per date | < number > array |
| **count\_strategy**<br>_optional_ |  | enum (sum, max) |
| **dates**<br>_optional_ |  | < string (date) > array |
| **display\_name**<br>_optional_ | Display name | string |
| **free**<br>_optional_ | If set to Truethen no payments are defined for category labels | boolean |
| **labels**<br>_optional_ |  | < string, [labels](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-get_multitenant_usages-post-categories-labels) \> map |
| **total\_cost**<br>_optional_ | Total category cost for the chosen period | number |
| **total\_usage**<br>_optional_ | Total category usage for the chosen period | number |
| **total\_usage\_type**<br>_optional_ | Describes what information is presented by total\_usage field | enum (total, latest) |
| **type**<br>_optional_ |  | string |
| **unit\_name**<br>_optional_ |  | string |
| **usages**<br>_optional_ | Category usage per date | < number > array |

**labels**

| Name | Description | Schema |
| --- | --- | --- |
| **costs**<br>_optional_ | Label cost per date | < number > array |
| **display\_name**<br>_optional_ | Display name | string |
| **pricing**<br>_optional_ |  | [pricing](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-get_multitenant_usages-post-categories-labels-pricing) |
| **total\_cost**<br>_optional_ | Total label cost for the chosen period | number |
| **total\_usage**<br>_optional_ | Total label usage for the chosen period | number |
| **usages**<br>_optional_ | Label usage per date | < number > array |

**pricing**

| Name | Schema |
| --- | --- |
| **price**<br>_optional_ | number |
| **units**<br>_optional_ | integer |

**tenants**

| Name | Description | Schema |
| --- | --- | --- |
| **costs**<br>_optional_ | Daily cost values, index-aligned with top-level dates | < number > array |
| **tenant\_id**<br>_optional_ |  | string |
| **tenant\_name**<br>_optional_ |  | string |
| **total\_cost**<br>_optional_ |  | number |
| **total\_usage**<br>_optional_ |  | number |
| **usages**<br>_optional_ | Daily usage values, index-aligned with top-level dates | < number > array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#security-12 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | root,system |

### POST /tenants.get\_resource\_history [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#post-tenantsget_resource_history "Direct link to POST /tenants.get_resource_history")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#description-13 "Direct link to Description")

Internal. Returns resource usage history for a specific tenant or across all

tenants. When tenant is specified the response follows

get\_resource\_history\_response (each series includes dates). When tenant is

omitted the response follows get\_resource\_history\_multitenant\_response (dates

hoisted to root, per-tenant entries contain values only).

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#parameters-13 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-get_resource_history-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **category**<br>_optional_ | Workers category for collecting statistics | string |
| **from\_date**<br>_required_ | Starting time (in seconds from epoch) | number |
| **interval**<br>_required_ | Time interval in seconds for a single statistics point. Minimum value is 1. | integer |
| **resource\_group**<br>_optional_ | Workers resource group for collecting statistics | string |
| **resource\_type**<br>_optional_ | The type of the resources to return on the chart <br>**Default** : `"computation_count"` | enum (computation\_count, computation\_util, memory, storage, network) |
| **tenant**<br>_optional_ | Single tenant ID. If omitted and tenants also omitted, returns multi-tenant <br>response for all tenants. | string |
| **tenants**<br>_optional_ | Optional list of tenant IDs for multi-tenant response. If omitted along with <br>tenant, all tenants are returned. | < string > array |
| **to\_date**<br>_required_ | Ending time (in seconds from epoch) | number |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#responses-13 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-get_resource_history-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **avg\_cpu\_load**<br>_optional_ | Activity series that display the average cpu load percentage in the given time <br>interval. | [tenants.resource\_usage\_series](https://clear.ml/docs/latest/docs/references/enterprise/definitions#tenantsresource_usage_series) |
| **avg\_gpu\_util**<br>_optional_ | Activity series that display the average gpu utilizations percentage in the <br>given time interval. | [tenants.resource\_usage\_series](https://clear.ml/docs/latest/docs/references/enterprise/definitions#tenantsresource_usage_series) |
| **computed\_interval**<br>_optional_ | The interval that was actually used for the histogram. May be larger than the <br>requested one. | integer |
| **cpu\_count**<br>_optional_ | Activity series that display the number of unique cpus that reported in the <br>given time interval. | [tenants.resource\_usage\_series](https://clear.ml/docs/latest/docs/references/enterprise/definitions#tenantsresource_usage_series) |
| **cpu\_idle\_count**<br>_optional_ | Activity series that display the number of unique cpus whose usage was below <br>predefined utilization threshold in the given time interval. | [tenants.resource\_usage\_series](https://clear.ml/docs/latest/docs/references/enterprise/definitions#tenantsresource_usage_series) |
| **cpu\_max\_allowed**<br>_optional_ | Series of maximum CPUs declared by cluster reports at each interval. | [tenants.resource\_usage\_series](https://clear.ml/docs/latest/docs/references/enterprise/definitions#tenantsresource_usage_series) |
| **gpu\_count**<br>_optional_ | Activity series that display the number of unique gpus that reported in the <br>given time interval. | [tenants.resource\_usage\_series](https://clear.ml/docs/latest/docs/references/enterprise/definitions#tenantsresource_usage_series) |
| **gpu\_idle\_count**<br>_optional_ | Activity series that display the number of unique gpus whose usage was below <br>predefined utilization threshold in the given time interval. | [tenants.resource\_usage\_series](https://clear.ml/docs/latest/docs/references/enterprise/definitions#tenantsresource_usage_series) |
| **gpu\_max\_allowed**<br>_optional_ | Series of maximum GPUs declared by cluster reports at each interval. | [tenants.resource\_usage\_series](https://clear.ml/docs/latest/docs/references/enterprise/definitions#tenantsresource_usage_series) |
| **gpu\_ram\_free**<br>_optional_ | Activity series that display the total amount of free gpu memory in Gb in the <br>given time interval. | [tenants.resource\_usage\_series](https://clear.ml/docs/latest/docs/references/enterprise/definitions#tenantsresource_usage_series) |
| **gpu\_ram\_total**<br>_optional_ | Activity series that display the total amount of gpu memory in Gb in the given <br>time interval. | [tenants.resource\_usage\_series](https://clear.ml/docs/latest/docs/references/enterprise/definitions#tenantsresource_usage_series) |
| **home\_free**<br>_optional_ | Activity series that display free disk space percentage in the given time <br>interval. | [tenants.resource\_usage\_series](https://clear.ml/docs/latest/docs/references/enterprise/definitions#tenantsresource_usage_series) |
| **network\_rx**<br>_optional_ | Activity series that display the network receive rate in Mb per second in the <br>given time interval. | [tenants.resource\_usage\_series](https://clear.ml/docs/latest/docs/references/enterprise/definitions#tenantsresource_usage_series) |
| **network\_tx**<br>_optional_ | Activity series that display the network transfer rate in Mb per second in the <br>given time interval. | [tenants.resource\_usage\_series](https://clear.ml/docs/latest/docs/references/enterprise/definitions#tenantsresource_usage_series) |
| **ram\_free**<br>_optional_ | Activity series that display the total amount of free ram in Gb in the given <br>time interval. | [tenants.resource\_usage\_series](https://clear.ml/docs/latest/docs/references/enterprise/definitions#tenantsresource_usage_series) |
| **ram\_total**<br>_optional_ | Activity series that display the total amount of ram in Gb in the given time <br>interval. | [tenants.resource\_usage\_series](https://clear.ml/docs/latest/docs/references/enterprise/definitions#tenantsresource_usage_series) |
| **worker\_count**<br>_optional_ | Activity series with the number of unique workers that reported in the given <br>time interval. | [tenants.resource\_usage\_series](https://clear.ml/docs/latest/docs/references/enterprise/definitions#tenantsresource_usage_series) |
| **worker\_max\_allowed**<br>_optional_ | Series of maximum workers declared by cluster reports at each interval. | [tenants.resource\_usage\_series](https://clear.ml/docs/latest/docs/references/enterprise/definitions#tenantsresource_usage_series) |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#security-13 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | root,system |

### POST /tenants.get\_resource\_usages [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#post-tenantsget_resource_usages "Direct link to POST /tenants.get_resource_usages")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#description-14 "Direct link to Description")

Internal. Get resource groups with their usages for a specific tenant or across

all tenants. When querying a specific tenant, includes quota information and

consumption percentages.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#parameters-14 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-get_resource_usages-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **events\_from\_date**<br>_optional_ | Starting time (in seconds from epoch) for retrieving events | number |
| **expand\_groups**<br>_optional_ | The keys of the groups for which separate worker usages will be returned | < string > array |
| **filters**<br>_optional_ | List of FilterRule ('OR' connection) | < string, [filters](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-get_resource_usages-post-filters) \> map |
| **last\_events**<br>_optional_ | The amount of last worker events to retrieve. Pass 0 in order not to retrieve <br>any | integer |
| **tenant**<br>_optional_ | Optional tenant ID. If omitted, returns data for all tenants. | string |

**filters**

| Name | Description | Schema |
| --- | --- | --- |
| **allowed\_values**<br>_optional_ | The list of allowed string values | < string > array |
| **max\_value**<br>_optional_ | Max value | number |
| **min\_value**<br>_optional_ | Min value | number |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#responses-14 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#security-14 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | root,system |

### POST /tenants.get\_tenant\_info [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#post-tenantsget_tenant_info "Direct link to POST /tenants.get_tenant_info")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#description-15 "Direct link to Description")

Internal. Get tenant usages info

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#parameters-15 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-get_tenant_info-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **from\_date**<br>_optional_ | Starting time (in seconds from epoch) for collecting statistics | string (date-time) |
| **tenant**<br>_required_ | Tenant ID | string |
| **to\_date**<br>_optional_ | Ending time (in seconds from epoch) for collecting statistics. Pass null for <br>now | string (date-time) |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#responses-15 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-get_tenant_info-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **days**<br>_optional_ | Period in days used for the calculation | integer |
| **gpu\_types**<br>_optional_ |  | [gpu\_types](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-get_tenant_info-post-gpu_types) |
| **name**<br>_optional_ | Tenant name | string |
| **projects**<br>_optional_ |  | [projects](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-get_tenant_info-post-projects) |
| **tasks**<br>_optional_ |  | [tasks](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-get_tenant_info-post-tasks) |
| **users**<br>_optional_ |  | [users](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-get_tenant_info-post-users) |

**gpu\_types**

| Name | Schema |
| --- | --- |
| **series**<br>_optional_ | < [series](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-get_tenant_info-post-gpu_types-series) \> array |
| **total**<br>_optional_ | < [total](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-get_tenant_info-post-gpu_types-total) \> array |

**series**

| Name | Description | Schema |
| --- | --- | --- |
| **cpu\_usage**<br>_optional_ | Tasks running task multiplied by cpu resource | < number > array |
| **cpu\_usage\_artifical\_weights**<br>_optional_ | Indicate whether artificial cpu resource weights were used | boolean |
| **dates**<br>_optional_ | Date timestamp in seconds | < number > array |
| **duration**<br>_optional_ | Tasks running time in seconds | < number > array |
| **gpu\_usage**<br>_optional_ | Tasks running task multiplied by gpu resource | < number > array |
| **gpu\_usage\_artifical\_weights**<br>_optional_ | Indicate whether artificial gpu resource weights were used | boolean |
| **id**<br>_optional_ |  | string |
| **name**<br>_optional_ |  | string |

**total**

| Name | Description | Schema |
| --- | --- | --- |
| **cpu\_artificial\_weights**<br>_optional_ | Indicate whether artificial cpu resource weights were used | boolean |
| **cpu\_usage**<br>_optional_ | Tasks running task multiplied by cpu resource | number |
| **duration**<br>_optional_ | Tasks running time in seconds | integer |
| **gpu\_artificial\_weights**<br>_optional_ | Indicate whether artificial gpu resource weights were used | boolean |
| **gpu\_usage**<br>_optional_ | Tasks running task multiplied by gpu resource | number |
| **id**<br>_optional_ |  | string |
| **name**<br>_optional_ |  | string |

**projects**

| Name | Description | Schema |
| --- | --- | --- |
| **last\_count**<br>_optional_ | The amount of projects created in the last days period | integer |
| **previous\_count**<br>_optional_ | The amount of projects created in the before last days period | integer |
| **total**<br>_optional_ | Total amount of projects | integer |

**tasks**

| Name | Description | Schema |
| --- | --- | --- |
| **dates\_histogram**<br>_optional_ | Created tasks per day | < [dates\_histogram](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-get_tenant_info-post-tasks-dates_histogram) \> array |
| **last\_count**<br>_optional_ | The amount of tasks created in the last days period | integer |
| **previous\_count**<br>_optional_ | The amount of tasks created in the before last days period | integer |
| **total**<br>_optional_ | Total amount of tasks | integer |

**dates\_histogram**

| Name | Description | Schema |
| --- | --- | --- |
| **count**<br>_optional_ | Tasks count | integer |
| **date**<br>_optional_ |  | string (date-time) |

**users**

| Name | Description | Schema |
| --- | --- | --- |
| **active**<br>_optional_ |  | < [active](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-get_tenant_info-post-users-active) \> array |
| **max\_allowed**<br>_optional_ | The maximum number of allowed users | integer |
| **pending**<br>_optional_ |  | < [pending](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-get_tenant_info-post-users-pending) \> array |

**active**

| Name | Description | Schema |
| --- | --- | --- |
| **created**<br>_optional_ | The time when the user was created | string |
| **email**<br>_optional_ | User email | string |
| **id**<br>_optional_ | User ID | string |
| **last\_login**<br>_optional_ | The last time the user performed login | string (date-time) |
| **name**<br>_optional_ | User name | string |
| **role**<br>_optional_ | User role | string |

**pending**

| Name | Description | Schema |
| --- | --- | --- |
| **added**<br>_optional_ | The date when the whitelist entry was created | string (date-time) |
| **email**<br>_optional_ | User email | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#security-15 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | root,system |

### POST /tenants.get\_tenant\_resources [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#post-tenantsget_tenant_resources "Direct link to POST /tenants.get_tenant_resources")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#description-16 "Direct link to Description")

Internal. Get a snapshot of the tenant's live and total resources. Used as a

pre-flight for tenant deletion.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#parameters-16 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-get_tenant_resources-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **tenant**<br>_required_ | Tenant ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#responses-16 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-get_tenant_resources-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **running**<br>_optional_ | Live entities currently using compute | [running](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-get_tenant_resources-post-running) |
| **totals**<br>_optional_ | All entities of each type, regardless of state | [totals](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-get_tenant_resources-post-totals) |

**running**

| Name | Description | Schema |
| --- | --- | --- |
| **active\_routes**<br>_optional_ | Number of enabled routes currently in use by running tasks | integer |
| **app\_tasks**<br>_optional_ | Number of running application instance tasks plus tasks they spawned | integer |
| **connected\_workers**<br>_optional_ | Number of workers that reported within the connected-worker timeout | integer |
| **pipeline\_tasks**<br>_optional_ | Number of running pipeline controller tasks | integer |
| **tasks**<br>_optional_ | Number of running tasks that are neither application nor pipeline tasks | integer |

**totals**

| Name | Description | Schema |
| --- | --- | --- |
| **datasets**<br>_optional_ | Total number of datasets (projects tagged as datasets) | integer |
| **dataviews**<br>_optional_ | Total number of dataviews | integer |
| **hyper\_datasets**<br>_optional_ | Total number of hyper datasets | integer |
| **reports**<br>_optional_ | Total number of reports | integer |
| **tasks**<br>_optional_ | Total number of tasks excluding reports and dataset-tagged tasks | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#security-16 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | root,system |

### POST /tenants.get\_tenant\_usages [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#post-tenantsget_tenant_usages "Direct link to POST /tenants.get_tenant_usages")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#description-17 "Direct link to Description")

Internal. Get tenant aggregated usages

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#parameters-17 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-get_tenant_usages-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **categories**<br>_optional_ | Selected categories | < string > array |
| **from\_date**<br>_required_ | Start date in the form YYYY-MM-DD | string (date) |
| **include\_labels**<br>_optional_ | If set the individual labels data is returned under the components <br>**Default** : `true` | boolean |
| **tenant**<br>_required_ | Tenant ID | string |
| **to\_date**<br>_required_ | End date in the form YYYY-MM-DD | string (date) |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#responses-17 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-get_tenant_usages-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **categories**<br>_optional_ |  | < string, [categories](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-get_tenant_usages-post-categories) \> map |
| **currency**<br>_optional_ |  | string |
| **name**<br>_optional_ | Tenant name | string |
| **total\_cost**<br>_optional_ |  | number |

**categories**

| Name | Description | Schema |
| --- | --- | --- |
| **costs**<br>_optional_ | Category cost per date | < number > array |
| **count\_strategy**<br>_optional_ |  | enum (sum, max) |
| **dates**<br>_optional_ |  | < string (date) > array |
| **display\_name**<br>_optional_ | Display name | string |
| **free**<br>_optional_ | If set to Truethen no payments are defined for category labels | boolean |
| **labels**<br>_optional_ |  | < string, [labels](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-get_tenant_usages-post-categories-labels) \> map |
| **total\_cost**<br>_optional_ | Total category cost for the chosen period | number |
| **total\_usage**<br>_optional_ | Total category usage for the chosen period | number |
| **total\_usage\_type**<br>_optional_ | Describes what information is presented by total\_usage field | enum (total, latest) |
| **type**<br>_optional_ |  | string |
| **unit\_name**<br>_optional_ |  | string |
| **usages**<br>_optional_ | Category usage per date | < number > array |

**labels**

| Name | Description | Schema |
| --- | --- | --- |
| **costs**<br>_optional_ | Label cost per date | < number > array |
| **display\_name**<br>_optional_ | Display name | string |
| **pricing**<br>_optional_ |  | [pricing](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-get_tenant_usages-post-categories-labels-pricing) |
| **total\_cost**<br>_optional_ | Total label cost for the chosen period | number |
| **total\_usage**<br>_optional_ | Total label usage for the chosen period | number |
| **usages**<br>_optional_ | Label usage per date | < number > array |

**pricing**

| Name | Schema |
| --- | --- |
| **price**<br>_optional_ | number |
| **units**<br>_optional_ | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#security-17 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | root,system |

### POST /tenants.get\_tenants [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#post-tenantsget_tenants "Direct link to POST /tenants.get_tenants")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#description-18 "Direct link to Description")

Internal. Get tenants list

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#parameters-18 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#responses-18 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-get_tenants-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **tenants**<br>_optional_ | List of tenants | < [tenants](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-get_tenants-post-tenants) \> array |

**tenants**

| Name | Schema |
| --- | --- |
| **admin\_emails**<br>_optional_ | < string > array |
| **default\_company**<br>_optional_ | boolean |
| **id**<br>_optional_ | string |
| **name**<br>_optional_ | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#security-18 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | root,system |

### POST /tenants.get\_usage\_configuration [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#post-tenantsget_usage_configuration "Direct link to POST /tenants.get_usage_configuration")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#description-19 "Direct link to Description")

Internal. Get the global usage aggregator configuration

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#parameters-19 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#responses-19 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-get_usage_configuration-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **events**<br>_optional_ | Categories keyed by category name | < string, [events](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-get_usage_configuration-post-events) \> map |
| **pricing**<br>_optional_ |  | [pricing](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-get_usage_configuration-post-pricing) |

**events**

| Name | Description | Schema |
| --- | --- | --- |
| **count\_strategy**<br>_optional_ | The algorithm used for calculating total usage per day (sum - all usage reports <br>are summed, max - the max value is taken) | enum (sum, max) |
| **display\_name**<br>_optional_ |  | string |
| **labels**<br>_optional_ | Category labels keyed by label name | < string, [labels](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-get_usage_configuration-post-events-labels) \> map |
| **read\_only**<br>_optional_ | If set the category originates from the global configuration and cannot be <br>edited by the tenant | boolean |
| **type**<br>_optional_ |  | enum (compute, storage, model\_tokens, users, service\_accounts) |
| **unit\_name**<br>_optional_ |  | string |

**labels**

| Name | Description | Schema |
| --- | --- | --- |
| **display\_name**<br>_optional_ |  | string |
| **enabled**<br>_optional_ | If set to Falsethe label data is neither collected nor returned | boolean |
| **pricing**<br>_optional_ |  | [pricing](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-get_usage_configuration-post-events-labels-pricing) |
| **read\_only**<br>_optional_ | If set the label originates from the global configuration and cannot be edited <br>by the tenant | boolean |

**pricing**

| Name | Schema |
| --- | --- |
| **price**<br>_optional_ | number |
| **units**<br>_optional_ | number |

**pricing**

| Name | Schema |
| --- | --- |
| **currency**<br>_optional_ | string |
| **read\_only**<br>_optional_ | boolean |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#security-19 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | root,system |

### POST /tenants.get\_volume\_templates [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#post-tenantsget_volume_templates "Direct link to POST /tenants.get_volume_templates")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#description-20 "Direct link to Description")

Internal. Get volume templates

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#parameters-20 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-get_volume_templates-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **ids**<br>_optional_ |  | < string > array |
| **tenant**<br>_optional_ | Tenant ID. If passed then only volume templates for this tenant are returned | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#responses-20 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-get_volume_templates-response-200) |

**Response 200**

| Name | Schema |
| --- | --- |
| **volume\_templates**<br>_optional_ | < [volume\_templates](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-get_volume_templates-post-volume_templates) \> array |

**volume\_templates**

| Name | Description | Schema |
| --- | --- | --- |
| **created**<br>_optional_ | Volume template creation time | string (date-time) |
| **description**<br>_optional_ | Volume template description | string |
| **global\_template\_variables**<br>_optional_ | List of global template variable IDs used in this template | < string > array |
| **id**<br>_optional_ | Volume template ID (for update of the existing volume template) | string |
| **last\_update**<br>_optional_ | Volume template last update time | string (date-time) |
| **name**<br>_optional_ | Volume Name | string |
| **spec**<br>_optional_ | Volume spec | string |
| **tenants**<br>_optional_ | The list of tenant IDs that have access to this volume template | < [tenants](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-get_volume_templates-post-volume_templates-tenants) \> array |
| **type**<br>_optional_ | Volume type | string |
| **variables**<br>_optional_ | The list of variable definitions | < [variables](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-get_volume_templates-post-volume_templates-variables) \> array |

**tenants**

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_optional_ |  | string |
| **in\_use**<br>_optional_ | The amount of tenant volumes based on this template | integer |
| **name**<br>_optional_ |  | string |

**variables**

| Name | Description | Schema |
| --- | --- | --- |
| **access**<br>_required_ | Who should set the environment variable | enum (tenant\_admin, user) |
| **default\_value**<br>_optional_ | The default value for the mandatory environment variable | string |
| **description**<br>_optional_ | Variable description | string |
| **display\_name**<br>_optional_ | Variable display name | string |
| **mandatory**<br>_optional_ | Whether environment variable is mandatory on not | boolean |
| **name**<br>_required_ | Variable name | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#security-20 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | root,system |

### POST /tenants.set\_tenant\_variable\_override [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#post-tenantsset_tenant_variable_override "Direct link to POST /tenants.set_tenant_variable_override")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#description-21 "Direct link to Description")

Set or update a tenant-level override for a global template variable

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#parameters-21 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#tenants-set_tenant_variable_override-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **override\_value**<br>_required_ | The override value for this tenant | string |
| **tenant\_id**<br>_required_ | Tenant (company) ID | string |
| **variable\_id**<br>_required_ | Global template variable ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#responses-21 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/tenants/\#security-21 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | root,system |

- [POST /tenants.add\_or\_update\_global\_template\_variable](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#post-tenantsadd_or_update_global_template_variable)
- [POST /tenants.add\_or\_update\_volume\_template](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#post-tenantsadd_or_update_volume_template)
- [POST /tenants.add\_tenant\_admin\_credentials](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#post-tenantsadd_tenant_admin_credentials)
- [POST /tenants.create\_tenant](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#post-tenantscreate_tenant)
- [POST /tenants.custom\_events](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#post-tenantscustom_events)
- [POST /tenants.delete\_global\_template\_variables](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#post-tenantsdelete_global_template_variables)
- [POST /tenants.delete\_tenant](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#post-tenantsdelete_tenant)
- [POST /tenants.delete\_tenant\_variable\_override](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#post-tenantsdelete_tenant_variable_override)
- [POST /tenants.delete\_volume\_templates](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#post-tenantsdelete_volume_templates)
- [POST /tenants.download\_events\_log](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#post-tenantsdownload_events_log)
- [POST /tenants.edit\_usage\_configuration](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#post-tenantsedit_usage_configuration)
- [POST /tenants.get\_global\_template\_variables](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#post-tenantsget_global_template_variables)
- [POST /tenants.get\_multitenant\_usages](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#post-tenantsget_multitenant_usages)
- [POST /tenants.get\_resource\_history](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#post-tenantsget_resource_history)
- [POST /tenants.get\_resource\_usages](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#post-tenantsget_resource_usages)
- [POST /tenants.get\_tenant\_info](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#post-tenantsget_tenant_info)
- [POST /tenants.get\_tenant\_resources](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#post-tenantsget_tenant_resources)
- [POST /tenants.get\_tenant\_usages](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#post-tenantsget_tenant_usages)
- [POST /tenants.get\_tenants](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#post-tenantsget_tenants)
- [POST /tenants.get\_usage\_configuration](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#post-tenantsget_usage_configuration)
- [POST /tenants.get\_volume\_templates](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#post-tenantsget_volume_templates)
- [POST /tenants.set\_tenant\_variable\_override](https://clear.ml/docs/latest/docs/references/enterprise/tenants/#post-tenantsset_tenant_variable_override)