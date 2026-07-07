---
url: "https://clear.ml/docs/latest/docs/references/enterprise/apps/"
title: "apps | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/enterprise/apps/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

### POST /apps.apply\_customization\_upgrade [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#post-appsapply_customization_upgrade "Direct link to POST /apps.apply_customization_upgrade")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#description "Direct link to Description")

Apply the upgrade by walking the diff: replace each conflicting override's

`default` with the target's default, optionally prune orphaned overrides, save

the customization, and emit one customization\_conflict audit event per replaced

override. Conflicts do NOT block the upgrade — by the time this is called the

apiserver-level enable/disable for the new version has already happened (or is

happening) elsewhere.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#parameters "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-apply_customization_upgrade-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **customization\_id**<br>_required_ |  | string |
| **prune\_orphaned**<br>_optional_ | **Default** : `false` | boolean |
| **target\_version**<br>_optional_ | Optional; latest available version is used if omitted. | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#responses "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-apply_customization_upgrade-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **applied**<br>_optional_ |  | boolean |
| **customization\_id**<br>_optional_ |  | string |
| **new\_fields\_count**<br>_optional_ |  | integer |
| **orphaned\_pruned**<br>_optional_ |  | < string > array |
| **preserved\_count**<br>_optional_ |  | integer |
| **replaced**<br>_optional_ | One entry per override that was rewritten. Mirrored in the audit-log stream. | < [replaced](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-apply_customization_upgrade-post-replaced) \> array |
| **upgraded\_from**<br>_optional_ |  | string |
| **upgraded\_to**<br>_optional_ |  | string |

**replaced**

| Name | Schema |
| --- | --- |
| **entry\_name**<br>_optional_ | string |
| **field**<br>_optional_ | string |
| **reason**<br>_optional_ | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#security "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | admin,system,root |

### POST /apps.batch\_delete [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#post-appsbatch_delete "Direct link to POST /apps.batch_delete")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#description-1 "Direct link to Description")

Delete multiple applications at once. Mirrors the warn+confirm+terminate

pattern: if any app in the batch has running instances and confirm\_stop is

false, returns a single dry-run response with per-app breakdown and no DB

change. If confirm\_stop is true, terminates instances per affected app, then

deletes all.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#parameters-1 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-batch_delete-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **confirm\_stop**<br>_optional_ | When true, terminates running instances of any affected app before deleting the <br>batch. When false (default) and any app has instances, returns a dry-run <br>response with requires\_confirmation=true. <br>**Default** : `false` | boolean |
| **force**<br>_optional_ | Deprecated alias. When true (and confirm\_stop is not set), is treated as <br>confirm\_stop=true for backwards compat. <br>**Default** : `false` | boolean |
| **ids**<br>_required_ | List of application IDs to delete | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#responses-1 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-batch_delete-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **apps**<br>_optional_ | Per-app breakdown of running instances and affected tenants. Only includes apps <br>that have running instances. | < [apps](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-batch_delete-post-apps) \> array |
| **failed**<br>_optional_ | Map of app ID to error message for failed deletions | object |
| **requires\_confirmation**<br>_optional_ | True when at least one app has running instances and confirm\_stop is false. | boolean |
| **running\_instances**<br>_optional_ | Total running instances across the batch. | integer |
| **stopped\_instances**<br>_optional_ | Total instances actually stopped (0 in dry-run mode). | integer |
| **succeeded**<br>_optional_ | List of successfully deleted app IDs (empty in dry-run mode) | < string > array |

**apps**

| Name | Schema |
| --- | --- |
| **affected\_tenants**<br>_optional_ | < [affected\_tenants](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-batch_delete-post-apps-affected_tenants) \> array |
| **app\_id**<br>_optional_ | string |
| **running\_instances**<br>_optional_ | integer |

**affected\_tenants**

| Name | Schema |
| --- | --- |
| **id**<br>_optional_ | string |
| **name**<br>_optional_ | string |
| **running**<br>_optional_ | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#security-1 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | admin,system,root |

### POST /apps.clean\_available\_apps [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#post-appsclean_available_apps "Direct link to POST /apps.clean_available_apps")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#description-2 "Direct link to Description")

Clean non-deployed app versions from the repository. Does not affect deployed

apps.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#parameters-2 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-clean_available_apps-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **app**<br>_optional_ | App ID to clean. If not provided, cleans all non-deployed versions. | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#responses-2 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-clean_available_apps-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **app\_ids**<br>_optional_ | App IDs that were affected | < string > array |
| **cleaned**<br>_optional_ | Number of app versions removed | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#security-2 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | admin,system,root |

### POST /apps.clear\_hub\_token [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#post-appsclear_hub_token "Direct link to POST /apps.clear_hub_token")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#description-3 "Direct link to Description")

Clear the hub token

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#parameters-3 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#responses-3 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-clear_hub_token-response-200) |

**Response 200**

| Name | Schema |
| --- | --- |
| **updated**<br>_optional_ | boolean |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#security-3 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root |

### POST /apps.create\_customization [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#post-appscreate_customization "Direct link to POST /apps.create_customization")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#description-4 "Direct link to Description")

Create a customization (named overlay variant) for an installed app. Stores

only the delta from the base app: appearance overrides + per-wizard-entry

overrides. Per the multi-customization-per-tenant rule, the same name may be

reused across customizations as long as no tenant resolves to two

customizations with the same name simultaneously — collisions are rejected at

