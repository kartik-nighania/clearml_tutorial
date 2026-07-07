---
url: "https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_profile/"
title: "User Settings | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_profile/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

In the **User Settings** section, manage your personal account details, configure system behavior, and set up
credentials for ClearML services.

## Profile [​](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_profile/\#profile "Direct link to Profile")

The profile tab presents user information.

**To edit the username:**

1. Hover over the username
2. Click ![Edit Pencil](https://clear.ml/docs/latest/icons/ico-edit.svg)
3. Change the name
4. Click ![Check Mark](https://clear.ml/docs/latest/icons/ico-save.svg) button

## Configuration [​](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_profile/\#configuration "Direct link to Configuration")

### Customizing UI Behavior [​](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_profile/\#customizing-ui-behavior "Direct link to Customizing UI Behavior")

Under **USER PREFERENCES**, users can set a few web UI options:

- **Show Hidden Projects** \- Show ClearML infrastructure projects alongside your own projects. Disabled by default. When
enabled, these projects are labeled with ![Hidden project](https://clear.ml/docs/latest/icons/ico-ghost.svg).

- **Don't show ClearML examples** \- Hide the preloaded ClearML example content (project, pipeline, dataset, etc.).

- **Disable HiDPI browser scale override** \- ClearML dynamically sets the browser scaling factor for an optimal page layout.
Disable for default desktop scale.

- **Don't show pro tips periodically** \- Stop showing ClearML usage tips on login. Disabled by default.

- **Block running user's scripts in the browser** \- Block any user and 3rd party scripts from running anywhere in the
WebApp. Note that if enabled, the WebApp will not display debug samples, [Hyper-Dataset frame previews](https://clear.ml/docs/latest/docs/hyperdatasets/previews),
and embedded resources in [reports](https://clear.ml/docs/latest/docs/webapp/webapp_reports).



note





Script blocking can be enforced by administrators through server-side configuration.


When set, the UI toggle is disabled and users cannot change the setting.

- **Hide specific container arguments** \- Specify which container environment variable values should be hidden in logs.
When printed, the variable values are replaced with `********`. By default, `CLEARML_API_SECRET_KEY`, `CLEARML_AGENT_GIT_PASS`,
`AWS_SECRET_ACCESS_KEY`, and `AZURE_STORAGE_KEY` values are redacted. To modify the hidden container argument list, click **Edit**.


Self-hosted ClearML Server

The self-hosted ClearML Server has an additional option to enable sharing anonymous telemetry data with the ClearML
engineering team.

### Browser Cloud Storage Access [​](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_profile/\#browser-cloud-storage-access "Direct link to Browser Cloud Storage Access")

Provide cloud storage access, so the browser will be able to display your cloud stored data, such as debug samples.

In the **Web App Cloud Access** section, enter the following credentials:

- **Bucket** \- The name of a Cloud bucket.
- **Key** \- The access key.
- **Secret / SAS** \- The secret key or shared access signature if required.
- **Token** \- For S3 services, session key for temporary credentials (if applicable).
- **AWS Region** \- The region for AWS S3.
- **Host (Endpoint)** \- The host for non-AWS S3 servers.

## Workspace [​](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_profile/\#workspace "Direct link to Workspace")

### Multiple Workspaces [​](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_profile/\#multiple-workspaces "Direct link to Multiple Workspaces")

ClearML Hosted Service Feature

Multiple workspaces are only available on the ClearML Hosted Service.

ClearML Hosted Service users can be members of multiple workspaces, which are listed under **WORKSPACE**.

To switch to another workspace, click on the **SWITCH TO WORKSPACE** button next to the name of the workspace you want
to switch to.

![Workspace configuration page](https://clear.ml/docs/latest/assets/images/settings_workspace_configuration-90f7f8653017c33fd55d6ef2426d9666.png#light-mode-only)![Workspace configuration page](https://clear.ml/docs/latest/assets/images/settings_workspace_configuration_dark-975502894bc6716e3b2b53a5f28f3776.png#dark-mode-only)

### ClearML API Credentials [​](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_profile/\#clearml-api-credentials "Direct link to ClearML API Credentials")

Generate ClearML credentials, made up of an access and secret key pair, and insert them into your [configuration file](https://clear.ml/docs/latest/docs/configs/clearml_conf)
or Jupyter Notebook to grant the ClearML SDK and the ClearML Agent API access to the server.

You can create credentials for any workspace that you are a member of.

**To create ClearML credentials:**

1. In **WORKSPACE**, expand the desired workspace's panel (self-deployed ClearML Server users have one workspace)

2. In **API Credentials**, click **\+ Create new credentials**

3. In the dialog that pops up, you can input a label for the new credentials


Credential Expiration

The ClearML Hosted Service and the ClearML Enterprise plan support setting an expiration period for API credentials.

The dialog displays new credentials, formatted as a ready-to-copy configuration file section (including server configuration
information).

![ClearML credentials](https://clear.ml/docs/latest/assets/images/settings_configuration_creation-62eca25dea434e650bf824020ee34892.png#light-mode-only)![ClearML credentials](https://clear.ml/docs/latest/assets/images/settings_configuration_creation_dark-a314373f6fb0b57cd59aefce20074dad.png#dark-mode-only)

You can edit the labels of credentials in your own workspace, or credentials that you created in other workspaces.

**To edit the credentials label:** hover over the desired credentials, and click ![Edit Pencil](https://clear.ml/docs/latest/icons/ico-edit.svg) .

You can revoke any credentials in your own workspace, or credentials that you created in other workspaces. Once revoked,
these credentials cannot be recovered.

**To revoke ClearML credentials:** hover over the desired credentials, and click ![Trash can](https://clear.ml/docs/latest/icons/ico-trash.svg) .

### AI Application Gateway Tokens [​](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_profile/\#ai-application-gateway-tokens "Direct link to AI Application Gateway Tokens")

Enterprise Feature

The AI Application Gateway is available under the ClearML Enterprise plan.

The [AI Application Gateway](https://clear.ml/docs/latest/docs/deploying_clearml/enterprise_deploy/appgw) enables external access to ClearML
tasks and applications. The gateway is configured with an
endpoint or external address (ingress), accessible from outside ClearML.

Generate tokens providing API access to the AI Application Gateway endpoints:

1. Click **Generate a Token**
2. Under `Label`, enter a descriptive name for the token
3. Under `Expiration`, enter the number of days the token should remain valid
4. Click `Generate`, which creates a token and copies it to your clipboard

The **AI Application Gateway Table** displays all tokens available to the user, and the following details:

- Token label
- Creation time
- Expiration time

To revoke a token, hover over the token's row and click ![Trash](https://clear.ml/docs/latest/icons/ico-trash.svg).

![AI App Gateway Token Table](https://clear.ml/docs/latest/assets/images/settings_token_management-62b9d1625a3ea78f48477d0b5336705e.png#light-mode-only)![AI App Gateway Token Table](https://clear.ml/docs/latest/assets/images/settings_token_management_dark-1e4780661d57893408616eedcffa1d65.png#dark-mode-only)

### Changing Your Workspace Name [​](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_profile/\#changing-your-workspace-name "Direct link to Changing Your Workspace Name")

To change the name of your own workspace, click **Edit workspace name**![Edit Pencil](https://clear.ml/docs/latest/icons/ico-edit.svg)
(under API credentials) **>** modify the name **>** click ![Check Mark](https://clear.ml/docs/latest/icons/ico-save.svg).

### Adding Users to Your Workspace [​](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_profile/\#adding-users-to-your-workspace "Direct link to Adding Users to Your Workspace")

To invite a user to your workspace, in the **MEMBERS** section:

1. Press the **INVITE USERS** button
2. Input the email in the dialog that pops up
3. Click **ADD**

A dialog box will appear with an invitation link to send to the invited users. Existing members will receive an in-app
notification informing them that they can join your workspace.

After inviting users, the page will redirect to the [Users & Groups](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_users) section, where the
pending invitations are displayed.

### Leaving a Workspace [​](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_profile/\#leaving-a-workspace "Direct link to Leaving a Workspace")

You can leave any workspace you've previously joined (except your personal workspace).

When leaving a workspace, you lose access to its resources (tasks, models, etc.) and your previously created access
credentials to that workspace are revoked. Tasks and associated artifacts that you logged to that workspace will remain
in that workspace. You can rejoin the workspace only if you are re-invited.

**To leave a workspace:**

1. In **WORKSPACE**, expand the desired workspace's panel
2. In **Members** **>** Click **LEAVE WORKSPACE**.

### Configuration Vault [​](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_profile/\#configuration-vault "Direct link to Configuration Vault")

Enterprise Feature

Configuration vaults are available under the ClearML Enterprise plan.

Use the configuration vault to store global ClearML configuration entries that can extend the ClearML [configuration file](https://clear.ml/docs/latest/docs/configs/clearml_conf)
of any ClearML Agents or the ClearML SDK running with your credentials. Productivity tip: Keep the vault disabled while
you edit your configuration, and enable it when the configuration is ready.

Vault entries will extend the configuration in the ClearML [configuration file](https://clear.ml/docs/latest/docs/configs/clearml_conf) if they don't
exist, and override values for those already present in the file.

Fill in values using any of ClearML supported configuration formats: HOCON / JSON / YAML.

**To edit vault contents:**

1. Click **EDIT** or double-click the vault box
2. Insert / edit the configurations in the vault
3. Press **OK**

**To apply vault contents:**

- Click the toggle atop the vault to enable / disable the configurations
- Once enabled, the configurations will be merged to the configuration file during ClearML and ClearML Agent usage

![Configuration vault](https://clear.ml/docs/latest/assets/images/settings_configuration_vault-1d9819e35164ed3f5383cd5c6e10f7d3.png#light-mode-only)![Configuration vault](https://clear.ml/docs/latest/assets/images/settings_configuration_vault_dark-cda874131008916e5ed8cd97347a7521.png#dark-mode-only)

- [Profile](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_profile/#profile)
- [Configuration](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_profile/#configuration)
  - [Customizing UI Behavior](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_profile/#customizing-ui-behavior)
  - [Browser Cloud Storage Access](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_profile/#browser-cloud-storage-access)
- [Workspace](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_profile/#workspace)
  - [Multiple Workspaces](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_profile/#multiple-workspaces)
  - [ClearML API Credentials](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_profile/#clearml-api-credentials)
  - [AI Application Gateway Tokens](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_profile/#ai-application-gateway-tokens)
  - [Changing Your Workspace Name](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_profile/#changing-your-workspace-name)
  - [Adding Users to Your Workspace](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_profile/#adding-users-to-your-workspace)
  - [Leaving a Workspace](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_profile/#leaving-a-workspace)
  - [Configuration Vault](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_profile/#configuration-vault)