---
url: "https://clear.ml/docs/latest/docs/references/enterprise/sso/"
title: "sso | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/enterprise/sso/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

### POST /sso.delete\_provider\_configurations [​](https://clear.ml/docs/latest/docs/references/enterprise/sso/\#post-ssodelete_provider_configurations "Direct link to POST /sso.delete_provider_configurations")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/sso/\#description "Direct link to Description")

Internal. Delete provider configurations by their IDs

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/sso/\#parameters "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/sso/#sso-delete_provider_configurations-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **company**<br>_optional_ | Can be specified by system users only | string |
| **ids**<br>_optional_ | IDs of configurations to delete | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/sso/\#responses "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/sso/#sso-delete_provider_configurations-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **deleted**<br>_optional_ | The amount of deleted configurations | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/sso/\#security "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /sso.download\_saml\_sp\_metadata [​](https://clear.ml/docs/latest/docs/references/enterprise/sso/\#post-ssodownload_saml_sp_metadata "Direct link to POST /sso.download_saml_sp_metadata")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/sso/\#description-1 "Direct link to Description")

Internal. Download SAML SP metadata

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/sso/\#parameters-1 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/sso/#sso-download_saml_sp_metadata-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **configuration**<br>_required_ | configuration | object |
| **provider**<br>_required_ | Provider ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/sso/\#responses-1 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/sso/\#security-1 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /sso.get\_oidc\_provider\_data\_from\_well\_known\_url [​](https://clear.ml/docs/latest/docs/references/enterprise/sso/\#post-ssoget_oidc_provider_data_from_well_known_url "Direct link to POST /sso.get_oidc_provider_data_from_well_known_url")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/sso/\#description-2 "Direct link to Description")

Internal. Retrieve endpoints data from well know urls

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/sso/\#parameters-2 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/sso/#sso-get_oidc_provider_data_from_well_known_url-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **url**<br>_required_ | The well known url to retrieve data from | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/sso/\#responses-2 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/sso/#sso-get_oidc_provider_data_from_well_known_url-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **authorization\_endpoint**<br>_optional_ | Url of the authorization endpoint | string |
| **end\_session\_endpoint**<br>_optional_ | Url of end session (logout) endpoint | string |
| **jwks\_uri**<br>_optional_ | Url to download the signing key | string |
| **revocation\_endpoint**<br>_optional_ | Url of token revokation endpoint | string |
| **token\_endpoint**<br>_optional_ | Url of the token endpoint | string |
| **userinfo\_endpoint**<br>_optional_ | Url of user info endpoint | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/sso/\#security-2 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /sso.get\_provider\_configuration\_template [​](https://clear.ml/docs/latest/docs/references/enterprise/sso/\#post-ssoget_provider_configuration_template "Direct link to POST /sso.get_provider_configuration_template")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/sso/\#description-3 "Direct link to Description")

Internal. Return the new or existing configuration template for the SSO

provider

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/sso/\#parameters-3 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/sso/#sso-get_provider_configuration_template-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **company**<br>_optional_ | Can be specified by system users only | string |
| **id**<br>_optional_ | Configuration ID. If specified then the existing cofiguration is returned. If <br>not specified then the new configuration is returned. For the new configuration <br>provider should be specified | string |
| **provider**<br>_optional_ | Provider ID | string |
| **well\_known\_url**<br>_optional_ | Well known url from the IDP server. Applicable to oidc providers only | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/sso/\#responses-3 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/sso/#sso-get_provider_configuration_template-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **config\_template**<br>_optional_ | Configuration form template | object |
| **error**<br>_optional_ | Well know url error | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/sso/\#security-3 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /sso.get\_provider\_configurations [​](https://clear.ml/docs/latest/docs/references/enterprise/sso/\#post-ssoget_provider_configurations "Direct link to POST /sso.get_provider_configurations")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/sso/\#description-4 "Direct link to Description")

Internal. Get the list of supported provider configurations

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/sso/\#parameters-4 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/sso/#sso-get_provider_configurations-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **company**<br>_optional_ | Can be specified by system users only | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/sso/\#responses-4 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/sso/#sso-get_provider_configurations-response-200) |

**Response 200**

