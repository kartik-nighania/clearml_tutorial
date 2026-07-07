---
url: "https://clear.ml/docs/latest/docs/references/enterprise/login/"
title: "login | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/enterprise/login/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

### POST /login.add\_whitelist\_entries [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#post-loginadd_whitelist_entries "Direct link to POST /login.add_whitelist_entries")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#description "Direct link to Description")

Adds new login whitelist entries.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#parameters "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/login/#login-add_whitelist_entries-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **emails**<br>_optional_ | Emails for which new entries should be created. | < string (email) > array |
| **is\_admin**<br>_optional_ | DEPRECATED legacy field, superseded by 'role' (introduced in 2.37). If set to <br>true then the users created from these entries will be admins. Otherwise <br>regular users. <br>**Default** : `false` | boolean |
| **role**<br>_optional_ | Role to assign to users created from these entries. Takes precedence over the <br>deprecated 'is\_admin' legacy field. | [login.assignable\_role](https://clear.ml/docs/latest/docs/references/enterprise/definitions#loginassignable_role) |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#responses "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/login/#login-add_whitelist_entries-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **added**<br>_optional_ | Emails for which new entries were actually added. | < string (email) > array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#security "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /login.finish\_sso\_callback [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#post-loginfinish_sso_callback "Direct link to POST /login.finish_sso_callback")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#description-1 "Direct link to Description")

Finalize the login process for the multitenant login flow

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#parameters-1 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/login/#login-finish_sso_callback-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **company**<br>_optional_ | Company ID | string |
| **session\_id**<br>_optional_ | ID of the session returned from the sso\_callback call | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#responses-1 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/login/#login-finish_sso_callback-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **company\_id**<br>_optional_ | The id of the company that the user logged into | string |
| **login\_status**<br>_optional_ | The status of the login. Indicates whether the user was logged in or sign up <br>required | [login.login\_status\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions#loginlogin_status_enum) |
| **signup\_info**<br>_optional_ | Info for the user sign up (in case the user does not exist) | [login.signup\_info](https://clear.ml/docs/latest/docs/references/enterprise/definitions#loginsignup_info) |
| **state**<br>_optional_ | The application state that was passed by the client in the beginning of the <br>login process | string |
| **token**<br>_optional_ | Generated token | string |
| **user\_id**<br>_optional_ | Logged-in user ID | string |

### POST /login.get\_settings [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#post-loginget_settings "Direct link to POST /login.get_settings")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#description-2 "Direct link to Description")

Get the company's login settings, including auto-login domains and user invites

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#parameters-2 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#responses-2 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/login/#login-get_settings-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **domains**<br>_optional_ | Auto-login domains | < string (hostname) > array |
| **whitelist\_entries**<br>_optional_ | Whitelist entries | < [login.whitelist\_entry](https://clear.ml/docs/latest/docs/references/enterprise/definitions#loginwhitelist_entry) \> array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#security-1 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /login.get\_whitelist [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#post-loginget_whitelist "Direct link to POST /login.get_whitelist")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#description-3 "Direct link to Description")

Get whitelist entries (optionally filtered). Reserved for internal use.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#parameters-3 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/login/#login-get_whitelist-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **domain**<br>_optional_ | Email domain. If provided, only whitelist entries with this specific domain <br>will be returned <br>NOTE: cannot be used in conjunction with email | string (hostname) |
| **email**<br>_optional_ | Email address. If provided, only whitelist entries which contain this email or <br>whose domain matches this email's domain will be returned <br>NOTE: cannot be used in conjunction with domain | string (email) |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#responses-3 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/login/#login-get_whitelist-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **entries**<br>_optional_ | List of whitelist entries | < [login.login\_white\_list\_v1\_5](https://clear.ml/docs/latest/docs/references/enterprise/definitions#loginlogin_white_list_v1_5) \> array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#security-2 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root |

### POST /login.logout [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#post-loginlogout "Direct link to POST /login.logout")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#description-4 "Direct link to Description")

Logout (including SSO, if used))

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#parameters-4 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/login/#login-logout-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **provider**<br>_optional_ | Provider key in case call is not authenticated | string |
| **redirect\_url**<br>_optional_ | Redirect URL to use in the provider's logout flow | string |
| **tenant**<br>_optional_ | Tenant name in multi tenant mode. Optional | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#responses-4 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/login/#login-logout-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **redirect\_url**<br>_optional_ | Provider logout flow redirect URL for the caller to follow | string |

### POST /login.remove\_whitelist\_entries [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#post-loginremove_whitelist_entries "Direct link to POST /login.remove_whitelist_entries")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#description-5 "Direct link to Description")

Remove existing login whitelist entries. Only possible for entries that have

not already been accepted.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#parameters-5 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/login/#login-remove_whitelist_entries-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **emails**<br>_optional_ | Emails for which whitelist entries should be removed. | < string (email) > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#responses-5 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/login/#login-remove_whitelist_entries-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **removed**<br>_optional_ | Emails for which white list entries were actually removed. | < string (email) > array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#security-3 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /login.set\_domains [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#post-loginset_domains "Direct link to POST /login.set_domains")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#description-6 "Direct link to Description")

Sets the auto-login domains for this company.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#parameters-6 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/login/#login-set_domains-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **domains**<br>_optional_ | Auto-login domains | < string (hostname) > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#responses-6 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#security-4 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /login.signup\_user [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#post-loginsignup_user "Direct link to POST /login.signup_user")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#description-7 "Direct link to Description")

Creates a new user and logges it in

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#parameters-7 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/login/#login-signup_user-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **return\_token**<br>_optional_ | Return the generated token in this call's result (token is always embedded in <br>the session) <br>**Default** : `false` | boolean |
| **signup\_data**<br>_required_ | Info for the user sign up | [signup\_data](https://clear.ml/docs/latest/docs/references/enterprise/login/#login-signup_user-post-signup_data) |

**signup\_data**

| Name | Description | Schema |
| --- | --- | --- |
| **additional\_info**<br>_optional_ | The user additional info | object |
| **avatar**<br>_optional_ | The user avatar | string |
| **company\_name**<br>_optional_ | Company name for the user. This field is required. In case the user was invited <br>to join the company this field cannot be changed | string |
| **crm\_form\_data**<br>_optional_ | The user data for the CRM system | [crm\_form\_data](https://clear.ml/docs/latest/docs/references/enterprise/login/#login-signup_user-post-signup_data-crm_form_data) |
| **email**<br>_optional_ | The user email | string |
| **family\_name**<br>_optional_ | The user family name | string |
| **given\_name**<br>_optional_ | The user given name | string |
| **name**<br>_optional_ | The user full name. This field is required | string |
| **signup\_token**<br>_optional_ | Sign-up token recieved from the sso\_callback call. This field is required | string |

**crm\_form\_data**

| Name | Description | Schema |
| --- | --- | --- |
| **form\_data**<br>_optional_ | The filled form data | string |
| **form\_id**<br>_optional_ | The ID of the form | string |
| **portal\_id**<br>_optional_ | The ID of the portal | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#responses-7 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/login/#login-signup_user-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **company\_id**<br>_optional_ | The id of the user company | string |
| **company\_name**<br>_optional_ | The name of the user company | string |
| **token**<br>_optional_ | Generated token | string |
| **user\_id**<br>_optional_ | Created user ID | string |

### POST /login.sso\_authorize [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#post-loginsso_authorize "Direct link to POST /login.sso_authorize")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#description-8 "Direct link to Description")

Return provider redirect URL.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#parameters-8 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/login/#login-sso_authorize-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **callback\_url**<br>_optional_ | Callback URL for this provider | string |
| **callback\_url\_prefix**<br>_optional_ | The callback url prefix. Used for building callback\_url if callback\_url is not <br>specified | string |
| **company\_hint**<br>_optional_ | Company ID hint. Used only in the multitenant login flow | string |
| **provider**<br>_required_ | SSO Provider name (id) | string |
| **state**<br>_optional_ | ASCII base64 encoded application state | string |
| **tenant**<br>_optional_ | Company ID to show only relevant login options | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#responses-8 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/login/#login-sso_authorize-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **redirect\_url**<br>_optional_ | Provider redirect URL | string |

### POST /login.sso\_callback [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#post-loginsso_callback "Direct link to POST /login.sso_callback")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#description-9 "Direct link to Description")

Handle callback received from provider. Returns user ID and embeds token on the

session.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#parameters-9 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/login/#login-sso_callback-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **args**<br>_required_ | Redirected callback args | < string, string > map |
| **callback\_url**<br>_required_ | Callback URL for this provider | string |
| **provider**<br>_required_ | SSO Provider name (id) | string |
| **return\_token**<br>_optional_ | Return the generated token in this call's result (token is always embedded in <br>the session) <br>**Default** : `false` | boolean |
| **signup\_flow**<br>_optional_ | If set to 'true' then the user is peforming signup. Otherwise login. <br>**Default** : `false` | boolean |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#responses-9 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/login/#login-sso_callback-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **choose\_company**<br>_optional_ | Company selection options for external tenant | [login.choose\_company](https://clear.ml/docs/latest/docs/references/enterprise/definitions#loginchoose_company) |
| **company\_id**<br>_optional_ | The id of the company that the user logged into | string |
| **login\_status**<br>_optional_ | The status of the login. Indicates whether the user was logged in or sign up <br>required | [login.login\_status\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions#loginlogin_status_enum) |
| **signup\_info**<br>_optional_ | Info for the user sign up (in case the user does not exist) | [login.signup\_info](https://clear.ml/docs/latest/docs/references/enterprise/definitions#loginsignup_info) |
| **state**<br>_optional_ | The application state that was passed by the client in the beginning of the <br>login process | string |
| **token**<br>_optional_ | Generated token | string |
| **user\_id**<br>_optional_ | Logged-in user ID | string |

### POST /login.sso\_callback\_duo [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#post-loginsso_callback_duo "Direct link to POST /login.sso_callback_duo")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#description-10 "Direct link to Description")

Handle post callback received from provider. Embeds token on the session and

redirects to the client callback.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#parameters-10 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#responses-10 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

### POST /login.sso\_callback\_google\_saml [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#post-loginsso_callback_google_saml "Direct link to POST /login.sso_callback_google_saml")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#description-11 "Direct link to Description")

Handle post callback received from provider. Embeds token on the session and

redirects to the client callback.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#parameters-11 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#responses-11 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

### POST /login.sso\_callback\_google\_saml\_support [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#post-loginsso_callback_google_saml_support "Direct link to POST /login.sso_callback_google_saml_support")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#description-12 "Direct link to Description")

Handle post callback received from provider. Embeds token on the session and

redirects to the client callback.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#parameters-12 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#responses-12 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

### POST /login.sso\_callback\_jumpcloudsaml [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#post-loginsso_callback_jumpcloudsaml "Direct link to POST /login.sso_callback_jumpcloudsaml")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#description-13 "Direct link to Description")

Handle post callback received from provider. Embeds token on the session and

redirects to the client callback.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#parameters-13 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#responses-13 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

### POST /login.sso\_callback\_keycloak [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#post-loginsso_callback_keycloak "Direct link to POST /login.sso_callback_keycloak")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#description-14 "Direct link to Description")

Handle post callback received from provider. Embeds token on the session and

redirects to the client callback.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#parameters-14 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#responses-14 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

### POST /login.sso\_callback\_microsoft\_ad [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#post-loginsso_callback_microsoft_ad "Direct link to POST /login.sso_callback_microsoft_ad")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#description-15 "Direct link to Description")

Handle post callback received from provider. Embeds token on the session and

redirects to the client callback.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#parameters-15 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#responses-15 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

### POST /login.sso\_callback\_saml [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#post-loginsso_callback_saml "Direct link to POST /login.sso_callback_saml")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#description-16 "Direct link to Description")

Generic saml handle post callback received from provider

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#parameters-16 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#responses-16 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

### POST /login.supported\_modes [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#post-loginsupported_modes "Direct link to POST /login.supported_modes")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#description-17 "Direct link to Description")

Return supported login modes.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#parameters-17 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/login/#login-supported_modes-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **company\_hint**<br>_optional_ | Company ID hint. Used only in the multitenant login flow | string |
| **internal**<br>_optional_ | Whether to return 'internal' providers <br>**Default** : `false` | boolean |
| **tenant**<br>_optional_ | External tenant to show login options only from the relevant companies | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#responses-17 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/login/#login-supported_modes-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **authenticated**<br>_optional_ | Is user authenticated | boolean |
| **basic**<br>_optional_ |  | [basic](https://clear.ml/docs/latest/docs/references/enterprise/login/#login-supported_modes-post-basic) |
| **free\_signup**<br>_optional_ | True if free signup is allowed on the server (i.e. any user verified by an SSO <br>provider can create an account) <br>**Default** : `false` | boolean |
| **sso**<br>_optional_ | SSO authentication providers | object |
| **sso\_providers**<br>_optional_ | The list of SSO authentication providers | < [sso\_providers](https://clear.ml/docs/latest/docs/references/enterprise/login/#login-supported_modes-post-sso_providers) \> array |
| **tenant**<br>_optional_ | The external tenant that was used for returning login providers | string |
| **tenant\_login**<br>_optional_ | 'true' if the apiserver is configured for per-tenant login. 'false' otherwise | boolean |

**basic**

| Name | Description | Schema |
| --- | --- | --- |
| **enabled**<br>_optional_ | Basic authentication (fixed users mode) mode enabled | boolean |
| **guest**<br>_optional_ |  | [guest](https://clear.ml/docs/latest/docs/references/enterprise/login/#login-supported_modes-post-basic-guest) |

**guest**

| Name | Description | Schema |
| --- | --- | --- |
| **enabled**<br>_optional_ | Basic authentication guest mode enabled | boolean |
| **name**<br>_optional_ | Guest name | string |
| **password**<br>_optional_ | Guest password | string |
| **username**<br>_optional_ | Guest username | string |

**sso\_providers**

| Name | Description | Schema |
| --- | --- | --- |
| **display\_name**<br>_optional_ | The display name of the sso provider | string |
| **name**<br>_optional_ | The name of the sso provider | string |

### POST /login.test\_sso\_callback [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#post-logintest_sso_callback "Direct link to POST /login.test_sso_callback")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#description-18 "Direct link to Description")

Tests callback received from provider. Returns user data from the provider and

error (if any)

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#parameters-18 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/login/#login-test_sso_callback-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **args**<br>_required_ | Redirected callback args | < string, string > map |
| **callback\_url**<br>_required_ | Callback URL for this provider | string |
| **provider**<br>_required_ | SSO Provider name (id) | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/login/\#responses-18 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/login/#login-test_sso_callback-response-200) |

**Response 200**

| Name | Schema |
| --- | --- |
| **configuration\_info**<br>_optional_ | [configuration\_info](https://clear.ml/docs/latest/docs/references/enterprise/login/#login-test_sso_callback-post-configuration_info) |
| **error\_msg**<br>_optional_ | string |
| **mapped\_user\_data**<br>_optional_ | [mapped\_user\_data](https://clear.ml/docs/latest/docs/references/enterprise/login/#login-test_sso_callback-post-mapped_user_data) |
| **user\_data**<br>_optional_ | object |

**configuration\_info**

| Name | Description | Schema |
| --- | --- | --- |
| **name**<br>_optional_ | The name of the configuration | string |
| **provider\_category**<br>_optional_ | The category of the provider | string |
| **provider\_name**<br>_optional_ | The name of the provider | string |

**mapped\_user\_data**

| Name | Description | Schema |
| --- | --- | --- |
| **avatar**<br>_optional_ | User avatar picture link | string |
| **email**<br>_optional_ | User email | string |
| **email\_verified**<br>_optional_ | User email verified | boolean |
| **family\_name**<br>_optional_ | User family name | string |
| **given\_name**<br>_optional_ | User given name | string |
| **groups**<br>_optional_ | The names of the user groups | < string > array |
| **name**<br>_optional_ | User name | string |
| **user\_id**<br>_optional_ | User ID | string |

- [POST /login.add\_whitelist\_entries](https://clear.ml/docs/latest/docs/references/enterprise/login/#post-loginadd_whitelist_entries)
- [POST /login.finish\_sso\_callback](https://clear.ml/docs/latest/docs/references/enterprise/login/#post-loginfinish_sso_callback)
- [POST /login.get\_settings](https://clear.ml/docs/latest/docs/references/enterprise/login/#post-loginget_settings)
- [POST /login.get\_whitelist](https://clear.ml/docs/latest/docs/references/enterprise/login/#post-loginget_whitelist)
- [POST /login.logout](https://clear.ml/docs/latest/docs/references/enterprise/login/#post-loginlogout)
- [POST /login.remove\_whitelist\_entries](https://clear.ml/docs/latest/docs/references/enterprise/login/#post-loginremove_whitelist_entries)
- [POST /login.set\_domains](https://clear.ml/docs/latest/docs/references/enterprise/login/#post-loginset_domains)
- [POST /login.signup\_user](https://clear.ml/docs/latest/docs/references/enterprise/login/#post-loginsignup_user)
- [POST /login.sso\_authorize](https://clear.ml/docs/latest/docs/references/enterprise/login/#post-loginsso_authorize)
- [POST /login.sso\_callback](https://clear.ml/docs/latest/docs/references/enterprise/login/#post-loginsso_callback)
- [POST /login.sso\_callback\_duo](https://clear.ml/docs/latest/docs/references/enterprise/login/#post-loginsso_callback_duo)
- [POST /login.sso\_callback\_google\_saml](https://clear.ml/docs/latest/docs/references/enterprise/login/#post-loginsso_callback_google_saml)
- [POST /login.sso\_callback\_google\_saml\_support](https://clear.ml/docs/latest/docs/references/enterprise/login/#post-loginsso_callback_google_saml_support)
- [POST /login.sso\_callback\_jumpcloudsaml](https://clear.ml/docs/latest/docs/references/enterprise/login/#post-loginsso_callback_jumpcloudsaml)
- [POST /login.sso\_callback\_keycloak](https://clear.ml/docs/latest/docs/references/enterprise/login/#post-loginsso_callback_keycloak)
- [POST /login.sso\_callback\_microsoft\_ad](https://clear.ml/docs/latest/docs/references/enterprise/login/#post-loginsso_callback_microsoft_ad)
- [POST /login.sso\_callback\_saml](https://clear.ml/docs/latest/docs/references/enterprise/login/#post-loginsso_callback_saml)
- [POST /login.supported\_modes](https://clear.ml/docs/latest/docs/references/enterprise/login/#post-loginsupported_modes)
- [POST /login.test\_sso\_callback](https://clear.ml/docs/latest/docs/references/enterprise/login/#post-logintest_sso_callback)