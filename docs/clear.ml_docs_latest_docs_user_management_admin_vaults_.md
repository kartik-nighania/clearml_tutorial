---
url: "https://clear.ml/docs/latest/docs/user_management/admin_vaults/"
title: "Administrator Vaults | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/user_management/admin_vaults/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

Enterprise Feature

Administrator Vaults are available under the ClearML Enterprise plan.

Administrators can set configuration for users, [service accounts](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_users#service-accounts),
and [user groups](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_users#user-groups) within a ClearML workspace by using central configuration
stores--or Administrator Vaults.

Administrators can define multiple [configuration vaults](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_profile#configuration-vault) which will
each be applied to their designated [user groups](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_users#user-groups), allowing for custom settings to be centrally managed.
Configuration vault values are applied to tasks run by members of the designated user groups. When applied, the configuration
vaults extend and/or override entries in the local ClearML [configuration file](https://clear.ml/docs/latest/docs/configs/clearml_conf)
where a ClearML task is executed.

Administrator vaults can be managed using both the [UI](https://clear.ml/docs/latest/docs/user_management/admin_vaults/#managing-vaults-via-the-clearml-ui) and [REST API](https://clear.ml/docs/latest/docs/user_management/admin_vaults/#managing-vaults-via-the-rest-api).

## Managing Vaults via the ClearML UI [​](https://clear.ml/docs/latest/docs/user_management/admin_vaults/\#managing-vaults-via-the-clearml-ui "Direct link to Managing Vaults via the ClearML UI")

Manage administrator vaults in ClearML UI, under **SETTINGS > Administrator Vaults**. Through this interface, administrators can:

- **View** and **enable/disable** vaults
- **Create** vaults
- **Edit** vault contents.

For more information see [Administrator Vaults](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_admin_vaults) settings page.

## Managing Vaults via the REST API [​](https://clear.ml/docs/latest/docs/user_management/admin_vaults/\#managing-vaults-via-the-rest-api "Direct link to Managing Vaults via the REST API")

Administrator Vaults can be managed programmatically using the ClearML REST API.

### ClearML Server [​](https://clear.ml/docs/latest/docs/user_management/admin_vaults/\#clearml-server "Direct link to ClearML Server")

API calls should be made to the API Server component, which, by default, is available in port 8008 if using HTTP, under
the subdomain `https://api.<clearml-server-domain>` or using the API path with the Web Server (e.g. `https://<clearml-server-domain>/api`).

From this point on, the server address will be referred to as `CLEARML_SERVER`.

### Authentication [​](https://clear.ml/docs/latest/docs/user_management/admin_vaults/\#authentication "Direct link to Authentication")

To authenticate REST API calls, you need ClearML Server credentials. Specifically, to manage organization vaults, you must use Admin User credentials. In the example below, `CLEARML_ACCESS_KEY` and `CLEARML_SECRET_KEY` refer to ClearML Admin User credentials.

An API token is required for all API calls, and should be generated using the admin credentials.

#### Generating an API Token [​](https://clear.ml/docs/latest/docs/user_management/admin_vaults/\#generating-an-api-token "Direct link to Generating an API Token")

To generate an API Token, use the following command:

```text
export CLEARML_API_TOKEN=$(curl -s -u "$CLEARML_ACCESS_KEY:$CLEARML_SECRET_KEY" $CLEARML_SERVER/auth.login | jq -r '.data.token')
```

All subsequent API calls can use this token by providing the authorization header with a bearer token:

```text
curl -s -H "Authorization: Bearer ${CLEARML_API_TOKEN}" <clearml-server>/...
```

### Administrator Vault API [​](https://clear.ml/docs/latest/docs/user_management/admin_vaults/\#administrator-vault-api "Direct link to Administrator Vault API")

#### List Existing Vaults [​](https://clear.ml/docs/latest/docs/user_management/admin_vaults/\#list-existing-vaults "Direct link to List Existing Vaults")

To list all existing vaults, use the following command:

```text
curl -s $CLEARML_SERVER/users.get_vaults -H "Authorization: Bearer $CLEARML_API_TOKEN"
```

The command returns a list of vaults in JSON format, under the `data` fields. For example:

```text
{

   "meta": {

       ...

   },

   "data": {

       "vaults": [\
\
           {\
\
               "data": "",\
\
               "description": "",\
\
               "enabled": true,\
\
               "format": "hocon",\
\
               "id": "<vault_ID>",\
\
               "scope": "user",\
\
               "type": "config"\
\
           }\
\
       ]

   }

}
```

This list also includes the admin user's personal vault defined using the ClearML UI interface in the **SETTINGS > Workspace**
section. This vault will appear as above, with the `user` value in the scope field. Administrator vaults use the ` group` scope.

#### Create a Vault [​](https://clear.ml/docs/latest/docs/user_management/admin_vaults/\#create-a-vault "Direct link to Create a Vault")

To create a new vault, use the following command:

```text
curl -s -XPUT $CLEARML_SERVER/users.add_or_update_vault \

-H "Authorization: Bearer $CLEARML_API_TOKEN" \

-H "Content-Type: application/json" \

--data-raw '{

   "group": "30795571-a470-4717-a80d-e8705fc776bf",

   "vault": {

       "scope": "group",

       "enabled": true,

       "data": "<vault configuration, same format as in clearml.conf>",

       "format": "hocon",

       "type": "config"

   }

}'
```

In the example above, the group ID `"30795571-a470-4717-a80d-e8705fc776bf"` refers to the Users group (to which all users
belong). You can define other groups in the [Users & Groups](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_users#user-groups)
settings page and create vaults for these specific groups.

The command returns the ID of the newly created vault. For example:

```text
{

   "meta": {

       ...

   },

   "data": {

       "vault": "ccc9bab1269542189ef088712436043f"

   }

}
```

#### Update a Vault [​](https://clear.ml/docs/latest/docs/user_management/admin_vaults/\#update-a-vault "Direct link to Update a Vault")

To update an existing vault, use the following command:

```text
curl -s -XPUT $CLEARML_SERVER/users.add_or_update_vault \

-H "Authorization: Bearer $CLEARML_API_TOKEN" \

-H "Content-Type: application/json" \

--data-raw '{

   "group": "30795571-a470-4717-a80d-e8705fc776bf",

   "vault": {

       "id": "<existing-vault-id>",

       "scope": "group",

       "enabled": true,

       "data": "<vault configuration, same format as in clearml.conf>",

       "format": "hocon",

       "type": "config"

   }

}'
```

Note that while this call is almost identical to the vault creation call, it includes a specific vault ID (`<existing-vault-id>`).

#### Delete a Vault [​](https://clear.ml/docs/latest/docs/user_management/admin_vaults/\#delete-a-vault "Direct link to Delete a Vault")

To delete an existing vault, use the following command:

```text
curl -s -XPUT $CLEARML_SERVER/users.delete_vaults \

-H "Authorization: Bearer $CLEARML_API_TOKEN" \

-H "Content-Type: application/json" \

--data-raw '{

   "vaults": ["<vault-id>"]

}'
```

Where `<vault-id>` is the ID of the vault to delete. Multiple vaults can be deleted by providing a list of IDs,
formatted as `"vaults": ["<vault-id-1>", "<vault-id-2>", ...]`.

note

Do not delete the user scope vault as it is managed by the UI.

The command returns output like this:

```text
{

   "meta": {

       ...

   },

   "data": {

       "deleted": 1

   }

}
```

- [Managing Vaults via the ClearML UI](https://clear.ml/docs/latest/docs/user_management/admin_vaults/#managing-vaults-via-the-clearml-ui)
- [Managing Vaults via the REST API](https://clear.ml/docs/latest/docs/user_management/admin_vaults/#managing-vaults-via-the-rest-api)
  - [ClearML Server](https://clear.ml/docs/latest/docs/user_management/admin_vaults/#clearml-server)
  - [Authentication](https://clear.ml/docs/latest/docs/user_management/admin_vaults/#authentication)
  - [Administrator Vault API](https://clear.ml/docs/latest/docs/user_management/admin_vaults/#administrator-vault-api)