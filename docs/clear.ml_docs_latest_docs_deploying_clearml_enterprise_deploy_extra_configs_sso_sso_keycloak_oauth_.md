---
url: "https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_keycloak_oauth/"
title: "Keycloak OAuth | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_keycloak_oauth/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

This guide explains how to configure Keycloak as an OAuth identity provider for ClearML Single Sign-On (SSO):

1. Register ClearML as a client in Keycloak
2. Ensure required claims (email, username, user ID) are returned
3. Provide client credentials and OAuth endpoints to ClearML Server

## Configure Keycloak [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_keycloak_oauth/\#configure-keycloak "Direct link to Configure Keycloak")

1. Register ClearML app with the callback URL: `<clearml_webapp_address>/callback_keycloak`

2. Make sure the following claims are returned:
   - `user_id`
   - `email`
   - `user name`
3. Save the following values, which will be used when configuring ClearML Server:
   - `client_id`
   - `client_secret`
   - `Auth url`
   - `Access token url`

## Configure ClearML Server [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_keycloak_oauth/\#configure-clearml-server "Direct link to Configure ClearML Server")

Set the following environment variables for the `apiserver`:

- KeyCloak Base URL: `CLEARML__services__login__sso__oauth_client__keycloak__base_url=<base url>` (Use the start of the token or authorization endpoint, usually the part just before `protocol/openid-connect/...`)
- KeyCloak Authorization Endpoint: `CLEARML__services__login__sso__oauth_client__keycloak__authorize_url=<authorization endpoint>`
- KeyCloak Access Token Endpoint: `CLEARML__services__login__sso__oauth_client__keycloak__access_token_url=<token endpoint>`
- KeyCloak Client ID: `CLEARML__secure__login__sso__oauth_client__keycloak__client_id="${KEYCLOAK_AUTH_CLIENT_ID}"`
- KeyCloak Client Secret: `CLEARML__secure__login__sso__oauth_client__keycloak__client_secret="${KEYCLOAK_AUTH_CLIENT_SECRET}"`
- KeyCloak IdP Logout Redirect - When logging out of the ClearML UI, this redirects the user to the Keycloak logout page: `CLEARML__services__login__sso__oauth_client__keycloak__idp_logout=true`
- Username Claim Override - By default, ClearML retrieves the Keycloak username under the `name` claim. Some Keycloak deployments
return the username under `preferred_username`. Use this variable to specify which claim contains the username: `CLEARML__services__login__sso__oauth_client__keycloak__claims__name=preferred_username`
- Default Company - Allows the identity provider to automatically create new users in ClearML without requiring them to be whitelisted in advance: `CLEARML__secure__login__sso__oauth_client__keycloak__default_company="<company_id>"`

## User Group Integration [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_keycloak_oauth/\#user-group-integration "Direct link to User Group Integration")

ClearML can sync group membership from Keycloak. For each Keycloak group you want to sync user membership with, manually
create a [user group](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_users#user-groups) with the same name in ClearML.

### In Keycloak [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_keycloak_oauth/\#in-keycloak "Direct link to In Keycloak")

When configuring the Open ID client for ClearML:

1. Navigate to the **Client Scopes** tab.
2. Click on the first row `<clearml client>-dedicated`
3. Click **Add Mapper** \> **By configuration** \> **Group membership**
4. In the opened dialog, configure the mapper:
   - Name: `groups`
   - Token claim name: `groups`
   - Uncheck the **Full group path**
5. Save the mapper.
6. Validate the token:
1. Go to **Client Details** \> **Client scope** \> **Evaluate**
2. Select a user with any group membership
3. Navigate to **Generated ID Token** and **Generated User Info**.
4. Inspect that in both cases you can see the group claims in the displayed user data.

### In ClearML Server [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_keycloak_oauth/\#in-clearml-server "Direct link to In ClearML Server")

Set the following environment variables to the `apiserver`:

- `CLEARML__services__login__sso__oauth_client__keycloak__groups__enabled=true`
- `CLEARML__services__login__sso__oauth_client__keycloak__groups__claim=groups`

#### Setting ClearML Administrators [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_keycloak_oauth/\#setting-clearml-administrators "Direct link to Setting ClearML Administrators")

You can designate ClearML users as administrators either by Keycloak [group association](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_keycloak_oauth/#setting-administrators-by-group-association) or by [role association](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_keycloak_oauth/#setting-administrator-by-user-role-association).

##### Setting Administrators by Group Association [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_keycloak_oauth/\#setting-administrators-by-group-association "Direct link to Setting Administrators by Group Association")

If you want the members of the particular Keycloak group to be ClearML admins, set the following environment variable
(the Keycloak group does not need to exist in ClearML):

```text
CLEARML__services__login__sso__oauth_client__keycloak__groups__admins=["<the name of admin group from Keycloak>"]
```

##### Setting Administrator by User Role Association [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_keycloak_oauth/\#setting-administrator-by-user-role-association "Direct link to Setting Administrator by User Role Association")

- To sync the admin role from Keycloak into ClearML, configure the following in Keycloak:
  - Assign the user an admin role
  - In the **Client Scopes** tab, make sure that `roles` claim is included in the access token or `userinfo` token
  - To use a custom group name for designating the admin role, set the following environment variable: `CLEARML__services__login__sso__oauth_client__keycloak__admin_role=<admin role name>`
- To manage ClearML user roles independently of Keycloak, either make sure that user roles are not returned in the
auth token/userinfo endpoint or set the following environment variable: `CLEARML__services__login__sso__oauth_client__keycloak__admin_role=`


#### Restrict User Signup [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_keycloak_oauth/\#restrict-user-signup "Direct link to Restrict User Signup")

To restrict login only to users whose Keycloak groups exist in ClearML, set the following environment variable:

```text
CLEARML__services__login__sso__oauth_client__keycloak__groups__prohibit_user_signup_if_not_in_group=true
```

## Additional Customizations [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_keycloak_oauth/\#additional-customizations "Direct link to Additional Customizations")

### KeyCloak Session Logout [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_keycloak_oauth/\#keycloak-session-logout "Direct link to KeyCloak Session Logout")

To auto logout a user from the Keycloak provider when the user logs out of ClearML, set the following environment variable:

```text
CLEARML__services__login__sso__oauth_client__keycloak__idp_logout=true
```

### User Info Source [​](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_keycloak_oauth/\#user-info-source "Direct link to User Info Source")

By default, user info is taken from the access token. To return the user info through the OAuth `userinfo` endpoint instead,
set the following environment variable:

```text
CLEARML__services__login__sso__oauth_client__keycloak__get_info_from_access_token=false
```

- [Configure Keycloak](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_keycloak_oauth/#configure-keycloak)
- [Configure ClearML Server](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_keycloak_oauth/#configure-clearml-server)
- [User Group Integration](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_keycloak_oauth/#user-group-integration)
  - [In Keycloak](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_keycloak_oauth/#in-keycloak)
  - [In ClearML Server](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_keycloak_oauth/#in-clearml-server)
- [Additional Customizations](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_keycloak_oauth/#additional-customizations)
  - [KeyCloak Session Logout](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_keycloak_oauth/#keycloak-session-logout)
  - [User Info Source](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/extra_configs/sso/sso_keycloak_oauth/#user-info-source)