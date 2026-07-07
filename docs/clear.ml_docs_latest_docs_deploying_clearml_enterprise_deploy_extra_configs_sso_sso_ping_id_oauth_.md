---
url: "https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_ping_id_oauth/"
title: "Ping Identity OAuth | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_ping_id_oauth/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

This guide explains how to configure **Ping Identity** as an OAuth provider for ClearML Single Sign-On (SSO):

1. Register and Configure the ClearML application in Ping Identity
2. Identity service configuration in the ClearML Server
3. Optionally, map group membership and admin roles from Ping into ClearML.

## Configure Ping Identity [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_ping_id_oauth/\#configure-ping-identity "Direct link to Configure Ping Identity")

1. Register a new ClearML app with the callback URL: `<clearml_webapp_address>/callback_ping`

2. Select the following scopes:
   - `openid`
   - `profile`
   - `email`
3. Make sure that the claims representing `user_id`, `email`, and `username` are returned in the token

4. Note the Client ID, Client secret, Auth URL, and Access token URL. They will be used in the ClearML Server configuration


## Configure ClearML Server [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_ping_id_oauth/\#configure-clearml-server "Direct link to Configure ClearML Server")

1. Define the following environment variables in your secret manager or runtime environment:
   - `PING_AUTH_CLIENT_ID`
   - `PING_AUTH_CLIENT_SECRET`
2. Set the following environment variables for the `apiserver`:
   - `CLEARML__services__login__sso__oauth_client__ping__authorize_url=<authorization endpoint>`
   - `CLEARML__services__login__sso__oauth_client__ping__access_token_url=<token endpoint>`
   - `CLEARML__secure__login__sso__oauth_client__ping__client_id="${PING_AUTH_CLIENT_ID}"`
   - `CLEARML__secure__login__sso__oauth_client__ping__client_secret="${PING_AUTH_CLIENT_SECRET}"`
3. If you enabled the PKCE for the ClearML app in Ping Identity, add the following environment variables:
   - `CLEARML__services__login__sso__oauth_client__ping__code_challenge=true`
   - `CLEARML__services__login__sso__oauth_client__ping__code_challenge_method=S256`
4. To allow the identity provider to automatically create new users in ClearML without requiring them to be whitelisted
in advance, set the following environment variable:





```text
CLEARML__secure__login__sso__oauth_client__ping__default_company="<company_id>"
```

5. To troubleshoot the integration between Ping and ClearML, you can enable SSO debug information in ClearML server logs:





```text
CLEARML__services__login__sso__oauth_client__ping__debug=true`
```


### User Group Integration [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_ping_id_oauth/\#user-group-integration "Direct link to User Group Integration")

ClearML can sync user admin roles and group assignments from Ping.

#### In Ping Identity [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_ping_id_oauth/\#in-ping-identity "Direct link to In Ping Identity")

Make sure that group memberships are included in the SSO token.

#### In ClearML Server [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_ping_id_oauth/\#in-clearml-server "Direct link to In ClearML Server")

Set the following environment variables:

- `CLEARML__services__login__sso__oauth_client__ping__groups__enabled=true`
- `CLEARML__services__login__sso__oauth_client__ping__groups__claim=<the name of the groups claim as returned from Ping>`

note

ClearML Groups are not created automatically and must be manually created. The group name comparison between Ping and
ClearML is case-sensitive by default. To make it case-insensitive, set the following:

```text
CLEARML__services__login__sso__oauth_client__ping__groups__case_sensitive=false
```

##### Setting ClearML Administrators [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_ping_id_oauth/\#setting-clearml-administrators "Direct link to Setting ClearML Administrators")

If you want the members of a particular Ping group to be admins in ClearML, add the following environment variable (the Ping group
does not have to exist ClearML):

```text
CLEARML__services__login__sso__oauth_client__ping__groups__admins=["<the name of admin group from Ping>"]
```

##### Restrict User Signup [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_ping_id_oauth/\#restrict-user-signup "Direct link to Restrict User Signup")

To restrict log in only to users whose Ping groups exist in ClearML, set the following environment variable:

```text
CLEARML__services__login__sso__oauth_client__ping__groups__prohibit_user_signup_if_not_in_group=true
```

- [Configure Ping Identity](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_ping_id_oauth/#configure-ping-identity)
- [Configure ClearML Server](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_ping_id_oauth/#configure-clearml-server)
  - [User Group Integration](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_ping_id_oauth/#user-group-integration)