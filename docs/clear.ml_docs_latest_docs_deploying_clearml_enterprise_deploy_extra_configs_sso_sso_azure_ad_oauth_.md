---
url: "https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_azure_ad_oauth/"
title: "Azure AD OAuth | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_azure_ad_oauth/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

This guide explains how to configure Azure Active Directory (Azure AD) as an OAuth provider for ClearML Single Sign-On (SSO).

Configuration requires two steps:

1. Register and Configure the ClearML application in Azure AD
2. Identity service configuration in the ClearML Server

## Configure Azure AD [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_azure_ad_oauth/\#configure-azure-ad "Direct link to Configure Azure AD")

1. Register the ClearML app with the redirect URI: `<clearml_webapp_address>/callback_azure_ad`
2. Select **Access tokens** to be returned from the authorization endpoint, and make sure that following claims are
returned in the access tokens: `email`, `preferred_username`, `upn`
3. Add client secret for the app and save the following app info:
   - Client ID
   - Client Secret
   - OAuth 2.0 authorization endpoint (v2)
   - OAuth 2.0 token endpoint (v2)

## Configure ClearML Server [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_azure_ad_oauth/\#configure-clearml-server "Direct link to Configure ClearML Server")

1. Define the following environment variables in your secret manager or runtime environment:
   - `AD_AUTH_CLIENT_ID`
   - `AD_AUTH_CLIENT_SECRET`
2. Set the following environment variables for the `apiserver`:
   - `CLEARML__services__login__sso__oauth_client__azure_ad__authorize_url=<authorization endpoint>`
   - `CLEARML__services__login__sso__oauth_client__azure_ad__access_token_url=<token endpoint>`
   - `CLEARML__secure__login__sso__oauth_client__azure_ad__client_id="${AD_AUTH_CLIENT_ID}"`
   - `CLEARML__secure__login__sso__oauth_client__azure_ad__client_secret="${AD_AUTH_CLIENT_SECRET}"`

To allow the identity provider to automatically create new users in ClearML without requiring them to be whitelisted in
advance, set the following environment variable:

```text
CLEARML__secure__login__sso__oauth_client__ad_oauth__default_company=${DEFAULT_COMPANY:?err}
```

- [Configure Azure AD](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_azure_ad_oauth/#configure-azure-ad)
- [Configure ClearML Server](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_azure_ad_oauth/#configure-clearml-server)