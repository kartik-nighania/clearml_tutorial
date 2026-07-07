---
url: "https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_google_oauth/"
title: "Google OAuth | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_google_oauth/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

This guide explains how to configure Google as an OAuth provider for ClearML Single Sign-On (SSO).

Configuration requires two steps:

1. Register and Configure the ClearML application in Google
2. Identity service configuration in the ClearML Server

## Configure Google as IdP [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_google_oauth/\#configure-google-as-idp "Direct link to Configure Google as IdP")

1. In the [Google Cloud Console](https://console.cloud.google.com/), go to the **APIs & Services** **>** **Credentials section** (`https://console.cloud.google.com/apis/credentials?project=\<project-id\>`)

2. Click **Create credentials** \> **OAuth Client ID**
   - Application type: Web application
   - Authorized redirect URIs: Add `<clearml_webapp_address>/callback_google`
   - Note the Client ID and Client Secret, they will be used when configuring the ClearML Server.

## Configure ClearML Server [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_google_oauth/\#configure-clearml-server "Direct link to Configure ClearML Server")

1. Define the following environment variables in your secret manager or runtime environment:
   - `GOOGLE_AUTH_CLIENT_ID`
   - `GOOGLE_AUTH_CLIENT_SECRET`
2. Set the following environment variables for the `apiserver`:
   - `CLEARML__secure__login__sso__oauth_client__google__client_id="${GOOGLE_AUTH_CLIENT_ID}"`
   - `CLEARML__secure__login__sso__oauth_client__google__client_secret="${GOOGLE_AUTH_CLIENT_SECRET}"`
3. To allow the identity provider to automatically create new users in ClearML without requiring them to be whitelisted
in advance, set the following environment variable:





```text
CLEARML__secure__login__sso__oauth_client__google__default_company="<company_id>"
```


- [Configure Google as IdP](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_google_oauth/#configure-google-as-idp)
- [Configure ClearML Server](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_google_oauth/#configure-clearml-server)