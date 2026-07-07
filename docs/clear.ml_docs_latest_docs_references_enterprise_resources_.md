---
url: "https://clear.ml/docs/latest/docs/references/enterprise/resources/"
title: "resources | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/enterprise/resources/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

### POST /resources.check\_edit\_configuration [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#post-resourcescheck_edit_configuration "Direct link to POST /resources.check_edit_configuration")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#description "Direct link to Description")

Check whether the edited configuration that is not provisioned yet exists

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#parameters "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#responses "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/resources/#resources-check_edit_configuration-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **exists**<br>_optional_ | 'true' if edited configuration exists | boolean |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#security "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /resources.connect\_policy\_profile [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#post-resourcesconnect_policy_profile "Direct link to POST /resources.connect_policy_profile")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#description-1 "Direct link to Description")

Create queue that connects policy to profile

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#parameters-1 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/resources/#resources-connect_policy_profile-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **display\_name**<br>_optional_ | Display queue name | string |
| **policy**<br>_optional_ | Policy ID | string |
| **profile**<br>_optional_ | Profile ID | string |
| **queue\_name**<br>_optional_ | Queue name | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#responses-1 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/resources/#resources-connect_policy_profile-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_optional_ | Queue ID | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#security-1 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /resources.create\_policy [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#post-resourcescreate_policy "Direct link to POST /resources.create_policy")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#description-2 "Direct link to Description")

Create new resource policy

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#parameters-2 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/resources/#resources-create_policy-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **description**<br>_optional_ | Policy description | string |
| **limit**<br>_optional_ | Policy limit | number |
| **name**<br>_required_ | Policy name | string |
| **reservation**<br>_optional_ | Policy reservation | number |
| **user\_group**<br>_required_ | Policy security group | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#responses-2 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/resources/#resources-create_policy-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_optional_ | Created policy ID | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#security-2 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /resources.delete\_policy [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#post-resourcesdelete_policy "Direct link to POST /resources.delete_policy")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#description-3 "Direct link to Description")

Delete existing resource policy

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#parameters-3 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/resources/#resources-delete_policy-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_required_ | Policy ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#responses-3 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/resources/#resources-delete_policy-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **deleted**<br>_optional_ | The number of deleted policies | integer |
| **deleted\_queues**<br>_optional_ | The number of deleted policy queues | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#security-3 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /resources.disconnect\_policy\_profile [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#post-resourcesdisconnect_policy_profile "Direct link to POST /resources.disconnect_policy_profile")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#description-4 "Direct link to Description")

Create queue that connects policy to profile

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#parameters-4 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/resources/#resources-disconnect_policy_profile-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **queue**<br>_optional_ | Queue id | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#responses-4 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/resources/#resources-disconnect_policy_profile-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **deleted**<br>_optional_ | Number of deleted queues | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#security-4 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /resources.enable\_policy\_manager [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#post-resourcesenable_policy_manager "Direct link to POST /resources.enable_policy_manager")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#description-5 "Direct link to Description")

Enable or disable policy manager

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#parameters-5 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/resources/#resources-enable_policy_manager-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **enable**<br>_optional_ | Set to 'true' to enable policy manager. 'false' otherwise <br>**Default** : `true` | boolean |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#responses-5 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#security-5 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /resources.get\_policies [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#post-resourcesget_policies "Direct link to POST /resources.get_policies")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#description-6 "Direct link to Description")

Get resource policies

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#parameters-6 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#responses-6 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/resources/#resources-get_policies-response-200) |

**Response 200**

