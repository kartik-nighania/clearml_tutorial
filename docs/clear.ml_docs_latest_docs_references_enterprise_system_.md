---
url: "https://clear.ml/docs/latest/docs/references/enterprise/system/"
title: "system | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/enterprise/system/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

### POST /system.company\_info [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#post-systemcompany_info "Direct link to POST /system.company_info")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#description "Direct link to Description")

Get company information.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#parameters "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/system/#system-company_info-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **company**<br>_optional_ | Company ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#responses "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/system/#system-company_info-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **active**<br>_optional_ | Company status | boolean |
| **defaults**<br>_optional_ | Company defaults | object |
| **id**<br>_optional_ | Company ID | string |
| **name**<br>_optional_ | Company Name | string |
| **services**<br>_optional_ | Company services | < [system.service\_info](https://clear.ml/docs/latest/docs/references/enterprise/definitions#systemservice_info) \> array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#security "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | root,system |

### POST /system.copy\_tasks [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#post-systemcopy_tasks "Direct link to POST /system.copy_tasks")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#description-1 "Direct link to Description")

Internal. Copy tasks from one company to another. Tasks cannot have any

reference to a non-public object (i.e. Dataset versions, models etc.). Task

parents will not be copied, and any task with a parent will be copied to a task

without a parent.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#parameters-1 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/system/#system-copy_tasks-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **company**<br>_required_ | Target company ID for the newly copied tasks | string |
| **new\_project\_name**<br>_optional_ | New project name for the newly copied tasks. (required if `project` was not <br>provided) | string |
| **project**<br>_optional_ | Target project ID for the newly copied tasks (required if \`new\_project\_name\`\` <br>was not provided, must belong to the target company) | string |
| **tasks**<br>_required_ | List of task IDs | < string > array |
| **user**<br>_required_ | Target user ID for the newly copied tasks (must belong to the target company) | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#responses-1 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/system/#system-copy_tasks-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **ids**<br>_optional_ | List of newly-created task IDs | < string > array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#security-1 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | root,system |

### POST /system.create\_company [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#post-systemcreate_company "Direct link to POST /system.create_company")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#description-2 "Direct link to Description")

Internal. Create a new company in the system

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#parameters-2 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/system/#system-create_company-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **defaults**<br>_optional_ |  | [system.company\_defaults](https://clear.ml/docs/latest/docs/references/enterprise/definitions#systemcompany_defaults) |
| **name**<br>_required_ | Company name <br>**Minimum length** : `3` | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#responses-2 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/system/#system-create_company-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **app\_queues**<br>_optional_ | The list of created app queues | < [app\_queues](https://clear.ml/docs/latest/docs/references/enterprise/system/#system-create_company-post-app_queues) \> array |
| **id**<br>_optional_ | Newly created company ID | string |

**app\_queues**

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_optional_ | Queue ID | string |
| **name**<br>_optional_ | Queue name | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#security-2 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | root,system |

### POST /system.get\_companies [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#post-systemget_companies "Direct link to POST /system.get_companies")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#description-3 "Direct link to Description")

Internal. List companies in the system

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#parameters-3 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/system/#system-get_companies-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **custom\_data**<br>_optional_ | custom\_data | [custom\_data](https://clear.ml/docs/latest/docs/references/enterprise/system/#system-get_companies-post-custom_data) |
| **custom\_events**<br>_optional_ | If set then return only companies with custom events configuration defined <br>**Default** : `false` | boolean |
| **name**<br>_optional_ | Company name (case insensitive) | string |
| **name\_pattern**<br>_optional_ | Company name pattern (python regex format) | string |

**custom\_data**

| Name | Description | Schema |
| --- | --- | --- |
| **users**<br>_required_ | If set then company users count is returned | boolean |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#responses-3 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/system/#system-get_companies-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **companies**<br>_optional_ | Companies matching the query | < [system.basic\_company\_info](https://clear.ml/docs/latest/docs/references/enterprise/definitions#systembasic_company_info) \> array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#security-3 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | root,system |

### POST /system.get\_company\_app\_instance\_access [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#post-systemget_company_app_instance_access "Direct link to POST /system.get_company_app_instance_access")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#description-4 "Direct link to Description")

Internal. Get company application instance access

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#parameters-4 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/system/#system-get_company_app_instance_access-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **company**<br>_required_ | Company ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#responses-4 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/system/#system-get_company_app_instance_access-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **app\_instance\_access**<br>_optional_ | app\_instance\_access | [app\_instance\_access](https://clear.ml/docs/latest/docs/references/enterprise/system/#system-get_company_app_instance_access-post-app_instance_access) |

**app\_instance\_access**

| Name | Description | Schema |
| --- | --- | --- |
| **admin\_access\_all**<br>_optional_ | If set to 'true' then admin can access any app instances regardless of the <br>rules | boolean |
| **allowed**<br>_optional_ |  | enum (all, owner, groups) |
| **applications**<br>_optional_ |  | < string, [applications](https://clear.ml/docs/latest/docs/references/enterprise/system/#system-get_company_app_instance_access-post-app_instance_access-applications) \> map |
| **categories**<br>_optional_ |  | < string, [categories](https://clear.ml/docs/latest/docs/references/enterprise/system/#system-get_company_app_instance_access-post-app_instance_access-categories) \> map |

**applications**

| Name | Schema |
| --- | --- |
| **allowed**<br>_optional_ | enum (all, owner, groups) |

**categories**

| Name | Schema |
| --- | --- |
| **allowed**<br>_optional_ | enum (all, owner, groups) |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#security-4 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | root,system |

### POST /system.get\_company\_custom\_events\_config [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#post-systemget_company_custom_events_config "Direct link to POST /system.get_company_custom_events_config")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#description-5 "Direct link to Description")

Internal. Get company custom events configuration

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#parameters-5 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/system/#system-get_company_custom_events_config-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **company**<br>_required_ | Company ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#responses-5 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/system/#system-get_company_custom_events_config-response-200) |

**Response 200**

| Name | Schema |
| --- | --- |
| **fields**<br>_optional_ | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#security-5 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | root,system |

### POST /system.get\_dataset\_versions [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#post-systemget_dataset_versions "Direct link to POST /system.get_dataset_versions")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#description-6 "Direct link to Description")

Internal. Gets the version tree of a dataset. This call will return information

from all companies

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#parameters-6 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/system/#system-get_dataset_versions-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **dataset**<br>_optional_ | Get versions for this dataset ID | string |
| **id**<br>_optional_ | List of IDs to filter by | < string > array |
| **order\_by**<br>_optional_ | List of field names to order by. When search\_text is used, '@text\_score' can be <br>used as a field representing the text score of returned documents. Use '-' <br>prefix to specify descending order. Optional, recommended when using page | string |
| **page**<br>_optional_ | Page number, returns a specific page out of the result list of datasets. <br>**Minimum value** : `0` | integer |
| **page\_size**<br>_optional_ | Page size, specifies the number of results returned in each page (last page may <br>contain fewer results) <br>**Minimum value** : `1` | integer |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#responses-6 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/system/#system-get_dataset_versions-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **versions**<br>_optional_ | List of versions | < [system.version](https://clear.ml/docs/latest/docs/references/enterprise/definitions#systemversion) \> array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#security-6 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | root,system |

### POST /system.get\_datasets [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#post-systemget_datasets "Direct link to POST /system.get_datasets")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#description-7 "Direct link to Description")

Internal. Gets a list of datasets information matching a query. This call will

return information from all companies

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#parameters-7 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/system/#system-get_datasets-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_optional_ | List of IDs to filter by | < string > array |
| **order\_by**<br>_optional_ | List of field names to order by. When search\_text is used, '@text\_score' can be <br>used as a field representing the text score of returned documents. Use '-' <br>prefix to specify descending order. Optional, recommended when using page | < string > array |
| **page**<br>_optional_ | Page number, returns a specific page out of the result list of datasets. <br>**Minimum value** : `0` | integer |
| **page\_size**<br>_optional_ | Page size, specifies the number of results returned in each page (last page may <br>contain fewer results) <br>**Minimum value** : `1` | integer |
| **system\_tags**<br>_optional_ | System tags filter. Use '-' for exclusion (e.g. \['-archived'\] for all non- <br>hidden datasets) | < string > array |
| **tags**<br>_optional_ | User-defined tags filter. Use '-' for exclusion | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#responses-7 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/system/#system-get_datasets-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **datasets**<br>_optional_ | List of datasets | < [system.dataset](https://clear.ml/docs/latest/docs/references/enterprise/definitions#systemdataset) \> array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#security-7 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | root,system |

### POST /system.update\_company\_app\_instance\_access [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#post-systemupdate_company_app_instance_access "Direct link to POST /system.update_company_app_instance_access")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#description-8 "Direct link to Description")

Internal. Set company application instance access

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#parameters-8 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/system/#system-update_company_app_instance_access-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **app\_instance\_access**<br>_required_ | app\_instance\_access | [app\_instance\_access](https://clear.ml/docs/latest/docs/references/enterprise/system/#system-update_company_app_instance_access-post-app_instance_access) |
| **company**<br>_required_ | Company ID | string |

**app\_instance\_access**

| Name | Description | Schema |
| --- | --- | --- |
| **admin\_access\_all**<br>_optional_ | If set to 'true' then admin can access any app instances regardless of the <br>rules | boolean |
| **allowed**<br>_optional_ |  | enum (all, owner, groups) |
| **applications**<br>_optional_ |  | < string, [applications](https://clear.ml/docs/latest/docs/references/enterprise/system/#system-update_company_app_instance_access-post-app_instance_access-applications) \> map |
| **categories**<br>_optional_ |  | < string, [categories](https://clear.ml/docs/latest/docs/references/enterprise/system/#system-update_company_app_instance_access-post-app_instance_access-categories) \> map |

**applications**

| Name | Schema |
| --- | --- |
| **allowed**<br>_optional_ | enum (all, owner, groups) |

**categories**

| Name | Schema |
| --- | --- |
| **allowed**<br>_optional_ | enum (all, owner, groups) |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#responses-8 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#security-8 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | root,system |

### POST /system.update\_company\_custom\_events\_config [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#post-systemupdate_company_custom_events_config "Direct link to POST /system.update_company_custom_events_config")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#description-9 "Direct link to Description")

Internal. Set company custom events configuration

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#parameters-9 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/system/#system-update_company_custom_events_config-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **company**<br>_required_ | Company ID | string |
| **fields**<br>_required_ | fields | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#responses-9 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#security-9 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | root,system |

### POST /system.update\_company\_settings [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#post-systemupdate_company_settings "Direct link to POST /system.update_company_settings")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#description-10 "Direct link to Description")

Internal. Update company settings

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#parameters-10 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/system/#system-update_company_settings-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **admin\_access\_all\_apps**<br>_optional_ | If set to 'true' then company admin can access running application instances <br>from all the company users | boolean |
| **allow\_service\_user\_admins**<br>_optional_ | If set to 'true' then company service accounts can have an admin role | boolean |
| **allowed\_service\_users**<br>_optional_ | Maximum number of the company service accounts | integer |
| **allowed\_users**<br>_optional_ | Maximum number of the company users | integer |
| **app\_access\_by\_owners**<br>_optional_ | Application ids that their instances can be accessed only by the users who ran <br>them | < string > array |
| **company**<br>_required_ | Company ID | string |
| **cookie\_options**<br>_optional_ | Cookies parameters overrides | [cookie\_options](https://clear.ml/docs/latest/docs/references/enterprise/system/#system-update_company_settings-post-cookie_options) |
| **exclude\_features**<br>_optional_ | List of server features not allowed for the company | < [system.features\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions#systemfeatures_enum) \> array |
| **excluded\_application\_categories**<br>_optional_ | Categories of the applications that are not supported for the company | < string > array |
| **feature\_set**<br>_optional_ | The company feature set | enum (basic, advanced) |
| **features**<br>_optional_ | List of the company features | < [system.features\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions#systemfeatures_enum) \> array |
| **max\_running\_apps**<br>_optional_ | Maximum amount of simaltaniously running apps for the company | integer |
| **supported\_application\_categories**<br>_optional_ | Categeries of the applications supported for the company | < string > array |
| **supported\_application\_ids**<br>_optional_ | Ids of the applications supported for the company. | < string > array |

**cookie\_options**

| Name | Description | Schema |
| --- | --- | --- |
| **domain**<br>_optional_ | Cookie domain. Can be <pyhocon.config\_tree.NoneValue object at 0x7f6851f81700> | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#responses-10 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/system/#system-update_company_settings-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **updated**<br>_optional_ | Whether the company seetings were updated | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#security-10 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | root,system |

### POST /system.update\_company\_sso\_config [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#post-systemupdate_company_sso_config "Direct link to POST /system.update_company_sso_config")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#description-11 "Direct link to Description")

Internal. Save company sso configuration

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#parameters-11 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/system/#system-update_company_sso_config-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **company**<br>_required_ | Company ID | string |
| **sso**<br>_required_ | sso config | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#responses-11 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/system/\#security-11 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | root,system |

- [POST /system.company\_info](https://clear.ml/docs/latest/docs/references/enterprise/system/#post-systemcompany_info)
- [POST /system.copy\_tasks](https://clear.ml/docs/latest/docs/references/enterprise/system/#post-systemcopy_tasks)
- [POST /system.create\_company](https://clear.ml/docs/latest/docs/references/enterprise/system/#post-systemcreate_company)
- [POST /system.get\_companies](https://clear.ml/docs/latest/docs/references/enterprise/system/#post-systemget_companies)
- [POST /system.get\_company\_app\_instance\_access](https://clear.ml/docs/latest/docs/references/enterprise/system/#post-systemget_company_app_instance_access)
- [POST /system.get\_company\_custom\_events\_config](https://clear.ml/docs/latest/docs/references/enterprise/system/#post-systemget_company_custom_events_config)
- [POST /system.get\_dataset\_versions](https://clear.ml/docs/latest/docs/references/enterprise/system/#post-systemget_dataset_versions)
- [POST /system.get\_datasets](https://clear.ml/docs/latest/docs/references/enterprise/system/#post-systemget_datasets)
- [POST /system.update\_company\_app\_instance\_access](https://clear.ml/docs/latest/docs/references/enterprise/system/#post-systemupdate_company_app_instance_access)
- [POST /system.update\_company\_custom\_events\_config](https://clear.ml/docs/latest/docs/references/enterprise/system/#post-systemupdate_company_custom_events_config)
- [POST /system.update\_company\_settings](https://clear.ml/docs/latest/docs/references/enterprise/system/#post-systemupdate_company_settings)
- [POST /system.update\_company\_sso\_config](https://clear.ml/docs/latest/docs/references/enterprise/system/#post-systemupdate_company_sso_config)