| Name | Schema |
| --- | --- |
| **configurations**<br>_optional_ | < [sso.configuration](https://clear.ml/docs/latest/docs/references/enterprise/definitions#ssoconfiguration) \> array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/sso/\#security-4 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /sso.get\_supported\_providers [​](https://clear.ml/docs/latest/docs/references/enterprise/sso/\#post-ssoget_supported_providers "Direct link to POST /sso.get_supported_providers")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/sso/\#description-5 "Direct link to Description")

Internal. Return supported provider types and their display names

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/sso/\#parameters-5 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/sso/\#responses-5 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/sso/#sso-get_supported_providers-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **providers**<br>_optional_ | The list of supported provider types | < [sso.provider](https://clear.ml/docs/latest/docs/references/enterprise/definitions#ssoprovider) \> array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/sso/\#security-5 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /sso.save\_provider\_configuration [​](https://clear.ml/docs/latest/docs/references/enterprise/sso/\#post-ssosave_provider_configuration "Direct link to POST /sso.save_provider_configuration")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/sso/\#description-6 "Direct link to Description")

Internal. Save provider configuration

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/sso/\#parameters-6 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/sso/#sso-save_provider_configuration-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **company**<br>_optional_ | Can be specified by system users only | string |
| **configuration**<br>_required_ | configuration | object |
| **provider**<br>_required_ | Provider ID | string |
| **support\_provider**<br>_optional_ | Support provider. Can be set by system user only | boolean |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/sso/\#responses-6 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/sso/\#security-6 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /sso.set\_provider\_configurations\_active [​](https://clear.ml/docs/latest/docs/references/enterprise/sso/\#post-ssoset_provider_configurations_active "Direct link to POST /sso.set_provider_configurations_active")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/sso/\#description-7 "Direct link to Description")

Internal. Delete provider configurations by their IDs

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/sso/\#parameters-7 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/sso/#sso-set_provider_configurations_active-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **active**<br>_optional_ | If set to 'true' then the configurations are activated. Otherwise deactivated <br>**Default** : `true` | boolean |
| **company**<br>_optional_ | Can be specified by system users only | string |
| **ids**<br>_optional_ | IDs of configurations to delete | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/sso/\#responses-7 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/sso/#sso-set_provider_configurations_active-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **updated**<br>_optional_ | The amount of updated configurations | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/sso/\#security-7 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

### POST /sso.test\_provider\_configuration [​](https://clear.ml/docs/latest/docs/references/enterprise/sso/\#post-ssotest_provider_configuration "Direct link to POST /sso.test_provider_configuration")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/sso/\#description-8 "Direct link to Description")

Internal. Validates provider configuration and returns the url for sso login

test

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/sso/\#parameters-8 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/sso/#sso-test_provider_configuration-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **configuration**<br>_required_ | configuration | object |
| **provider**<br>_required_ | Provider ID | string |
| **state**<br>_optional_ | ASCII base64 encoded application state | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/sso/\#responses-8 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/sso/#sso-test_provider_configuration-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **redirect\_url**<br>_optional_ | Provider redirect URL | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/sso/\#security-8 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root,admin |

- [POST /sso.delete\_provider\_configurations](https://clear.ml/docs/latest/docs/references/enterprise/sso/#post-ssodelete_provider_configurations)
- [POST /sso.download\_saml\_sp\_metadata](https://clear.ml/docs/latest/docs/references/enterprise/sso/#post-ssodownload_saml_sp_metadata)
- [POST /sso.get\_oidc\_provider\_data\_from\_well\_known\_url](https://clear.ml/docs/latest/docs/references/enterprise/sso/#post-ssoget_oidc_provider_data_from_well_known_url)
- [POST /sso.get\_provider\_configuration\_template](https://clear.ml/docs/latest/docs/references/enterprise/sso/#post-ssoget_provider_configuration_template)
- [POST /sso.get\_provider\_configurations](https://clear.ml/docs/latest/docs/references/enterprise/sso/#post-ssoget_provider_configurations)
- [POST /sso.get\_supported\_providers](https://clear.ml/docs/latest/docs/references/enterprise/sso/#post-ssoget_supported_providers)
- [POST /sso.save\_provider\_configuration](https://clear.ml/docs/latest/docs/references/enterprise/sso/#post-ssosave_provider_configuration)
- [POST /sso.set\_provider\_configurations\_active](https://clear.ml/docs/latest/docs/references/enterprise/sso/#post-ssoset_provider_configurations_active)
- [POST /sso.test\_provider\_configuration](https://clear.ml/docs/latest/docs/references/enterprise/sso/#post-ssotest_provider_configuration)