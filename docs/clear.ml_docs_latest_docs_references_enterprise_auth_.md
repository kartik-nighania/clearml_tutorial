---
url: "https://clear.ml/docs/latest/docs/references/enterprise/auth/"
title: "auth | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/enterprise/auth/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

### POST /auth.add\_user [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#post-authadd_user "Direct link to POST /auth.add_user")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#description "Direct link to Description")

Add a new user manually. Only supported in on-premises deployments

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#parameters "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/auth/#auth-add_user-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **additional\_info**<br>_optional_ | User additional info | object |
| **avatar**<br>_optional_ | Avatar URL | string |
| **company**<br>_optional_ | Associated company ID. If not provided, the caller's company ID will be used | string |
| **email**<br>_required_ | Email address uniquely identifying the user | string |
| **family\_name**<br>_optional_ | Family name | string |
| **given\_name**<br>_optional_ | Given name | string |
| **name**<br>_required_ | User name (makes the auth entry more readable) | string |
| **provider**<br>_optional_ | Provider ID indicating the external provider used to authenticate the user | string |
| **provider\_token**<br>_optional_ | Provider-issued token for this user | string |
| **provider\_user\_id**<br>_optional_ | Unique user ID assigned by the external provider | string |
| **secret\_key**<br>_optional_ | A secret key (used as the user's password) | string |
| **user\_provided\_email**<br>_optional_ | User provided email | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#responses "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/auth/#auth-add_user-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_optional_ | New user ID | string |
| **secret**<br>_optional_ | The secret key used as the user's password | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#security "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /auth.create\_credentials [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#post-authcreate_credentials "Direct link to POST /auth.create_credentials")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#description-1 "Direct link to Description")

Creates a new set of credentials for the authenticated user. New key/secret is

returned. Note: Secret will never be returned in any other API call. If a

secret is lost or compromised, the key should be revoked and a new set of

credentials can be created.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#parameters-1 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/auth/#auth-create_credentials-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **expiration\_sec**<br>_optional_ | Requested credentials expiration time in seconds | integer |
| **label**<br>_optional_ | Optional credentials label | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#responses-1 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/auth/#auth-create_credentials-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **credentials**<br>_optional_ | Created credentials | [auth.credentials](https://clear.ml/docs/latest/docs/references/enterprise/definitions#authcredentials) |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#security-1 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /auth.create\_service\_user [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#post-authcreate_service_user "Direct link to POST /auth.create_service_user")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#description-2 "Direct link to Description")

Internal. Creates a new service user

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#parameters-2 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/auth/#auth-create_service_user-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **allow\_running\_as\_owner**<br>_optional_ | Whether the service user can impersonate as another user <br>**Default** : `false` | boolean |
| **credentials\_expiration\_sec**<br>_optional_ | Requested credentials expiration time in seconds | integer |
| **name**<br>_required_ | User name (makes the auth entry more readable) | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#responses-2 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/auth/#auth-create_service_user-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **credentials**<br>_optional_ | Created credentials | [auth.credentials](https://clear.ml/docs/latest/docs/references/enterprise/definitions#authcredentials) |
| **id**<br>_optional_ | New user ID | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#security-2 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /auth.create\_user [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#post-authcreate_user "Direct link to POST /auth.create_user")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#description-3 "Direct link to Description")

Internal. Creates a new user auth entry. Intended for internal use.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#parameters-3 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/auth/#auth-create_user-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **additional\_info**<br>_optional_ | User additional info | object |
| **avatar**<br>_optional_ | Avatar URL | string |
| **company**<br>_required_ | Associated company ID | string |
| **email**<br>_required_ | Email address uniquely identifying the user | string |
| **family\_name**<br>_optional_ | Family name | string |
| **given\_name**<br>_optional_ | Given name | string |
| **internal**<br>_optional_ | Whether the user is internal. Only system users can create internal users <br>**Default** : `false` | boolean |
| **name**<br>_required_ | User name (makes the auth entry more readable) | string |
| **provider**<br>_optional_ | Provider ID indicating the external provider used to authenticate the user | string |
| **provider\_token**<br>_optional_ | Provider-issued token for this user | string |
| **provider\_user\_id**<br>_optional_ | Unique user ID assigned by the external provider | string |
| **role**<br>_optional_ | User role | [auth.role](https://clear.ml/docs/latest/docs/references/enterprise/definitions#authrole) |
| **user\_provided\_email**<br>_optional_ | User provided email | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#responses-3 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/auth/#auth-create_user-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_optional_ | New user ID | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#security-3 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /auth.delete\_user [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#post-authdelete_user "Direct link to POST /auth.delete_user")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#description-4 "Direct link to Description")

Delete a new user manually. Only supported in on-premises deployments. This

only removes the user's auth entry so that any references to the deleted user's

ID will still have valid user information

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#parameters-4 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/auth/#auth-delete_user-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **user**<br>_required_ | User ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#responses-4 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/auth/#auth-delete_user-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **deleted**<br>_optional_ | True if user was successfully deleted, False otherwise | boolean |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#security-4 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /auth.edit\_credentials [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#post-authedit_credentials "Direct link to POST /auth.edit_credentials")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#description-5 "Direct link to Description")

Updates the label of the existing credentials for the authenticated user.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#parameters-5 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/auth/#auth-edit_credentials-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **access\_key**<br>_required_ | Existing credentials key | string |
| **label**<br>_optional_ | New credentials label | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#responses-5 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/auth/#auth-edit_credentials-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **updated**<br>_optional_ | Number of credentials updated | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#security-5 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /auth.edit\_user [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#post-authedit_user "Direct link to POST /auth.edit_user")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#description-6 "Direct link to Description")

Edit a users' auth data properties

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#parameters-6 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/auth/#auth-edit_user-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **role**<br>_optional_ | The new user's role within the company | [auth.role](https://clear.ml/docs/latest/docs/references/enterprise/definitions#authrole) |
| **user**<br>_optional_ | User ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#responses-6 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/auth/#auth-edit_user-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **fields**<br>_optional_ | Updated fields names and values | object |
| **updated**<br>_optional_ | Number of users updated (0 or 1) | number |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#security-6 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /auth.fixed\_users\_mode [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#post-authfixed_users_mode "Direct link to POST /auth.fixed_users_mode")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#description-7 "Direct link to Description")

Internal. Return fixed users mode status

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#parameters-7 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#responses-7 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/auth/#auth-fixed_users_mode-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **enabled**<br>_optional_ | Fixed users mode enabled | boolean |

### POST /auth.generate\_endpoint\_router\_token [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#post-authgenerate_endpoint_router_token "Direct link to POST /auth.generate_endpoint_router_token")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#description-8 "Direct link to Description")

Internal. Get a router token that provides task access to non-clearml user

through specific routes

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#parameters-8 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/auth/#auth-generate_endpoint_router_token-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **endpoints**<br>_required_ | IDs of the routes that this token can be used for | < string > array |
| **expiration\_sec**<br>_optional_ | Requested token expiration time in seconds. Cannot be larger then <br>max\_expiration\_sec returned from auth.get\_router\_tokens | integer |
| **label**<br>_required_ | Token label | string |
| **metadata**<br>_optional_ | Token metadata | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#responses-8 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/auth/#auth-generate_endpoint_router_token-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **token**<br>_optional_ | User auth token used for verifying task access | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#security-7 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /auth.generate\_router\_token [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#post-authgenerate_router_token "Direct link to POST /auth.generate_router_token")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#description-9 "Direct link to Description")

Internal. Get a router token based on supplied credentials (key/secret).

Intended for use by users with key/secret credentials that wish to obtain a

token for use with the task router / App Gateway. Token can only be used to

verify task access by the router.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#parameters-9 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/auth/#auth-generate_router_token-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **expiration\_sec**<br>_optional_ | Requested token expiration time in seconds. Cannot be larger then <br>max\_expiration\_sec returned from auth.get\_router\_tokens | integer |
| **label**<br>_required_ | Token label | string |
| **user**<br>_optional_ | The user to generate token for. Only admin users can generate tokens for other <br>users | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#responses-9 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/auth/#auth-generate_router_token-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **token**<br>_optional_ | User auth token used for verifying task access | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#security-8 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /auth.get\_credentials [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#post-authget_credentials "Direct link to POST /auth.get_credentials")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#description-10 "Direct link to Description")

Returns all existing credential keys for the authenticated user. Note: Only

credential keys are returned.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#parameters-10 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#responses-10 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/auth/#auth-get_credentials-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **additional\_credentials**<br>_optional_ | The user credentials for the user tenant companies, each with an empty secret <br>field. | < string, [auth.credential\_key](https://clear.ml/docs/latest/docs/references/enterprise/definitions#authcredential_key) \> map |
| **credentials**<br>_optional_ | List of credentials for the user own company, each with an empty secret field. | < [auth.credential\_key](https://clear.ml/docs/latest/docs/references/enterprise/definitions#authcredential_key) \> array |
| **default\_expiration\_sec**<br>_optional_ | Default credentials expiration in seconds | integer |
| **max\_credentials**<br>_optional_ | Max credenitals allowed for the user | integer |
| **max\_expiration\_sec**<br>_optional_ | Maximum credentials expiration in seconds for non-admin users | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#security-9 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /auth.get\_router\_tokens [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#post-authget_router_tokens "Direct link to POST /auth.get_router_tokens")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#description-11 "Direct link to Description")

Internal. Get Router tokens. Only admin users can get revoked tokens, other

user tokens or endpoint tokens

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#parameters-11 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/auth/#auth-get_router_tokens-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **include\_revoked**<br>_optional_ | If set to 'true' then revoked tokens are also returned <br>**Default** : `false` | boolean |
| **only\_fields**<br>_optional_ | List of document's field names (nesting is supported using '.', e.g. <br>user.name). If provided, this list defines the query's projection (only these <br>fields will be returned for each result entry) | < string > array |
| **order\_by**<br>_optional_ | List of field names to order by. Use '-' prefix to specify descending order. <br>Optional, recommended when using page | < string > array |
| **page**<br>_optional_ | Page number, returns a specific page out of the resulting list of tokens <br>**Minimum value** : `0` | integer |
| **page\_size**<br>_optional_ | Page size, specifies the number of results returned in each page (last page may <br>contain fewer results) <br>**Minimum value** : `1` | integer |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#responses-11 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/auth/#auth-get_router_tokens-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **max\_expiration\_sec**<br>_optional_ | Max router token expiration in seconds | integer |
| **tokens**<br>_optional_ |  | < [tokens](https://clear.ml/docs/latest/docs/references/enterprise/auth/#auth-get_router_tokens-post-tokens) \> array |

**tokens**

| Name | Description | Schema |
| --- | --- | --- |
| **created**<br>_optional_ | Token creation time | string (date-time) |
| **created\_by**<br>_optional_ | User who created the token | object |
| **endpoints**<br>_optional_ | IDs of the routes that this token can be used for. Only for endpoint tokens | < object > array |
| **expires**<br>_optional_ | Token expiration time | string (date-time) |
| **id**<br>_optional_ | Token ID | string |
| **key**<br>_optional_ | Token key | string |
| **label**<br>_optional_ | Token Label | string |
| **metadata**<br>_optional_ | Token metadata. Only for endpoint tokens | object |
| **revoked**<br>_optional_ | Whether the token revoked | boolean |
| **revoked\_at**<br>_optional_ | Token revokation time | string (date-time) |
| **revoked\_by**<br>_optional_ | User who revoked the token | object |
| **type**<br>_optional_ | Token type | enum (endpoint\_token, identity\_token) |
| **user**<br>_optional_ | Token user | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#security-10 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /auth.get\_task\_token [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#post-authget_task_token "Direct link to POST /auth.get_task_token")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#description-12 "Direct link to Description")

Get a task-limited token based on supplied credentials (token or key/secret).

Intended for use by users who wish to run a task under limited credentials.

Returned token will be limited so that all operations can only be performed on

the specified task.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#parameters-12 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/auth/#auth-get_task_token-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **expiration\_sec**<br>_optional_ | Requested token expiration time in seconds. Not guaranteed, might be <br>overridden by the service | integer |
| **task**<br>_required_ | Task ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#responses-12 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/auth/#auth-get_task_token-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **token**<br>_optional_ | Token string | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#security-11 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /auth.get\_task\_token\_for\_user [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#post-authget_task_token_for_user "Direct link to POST /auth.get_task_token_for_user")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#description-13 "Direct link to Description")

Internal. Get a task-limited token for the specified user. Intended for

internal use. Token will be limited by appropriate permissions for the provided

user and restricted for operations only for the provided task.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#parameters-13 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/auth/#auth-get_task_token_for_user-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **company**<br>_required_ | Company ID | string |
| **expiration\_sec**<br>_optional_ | Requested token expiration time in seconds. Not guaranteed, might be <br>overridden by the service | integer |
| **task**<br>_required_ | Task ID | string |
| **user**<br>_required_ | User ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#responses-13 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/auth/#auth-get_task_token_for_user-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **token**<br>_optional_ | Token string | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#security-12 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root |

### POST /auth.get\_token\_for\_user [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#post-authget_token_for_user "Direct link to POST /auth.get_token_for_user")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#description-14 "Direct link to Description")

Internal. Get a token for the specified user. Intended for internal use. Token

will be limited by appropriate permissions for the provided user.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#parameters-14 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/auth/#auth-get_token_for_user-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **company**<br>_required_ | Company ID | string |
| **expiration\_sec**<br>_optional_ | Requested token expiration time in seconds. Not guaranteed, might be <br>overridden by the service | integer |
| **user**<br>_required_ | User ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#responses-14 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/auth/#auth-get_token_for_user-response-200) |

**Response 200**

| Name | Schema |
| --- | --- |
| **token**<br>_optional_ | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#security-13 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root |

### POST /auth.get\_users\_info [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#post-authget_users_info "Direct link to POST /auth.get_users_info")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#description-15 "Direct link to Description")

Internal. retrieves email and created time of users

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#parameters-15 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/auth/#auth-get_users_info-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **emails**<br>_optional_ | user emails to retrieve information of | < string > array |
| **include\_providers\_info**<br>_optional_ | If set then user info stored for each provider is returned <br>**Default** : `false` | boolean |
| **users**<br>_optional_ | user IDs to retrieve information of | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#responses-15 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/auth/#auth-get_users_info-response-200) |

**Response 200**

| Name | Schema |
| --- | --- |
| **users**<br>_optional_ | < string, [users](https://clear.ml/docs/latest/docs/references/enterprise/auth/#auth-get_users_info-post-users) \> map |

**users**

| Name | Schema |
| --- | --- |
| **created**<br>_optional_ | string (date-time) |
| **email**<br>_optional_ | string |
| **id**<br>_optional_ | string |
| **providers**<br>_optional_ | object |
| **role**<br>_optional_ | string |
| **sec\_groups**<br>_optional_ | < string > array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#security-14 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root |

### POST /auth.locate\_credentials [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#post-authlocate_credentials "Direct link to POST /auth.locate_credentials")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#description-16 "Direct link to Description")

Get user and credentials info info from the access key

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#parameters-16 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/auth/#auth-locate_credentials-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **access\_key**<br>_required_ | Existing credentials key | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#responses-16 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/auth/#auth-locate_credentials-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **expire**<br>_optional_ | Credential expiration time (UTC) | string (date-time) |
| **label**<br>_optional_ | Credentials label | string |
| **last\_used**<br>_optional_ | The time when the credentials were last used | string (date-time) |
| **last\_used\_from**<br>_optional_ |  | string |
| **name**<br>_optional_ | User name | string |
| **user**<br>_optional_ | User ID | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#security-15 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | admin,system,root |

### POST /auth.login [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#post-authlogin "Direct link to POST /auth.login")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#description-17 "Direct link to Description")

Get a token based on supplied credentials (key/secret). Intended for use by

users with key/secret credentials that wish to obtain a token for use with

other services. Token will be limited by the same permissions that exist for

the credentials used in this call.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#parameters-17 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/auth/#auth-login-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **expiration\_sec**<br>_optional_ | Requested token expiration time in seconds. Not guaranteed, might be <br>overridden by the service | integer |
| **set\_cookie**<br>_optional_ | Set a cookie with the generated token on the response <br>**Default** : `true` | boolean |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#responses-17 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/auth/#auth-login-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **token**<br>_optional_ | Token string | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#security-16 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /auth.logout [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#post-authlogout "Direct link to POST /auth.logout")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#description-18 "Direct link to Description")

Removes the authentication cookie from the current session

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#parameters-18 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#responses-18 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#security-17 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /auth.redirect\_to\_router [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#post-authredirect_to_router "Direct link to POST /auth.redirect_to_router")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#description-19 "Direct link to Description")

Generates the auth code for the passed router and task and redirects the client

to the router

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#parameters-19 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/auth/#auth-redirect_to_router-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **path**<br>_optional_ | Path to use when redirecting | string |
| **route**<br>_optional_ | Route ID. Either task or route (or both) should be specified | string |
| **router**<br>_required_ | Router ID. Should match one of the configured server routers | string |
| **subdomain**<br>_optional_ | Subdomain to use when redirecting | string |
| **task**<br>_optional_ | Task ID. Either task or route (or both) should be specified | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#responses-19 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#security-18 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /auth.reload\_config [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#post-authreload_config "Direct link to POST /auth.reload_config")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#description-20 "Direct link to Description")

Reload auth configuration (currently supports blocking tokens). For user roles

associated with a company (Admin, Superuser) this call will only affect

company-related configuration.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#parameters-20 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#responses-20 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#security-19 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin,superuser |

### POST /auth.revoke\_credentials [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#post-authrevoke_credentials "Direct link to POST /auth.revoke_credentials")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#description-21 "Direct link to Description")

Revokes (and deletes) a set (key, secret) of credentials for the authenticated

user.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#parameters-21 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/auth/#auth-revoke_credentials-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **access\_key**<br>_optional_ | Credentials key | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#responses-21 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/auth/#auth-revoke_credentials-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **revoked**<br>_optional_ | Number of credentials revoked | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#security-20 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /auth.revoke\_router\_tokens [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#post-authrevoke_router_tokens "Direct link to POST /auth.revoke_router_tokens")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#description-22 "Direct link to Description")

Internal. Remove router tokens by ids

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#parameters-22 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/auth/#auth-revoke_router_tokens-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **ids**<br>_required_ | IDs of the tokens to revoke. Only admins can remove tokens for other users | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#responses-22 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/auth/#auth-revoke_router_tokens-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **revoked**<br>_optional_ | The number of revoked tokens | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#security-21 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /auth.set\_credentials [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#post-authset_credentials "Direct link to POST /auth.set_credentials")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#description-23 "Direct link to Description")

Set a secret\_key for a given access\_key. Only supported in on-premises

deployments

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#parameters-23 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/auth/#auth-set_credentials-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **access\_key**<br>_required_ | Credentials key. Must be identical to the user's ID (this is the only value <br>supported in on-premises deployments) | string |
| **secret\_key**<br>_required_ | New secret key | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#responses-23 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/auth/#auth-set_credentials-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **set**<br>_optional_ | True if secret was successfully set, False otherwise | boolean |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#security-22 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /auth.validate\_router\_code [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#post-authvalidate_router_code "Direct link to POST /auth.validate_router_code")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#description-24 "Direct link to Description")

Internal. Validate the previously issued router auth code and return the auth

token. Can be called by admin users or service accounts

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#parameters-24 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/auth/#auth-validate_router_code-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **code**<br>_required_ | The code received by the router from redirect\_to\_router call | string |
| **route**<br>_optional_ | Route ID. Either task or route (or both) should be specified | string |
| **router**<br>_required_ | Router ID. Should be the same as used for the code generation | string |
| **task**<br>_optional_ | Task ID. Either task or route (or both) should be specified | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#responses-24 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/auth/#auth-validate_router_code-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **token**<br>_optional_ | User auth token used for verifying task access | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#security-23 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /auth.validate\_token [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#post-authvalidate_token "Direct link to POST /auth.validate_token")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#description-25 "Direct link to Description")

Internal. Validate a token and return user identity if valid. Intended for

internal use.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#parameters-25 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/auth/#auth-validate_token-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **token**<br>_required_ | Token string | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#responses-25 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/auth/#auth-validate_token-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **company**<br>_optional_ | Associated company ID | string |
| **role**<br>_optional_ | User role (system, root, admin, user, ...) | string |
| **tenant**<br>_optional_ | Tenant company ID | string |
| **tenants**<br>_optional_ | List of all the tenant companies that the user joined | < string > array |
| **user**<br>_optional_ | Associated user ID | string |
| **valid**<br>_optional_ | Boolean indicating if the token is valid | boolean |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#security-24 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root |

### POST /auth.validate\_user [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#post-authvalidate_user "Direct link to POST /auth.validate_user")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#description-26 "Direct link to Description")

Internal. Validate a user using an email and provider user ID. Intended for

internal use.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#parameters-26 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/auth/#auth-validate_user-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **email**<br>_required_ | Email address uniquely identifying the user | string |
| **provider**<br>_required_ | Provider ID indicating the external provider used to authenticate the user | string |
| **provider\_token**<br>_optional_ | Provider-issued token for this user | string |
| **provider\_user\_id**<br>_required_ | Unique user ID assigned by the external provider | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#responses-26 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/auth/#auth-validate_user-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **company**<br>_optional_ | Associated company ID | string |
| **msg**<br>_optional_ | Validation message | string |
| **user**<br>_optional_ | Associated user ID | string |
| **valid**<br>_optional_ | Boolean indicating if the user is valid | boolean |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/auth/\#security-25 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root |

- [POST /auth.add\_user](https://clear.ml/docs/latest/docs/references/enterprise/auth/#post-authadd_user)
- [POST /auth.create\_credentials](https://clear.ml/docs/latest/docs/references/enterprise/auth/#post-authcreate_credentials)
- [POST /auth.create\_service\_user](https://clear.ml/docs/latest/docs/references/enterprise/auth/#post-authcreate_service_user)
- [POST /auth.create\_user](https://clear.ml/docs/latest/docs/references/enterprise/auth/#post-authcreate_user)
- [POST /auth.delete\_user](https://clear.ml/docs/latest/docs/references/enterprise/auth/#post-authdelete_user)
- [POST /auth.edit\_credentials](https://clear.ml/docs/latest/docs/references/enterprise/auth/#post-authedit_credentials)
- [POST /auth.edit\_user](https://clear.ml/docs/latest/docs/references/enterprise/auth/#post-authedit_user)
- [POST /auth.fixed\_users\_mode](https://clear.ml/docs/latest/docs/references/enterprise/auth/#post-authfixed_users_mode)
- [POST /auth.generate\_endpoint\_router\_token](https://clear.ml/docs/latest/docs/references/enterprise/auth/#post-authgenerate_endpoint_router_token)
- [POST /auth.generate\_router\_token](https://clear.ml/docs/latest/docs/references/enterprise/auth/#post-authgenerate_router_token)
- [POST /auth.get\_credentials](https://clear.ml/docs/latest/docs/references/enterprise/auth/#post-authget_credentials)
- [POST /auth.get\_router\_tokens](https://clear.ml/docs/latest/docs/references/enterprise/auth/#post-authget_router_tokens)
- [POST /auth.get\_task\_token](https://clear.ml/docs/latest/docs/references/enterprise/auth/#post-authget_task_token)
- [POST /auth.get\_task\_token\_for\_user](https://clear.ml/docs/latest/docs/references/enterprise/auth/#post-authget_task_token_for_user)
- [POST /auth.get\_token\_for\_user](https://clear.ml/docs/latest/docs/references/enterprise/auth/#post-authget_token_for_user)
- [POST /auth.get\_users\_info](https://clear.ml/docs/latest/docs/references/enterprise/auth/#post-authget_users_info)
- [POST /auth.locate\_credentials](https://clear.ml/docs/latest/docs/references/enterprise/auth/#post-authlocate_credentials)
- [POST /auth.login](https://clear.ml/docs/latest/docs/references/enterprise/auth/#post-authlogin)
- [POST /auth.logout](https://clear.ml/docs/latest/docs/references/enterprise/auth/#post-authlogout)
- [POST /auth.redirect\_to\_router](https://clear.ml/docs/latest/docs/references/enterprise/auth/#post-authredirect_to_router)
- [POST /auth.reload\_config](https://clear.ml/docs/latest/docs/references/enterprise/auth/#post-authreload_config)
- [POST /auth.revoke\_credentials](https://clear.ml/docs/latest/docs/references/enterprise/auth/#post-authrevoke_credentials)
- [POST /auth.revoke\_router\_tokens](https://clear.ml/docs/latest/docs/references/enterprise/auth/#post-authrevoke_router_tokens)
- [POST /auth.set\_credentials](https://clear.ml/docs/latest/docs/references/enterprise/auth/#post-authset_credentials)
- [POST /auth.validate\_router\_code](https://clear.ml/docs/latest/docs/references/enterprise/auth/#post-authvalidate_router_code)
- [POST /auth.validate\_token](https://clear.ml/docs/latest/docs/references/enterprise/auth/#post-authvalidate_token)
- [POST /auth.validate\_user](https://clear.ml/docs/latest/docs/references/enterprise/auth/#post-authvalidate_user)