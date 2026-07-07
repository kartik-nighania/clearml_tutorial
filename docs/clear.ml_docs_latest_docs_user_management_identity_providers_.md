---
url: "https://clear.ml/docs/latest/docs/user_management/identity_providers/"
title: "Identity Providers | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/user_management/identity_providers/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

Enterprise Feature

Identity provider integration is available under the ClearML Enterprise plan.

Administrators can seamlessly connect ClearML with their identity service providers to easily implement single sign-on
(SSO). Once an identity provider connection is configured and enabled, the option appears in your server login page.

In addition to authentication, ClearML can also retrieve user profile data and group membership details—facilitating user
provisioning and role assignment.

ClearML supports standard protocols and popular providers:

- OAuth
  - [Amazon Cognito](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_amazon_cognito_oauth)
  - [Azure AD](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_azure_ad_oauth)
  - [Google](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_google_oauth)
  - [Keycloak](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_keycloak_oauth)
  - [Microsoft AD](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_microsoft_ad_oauth)
  - [Ping Identity](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_ping_id_oauth)
  - [Okta](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_okta_oauth)
- SAML
  - [Duo](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_duo_saml)
  - [Google](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_google_saml)
  - [Microsoft AD and Azure AD](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_microsoft_ad_saml)
- [LDAP](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_ldap)

For a complete list of supported providers, see [Identity Providers](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_id_providers).