| Name | Schema |
| --- | --- |
| **policies**<br>_optional_ | < [policies](https://clear.ml/docs/latest/docs/references/enterprise/resources/#resources-get_policies-post-policies) \> array |

**policies**

| Name | Description | Schema |
| --- | --- | --- |
| **description**<br>_optional_ | Policy description | string |
| **id**<br>_optional_ | Policy ID | string |
| **limit**<br>_optional_ | Policy limit | number |
| **missing\_profile\_connections**<br>_optional_ | Set to Trueif the policy has no profile connections | boolean |
| **name**<br>_optional_ | Policy name | string |
| **reservation**<br>_optional_ | Policy reservation | number |
| **usage**<br>_optional_ | Current policy usage | number |
| **user\_group**<br>_optional_ | Policy security group ID | string |
| **user\_group\_name**<br>_optional_ | Policy security group name | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#security-6 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /resources.get\_policy\_data [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#post-resourcesget_policy_data "Direct link to POST /resources.get_policy_data")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#description-7 "Direct link to Description")

Get resource policy data

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#parameters-7 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/resources/#resources-get_policy_data-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_optional_ | Policy ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#responses-7 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/resources/#resources-get_policy_data-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **description**<br>_optional_ | Policy description | string |
| **id**<br>_optional_ | Policy ID | string |
| **limit**<br>_optional_ | Policy limit | number |
| **missing\_profile\_connections**<br>_optional_ | Set to Trueif the policy has no profile connections | boolean |
| **name**<br>_optional_ | Policy name | string |
| **profile\_links**<br>_optional_ |  | < [profile\_links](https://clear.ml/docs/latest/docs/references/enterprise/resources/#resources-get_policy_data-post-profile_links) \> array |
| **reservation**<br>_optional_ | Policy reservation | number |
| **tasks**<br>_optional_ |  | < [tasks](https://clear.ml/docs/latest/docs/references/enterprise/resources/#resources-get_policy_data-post-tasks) \> array |
| **usage**<br>_optional_ | Current policy usage | number |
| **user\_group**<br>_optional_ | Policy security group ID | string |
| **user\_group\_name**<br>_optional_ | Policy security group name | string |

**profile\_links**

| Name | Schema |
| --- | --- |
| **profile**<br>_optional_ | [profile](https://clear.ml/docs/latest/docs/references/enterprise/resources/#resources-get_policy_data-post-profile_links-profile) |
| **queue**<br>_optional_ | [queue](https://clear.ml/docs/latest/docs/references/enterprise/resources/#resources-get_policy_data-post-profile_links-queue) |

**profile**

| Name | Description | Schema |
| --- | --- | --- |
| **cost\_field**<br>_optional_ | Task field to take the cost from | string |
| **description**<br>_optional_ | Profile description | string |
| **id**<br>_required_ | Profile ID | string |
| **name**<br>_required_ | Profile name | string |
| **policy\_connections**<br>_optional_ | Array of the incoming queues | < [policy\_connections](https://clear.ml/docs/latest/docs/references/enterprise/resources/#resources-get_policy_data-post-profile_links-profile-policy_connections) \> array |
| **pool\_links**<br>_optional_ | Array of pool links | < [pool\_links](https://clear.ml/docs/latest/docs/references/enterprise/resources/#resources-get_policy_data-post-profile_links-profile-pool_links) \> array |
| **profile\_cost**<br>_optional_ | The cost of using this profile | number |
| **queued\_jobs**<br>_optional_ | The amount of jobs currently queued for this profile | integer |
| **running\_jobs**<br>_optional_ | The amount of jobs currently running with this profile | integer |

**policy\_connections**

| Name | Description | Schema |
| --- | --- | --- |
| **display\_name**<br>_optional_ | Resource policy connection display name | string |
| **id**<br>_required_ | Resource policy connection ID | string |
| **name**<br>_required_ | Resource policy connection name | string |
| **policy\_name**<br>_optional_ | Resource policy name | string |

**pool\_links**

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_required_ | Link ID | string |
| **name**<br>_required_ | Link name | string |
| **pool**<br>_required_ | Pool ID | string |
| **queue\_name**<br>_optional_ | Pool link queue name (if exists) | string |

**queue**

| Name | Description | Schema |
| --- | --- | --- |
| **display\_name**<br>_optional_ | Display Queue Name | string |
| **id**<br>_optional_ | Queue ID | string |
| **name**<br>_optional_ | Queue Name | string |

**tasks**

| Name | Description | Schema |
| --- | --- | --- |
| **cost**<br>_optional_ | Task cost | number |
| **id**<br>_optional_ | Task ID | string |
| **name**<br>_optional_ | Task Name | string |
| **project**<br>_optional_ |  | [project](https://clear.ml/docs/latest/docs/references/enterprise/resources/#resources-get_policy_data-post-tasks-project) |
| **started**<br>_optional_ | Task start time (UTC) | string (date-time) |
| **status**<br>_optional_ | Task status | [resources.task\_status\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions#resourcestask_status_enum) |
| **type**<br>_optional_ | Task type | [resources.task\_type\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions#resourcestask_type_enum) |
| **user**<br>_optional_ |  | [user](https://clear.ml/docs/latest/docs/references/enterprise/resources/#resources-get_policy_data-post-tasks-user) |

**project**

| Name | Schema |
| --- | --- |
| **id**<br>_optional_ | string |
| **name**<br>_optional_ | string |

**user**

| Name | Schema |
| --- | --- |
| **id**<br>_optional_ | string |
| **name**<br>_optional_ | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#security-7 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /resources.get\_resource\_configuration [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#post-resourcesget_resource_configuration "Direct link to POST /resources.get_resource_configuration")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#description-8 "Direct link to Description")

Gets resource configuration

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#parameters-8 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/resources/#resources-get_resource_configuration-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **edit**<br>_optional_ | If set to Truethen configuration for editing is returned. Otherwise currently <br>published configuration <br>**Default** : `true` | boolean |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#responses-8 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/resources/#resources-get_resource_configuration-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **configuration**<br>_optional_ | Resource configuration | [configuration](https://clear.ml/docs/latest/docs/references/enterprise/resources/#resources-get_resource_configuration-post-configuration) |
| **policy\_manager**<br>_optional_ | Policy manager properties returned only if called with edit: 'false' | [policy\_manager](https://clear.ml/docs/latest/docs/references/enterprise/resources/#resources-get_resource_configuration-post-policy_manager) |

**configuration**

| Name | Schema |
| --- | --- |
| **pools**<br>_optional_ | < [pools](https://clear.ml/docs/latest/docs/references/enterprise/resources/#resources-get_resource_configuration-post-configuration-pools) \> array |
| **profiles**<br>_optional_ | < [profiles](https://clear.ml/docs/latest/docs/references/enterprise/resources/#resources-get_resource_configuration-post-configuration-profiles) \> array |

**pools**

| Name | Description | Schema |
| --- | --- | --- |
| **description**<br>_optional_ | Pool description | string |
| **id**<br>_required_ | Pool ID | string |
| **links**<br>_optional_ | Links from resource profiles | < string > array |
| **name**<br>_required_ | Pool name | string |
| **resources**<br>_optional_ | The amount of resources | integer |
| **usage**<br>_optional_ | The current pool usage | integer |

**profiles**

| Name | Description | Schema |
| --- | --- | --- |
| **cost\_field**<br>_optional_ | Task field to take the cost from | string |
| **description**<br>_optional_ | Profile description | string |
| **id**<br>_required_ | Profile ID | string |
| **name**<br>_required_ | Profile name | string |
| **policy\_connections**<br>_optional_ | Array of the incoming queues | < [policy\_connections](https://clear.ml/docs/latest/docs/references/enterprise/resources/#resources-get_resource_configuration-post-configuration-profiles-policy_connections) \> array |
| **pool\_links**<br>_optional_ | Array of pool links | < [pool\_links](https://clear.ml/docs/latest/docs/references/enterprise/resources/#resources-get_resource_configuration-post-configuration-profiles-pool_links) \> array |
| **profile\_cost**<br>_optional_ | The cost of using this profile | number |
| **queued\_jobs**<br>_optional_ | The amount of jobs currently queued for this profile | integer |
| **running\_jobs**<br>_optional_ | The amount of jobs currently running with this profile | integer |

**policy\_connections**

| Name | Description | Schema |
| --- | --- | --- |
| **display\_name**<br>_optional_ | Resource policy connection display name | string |
| **id**<br>_required_ | Resource policy connection ID | string |
| **name**<br>_required_ | Resource policy connection name | string |
| **policy\_name**<br>_optional_ | Resource policy name | string |

**pool\_links**

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_required_ | Link ID | string |
| **name**<br>_required_ | Link name | string |
| **pool**<br>_required_ | Pool ID | string |
| **queue\_name**<br>_optional_ | Pool link queue name (if exists) | string |

**policy\_manager**

| Name | Description | Schema |
| --- | --- | --- |
| **enabled**<br>_optional_ | 'true' if enabled. 'false' otherwise | boolean |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#security-8 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /resources.get\_resource\_pools [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#post-resourcesget_resource_pools "Direct link to POST /resources.get_resource_pools")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#description-9 "Direct link to Description")

Gets resource pools

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#parameters-9 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#responses-9 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/resources/#resources-get_resource_pools-response-200) |

**Response 200**

| Name | Schema |
| --- | --- |
| **pools**<br>_optional_ | < [pools](https://clear.ml/docs/latest/docs/references/enterprise/resources/#resources-get_resource_pools-post-pools) \> array |

**pools**

| Name | Description | Schema |
| --- | --- | --- |
| **description**<br>_optional_ | Pool description | string |
| **id**<br>_required_ | Pool ID | string |
| **links**<br>_optional_ | Links from resource profiles | < string > array |
| **name**<br>_required_ | Pool name | string |
| **resources**<br>_optional_ | The amount of resources | integer |
| **updated**<br>_optional_ | The last update time for the pool | string (datetime) |
| **updated\_by**<br>_optional_ | The user who updated the pool last time | string (datetime) |
| **usage**<br>_optional_ | The current pool usage | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#security-9 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /resources.get\_resource\_profiles [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#post-resourcesget_resource_profiles "Direct link to POST /resources.get_resource_profiles")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#description-10 "Direct link to Description")

Gets resource profiles

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#parameters-10 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#responses-10 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/resources/#resources-get_resource_profiles-response-200) |

**Response 200**

| Name | Schema |
| --- | --- |
| **profiles**<br>_optional_ | < [profiles](https://clear.ml/docs/latest/docs/references/enterprise/resources/#resources-get_resource_profiles-post-profiles) \> array |

**profiles**

| Name | Description | Schema |
| --- | --- | --- |
| **cost\_field**<br>_optional_ | Task field to take the cost from | string |
| **description**<br>_optional_ | Profile description | string |
| **id**<br>_required_ | Profile ID | string |
| **name**<br>_required_ | Profile name | string |
| **policy\_connections**<br>_optional_ | Array of the incoming queues | < [policy\_connections](https://clear.ml/docs/latest/docs/references/enterprise/resources/#resources-get_resource_profiles-post-profiles-policy_connections) \> array |
| **pool\_links**<br>_optional_ | Array of pool links | < [pool\_links](https://clear.ml/docs/latest/docs/references/enterprise/resources/#resources-get_resource_profiles-post-profiles-pool_links) \> array |
| **profile\_cost**<br>_optional_ | The cost of using this profile | number |
| **queued\_jobs**<br>_optional_ | The amount of jobs currently queued for this profile | integer |
| **running\_jobs**<br>_optional_ | The amount of jobs currently running with this profile | integer |
| **updated**<br>_optional_ | The last update time for the profile | string (datetime) |
| **updated\_by**<br>_optional_ | The user who updated the profile last time | string (datetime) |

**policy\_connections**

| Name | Description | Schema |
| --- | --- | --- |
| **display\_name**<br>_optional_ | Resource policy connection display name | string |
| **id**<br>_required_ | Resource policy connection ID | string |
| **name**<br>_required_ | Resource policy connection name | string |
| **policy\_name**<br>_optional_ | Resource policy name | string |

**pool\_links**

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_required_ | Link ID | string |
| **name**<br>_required_ | Link name | string |
| **pool**<br>_required_ | Pool ID | string |
| **queue\_name**<br>_optional_ | Pool link queue name (if exists) | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#security-10 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /resources.move\_policy [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#post-resourcesmove_policy "Direct link to POST /resources.move_policy")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#description-11 "Direct link to Description")

Move policy to another user group

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#parameters-11 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/resources/#resources-move_policy-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_required_ | Resource Policy ID | string |
| **user\_group**<br>_required_ | Policy security group | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#responses-11 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/resources/#resources-move_policy-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **dequeued\_tasks**<br>_optional_ | The number of the tasks dequeued from policy queues | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#security-11 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /resources.publish\_resource\_configuration [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#post-resourcespublish_resource_configuration "Direct link to POST /resources.publish_resource_configuration")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#description-12 "Direct link to Description")

Sets resource configuration

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#parameters-12 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#responses-12 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/resources/#resources-publish_resource_configuration-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **created\_links**<br>_optional_ | The number of created links | integer |
| **created\_pools**<br>_optional_ | The number of created pools | integer |
| **created\_profiles**<br>_optional_ | The number of created profiles | integer |
| **deleted\_links**<br>_optional_ | The number of deleted links | integer |
| **deleted\_policy\_connections**<br>_optional_ | The number of deleted policy connections | integer |
| **deleted\_pools**<br>_optional_ | The number of deleted pools | integer |
| **deleted\_profiles**<br>_optional_ | The number of deleted profiles | integer |
| **updated\_links**<br>_optional_ | The number of updated links | integer |
| **updated\_pools**<br>_optional_ | The number of updated pools | integer |
| **updated\_profiles**<br>_optional_ | The number of updated profiles | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#security-12 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /resources.reset\_resource\_configuration [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#post-resourcesreset_resource_configuration "Direct link to POST /resources.reset_resource_configuration")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#description-13 "Direct link to Description")

Resets reset configuration

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#parameters-13 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#responses-13 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#security-13 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /resources.set\_resource\_configuration [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#post-resourcesset_resource_configuration "Direct link to POST /resources.set_resource_configuration")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#description-14 "Direct link to Description")

Sets resource configuration

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#parameters-14 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/resources/#resources-set_resource_configuration-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **pools**<br>_optional_ | pools | < [pools](https://clear.ml/docs/latest/docs/references/enterprise/resources/#resources-set_resource_configuration-post-pools) \> array |
| **profiles**<br>_optional_ | profiles | < [profiles](https://clear.ml/docs/latest/docs/references/enterprise/resources/#resources-set_resource_configuration-post-profiles) \> array |

**pools**

| Name | Description | Schema |
| --- | --- | --- |
| **description**<br>_optional_ | Pool description | string |
| **id**<br>_required_ | Pool ID | string |
| **links**<br>_optional_ | Links from resource profiles | < string > array |
| **name**<br>_required_ | Pool name | string |
| **resources**<br>_optional_ | The amount of resources | integer |

**profiles**

| Name | Description | Schema |
| --- | --- | --- |
| **cost\_field**<br>_optional_ | Task field to take the cost from | string |
| **description**<br>_optional_ | Profile description | string |
| **id**<br>_required_ | Profile ID | string |
| **name**<br>_required_ | Profile name | string |
| **policy\_connections**<br>_optional_ | Array of the incoming queues | < [policy\_connections](https://clear.ml/docs/latest/docs/references/enterprise/resources/#resources-set_resource_configuration-post-profiles-policy_connections) \> array |
| **pool\_links**<br>_optional_ | Array of pool links | < [pool\_links](https://clear.ml/docs/latest/docs/references/enterprise/resources/#resources-set_resource_configuration-post-profiles-pool_links) \> array |
| **profile\_cost**<br>_optional_ | The cost of using this profile | number |

**policy\_connections**

| Name | Description | Schema |
| --- | --- | --- |
| **display\_name**<br>_optional_ | Resource policy connection display name | string |
| **id**<br>_required_ | Resource policy connection ID | string |
| **name**<br>_required_ | Resource policy connection name | string |
| **policy\_name**<br>_optional_ | Resource policy name | string |

**pool\_links**

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_required_ | Link ID | string |
| **name**<br>_required_ | Link name | string |
| **pool**<br>_required_ | Pool ID | string |
| **queue\_name**<br>_optional_ | Pool link queue name (if exists) | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#responses-14 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#security-14 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /resources.test\_configuration\_publishing [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#post-resourcestest_configuration_publishing "Direct link to POST /resources.test_configuration_publishing")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#description-15 "Direct link to Description")

Returns data on the changes to be done when the current editing configuration

is published

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#parameters-15 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#responses-15 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/resources/#resources-test_configuration_publishing-response-200) |

**Response 200**

| Name | Schema |
| --- | --- |
| **affected\_policies**<br>_optional_ | < [affected\_policies](https://clear.ml/docs/latest/docs/references/enterprise/resources/#resources-test_configuration_publishing-post-affected_policies) \> array |
| **not\_linked\_profiles**<br>_optional_ | < [not\_linked\_profiles](https://clear.ml/docs/latest/docs/references/enterprise/resources/#resources-test_configuration_publishing-post-not_linked_profiles) \> array |

**affected\_policies**

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_optional_ | Policy ID | string |
| **name**<br>_optional_ | Policy name | string |
| **queues\_to\_delete**<br>_optional_ |  | < [queues\_to\_delete](https://clear.ml/docs/latest/docs/references/enterprise/resources/#resources-test_configuration_publishing-post-affected_policies-queues_to_delete) \> array |

**queues\_to\_delete**

| Name | Description | Schema |
| --- | --- | --- |
| **display\_name**<br>_optional_ | Policy queue display name | string |
| **id**<br>_optional_ | Policy queue ID | string |
| **name**<br>_optional_ | Policy queue name | string |
| **tasks**<br>_optional_ | The number of tasks to dequeue | integer |

**not\_linked\_profiles**

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_optional_ | Profile ID | string |
| **name**<br>_optional_ | Profile name | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#security-15 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /resources.update\_policy [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#post-resourcesupdate_policy "Direct link to POST /resources.update_policy")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#description-16 "Direct link to Description")

Update existing resource policy

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#parameters-16 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/resources/#resources-update_policy-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **description**<br>_optional_ | Policy description | string |
| **id**<br>_required_ | Policy ID | string |
| **limit**<br>_optional_ | Policy limit | number |
| **name**<br>_optional_ | Policy name | string |
| **reservation**<br>_optional_ | Policy reservation | number |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#responses-16 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/resources/#resources-update_policy-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **updated**<br>_optional_ | The number of updated policies | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#security-16 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /resources.validate\_move\_policy [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#post-resourcesvalidate_move_policy "Direct link to POST /resources.validate_move_policy")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#description-17 "Direct link to Description")

Move policy to another user group

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#parameters-17 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/resources/#resources-validate_move_policy-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_required_ | Resource Policy ID | string |
| **user\_group**<br>_required_ | Policy security group | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#responses-17 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/resources/#resources-validate_move_policy-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **tasks\_to\_dequeue**<br>_optional_ | The number of the tasks to be dequeued from policy queues | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/resources/\#security-17 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

- [POST /resources.check\_edit\_configuration](https://clear.ml/docs/latest/docs/references/enterprise/resources/#post-resourcescheck_edit_configuration)
- [POST /resources.connect\_policy\_profile](https://clear.ml/docs/latest/docs/references/enterprise/resources/#post-resourcesconnect_policy_profile)
- [POST /resources.create\_policy](https://clear.ml/docs/latest/docs/references/enterprise/resources/#post-resourcescreate_policy)
- [POST /resources.delete\_policy](https://clear.ml/docs/latest/docs/references/enterprise/resources/#post-resourcesdelete_policy)
- [POST /resources.disconnect\_policy\_profile](https://clear.ml/docs/latest/docs/references/enterprise/resources/#post-resourcesdisconnect_policy_profile)
- [POST /resources.enable\_policy\_manager](https://clear.ml/docs/latest/docs/references/enterprise/resources/#post-resourcesenable_policy_manager)
- [POST /resources.get\_policies](https://clear.ml/docs/latest/docs/references/enterprise/resources/#post-resourcesget_policies)
- [POST /resources.get\_policy\_data](https://clear.ml/docs/latest/docs/references/enterprise/resources/#post-resourcesget_policy_data)
- [POST /resources.get\_resource\_configuration](https://clear.ml/docs/latest/docs/references/enterprise/resources/#post-resourcesget_resource_configuration)
- [POST /resources.get\_resource\_pools](https://clear.ml/docs/latest/docs/references/enterprise/resources/#post-resourcesget_resource_pools)
- [POST /resources.get\_resource\_profiles](https://clear.ml/docs/latest/docs/references/enterprise/resources/#post-resourcesget_resource_profiles)
- [POST /resources.move\_policy](https://clear.ml/docs/latest/docs/references/enterprise/resources/#post-resourcesmove_policy)
- [POST /resources.publish\_resource\_configuration](https://clear.ml/docs/latest/docs/references/enterprise/resources/#post-resourcespublish_resource_configuration)
- [POST /resources.reset\_resource\_configuration](https://clear.ml/docs/latest/docs/references/enterprise/resources/#post-resourcesreset_resource_configuration)
- [POST /resources.set\_resource\_configuration](https://clear.ml/docs/latest/docs/references/enterprise/resources/#post-resourcesset_resource_configuration)
- [POST /resources.test\_configuration\_publishing](https://clear.ml/docs/latest/docs/references/enterprise/resources/#post-resourcestest_configuration_publishing)
- [POST /resources.update\_policy](https://clear.ml/docs/latest/docs/references/enterprise/resources/#post-resourcesupdate_policy)
- [POST /resources.validate\_move\_policy](https://clear.ml/docs/latest/docs/references/enterprise/resources/#post-resourcesvalidate_move_policy)