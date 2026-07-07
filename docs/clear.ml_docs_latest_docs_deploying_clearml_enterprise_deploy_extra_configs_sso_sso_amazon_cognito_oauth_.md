---
url: "https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_amazon_cognito_oauth/"
title: "Amazon Cognito OAuth | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_amazon_cognito_oauth/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

This guide explains how to configure Amazon Cognito as an OAuth provider for ClearML Single Sign-On (SSO).

Configuration requires two steps:

1. Register and Configure the ClearML application in Amazon Cognito
2. Identity service configuration in the ClearML Server

## Configure Amazon Cognito [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_amazon_cognito_oauth/\#configure-amazon-cognito "Direct link to Configure Amazon Cognito")

1. Select a user pool in Amazon Cognito. Make sure the pool includes the required user attributes "email" and "preferred\_username"
2. In the user pool **App Integration** section, create an app client for ClearML with the following properties:

   - App type - Confidential client
   - Client secret - Generate a client secret
   - Hosted UI Settings > Allowed callback URLs > add the URL `<clearml_webapp_address>/callback_cognito`
   - OAuth 2.0 grant types - Authorization code grant
   - OpenID Connect scopes - OpenID, Profile, Email

## Configure ClearML Server [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_amazon_cognito_oauth/\#configure-clearml-server "Direct link to Configure ClearML Server")

1. Define the following environment variables in your secret manager or runtime environment:
   - `COGNITO_AUTH_CLIENT_ID`
   - `COGNITO_AUTH_CLIENT_SECRET`
2. Set the following environment variables for the `apiserver`:

   - `CLEARML__services__login__sso__oauth_client__cognito__authorize_url=<authorization endpoint>` (Authorization
     endpoint format should be `<cognito_domain_of_the_pool>/oauth2/authorize`)
   - `CLEARML__services__login__sso__oauth_client__cognito__access_token_url=<token endpoint>` (Token endpoint format
     should be `<cognito_domain_of_the_pool>/oauth2/token`)
   - `CLEARML__secure__login__sso__oauth_client__cognito__client_id="${COGNITO_AUTH_CLIENT_ID}"`
   - `CLEARML__secure__login__sso__oauth_client__cognito__client_secret="${COGNITO_AUTH_CLIENT_SECRET}"`

### External Identity Provider [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_amazon_cognito_oauth/\#external-identity-provider "Direct link to External Identity Provider")

If the user pool relies on an external identity provider, add the following environment
variable:

```text
CLEARML__services__login__sso__oauth_client__cognito__identity_provider=<external_idp_name_as_defined_in_the_user_pool>
```

### Default Company Assignment [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_amazon_cognito_oauth/\#default-company-assignment "Direct link to Default Company Assignment")

To allow the identity provider to automatically create new users in ClearML without requiring them to be whitelisted in
advance, set the following environment variable:

```text
CLEARML__secure__login__sso__oauth_client__cognito__default_company="<company_id>"
```

### Custom Display Name [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_amazon_cognito_oauth/\#custom-display-name "Direct link to Custom Display Name")

To customize the provider’s login option appears in the ClearML login screen:

```text
CLEARML__services__login__sso__oauth_client__cognito__display_name="New display name"
```

- [Configure Amazon Cognito](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_amazon_cognito_oauth/#configure-amazon-cognito)
- [Configure ClearML Server](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_amazon_cognito_oauth/#configure-clearml-server)
  - [External Identity Provider](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_amazon_cognito_oauth/#external-identity-provider)
  - [Default Company Assignment](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_amazon_cognito_oauth/#default-company-assignment)
  - [Custom Display Name](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_amazon_cognito_oauth/#custom-display-name)