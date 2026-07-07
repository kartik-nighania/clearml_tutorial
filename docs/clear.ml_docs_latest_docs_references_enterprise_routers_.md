---
url: "https://clear.ml/docs/latest/docs/references/enterprise/routers/"
title: "routers | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/enterprise/routers/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

### POST /routers.add\_or\_update\_route [​](https://clear.ml/docs/latest/docs/references/enterprise/routers/\#post-routersadd_or_update_route "Direct link to POST /routers.add_or_update_route")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/routers/\#description "Direct link to Description")

Internal. Add a new route or update an existing one. If route ID is passed then

the route should exist

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/routers/\#parameters "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/routers/#routers-add_or_update_route-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **auth\_enabled**<br>_optional_ | Enable auth if 'true' <br>**Default** : `true` | boolean |
| **enabled**<br>_optional_ | If set to 'true' then the router is marked as enabled. Otherwise disabled <br>**Default** : `true` | boolean |
| **id**<br>_optional_ | Route ID | string |
| **load\_balancer**<br>_optional_ | load\_balancer | [load\_balancer](https://clear.ml/docs/latest/docs/references/enterprise/routers/#routers-add_or_update_route-post-load_balancer) |
| **name**<br>_required_ | Route Name | string |
| **path**<br>_optional_ | Route Path. Required for type 'path' | string |
| **subdomain**<br>_optional_ | Route Subdomain. Required for type 'subdomain' | string |
| **type**<br>_required_ | Route type | enum (path, subdomain) |
| **user\_groups**<br>_optional_ | Users from those groups are allowed to access the route | < string > array |

**load\_balancer**

| Name | Description | Schema |
| --- | --- | --- |
| **enabled**<br>_optional_ | **Default** : `true` | boolean |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/routers/\#responses "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/routers/#routers-add_or_update_route-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_optional_ | ID of the created or updated route | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/routers/\#security "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /routers.check\_route\_name [​](https://clear.ml/docs/latest/docs/references/enterprise/routers/\#post-routerscheck_route_name "Direct link to POST /routers.check_route_name")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/routers/\#description-1 "Direct link to Description")

Internal. Checks whether the route with the name, path or subdomain can be

created

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/routers/\#parameters-1 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/routers/#routers-check_route_name-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **field**<br>_required_ | Route Property Name | enum (name, path, subdomain) |
| **value**<br>_required_ | Route Property Value | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/routers/\#responses-1 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/routers/\#security-1 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /routers.check\_task\_route\_access [​](https://clear.ml/docs/latest/docs/references/enterprise/routers/\#post-routerscheck_task_route_access "Direct link to POST /routers.check_task_route_access")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/routers/\#description-2 "Direct link to Description")

Internal. Validate task and route access. Throws exception if either requested

task or route is not available to token

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/routers/\#parameters-2 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/routers/#routers-check_task_route_access-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **access**<br>_optional_ | Access permission to check <br>**Default** : `"read_write"` | enum (read, read\_write) |
| **route**<br>_optional_ | Route ID | string |
| **tasks**<br>_optional_ | Task IDs | < string > array |
| **token**<br>_required_ | Router token for verifying access. Endpoint token can verify route access only. | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/routers/\#responses-2 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/routers/\#security-2 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /routers.delete\_routes [​](https://clear.ml/docs/latest/docs/references/enterprise/routers/\#post-routersdelete_routes "Direct link to POST /routers.delete_routes")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/routers/\#description-3 "Direct link to Description")

Internal. Delete task routes

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/routers/\#parameters-3 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/routers/#routers-delete_routes-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **force**<br>_optional_ | Allows to disable active routes <br>**Default** : `false` | boolean |
| **ids**<br>_optional_ | IDs of the routes to delete | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/routers/\#responses-3 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/routers/#routers-delete_routes-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **deleted**<br>_optional_ | The number of deleted routes | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/routers/\#security-3 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /routers.get\_routes [​](https://clear.ml/docs/latest/docs/references/enterprise/routers/\#post-routersget_routes "Direct link to POST /routers.get_routes")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/routers/\#description-4 "Direct link to Description")

Internal. Get all routes

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/routers/\#parameters-4 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/routers/#routers-get_routes-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **auth\_enabled**<br>_optional_ | Indication whether to retrieve only routes that are auth\_enabled | boolean |
| **enabled**<br>_optional_ | Set it to 'true' to retrieve only enabled routes. Set it to 'false' to retrieve <br>only disabled routes | boolean |
| **id**<br>_optional_ | List of route IDs used to filter results | < string > array |
| **last\_update**<br>_optional_ | List of last\_update constraint strings (utcformat, epoch) with an optional <br>prefix modifier (>, >=, <, <=) | < string > array |
| **name**<br>_optional_ | Get only routes whose name matches this pattern (python regular expression <br>syntax) | string |
| **only\_fields**<br>_optional_ | List of document field names (nesting is supported using '.', e.g. <br>execution.model\_labels). If provided, this list defines the query's projection <br>(only these fields will be returned for each result entry) | < string > array |
| **order\_by**<br>_optional_ | List of field names to order by. When search\_text is used, '@text\_score' can be <br>used as a field representing the text score of returned documents. Use '-' <br>prefix to specify descending order. Optional, recommended when using page | < string > array |
| **page**<br>_optional_ | Page number, returns a specific page out of the result list of results. <br>**Minimum value** : `0` | integer |
| **page\_size**<br>_optional_ | Page size, specifies the number of results returned in each page (last page may <br>contain fewer results) <br>**Minimum value** : `1` | integer |
| **path**<br>_optional_ | Get only routes whose path matches this pattern (python regular expression <br>syntax) | string |
| **search\_text**<br>_optional_ | Free text search query | string |
| **subdomain**<br>_optional_ | Get only routes whose subdomain matches this pattern (python regular experssion <br>syntax) | string |
| **type**<br>_optional_ | List of route types | < string > array |
| **user**<br>_optional_ | List of user IDs used to filter results by the route's creating user | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/routers/\#responses-4 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/routers/#routers-get_routes-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **routes**<br>_optional_ | Routes list | < [routes](https://clear.ml/docs/latest/docs/references/enterprise/routers/#routers-get_routes-post-routes) \> array |

**routes**

| Name | Description | Schema |
| --- | --- | --- |
| **auth\_enabled**<br>_optional_ | Enable auth if 'true' <br>**Default** : `true` | boolean |
| **created**<br>_optional_ | Route creation time | string (date-time) |
| **enabled**<br>_optional_ | If set to 'true' then the router is marked as enabled. Otherwise disabled <br>**Default** : `true` | boolean |
| **id**<br>_optional_ | Route ID | string |
| **last\_update**<br>_optional_ | The last time when the route was updated | string (date-time) |
| **load\_balancer**<br>_optional_ | load\_balancer | [load\_balancer](https://clear.ml/docs/latest/docs/references/enterprise/routers/#routers-get_routes-post-routes-load_balancer) |
| **name**<br>_required_ | Route Name | string |
| **path**<br>_optional_ | Route Path. Required for type 'path' | string |
| **status**<br>_optional_ | Route status | enum (available, active) |
| **subdomain**<br>_optional_ | Route Subdomain. Required for type 'subdomain' | string |
| **tasks**<br>_optional_ |  | < [tasks](https://clear.ml/docs/latest/docs/references/enterprise/routers/#routers-get_routes-post-routes-tasks) \> array |
| **type**<br>_required_ | Route type | enum (path, subdomain) |
| **updated\_by**<br>_optional_ | ID of use the user who performed last update | string |
| **urls**<br>_optional_ |  | < string > array |
| **user\_groups**<br>_optional_ | Users from those groups are allowed to access the route | < string > array |

**load\_balancer**

| Name | Description | Schema |
| --- | --- | --- |
| **enabled**<br>_optional_ | **Default** : `true` | boolean |

**tasks**

| Name | Description | Schema |
| --- | --- | --- |
| **app\_id**<br>_optional_ | Task application ID. Only for application tasks | string |
| **id**<br>_optional_ | Task ID | string |
| **name**<br>_optional_ | Task Name | string |
| **project**<br>_optional_ | Task project ID | string |
| **target**<br>_optional_ | Route target | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/routers/\#security-4 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /routers.get\_task\_routers [​](https://clear.ml/docs/latest/docs/references/enterprise/routers/\#post-routersget_task_routers "Direct link to POST /routers.get_task_routers")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/routers/\#description-5 "Direct link to Description")

Internal. Get task routers

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/routers/\#parameters-5 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/routers/#routers-get_task_routers-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **task\_only\_fields**<br>_optional_ | task\_only\_fields | < string > array |
| **task\_order\_by**<br>_optional_ | task\_order\_by | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/routers/\#responses-5 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/routers/#routers-get_task_routers-response-200) |

**Response 200**

| Name | Schema |
| --- | --- |
| **routers**<br>_optional_ | < [routers](https://clear.ml/docs/latest/docs/references/enterprise/routers/#routers-get_task_routers-post-routers) \> array |

**routers**

| Name | Description | Schema |
| --- | --- | --- |
| **last\_update\_timestamp**<br>_optional_ | Time in seconds since epoch from the last router update | integer |
| **router**<br>_required_ | Router ID | string |
| **routes**<br>_optional_ | Information about routes | < [routes](https://clear.ml/docs/latest/docs/references/enterprise/routers/#routers-get_task_routers-post-routers-routes) \> array |
| **tasks**<br>_optional_ | The details of the tasks served with the router | < object > array |
| **uptime**<br>_optional_ | Time in seconds since the router started | integer |
| **url**<br>_required_ | Router Url | string |
| **version**<br>_optional_ | Task router version | string |

**routes**

| Name | Description | Schema |
| --- | --- | --- |
| **name**<br>_optional_ | Route Name | string |
| **tasks**<br>_optional_ | Task IDs | < string > array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/routers/\#security-5 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /routers.set\_route\_enabled [​](https://clear.ml/docs/latest/docs/references/enterprise/routers/\#post-routersset_route_enabled "Direct link to POST /routers.set_route_enabled")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/routers/\#description-6 "Direct link to Description")

Internal. Enable or disable route

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/routers/\#parameters-6 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/routers/#routers-set_route_enabled-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **enabled**<br>_required_ | Route enabled status | boolean |
| **force**<br>_optional_ | Allows to disable active routes <br>**Default** : `false` | boolean |
| **id**<br>_required_ | Route ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/routers/\#responses-6 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/routers/\#security-6 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /routers.task\_router\_report [​](https://clear.ml/docs/latest/docs/references/enterprise/routers/\#post-routerstask_router_report "Direct link to POST /routers.task_router_report")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/routers/\#description-7 "Direct link to Description")

Internal. Registers task router. Can be called by admin users or service

accounts

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/routers/\#parameters-7 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/routers/#routers-task_router_report-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **router**<br>_required_ | Router ID | string |
| **status**<br>_optional_ | status | [status](https://clear.ml/docs/latest/docs/references/enterprise/routers/#routers-task_router_report-post-status) |
| **timeout**<br>_optional_ | Registration timeout in seconds. If timeout seconds have passed since the <br>task\_router last call to register, the task router is automatically removed <br>from the list of registered task routers. | integer |
| **url**<br>_required_ | Router url | string |
| **version**<br>_optional_ | Task router version | string |

**status**

| Name | Description | Schema |
| --- | --- | --- |
| **last\_update\_timestamp**<br>_optional_ | Time in seconds since epoch from the last router update | integer |
| **routes**<br>_optional_ | The list of routes | < [routes](https://clear.ml/docs/latest/docs/references/enterprise/routers/#routers-task_router_report-post-status-routes) \> array |
| **tasks**<br>_optional_ | IDs of the tasks served with the router | < string > array |
| **uptime**<br>_optional_ | Time in seconds since the router started | integer |

**routes**

| Name | Description | Schema |
| --- | --- | --- |
| **name**<br>_optional_ | Route Name | string |
| **tasks**<br>_optional_ | Task IDs | < [tasks](https://clear.ml/docs/latest/docs/references/enterprise/routers/#routers-task_router_report-post-status-routes-tasks) \> array |
| **url**<br>_optional_ | Rout Url | string |

**tasks**

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_optional_ | Task ID | string |
| **upstream\_server**<br>_optional_ | The upstream server address | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/routers/\#responses-7 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/routers/\#security-7 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /routers.unregister [​](https://clear.ml/docs/latest/docs/references/enterprise/routers/\#post-routersunregister "Direct link to POST /routers.unregister")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/routers/\#description-8 "Direct link to Description")

Internal. Unregisters task router. Can be called by admin users or service

accounts

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/routers/\#parameters-8 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/routers/#routers-unregister-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **router**<br>_required_ | Router ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/routers/\#responses-8 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/routers/\#security-8 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

- [POST /routers.add\_or\_update\_route](https://clear.ml/docs/latest/docs/references/enterprise/routers/#post-routersadd_or_update_route)
- [POST /routers.check\_route\_name](https://clear.ml/docs/latest/docs/references/enterprise/routers/#post-routerscheck_route_name)
- [POST /routers.check\_task\_route\_access](https://clear.ml/docs/latest/docs/references/enterprise/routers/#post-routerscheck_task_route_access)
- [POST /routers.delete\_routes](https://clear.ml/docs/latest/docs/references/enterprise/routers/#post-routersdelete_routes)
- [POST /routers.get\_routes](https://clear.ml/docs/latest/docs/references/enterprise/routers/#post-routersget_routes)
- [POST /routers.get\_task\_routers](https://clear.ml/docs/latest/docs/references/enterprise/routers/#post-routersget_task_routers)
- [POST /routers.set\_route\_enabled](https://clear.ml/docs/latest/docs/references/enterprise/routers/#post-routersset_route_enabled)
- [POST /routers.task\_router\_report](https://clear.ml/docs/latest/docs/references/enterprise/routers/#post-routerstask_router_report)
- [POST /routers.unregister](https://clear.ml/docs/latest/docs/references/enterprise/routers/#post-routersunregister)