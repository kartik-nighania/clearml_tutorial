---
url: "https://clear.ml/docs/latest/docs/references/api/login/"
title: "login | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/api/login/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

### POST /login.logout [​](https://clear.ml/docs/latest/docs/references/api/login/\#post-loginlogout "Direct link to POST /login.logout")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/login/\#description "Direct link to Description")

Logout (including SSO, if used))

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/login/\#parameters "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/login/\#responses "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

### POST /login.supported\_modes [​](https://clear.ml/docs/latest/docs/references/api/login/\#post-loginsupported_modes "Direct link to POST /login.supported_modes")

#### Description [​](https://clear.ml/docs/latest/docs/references/api/login/\#description-1 "Direct link to Description")

Return supported login modes.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/api/login/\#parameters-1 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/api/login/\#responses-1 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/api/login/#login-supported_modes-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **authenticated**<br>_optional_ | Is user authenticated | boolean |
| **basic**<br>_optional_ |  | [basic](https://clear.ml/docs/latest/docs/references/api/login/#login-supported_modes-post-basic) |
| **server\_errors**<br>_optional_ | Server initialization errors | [server\_errors](https://clear.ml/docs/latest/docs/references/api/login/#login-supported_modes-post-server_errors) |
| **sso**<br>_optional_ | SSO authentication providers | < string, string > map |
| **sso\_providers**<br>_optional_ | The list of SSO authentication providers | < object > array |

**basic**

| Name | Description | Schema |
| --- | --- | --- |
| **enabled**<br>_optional_ | Basic aothentication (fixed users mode) mode enabled | boolean |
| **guest**<br>_optional_ |  | [guest](https://clear.ml/docs/latest/docs/references/api/login/#login-supported_modes-post-basic-guest) |

**guest**

| Name | Description | Schema |
| --- | --- | --- |
| **enabled**<br>_optional_ | Basic aothentication guest mode enabled | boolean |
| **name**<br>_optional_ | Guest name | string |
| **password**<br>_optional_ | Guest password | string |
| **username**<br>_optional_ | Guest username | string |

**server\_errors**

| Name | Description | Schema |
| --- | --- | --- |
| **es\_connection\_error**<br>_optional_ | Indicate an error communicating to Elasticsearch | boolean |
| **missed\_es\_upgrade**<br>_optional_ | Indicate that Elasticsearch database was not upgraded from version 5 | boolean |

- [POST /login.logout](https://clear.ml/docs/latest/docs/references/api/login/#post-loginlogout)
- [POST /login.supported\_modes](https://clear.ml/docs/latest/docs/references/api/login/#post-loginsupported_modes)