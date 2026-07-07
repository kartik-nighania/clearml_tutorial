---
url: "https://clear.ml/docs/latest/docs/references/enterprise/organization/"
title: "organization | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/enterprise/organization/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

### POST /organization.allow\_project\_workloads [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#post-organizationallow_project_workloads "Direct link to POST /organization.allow_project_workloads")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#description "Direct link to Description")

Internal. Determines whether the project workloads can be called on the passed

project by the calling user

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#parameters "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/organization/#organization-allow_project_workloads-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **project**<br>_required_ | Project ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#responses "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/organization/#organization-allow_project_workloads-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **allowed**<br>_optional_ | 'true' if the project workloads allowed. 'false' otherwise | boolean |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#security "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /organization.delete\_usage\_configuration [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#post-organizationdelete_usage_configuration "Direct link to POST /organization.delete_usage_configuration")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#description-1 "Direct link to Description")

Delete the calling tenant's usage aggregator configuration additions

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#parameters-1 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#responses-1 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/organization/#organization-delete_usage_configuration-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **deleted**<br>_optional_ | Number of deleted configurations | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#security-1 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /organization.download\_for\_get\_all [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#post-organizationdownload_for_get_all "Direct link to POST /organization.download_for_get_all")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#description-2 "Direct link to Description")

Generates a file for the download

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#parameters-2 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/organization/#organization-download_for_get_all-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **prepare\_id**<br>_required_ | Call ID returned by a call to prepare\_download\_for\_get\_all | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#responses-2 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#security-2 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /organization.edit\_usage\_configuration [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#post-organizationedit_usage_configuration "Direct link to POST /organization.edit_usage_configuration")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#description-3 "Direct link to Description")

Edit the usage aggregator configuration for the calling tenant. Only categories

and labels that are not defined in the global configuration are stored. Returns

