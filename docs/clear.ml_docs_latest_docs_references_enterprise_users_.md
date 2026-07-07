---
url: "https://clear.ml/docs/latest/docs/references/enterprise/users/"
title: "users | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/enterprise/users/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

### POST /users.accept\_terms\_of\_use [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#post-usersaccept_terms_of_use "Direct link to POST /users.accept_terms_of_use")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#description "Direct link to Description")

Accept terms of use

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#parameters "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/users/#users-accept_terms_of_use-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **version**<br>_required_ | Terms of use version | number |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#responses "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/users/#users-accept_terms_of_use-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **fields**<br>_optional_ | Updated fields names and values | object |
| **updated**<br>_optional_ | Number of updated user objects (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#security "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /users.add\_or\_update\_vault [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#post-usersadd_or_update_vault "Direct link to POST /users.add_or_update_vault")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#description-1 "Direct link to Description")

Add a new vault document or update an existing vault document. Note that a non-

admin user can only add or edit user-scope vault documents

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#parameters-1 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/users/#users-add_or_update_vault-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **group**<br>_optional_ | Group ID in case `group` scope was used in the vault | string |
| **user**<br>_optional_ | User ID in case `user` scope was used in the vault, used instead of the calling <br>user. Available only for admin users | string |
| **vault**<br>_required_ | Vault document data. If the vault ID field is set, an existing vault document <br>will be updated, otherwise a new vault document will be created | [users.vault](https://clear.ml/docs/latest/docs/references/enterprise/definitions#usersvault) |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#responses-1 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/users/#users-add_or_update_vault-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **vault**<br>_optional_ | Added/updated vault ID | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#security-1 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /users.create [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#post-userscreate "Direct link to POST /users.create")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#description-2 "Direct link to Description")

Internal. Create a new user object. Reserved for internal use.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#parameters-2 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/users/#users-create-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **additional\_info**<br>_optional_ | User additional info | object |
| **avatar**<br>_optional_ | Avatar URL | string |
| **company**<br>_required_ | Company ID | string |
| **family\_name**<br>_optional_ | Family name | string |
| **given\_name**<br>_optional_ | Given name | string |
| **id**<br>_required_ | User ID | string |
| **name**<br>_required_ | Full name | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#responses-2 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#security-2 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root |

### POST /users.delete [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#post-usersdelete "Direct link to POST /users.delete")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#description-3 "Direct link to Description")

Internal. Delete a user

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#parameters-3 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/users/#users-delete-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **user**<br>_required_ | ID of user to delete | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#responses-3 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#security-3 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root |

### POST /users.delete\_vaults [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#post-usersdelete_vaults "Direct link to POST /users.delete_vaults")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#description-4 "Direct link to Description")

Delete the specified vault documents. Note that a non-admin user can only

delete user-scope vault documents

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#parameters-4 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/users/#users-delete_vaults-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **vaults**<br>_optional_ | A list of vault documents IDs | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#responses-4 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/users/#users-delete_vaults-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **deleted**<br>_optional_ | Number of vault documents deleted | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#security-4 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /users.get\_all [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#post-usersget_all "Direct link to POST /users.get_all")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#description-5 "Direct link to Description")

Internal. Get all user objects

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#parameters-5 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/users/#users-get_all-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_optional_ | List of user IDs used to filter results | < string > array |
| **include\_auth**<br>_optional_ | Include user auth info (email, created, role, providers and sec\_groups) in <br>results. Only available to admin users. <br>**Default** : `false` | boolean |
| **include\_providers\_info**<br>_optional_ | If set then user info stored for each provider is returned. Works together with <br>'include\_auth' parameter <br>**Default** : `false` | boolean |
| **name**<br>_optional_ | Get only users whose name matches this pattern (python regular expression <br>syntax) | string |
| **only\_fields**<br>_optional_ | List of user field names (if applicable, nesting is supported using '.'). If <br>provided, this list defines the query's projection (only these fields will be <br>returned for each result entry) | < string > array |
| **order\_by**<br>_optional_ | List of field names to order by. Use '-' prefix to specify descending order. <br>Optional, recommended when using page | < string > array |
| **page**<br>_optional_ | Page number, returns a specific page out of the resulting list of users <br>**Minimum value** : `0` | integer |
| **page\_size**<br>_optional_ | Page size, specifies the number of results returned in each page (last page may <br>contain fewer results) <br>**Minimum value** : `1` | integer |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#responses-5 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/users/#users-get_all-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **users**<br>_optional_ | User list | < [users.user](https://clear.ml/docs/latest/docs/references/enterprise/definitions#usersuser) \> array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#security-5 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /users.get\_all\_ex [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#post-usersget_all_ex "Direct link to POST /users.get_all_ex")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#description-6 "Direct link to Description")

Internal. Get all user objects

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#parameters-6 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/users/#users-get_all_ex-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **active\_in\_projects**<br>_optional_ | List of project IDs. If provided, return only users that were active in these <br>projects. If empty list is provided, return users that were active in any <br>project | < string > array |
| **id**<br>_optional_ | List of user IDs used to filter results | < string > array |
| **include\_activity**<br>_optional_ | Return user activity. Works together with 'include\_auth' parameter <br>**Default** : `false` | boolean |
| **include\_auth**<br>_optional_ | Include user auth info (email, created, role, providers and sec\_groups) in <br>results. Only available to admin users. <br>**Default** : `false` | boolean |
| **name**<br>_optional_ | Get only users whose name matches this pattern (python regular expression <br>syntax) | string |
| **only\_fields**<br>_optional_ | List of user field names (if applicable, nesting is supported using '.'). If <br>provided, this list defines the query's projection (only these fields will be <br>returned for each result entry) | < string > array |
| **order\_by**<br>_optional_ | List of field names to order by. Use '-' prefix to specify descending order. <br>Optional, recommended when using page | < string > array |
| **page**<br>_optional_ | Page number, returns a specific page out of the resulting list of users <br>**Minimum value** : `0` | integer |
| **page\_size**<br>_optional_ | Page size, specifies the number of results returned in each page (last page may <br>contain fewer results) <br>**Minimum value** : `1` | integer |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#responses-6 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/users/#users-get_all_ex-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **users**<br>_optional_ | User list | < [users.user](https://clear.ml/docs/latest/docs/references/enterprise/definitions#usersuser) \> array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#security-6 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /users.get\_by\_id [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#post-usersget_by_id "Direct link to POST /users.get_by_id")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#description-7 "Direct link to Description")

Gets user information

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#parameters-7 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/users/#users-get_by_id-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **user**<br>_required_ | User ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#responses-7 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/users/#users-get_by_id-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **user**<br>_optional_ | User info | [users.user](https://clear.ml/docs/latest/docs/references/enterprise/definitions#usersuser) |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#security-7 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /users.get\_current\_user [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#post-usersget_current_user "Direct link to POST /users.get_current_user")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#description-8 "Direct link to Description")

Gets current user information, based on the authenticated user making the call.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#parameters-8 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/users/#users-get_current_user-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **get\_supported\_features**<br>_optional_ | If set to 'true' then return the features supported for this user <br>**Default** : `false` | boolean |
| **return\_inactive\_companies**<br>_optional_ | If set to 'true' then deleted companies are also returned <br>**Default** : `false` | boolean |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#responses-8 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/users/#users-get_current_user-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **getting\_started**<br>_optional_ | Getting stated info | object |
| **sec\_groups**<br>_optional_ |  | < [sec\_groups](https://clear.ml/docs/latest/docs/references/enterprise/users/#users-get_current_user-post-sec_groups) \> array |
| **settings**<br>_optional_ |  | [settings](https://clear.ml/docs/latest/docs/references/enterprise/users/#users-get_current_user-post-settings) |
| **supported\_features**<br>_optional_ | The list of the features | < [users.features\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions#usersfeatures_enum) \> array |
| **terms\_of\_use**<br>_optional_ | Terms of use information | [terms\_of\_use](https://clear.ml/docs/latest/docs/references/enterprise/users/#users-get_current_user-post-terms_of_use) |
| **trial\_features**<br>_optional_ |  | < [trial\_features](https://clear.ml/docs/latest/docs/references/enterprise/users/#users-get_current_user-post-trial_features) \> array |
| **user**<br>_optional_ | User info | [users.get\_current\_user\_response\_user\_object](https://clear.ml/docs/latest/docs/references/enterprise/definitions#usersget_current_user_response_user_object) |

**sec\_groups**

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_optional_ | Security group ID | string |
| **name**<br>_optional_ | Security group name | string |

**settings**

| Name | Description | Schema |
| --- | --- | --- |
| **max\_download\_items**<br>_optional_ | The maximum items downloaded for this user in csv file downloads | string |

**terms\_of\_use**

| Name | Description | Schema |
| --- | --- | --- |
| **accept\_required**<br>_optional_ | User is required to accept new terms of use (terms of use were never accepted <br>or accepted version has been deprecated) | boolean |
| **latest**<br>_optional_ | Latest terms of use. Returned only in case accept is required | [users.terms\_of\_use](https://clear.ml/docs/latest/docs/references/enterprise/definitions#usersterms_of_use) |

**trial\_features**

| Name | Schema |
| --- | --- |
| **name**<br>_optional_ | enum (user\_management, user\_management\_advanced, permissions, applications, experiments, queues, queue\_management, data\_management, config\_vault, app\_management, pipelines, reports, show\_dashboard, show\_model\_view, show\_projects, resource\_dashboard, sso\_management, service\_users, resource\_policy, show\_datasets, show\_orchestration, model\_serving, show\_app\_gateways, project\_workloads, tenant\_usages) |
| **status**<br>_optional_ | enum (ongoing, ended) |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#security-8 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /users.get\_organization\_vaults [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#post-usersget_organization_vaults "Direct link to POST /users.get_organization_vaults")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#description-9 "Direct link to Description")

Internal. Get all vault documents from organization groups

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#parameters-9 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/users/#users-get_organization_vaults-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **enabled**<br>_optional_ | If true, returns only enabled vault documents <br>**Default** : `false` | boolean |
| **preview\_data**<br>_optional_ | Return data with hidden leaf strings. Supported formats 'json', 'yaml', 'hocon' <br>**Default** : `false` | boolean |
| **types**<br>_optional_ | Filter by vault type | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#responses-9 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/users/#users-get_organization_vaults-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **vaults**<br>_optional_ | List of user-viewable vault documents | < [users.vault\_data](https://clear.ml/docs/latest/docs/references/enterprise/definitions#usersvault_data) \> array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#security-9 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /users.get\_preferences [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#post-usersget_preferences "Direct link to POST /users.get_preferences")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#description-10 "Direct link to Description")

Get user preferences

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#parameters-10 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#responses-10 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/users/#users-get_preferences-response-200) |

**Response 200**

| Name | Schema |
| --- | --- |
| **preferences**<br>_optional_ | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#security-10 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /users.get\_role\_options [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#post-usersget_role_options "Direct link to POST /users.get_role_options")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#description-11 "Direct link to Description")

Internal. List assignable user roles and their display names

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#parameters-11 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#responses-11 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/users/#users-get_role_options-response-200) |

**Response 200**

| Name | Schema |
| --- | --- |
| **roles**<br>_optional_ | < [roles](https://clear.ml/docs/latest/docs/references/enterprise/users/#users-get_role_options-post-roles) \> array |

**roles**

| Name | Description | Schema |
| --- | --- | --- |
| **display\_name**<br>_optional_ | Human-readable role name for UI display | string |
| **role**<br>_optional_ | Role identifier | [users.assignable\_role](https://clear.ml/docs/latest/docs/references/enterprise/definitions#usersassignable_role) |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#security-11 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /users.get\_service\_users [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#post-usersget_service_users "Direct link to POST /users.get_service_users")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#description-12 "Direct link to Description")

Internal. Get service users

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#parameters-12 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#responses-12 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/users/#users-get_service_users-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **allow\_admins**<br>_optional_ | Whether service users can be set as Admins | boolean |
| **allowed\_service\_users**<br>_optional_ | Maximum allowed service users in the company | integer |
| **default\_expiration\_sec**<br>_optional_ | Default credentials expiration in seconds | integer |
| **max\_expiration\_sec**<br>_optional_ | Maximum credentials expiration in seconds for non-admin users | integer |
| **users**<br>_optional_ | List of users | < [users](https://clear.ml/docs/latest/docs/references/enterprise/users/#users-get_service_users-post-users) \> array |

**users**

| Name | Description | Schema |
| --- | --- | --- |
| **allow\_running\_as\_owner**<br>_optional_ |  | boolean |
| **credentials**<br>_optional_ | Number of credentials | integer |
| **id**<br>_optional_ | User ID | string |
| **last\_active\_time**<br>_optional_ | The last time when the user logged in | string (date-time) |
| **name**<br>_optional_ | User Name | string |
| **role**<br>_optional_ | User Role | [users.role](https://clear.ml/docs/latest/docs/references/enterprise/definitions#usersrole) |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#security-12 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /users.get\_terms\_of\_use [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#post-usersget_terms_of_use "Direct link to POST /users.get_terms_of_use")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#description-13 "Direct link to Description")

Get terms of use information

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#parameters-13 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/users/#users-get_terms_of_use-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **version**<br>_optional_ | Terms of use version | number |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#responses-13 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/users/#users-get_terms_of_use-response-200) |

**Response 200**

| Name | Schema |
| --- | --- |
| **terms\_of\_use**<br>_optional_ | [users.terms\_of\_use](https://clear.ml/docs/latest/docs/references/enterprise/definitions#usersterms_of_use) |

### POST /users.get\_vault\_operations\_log [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#post-usersget_vault_operations_log "Direct link to POST /users.get_vault_operations_log")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#description-14 "Direct link to Description")

Internal. Get the operations log for vaults. If no vault is specified, returns

logs for all vaults

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#parameters-14 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/users/#users-get_vault_operations_log-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **from\_timestamp**<br>_optional_ | Return logs created at or after this timestamp (ISO 8601 format) | string (date-time) |
| **group**<br>_optional_ | Group adjacent log records with the same operation. Turned on by default. Pass <br>'null' in order to cancel | [group](https://clear.ml/docs/latest/docs/references/enterprise/users/#users-get_vault_operations_log-post-group) |
| **operations**<br>_optional_ | Filter by operation types (e.g. create, edit, delete, activate, deactivate) | < string > array |
| **order**<br>_optional_ | The time sorting <br>**Default** : `"desc"` | enum (asc, desc) |
| **page**<br>_optional_ | The page to retrieve | integer |
| **page\_size**<br>_optional_ | The amount of records to retrieve | integer |
| **scope**<br>_optional_ | Filter by vault scope (e.g. organization, group, service\_account, user). <br>Defaults to organization and group | < string > array |
| **to\_timestamp**<br>_optional_ | Return logs created at or before this timestamp (ISO 8601 format) | string (date-time) |
| **users**<br>_optional_ | Filter by user IDs | < string > array |
| **vaults**<br>_optional_ | Vault IDs to filter by. If not specified, returns logs for all vaults | < string > array |

**group**

| Name | Description | Schema |
| --- | --- | --- |
| **index**<br>_optional_ | Which element of the group to return. 0 - first, -1 - last | integer |
| **order**<br>_optional_ | Sorting inside the group <br>**Default** : `"asc"` | enum (asc, desc) |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#responses-14 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/users/#users-get_vault_operations_log-response-200) |

**Response 200**

| Name | Schema |
| --- | --- |
| **operations**<br>_optional_ | < [operations](https://clear.ml/docs/latest/docs/references/enterprise/users/#users-get_vault_operations_log-post-operations) \> array |

**operations**

| Name | Description | Schema |
| --- | --- | --- |
| **created**<br>_optional_ | Log record creation time | string (date-time) |
| **ip**<br>_optional_ | The calling client IP | string |
| **operation**<br>_optional_ | The operation that was performed on the vault | string |
| **originator**<br>_optional_ | The calling client type | string |
| **originator\_version**<br>_optional_ | The calling client version | string |
| **reason**<br>_optional_ | The reason for the vault operation | string |
| **scope**<br>_optional_ | The scope of the vault (user, service\_account, group, organization) | string |
| **user**<br>_optional_ | The user who performed the operation | [user](https://clear.ml/docs/latest/docs/references/enterprise/users/#users-get_vault_operations_log-post-operations-user) |
| **vault\_description**<br>_optional_ | The description of the vault this operation was performed on | string |

**user**

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_optional_ | User ID | string |
| **name**<br>_optional_ | User display name | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#security-13 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /users.get\_vault\_operations\_log\_filters [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#post-usersget_vault_operations_log_filters "Direct link to POST /users.get_vault_operations_log_filters")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#description-15 "Direct link to Description")

Internal. Get available filter options for the vault operations log

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#parameters-15 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#responses-15 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/users/#users-get_vault_operations_log_filters-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **operations**<br>_optional_ | Distinct operation types found in the log | < string > array |
| **users**<br>_optional_ | Users who performed vault operations | < [users](https://clear.ml/docs/latest/docs/references/enterprise/users/#users-get_vault_operations_log_filters-post-users) \> array |
| **vaults**<br>_optional_ | Available vaults with their descriptions | < [vaults](https://clear.ml/docs/latest/docs/references/enterprise/users/#users-get_vault_operations_log_filters-post-vaults) \> array |

**users**

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_optional_ | User ID | string |
| **name**<br>_optional_ | User display name | string |

**vaults**

| Name | Description | Schema |
| --- | --- | --- |
| **description**<br>_optional_ | Vault description | string |
| **id**<br>_optional_ | Vault ID | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#security-14 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /users.get\_vaults [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#post-usersget_vaults "Direct link to POST /users.get_vaults")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#description-16 "Direct link to Description")

Get all vault documents viewable by the user

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#parameters-16 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/users/#users-get_vaults-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **enabled**<br>_optional_ | If true, returns only enabled vault documents <br>**Default** : `false` | boolean |
| **preview\_data**<br>_optional_ | Return data with hidden leaf strings. Supported formats 'json', 'yaml', 'hocon' <br>**Default** : `false` | boolean |
| **types**<br>_optional_ | Filter by vault type | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#responses-16 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/users/#users-get_vaults-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **vaults**<br>_optional_ | List of user-viewable vault documents | < [users.vault\_data](https://clear.ml/docs/latest/docs/references/enterprise/definitions#usersvault_data) \> array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#security-15 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /users.get\_whitelist [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#post-usersget_whitelist "Direct link to POST /users.get_whitelist")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#description-17 "Direct link to Description")

Internal. Get whitelist entries (optionally filtered). Reserved for internal

use.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#parameters-17 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/users/#users-get_whitelist-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **domain**<br>_optional_ | Email domain. If provided, only whitelist entries with this specific domain <br>will be returned <br>NOTE: cannot be used in conjunction with email | string (hostname) |
| **email**<br>_optional_ | Email address. If provided, only whitelist entries which contain this email or <br>whose domain matches this email's domain will be returned <br>NOTE: cannot be used in conjunction with domain | string (email) |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#responses-17 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/users/#users-get_whitelist-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **entries**<br>_optional_ | List of whitelist entries | < [users.login\_white\_list\_v1\_5](https://clear.ml/docs/latest/docs/references/enterprise/definitions#userslogin_white_list_v1_5) \> array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#security-16 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root |

### POST /users.set\_admin [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#post-usersset_admin "Direct link to POST /users.set_admin")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#description-18 "Direct link to Description")

Internal. DEPRECATED: use 'users.set\_role' instead. Toggle a user between the

admin and regular-user roles.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#parameters-18 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/users/#users-set_admin-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **admin**<br>_optional_ | Make the user admin if True. Otherwise regular user <br>**Default** : `true` | boolean |
| **user**<br>_optional_ | User ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#responses-18 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/users/#users-set_admin-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **updated**<br>_optional_ | Number of users updated (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#security-17 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /users.set\_preferences [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#post-usersset_preferences "Direct link to POST /users.set_preferences")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#description-19 "Direct link to Description")

Set user preferences

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#parameters-19 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/users/#users-set_preferences-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **preferences**<br>_required_ | Updates to user preferences. A mapping from keys in dot notation to values. For <br>example, `{"a.b": 0}` will set the key "b" in object "a" to 0. | object |
| **return\_updated**<br>_optional_ | If set to 'true' and update was succcessful then return updated preferences <br>**Default** : `true` | boolean |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#responses-19 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/users/#users-set_preferences-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **fields**<br>_optional_ | If the preferences were updated successfully then return the updated <br>preferences | object |
| **updated**<br>_optional_ | Number of updated user objects (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#security-18 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /users.set\_role [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#post-usersset_role "Direct link to POST /users.set_role")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#description-20 "Direct link to Description")

Internal. Set a user's role within the company

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#parameters-20 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/users/#users-set_role-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **role**<br>_required_ | Target role for the user | [users.assignable\_role](https://clear.ml/docs/latest/docs/references/enterprise/definitions#usersassignable_role) |
| **user**<br>_required_ | User ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#responses-20 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/users/#users-set_role-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **updated**<br>_optional_ | Number of users updated (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#security-19 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /users.update [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#post-usersupdate "Direct link to POST /users.update")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#description-21 "Direct link to Description")

Update a user object

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#parameters-21 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/users/#users-update-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **avatar**<br>_optional_ | Avatar URL | string |
| **family\_name**<br>_optional_ | Family name | string |
| **given\_name**<br>_optional_ | Given name | string |
| **name**<br>_optional_ | Full name | string |
| **user**<br>_required_ | User ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#responses-21 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/users/#users-update-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **fields**<br>_optional_ | Updated fields names and values | object |
| **updated**<br>_optional_ | Number of updated user objects (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#security-20 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /users.update\_service\_user [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#post-usersupdate_service_user "Direct link to POST /users.update_service_user")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#description-22 "Direct link to Description")

Internal. Updates an existing service user

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#parameters-22 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/users/#users-update_service_user-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **allow\_running\_as\_owner**<br>_optional_ | Whether the service user can impersonate as another user | boolean |
| **name**<br>_optional_ | User name (makes the auth entry more readable) | string |
| **user**<br>_required_ | Service User ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#responses-22 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/users/#users-update_service_user-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **updated**<br>_optional_ | Number of updated service user objects (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/users/\#security-21 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

- [POST /users.accept\_terms\_of\_use](https://clear.ml/docs/latest/docs/references/enterprise/users/#post-usersaccept_terms_of_use)
- [POST /users.add\_or\_update\_vault](https://clear.ml/docs/latest/docs/references/enterprise/users/#post-usersadd_or_update_vault)
- [POST /users.create](https://clear.ml/docs/latest/docs/references/enterprise/users/#post-userscreate)
- [POST /users.delete](https://clear.ml/docs/latest/docs/references/enterprise/users/#post-usersdelete)
- [POST /users.delete\_vaults](https://clear.ml/docs/latest/docs/references/enterprise/users/#post-usersdelete_vaults)
- [POST /users.get\_all](https://clear.ml/docs/latest/docs/references/enterprise/users/#post-usersget_all)
- [POST /users.get\_all\_ex](https://clear.ml/docs/latest/docs/references/enterprise/users/#post-usersget_all_ex)
- [POST /users.get\_by\_id](https://clear.ml/docs/latest/docs/references/enterprise/users/#post-usersget_by_id)
- [POST /users.get\_current\_user](https://clear.ml/docs/latest/docs/references/enterprise/users/#post-usersget_current_user)
- [POST /users.get\_organization\_vaults](https://clear.ml/docs/latest/docs/references/enterprise/users/#post-usersget_organization_vaults)
- [POST /users.get\_preferences](https://clear.ml/docs/latest/docs/references/enterprise/users/#post-usersget_preferences)
- [POST /users.get\_role\_options](https://clear.ml/docs/latest/docs/references/enterprise/users/#post-usersget_role_options)
- [POST /users.get\_service\_users](https://clear.ml/docs/latest/docs/references/enterprise/users/#post-usersget_service_users)
- [POST /users.get\_terms\_of\_use](https://clear.ml/docs/latest/docs/references/enterprise/users/#post-usersget_terms_of_use)
- [POST /users.get\_vault\_operations\_log](https://clear.ml/docs/latest/docs/references/enterprise/users/#post-usersget_vault_operations_log)
- [POST /users.get\_vault\_operations\_log\_filters](https://clear.ml/docs/latest/docs/references/enterprise/users/#post-usersget_vault_operations_log_filters)
- [POST /users.get\_vaults](https://clear.ml/docs/latest/docs/references/enterprise/users/#post-usersget_vaults)
- [POST /users.get\_whitelist](https://clear.ml/docs/latest/docs/references/enterprise/users/#post-usersget_whitelist)
- [POST /users.set\_admin](https://clear.ml/docs/latest/docs/references/enterprise/users/#post-usersset_admin)
- [POST /users.set\_preferences](https://clear.ml/docs/latest/docs/references/enterprise/users/#post-usersset_preferences)
- [POST /users.set\_role](https://clear.ml/docs/latest/docs/references/enterprise/users/#post-usersset_role)
- [POST /users.update](https://clear.ml/docs/latest/docs/references/enterprise/users/#post-usersupdate)
- [POST /users.update\_service\_user](https://clear.ml/docs/latest/docs/references/enterprise/users/#post-usersupdate_service_user)