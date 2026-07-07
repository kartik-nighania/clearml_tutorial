---
url: "https://clear.ml/docs/latest/docs/references/enterprise/permissions/"
title: "permissions | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/enterprise/permissions/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

### POST /permissions.add\_or\_update\_access\_rule [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#post-permissionsadd_or_update_access_rule "Direct link to POST /permissions.add_or_update_access_rule")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#description "Direct link to Description")

Edit existing entity access rule or add a new one

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#parameters "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/permissions/#permissions-add_or_update_access_rule-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **access\_permission**<br>_required_ | The access permission that this rule grants | [permissions.access\_permission\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions#permissionsaccess_permission_enum) |
| **description**<br>_required_ | The description of the rule | string |
| **entity\_id**<br>_optional_ | ID of the entity that this access rule gives access to. Shape depends on <br>entity\_type: - project/task/model/dataview/dataset/dataset\_version/queue/route: <br>the entity's Mongo doc id, or " _" for all entities of that type. For project_<br>_rules, null can also be passed for the top level entities access. - app_<br>_(DAG-19215): the `Application.app_id` string declared in the app's HOCON_<br>_template (NOT the Mongo doc \_id) — e.g. "vscode", "hpo-app". "_" grants all <br>apps. - app\_category (DAG-19215): the category string itself — e.g. "AI dev", <br>"deploy". The string is compared byte-for-byte against <br>`Application.info.category` at runtime; mismatched strings produce inert rules. <br>"\*" grants all categories. For app and app\_category, the entity\_id is NOT <br>enriched server-side on read (entity\_name / entity\_display\_name come back <br>null); render the raw entity\_id in the FE. | string |
| **entity\_type**<br>_required_ | The type of the entity that this access rule gives access to | [permissions.entity\_type\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions#permissionsentity_type_enum) |
| **groups**<br>_required_ | The list of the rule user groups | < string > array |
| **id**<br>_optional_ | Rule id. If specified and the rule with the id is found then it is updated. <br>Otherwise the new rule with this id is created | string |
| **name**<br>_required_ | The name of the rule | string |
| **users**<br>_required_ | The list of the rule users | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#responses "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/permissions/#permissions-add_or_update_access_rule-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_optional_ | The id of the created or edited access rule | string |
| **name**<br>_optional_ | The name of the rule | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#security "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /permissions.add\_or\_update\_user\_group [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#post-permissionsadd_or_update_user_group "Direct link to POST /permissions.add_or_update_user_group")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#description-1 "Direct link to Description")

Edit existing user group or add a new one

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#parameters-1 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/permissions/#permissions-add_or_update_user_group-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **description**<br>_optional_ | The description of the group | string |
| **id**<br>_optional_ | User group id. If specified and the group with the id is found then it is <br>updated. Otherwise the new group with this id is created | string |
| **name**<br>_optional_ | The name of the group | string |
| **users**<br>_optional_ | The list of the group users | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#responses-1 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/permissions/#permissions-add_or_update_user_group-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **assignable**<br>_optional_ | The assignable property of the group | boolean |
| **id**<br>_optional_ | The id of the created or edited security group | string |
| **name**<br>_optional_ | The name of the group | string |
| **system**<br>_optional_ | The system property of the group | boolean |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#security-1 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /permissions.check\_entity\_access [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#post-permissionscheck_entity_access "Direct link to POST /permissions.check_entity_access")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#description-2 "Direct link to Description")

Internal. Check whether the given entity has the requested access permission

for the calling user

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#parameters-2 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/permissions/#permissions-check_entity_access-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **access\_permission**<br>_optional_ | The access permission to check | [permissions.access\_permission\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions#permissionsaccess_permission_enum) |
| **entity\_id**<br>_optional_ | ID of the entity to check | string |
| **entity\_type**<br>_optional_ | The type of the entity | [permissions.entity\_type\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions#permissionsentity_type_enum) |
| **token**<br>_optional_ | Router token for verifying access. Should be a user token. | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#responses-2 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#security-2 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /permissions.delete\_access\_rules [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#post-permissionsdelete_access_rules "Direct link to POST /permissions.delete_access_rules")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#description-3 "Direct link to Description")

Delete entity access rules

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#parameters-3 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/permissions/#permissions-delete_access_rules-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **rules**<br>_required_ | IDs of the rules to delete | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#responses-3 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/permissions/#permissions-delete_access_rules-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **deleted**<br>_optional_ | The amount of deleted rules | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#security-3 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /permissions.delete\_user\_groups [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#post-permissionsdelete_user_groups "Direct link to POST /permissions.delete_user_groups")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#description-4 "Direct link to Description")

Delete user groups

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#parameters-4 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/permissions/#permissions-delete_user_groups-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **groups**<br>_required_ | IDs of the groups to delete | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#responses-4 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/permissions/#permissions-delete_user_groups-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **deleted**<br>_optional_ | The number of deleted groups | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#security-4 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /permissions.ensure\_default\_access\_rules [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#post-permissionsensure_default_access_rules "Direct link to POST /permissions.ensure_default_access_rules")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#description-5 "Direct link to Description")

Restore all the default access rules. For safety reasons works only if

permissions are disabled

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#parameters-5 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/permissions/#permissions-ensure_default_access_rules-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **groups**<br>_optional_ | If empty then access rules are restored for all the groups. Otherwise only for <br>the passed ones | < enum (admins, users) > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#responses-5 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/permissions/#permissions-ensure_default_access_rules-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **restored**<br>_optional_ | The amount of restored rules | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#security-5 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /permissions.get\_access\_rules [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#post-permissionsget_access_rules "Direct link to POST /permissions.get_access_rules")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#description-6 "Direct link to Description")

Get the list of entity access rules

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#parameters-6 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/permissions/#permissions-get_access_rules-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **rules**<br>_optional_ | IDs of the rules to retrieve. If not passed or empty then all the company <br>access rules are returned | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#responses-6 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/permissions/#permissions-get_access_rules-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **rules**<br>_optional_ | Access rules list | < [rules](https://clear.ml/docs/latest/docs/references/enterprise/permissions/#permissions-get_access_rules-post-rules) \> array |

**rules**

| Name | Description | Schema |
| --- | --- | --- |
| **access\_permission**<br>_optional_ | The access permission that this rule grants | [permissions.access\_permission\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions#permissionsaccess_permission_enum) |
| **autocreated**<br>_optional_ | If set to 'true' then the group should not be edited by end users | boolean |
| **description**<br>_optional_ | Access rule description | string |
| **entity\_display\_name**<br>_optional_ | Display name for the entity (if applicable) | string |
| **entity\_id**<br>_optional_ | ID of the entity that this access rule gives access to | string |
| **entity\_name**<br>_optional_ | The name of the entity. null if the entity not found | string |
| **entity\_type**<br>_optional_ | The type of the entity that this access rule gives access to | [permissions.entity\_type\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions#permissionsentity_type_enum) |
| **groups**<br>_optional_ | List of groups that this access rule grants permission | < [groups](https://clear.ml/docs/latest/docs/references/enterprise/permissions/#permissions-get_access_rules-post-rules-groups) \> array |
| **id**<br>_optional_ | Access rule id | string |
| **metadata**<br>_optional_ |  | object |
| **name**<br>_optional_ | Access rule name | string |
| **users**<br>_optional_ | List of users that this access rule grants permission | < [users](https://clear.ml/docs/latest/docs/references/enterprise/permissions/#permissions-get_access_rules-post-rules-users) \> array |

**groups**

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_optional_ | Group ID | string |
| **name**<br>_optional_ | Group name | string |

**users**

| Name | Description | Schema |
| --- | --- | --- |
| **email**<br>_optional_ | User email | string |
| **id**<br>_optional_ | User ID | string |
| **name**<br>_optional_ | User name | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#security-6 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /permissions.get\_company\_users [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#post-permissionsget_company_users "Direct link to POST /permissions.get_company_users")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#description-7 "Direct link to Description")

Get the list of users who either belong to the company or joined it

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#parameters-7 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#responses-7 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/permissions/#permissions-get_company_users-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **users**<br>_optional_ | The list of users | < [permissions.user](https://clear.ml/docs/latest/docs/references/enterprise/definitions#permissionsuser) \> array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#security-7 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /permissions.get\_entity\_access\_categories [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#post-permissionsget_entity_access_categories "Direct link to POST /permissions.get_entity_access_categories")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#description-8 "Direct link to Description")

Get the list of entity types and possible access categories for each entity

type

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#parameters-8 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#responses-8 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/permissions/#permissions-get_entity_access_categories-response-200) |

**Response 200**

| Name | Schema |
| --- | --- |
| **entity\_types**<br>_optional_ | < [entity\_types](https://clear.ml/docs/latest/docs/references/enterprise/permissions/#permissions-get_entity_access_categories-post-entity_types) \> array |

**entity\_types**

| Name | Description | Schema |
| --- | --- | --- |
| **categories**<br>_optional_ | The list of access categories for the given entity type | < string > array |
| **type**<br>_optional_ | Entity type | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#security-8 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /permissions.get\_user\_groups [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#post-permissionsget_user_groups "Direct link to POST /permissions.get_user_groups")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#description-9 "Direct link to Description")

Get the list of company user groups

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#parameters-9 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/permissions/#permissions-get_user_groups-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **groups**<br>_optional_ | IDs of the groups to retrieve. If not passed or empty then all the company user <br>groups are returned | < string > array |
| **include\_permissions**<br>_optional_ | If set the service permissions for the user group are returned <br>**Default** : `false` | boolean |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#responses-9 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/permissions/#permissions-get_user_groups-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **groups**<br>_optional_ | User groups list | < [groups](https://clear.ml/docs/latest/docs/references/enterprise/permissions/#permissions-get_user_groups-post-groups) \> array |

**groups**

| Name | Description | Schema |
| --- | --- | --- |
| **assignable**<br>_optional_ | Indicates whether users can be assigned to the group or removed from the group | boolean |
| **description**<br>_optional_ | User group description | string |
| **id**<br>_optional_ | User group id | string |
| **name**<br>_optional_ | User group name | string |
| **permissions**<br>_optional_ |  | < object > array |
| **system**<br>_optional_ | Indicates whether the group can be edited | boolean |
| **users**<br>_optional_ | List of users belonging to the group | < [users](https://clear.ml/docs/latest/docs/references/enterprise/permissions/#permissions-get_user_groups-post-groups-users) \> array |

**users**

| Name | Description | Schema |
| --- | --- | --- |
| **email**<br>_optional_ | User email | string |
| **id**<br>_optional_ | User ID | string |
| **name**<br>_optional_ | User name | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#security-9 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /permissions.restore\_default\_access\_rules [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#post-permissionsrestore_default_access_rules "Direct link to POST /permissions.restore_default_access_rules")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#description-10 "Direct link to Description")

Restore all the default access rules for default and admin security groups

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#parameters-10 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#responses-10 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/permissions/#permissions-restore_default_access_rules-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **restored**<br>_optional_ | The amount of restored rules | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/permissions/\#security-10 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

- [POST /permissions.add\_or\_update\_access\_rule](https://clear.ml/docs/latest/docs/references/enterprise/permissions/#post-permissionsadd_or_update_access_rule)
- [POST /permissions.add\_or\_update\_user\_group](https://clear.ml/docs/latest/docs/references/enterprise/permissions/#post-permissionsadd_or_update_user_group)
- [POST /permissions.check\_entity\_access](https://clear.ml/docs/latest/docs/references/enterprise/permissions/#post-permissionscheck_entity_access)
- [POST /permissions.delete\_access\_rules](https://clear.ml/docs/latest/docs/references/enterprise/permissions/#post-permissionsdelete_access_rules)
- [POST /permissions.delete\_user\_groups](https://clear.ml/docs/latest/docs/references/enterprise/permissions/#post-permissionsdelete_user_groups)
- [POST /permissions.ensure\_default\_access\_rules](https://clear.ml/docs/latest/docs/references/enterprise/permissions/#post-permissionsensure_default_access_rules)
- [POST /permissions.get\_access\_rules](https://clear.ml/docs/latest/docs/references/enterprise/permissions/#post-permissionsget_access_rules)
- [POST /permissions.get\_company\_users](https://clear.ml/docs/latest/docs/references/enterprise/permissions/#post-permissionsget_company_users)
- [POST /permissions.get\_entity\_access\_categories](https://clear.ml/docs/latest/docs/references/enterprise/permissions/#post-permissionsget_entity_access_categories)
- [POST /permissions.get\_user\_groups](https://clear.ml/docs/latest/docs/references/enterprise/permissions/#post-permissionsget_user_groups)
- [POST /permissions.restore\_default\_access\_rules](https://clear.ml/docs/latest/docs/references/enterprise/permissions/#post-permissionsrestore_default_access_rules)