the updated configuration.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#parameters-3 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/organization/#organization-edit_usage_configuration-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **events**<br>_optional_ | Categories keyed by category name | < string, [events](https://clear.ml/docs/latest/docs/references/enterprise/organization/#organization-edit_usage_configuration-post-events) \> map |
| **pricing**<br>_optional_ |  | [pricing](https://clear.ml/docs/latest/docs/references/enterprise/organization/#organization-edit_usage_configuration-post-pricing) |

**events**

| Name | Description | Schema |
| --- | --- | --- |
| **count\_strategy**<br>_optional_ | The algorithm used for calculating total usage per day (sum - all usage reports <br>are summed, max - the max value is taken) | enum (sum, max) |
| **display\_name**<br>_optional_ |  | string |
| **labels**<br>_optional_ | Category labels keyed by label name | < string, [labels](https://clear.ml/docs/latest/docs/references/enterprise/organization/#organization-edit_usage_configuration-post-events-labels) \> map |
| **read\_only**<br>_optional_ | If set the category originates from the global configuration and cannot be <br>edited by the tenant | boolean |
| **type**<br>_optional_ |  | enum (compute, storage, model\_tokens, users, service\_accounts) |
| **unit\_name**<br>_optional_ |  | string |

**labels**

| Name | Description | Schema |
| --- | --- | --- |
| **display\_name**<br>_optional_ |  | string |
| **enabled**<br>_optional_ | If set to Falsethe label data is neither collected nor returned | boolean |
| **pricing**<br>_optional_ |  | [pricing](https://clear.ml/docs/latest/docs/references/enterprise/organization/#organization-edit_usage_configuration-post-events-labels-pricing) |
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

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#responses-3 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/organization/#organization-edit_usage_configuration-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **events**<br>_optional_ | Categories keyed by category name | < string, [events](https://clear.ml/docs/latest/docs/references/enterprise/organization/#organization-edit_usage_configuration-post-events) \> map |
| **pricing**<br>_optional_ |  | [pricing](https://clear.ml/docs/latest/docs/references/enterprise/organization/#organization-edit_usage_configuration-post-pricing) |

**events**

| Name | Description | Schema |
| --- | --- | --- |
| **count\_strategy**<br>_optional_ | The algorithm used for calculating total usage per day (sum - all usage reports <br>are summed, max - the max value is taken) | enum (sum, max) |
| **display\_name**<br>_optional_ |  | string |
| **labels**<br>_optional_ | Category labels keyed by label name | < string, [labels](https://clear.ml/docs/latest/docs/references/enterprise/organization/#organization-edit_usage_configuration-post-events-labels) \> map |
| **read\_only**<br>_optional_ | If set the category originates from the global configuration and cannot be <br>edited by the tenant | boolean |
| **type**<br>_optional_ |  | enum (compute, storage, model\_tokens, users, service\_accounts) |
| **unit\_name**<br>_optional_ |  | string |

**labels**

| Name | Description | Schema |
| --- | --- | --- |
| **display\_name**<br>_optional_ |  | string |
| **enabled**<br>_optional_ | If set to Falsethe label data is neither collected nor returned | boolean |
| **pricing**<br>_optional_ |  | [pricing](https://clear.ml/docs/latest/docs/references/enterprise/organization/#organization-edit_usage_configuration-post-events-labels-pricing) |
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

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#security-3 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /organization.get\_entities\_count [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#post-organizationget_entities_count "Direct link to POST /organization.get_entities_count")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#description-4 "Direct link to Description")

Get counts for the company entities according to the passed search criteria

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#parameters-4 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/organization/#organization-get_entities_count-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **active\_users**<br>_optional_ | The list of users that were active in the project. If passes then the resulting <br>projects are filtered to the ones that have tasks created by these users | < string > array |
| **allow\_public**<br>_optional_ | Allow public entities to be counted in the results <br>**Default** : `true` | boolean |
| **dataset\_versions**<br>_optional_ | Search criteria for dataset versions | object |
| **datasets**<br>_optional_ | Search criteria for datasets | object |
| **dataviews**<br>_optional_ | Search criteria for dataviews | object |
| **hyper\_dataset\_versions**<br>_optional_ | Search criteria for hyper dataset versions | object |
| **hyper\_datasets**<br>_optional_ | Search criteria for hyper datasets | object |
| **limit**<br>_optional_ | If specified then items only up to this limit are counted | integer |
| **models**<br>_optional_ | Search criteria for models | object |
| **pipeline\_runs**<br>_optional_ | Search criteria for pipeline runs | object |
| **pipelines**<br>_optional_ | Search criteria for pipelines | object |
| **projects**<br>_optional_ | Search criteria for projects | object |
| **reports**<br>_optional_ | Search criteria for reports | object |
| **search\_hidden**<br>_optional_ | If set to 'true' then hidden projects and tasks are included in the search <br>results <br>**Default** : `false` | boolean |
| **tasks**<br>_optional_ | Search criteria for experiments | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#responses-4 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/organization/#organization-get_entities_count-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **dataset\_versions**<br>_optional_ | The number of dataset versions matching the criteria | integer |
| **datasets**<br>_optional_ | The number of datasets matching the criteria | integer |
| **dataviews**<br>_optional_ | The number of dataviews matching the criteria | integer |
| **errors**<br>_optional_ |  | [errors](https://clear.ml/docs/latest/docs/references/enterprise/organization/#organization-get_entities_count-post-errors) |
| **hyper\_dataset\_versions**<br>_optional_ | The number of hyper dataset versions matching the criteria | integer |
| **hyper\_datasets**<br>_optional_ | The number of hyper datasets matching the criteria | integer |
| **models**<br>_optional_ | The number of models matching the criteria | integer |
| **pipeline\_runs**<br>_optional_ | The number of pipeline runs matching the criteria | integer |
| **pipelines**<br>_optional_ | The number of pipelines matching the criteria | integer |
| **projects**<br>_optional_ | The number of projects matching the criteria | integer |
| **reports**<br>_optional_ | The number of reports matching the criteria | integer |
| **tasks**<br>_optional_ | The number of experiments matching the criteria | integer |

**errors**

| Name | Schema |
| --- | --- |
| **dataset\_versions**<br>_optional_ | string |
| **datasets**<br>_optional_ | string |
| **dataviews**<br>_optional_ | string |
| **hyper\_dataset\_versions**<br>_optional_ | string |
| **hyperdatasets**<br>_optional_ | string |
| **models**<br>_optional_ | string |
| **pipeline\_runs**<br>_optional_ | string |
| **pipelines**<br>_optional_ | string |
| **projects**<br>_optional_ | string |
| **reports**<br>_optional_ | string |
| **tasks**<br>_optional_ | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#security-4 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /organization.get\_project\_company [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#post-organizationget_project_company "Direct link to POST /organization.get_project_company")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#description-5 "Direct link to Description")

Get the company that the project belongs to (provided that the user has access

to this company)

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#parameters-5 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/organization/#organization-get_project_company-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **project**<br>_required_ | The id of the project | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#responses-5 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/organization/#organization-get_project_company-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **company**<br>_optional_ | If the project can be found under one of the user companies then its company id <br>is returned. Otherwise None | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#security-5 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /organization.get\_project\_workloads [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#post-organizationget_project_workloads "Direct link to POST /organization.get_project_workloads")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#description-6 "Direct link to Description")

Get projects usage breakdown

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#parameters-6 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/organization/#organization-get_project_workloads-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **breakdown\_keys**<br>_optional_ | breakdown keys | < enum (project, user, queue) > array |
| **from\_date**<br>_required_ | Starting time (in seconds from epoch) for collecting statistics | string (date-time) |
| **include\_development**<br>_optional_ | If set to 'true' then development tasks are also returned <br>**Default** : `false` | boolean |
| **projects**<br>_required_ | Project IDs | < string > array |
| **to\_date**<br>_required_ | Ending time (in seconds from epoch) for collecting statistics. Pass null for <br>now | string (date-time) |
| **usage\_fields**<br>_optional_ | usage\_fields | < enum (duration, cpu\_usage, gpu\_usage) > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#responses-6 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/organization/#organization-get_project_workloads-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **projects**<br>_optional_ | Usages by project | [organization.workloads](https://clear.ml/docs/latest/docs/references/enterprise/definitions#organizationworkloads) |
| **queues**<br>_optional_ | Usages by user | [organization.workloads](https://clear.ml/docs/latest/docs/references/enterprise/definitions#organizationworkloads) |
| **users**<br>_optional_ | Usages by user | [organization.workloads](https://clear.ml/docs/latest/docs/references/enterprise/definitions#organizationworkloads) |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#security-6 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /organization.get\_services [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#post-organizationget_services "Direct link to POST /organization.get_services")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#description-7 "Direct link to Description")

Get company services

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#parameters-7 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#responses-7 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/organization/#organization-get_services-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **services**<br>_optional_ | Company services | < [organization.service\_info](https://clear.ml/docs/latest/docs/references/enterprise/definitions#organizationservice_info) \> array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#security-7 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /organization.get\_tags [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#post-organizationget_tags "Direct link to POST /organization.get_tags")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#description-8 "Direct link to Description")

Get all the user and system tags used for the company tasks and models

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#parameters-8 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/organization/#organization-get_tags-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **filter**<br>_optional_ | Filter on entities to collect tags from | [filter](https://clear.ml/docs/latest/docs/references/enterprise/organization/#organization-get_tags-post-filter) |
| **include\_system**<br>_optional_ | If set to 'true' then the list of the system tags is also returned. The default <br>value is 'false' <br>**Default** : `false` | boolean |

**filter**

| Name | Description | Schema |
| --- | --- | --- |
| **system\_tags**<br>_optional_ | The list of system tag values to filter by. Use 'null' value to specify empty <br>system tags. Use '\_\_Snot' value to specify that the following value should be <br>excluded | < string > array |
| **tags**<br>_optional_ | The list of tag values to filter by. Use 'null' value to specify empty tags. <br>Use '\_\_Snot' value to specify that the following value should be excluded | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#responses-8 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/organization/#organization-get_tags-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **system\_tags**<br>_optional_ | The list of unique system tag values. Returned only if 'include\_system' is set <br>to 'true' in the request | < string > array |
| **tags**<br>_optional_ | The list of unique tag values | < string > array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#security-8 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /organization.get\_tenant\_usages [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#post-organizationget_tenant_usages "Direct link to POST /organization.get_tenant_usages")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#description-9 "Direct link to Description")

Get tenant aggregated usages

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#parameters-9 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/organization/#organization-get_tenant_usages-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **categories**<br>_optional_ | Selected categories | < string > array |
| **from\_date**<br>_required_ | Start date in the form YYYY-MM-DD | string (date) |
| **include\_labels**<br>_optional_ | If set the individual labels data is returned under the components <br>**Default** : `true` | boolean |
| **to\_date**<br>_required_ | End date in the form YYYY-MM-DD | string (date) |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#responses-9 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/organization/#organization-get_tenant_usages-response-200) |

**Response 200**

| Name | Schema |
| --- | --- |
| **categories**<br>_optional_ | < string, [categories](https://clear.ml/docs/latest/docs/references/enterprise/organization/#organization-get_tenant_usages-post-categories) \> map |
| **currency**<br>_optional_ | string |
| **total\_cost**<br>_optional_ | number |

**categories**

| Name | Description | Schema |
| --- | --- | --- |
| **costs**<br>_optional_ | Category cost per date | < number > array |
| **count\_strategy**<br>_optional_ |  | enum (sum, max) |
| **dates**<br>_optional_ |  | < string (date) > array |
| **display\_name**<br>_optional_ | Display name | string |
| **free**<br>_optional_ | If set to Truethen no payments are defined for category labels | boolean |
| **labels**<br>_optional_ |  | < string, [labels](https://clear.ml/docs/latest/docs/references/enterprise/organization/#organization-get_tenant_usages-post-categories-labels) \> map |
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
| **pricing**<br>_optional_ |  | [pricing](https://clear.ml/docs/latest/docs/references/enterprise/organization/#organization-get_tenant_usages-post-categories-labels-pricing) |
| **total\_cost**<br>_optional_ | Total label cost for the chosen period | number |
| **total\_usage**<br>_optional_ | Total label usage for the chosen period | number |
| **usages**<br>_optional_ | Label usage per date | < number > array |

**pricing**

| Name | Schema |
| --- | --- |
| **price**<br>_optional_ | number |
| **units**<br>_optional_ | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#security-9 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /organization.get\_ui\_actions [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#post-organizationget_ui_actions "Direct link to POST /organization.get_ui_actions")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#description-10 "Direct link to Description")

Get custom UI Actions

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#parameters-10 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#responses-10 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/organization/#organization-get_ui_actions-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **objects**<br>_optional_ | Mapping of object type to list of custom UI actions | < string, < [organization.ui\_action](https://clear.ml/docs/latest/docs/references/enterprise/definitions#organizationui_action) \> array > map |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#security-10 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /organization.get\_usage\_configuration [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#post-organizationget_usage_configuration "Direct link to POST /organization.get_usage_configuration")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#description-11 "Direct link to Description")

Get the usage aggregator configuration for the calling tenant (the global

configuration plus the tenant's own additions)

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#parameters-11 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#responses-11 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/organization/#organization-get_usage_configuration-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **events**<br>_optional_ | Categories keyed by category name | < string, [events](https://clear.ml/docs/latest/docs/references/enterprise/organization/#organization-get_usage_configuration-post-events) \> map |
| **pricing**<br>_optional_ |  | [pricing](https://clear.ml/docs/latest/docs/references/enterprise/organization/#organization-get_usage_configuration-post-pricing) |

**events**

| Name | Description | Schema |
| --- | --- | --- |
| **count\_strategy**<br>_optional_ | The algorithm used for calculating total usage per day (sum - all usage reports <br>are summed, max - the max value is taken) | enum (sum, max) |
| **display\_name**<br>_optional_ |  | string |
| **labels**<br>_optional_ | Category labels keyed by label name | < string, [labels](https://clear.ml/docs/latest/docs/references/enterprise/organization/#organization-get_usage_configuration-post-events-labels) \> map |
| **read\_only**<br>_optional_ | If set the category originates from the global configuration and cannot be <br>edited by the tenant | boolean |
| **type**<br>_optional_ |  | enum (compute, storage, model\_tokens, users, service\_accounts) |
| **unit\_name**<br>_optional_ |  | string |

**labels**

| Name | Description | Schema |
| --- | --- | --- |
| **display\_name**<br>_optional_ |  | string |
| **enabled**<br>_optional_ | If set to Falsethe label data is neither collected nor returned | boolean |
| **pricing**<br>_optional_ |  | [pricing](https://clear.ml/docs/latest/docs/references/enterprise/organization/#organization-get_usage_configuration-post-events-labels-pricing) |
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

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#security-11 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /organization.prepare\_download\_for\_get\_all [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#post-organizationprepare_download_for_get_all "Direct link to POST /organization.prepare_download_for_get_all")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#description-12 "Direct link to Description")

Prepares download from get\_all\_ex parameters

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#parameters-12 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/organization/#organization-prepare_download_for_get_all-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **allow\_public**<br>_optional_ | Allow public entities to be returned in the results <br>**Default** : `true` | boolean |
| **entity\_type**<br>_required_ | The type of the entity to retrieve | enum (task, model, dataview) |
| **field\_mappings**<br>_required_ | The name and value mappings for the exported fields. The fields that are not in <br>the mappings will not be exported | < [organization.field\_mapping](https://clear.ml/docs/latest/docs/references/enterprise/definitions#organizationfield_mapping) \> array |
| **only\_fields**<br>_required_ | List of task field names (nesting is supported using '.', e.g. <br>execution.model\_labels). If provided, this list defines the query's projection <br>(only these fields will be returned for each result entry) | < string > array |
| **search\_hidden**<br>_optional_ | If set to 'true' then hidden entities are included in the search results <br>**Default** : `false` | boolean |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#responses-12 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/organization/#organization-prepare_download_for_get_all-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **prepare\_id**<br>_optional_ | Prepare ID (use when calling 'download\_for\_get\_all') | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#security-12 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /organization.update\_company\_logo [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#post-organizationupdate_company_logo "Direct link to POST /organization.update_company_logo")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#description-13 "Direct link to Description")

Update the logo of the user company

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#parameters-13 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/organization/#organization-update_company_logo-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **company**<br>_optional_ | The ID of the company to update. By default the user company is updated. Only <br>system users are allowed to change other companies names | string |
| **data**<br>_required_ | Logo data (max 100Kb) | string |
| **format**<br>_required_ | Logo data format | enum (base64, url) |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#responses-13 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/organization/#organization-update_company_logo-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **updated**<br>_optional_ | Number of companies updated (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#security-13 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | admin |

### POST /organization.update\_company\_name [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#post-organizationupdate_company_name "Direct link to POST /organization.update_company_name")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#description-14 "Direct link to Description")

Update the name of the user company

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#parameters-14 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/organization/#organization-update_company_name-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **company**<br>_optional_ | The ID of the company to update. By default the user company is updated. Only <br>system users are allowed to change other companies names | string |
| **new\_name**<br>_required_ | The new name for the company | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#responses-14 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/organization/#organization-update_company_name-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **updated**<br>_optional_ | Number of companies updated (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/organization/\#security-14 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | admin |

- [POST /organization.allow\_project\_workloads](https://clear.ml/docs/latest/docs/references/enterprise/organization/#post-organizationallow_project_workloads)
- [POST /organization.delete\_usage\_configuration](https://clear.ml/docs/latest/docs/references/enterprise/organization/#post-organizationdelete_usage_configuration)
- [POST /organization.download\_for\_get\_all](https://clear.ml/docs/latest/docs/references/enterprise/organization/#post-organizationdownload_for_get_all)
- [POST /organization.edit\_usage\_configuration](https://clear.ml/docs/latest/docs/references/enterprise/organization/#post-organizationedit_usage_configuration)
- [POST /organization.get\_entities\_count](https://clear.ml/docs/latest/docs/references/enterprise/organization/#post-organizationget_entities_count)
- [POST /organization.get\_project\_company](https://clear.ml/docs/latest/docs/references/enterprise/organization/#post-organizationget_project_company)
- [POST /organization.get\_project\_workloads](https://clear.ml/docs/latest/docs/references/enterprise/organization/#post-organizationget_project_workloads)
- [POST /organization.get\_services](https://clear.ml/docs/latest/docs/references/enterprise/organization/#post-organizationget_services)
- [POST /organization.get\_tags](https://clear.ml/docs/latest/docs/references/enterprise/organization/#post-organizationget_tags)
- [POST /organization.get\_tenant\_usages](https://clear.ml/docs/latest/docs/references/enterprise/organization/#post-organizationget_tenant_usages)
- [POST /organization.get\_ui\_actions](https://clear.ml/docs/latest/docs/references/enterprise/organization/#post-organizationget_ui_actions)
- [POST /organization.get\_usage\_configuration](https://clear.ml/docs/latest/docs/references/enterprise/organization/#post-organizationget_usage_configuration)
- [POST /organization.prepare\_download\_for\_get\_all](https://clear.ml/docs/latest/docs/references/enterprise/organization/#post-organizationprepare_download_for_get_all)
- [POST /organization.update\_company\_logo](https://clear.ml/docs/latest/docs/references/enterprise/organization/#post-organizationupdate_company_logo)
- [POST /organization.update\_company\_name](https://clear.ml/docs/latest/docs/references/enterprise/organization/#post-organizationupdate_company_name)