---
url: "https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_okta_oauth/"
title: "Okta OAuth | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_okta_oauth/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

This guide explains how to configure **Okta** as an OAuth provider for ClearML Single Sign-On (SSO).

Configuration requires two steps:

1. Register and Configure the ClearML application in Okta
2. Identity service configuration in the ClearML Server

## Configure Okta [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_okta_oauth/\#configure-okta "Direct link to Configure Okta")

1. Register the ClearML Okta app with the callback URL: `<clearml_webapp_address>/callback_okta`

2. Make sure that the following claims are configured to be returned: "sub", "email", "name", "email\_verified"

3. Make sure that the relevant users are allowed under the ClearML Okta app configuration

4. Send the "client\_id", "client\_secret", "authorize\_url" and "access\_token\_url". These can be obtained by accessing
`https://${OktaDomain}/oauth2/${authorizationServerId}/.well-known/openid-configuration` and retrieving "authorization\_endpoint" and "token\_endpoint"


## Configure ClearML Server [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_okta_oauth/\#configure-clearml-server "Direct link to Configure ClearML Server")

1. Define the following environment variables in your secret manager or runtime environment:
   - `OKTA_AUTH_CLIENT_ID`
   - `OKTA_AUTH_CLIENT_SECRET`
2. Define the following environment variables:
   - `CLEARML__services__login__sso__oauth_client__okta__base_url=https://${yourOktaDomain}/oauth2/${authorizationServerId}/`
   - `CLEARML__services__login__sso__oauth_client__okta__authorize_url=<authorization endpoint>`
   - `CLEARML__services__login__sso__oauth_client__okta__access_token_url=<token endpoint>`
   - `CLEARML__secure__login__sso__oauth_client__okta__client_id="${OKTA_AUTH_CLIENT_ID}"`
   - `CLEARML__secure__login__sso__oauth_client__okta__client_secret="${OKTA_AUTH_CLIENT_SECRET}"`

- [Configure Okta](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_okta_oauth/#configure-okta)
- [Configure ClearML Server](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_okta_oauth/#configure-clearml-server)