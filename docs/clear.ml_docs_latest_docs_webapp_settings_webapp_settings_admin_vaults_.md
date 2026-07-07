---
url: "https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_admin_vaults/"
title: "Administrator Vaults | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_admin_vaults/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

Enterprise Feature

Administrator vaults are available under the ClearML Enterprise plan.

Administrators can define multiple [configuration vaults](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_profile#configuration-vault) which will each be applied to designated
[user groups](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_users). There are three types of vaults:

- [Client configuration (Agent/SDK/CLI)](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_admin_vaults/#client-configuration-agentsdkcli)
- [UI storage credentials](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_admin_vaults/#ui-storage-credentials)
- [SSH server](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_admin_vaults/#ssh-server)

To apply its contents, a vault should be enabled in the [Administrator Vault Table](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_admin_vaults/#administrator-vault-table).

## Client Configuration (Agent/SDK/CLI) [​](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_admin_vaults/\#client-configuration-agentsdkcli "Direct link to Client Configuration (Agent/SDK/CLI)")

Client configuration vaults extend and/or override entries in the local ClearML [configuration file](https://clear.ml/docs/latest/docs/configs/clearml_conf)
where a task is executed. Vault values will be applied to tasks run by members of the designated user groups.

New entries will extend the configuration in the local ClearML [configuration file](https://clear.ml/docs/latest/docs/configs/clearml_conf).
Most existing configuration file entries will be overridden by the vault values.

note

The following configuration values are machine and/or agent specific, so they can't be set in a configuration vault:

- `agent.cuda_version`
- `agent.cudnn_version`
- `agent.default_python`
- `agent.worker_id`
- `agent.worker_name`
- `agent.debug`

**To create a Client configuration vault:**

1. Click **\+ Add Vault**
2. Fill in vault details:
1. Vault name - Name that appears in the Administrator Vaults table
2. User Group - Specify the User Group that the vault affects
3. Target - Vault type. Select `Client (Agent/SDK/UI)`
4. Format - Specify the configuration format: HOCON / JSON / YAML.
5. Fill in the configuration values (click ![Info](https://clear.ml/docs/latest/icons/ico-info.svg)
      to view configuration file reference). To import an existing configuration file, click ![Import](https://clear.ml/docs/latest/icons/ico-import.svg).
3. Click **Save**

## UI Storage Credentials [​](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_admin_vaults/\#ui-storage-credentials "Direct link to UI Storage Credentials")

UI storage credential vaults configure UI access to cloud storage credentials for a designated group of users.

**To create a vault:**

1. Click **\+ Add Vault**
2. Fill in vault details:
1. Vault name - Name that appears in the Administrator Vaults table
2. User Group - Specify the User Group that the vault affects
3. Target - Vault type. Select `UI storage credentials`
4. \+ Add access keys - Enter storage credentials (see [Browser Cloud Storage Access](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_profile#browser-cloud-storage-access))
3. Click **Save**

## SSH Server [​](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_admin_vaults/\#ssh-server "Direct link to SSH Server")

SSH Server Vaults configure SSH keys for SSH sessions spun up through the [SSH Session application](https://clear.ml/docs/latest/docs/webapp/applications/apps_ssh_session)
or [ClearML Session](https://clear.ml/docs/latest/docs/apps/clearml_session) by users in the user groups assigned to the vaults.

- The private keys (`ssh_host_*_key`) are stored in the vault.
- The corresponding public keys (`ssh_host_*_key__pub`) are installed on the SSH server to allow clients to verify the
server’s identity.

**To create an SSH server vault:**

1. Click + Add Vault
2. Fill in vault details:


   - Vault name - Name that appears in the Administrator Vaults table
   - User Group - Specify the User Group that the vault affects
   - Target - Vault type. Select `SSH Server`
   - Add SSH keys. For example:


```text
{

  "ssh_host_ecdsa_key": "-----BEGIN EC PRIVATE KEY----- …. -----END EC PRIVATE KEY-----\n",

  "ssh_host_ed25519_key": "-----BEGIN OPENSSH PRIVATE KEY----- …. -----END OPENSSH PRIVATE KEY-----\n",

  "ssh_host_rsa_key": "-----BEGIN RSA PRIVATE KEY----- … -----END RSA PRIVATE KEY-----\n",

  "ssh_host_rsa_key__pub": "ssh-rsa …",

  "ssh_host_ecdsa_key__pub": "ecdsa-sha2-nistp256 …",

  "ssh_host_ed25519_key__pub": "ssh-ed25519 …"

}
```

3. Click Save

## Administrator Vault Table [​](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_admin_vaults/\#administrator-vault-table "Direct link to Administrator Vault Table")

The **Administrator Vaults** table lists all currently defined vaults, and the following details:

- Active - Toggle to enable / disable the vault
- Name - Vault name
- Target - Type of vault: `Client (Agent/SDK/CLI)`, `UI storage credentials`, or `SSH server`
- Group - User groups to apply this vault to
- ID - Vault ID (click to copy)
- Vault Content - Vault content summary
- Update - Last update time

Hover over a vault in the table and click ![Dot menu](https://clear.ml/docs/latest/icons/ico-dots-v-menu.svg)
to access vault actions:

- Download
- Edit
- Delete
- View log - View a history of vault activity: vault action (e.g. activate, deactivate, edit, etc.), acting user, and action time.

![Admin vaults](https://clear.ml/docs/latest/assets/images/settings_admin_vaults-f027201635bd55c6a02e69eff53e9df6.png#light-mode-only)![Admin vaults](https://clear.ml/docs/latest/assets/images/settings_admin_vaults_dark-b825e9aafc0f1dd6ae864181d1878204.png#dark-mode-only)

## Activity Log [​](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_admin_vaults/\#activity-log "Direct link to Activity Log")

The activity log displays a detailed history of activity across all admin vaults:

- Vault name
- Action: Operation performed on the vault
  - Create / Delete
  - Activate / Deactivate
  - Edit
- Action time
- User who performed the action.

Use the column filters ![Filter](https://clear.ml/docs/latest/icons/ico-filter-off.svg) to
filter the log by vault name, action, time range, or acting user.

![Admin vaults](https://clear.ml/docs/latest/assets/images/settings_admin_vaults_log-e17a86e41591e07c8b837516eada8393.png#light-mode-only)![Admin vaults](https://clear.ml/docs/latest/assets/images/settings_admin_vaults_log_dark-3286f6a068875b5274f72007ca1e9206.png#dark-mode-only)

- [Client Configuration (Agent/SDK/CLI)](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_admin_vaults/#client-configuration-agentsdkcli)
- [UI Storage Credentials](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_admin_vaults/#ui-storage-credentials)
- [SSH Server](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_admin_vaults/#ssh-server)
- [Administrator Vault Table](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_admin_vaults/#administrator-vault-table)
- [Activity Log](https://clear.ml/docs/latest/docs/webapp/settings/webapp_settings_admin_vaults/#activity-log)