save time.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#parameters-4 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-create_customization-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **app\_id**<br>_required_ | Application ID this customization overlays. | string |
| **appearance\_overrides**<br>_optional_ | Sparse map of overridable AppInfo fields. Allowed keys: name, icon, <br>description, category, badges, provider. Other keys are rejected with <br>invalid\_override\_field. | object |
| **assignment**<br>_optional_ | Tenant scoping for this customization (independent of the base app's <br>AppRecord). | [assignment](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-create_customization-post-assignment) |
| **name**<br>_required_ | Display label. Unique per (app\_id, tenant) at resolution time. | string |
| **wizard\_overrides**<br>_optional_ | Per-wizard-entry overrides. Each item must include entry\_name; allowed override <br>keys: title, info, default, hidden. Structural fields (type, target, name, <br>choices, conditional) are not overridable. | < object > array |

**assignment**

| Name | Schema |
| --- | --- |
| **mode**<br>_optional_ | enum (all, include, exclude) |
| **tenants**<br>_optional_ | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#responses-4 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-create_customization-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **app\_id**<br>_optional_ | Base application this customization overlays. | string |
| **appearance\_overrides**<br>_optional_ | Sparse map of overridden AppInfo fields. Allowed keys: name, icon, description, <br>category, badges, provider. Only keys present here override the base; absent <br>keys fall through to the base AppInfo. | object |
| **assignment**<br>_optional_ | Tenant scoping for this customization (independent of the base app's AppRecord <br>assignment). When mode=all the customization is visible to every tenant; <br>include/exclude restrict to the listed tenants. | [assignment](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-create_customization-post-assignment) |
| **id**<br>_optional_ | Customization ID (assigned by the server on create). | string |
| **last\_update**<br>_optional_ | Last write timestamp. | string (date-time) |
| **launch\_locked**<br>_optional_ | Admin launch lock on this customization (toggled via apps.set\_launch\_lock with <br>customization\_id). True means the customization stays visible but <br>apps.launch\_instance refuses new instances launched against it; running <br>instances are untouched. | boolean |
| **name**<br>_optional_ | Display label. Unique per (app\_id, tenant) at resolution time. | string |
| **state**<br>_optional_ | Mapping-driven lock-axis state for this customization. Only populated when the <br>call is scoped to a specific tenant (e.g. get\_customizations with tenant\_id, or <br>the embedded form in get\_tenant\_apps). Reflects the TenantAppMapping row for <br>the (tenant, customization) pair: `enabled` means launchable; `disabled` means <br>the customization is still deployed (the row exists) but apps.launch\_instance <br>refuses new instances. Absence of a row means the customization is not deployed <br>to this tenant — in that case the customization will not appear in the tenant- <br>scoped list at all. Replaces the legacy `launch_locked` field once the FE has <br>migrated. | enum (enabled, disabled) |
| **updated\_by**<br>_optional_ | User id of the most recent writer. | string |
| **wizard\_overrides**<br>_optional_ | Per-wizard-entry overrides keyed by entry\_name. Each item may contain title, <br>info, default. Structural fields (type, target, name, choices, conditional) are <br>not overridable. Dropping a field from the launch form is intentionally not <br>offered — that is a template-author decision (EntryType.hidden / <br>WizardEntryBase.disabled in the .app.conf upload). | < [wizard\_overrides](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-create_customization-post-wizard_overrides) \> array |

**assignment**

| Name | Description | Schema |
| --- | --- | --- |
| **mode**<br>_optional_ |  | enum (all, include, exclude) |
| **tenant\_count**<br>_optional_ | Optional. Populated only on the get\_all\_apps embedded form: count of tenants <br>the customization resolves to (for include = len(tenants); for exclude = <br>total\_tenants - len(tenants); for all = total\_tenants). | integer |
| **tenants**<br>_optional_ | Resolved tenant ids enriched with display names. For include/exclude the list <br>is the explicit tenant set; for mode=all this is empty. | < [tenants](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-create_customization-post-assignment-tenants) \> array |
| **total\_tenants**<br>_optional_ | Optional. Populated only on the get\_all\_apps embedded form: total number of <br>tenants in the system at the time of the request. | integer |

**tenants**

| Name | Schema |
| --- | --- |
| **id**<br>_optional_ | string |
| **name**<br>_optional_ | string |

**wizard\_overrides**

| Name | Description | Schema |
| --- | --- | --- |
| **entry\_name**<br>_optional_ | Name of the wizard entry being overridden. Required. | string |
| **info**<br>_optional_ | Optional override of the entry's helper/info text. | string |
| **title**<br>_optional_ | Optional override of the entry's display title. | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#security-4 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | admin,system,root |

### POST /apps.delete [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#post-appsdelete "Direct link to POST /apps.delete")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#description-5 "Direct link to Description")

Delete application. Mirrors the warn+confirm+terminate pattern of apps.enable

undeploy and apps.set\_tenant\_assignment. If running instances exist and

confirm\_stop is false, returns a dry-run with running\_instances +

affected\_tenants and no DB change. If confirm\_stop is true, terminates

instances first, then deletes.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#parameters-5 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-delete-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **app**<br>_required_ | Application ID | string |
| **confirm\_stop**<br>_optional_ | When true, terminates running instances of the app before deleting. When false <br>(default) and instances exist, returns a dry-run response with <br>requires\_confirmation=true. <br>**Default** : `false` | boolean |
| **force**<br>_optional_ | Deprecated alias. When true (and confirm\_stop is not set), is treated as <br>confirm\_stop=true for backwards compat. <br>**Default** : `false` | boolean |
| **version**<br>_optional_ | Application version | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#responses-5 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-delete-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **affected\_tenants**<br>_optional_ | Tenants that have running instances of this app, with per-tenant counts. | < [affected\_tenants](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-delete-post-affected_tenants) \> array |
| **deleted**<br>_optional_ | Number of Application docs deleted (0 in dry-run mode) | integer |
| **requires\_confirmation**<br>_optional_ | True when running instances exist and confirm\_stop is false. Caller should re- <br>call with confirm\_stop=true to proceed. | boolean |
| **running\_instances**<br>_optional_ | Total running instances detected for this app | integer |
| **stopped\_instances**<br>_optional_ | Number of instances actually stopped (0 in dry-run mode) | integer |

**affected\_tenants**

| Name | Schema |
| --- | --- |
| **id**<br>_optional_ | string |
| **name**<br>_optional_ | string |
| **running**<br>_optional_ | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#security-5 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | admin,system,root |

### POST /apps.delete\_customization [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#post-appsdelete_customization "Direct link to POST /apps.delete_customization")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#description-6 "Direct link to Description")

Delete a customization. Mirrors the warn+confirm+terminate pattern of

apps.delete (base app). If running task instances reference this customization

and confirm\_stop is false, returns a dry-run with running\_instances +

affected\_tenants and no DB change. If confirm\_stop is true, terminates

instances first, then deletes the doc and cascade-deletes its TenantAppMapping

rows.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#parameters-6 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-delete_customization-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **confirm\_stop**<br>_optional_ | When true, terminates running task instances of the customization before <br>deleting. When false (default) and instances exist, returns a dry-run response <br>with requires\_confirmation=true. <br>**Default** : `false` | boolean |
| **customization\_id**<br>_required_ |  | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#responses-6 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-delete_customization-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **affected\_tenants**<br>_optional_ | Tenants that have running instances of this customization, with per-tenant <br>counts. | < [affected\_tenants](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-delete_customization-post-affected_tenants) \> array |
| **deleted**<br>_optional_ | Id of the deleted customization (empty when dry-run or was\_already\_gone). | string |
| **requires\_confirmation**<br>_optional_ | True when running instances exist and confirm\_stop is false. Caller should re- <br>call with confirm\_stop=true to proceed. | boolean |
| **running\_instances**<br>_optional_ | Total running task instances detected for this customization. | integer |
| **stopped\_instances**<br>_optional_ | Number of instances actually stopped (0 in dry-run mode). | integer |
| **was\_already\_gone**<br>_optional_ | True when no customization with this id existed at call time. Treated as a <br>successful no-op. | boolean |

**affected\_tenants**

| Name | Schema |
| --- | --- |
| **id**<br>_optional_ | string |
| **name**<br>_optional_ | string |
| **running**<br>_optional_ | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#security-6 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | admin,system,root |

### POST /apps.deploy\_all [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#post-appsdeploy_all "Direct link to POST /apps.deploy_all")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#description-7 "Direct link to Description")

Snapshot the current tenant list and upsert an enabled mapping for each. New

tenants created after this call are picked up by the onboarding hook, not this

snapshot.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#parameters-7 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-deploy_all-request) |

**request**

| Name | Schema |
| --- | --- |
| **application\_id**<br>_required_ | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#responses-7 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-deploy_all-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **enabled**<br>_optional_ | Rows now in state=enabled as a result of this call (newly created or flipped <br>from disabled). | integer |
| **tenants**<br>_optional_ |  | < string > array |
| **unchanged**<br>_optional_ | Rows already in state=enabled (no-op for this tenant). | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#security-7 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | admin,system,root |

### POST /apps.deploy\_per\_tenant [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#post-appsdeploy_per_tenant "Direct link to POST /apps.deploy_per_tenant")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#description-8 "Direct link to Description")

Bulk-upsert (tenant, application) mappings with state=enabled, one per tenant

in tenant\_ids — i.e. deploy + enable in a single call. Idempotent per row: re-

deploying an already-enabled pair is a no-op; re-deploying a disabled pair

flips it back to enabled. Pass an array of length 1 for the single-tenant case.

All tenant ids are validated up front — an unknown tenant aborts the call with

no writes.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#parameters-8 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-deploy_per_tenant-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **application\_id**<br>_required_ | Either a base app\_id or a customization id. The server distinguishes. | string |
| **tenant\_ids**<br>_required_ | Tenant company IDs. Must contain at least one element. | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#responses-8 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-deploy_per_tenant-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **application\_id**<br>_optional_ |  | string |
| **results**<br>_optional_ | Per-tenant result, in input order. | < [results](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-deploy_per_tenant-post-results) \> array |

**results**

| Name | Description | Schema |
| --- | --- | --- |
| **changed**<br>_optional_ | False if the row already had state=enabled (no-op). | boolean |
| **created**<br>_optional_ | True if the row was created; false if updated or no-op. | boolean |
| **state**<br>_optional_ |  | enum (enabled, disabled) |
| **tenant\_id**<br>_optional_ |  | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#security-8 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | admin,system,root |

### POST /apps.disable\_all [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#post-appsdisable_all "Direct link to POST /apps.disable_all")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#description-9 "Direct link to Description")

Flip every existing mapping row for this application to state=disabled. Does

NOT create disabled rows for tenants that have no row yet — that's what

disable\_per\_tenant is for. Does NOT remove rows — that's what undeploy\_all is

for.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#parameters-9 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-disable_all-request) |

**request**

| Name | Schema |
| --- | --- |
| **application\_id**<br>_required_ | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#responses-9 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-disable_all-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **application\_id**<br>_optional_ |  | string |
| **disabled**<br>_optional_ | Number of rows flipped to disabled. | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#security-9 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | admin,system,root |

### POST /apps.disable\_per\_tenant [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#post-appsdisable_per_tenant "Direct link to POST /apps.disable_per_tenant")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#description-10 "Direct link to Description")

Bulk-upsert (tenant, application) mappings with state=disabled, one per tenant

in tenant\_ids. Missing rows are created in the disabled state so they are

addressable for later re-enable via deploy\_per\_tenant. Note: this verb does NOT

undo deployment — the row still exists, the tenant still sees the app, only

launch is blocked. To remove the row entirely (the deployment axis undo), use

undeploy\_per\_tenant. Pass an array of length 1 for the single-tenant case.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#parameters-10 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-disable_per_tenant-request) |

**request**

| Name | Schema |
| --- | --- |
| **application\_id**<br>_required_ | string |
| **tenant\_ids**<br>_required_ | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#responses-10 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-disable_per_tenant-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **application\_id**<br>_optional_ |  | string |
| **results**<br>_optional_ | Per-tenant result, in input order. | < [results](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-disable_per_tenant-post-results) \> array |

**results**

| Name | Schema |
| --- | --- |
| **changed**<br>_optional_ | boolean |
| **created**<br>_optional_ | boolean |
| **state**<br>_optional_ | enum (enabled, disabled) |
| **tenant\_id**<br>_optional_ | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#security-10 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | admin,system,root |

### POST /apps.edit\_instance [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#post-appsedit_instance "Direct link to POST /apps.edit_instance")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#description-11 "Direct link to Description")

Edit params of the existing app instance

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#parameters-11 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-edit_instance-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **instance**<br>_required_ | Application instance ID | string |
| **update\_params**<br>_required_ | params to update | object |
| **user\_groups**<br>_optional_ | IDs of the user groups that this instance is shared with | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#responses-11 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-edit_instance-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **updated**<br>_optional_ | Number of application instances updated (0 or 1) | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#security-11 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /apps.enable [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#post-appsenable "Direct link to POST /apps.enable")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#description-12 "Direct link to Description")

Enable or disable an app version. Extended with PMC-specific behavior:

single\_active enforces one-active-version-per-app, confirm\_stop drives warn-

then-confirm-then-terminate on undeploy when running instances exist, and

`force` drives the dry-run-then-confirm flow when a new version would conflict

with existing customizations.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#parameters-12 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-enable-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **app**<br>_required_ | Application ID | string |
| **confirm\_stop**<br>_optional_ | Used together with single\_active when undeploying. When false (default) and <br>running instances exist, returns a dry-run with requires\_confirmation=true and <br>no DB change. When true, terminates running instances and proceeds. <br>**Default** : `false` | boolean |
| **enable**<br>_required_ | If set to Truethe the app is enabled. Otherwise disabled <br>**Default** : `true` | boolean |
| **force**<br>_optional_ | Two-step customization-conflict guard for the deploy path. When false (default) <br>and the target version would conflict with existing customizations' <br>wizard\_overrides, the enable is REFUSED with <br>requires\_customization\_confirmation=true and the affected\_customizations list. <br>Admin reviews the list and re-calls with force=true. When true, the enable <br>proceeds AND every affected customization is auto-rewritten to the new defaults <br>(same path as apps.apply\_customization\_upgrade, with prune\_orphaned=false). <br>`customization_conflict` audit events are emitted per replaced field — that's <br>the source of truth for what changed; no persistent flag is written on <br>customizations. <br>**Default** : `false` | boolean |
| **single\_active**<br>_optional_ | PMC mode. On deploy: deactivates all other versions of the same app, ensuring <br>exactly one is active. On undeploy: stops running instances and auto-activates <br>the next remaining version (only when version is specified). <br>**Default** : `false` | boolean |
| **version**<br>_optional_ | Application version | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#responses-12 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-enable-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **activated\_version**<br>_optional_ | On undeploy with single\_active and a specific version: the next-highest <br>remaining version that was auto-activated. Null when no auto-activation <br>occurred (e.g. version omitted, or no other versions exist). | string |
| **affected\_customizations**<br>_optional_ | Dry-run output (when requires\_customization\_confirmation=true): one entry per <br>customization whose wizard\_overrides would conflict with the target version. <br>Includes the per-field conflict detail so the FE can render a confirmation <br>dialog. | < [affected\_customizations](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-enable-post-affected_customizations) \> array |
| **affected\_tenants**<br>_optional_ | On undeploy: per-tenant breakdown of running task instances detected for the <br>version(s) being undeployed. Empty when no instances are running. Same shape as <br>apps.undeploy\_per\_tenant.affected\_tenants, <br>apps.set\_tenant\_assignment.affected\_tenants and <br>apps.delete\_customization.affected\_tenants so the FE confirm dialog is reusable <br>across all four flows. | < [affected\_tenants](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-enable-post-affected_tenants) \> array |
| **auto\_applied\_customizations**<br>_optional_ | Force-path output (when force=true and customizations were rewritten): <br>customization\_ids that were auto-applied to the new version via the <br>apps.apply\_customization\_upgrade pipeline. Per-customization audit detail lives <br>in the standard customization\_conflict audit stream. | < string > array |
| **is\_downgrade**<br>_optional_ | On deploy: true when the newly enabled version is older than previous\_version <br>(string compare). | boolean |
| **previous\_version**<br>_optional_ | On deploy: the version that was active before this call (if any). Null if no <br>version was active. | string |
| **requires\_confirmation**<br>_optional_ | True when running instances exist and confirm\_stop is false. Caller should re- <br>call with confirm\_stop=true to proceed. | boolean |
| **requires\_customization\_confirmation**<br>_optional_ | True when the target version conflicts with one or more customizations and <br>force is false. Caller should review affected\_customizations and re-call with <br>force=true to proceed. | boolean |
| **running\_instances**<br>_optional_ | On undeploy: number of running task instances detected for the version(s) being <br>undeployed. | integer |
| **stopped\_instances**<br>_optional_ | On undeploy with confirm\_stop=true: number of instances actually stopped. | integer |
| **updated**<br>_optional_ | Number of Application docs modified (0 in dry-run mode) | integer |

**affected\_customizations**

| Name | Description | Schema |
| --- | --- | --- |
| **conflicts**<br>_optional_ | Per-field conflict detail from the upgrade diff: entry\_name + overridden\_fields <br>\+ reason + override\_value + new\_default + new\_type. | < object > array |
| **customization\_id**<br>_optional_ |  | string |
| **name**<br>_optional_ |  | string |

**affected\_tenants**

| Name | Schema |
| --- | --- |
| **id**<br>_optional_ | string |
| **name**<br>_optional_ | string |
| **running**<br>_optional_ | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#security-12 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | admin,system,root |

### POST /apps.get\_all\_apps [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#post-appsget_all_apps "Direct link to POST /apps.get_all_apps")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#description-13 "Direct link to Description")

Get all applications (installed and available) with version info. Admin only.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#parameters-13 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#responses-13 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_all_apps-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **apps**<br>_optional_ | List of all applications grouped by app\_id | < [apps](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_all_apps-post-apps) \> array |

**apps**

| Name | Description | Schema |
| --- | --- | --- |
| **app\_id**<br>_optional_ | Application ID | string |
| **category**<br>_optional_ | Application category | string |
| **customizations**<br>_optional_ | Customizations (overlay variants) of this app, embedded so admin views can <br>render them as nested child rows without a per-app fanout to <br>apps.get\_customizations. | < [customizations](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_all_apps-post-apps-customizations) \> array |
| **deployed**<br>_optional_ | Whether any version of this app is currently installed (apps.enable=true on at <br>least one version). | boolean |
| **deployed\_version**<br>_optional_ | The version currently installed (apps.enable=true), or null if no version is <br>installed. | string |
| **description**<br>_optional_ | Application description | string |
| **icon**<br>_optional_ | Icon URL surfaced for admin UIs. For apps uploaded from a real .app.conf zip <br>this is typically `api/apps.get_asset?app=<id>&version=<v>&uri=<file>`<br>(resolves against the stored Asset collection); externally-pointed icons may be <br>any absolute URL the browser can reach. May be null/empty for stub-uploaded <br>apps. | string |
| **latest\_version**<br>_optional_ | The latest (highest) version available | string |
| **name**<br>_optional_ | Application name | string |
| **provider**<br>_optional_ | Application provider | string |
| **rollup**<br>_optional_ | Mapping-driven tenant rollup for this base app: how many tenants are in each <br>state. Replaces the legacy `assignment.mode/tenants` \+ `launch_locked` triple. | [rollup](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_all_apps-post-apps-rollup) |
| **status**<br>_optional_ | Single-chip summary the FE renders without math on `rollup`. `deployed` = at <br>least one tenant has state=enabled (launchable somewhere); `disabled` = no <br>enabled tenants but at least one disabled (locked everywhere it's deployed); <br>`not_deployed` = no tenant rows at all. Priority is `deployed > disabled >  <br/>not_deployed` — an app with both enabled and disabled tenants is reported as <br>`deployed`; use `rollup` for the breakdown. | enum (deployed, disabled, not\_deployed) |
| **versions**<br>_optional_ | All versions of this app | < [versions](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_all_apps-post-apps-versions) \> array |

**customizations**

| Name | Description | Schema |
| --- | --- | --- |
| **appearance\_overrides**<br>_optional_ |  | object |
| **id**<br>_optional_ |  | string |
| **last\_update**<br>_optional_ |  | string (date-time) |
| **name**<br>_optional_ |  | string |
| **rollup**<br>_optional_ | Mapping-driven tenant rollup for this customization. Unlike base apps, <br>customizations are NOT auto-onboarded to new tenants, so `not_deployed` is <br>omitted (it would be misleading). | [rollup](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_all_apps-post-apps-customizations-rollup) |
| **status**<br>_optional_ | Single-chip summary for this customization. Same enum as the parent app's <br>`status`; `not_deployed` is the common initial state for a customization with <br>no tenant rows yet. | enum (deployed, disabled, not\_deployed) |
| **tenants**<br>_optional_ | Per-tenant breakdown for this customization — every tenant with a <br>TenantAppMapping row, enriched with display name and lock-axis state. Tenants <br>without a row are omitted (= not deployed to that tenant). Base apps don't <br>carry this list (their roster is every tenant after onboarding — too large to <br>inline); use apps.get\_tenant\_assignment(app\_id) when you need the per-tenant <br>view for a base. | < [tenants](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_all_apps-post-apps-customizations-tenants) \> array |
| **updated\_by**<br>_optional_ |  | string |
| **wizard\_overrides**<br>_optional_ |  | < object > array |

**rollup**

| Name | Schema |
| --- | --- |
| **disabled**<br>_optional_ | integer |
| **enabled**<br>_optional_ | integer |
| **total\_tenants**<br>_optional_ | integer |

**tenants**

| Name | Schema |
| --- | --- |
| **id**<br>_optional_ | string |
| **name**<br>_optional_ | string |
| **state**<br>_optional_ | enum (enabled, disabled) |

**rollup**

| Name | Description | Schema |
| --- | --- | --- |
| **disabled**<br>_optional_ | Tenants with state=disabled (visible, launch blocked). | integer |
| **enabled**<br>_optional_ | Tenants with state=enabled (launchable). | integer |
| **not\_deployed**<br>_optional_ | Tenants with no row for this app. Equal to total\_tenants - enabled - disabled. | integer |
| **total\_tenants**<br>_optional_ |  | integer |

**versions**

| Name | Description | Schema |
| --- | --- | --- |
| **enabled**<br>_optional_ | Whether this version is installed (apps.enable). NOT the tenant-mapping state — <br>that lives on `rollup`. | boolean |
| **last\_update**<br>_optional_ | Last update time | string (date-time) |
| **origin**<br>_optional_ | Where this version came from: manual, hub, or bundled | string |
| **version**<br>_optional_ | Version string | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#security-13 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | admin,system,root |

### POST /apps.get\_app\_upgrade\_impact [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#post-appsget_app_upgrade_impact "Direct link to POST /apps.get_app_upgrade_impact")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#description-14 "Direct link to Description")

Bulk variant of get\_customization\_upgrade\_diff: returns the diff for every

customization of `app_id` against `target_version` in a single call. The target

template is parsed once server-side and reused across all customizations —

replaces the N+1 fan-out clients otherwise have to do (list customizations,

then call apps.get\_customization\_upgrade\_diff once per row). Designed so any

upgrade-preview UI — not just the bundled webapp — can answer 'what does this

version do to all customizations on this app?' in a single round trip.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#parameters-14 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_app_upgrade_impact-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **app\_id**<br>_required_ |  | string |
| **target\_version**<br>_optional_ | Optional. When omitted, the latest available version of `app_id` is used. | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#responses-14 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_app_upgrade_impact-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **app\_id**<br>_optional_ |  | string |
| **current\_version**<br>_optional_ | The currently-deployed (enabled) version of this app, or null. | string |
| **customizations**<br>_optional_ | Per-customization diff. Same shape as get\_customization\_upgrade\_diff's <br>response, with customization\_id and customization\_name added. | < [customizations](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_app_upgrade_impact-post-customizations) \> array |
| **customizations\_affected**<br>_optional_ | Customizations whose conflicts list is non-empty against the target version. | integer |
| **customizations\_total**<br>_optional_ | Total customizations on this app. | integer |
| **target\_version**<br>_optional_ |  | string |

**customizations**

| Name | Schema |
| --- | --- |
| **conflicts**<br>_optional_ | < [conflicts](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_app_upgrade_impact-post-customizations-conflicts) \> array |
| **customization\_id**<br>_optional_ | string |
| **customization\_name**<br>_optional_ | string |
| **new\_fields**<br>_optional_ | < [new\_fields](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_app_upgrade_impact-post-customizations-new_fields) \> array |
| **orphaned**<br>_optional_ | < [orphaned](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_app_upgrade_impact-post-customizations-orphaned) \> array |
| **preserved**<br>_optional_ | < [preserved](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_app_upgrade_impact-post-customizations-preserved) \> array |

**conflicts**

| Name | Schema |
| --- | --- |
| **entry\_name**<br>_optional_ | string |
| **new\_type**<br>_optional_ | string |
| **overridden\_fields**<br>_optional_ | < string > array |
| **reason**<br>_optional_ | enum (type\_changed, range\_violation, choice\_removed) |

**new\_fields**

| Name | Schema |
| --- | --- |
| **entry\_name**<br>_optional_ | string |
| **title**<br>_optional_ | string |
| **type**<br>_optional_ | string |

**orphaned**

| Name | Schema |
| --- | --- |
| **entry\_name**<br>_optional_ | string |
| **overridden\_fields**<br>_optional_ | < string > array |

**preserved**

| Name | Schema |
| --- | --- |
| **entry\_name**<br>_optional_ | string |
| **overridden\_fields**<br>_optional_ | < string > array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#security-14 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | admin,system,root |

### POST /apps.get\_apps [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#post-appsget_apps "Direct link to POST /apps.get_apps")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#description-15 "Direct link to Description")

Return the list of the available applications

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#parameters-15 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_apps-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **app\_usages**<br>_optional_ | If set to 'true' then return running and pending apps counts <br>**Default** : `false` | boolean |
| **exclude**<br>_optional_ | apps to exclude | [exclude](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_apps-post-exclude) |
| **include**<br>_optional_ | apps to include | [include](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_apps-post-include) |

**exclude**

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_optional_ | Regex condition on app id | < string > array |

**include**

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_optional_ | Regex condition on app id | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#responses-15 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_apps-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **apps**<br>_optional_ |  | < [apps.app\_info\_with\_usages](https://clear.ml/docs/latest/docs/references/enterprise/definitions#appsapp_info_with_usages) \> array |
| **apps\_queue**<br>_optional_ | Apps queue usage | [apps\_queue](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_apps-post-apps_queue) |

**apps\_queue**

| Name | Description | Schema |
| --- | --- | --- |
| **max\_allowed**<br>_optional_ | The maximum number of the company application instances that can be run on the <br>server queue | integer |
| **pending**<br>_optional_ | The total amount of the company application instances pending on the server <br>queue | integer |
| **running**<br>_optional_ | The total number of the company application instances running on the server <br>queue | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#security-15 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /apps.get\_asset [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#post-appsget_asset "Direct link to POST /apps.get_asset")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#description-16 "Direct link to Description")

Retrieve application asset

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#parameters-16 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_asset-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **app**<br>_required_ | Application ID | string |
| **uri**<br>_required_ | Asset uri | string |
| **version**<br>_required_ | Application version | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#responses-16 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#security-16 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /apps.get\_assignments\_summary [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#post-appsget_assignments_summary "Direct link to POST /apps.get_assignments_summary")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#description-17 "Direct link to Description")

Get assignment summary for all deployed apps

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#parameters-17 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#responses-17 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_assignments_summary-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **apps**<br>_optional_ | Mapping-driven per-app rollup: per base app, the count of tenants in each <br>state. | < [apps](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_assignments_summary-post-apps) \> array |

**apps**

| Name | Description | Schema |
| --- | --- | --- |
| **app\_id**<br>_optional_ |  | string |
| **disabled**<br>_optional_ | Number of tenants with a TenantAppMapping row in state=disabled (visible to <br>admin, launch blocked). | integer |
| **enabled**<br>_optional_ | Number of tenants with a TenantAppMapping row in state=enabled for this app <br>(launchable). | integer |
| **name**<br>_optional_ | Display name (from the latest enabled version's AppInfo) | string |
| **not\_deployed**<br>_optional_ | Number of tenants with no mapping row for this app. Equal to total\_tenants - <br>enabled - disabled. | integer |
| **total\_tenants**<br>_optional_ | Total number of tenants on the server | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#security-17 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | admin,system,root |

### POST /apps.get\_categories [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#post-appsget_categories "Direct link to POST /apps.get_categories")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#description-18 "Direct link to Description")

DAG-19215. Return the distinct list of app catalog categories currently

installed on this server, sorted alphabetically. Feeds the tenant-RBAC editor

(user group → app\_categories picker) and any FE control that needs the live

category vocabulary. Empty/unset categories are excluded.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#parameters-18 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#responses-18 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_categories-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **categories**<br>_optional_ | Distinct, sorted, non-empty category strings from the installed app catalog. | < string > array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#security-18 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /apps.get\_customization [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#post-appsget_customization "Direct link to POST /apps.get_customization")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#description-19 "Direct link to Description")

Get a single customization with full overrides + tenant names.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#parameters-19 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_customization-request) |

**request**

| Name | Schema |
| --- | --- |
| **customization\_id**<br>_required_ | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#responses-19 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_customization-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **app\_id**<br>_optional_ | Base application this customization overlays. | string |
| **appearance\_overrides**<br>_optional_ | Sparse map of overridden AppInfo fields. Allowed keys: name, icon, description, <br>category, badges, provider. Only keys present here override the base; absent <br>keys fall through to the base AppInfo. | object |
| **assignment**<br>_optional_ | Tenant scoping for this customization (independent of the base app's AppRecord <br>assignment). When mode=all the customization is visible to every tenant; <br>include/exclude restrict to the listed tenants. | [assignment](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_customization-post-assignment) |
| **id**<br>_optional_ | Customization ID (assigned by the server on create). | string |
| **last\_update**<br>_optional_ | Last write timestamp. | string (date-time) |
| **launch\_locked**<br>_optional_ | Admin launch lock on this customization (toggled via apps.set\_launch\_lock with <br>customization\_id). True means the customization stays visible but <br>apps.launch\_instance refuses new instances launched against it; running <br>instances are untouched. | boolean |
| **name**<br>_optional_ | Display label. Unique per (app\_id, tenant) at resolution time. | string |
| **state**<br>_optional_ | Mapping-driven lock-axis state for this customization. Only populated when the <br>call is scoped to a specific tenant (e.g. get\_customizations with tenant\_id, or <br>the embedded form in get\_tenant\_apps). Reflects the TenantAppMapping row for <br>the (tenant, customization) pair: `enabled` means launchable; `disabled` means <br>the customization is still deployed (the row exists) but apps.launch\_instance <br>refuses new instances. Absence of a row means the customization is not deployed <br>to this tenant — in that case the customization will not appear in the tenant- <br>scoped list at all. Replaces the legacy `launch_locked` field once the FE has <br>migrated. | enum (enabled, disabled) |
| **updated\_by**<br>_optional_ | User id of the most recent writer. | string |
| **wizard\_overrides**<br>_optional_ | Per-wizard-entry overrides keyed by entry\_name. Each item may contain title, <br>info, default. Structural fields (type, target, name, choices, conditional) are <br>not overridable. Dropping a field from the launch form is intentionally not <br>offered — that is a template-author decision (EntryType.hidden / <br>WizardEntryBase.disabled in the .app.conf upload). | < [wizard\_overrides](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_customization-post-wizard_overrides) \> array |

**assignment**

| Name | Description | Schema |
| --- | --- | --- |
| **mode**<br>_optional_ |  | enum (all, include, exclude) |
| **tenant\_count**<br>_optional_ | Optional. Populated only on the get\_all\_apps embedded form: count of tenants <br>the customization resolves to (for include = len(tenants); for exclude = <br>total\_tenants - len(tenants); for all = total\_tenants). | integer |
| **tenants**<br>_optional_ | Resolved tenant ids enriched with display names. For include/exclude the list <br>is the explicit tenant set; for mode=all this is empty. | < [tenants](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_customization-post-assignment-tenants) \> array |
| **total\_tenants**<br>_optional_ | Optional. Populated only on the get\_all\_apps embedded form: total number of <br>tenants in the system at the time of the request. | integer |

**tenants**

| Name | Schema |
| --- | --- |
| **id**<br>_optional_ | string |
| **name**<br>_optional_ | string |

**wizard\_overrides**

| Name | Description | Schema |
| --- | --- | --- |
| **entry\_name**<br>_optional_ | Name of the wizard entry being overridden. Required. | string |
| **info**<br>_optional_ | Optional override of the entry's helper/info text. | string |
| **title**<br>_optional_ | Optional override of the entry's display title. | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#security-19 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | admin,system,root |

### POST /apps.get\_customization\_editor\_state [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#post-appsget_customization_editor_state "Direct link to POST /apps.get_customization_editor_state")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#description-20 "Direct link to Description")

Single-call composer for the PMC tenant→Applications editor. Returns the base

app's appearance + wizard (so the editor can show every overridable field pre-

filled with base values), the existing customization overlay (when

customization\_id is supplied — resolves with the same tenant entitlement check

used at launch), and a static hint listing which fields are overridable.

Replaces the 2-3 round-trip dance of get\_apps + get\_launch\_template +

get\_customization.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#parameters-20 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_customization_editor_state-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **app\_id**<br>_required_ | Application ID whose editor state is being requested. | string |
| **customization\_id**<br>_optional_ | Optional. When set the editor opens in 'edit existing' mode and the <br>response.customization is populated. When absent the editor opens in 'create <br>new' mode and response.customization is null. | string |
| **tenant\_id**<br>_required_ | Tenant (company) ID the editor is scoped to. Used to verify the calling admin's <br>entitlement to the customization (when customization\_id is supplied) and <br>recorded so save calls pre-fill assignment={mode:include, tenants:\[tenant\_id\]}. | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#responses-20 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_customization_editor_state-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **app\_id**<br>_optional_ |  | string |
| **base**<br>_optional_ | Snapshot of the base app the editor is overlaying. The editor renders these <br>fields as the starting point for every overridable field; on save the UI sends <br>back ONLY the fields the admin changed (sparse delta) via <br>create/update\_customization. | [base](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_customization_editor_state-post-base) |
| **customization**<br>_optional_ | Existing customization (when customization\_id was supplied), or null. UI uses <br>this to pre-fill the editor with the current overlay; on save it sends a PATCH <br>via apps.update\_customization. | [customization](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_customization_editor_state-post-customization) |
| **overridable**<br>_optional_ | Hint to the editor: which fields it may expose as editable. Server- <br>authoritative — UI should not attempt to override anything outside these <br>allowlists; create\_customization / update\_customization will reject unknown <br>keys. | [overridable](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_customization_editor_state-post-overridable) |
| **tenant\_id**<br>_optional_ |  | string |

**base**

| Name | Description | Schema |
| --- | --- | --- |
| **appearance**<br>_optional_ | AppInfo subset corresponding to overridable.appearance keys. UI renders these <br>as the default values for the appearance form. | object |
| **wizard**<br>_optional_ | Same shape as apps.get\_launch\_template's launch\_template field — <br>formFieldGroups with their entries. UI renders the form and lets the admin <br>override title/info/default/hidden per entry. | object |

**customization**

| Name | Description | Schema |
| --- | --- | --- |
| **app\_id**<br>_optional_ | Base application this customization overlays. | string |
| **appearance\_overrides**<br>_optional_ | Sparse map of overridden AppInfo fields. Allowed keys: name, icon, description, <br>category, badges, provider. Only keys present here override the base; absent <br>keys fall through to the base AppInfo. | object |
| **assignment**<br>_optional_ | Tenant scoping for this customization (independent of the base app's AppRecord <br>assignment). When mode=all the customization is visible to every tenant; <br>include/exclude restrict to the listed tenants. | [assignment](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_customization_editor_state-post-customization-assignment) |
| **id**<br>_optional_ | Customization ID (assigned by the server on create). | string |
| **last\_update**<br>_optional_ | Last write timestamp. | string (date-time) |
| **launch\_locked**<br>_optional_ | Admin launch lock on this customization (toggled via apps.set\_launch\_lock with <br>customization\_id). True means the customization stays visible but <br>apps.launch\_instance refuses new instances launched against it; running <br>instances are untouched. | boolean |
| **name**<br>_optional_ | Display label. Unique per (app\_id, tenant) at resolution time. | string |
| **state**<br>_optional_ | Mapping-driven lock-axis state for this customization. Only populated when the <br>call is scoped to a specific tenant (e.g. get\_customizations with tenant\_id, or <br>the embedded form in get\_tenant\_apps). Reflects the TenantAppMapping row for <br>the (tenant, customization) pair: `enabled` means launchable; `disabled` means <br>the customization is still deployed (the row exists) but apps.launch\_instance <br>refuses new instances. Absence of a row means the customization is not deployed <br>to this tenant — in that case the customization will not appear in the tenant- <br>scoped list at all. Replaces the legacy `launch_locked` field once the FE has <br>migrated. | enum (enabled, disabled) |
| **updated\_by**<br>_optional_ | User id of the most recent writer. | string |
| **wizard\_overrides**<br>_optional_ | Per-wizard-entry overrides keyed by entry\_name. Each item may contain title, <br>info, default. Structural fields (type, target, name, choices, conditional) are <br>not overridable. Dropping a field from the launch form is intentionally not <br>offered — that is a template-author decision (EntryType.hidden / <br>WizardEntryBase.disabled in the .app.conf upload). | < [wizard\_overrides](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_customization_editor_state-post-customization-wizard_overrides) \> array |

**assignment**

| Name | Description | Schema |
| --- | --- | --- |
| **mode**<br>_optional_ |  | enum (all, include, exclude) |
| **tenant\_count**<br>_optional_ | Optional. Populated only on the get\_all\_apps embedded form: count of tenants <br>the customization resolves to (for include = len(tenants); for exclude = <br>total\_tenants - len(tenants); for all = total\_tenants). | integer |
| **tenants**<br>_optional_ | Resolved tenant ids enriched with display names. For include/exclude the list <br>is the explicit tenant set; for mode=all this is empty. | < [tenants](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_customization_editor_state-post-customization-assignment-tenants) \> array |
| **total\_tenants**<br>_optional_ | Optional. Populated only on the get\_all\_apps embedded form: total number of <br>tenants in the system at the time of the request. | integer |

**tenants**

| Name | Schema |
| --- | --- |
| **id**<br>_optional_ | string |
| **name**<br>_optional_ | string |

**wizard\_overrides**

| Name | Description | Schema |
| --- | --- | --- |
| **entry\_name**<br>_optional_ | Name of the wizard entry being overridden. Required. | string |
| **info**<br>_optional_ | Optional override of the entry's helper/info text. | string |
| **title**<br>_optional_ | Optional override of the entry's display title. | string |

**overridable**

| Name | Description | Schema |
| --- | --- | --- |
| **appearance**<br>_optional_ | Whitelisted AppInfo keys allowed in customization.appearance\_overrides. | < string > array |
| **wizard\_entry**<br>_optional_ | Whitelisted per-wizard-entry override keys allowed in items of <br>customization.wizard\_overrides. | < string > array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#security-20 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | admin,system,root |

### POST /apps.get\_customization\_upgrade\_diff [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#post-appsget_customization_upgrade_diff "Direct link to POST /apps.get_customization_upgrade_diff")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#description-21 "Direct link to Description")

Compare a customization's wizard\_overrides against a target version's wizard

and report what would change on upgrade. Per the PRD this is the passive-

notification primitive — when an admin opens the customization view we run this

against the latest available version and surface any conflicts. The diff itself

is read-only; nothing in the database changes here.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#parameters-21 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_customization_upgrade_diff-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **customization\_id**<br>_required_ |  | string |
| **target\_version**<br>_optional_ | Optional. When omitted, the latest available version of the same app\_id is <br>used. | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#responses-21 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_customization_upgrade_diff-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **app\_id**<br>_optional_ |  | string |
| **conflicts**<br>_optional_ | Overrides whose value violates the target entry's type/range/choices. <br>apply\_customization\_upgrade replaces these with the target's default and emits <br>a customization\_conflict audit event per replacement. | < [conflicts](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_customization_upgrade_diff-post-conflicts) \> array |
| **current\_version**<br>_optional_ | The currently-deployed (enabled) version, or null. | string |
| **customization\_id**<br>_optional_ |  | string |
| **customization\_name**<br>_optional_ |  | string |
| **new\_fields**<br>_optional_ | Entries in the target version that have no override yet. Take the target <br>entry's default at launch time. | < [new\_fields](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_customization_upgrade_diff-post-new_fields) \> array |
| **orphaned**<br>_optional_ | Overrides whose entry was removed in the target version. Inert by default — <br>they re-apply if the entry comes back in a later version. Pass <br>prune\_orphaned=true on apply to drop them. | < [orphaned](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_customization_upgrade_diff-post-orphaned) \> array |
| **preserved**<br>_optional_ | Overrides whose entry still exists with compatible types. Will continue to <br>apply on upgrade. | < [preserved](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_customization_upgrade_diff-post-preserved) \> array |
| **target\_version**<br>_optional_ |  | string |

**conflicts**

| Name | Schema |
| --- | --- |
| **entry\_name**<br>_optional_ | string |
| **new\_type**<br>_optional_ | string |
| **overridden\_fields**<br>_optional_ | < string > array |
| **reason**<br>_optional_ | enum (type\_changed, range\_violation, choice\_removed) |

**new\_fields**

| Name | Schema |
| --- | --- |
| **entry\_name**<br>_optional_ | string |
| **title**<br>_optional_ | string |
| **type**<br>_optional_ | string |

**orphaned**

| Name | Schema |
| --- | --- |
| **entry\_name**<br>_optional_ | string |
| **overridden\_fields**<br>_optional_ | < string > array |

**preserved**

| Name | Schema |
| --- | --- |
| **entry\_name**<br>_optional_ | string |
| **overridden\_fields**<br>_optional_ | < string > array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#security-21 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | admin,system,root |

### POST /apps.get\_customizations [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#post-appsget_customizations "Direct link to POST /apps.get_customizations")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#description-22 "Direct link to Description")

List customizations. Optional app\_id filter. Optional tenant\_id scope — when

supplied, only customizations with a TenantAppMapping row for that tenant are

returned, and each row carries its `state` (enabled/disabled) sourced from the

mapping. Without tenant\_id the list is unscoped and `state` is omitted. Tenant

ids on the returned `assignment` field are enriched with display names via a

single bulk Company query — no per-row fanout.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#parameters-22 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_customizations-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **app\_id**<br>_optional_ | Optional: list only customizations of this app. | string |
| **tenant\_id**<br>_optional_ | Optional: scope to customizations the tenant has a TenantAppMapping row for. <br>When set, each item carries a `state` (enabled/disabled) reflecting that row. <br>To create the row use apps.deploy\_per\_tenant with the customization\_id; to <br>remove it use apps.undeploy\_per\_tenant. | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#responses-22 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_customizations-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **customizations**<br>_optional_ | List of customizations matching the filter. | < [customizations](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_customizations-post-customizations) \> array |

**customizations**

| Name | Description | Schema |
| --- | --- | --- |
| **app\_id**<br>_optional_ | Base application this customization overlays. | string |
| **appearance\_overrides**<br>_optional_ | Sparse map of overridden AppInfo fields. Allowed keys: name, icon, description, <br>category, badges, provider. Only keys present here override the base; absent <br>keys fall through to the base AppInfo. | object |
| **assignment**<br>_optional_ | Tenant scoping for this customization (independent of the base app's AppRecord <br>assignment). When mode=all the customization is visible to every tenant; <br>include/exclude restrict to the listed tenants. | [assignment](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_customizations-post-customizations-assignment) |
| **id**<br>_optional_ | Customization ID (assigned by the server on create). | string |
| **last\_update**<br>_optional_ | Last write timestamp. | string (date-time) |
| **launch\_locked**<br>_optional_ | Admin launch lock on this customization (toggled via apps.set\_launch\_lock with <br>customization\_id). True means the customization stays visible but <br>apps.launch\_instance refuses new instances launched against it; running <br>instances are untouched. | boolean |
| **name**<br>_optional_ | Display label. Unique per (app\_id, tenant) at resolution time. | string |
| **state**<br>_optional_ | Mapping-driven lock-axis state for this customization. Only populated when the <br>call is scoped to a specific tenant (e.g. get\_customizations with tenant\_id, or <br>the embedded form in get\_tenant\_apps). Reflects the TenantAppMapping row for <br>the (tenant, customization) pair: `enabled` means launchable; `disabled` means <br>the customization is still deployed (the row exists) but apps.launch\_instance <br>refuses new instances. Absence of a row means the customization is not deployed <br>to this tenant — in that case the customization will not appear in the tenant- <br>scoped list at all. Replaces the legacy `launch_locked` field once the FE has <br>migrated. | enum (enabled, disabled) |
| **updated\_by**<br>_optional_ | User id of the most recent writer. | string |
| **wizard\_overrides**<br>_optional_ | Per-wizard-entry overrides keyed by entry\_name. Each item may contain title, <br>info, default. Structural fields (type, target, name, choices, conditional) are <br>not overridable. Dropping a field from the launch form is intentionally not <br>offered — that is a template-author decision (EntryType.hidden / <br>WizardEntryBase.disabled in the .app.conf upload). | < [wizard\_overrides](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_customizations-post-customizations-wizard_overrides) \> array |

**assignment**

| Name | Description | Schema |
| --- | --- | --- |
| **mode**<br>_optional_ |  | enum (all, include, exclude) |
| **tenant\_count**<br>_optional_ | Optional. Populated only on the get\_all\_apps embedded form: count of tenants <br>the customization resolves to (for include = len(tenants); for exclude = <br>total\_tenants - len(tenants); for all = total\_tenants). | integer |
| **tenants**<br>_optional_ | Resolved tenant ids enriched with display names. For include/exclude the list <br>is the explicit tenant set; for mode=all this is empty. | < [tenants](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_customizations-post-customizations-assignment-tenants) \> array |
| **total\_tenants**<br>_optional_ | Optional. Populated only on the get\_all\_apps embedded form: total number of <br>tenants in the system at the time of the request. | integer |

**tenants**

| Name | Schema |
| --- | --- |
| **id**<br>_optional_ | string |
| **name**<br>_optional_ | string |

**wizard\_overrides**

| Name | Description | Schema |
| --- | --- | --- |
| **entry\_name**<br>_optional_ | Name of the wizard entry being overridden. Required. | string |
| **info**<br>_optional_ | Optional override of the entry's helper/info text. | string |
| **title**<br>_optional_ | Optional override of the entry's display title. | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#security-22 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | admin,system,root |

### POST /apps.get\_hub\_token\_status [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#post-appsget_hub_token_status "Direct link to POST /apps.get_hub_token_status")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#description-23 "Direct link to Description")

Get hub token configuration status. Never returns the token itself.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#parameters-23 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | object |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#responses-23 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_hub_token_status-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **assignment\_page\_url**<br>_optional_ | Customer Hub assignment-page URL configured on this install <br>(services.applications.hub.assignment\_page\_url). Lets the FE render a 'go to <br>assignment page' CTA in the token-management view. Empty string means the <br>install hasn't configured one and the FE should hide the link. | string |
| **configured**<br>_optional_ | Whether a hub token is configured | boolean |
| **last\_update**<br>_optional_ | When the token was last set or cleared | string (date-time) |
| **source**<br>_optional_ | Token source: env (environment variable) or db (set via API) | string |
| **updated\_by**<br>_optional_ | User who last modified the token | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#security-23 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root |

### POST /apps.get\_info\_template [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#post-appsget_info_template "Direct link to POST /apps.get_info_template")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#description-24 "Direct link to Description")

Return the dashboard template for the application

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#parameters-24 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_info_template-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **instance**<br>_required_ | Application Instance ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#responses-24 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_info_template-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **info\_template**<br>_optional_ | Dashboard form template | object |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#security-24 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /apps.get\_instance\_info [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#post-appsget_instance_info "Direct link to POST /apps.get_instance_info")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#description-25 "Direct link to Description")

Get info for the existing app instance

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#parameters-25 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_instance_info-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **instance**<br>_required_ | Application instance ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#responses-25 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_instance_info-response-200) |

**Response 200**

| Name | Schema |
| --- | --- |
| **info**<br>_optional_ | [apps.application\_instance](https://clear.ml/docs/latest/docs/references/enterprise/definitions#appsapplication_instance) |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#security-25 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /apps.get\_instances [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#post-appsget_instances "Direct link to POST /apps.get_instances")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#description-26 "Direct link to Description")

Return the list of the application instances

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#parameters-26 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_instances-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **app**<br>_optional_ | Application ID. Required for non admin users | string |
| **current\_user**<br>_optional_ | If set to 'true' then only the instances ran by the current user are returned <br>**Default** : `false` | boolean |
| **customization\_id**<br>_optional_ | If passed, only instances launched from this AppCustomization are returned. <br>Pass an empty string to return only vanilla (non-customized) instances of the <br>app. When neither `customization_id` nor `include_customizations` is set, the <br>response defaults to vanilla-only — `app=X` alone means "base-app launches of <br>X", not "everything under X". | string |
| **include\_customizations**<br>_optional_ | Opt-in for the umbrella semantic: when true (and customization\_id is not set), <br>instances of `app` AND of every customization of `app` are returned together. <br>Default false — `app=X` without further qualification returns base-app launches <br>only. <br>**Default** : `false` | boolean |
| **name**<br>_optional_ | Regex pattern for the app instance name | string |
| **page**<br>_optional_ | Page number, returns a specific page out of the resulting list of tasks <br>**Minimum value** : `0` | integer |
| **page\_size**<br>_optional_ | Page size, specifies the number of results returned in each page (last page may <br>contain fewer results) <br>**Minimum value** : `1` | integer |
| **show\_archived**<br>_optional_ | If not set then archived instances are not shown <br>**Default** : `false` | boolean |
| **status**<br>_optional_ | The status of the application instances to return. If not passed then all <br>instances will be returned | [apps.application\_instance\_status\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions#appsapplication_instance_status_enum) |
| **summary**<br>_optional_ | If set the app summary returned instead of the full app info <br>**Default** : `false` | boolean |
| **updated\_since**<br>_optional_ | Timestamp in seconds since epoch. Only app instances that got updated after the <br>timestamp will be returned | integer |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#responses-26 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_instances-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **instances**<br>_optional_ | Application instances | < [apps.application\_instance\_summary](https://clear.ml/docs/latest/docs/references/enterprise/definitions#appsapplication_instance_summary) \> array |
| **usage**<br>_optional_ | App usage info. Returned only for the first page | [usage](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_instances-post-usage) |

**usage**

| Name | Description | Schema |
| --- | --- | --- |
| **max\_allowed**<br>_optional_ | The maximum number of the company application instances that can be run on the <br>server queue | integer |
| **running**<br>_optional_ | The total number of the company application instances running on the server <br>queue | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#security-26 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /apps.get\_launch\_template [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#post-appsget_launch_template "Direct link to POST /apps.get_launch_template")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#description-27 "Direct link to Description")

Return the configuration template for the application

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#parameters-27 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_launch_template-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **app**<br>_optional_ | Application ID | string |
| **customization\_id**<br>_optional_ | Optional AppCustomization ID. When supplied, the customization's <br>wizard\_overrides are merged onto the base app's wizard before serving the <br>template — the form reflects per-entry title/info/default/hidden overrides. <br>Vanilla template returned when omitted. | string |
| **dependent\_on**<br>_optional_ | Only return template fields dependent on the specified fields (with selected <br>values). Also applies the dependency values in the choices query. | object |
| **instance**<br>_optional_ | Application Instance ID. If not passed then the template for the latest version <br>of the app is returned | string |
| **source\_ui\_render**<br>_optional_ | The default value for source rendering if 'ui\_render' is not set on the source <br>**Default** : `false` | boolean |
| **user\_groups**<br>_optional_ | The list of user groups for selection. 'null' if selection combo should not be <br>shown at all | < [user\_groups](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_launch_template-post-user_groups) \> array |

**user\_groups**

| Name | Description | Schema |
| --- | --- | --- |
| **description**<br>_optional_ | User Group description | string |
| **id**<br>_optional_ | User Group ID | string |
| **name**<br>_optional_ | User Group name | string |
| **users**<br>_optional_ | The list of users in the group | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#responses-27 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_launch_template-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **launch\_template**<br>_optional_ | Configuration form template | object |
| **missing\_router**<br>_optional_ | 'true' if the application requires task router and no task router available for <br>the company | boolean |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#security-27 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /apps.get\_tenant\_apps [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#post-appsget_tenant_apps "Direct link to POST /apps.get_tenant_apps")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#description-28 "Direct link to Description")

PMC admin view: every (base app, customization) the tenant has a

TenantAppMapping row for, regardless of state. Each row carries `status`

(deployed/disabled/not\_deployed) aligned with apps.get\_all\_apps's vocabulary.

`not_deployed` appears only on the synthesized base parent when a customization

has a row for this tenant but the base does not — the base is synthesized so

the FE always has a parent for the customization.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#parameters-28 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_tenant_apps-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **tenant\_id**<br>_required_ | Tenant (company) ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#responses-28 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_tenant_apps-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **apps**<br>_optional_ | Per-base-app view for the tenant, ordered by app\_id. | < [apps](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_tenant_apps-post-apps) \> array |
| **tenant\_id**<br>_optional_ |  | string |
| **tenant\_name**<br>_optional_ |  | string |

**apps**

| Name | Description | Schema |
| --- | --- | --- |
| **app\_id**<br>_optional_ |  | string |
| **category**<br>_optional_ | Category (tab) the base app declares in its AppInfo. May be null when the app's <br>template doesn't set one. | string |
| **customizations**<br>_optional_ | Customizations of this base that have a TenantAppMapping row for this tenant, <br>newest-first. | < [customizations](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_tenant_apps-post-apps-customizations) \> array |
| **description**<br>_optional_ | Description for this app (parity with apps.get\_all\_apps). | string |
| **icon**<br>_optional_ | Icon URL — typically `api/apps.get_asset?app=<id>&version=<v>&uri=<file>` for <br>apps uploaded from a .app.conf zip; may be an absolute URL or null. | string |
| **name**<br>_optional_ | Display name (from the latest enabled version's AppInfo) | string |
| **provider**<br>_optional_ | Provider for this app (parity with apps.get\_all\_apps). | string |
| **status**<br>_optional_ | Lock-axis status of the base app's TenantAppMapping row for this tenant. <br>`deployed` = launchable; `disabled` = visible to admin but apps.launch\_instance <br>refuses new instances; `not_deployed` = no row exists for the base (only a <br>customization carries the tenant — the base entry is synthesized so the FE has <br>a parent for the customization). To go from any status back to `not_deployed`, <br>call apps.undeploy\_per\_tenant. Replaces the legacy `mode` \+ `launch_locked`<br>fields. | enum (deployed, disabled, not\_deployed) |
| **version**<br>_optional_ | Currently active version of this app | string |

**customizations**

| Name | Description | Schema |
| --- | --- | --- |
| **appearance\_overrides**<br>_optional_ | Sparse map of overridden AppInfo fields for this customization (same shape as <br>on apps.get\_customization). | object |
| **category**<br>_optional_ | Effective category for this customization: appearance\_overrides.category when <br>overridden, otherwise inherited from the base app. | string |
| **customization\_id**<br>_optional_ |  | string |
| **last\_update**<br>_optional_ |  | string (date-time) |
| **name**<br>_optional_ |  | string |
| **status**<br>_optional_ | Lock-axis status of this customization's TenantAppMapping row for this tenant. <br>`deployed` = launchable; `disabled` = launch blocked (row still exists). <br>`not_deployed` is not reachable here — customizations without a row for this <br>tenant are filtered out. To remove the customization from this tenant entirely, <br>call apps.undeploy\_per\_tenant with the customization\_id. | enum (deployed, disabled) |
| **wizard\_overrides**<br>_optional_ | Per-wizard-entry overrides for this customization (same shape as on <br>apps.get\_customization). Inlined here so the PMC tenant-detail view can render <br>the overlay without an extra fetch. | < object > array |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#security-28 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | admin,system,root |

### POST /apps.get\_tenant\_assignment [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#post-appsget_tenant_assignment "Direct link to POST /apps.get_tenant_assignment")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#description-29 "Direct link to Description")

Per-app assignment view: for the given app, return every tenant with a

TenantAppMapping row and its per-row state. Tenants with no row are absent from

the list (= not deployed). Tenant ids are enriched with display names.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#parameters-29 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_tenant_assignment-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **app\_id**<br>_required_ | Application ID | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#responses-29 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_tenant_assignment-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **app\_id**<br>_optional_ |  | string |
| **tenants**<br>_optional_ | Per-tenant rows for this app. Each entry includes the tenant id, display name, <br>and state (enabled/disabled). Tenants without a TenantAppMapping row for this <br>app are not listed. | < [tenants](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-get_tenant_assignment-post-tenants) \> array |

**tenants**

| Name | Schema |
| --- | --- |
| **id**<br>_optional_ | string |
| **name**<br>_optional_ | string |
| **state**<br>_optional_ | enum (enabled, disabled) |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#security-29 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | admin,system,root |

### POST /apps.launch\_instance [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#post-appslaunch_instance "Direct link to POST /apps.launch_instance")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#description-30 "Direct link to Description")

Launch the app instance with user params

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#parameters-30 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-launch_instance-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **app**<br>_required_ | Application ID | string |
| **customization\_id**<br>_optional_ | Optional AppCustomization ID. When supplied, the customization's <br>wizard\_overrides are merged onto the base wizard before validating <br>launch\_params, and the customization\_id is recorded on the resulting instance. | string |
| **launch\_params**<br>_required_ | params to launch with | object |
| **task\_name**<br>_optional_ | Override default task name | string |
| **user\_groups**<br>_optional_ | IDs of the user groups that this instance is shared with | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#responses-30 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-launch_instance-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **instance**<br>_optional_ | Application instance ID | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#security-30 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /apps.relaunch\_instance [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#post-appsrelaunch_instance "Direct link to POST /apps.relaunch_instance")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#description-31 "Direct link to Description")

Re-launch an existing application instance: stop and archive the original

instance, then launch a fresh instance reusing the original's configuration.

The archived original is deleted automatically (together with its artifacts)

once the new instance reaches a terminal status. The original's stored launch

params, customization and user groups are reused unless overridden.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#parameters-31 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-relaunch_instance-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **instance**<br>_required_ | ID of the application instance to re-launch | string |
| **launch\_params**<br>_optional_ | Optional launch params override. When omitted, the original instance's stored <br>configuration is reused. | object |
| **task\_name**<br>_optional_ | Override default task name | string |
| **user\_groups**<br>_optional_ | IDs of the user groups the new instance is shared with. When omitted, the <br>original instance's groups are reused. | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#responses-31 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-relaunch_instance-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **instance**<br>_optional_ | ID of the newly launched application instance | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#security-31 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | all |

### POST /apps.set\_hub\_token [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#post-appsset_hub_token "Direct link to POST /apps.set_hub_token")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#description-32 "Direct link to Description")

Set or replace the hub token for fetching apps from the ClearML marketplace

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#parameters-32 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-set_hub_token-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **token**<br>_required_ | The hub API token | string |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#responses-32 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-set_hub_token-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **assignment\_page\_url**<br>_optional_ | Customer Hub assignment-page URL configured on this install <br>(services.applications.hub.assignment\_page\_url). Surfaced here so the FE can <br>render a 'go to assignment page' CTA right after the admin adds the token, <br>without a follow-up get\_hub\_token\_status call. Empty string means the install <br>hasn't configured one and the FE should hide the link. | string |
| **updated**<br>_optional_ |  | boolean |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#security-32 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | system,root |

### POST /apps.set\_launch\_lock [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#post-appsset_launch_lock "Direct link to POST /apps.set_launch_lock")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#description-33 "Direct link to Description")

Toggle the admin-controlled launch lock for an app OR a customization. Exactly

one of app\_id / customization\_id must be supplied. When locked=true,

apps.launch\_instance refuses new instances launched against that resource for

every tenant; running instances are NOT stopped and the row remains visible in

apps.get\_apps with launch\_locked=true so the UI can grey out the launch action.

Locking a base app cascades: launches of every customization of that app are

also refused. The admin lock is independent of the per-version AppInfo.disabled

flag (template author intent, surfaced as `disabled` on catalog rows) — either

being true blocks launch. Distinct from apps.enable, which is a per-version

catalog-visibility toggle.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#parameters-33 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-set_launch_lock-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **app\_id**<br>_optional_ | Application ID. Mutually exclusive with customization\_id. | string |
| **customization\_id**<br>_optional_ | AppCustomization ID. Mutually exclusive with app\_id. | string |
| **locked**<br>_required_ | True to install the admin launch lock; false to clear it. Note: for apps, <br>clearing does not override an upload-time disabled flag in the app template. | boolean |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#responses-33 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-set_launch_lock-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **app\_id**<br>_optional_ | Echoed when app\_id was supplied. | string |
| **customization\_id**<br>_optional_ | Echoed when customization\_id was supplied. | string |
| **locked**<br>_optional_ | Resulting launch-lock state after the toggle. | boolean |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#security-33 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | admin,system,root |

### POST /apps.set\_tenant\_assignment [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#post-appsset_tenant_assignment "Direct link to POST /apps.set_tenant_assignment")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#description-34 "Direct link to Description")

Set tenant assignment for an app (all, include, or exclude mode). When the

change removes tenants that have running instances, returns a dry-run unless

confirm\_stop=true; on confirmation, running instances on removed tenants are

terminated.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#parameters-34 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-set_tenant_assignment-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **app\_id**<br>_required_ | Application ID | string |
| **confirm\_stop**<br>_optional_ | When true, terminates running instances on tenants that lose access before <br>applying the assignment change. When false (default) and such instances exist, <br>returns a dry-run with requires\_confirmation=true and no DB change. <br>**Default** : `false` | boolean |
| **mode**<br>_required_ | Assignment mode: all, include, or exclude | enum (all, include, exclude) |
| **tenants**<br>_optional_ | Tenant IDs (for include/exclude modes) | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#responses-34 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-set_tenant_assignment-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **affected\_tenants**<br>_optional_ | Tenants that would lose access and have running instances, with per-tenant <br>counts. | < [affected\_tenants](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-set_tenant_assignment-post-affected_tenants) \> array |
| **app\_id**<br>_optional_ |  | string |
| **mode**<br>_optional_ |  | string |
| **requires\_confirmation**<br>_optional_ | True when running instances exist on tenants that would lose access and <br>confirm\_stop is false. | boolean |
| **running\_instances**<br>_optional_ | Total running instances across all tenants that would lose access. Populated in <br>dry-run. | integer |
| **stopped\_instances**<br>_optional_ | Number of instances actually stopped on tenants that lost access (0 in dry-run <br>or when no removals). | integer |
| **updated**<br>_optional_ | True when the assignment was applied. False in dry-run mode. | boolean |

**affected\_tenants**

| Name | Schema |
| --- | --- |
| **id**<br>_optional_ | string |
| **name**<br>_optional_ | string |
| **running**<br>_optional_ | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#security-34 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | admin,system,root |

### POST /apps.undeploy\_all [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#post-appsundeploy_all "Direct link to POST /apps.undeploy_all")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#description-35 "Direct link to Description")

Delete every mapping row for this application — the deployment-axis undo of

deploy\_all. State is irrelevant; both enabled and disabled rows are removed.

Idempotent — re-running on an application with no rows returns removed=0.

Running-instance gate: same semantics as undeploy\_per\_tenant, but the affected

tenants are derived from the existing mapping rows.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#parameters-35 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-undeploy_all-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **application\_id**<br>_required_ |  | string |
| **confirm\_stop**<br>_optional_ | When true, running Task instances on every currently-mapped tenant are stopped <br>before the mapping rows are removed. When false (default) and any mapped tenant <br>has a running instance, the call returns requires\_confirmation=true and makes <br>no changes. <br>**Default** : `false` | boolean |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#responses-35 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-undeploy_all-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **affected\_tenants**<br>_optional_ | Mapped tenants with at least one running instance. Present only when <br>requires\_confirmation=true. | < [affected\_tenants](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-undeploy_all-post-affected_tenants) \> array |
| **application\_id**<br>_optional_ |  | string |
| **removed**<br>_optional_ | Number of rows deleted. 0 when requires\_confirmation=true (no rows were <br>touched). | integer |
| **requires\_confirmation**<br>_optional_ | True iff the call was refused because running instances exist. In that case <br>`running_instances` \+ `affected_tenants` carry the detail and no row was <br>removed. | boolean |
| **running\_instances**<br>_optional_ | Total running instances across mapped tenants. Present only when <br>requires\_confirmation=true. | integer |
| **stopped\_instances**<br>_optional_ | Number of Task instances stopped before the undeploy. Only present when <br>confirm\_stop=true was passed and instances were running. | integer |

**affected\_tenants**

| Name | Schema |
| --- | --- |
| **id**<br>_optional_ | string |
| **name**<br>_optional_ | string |
| **running**<br>_optional_ | integer |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#security-35 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | admin,system,root |

### POST /apps.undeploy\_per\_tenant [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#post-appsundeploy_per_tenant "Direct link to POST /apps.undeploy_per_tenant")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#description-36 "Direct link to Description")

Delete (tenant, application) mapping rows for every tenant in tenant\_ids — the

deployment-axis undo of deploy\_per\_tenant. State of the row before removal is

irrelevant: both enabled and disabled rows are removed. Idempotent per row: a

missing row produces removed=false. Tenants are validated up front — an unknown

tenant aborts the call with no deletions. Running-instance gate: if any of the

target tenants has running Task instances against this application, the call

refuses with requires\_confirmation=true and returns the affected tenants

WITHOUT deleting any row. Pass confirm\_stop=true to stop those instances first

and then delete the rows.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#parameters-36 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-undeploy_per_tenant-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **application\_id**<br>_required_ |  | string |
| **confirm\_stop**<br>_optional_ | When true, running Task instances on the affected tenants are stopped before <br>the mapping rows are removed. When false (default) and any tenant has a running <br>instance, the call returns requires\_confirmation=true and makes no changes. <br>**Default** : `false` | boolean |
| **tenant\_ids**<br>_required_ |  | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#responses-36 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-undeploy_per_tenant-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **affected\_tenants**<br>_optional_ | Tenants with at least one running instance, with their display name and running <br>count. Present only when requires\_confirmation=true. | < [affected\_tenants](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-undeploy_per_tenant-post-affected_tenants) \> array |
| **application\_id**<br>_optional_ |  | string |
| **requires\_confirmation**<br>_optional_ | True iff the call was refused because running instances exist. In that case <br>`running_instances` \+ `affected_tenants` carry the detail and no row was <br>removed. | boolean |
| **results**<br>_optional_ | Per-tenant result, in input order. Omitted when requires\_confirmation is true <br>(no rows were touched). | < [results](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-undeploy_per_tenant-post-results) \> array |
| **running\_instances**<br>_optional_ | Total running instances across the affected tenants. Present only when <br>requires\_confirmation=true. | integer |
| **stopped\_instances**<br>_optional_ | Number of Task instances stopped before the undeploy. Only present when <br>confirm\_stop=true was passed and instances were running. | integer |

**affected\_tenants**

| Name | Schema |
| --- | --- |
| **id**<br>_optional_ | string |
| **name**<br>_optional_ | string |
| **running**<br>_optional_ | integer |

**results**

| Name | Description | Schema |
| --- | --- | --- |
| **removed**<br>_optional_ | True if a row existed and was deleted; false if no row was present. | boolean |
| **tenant\_id**<br>_optional_ |  | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#security-36 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | admin,system,root |

### POST /apps.update\_customization [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#post-appsupdate_customization "Direct link to POST /apps.update_customization")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#description-37 "Direct link to Description")

Partially update a customization. Any of name / appearance\_overrides /

wizard\_overrides / assignment may be supplied. Same uniqueness rule as

create\_customization re-runs against the new state.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#parameters-37 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-update_customization-request) |

**request**

| Name | Schema |
| --- | --- |
| **appearance\_overrides**<br>_optional_ | object |
| **assignment**<br>_optional_ | [assignment](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-update_customization-post-assignment) |
| **customization\_id**<br>_required_ | string |
| **name**<br>_optional_ | string |
| **wizard\_overrides**<br>_optional_ | < object > array |

**assignment**

| Name | Schema |
| --- | --- |
| **mode**<br>_optional_ | enum (all, include, exclude) |
| **tenants**<br>_optional_ | < string > array |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#responses-37 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-update_customization-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **app\_id**<br>_optional_ | Base application this customization overlays. | string |
| **appearance\_overrides**<br>_optional_ | Sparse map of overridden AppInfo fields. Allowed keys: name, icon, description, <br>category, badges, provider. Only keys present here override the base; absent <br>keys fall through to the base AppInfo. | object |
| **assignment**<br>_optional_ | Tenant scoping for this customization (independent of the base app's AppRecord <br>assignment). When mode=all the customization is visible to every tenant; <br>include/exclude restrict to the listed tenants. | [assignment](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-update_customization-post-assignment) |
| **id**<br>_optional_ | Customization ID (assigned by the server on create). | string |
| **last\_update**<br>_optional_ | Last write timestamp. | string (date-time) |
| **launch\_locked**<br>_optional_ | Admin launch lock on this customization (toggled via apps.set\_launch\_lock with <br>customization\_id). True means the customization stays visible but <br>apps.launch\_instance refuses new instances launched against it; running <br>instances are untouched. | boolean |
| **name**<br>_optional_ | Display label. Unique per (app\_id, tenant) at resolution time. | string |
| **state**<br>_optional_ | Mapping-driven lock-axis state for this customization. Only populated when the <br>call is scoped to a specific tenant (e.g. get\_customizations with tenant\_id, or <br>the embedded form in get\_tenant\_apps). Reflects the TenantAppMapping row for <br>the (tenant, customization) pair: `enabled` means launchable; `disabled` means <br>the customization is still deployed (the row exists) but apps.launch\_instance <br>refuses new instances. Absence of a row means the customization is not deployed <br>to this tenant — in that case the customization will not appear in the tenant- <br>scoped list at all. Replaces the legacy `launch_locked` field once the FE has <br>migrated. | enum (enabled, disabled) |
| **updated\_by**<br>_optional_ | User id of the most recent writer. | string |
| **wizard\_overrides**<br>_optional_ | Per-wizard-entry overrides keyed by entry\_name. Each item may contain title, <br>info, default. Structural fields (type, target, name, choices, conditional) are <br>not overridable. Dropping a field from the launch form is intentionally not <br>offered — that is a template-author decision (EntryType.hidden / <br>WizardEntryBase.disabled in the .app.conf upload). | < [wizard\_overrides](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-update_customization-post-wizard_overrides) \> array |

**assignment**

| Name | Description | Schema |
| --- | --- | --- |
| **mode**<br>_optional_ |  | enum (all, include, exclude) |
| **tenant\_count**<br>_optional_ | Optional. Populated only on the get\_all\_apps embedded form: count of tenants <br>the customization resolves to (for include = len(tenants); for exclude = <br>total\_tenants - len(tenants); for all = total\_tenants). | integer |
| **tenants**<br>_optional_ | Resolved tenant ids enriched with display names. For include/exclude the list <br>is the explicit tenant set; for mode=all this is empty. | < [tenants](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-update_customization-post-assignment-tenants) \> array |
| **total\_tenants**<br>_optional_ | Optional. Populated only on the get\_all\_apps embedded form: total number of <br>tenants in the system at the time of the request. | integer |

**tenants**

| Name | Schema |
| --- | --- |
| **id**<br>_optional_ | string |
| **name**<br>_optional_ | string |

**wizard\_overrides**

| Name | Description | Schema |
| --- | --- | --- |
| **entry\_name**<br>_optional_ | Name of the wizard entry being overridden. Required. | string |
| **info**<br>_optional_ | Optional override of the entry's helper/info text. | string |
| **title**<br>_optional_ | Optional override of the entry's display title. | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#security-37 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | admin,system,root |

### POST /apps.upload [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#post-appsupload "Direct link to POST /apps.upload")

#### Description [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#description-38 "Direct link to Description")

Upload applications. Supports single ZIPs and bulk tar.gz archives.

#### Parameters [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#parameters-38 "Direct link to Parameters")

| Type | Name | Description | Schema |
| --- | --- | --- | --- |
| **Body** | **request**<br>_required_ | request body | [request](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-upload-request) |

**request**

| Name | Description | Schema |
| --- | --- | --- |
| **enable**<br>_optional_ | If set to Truethen the newly uploaded apps are enabled <br>**Default** : `true` | boolean |
| **make\_latest**<br>_optional_ | Make the imported versions of the apps latest by disabling higher version of <br>the same apps <br>**Default** : `false` | boolean |
| **origin**<br>_optional_ | Origin of the uploaded apps: manual (default), hub, or bundled <br>**Default** : `"manual"` | enum (manual, hub, bundled) |
| **update\_existing**<br>_optional_ | If set to Truethen existing apps can be updated <br>**Default** : `false` | boolean |

#### Responses [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#responses-38 "Direct link to Responses")

| HTTP Code | Schema |
| --- | --- |
| **200** | [Response 200](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-upload-response-200) |

**Response 200**

| Name | Description | Schema |
| --- | --- | --- |
| **failed**<br>_optional_ | The list of the files that failed uploading with the corresponding errors | < [failed](https://clear.ml/docs/latest/docs/references/enterprise/apps/#apps-upload-post-failed) \> array |
| **succeeded**<br>_optional_ | The list of the files that were successfully uploaded | < string > array |

**failed**

| Name | Schema |
| --- | --- |
| **error**<br>_optional_ | string |
| **name**<br>_optional_ | string |

#### Security [​](https://clear.ml/docs/latest/docs/references/enterprise/apps/\#security-38 "Direct link to Security")

| Type | Name | Scopes |
| --- | --- | --- |
| **Bearer** | **clearml** | admin,system,root |

- [POST /apps.apply\_customization\_upgrade](https://clear.ml/docs/latest/docs/references/enterprise/apps/#post-appsapply_customization_upgrade)
- [POST /apps.batch\_delete](https://clear.ml/docs/latest/docs/references/enterprise/apps/#post-appsbatch_delete)
- [POST /apps.clean\_available\_apps](https://clear.ml/docs/latest/docs/references/enterprise/apps/#post-appsclean_available_apps)
- [POST /apps.clear\_hub\_token](https://clear.ml/docs/latest/docs/references/enterprise/apps/#post-appsclear_hub_token)
- [POST /apps.create\_customization](https://clear.ml/docs/latest/docs/references/enterprise/apps/#post-appscreate_customization)
- [POST /apps.delete](https://clear.ml/docs/latest/docs/references/enterprise/apps/#post-appsdelete)
- [POST /apps.delete\_customization](https://clear.ml/docs/latest/docs/references/enterprise/apps/#post-appsdelete_customization)
- [POST /apps.deploy\_all](https://clear.ml/docs/latest/docs/references/enterprise/apps/#post-appsdeploy_all)
- [POST /apps.deploy\_per\_tenant](https://clear.ml/docs/latest/docs/references/enterprise/apps/#post-appsdeploy_per_tenant)
- [POST /apps.disable\_all](https://clear.ml/docs/latest/docs/references/enterprise/apps/#post-appsdisable_all)
- [POST /apps.disable\_per\_tenant](https://clear.ml/docs/latest/docs/references/enterprise/apps/#post-appsdisable_per_tenant)
- [POST /apps.edit\_instance](https://clear.ml/docs/latest/docs/references/enterprise/apps/#post-appsedit_instance)
- [POST /apps.enable](https://clear.ml/docs/latest/docs/references/enterprise/apps/#post-appsenable)
- [POST /apps.get\_all\_apps](https://clear.ml/docs/latest/docs/references/enterprise/apps/#post-appsget_all_apps)
- [POST /apps.get\_app\_upgrade\_impact](https://clear.ml/docs/latest/docs/references/enterprise/apps/#post-appsget_app_upgrade_impact)
- [POST /apps.get\_apps](https://clear.ml/docs/latest/docs/references/enterprise/apps/#post-appsget_apps)
- [POST /apps.get\_asset](https://clear.ml/docs/latest/docs/references/enterprise/apps/#post-appsget_asset)
- [POST /apps.get\_assignments\_summary](https://clear.ml/docs/latest/docs/references/enterprise/apps/#post-appsget_assignments_summary)
- [POST /apps.get\_categories](https://clear.ml/docs/latest/docs/references/enterprise/apps/#post-appsget_categories)
- [POST /apps.get\_customization](https://clear.ml/docs/latest/docs/references/enterprise/apps/#post-appsget_customization)
- [POST /apps.get\_customization\_editor\_state](https://clear.ml/docs/latest/docs/references/enterprise/apps/#post-appsget_customization_editor_state)
- [POST /apps.get\_customization\_upgrade\_diff](https://clear.ml/docs/latest/docs/references/enterprise/apps/#post-appsget_customization_upgrade_diff)
- [POST /apps.get\_customizations](https://clear.ml/docs/latest/docs/references/enterprise/apps/#post-appsget_customizations)
- [POST /apps.get\_hub\_token\_status](https://clear.ml/docs/latest/docs/references/enterprise/apps/#post-appsget_hub_token_status)
- [POST /apps.get\_info\_template](https://clear.ml/docs/latest/docs/references/enterprise/apps/#post-appsget_info_template)
- [POST /apps.get\_instance\_info](https://clear.ml/docs/latest/docs/references/enterprise/apps/#post-appsget_instance_info)
- [POST /apps.get\_instances](https://clear.ml/docs/latest/docs/references/enterprise/apps/#post-appsget_instances)
- [POST /apps.get\_launch\_template](https://clear.ml/docs/latest/docs/references/enterprise/apps/#post-appsget_launch_template)
- [POST /apps.get\_tenant\_apps](https://clear.ml/docs/latest/docs/references/enterprise/apps/#post-appsget_tenant_apps)
- [POST /apps.get\_tenant\_assignment](https://clear.ml/docs/latest/docs/references/enterprise/apps/#post-appsget_tenant_assignment)
- [POST /apps.launch\_instance](https://clear.ml/docs/latest/docs/references/enterprise/apps/#post-appslaunch_instance)
- [POST /apps.relaunch\_instance](https://clear.ml/docs/latest/docs/references/enterprise/apps/#post-appsrelaunch_instance)
- [POST /apps.set\_hub\_token](https://clear.ml/docs/latest/docs/references/enterprise/apps/#post-appsset_hub_token)
- [POST /apps.set\_launch\_lock](https://clear.ml/docs/latest/docs/references/enterprise/apps/#post-appsset_launch_lock)
- [POST /apps.set\_tenant\_assignment](https://clear.ml/docs/latest/docs/references/enterprise/apps/#post-appsset_tenant_assignment)
- [POST /apps.undeploy\_all](https://clear.ml/docs/latest/docs/references/enterprise/apps/#post-appsundeploy_all)
- [POST /apps.undeploy\_per\_tenant](https://clear.ml/docs/latest/docs/references/enterprise/apps/#post-appsundeploy_per_tenant)
- [POST /apps.update\_customization](https://clear.ml/docs/latest/docs/references/enterprise/apps/#post-appsupdate_customization)
- [POST /apps.upload](https://clear.ml/docs/latest/docs/references/enterprise/apps/#post-appsupload)