---
url: "https://clear.ml/docs/latest/docs/references/enterprise/definitions/"
title: "API Definitions | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

## Definitions [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#definitions "Direct link to Definitions")

## apps.app\_info [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#appsapp_info "Direct link to apps.app_info")

| Name | Description | Schema |
| --- | --- | --- |
| **active**<br>_optional_ | Indicates whether the application version is active | boolean |
| **badges**<br>_optional_ | List of the application badges | < string > array |
| **category**<br>_optional_ | Application category | string |
| **confirm\_config\_update**<br>_optional_ | Indicates whether the configuration update should be confirmed by the end user <br>**Default** : `false` | boolean |
| **customization\_id**<br>_optional_ | Customization ID when this row represents an AppCustomization (overlay <br>variant). Null on vanilla rows (the base app itself). Use this as the <br>addressing primitive for the launch path when present. | string |
| **customization\_name**<br>_optional_ | Customization display name. Populated only when `customization_id` is set. | string |
| **description**<br>_optional_ | Application description | string |
| **details\_page**<br>_optional_ | The link template for the running instance details | [apps.details\_page\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#apps-details_page_enum) |
| **icon**<br>_optional_ | The link to the application icon | string |
| **id**<br>_optional_ | Application ID | string |
| **missing\_router**<br>_optional_ | 'true' if the application requires task router and no task router available for <br>the company | boolean |
| **name**<br>_optional_ | Application name | string |
| **no\_info\_html**<br>_optional_ | The link to the html that will be shown in case no info template is defined | string |
| **no\_info\_image**<br>_optional_ | The link to the image that will be shown in case no info template is defined | string |
| **provider**<br>_optional_ | Application provider | string |
| **state**<br>_optional_ | TenantAppMapping row state for the calling tenant. Mirrors the exact field that <br>apps.disable\_per\_tenant / apps.deploy\_per\_tenant mutate. `enabled` = <br>launchable; `disabled` = admin-locked for this tenant (row stays visible in the <br>catalog so the FE can render it greyed-out; apps.launch\_instance refuses to <br>start new instances). Rows without any TenantAppMapping row at all are filtered <br>out of the response entirely. The single source of truth the FE checks for 'can <br>launch'. | enum (enabled, disabled) |
| **user\_group\_sharing**<br>_optional_ | 'true' if the application supports user group sharing | boolean |
| **version**<br>_optional_ | Application version | string |

## apps.app\_info\_with\_usages [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#appsapp_info_with_usages "Direct link to apps.app_info_with_usages")

| Name | Description | Schema |
| --- | --- | --- |
| **active**<br>_optional_ | Indicates whether the application version is active | boolean |
| **badges**<br>_optional_ | List of the application badges | < string > array |
| **category**<br>_optional_ | Application category | string |
| **confirm\_config\_update**<br>_optional_ | Indicates whether the configuration update should be confirmed by the end user <br>**Default** : `false` | boolean |
| **customization\_id**<br>_optional_ | Customization ID when this row represents an AppCustomization (overlay <br>variant). Null on vanilla rows (the base app itself). Use this as the <br>addressing primitive for the launch path when present. | string |
| **customization\_name**<br>_optional_ | Customization display name. Populated only when `customization_id` is set. | string |
| **description**<br>_optional_ | Application description | string |
| **details\_page**<br>_optional_ | The link template for the running instance details | [apps.details\_page\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#apps-details_page_enum) |
| **icon**<br>_optional_ | The link to the application icon | string |
| **id**<br>_optional_ | Application ID | string |
| **missing\_router**<br>_optional_ | 'true' if the application requires task router and no task router available for <br>the company | boolean |
| **name**<br>_optional_ | Application name | string |
| **no\_info\_html**<br>_optional_ | The link to the html that will be shown in case no info template is defined | string |
| **no\_info\_image**<br>_optional_ | The link to the image that will be shown in case no info template is defined | string |
| **pending**<br>_optional_ | The amount of pending app instances | integer |
| **provider**<br>_optional_ | Application provider | string |
| **running**<br>_optional_ | The amount of running app instances | integer |
| **state**<br>_optional_ | TenantAppMapping row state for the calling tenant. Mirrors the exact field that <br>apps.disable\_per\_tenant / apps.deploy\_per\_tenant mutate. `enabled` = <br>launchable; `disabled` = admin-locked for this tenant (row stays visible in the <br>catalog so the FE can render it greyed-out; apps.launch\_instance refuses to <br>start new instances). Rows without any TenantAppMapping row at all are filtered <br>out of the response entirely. The single source of truth the FE checks for 'can <br>launch'. | enum (enabled, disabled) |
| **user\_group\_sharing**<br>_optional_ | 'true' if the application supports user group sharing | boolean |
| **version**<br>_optional_ | Application version | string |

## apps.application\_instance [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#appsapplication_instance "Direct link to apps.application_instance")

| Name | Description | Schema |
| --- | --- | --- |
| **active\_duration**<br>_optional_ | Application instance duration time (seconds) | integer |
| **application**<br>_optional_ | Application instance parameters | [application](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#apps-application_instance-application) |
| **comment**<br>_optional_ | Free text comment | string |
| **company**<br>_optional_ | Company ID | string |
| **completed**<br>_optional_ | Application instance end time (UTC) | string (date-time) |
| **created**<br>_optional_ | Application creation time (UTC) | string (date-time) |
| **id**<br>_optional_ | Application instance id | string |
| **last\_change**<br>_optional_ | Last update time | string (date-time) |
| **name**<br>_optional_ | Application instance Name | string |
| **project**<br>_optional_ | Project ID of the project to which this application is assigned | string |
| **queue**<br>_optional_ | The ID of the queue where the app instance is enqueued | string |
| **queue\_name**<br>_optional_ | The name of the queue where the app instance is enqueued | string |
| **readonly**<br>_optional_ | If true then this app instance cannot be modified | boolean |
| **setting\_up**<br>_optional_ | If true then the agent is setting up the task and has not started its execution <br>yet | boolean |
| **started**<br>_optional_ | Application instance start time (UTC) | string (date-time) |
| **status**<br>_optional_ |  | [apps.task\_status\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#apps-task_status_enum) |
| **status\_changed**<br>_optional_ | Last status change time | string (date-time) |
| **status\_message**<br>_optional_ | free text string representing info about the status | string |
| **status\_reason**<br>_optional_ | Reason for last status change | string |
| **user**<br>_optional_ | Associated user id | string |
| **user\_groups**<br>_optional_ | IDs of the user groups that this instance is shared with | < string > array |
| **valid\_app\_version**<br>_optional_ | True if the version of the application template matches the version of the <br>current application template. False otherwise | boolean |

**application**

| Name | Description | Schema |
| --- | --- | --- |
| **app\_id**<br>_optional_ | ID of the application template | string |
| **configuration**<br>_optional_ | Configuration parameters | object |
| **customization\_id**<br>_optional_ | ID of the AppCustomization this instance was launched from (null for vanilla) | string |
| **internal\_execution**<br>_optional_ | True if the app is scheduled for the execution by internal agent. False <br>otherwise | boolean |
| **run\_by\_admin**<br>_optional_ | Indicates whether the application was run by an admin or system user | boolean |
| **version**<br>_optional_ | The version of the application template | string |

## apps.application\_instance\_status\_enum [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#appsapplication_instance_status_enum "Direct link to apps.application_instance_status_enum")

_Type_ : enum (running, stopped)

## apps.application\_instance\_summary [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#appsapplication_instance_summary "Direct link to apps.application_instance_summary")

| Name | Description | Schema |
| --- | --- | --- |
| **active\_duration**<br>_optional_ | Application instance duration time (seconds) | integer |
| **application**<br>_optional_ | Application instance parameters | [application](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#apps-application_instance_summary-application) |
| **id**<br>_optional_ | Application instance id | string |
| **last\_change**<br>_optional_ | Last update time | string (date-time) |
| **name**<br>_optional_ | Application instance Name | string |
| **readonly**<br>_optional_ | If true then this app instance cannot be modified | boolean |
| **status**<br>_optional_ |  | [apps.task\_status\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#apps-task_status_enum) |
| **user\_groups**<br>_optional_ | IDs of the user groups that this instance is shared with | < string > array |

**application**

| Name | Description | Schema |
| --- | --- | --- |
| **customization\_id**<br>_optional_ | ID of the AppCustomization this instance was launched from (null for vanilla) | string |
| **version**<br>_optional_ | The version of the application template | string |

## apps.details\_page\_enum [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#appsdetails_page_enum "Direct link to apps.details_page_enum")

_Type_ : enum (task, project)

## apps.task\_status\_enum [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#appstask_status_enum "Direct link to apps.task_status_enum")

_Type_ : enum (created, queued, in\_progress, stopped, published, publishing, closed, failed, completed, unknown)

## auth.credential\_key [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#authcredential_key "Direct link to auth.credential_key")

| Name | Description | Schema |
| --- | --- | --- |
| **access\_key**<br>_optional_ |  | string |
| **created**<br>_optional_ |  | string (date-time) |
| **expire**<br>_optional_ | Credential expiration time (UTC) | string (date-time) |
| **label**<br>_optional_ | Optional credentials label | string |
| **last\_used**<br>_optional_ |  | string (date-time) |
| **last\_used\_from**<br>_optional_ |  | string |

## auth.credentials [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#authcredentials "Direct link to auth.credentials")

| Name | Description | Schema |
| --- | --- | --- |
| **access\_key**<br>_optional_ | Credentials access key | string |
| **expire**<br>_optional_ | Credential expiration time (UTC) | string (date-time) |
| **label**<br>_optional_ | Optional credentials label | string |
| **secret\_key**<br>_optional_ | Credentials secret key | string |

## auth.role [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#authrole "Direct link to auth.role")

_Type_ : enum (admin, superuser, user, annotator, consumer)

## billing.payment\_details [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#billingpayment_details "Direct link to billing.payment_details")

The last payment details

| Name | Schema |
| --- | --- |
| **amount**<br>_optional_ | string |
| **currency**<br>_optional_ | string |
| **next\_retry\_date**<br>_optional_ | string |
| **status**<br>_optional_ | enum (failed, succeeded) |
| **time**<br>_optional_ | string (date-time) |

## billing.resource\_usage [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#billingresource_usage "Direct link to billing.resource_usage")

Resource usage

| Name | Description | Schema |
| --- | --- | --- |
| **base**<br>_optional_ | The free amount of the resource for the paid tier. Not relevant for the free <br>tier | number |
| **details**<br>_optional_ | Resource usage per app | object |
| **limit**<br>_optional_ | The limit for the resource usage | number |
| **payment**<br>_optional_ | The payment for the resoure due to the current usage. Not relevant for the free <br>tier | number |
| **used**<br>_optional_ | The used amount of the resource | number |

## datasets.dataset [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#datasetsdataset "Direct link to datasets.dataset")

| Name | Description | Schema |
| --- | --- | --- |
| **comment**<br>_optional_ |  | string |
| **company**<br>_optional_ | Company ID | string |
| **created**<br>_optional_ | Dataset creation time (UTC) | string (date-time) |
| **display\_stats**<br>_optional_ | Calculated statistics for the latest committed or published version | [datasets.statistics](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#datasets-statistics) |
| **display\_version\_name**<br>_optional_ | The name of the version from which statistics are taken | string |
| **head\_version**<br>_optional_ | The most recent version for write operations. Calculated as the non-published <br>version with the longest path to the root. | [datasets.version](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#datasets-version) |
| **id**<br>_optional_ | Dataset ID | string |
| **last\_update**<br>_optional_ | Time of last update (UTC). Updated on dataset update; on any version operation: <br>when version is created, modified, committed, published or deleted; and on any <br>frame operation: when frames are added, modified or deleted. | string (date-time) |
| **metadata**<br>_optional_ | User-provided metadata | object |
| **name**<br>_optional_ | Dataset name | string |
| **paradigm**<br>_optional_ | 'single\_version' for datasets whose version tree has only one path, 'general' <br>otherwise | [datasets.version\_paradigm\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#datasets-version_paradigm_enum) |
| **project**<br>_optional_ | Associated project ID | string |
| **system\_tags**<br>_optional_ | List of system tags. This field is reserved for system use, please don't use <br>it. | < string > array |
| **tags**<br>_optional_ | List of user-defined tags | < string > array |
| **terms\_of\_use**<br>_optional_ | Terms of use string | string |
| **user**<br>_optional_ | Associated user ID | string |
| **version\_count**<br>_optional_ | Amount of versions in dataset. Only supported by datasets.get\_all. | integer |

## datasets.frame [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#datasetsframe "Direct link to datasets.frame")

| Name | Description | Schema |
| --- | --- | --- |
| **blob**<br>_optional_ | Raw data (blob) for the frame | string |
| **context\_id**<br>_optional_ | Context ID. Used for the default frames sorting. If not set then it is filled <br>from the uri of the first source. | string |
| **id**<br>_optional_ | Frame id. Must be unique within the dataset's version. If already exists, will <br>cause existing frame to be updated | string |
| **meta**<br>_optional_ | Additional metadata dictionary for the frame. Please note that using this field <br>effectively defines a schema (dictionary structure and types used as values) - <br>frames within the same dataset cannot use conflicting schemas for this field <br>(see documentation for more details). | object |
| **meta\_blob**<br>_optional_ | Non searchable metadata dictionary for the frame. The fields in this object <br>cannot be searched by and are not added to the frame schema | object |
| **rois**<br>_optional_ | Frame regions of interest | < [datasets.roi](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#datasets-roi) \> array |
| **sources**<br>_required_ | Sources of this frame | < [datasets.source](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#datasets-source) \> array |
| **timestamp**<br>_optional_ | Frame's offset in milliseconds, used primarily for video content. Used for the <br>default frames sorting as the secondary key (with the primary key being <br>'context\_id'). For images, this value should typically be 0. If not set, value <br>is filled from the timestamp of the first source. We recommend using this field <br>only in cases concerning the default sorting behavior. | integer |

## datasets.frame\_15 [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#datasetsframe_15 "Direct link to datasets.frame_15")

| Name | Description | Schema |
| --- | --- | --- |
| **blob**<br>_optional_ | Raw data (blob) for the frame | string |
| **content\_type**<br>_optional_ | Frame content type (e.g. 'image/jpeg', 'image/png') | string |
| **context\_id**<br>_optional_ | Context ID. Used for the default frames sorting. If not set then it is filled <br>from the uri of the first source. | string |
| **height**<br>_optional_ | Frame height in pixels | integer |
| **id**<br>_optional_ | Frame id. Must be unique within the dataset's version. If already exists, will <br>cause existing frame to be updated | string |
| **meta**<br>_optional_ | Additional metadata dictionary for the frame. Please note that using this field <br>effectively defines a schema (dictionary structure and types used as values) - <br>frames within the same dataset cannot use conflicting schemas for this field <br>(see documentation for more details). | object |
| **rois**<br>_optional_ | Frame regions of interest | < [datasets.roi](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#datasets-roi) \> array |
| **sources**<br>_required_ | Sources of this frame | < [datasets.source](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#datasets-source) \> array |
| **src**<br>_optional_ | Frame source data URI | string |
| **timestamp**<br>_optional_ | Frame's offset in milliseconds, used primarily for video content. Used for the <br>default frames sorting as the secondary key (with the primary key being <br>'context\_id'). For images, this value should typically be 0. If not set, value <br>is filled from the timestamp of the first source. We recommend using this field <br>only in cases concerning the default sorting behavior. | integer |
| **width**<br>_optional_ | Frame width in pixels | integer |

## datasets.mask [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#datasetsmask "Direct link to datasets.mask")

| Name | Description | Schema |
| --- | --- | --- |
| **content\_type**<br>_optional_ | Content type (e.g. 'image/jpeg', 'image/png') | string |
| **height**<br>_optional_ | Height in pixels | integer |
| **id**<br>_required_ | unique ID (in this frame) | string |
| **timestamp**<br>_optional_ | Timestamp in the source data (for video content. for images, this value should <br>be 0) | integer |
| **uri**<br>_required_ | Data URI | string |
| **width**<br>_optional_ | Width in pixels | integer |

## datasets.multi\_field\_pattern\_data [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#datasetsmulti_field_pattern_data "Direct link to datasets.multi_field_pattern_data")

| Name | Description | Schema |
| --- | --- | --- |
| **datetime**<br>_optional_ | Date time conditions (applicable only to datetime fields). Either 'pattern' or <br>'datetime' should be specified | string |
| **fields**<br>_optional_ | List of field names | < string > array |
| **pattern**<br>_optional_ | Pattern string (regex). Either 'pattern' or 'datetime' should be specified | string |

## datasets.preview [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#datasetspreview "Direct link to datasets.preview")

| Name | Description | Schema |
| --- | --- | --- |
| **content\_type**<br>_optional_ | Content type (e.g. 'image/jpeg', 'image/png') | string |
| **height**<br>_optional_ | Height in pixels | integer |
| **timestamp**<br>_optional_ | Timestamp in the source data (for video content. for images, this value should <br>be 0) | integer |
| **uri**<br>_required_ | Data URI | string |
| **width**<br>_optional_ | Width in pixels | integer |

## datasets.roi [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#datasetsroi "Direct link to datasets.roi")

| Name | Description | Schema |
| --- | --- | --- |
| **confidence**<br>_optional_ | ROI confidence | number |
| **id**<br>_optional_ | ROI id | string |
| **label**<br>_required_ | ROI labels | < string > array |
| **mask**<br>_optional_ | Mask info for this ROI | [datasets.roi\_mask](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#datasets-roi_mask) |
| **meta**<br>_optional_ | Additional metadata dictionary for the roi | object |
| **poly**<br>_optional_ | ROI polygon (x0, y0, ..., xn, yn) | < number > array |
| **sources**<br>_optional_ | Source ID | < string > array |

## datasets.roi\_mask [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#datasetsroi_mask "Direct link to datasets.roi_mask")

| Name | Description | Schema |
| --- | --- | --- |
| **id**<br>_required_ | Mask ID | string |
| **value**<br>_required_ | Mask value | < integer > array |

## datasets.schema\_type\_enum [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#datasetsschema_type_enum "Direct link to datasets.schema_type_enum")

_Type_ : enum (frame, source, roi, all)

## datasets.source [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#datasetssource "Direct link to datasets.source")

| Name | Description | Schema |
| --- | --- | --- |
| **content\_type**<br>_optional_ | Content type (e.g. 'image/jpeg', 'image/png') | string |
| **height**<br>_optional_ | Height in pixels | integer |
| **id**<br>_required_ | Source unique ID within this DatasetVersion | string |
| **masks**<br>_optional_ |  | < [datasets.mask](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#datasets-mask) \> array |
| **meta**<br>_optional_ | Additional metadata dictionary for the source | object |
| **preview**<br>_optional_ |  | [datasets.preview](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#datasets-preview) |
| **timestamp**<br>_optional_ | Timestamp in the source data (for video content. for images, this value should <br>be 0) | integer |
| **uri**<br>_required_ | Source data URI | string |
| **width**<br>_optional_ | Width in pixels | integer |

## datasets.stat\_count [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#datasetsstat_count "Direct link to datasets.stat_count")

| Name | Description | Schema |
| --- | --- | --- |
| **count**<br>_optional_ | Item name | integer |
| **name**<br>_optional_ | Number of appearances | string |

## datasets.statistics [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#datasetsstatistics "Direct link to datasets.statistics")

| Name | Schema |
| --- | --- |
| **content\_types**<br>_optional_ | < [datasets.stat\_count](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#datasets-stat_count) \> array |
| **frames**<br>_optional_ | < [datasets.stat\_count](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#datasets-stat_count) \> array |
| **labels**<br>_optional_ | < [datasets.stat\_count](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#datasets-stat_count) \> array |

## datasets.version [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#datasetsversion "Direct link to datasets.version")

| Name | Description | Schema |
| --- | --- | --- |
| **comment**<br>_optional_ | Version comment | string |
| **committed**<br>_optional_ | Commit time | string (date-time) |
| **committed\_frames\_ts**<br>_optional_ | Timestamp of last committed frame | number |
| **committed\_rois\_ts**<br>_optional_ | Timestamp of last committed ROI | number |
| **company**<br>_optional_ | Company ID | string |
| **created**<br>_optional_ | Version creation time (UTC) | string (date-time) |
| **dataset**<br>_optional_ | Datset ID | string |
| **es\_index**<br>_optional_ | Name of elasticsearch index | string |
| **id**<br>_optional_ | Version ID | string |
| **last\_frames\_update**<br>_optional_ | Last time version was created, committed or frames were updated or saved | string (date-time) |
| **metadata**<br>_optional_ | User-provided metadata | object |
| **name**<br>_optional_ | Version name | string |
| **parent**<br>_optional_ | Version parent ID | string |
| **published**<br>_optional_ | Publish time | string (date-time) |
| **stats**<br>_optional_ | Version statistics | [datasets.statistics](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#datasets-statistics) |
| **status**<br>_optional_ | Version status | [datasets.version\_status\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#datasets-version_status_enum) |
| **system\_tags**<br>_optional_ | List of system tags. This field is reserved for system use, please don't use <br>it. | < string > array |
| **tags**<br>_optional_ | List of user-defined tags | < string > array |
| **task**<br>_optional_ | Task ID of the task which created the version | string |
| **user**<br>_optional_ | Associated user ID | string |

## datasets.version\_paradigm\_enum [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#datasetsversion_paradigm_enum "Direct link to datasets.version_paradigm_enum")

_Type_ : enum (single\_version, general)

## datasets.version\_status\_enum [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#datasetsversion_status_enum "Direct link to datasets.version_status_enum")

_Type_ : enum (draft, committing, committed, published)

## dataviews.augmentation [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#dataviewsaugmentation "Direct link to dataviews.augmentation")

| Name | Description | Schema |
| --- | --- | --- |
| **crop\_around\_rois**<br>_optional_ | Crop image data around all frame ROIs | boolean |
| **sets**<br>_optional_ | List of augmentation sets | < [dataviews.augmentation\_set](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#dataviews-augmentation_set) \> array |

## dataviews.augmentation\_set [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#dataviewsaugmentation_set "Direct link to dataviews.augmentation_set")

| Name | Description | Schema |
| --- | --- | --- |
| **arguments**<br>_optional_ | Arguments dictionary per custom augmentation type. | < string, object > map |
| **cls**<br>_optional_ | Augmentation class | string |
| **strength**<br>_optional_ | Augmentation strength. Range \[0,). <br>**Minimum value** : `0` | number |\
| **types**<br>_optional_ | Augmentation type | < string > array |\
\
## dataviews.dataview [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#dataviewsdataview "Direct link to dataviews.dataview")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **augmentation**<br>_optional_ | Augmentation parameters. Only for training and testing tasks. | [dataviews.augmentation](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#dataviews-augmentation) |\
| **company**<br>_optional_ | Company id | string |\
| **created**<br>_optional_ | Dataview creation time (UTC) | string (date-time) |\
| **description**<br>_optional_ | Dataview description | string |\
| **filters**<br>_optional_ | List of FilterRule ('OR' connection) | < [dataviews.filter\_rule](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#dataviews-filter_rule) \> array |\
| **id**<br>_required_ | Dataview ID | string |\
| **iteration**<br>_optional_ | Iteration parameters. Not applicable for register (import) tasks. | [dataviews.iteration](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#dataviews-iteration) |\
| **labels\_enumeration**<br>_optional_ | Labels enumerations, specifies numbers to be assigned to ROI labels when <br>getting frames | < string, integer > map |\
| **mapping**<br>_optional_ | Mapping parameters | [dataviews.mapping](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#dataviews-mapping) |\
| **name**<br>_required_ | Dataview name | string |\
| **output\_rois**<br>_optional_ | 'all\_in\_frame' - all rois for a frame are returned 'only\_filtered' - only rois <br>which led this frame to be selected 'frame\_per\_roi' - single roi per frame. <br>Frame can be returned multiple times with a different roi each time. Note: this <br>should be used for Training tasks only Note: frame\_per\_roi implies that only <br>filtered rois will be returned | [dataviews.output\_rois\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#dataviews-output_rois_enum) |\
| **project**<br>_optional_ | Project ID of the project to which this task is assigned | string |\
| **system\_tags**<br>_optional_ | System tags list. This field is reserved for system use, please don't use it. | < string > array |\
| **tags**<br>_optional_ | User-defined tags list | < string > array |\
| **user**<br>_optional_ | Associated user id | string |\
| **versions**<br>_optional_ | List of dataview entries. All tasks must have at least one dataview. | < [dataviews.dataview\_entry](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#dataviews-dataview_entry) \> array |\
\
## dataviews.dataview\_entry [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#dataviewsdataview_entry "Direct link to dataviews.dataview_entry")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **dataset**<br>_required_ | Existing Dataset id | string |\
| **merge\_with**<br>_optional_ | Version ID to merge with | string |\
| **version**<br>_required_ | Version id of a version belonging to the dataset | string |\
\
## dataviews.filter\_by\_roi\_enum [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#dataviewsfilter_by_roi_enum "Direct link to dataviews.filter_by_roi_enum")\
\
_Type_ : enum (disabled, no\_rois, label\_rules)\
\
## dataviews.filter\_label\_rule [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#dataviewsfilter_label_rule "Direct link to dataviews.filter_label_rule")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **conf\_range**<br>_optional_ | Range of ROI confidence level in the frame (min, max). -1 for not applicable <br>Both min and max can be either -1 or positive. 2nd number (max) must be either <br>-1 or larger than or equal to the 1st number (min) | < number > array |\
| **count\_range**<br>_optional_ | Range of times ROI appears in the frame (min, max). -1 for not applicable. Both <br>integers must be larger than or equal to -1. 2nd integer (max) must be either <br>-1 or larger than or equal to the 1st integer (min) | < integer > array |\
| **label**<br>_required_ | Lucene format query (see lucene query syntax). Default search field is <br>label.keyword and default operator is AND, so searching for: <br>'Bus Stop' Blue <br>is equivalent to: <br>Label.keyword:'Bus Stop' AND label.keyword:'Blue' | string |\
| **must\_not**<br>_optional_ | If set then the label must not exist or lucene query must not be true. The <br>default value is false <br>**Default** : `false` | boolean |\
\
## dataviews.filter\_rule [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#dataviewsfilter_rule "Direct link to dataviews.filter_rule")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **dataset**<br>_required_ | Dataset ID. Must be a dataset which is in the task's view. If set to '\*' all <br>datasets in View are used. | string |\
| **filter\_by\_roi**<br>_optional_ | Type of filter. Optional, the default value is 'label\_rules' | [dataviews.filter\_by\_roi\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#dataviews-filter_by_roi_enum) |\
| **frame\_query**<br>_optional_ | Frame filter, in Lucene query syntax | string |\
| **label\_rules**<br>_optional_ | List of FilterLabelRule ('AND' connection) <br>disabled - No filtering by ROIs. Select all frames, even if they don't have <br>ROIs (all frames) <br>no\_rois - Select only frames without ROIs (empty frames) <br>label\_rules - Select frames according to label rules | < [dataviews.filter\_label\_rule](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#dataviews-filter_label_rule) \> array |\
| **sources\_query**<br>_optional_ | Sources filter, in Lucene query syntax. Filters sources in each frame. | string |\
| **vector\_search**<br>_optional_ | Vector search rule | [vector\_search](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#dataviews-filter_rule-vector_search) |\
| **version**<br>_optional_ | Dataset version to apply rule to. Must belong to the dataset and be in the <br>task's view. If set to '\*' all version of the datasets in View are used. | string |\
| **weight**<br>_optional_ | Rule weight. Default is 1 | number |\
\
**vector\_search**\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **field**<br>_required_ | Vector field name | string |\
| **min\_score**<br>_optional_ | Min allowed score | number |\
| **similarity\_func**<br>_optional_ | The function for calculating distance from the search vector | [dataviews.similarity\_function](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#dataviews-similarity_function) |\
| **sort**<br>_optional_ |  | enum (asc, desc) |\
| **vector**<br>_required_ | The search vector | < number > array |\
\
## dataviews.iteration [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#dataviewsiteration "Direct link to dataviews.iteration")\
\
Sequential Iteration API configuration\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **infinite**<br>_optional_ | Infinite iteration | boolean |\
| **jump**<br>_optional_ | Jump entry | [dataviews.jump](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#dataviews-jump) |\
| **limit**<br>_optional_ | Maximum frames per task. If not passed, frames will end when no more matching <br>frames are found, unless infinite is True. | integer |\
| **min\_sequence**<br>_optional_ | Length (in ms) of video clips to return. This is used in random order, and in <br>sequential order only if jumping is provided and only for video frames | integer |\
| **order**<br>_optional_ | Input frames order. Values: 'sequential', 'random' In Sequential mode frames <br>will be returned according to the order in which the frames were added to the <br>dataset. | [dataviews.iteration\_order\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#dataviews-iteration_order_enum) |\
| **random\_seed**<br>_optional_ | Random seed used when iterating over the dataview | integer |\
\
## dataviews.iteration\_order\_enum [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#dataviewsiteration_order_enum "Direct link to dataviews.iteration_order_enum")\
\
_Type_ : enum (sequential, random)\
\
## dataviews.jump [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#dataviewsjump "Direct link to dataviews.jump")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **time**<br>_optional_ | Max time in milliseconds between frames | integer |\
\
## dataviews.label\_source [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#dataviewslabel_source "Direct link to dataviews.label_source")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **dataset**<br>_optional_ | Source dataset id. '\*' for all datasets in view | string |\
| **labels**<br>_optional_ | List of source labels (AND connection). '\*' indicates any label. Labels must <br>exist in at least one of the dataset versions in the task's view | < string > array |\
| **version**<br>_optional_ | Source dataset version id. Default is '\*' (for all versions in dataset in the <br>view) Version must belong to the selected dataset, and must be in the task's <br>view\[i\] | string |\
\
## dataviews.mapping [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#dataviewsmapping "Direct link to dataviews.mapping")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **rules**<br>_optional_ | Rules list | < [dataviews.mapping\_rule](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#dataviews-mapping_rule) \> array |\
\
## dataviews.mapping\_rule [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#dataviewsmapping_rule "Direct link to dataviews.mapping_rule")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **source**<br>_optional_ | Source label info | [dataviews.label\_source](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#dataviews-label_source) |\
| **target**<br>_optional_ | Target label name | string |\
\
## dataviews.multi\_field\_pattern\_data [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#dataviewsmulti_field_pattern_data "Direct link to dataviews.multi_field_pattern_data")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **datetime**<br>_optional_ | Date time conditions (applicable only to datetime fields). Either 'pattern' or <br>'datetime' should be specified | string |\
| **fields**<br>_optional_ | List of field names | < string > array |\
| **pattern**<br>_optional_ | Pattern string (regex). Either 'pattern' or 'datetime' should be specified | string |\
\
## dataviews.output\_rois\_enum [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#dataviewsoutput_rois_enum "Direct link to dataviews.output_rois_enum")\
\
_Type_ : enum (all\_in\_frame, only\_filtered, frame\_per\_roi)\
\
## dataviews.similarity\_function [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#dataviewssimilarity_function "Direct link to dataviews.similarity_function")\
\
_Type_ : enum (l2\_norm, dot\_product, cosine)\
\
## events.debug\_image\_sample\_response [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#eventsdebug_image_sample_response "Direct link to events.debug_image_sample_response")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **event**<br>_optional_ | Debug image event | object |\
| **max\_iteration**<br>_optional_ | maximal valid iteration for the variant | integer |\
| **min\_iteration**<br>_optional_ | minimal valid iteration for the variant | integer |\
| **scroll\_id**<br>_optional_ | Scroll ID to pass to the next calls to get\_debug\_image\_sample or <br>next\_debug\_image\_sample | string |\
\
## events.debug\_images\_response [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#eventsdebug_images_response "Direct link to events.debug_images_response")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **metrics**<br>_optional_ | Debug image events grouped by tasks and iterations | < [events.debug\_images\_response\_task\_metrics](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#events-debug_images_response_task_metrics) \> array |\
| **scroll\_id**<br>_optional_ | Scroll ID for getting more results | string |\
\
## events.debug\_images\_response\_task\_metrics [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#eventsdebug_images_response_task_metrics "Direct link to events.debug_images_response_task_metrics")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **iterations**<br>_optional_ |  | < [iterations](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#events-debug_images_response_task_metrics-iterations) \> array |\
| **task**<br>_optional_ | Task ID | string |\
\
**iterations**\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **events**<br>_optional_ |  | < object > array |\
| **iter**<br>_optional_ | Iteration number | integer |\
\
## events.event\_type\_enum [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#eventsevent_type_enum "Direct link to events.event_type_enum")\
\
_Type_ : enum (training\_stats\_scalar, training\_stats\_vector, training\_debug\_image, plot, log)\
\
## events.log\_level\_enum [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#eventslog_level_enum "Direct link to events.log_level_enum")\
\
_Type_ : enum (notset, debug, verbose, info, warn, warning, error, fatal, critical)\
\
## events.metric\_variants [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#eventsmetric_variants "Direct link to events.metric_variants")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **metric**<br>_optional_ | The metric name | string |\
| **variants**<br>_optional_ | The names of the metric variants | < string > array |\
\
## events.metrics\_image\_event [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#eventsmetrics_image_event "Direct link to events.metrics_image_event")\
\
An image or video was dumped to storage for debugging\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **iter**<br>_optional_ | Iteration | integer |\
| **key**<br>_optional_ | File key | string |\
| **metric**<br>_optional_ | Metric name, e.g. 'count', 'loss', 'accuracy' | string |\
| **task**<br>_required_ | Task ID (required) | string |\
| **timestamp**<br>_optional_ | Epoch milliseconds UTC, will be set by the server if not set. | number |\
| **type**<br>_required_ | 'training\_debug\_image' | string |\
| **url**<br>_optional_ | File URL | string |\
| **variant**<br>_optional_ | E.g. 'class\_1', 'total', 'average | string |\
\
## events.metrics\_plot\_event [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#eventsmetrics_plot_event "Direct link to events.metrics_plot_event")\
\
An entire plot (not single datapoint) and it's layout. Used for plotting ROC\
\
curves, confidence matrices, etc. when evaluating the net.\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **iter**<br>_optional_ | Iteration | integer |\
| **metric**<br>_optional_ | Metric name, e.g. 'count', 'loss', 'accuracy' | string |\
| **plot\_str**<br>_optional_ | An entire plot (not single datapoint) and it's layout. Used for plotting ROC <br>curves, confidence matrices, etc. when evaluating the net. | string |\
| **skip\_validation**<br>_optional_ | If set then plot\_str is not checked for a valid json. The default is False | boolean |\
| **task**<br>_required_ | Task ID (required) | string |\
| **timestamp**<br>_optional_ | Epoch milliseconds UTC, will be set by the server if not set. | number |\
| **type**<br>_required_ | 'plot' | string |\
| **variant**<br>_optional_ | E.g. 'class\_1', 'total', 'average | string |\
\
## events.metrics\_scalar\_event [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#eventsmetrics_scalar_event "Direct link to events.metrics_scalar_event")\
\
Used for reporting scalar metrics during training task\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **iter**<br>_optional_ | Iteration | integer |\
| **metric**<br>_optional_ | Metric name, e.g. 'count', 'loss', 'accuracy' | string |\
| **task**<br>_required_ | Task ID (required) | string |\
| **timestamp**<br>_optional_ | Epoch milliseconds UTC, will be set by the server if not set. | number |\
| **type**<br>_required_ | 'training\_stats\_scalar' | string |\
| **value**<br>_optional_ |  | number |\
| **variant**<br>_optional_ | E.g. 'class\_1', 'total', 'average' | string |\
| **x\_axis\_label**<br>_optional_ | Custom X-Axis label to be used when displaying the scalars histogram | string |\
\
## events.metrics\_vector\_event [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#eventsmetrics_vector_event "Direct link to events.metrics_vector_event")\
\
Used for reporting vector metrics during training task\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **iter**<br>_optional_ | Iteration | integer |\
| **metric**<br>_optional_ | Metric name, e.g. 'count', 'loss', 'accuracy' | string |\
| **task**<br>_required_ | Task ID (required) | string |\
| **timestamp**<br>_optional_ | Epoch milliseconds UTC, will be set by the server if not set. | number |\
| **type**<br>_optional_ | 'training\_stats\_vector' | string |\
| **values**<br>_optional_ | vector of float values | < number > array |\
| **variant**<br>_optional_ | E.g. 'class\_1', 'total', 'average | string |\
\
## events.plot\_sample\_response [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#eventsplot_sample_response "Direct link to events.plot_sample_response")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **events**<br>_optional_ | Plot events | < object > array |\
| **max\_iteration**<br>_optional_ | maximal valid iteration for the metric | integer |\
| **min\_iteration**<br>_optional_ | minimal valid iteration for the metric | integer |\
| **scroll\_id**<br>_optional_ | Scroll ID to pass to the next calls to get\_plot\_sample or next\_plot\_sample | string |\
\
## events.plots\_response [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#eventsplots_response "Direct link to events.plots_response")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **metrics**<br>_optional_ | Plot events grouped by tasks and iterations | < [events.plots\_response\_task\_metrics](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#events-plots_response_task_metrics) \> array |\
| **scroll\_id**<br>_optional_ | Scroll ID for getting more results | string |\
\
## events.plots\_response\_task\_metrics [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#eventsplots_response_task_metrics "Direct link to events.plots_response_task_metrics")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **iterations**<br>_optional_ |  | < [iterations](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#events-plots_response_task_metrics-iterations) \> array |\
| **task**<br>_optional_ | Task ID | string |\
\
**iterations**\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **events**<br>_optional_ |  | < object > array |\
| **iter**<br>_optional_ | Iteration number | integer |\
\
## events.scalar\_key\_enum [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#eventsscalar_key_enum "Direct link to events.scalar_key_enum")\
\
_Type_ : enum (iter, timestamp, iso\_time)\
\
## events.single\_value\_metrics\_response [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#eventssingle_value_metrics_response "Direct link to events.single_value_metrics_response")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **tasks**<br>_optional_ | Single value metrics grouped by task | < [events.single\_value\_task\_metrics](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#events-single_value_task_metrics) \> array |\
\
## events.single\_value\_task\_metrics [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#eventssingle_value_task_metrics "Direct link to events.single_value_task_metrics")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **task**<br>_optional_ | Task ID | string |\
| **task\_name**<br>_optional_ | Task name | string |\
| **values**<br>_optional_ |  | < [values](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#events-single_value_task_metrics-values) \> array |\
\
**values**\
\
| Name | Schema |\
| --- | --- |\
| **metric**<br>_optional_ | string |\
| **timestamp**<br>_optional_ | number |\
| **value**<br>_optional_ | number |\
| **variant**<br>_optional_ | string |\
\
## events.task\_log\_event [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#eventstask_log_event "Direct link to events.task_log_event")\
\
A log event associated with a task.\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **level**<br>_optional_ | Log level. | [events.log\_level\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#events-log_level_enum) |\
| **msg**<br>_optional_ | Log message. | string |\
| **task**<br>_required_ | Task ID (required) | string |\
| **timestamp**<br>_optional_ | Epoch milliseconds UTC, will be set by the server if not set. | number |\
| **type**<br>_required_ | 'log' | string |\
| **worker**<br>_optional_ | Name of machine running the task. | string |\
\
## events.task\_metric [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#eventstask_metric "Direct link to events.task_metric")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **metric**<br>_optional_ | Metric name | string |\
| **task**<br>_required_ | Task ID | string |\
\
## events.task\_metric\_variants [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#eventstask_metric_variants "Direct link to events.task_metric_variants")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **metric**<br>_optional_ | Metric name | string |\
| **task**<br>_required_ | Task ID | string |\
| **variants**<br>_optional_ | Metric variant names | < string > array |\
\
## frames.augmentation [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#framesaugmentation "Direct link to frames.augmentation")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **arguments**<br>_optional_ | Arguments dictionary, passed to custom augmentations. | object |\
| **cls**<br>_optional_ | Augmentation class (see global definitions) | string |\
| **params**<br>_optional_ | Transform parameters, an array ot 3 randomly generated values. Fixed values are <br>passed in case of affine reflect augmentation. | < number > array |\
| **strength**<br>_optional_ | Transform strength. Required for pixel transforms. | number |\
| **trans\_mat**<br>_optional_ | Transform matrix (list of lists). Required for affine transforms. | < < number > array > array |\
| **type**<br>_optional_ | Augmentation type (see global definitions) | string |\
\
## frames.dataset\_version [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#framesdataset_version "Direct link to frames.dataset_version")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **id**<br>_optional_ | Dataset id | string |\
| **version**<br>_optional_ | Dataset version id | string |\
\
## frames.dataview [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#framesdataview "Direct link to frames.dataview")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **augmentation**<br>_optional_ | Augmentation parameters. Only for training and testing tasks. | [frames.dv\_augmentation](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#frames-dv_augmentation) |\
| **filters**<br>_optional_ | List of FilterRule ('OR' relationship) | < [frames.filter\_rule](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#frames-filter_rule) \> array |\
| **iteration**<br>_optional_ | Iteration parameters. Not applicable for register (import) tasks. | [frames.iteration](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#frames-iteration) |\
| **labels\_enumeration**<br>_optional_ | Labels enumerations, specifies numbers to be assigned to ROI labels when <br>getting frames | < string, integer > map |\
| **mapping**<br>_optional_ | Mapping parameters | [frames.mapping](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#frames-mapping) |\
| **output\_rois**<br>_optional_ | 'all\_in\_frame' - all rois for a frame are returned <br>'only\_filtered' - only rois which led this frame to be selected <br>'frame\_per\_roi' - single roi per frame. Frame can be returned multiple times <br>with a different roi each time. <br>Note: this should be used for Training tasks only <br>Note: frame\_per\_roi implies that only filtered rois will be returned | [frames.output\_rois\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#frames-output_rois_enum) |\
| **versions**<br>_optional_ | View dataset versions | < [frames.view\_entry](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#frames-view_entry) \> array |\
\
## frames.dv\_augmentation [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#framesdv_augmentation "Direct link to frames.dv_augmentation")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **crop\_around\_rois**<br>_optional_ | Crop image data around all frame ROIs | boolean |\
| **sets**<br>_optional_ | List of augmentation sets | < [frames.dv\_augmentation\_set](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#frames-dv_augmentation_set) \> array |\
\
## frames.dv\_augmentation\_set [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#framesdv_augmentation_set "Direct link to frames.dv_augmentation_set")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **arguments**<br>_optional_ | Arguments dictionary per custom augmentation type. | < string, object > map |\
| **cls**<br>_optional_ | Augmentation class | string |\
| **strength**<br>_optional_ | Augmentation strength. Range \[0,). <br>**Minimum value** : `0` | number |\
| **types**<br>_optional_ | Augmentation type | < string > array |\
\
## frames.filter\_by\_roi\_enum [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#framesfilter_by_roi_enum "Direct link to frames.filter_by_roi_enum")\
\
_Type_ : enum (disabled, no\_rois, label\_rules)\
\
## frames.filter\_label\_rule [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#framesfilter_label_rule "Direct link to frames.filter_label_rule")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **conf\_range**<br>_optional_ | Range of ROI confidence level in the frame (min, max). -1 for not applicable <br>Both min and max can be either -1 or positive. 2nd number (max) must be either <br>-1 or larger than or equal to the 1st number (min) | < number > array |\
| **count\_range**<br>_optional_ | Range of times ROI appears in the frame (min, max). -1 for not applicable. Both <br>integers must be larger than or equal to -1. 2nd integer (max) must be either <br>-1 or larger than or equal to the 1st integer (min) | < integer > array |\
| **label**<br>_required_ | Lucene format query (see lucene query syntax). Default search field is <br>label.keyword and default operator is AND, so searching for: <br>'Bus Stop' Blue <br>is equivalent to: <br>Label.keyword:'Bus Stop' AND label.keyword:'Blue' | string |\
| **must\_not**<br>_optional_ | If set then the label must not exist or lucene query must not be true. The <br>default value is false <br>**Default** : `false` | boolean |\
\
## frames.filter\_rule [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#framesfilter_rule "Direct link to frames.filter_rule")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **dataset**<br>_required_ | Dataset ID. Must be a dataset which is in the task's view. If set to '\*' all <br>datasets in View are used. | string |\
| **filter\_by\_roi**<br>_optional_ | Type of filter. Optional, the default value is 'label\_rules' | [frames.filter\_by\_roi\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#frames-filter_by_roi_enum) |\
| **frame\_query**<br>_optional_ | Frame filter, in Lucene query syntax | string |\
| **label\_rules**<br>_optional_ | List of FilterLabelRule ('AND' connection) <br>disabled - No filtering by ROIs. Select all frames, even if they don't have <br>ROIs (all frames) <br>no\_rois - Select only frames without ROIs (empty frames) <br>label\_rules - Select frames according to label rules | < [frames.filter\_label\_rule](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#frames-filter_label_rule) \> array |\
| **sources\_query**<br>_optional_ | Sources filter, in Lucene query syntax. Filters sources in each frame. | string |\
| **vector\_search**<br>_optional_ | Vector search rule | [vector\_search](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#frames-filter_rule-vector_search) |\
| **version**<br>_optional_ | Dataset version to apply rule to. Must belong to the dataset and be in the <br>task's view. If set to '\*' all version of the datasets in View are used. | string |\
| **weight**<br>_optional_ | Rule weight. Default is 1 | number |\
\
**vector\_search**\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **field**<br>_required_ | Vector field name | string |\
| **min\_score**<br>_optional_ | Min allowed score | number |\
| **similarity\_func**<br>_optional_ | The function for calculating distance from the search vector | [frames.similarity\_function](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#frames-similarity_function) |\
| **sort**<br>_optional_ |  | enum (asc, desc) |\
| **vector**<br>_required_ | The search vector | < number > array |\
\
## frames.flow\_control [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#framesflow_control "Direct link to frames.flow_control")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **bidirectional**<br>_optional_ | If set then frames retreival can go either forward or backwards. Otherwise only <br>forward. The default is False. The limitations of bidirectional navigation: - <br>Frames are always returned in sequential order - The iteration is finite (no <br>support for infinite iteration) | boolean |\
| **navigate\_backwards**<br>_optional_ | When bidirectional is True, settings this to True navigates backwards duing <br>frames retreival. Default is False | boolean |\
\
## frames.frame [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#framesframe "Direct link to frames.frame")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **augmentation**<br>_optional_ | List of augmentations | < [frames.augmentation](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#frames-augmentation) \> array |\
| **blob**<br>_optional_ | Raw data (blob) for the frame | string |\
| **context\_id**<br>_optional_ | Context ID. Used for the default frames sorting. If not set then it is filled <br>from the uri of the first source. | string |\
| **dataset**<br>_optional_ | Frame's dataset version | [frames.dataset\_version](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#frames-dataset_version) |\
| **deleted**<br>_optional_ | Set to 'true' for the deleted frames | boolean |\
| **id**<br>_optional_ | Frame id | string |\
| **is\_key\_frame**<br>_optional_ | Is this a key frame (only applicable in frames who'se src is a video) | boolean |\
| **key\_frame**<br>_optional_ | ID of the key frame that this frame belongs to | string |\
| **label\_rule\_counts**<br>_optional_ | The number of matched roi per lable rule | object |\
| **labels\_size**<br>_optional_ | Number of labels returned | integer |\
| **meta**<br>_optional_ | Additional metadata dictionary for the frame. Please note that using this field <br>effectively defines a schema (dictionary structure and types used as values) - <br>frames within the same dataset cannot use conflicting schemas for this field <br>(see documentation for more details). | object |\
| **meta\_blob**<br>_optional_ | Non searchable metadata dictionary for the frame. The fields in this object <br>cannot be searched by and are not added to the frame schema | object |\
| **new\_ver**<br>_optional_ | Newer version of this frame, if asked to merge | [frames.frame](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#frames-frame) |\
| **rois**<br>_optional_ | Frame regions of interest | < [frames.roi](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#frames-roi) \> array |\
| **rule\_name**<br>_optional_ | Name of the filtering rule according to which this frame was provided (if <br>applicable) | string |\
| **saved**<br>_optional_ | Last time frame was saved (timestamp) | integer |\
| **saved\_in\_version**<br>_optional_ | Last version this frame was saved in (version ID) | string |\
| **sources**<br>_optional_ | Sources of this frame | < [frames.source](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#frames-source) \> array |\
| **timestamp**<br>_optional_ | Frame's offset in milliseconds, used primarily for video content. Used for the <br>default frames sorting as the secondary key (with the primary key being <br>'context\_id'). For images, this value should typically be 0. If not set, value <br>is filled from the timestamp of the first source. We recommend using this field <br>only in cases concerning the default sorting behavior. | integer |\
| **updated**<br>_optional_ | Last time frame was saved (timestamp) | integer |\
| **updated\_in\_version**<br>_optional_ | Last version this frame was updated in (version ID) | string |\
| **video\_gop**<br>_optional_ | Video encoding GOP value for the source of this frame. Only valid for video <br>frames | number |\
\
## frames.frame\_15 [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#framesframe_15 "Direct link to frames.frame_15")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **augmentation**<br>_optional_ | List of augmentations | < [frames.augmentation](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#frames-augmentation) \> array |\
| **blob**<br>_optional_ | Raw data (blob) for the frame | string |\
| **content\_type**<br>_optional_ | Frame content type (e.g. 'image/jpeg', 'image/png') | string |\
| **context\_id**<br>_optional_ | Context ID. Used for the default frames sorting. If not set then it is filled <br>from the uri of the first source. | string |\
| **dataset**<br>_optional_ | Frame's dataset version | [frames.dataset\_version](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#frames-dataset_version) |\
| **height**<br>_optional_ | Frame height in pixels | integer |\
| **id**<br>_optional_ | Frame id | string |\
| **is\_key\_frame**<br>_optional_ | Is this a key frame (only applicable in frames who'se src is a video) | boolean |\
| **key\_frame**<br>_optional_ | ID of the key frame that this frame belongs to | string |\
| **label\_stats**<br>_optional_ | Mapping of label name to number of appearances | object |\
| **labels\_size**<br>_optional_ | Number of labels returned | integer |\
| **meta**<br>_optional_ | Additional metadata dictionary for the frame. Please note that using this field <br>effectively defines a schema (dictionary structure and types used as values) - <br>frames within the same dataset cannot use conflicting schemas for this field <br>(see documentation for more details). | object |\
| **new\_ver**<br>_optional_ | Newer version of this frame, if asked to merge | [frames.frame\_15](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#frames-frame_15) |\
| **rois**<br>_optional_ | Frame regions of interest | < [frames.roi](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#frames-roi) \> array |\
| **rule\_name**<br>_optional_ | Name of the filtering rule according to which this frame was provided (if <br>applicable) | string |\
| **saved**<br>_optional_ | Last time frame was saved (timestamp) | integer |\
| **saved\_in\_version**<br>_optional_ | Last version this frame was saved in (version ID) | string |\
| **sources**<br>_optional_ | Sources of this frame | < [frames.source](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#frames-source) \> array |\
| **src**<br>_optional_ | Frame data URI | string |\
| **task**<br>_optional_ | Task which created the frame | string |\
| **timestamp**<br>_optional_ | Frame's offset in milliseconds, used primarily for video content. Used for the <br>default frames sorting as the secondary key (with the primary key being <br>'context\_id'). For images, this value should typically be 0. If not set, value <br>is filled from the timestamp of the first source. We recommend using this field <br>only in cases concerning the default sorting behavior. | integer |\
| **updated**<br>_optional_ | Last time frame was saved (timestamp) | integer |\
| **updated\_in\_version**<br>_optional_ | Last version this frame was updated in (version ID) | string |\
| **video\_gop**<br>_optional_ | Video encoding GOP value for the source of this frame. Only valid for video <br>frames | number |\
| **width**<br>_optional_ | Frame width in pixels | integer |\
\
## frames.iteration [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#framesiteration "Direct link to frames.iteration")\
\
Sequential Iteration API configuration\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **infinite**<br>_optional_ | Infinite iteration | boolean |\
| **jump**<br>_optional_ | Jump entry | [frames.jump](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#frames-jump) |\
| **limit**<br>_optional_ | Maximum frames per task. If not passed, frames will end when no more matching <br>frames are found, unless infinite is True. | integer |\
| **min\_sequence**<br>_optional_ | Length (in ms) of video clips to return. This is used in random order, and in <br>sequential order only if jumping is provided and only for video frames | integer |\
| **order**<br>_optional_ | Input frames order. Values: 'sequential', 'random' In Sequential mode frames <br>will be returned according to the order in which the frames were added to the <br>dataset. | [frames.iteration\_order\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#frames-iteration_order_enum) |\
| **random\_seed**<br>_optional_ | Random seed used when iterating over the dataview | integer |\
\
## frames.iteration\_order\_enum [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#framesiteration_order_enum "Direct link to frames.iteration_order_enum")\
\
_Type_ : enum (sequential, random)\
\
## frames.jump [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#framesjump "Direct link to frames.jump")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **time**<br>_optional_ | Max time in milliseconds between frames | integer |\
\
## frames.label\_source [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#frameslabel_source "Direct link to frames.label_source")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **dataset**<br>_optional_ | Source dataset id. '\*' for all datasets in view | string |\
| **labels**<br>_optional_ | List of source labels (AND connection). '\*' indicates any label. Labels must <br>exist in at least one of the dataset versions in the task's view | < string > array |\
| **version**<br>_optional_ | Source dataset version id. Default is '\*' (for all versions in dataset in the <br>view) Version must belong to the selected dataset, and must be in the task's <br>view\[i\] | string |\
\
## frames.mapping [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#framesmapping "Direct link to frames.mapping")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **rules**<br>_optional_ | Rules list | < [frames.mapping\_rule](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#frames-mapping_rule) \> array |\
\
## frames.mapping\_rule [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#framesmapping_rule "Direct link to frames.mapping_rule")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **source**<br>_optional_ | Source label info | [frames.label\_source](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#frames-label_source) |\
| **target**<br>_optional_ | Target label name | string |\
\
## frames.mask [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#framesmask "Direct link to frames.mask")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **content\_type**<br>_optional_ | Content type (e.g. 'image/jpeg', 'image/png') | string |\
| **height**<br>_optional_ | Height in pixels | integer |\
| **id**<br>_optional_ | unique ID (in this frame) | string |\
| **timestamp**<br>_optional_ | Timestamp in the source data (for video content. for images, this value should <br>be 0) | integer |\
| **uri**<br>_optional_ | Data URI | string |\
| **width**<br>_optional_ | Width in pixels | integer |\
\
## frames.output\_rois\_enum [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#framesoutput_rois_enum "Direct link to frames.output_rois_enum")\
\
_Type_ : enum (all\_in\_frame, only\_filtered, frame\_per\_roi)\
\
## frames.preview [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#framespreview "Direct link to frames.preview")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **content\_type**<br>_optional_ | Content type (e.g. 'image/jpeg', 'image/png') | string |\
| **height**<br>_optional_ | Height in pixels | integer |\
| **timestamp**<br>_optional_ | Timestamp in the source data (for video content. for images, this value should <br>be 0) | integer |\
| **uri**<br>_optional_ | Data URI | string |\
| **width**<br>_optional_ | Width in pixels | integer |\
\
## frames.roi [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#framesroi "Direct link to frames.roi")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **area**<br>_optional_ | ROI area (not used) | integer |\
| **confidence**<br>_optional_ | ROI confidence | number |\
| **id**<br>_optional_ | ROI id | string |\
| **label**<br>_optional_ | ROI labels | < string > array |\
| **label\_num**<br>_optional_ | Label number according to the specified labels mapping Used only when ROI is <br>returned as part of a task's frame. | integer |\
| **mask**<br>_optional_ | Mask info for this ROI | [frames.roi\_mask](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#frames-roi_mask) |\
| **meta**<br>_optional_ | Additional metadata dictionary for the roi | object |\
| **poly**<br>_optional_ | ROI polygon (x0, y0, ..., xn, yn) | < number > array |\
| **sources**<br>_optional_ | Sources that this ROI belongs to | < string > array |\
\
## frames.roi\_mask [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#framesroi_mask "Direct link to frames.roi_mask")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **id**<br>_required_ | Mask ID | string |\
| **value**<br>_required_ | Mask value | < integer > array |\
\
## frames.rule\_count [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#framesrule_count "Direct link to frames.rule_count")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **accurate**<br>_optional_ | True if the provided count is accurate. If False, 'reason' will contain the <br>reason why. | boolean |\
| **count**<br>_optional_ | Number of frames matching this rule | integer |\
| **name**<br>_optional_ | Rule name | string |\
| **reason**<br>_optional_ | Reason for the count being inaccurate if 'accurate' is True, empty otherwise. | string |\
| **rule\_index**<br>_optional_ | Rule index | integer |\
\
## frames.similarity\_function [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#framessimilarity_function "Direct link to frames.similarity_function")\
\
_Type_ : enum (l2\_norm, dot\_product, cosine)\
\
## frames.snippet [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#framessnippet "Direct link to frames.snippet")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **\_key**<br>_optional_ | The grouping key for the agggregated frames | string |\
| **\_score**<br>_optional_ | For vector search return the similarity score that frame vector field got <br>relative to the input vector | number |\
| **augmentation**<br>_optional_ | List of augmentations | < [frames.augmentation](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#frames-augmentation) \> array |\
| **blob**<br>_optional_ | Raw data (blob) for the frame | string |\
| **context\_id**<br>_optional_ | Context ID. Used for the default frames sorting. If not set then it is filled <br>from the uri of the first source. | string |\
| **dataset**<br>_optional_ | Frame's dataset version | [frames.dataset\_version](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#frames-dataset_version) |\
| **deleted**<br>_optional_ | Set to 'true' for the deleted frames | boolean |\
| **id**<br>_optional_ | Frame id | string |\
| **is\_key\_frame**<br>_optional_ | Is this a key frame (only applicable in frames who'se src is a video) | boolean |\
| **key\_frame**<br>_optional_ | ID of the key frame that this frame belongs to | string |\
| **label\_rule\_counts**<br>_optional_ | The number of matched roi per lable rule | object |\
| **labels\_size**<br>_optional_ | Number of labels returned | integer |\
| **meta**<br>_optional_ | Additional metadata dictionary for the frame. Please note that using this field <br>effectively defines a schema (dictionary structure and types used as values) - <br>frames within the same dataset cannot use conflicting schemas for this field <br>(see documentation for more details). | object |\
| **meta\_blob**<br>_optional_ | Non searchable metadata dictionary for the frame. The fields in this object <br>cannot be searched by and are not added to the frame schema | object |\
| **new\_ver**<br>_optional_ | Newer version of this frame, if asked to merge | [frames.frame](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#frames-frame) |\
| **num\_frames**<br>_optional_ | Number of frames represented by this snippet | integer |\
| **rois**<br>_optional_ | Frame regions of interest | < [frames.roi](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#frames-roi) \> array |\
| **rule\_name**<br>_optional_ | Name of the filtering rule according to which this frame was provided (if <br>applicable) | string |\
| **saved**<br>_optional_ | Last time frame was saved (timestamp) | integer |\
| **saved\_in\_version**<br>_optional_ | Last version this frame was saved in (version ID) | string |\
| **sources**<br>_optional_ | Sources of this frame | < [frames.source](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#frames-source) \> array |\
| **timestamp**<br>_optional_ | Frame's offset in milliseconds, used primarily for video content. Used for the <br>default frames sorting as the secondary key (with the primary key being <br>'context\_id'). For images, this value should typically be 0. If not set, value <br>is filled from the timestamp of the first source. We recommend using this field <br>only in cases concerning the default sorting behavior. | integer |\
| **updated**<br>_optional_ | Last time frame was saved (timestamp) | integer |\
| **updated\_in\_version**<br>_optional_ | Last version this frame was updated in (version ID) | string |\
| **video\_gop**<br>_optional_ | Video encoding GOP value for the source of this frame. Only valid for video <br>frames | number |\
\
## frames.source [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#framessource "Direct link to frames.source")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **content\_type**<br>_optional_ | Content type (e.g. 'image/jpeg', 'image/png') | string |\
| **height**<br>_optional_ | Height in pixels | integer |\
| **id**<br>_optional_ | unique ID (in this frame) | string |\
| **masks**<br>_optional_ |  | < [frames.mask](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#frames-mask) \> array |\
| **meta**<br>_optional_ | Additional metadata dictionary for the source | object |\
| **preview**<br>_optional_ |  | [frames.preview](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#frames-preview) |\
| **timestamp**<br>_optional_ | Timestamp in the source data (for video content. for images, this value should <br>be 0) | integer |\
| **uri**<br>_optional_ | Data URI | string |\
| **width**<br>_optional_ | Width in pixels | integer |\
\
## frames.stat\_count [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#framesstat_count "Direct link to frames.stat_count")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **count**<br>_optional_ | Item name | integer |\
| **name**<br>_optional_ | Number of appearances | string |\
\
## frames.view\_entry [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#framesview_entry "Direct link to frames.view_entry")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **dataset**<br>_optional_ | Existing Dataset id | string |\
| **merge\_with**<br>_optional_ | Version ID to merge with | string |\
| **version**<br>_optional_ | Version id of a version belonging to the dataset | string |\
\
## login.assignable\_role [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#loginassignable_role "Direct link to login.assignable_role")\
\
Roles that can be assigned to a user via the API\
\
_Type_ : enum (admin, user, consumer)\
\
## login.choose\_company [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#loginchoose_company "Direct link to login.choose_company")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **companies**<br>_optional_ | Companies info | < [companies](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#login-choose_company-companies) \> array |\
| **session\_id**<br>_optional_ | Login session ID | string |\
| **tenant**<br>_optional_ | External tenant ID | string |\
\
**companies**\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **id**<br>_optional_ | Company ID | string |\
| **logo**<br>_optional_ | Company logo | string |\
| **logo\_fmt**<br>_optional_ | Company logo format | string |\
| **name**<br>_optional_ | Company Name | string |\
\
## login.login\_status\_enum [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#loginlogin_status_enum "Direct link to login.login_status_enum")\
\
_Type_ : enum (logged\_in, signup\_required, choose\_company)\
\
## login.login\_white\_list [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#loginlogin_white_list "Direct link to login.login_white_list")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **company**<br>_optional_ | Company | string |\
| **domain**<br>_optional_ | Email domain name (all addresses under the domain are included in this <br>whitelist entry) | string (hostname) |\
| **emails**<br>_optional_ | List of email addresses (all addresses in this list are included in this <br>whitelist entry) | < [login.login\_white\_list\_email\_entry](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#login-login_white_list_email_entry) \> array |\
| **group**<br>_optional_ | Group ID to be assigned to users added through this whitelist | string |\
| **id**<br>_optional_ | Whitelist entry ID | string |\
| **is\_admin**<br>_optional_ | DEPRECATED legacy field, superseded by 'role'. Derived from role==admin and <br>emitted only for backwards compatibility with clients that still read it. | boolean |\
| **role**<br>_optional_ | Role assigned to users created from this whitelist | [login.assignable\_role](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#login-assignable_role) |\
\
## login.login\_white\_list\_email\_entry [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#loginlogin_white_list_email_entry "Direct link to login.login_white_list_email_entry")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **added**<br>_optional_ | The time this email entry was added | string (date-time) |\
| **email**<br>_optional_ | Email address | string (email) |\
\
## login.login\_white\_list\_v1\_5 [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#loginlogin_white_list_v1_5 "Direct link to login.login_white_list_v1_5")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **company**<br>_optional_ | Company | string |\
| **domain**<br>_optional_ | Email domain name (all addresses under the domain are included in this <br>whitelist entry) | string (hostname) |\
| **emails**<br>_optional_ | List of email addresses (all addresses in this list are included in this <br>whitelist entry) | < [login.login\_white\_list\_email\_entry](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#login-login_white_list_email_entry) \> array |\
| **group**<br>_optional_ | Group ID to be assigned to users added through this whitelist | string |\
| **id**<br>_optional_ | Whitelist entry ID | string |\
| **is\_admin**<br>_optional_ | DEPRECATED legacy field, superseded by 'role'. Derived from role==admin and <br>emitted only for backwards compatibility with clients that still read it. | boolean |\
| **role**<br>_optional_ | Role assigned to users created from this whitelist | [login.assignable\_role](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#login-assignable_role) |\
\
## login.role [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#loginrole "Direct link to login.role")\
\
_Type_ : enum (admin, superuser, user, annotator, consumer)\
\
## login.signup\_info [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#loginsignup_info "Direct link to login.signup_info")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **avatar**<br>_optional_ | The user avatar as received from auth provider | string |\
| **company\_name**<br>_optional_ | Company name for the user. In case the user was invited to join the company <br>this field cannot be changed | string |\
| **crm\_form**<br>_optional_ | The crm form template for the user signup | string |\
| **email**<br>_optional_ | The user email as received from auth provider | string |\
| **email\_verify\_state**<br>_optional_ | App state stored until email was verified | string |\
| **family\_name**<br>_optional_ | The user family name as received from auth provider | string |\
| **given\_name**<br>_optional_ | The user given name as received from auth provider | string |\
| **name**<br>_optional_ | The user full name as received from auth provide | string |\
| **signup\_token**<br>_optional_ | Sign-up token. Should be passed back to the Signup call | string |\
\
## login.whitelist\_entry [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#loginwhitelist_entry "Direct link to login.whitelist_entry")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **accepted**<br>_optional_ | Time the entry was accepted | string (date-time) |\
| **added**<br>_optional_ | Time that the entry was added | string (date-time) |\
| **email**<br>_optional_ | Email address | string (email) |\
| **status**<br>_optional_ | Entry status | enum (pending, accepted) |\
| **user**<br>_optional_ | The user info (if the user was created) | [user](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#login-whitelist_entry-user) |\
\
**user**\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **id**<br>_optional_ | The user ID | string |\
| **name**<br>_optional_ | The user full name | string |\
| **role**<br>_optional_ | The user role | [login.role](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#login-role) |\
\
## models.last\_metrics\_event [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#modelslast_metrics_event "Direct link to models.last_metrics_event")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **count**<br>_optional_ | The total count of reported values | integer |\
| **first\_value**<br>_optional_ | First value reported | number |\
| **first\_value\_iteration**<br>_optional_ | The iteration at which the first value was reported | integer |\
| **max\_value**<br>_optional_ | Maximum value reported | number |\
| **max\_value\_iteration**<br>_optional_ | The iteration at which the maximum value was reported | integer |\
| **mean\_value**<br>_optional_ | The mean value | number |\
| **metric**<br>_optional_ | Metric name | string |\
| **min\_value**<br>_optional_ | Minimum value reported | number |\
| **min\_value\_iteration**<br>_optional_ | The iteration at which the minimum value was reported | integer |\
| **value**<br>_optional_ | Last value reported | number |\
| **variant**<br>_optional_ | Variant name | string |\
| **x\_axis\_label**<br>_optional_ | The user defined value for the X-Axis name stored with the event | string |\
\
## models.last\_metrics\_variants [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#modelslast_metrics_variants "Direct link to models.last_metrics_variants")\
\
Last metric events, one for each variant hash\
\
_Type_ : < string, [models.last\_metrics\_event](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#models-last_metrics_event) \> map\
\
## models.metadata\_item [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#modelsmetadata_item "Direct link to models.metadata_item")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **key**<br>_optional_ | The key uniquely identifying the metadata item inside the given entity | string |\
| **type**<br>_optional_ | The type of the metadata item | string |\
| **value**<br>_optional_ | The value stored in the metadata item | string |\
\
## models.model [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#modelsmodel "Direct link to models.model")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **comment**<br>_optional_ | Model comment | string |\
| **company**<br>_optional_ | Company id | string |\
| **created**<br>_optional_ | Model creation time | string (date-time) |\
| **design**<br>_optional_ | Json object representing the model design. Should be identical to the network <br>design of the task which created the model | object |\
| **framework**<br>_optional_ | Framework on which the model is based. Should be identical to the framework of <br>the task which created the model | string |\
| **id**<br>_optional_ | Model id | string |\
| **labels**<br>_optional_ | Json object representing the ids of the labels in the model. The keys are the <br>layers' names and the values are the ids. | < string, integer > map |\
| **last\_iteration**<br>_optional_ | Last iteration reported for this model | integer |\
| **last\_metrics**<br>_optional_ | Last metric variants (hash to events), one for each metric hash | < string, [models.last\_metrics\_variants](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#models-last_metrics_variants) \> map |\
| **last\_update**<br>_optional_ | Model last update time | string (date-time) |\
| **metadata**<br>_optional_ | Model metadata | < string, [models.metadata\_item](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#models-metadata_item) \> map |\
| **name**<br>_optional_ | Model name | string |\
| **parent**<br>_optional_ | Parent model ID | string |\
| **project**<br>_optional_ | Associated project ID | string |\
| **ready**<br>_optional_ | Indication if the model is final and can be used by other tasks | boolean |\
| **stats**<br>_optional_ | Model statistics | [stats](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#models-model-stats) |\
| **system\_tags**<br>_optional_ | System tags. This field is reserved for system use, please don't use it. | < string > array |\
| **tags**<br>_optional_ | User-defined tags | < string > array |\
| **task**<br>_optional_ | Task ID of task in which the model was created | string |\
| **ui\_cache**<br>_optional_ | UI cache for this model | object |\
| **uri**<br>_optional_ | URI for the model, pointing to the destination storage. | string |\
| **user**<br>_optional_ | Associated user id | string |\
\
**stats**\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **labels\_count**<br>_optional_ | Number of the model labels | integer |\
\
## models.multi\_field\_pattern\_data [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#modelsmulti_field_pattern_data "Direct link to models.multi_field_pattern_data")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **datetime**<br>_optional_ | Date time conditions (applicable only to datetime fields). Either 'pattern' or <br>'datetime' should be specified | string |\
| **fields**<br>_optional_ | List of field names | < string > array |\
| **pattern**<br>_optional_ | Pattern string (regex). Either 'pattern' or 'datetime' should be specified | string |\
\
## organization.field\_mapping [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#organizationfield_mapping "Direct link to organization.field_mapping")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **field**<br>_required_ | The source field name as specified in the only\_fields | string |\
| **name**<br>_optional_ | The column name in the exported csv file | string |\
| **values**<br>_optional_ |  | < [organization.value\_mapping](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#organization-value_mapping) \> array |\
\
## organization.invite [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#organizationinvite "Direct link to organization.invite")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **company**<br>_optional_ | Company ID | string |\
| **created**<br>_optional_ | Invite creation time (UTC) | string (date-time) |\
| **emails**<br>_optional_ | Invited emails | < string > array |\
| **expires**<br>_optional_ | Invite expiration time (UTC) | string (date-time) |\
| **id**<br>_optional_ | Invite id | string |\
| **user**<br>_optional_ | Associated user id | string |\
\
## organization.match\_set [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#organizationmatch_set "Direct link to organization.match_set")\
\
| Name | Schema |\
| --- | --- |\
| **rules**<br>_optional_ | < [organization.match\_spec](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#organization-match_spec) \> array |\
\
## organization.match\_spec [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#organizationmatch_spec "Direct link to organization.match_spec")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **field**<br>_optional_ | Match field. Denotes the object field path this spec references. | string |\
| **obj\_type**<br>_optional_ | Type of object this match spec refers to (e.g. frame) | string |\
| **regex**<br>_optional_ | Python-style regex. This spec matches the field if the field's value is matched <br>by thie regex. | string |\
\
## organization.service\_info [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#organizationservice_info "Direct link to organization.service_info")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **match\_sets**<br>_optional_ | A list of match specs sets. Each nested set represents a set of specs - a <br>nested set is matched if all specs in this nested set match (AND relation). <br>Nested sets have an OR relation, meaning that if at least one of them is <br>matched, the service can be used. | < [organization.match\_set](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#organization-match_set) \> array |\
| **type**<br>_optional_ | Service type | string |\
| **url**<br>_optional_ | Service URL | string |\
| **use\_fallback**<br>_optional_ | If set and url is not responding then the original url will be contacted | boolean |\
\
## organization.ui\_action [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#organizationui_action "Direct link to organization.ui_action")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **action**<br>_optional_ | Action request details | [action](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#organization-ui_action-action) |\
| **name**<br>_optional_ | Action name | string |\
| **tooltip**<br>_optional_ | Action tooltip | string |\
\
**action**\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **headers**<br>_optional_ | Additional request headers | < string, string > map |\
| **method**<br>_optional_ | HTTP method | enum (get, GET, post, POST, delete, DELETE) |\
| **payload**<br>_optional_ | Request payload | string |\
| **url**<br>_optional_ | Request URL | string |\
\
## organization.user\_details [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#organizationuser_details "Direct link to organization.user_details")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **avatar**<br>_optional_ | User avatar (URL or base64-encoded data) | string |\
| **id**<br>_optional_ | User ID | string |\
| **name**<br>_optional_ | User Name | string |\
| **support**<br>_optional_ | Set to 'true' for the support users. Only internal users can see other support <br>users | boolean |\
\
## organization.value\_mapping [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#organizationvalue_mapping "Direct link to organization.value_mapping")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **key**<br>_required_ | Original value | object |\
| **value**<br>_required_ | Translated value | object |\
\
## organization.workloads [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#organizationworkloads "Direct link to organization.workloads")\
\
| Name | Schema |\
| --- | --- |\
| **series**<br>_optional_ | < [series](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#organization-workloads-series) \> array |\
| **total**<br>_optional_ | < [total](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#organization-workloads-total) \> array |\
\
**series**\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **cpu\_usage**<br>_optional_ | Tasks running task multiplied by cpu resource | < number > array |\
| **cpu\_usage\_artifical\_weights**<br>_optional_ | Indicate whether artificial cpu resource weights were used | boolean |\
| **dates**<br>_optional_ | Date timestamp in seconds | < number > array |\
| **duration**<br>_optional_ | Tasks running time in seconds | < number > array |\
| **gpu\_usage**<br>_optional_ | Tasks running task multiplied by gpu resource | < number > array |\
| **gpu\_usage\_artifical\_weights**<br>_optional_ | Indicate whether artificial gpu resource weights were used | boolean |\
| **id**<br>_optional_ |  | string |\
| **name**<br>_optional_ |  | string |\
\
**total**\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **cpu\_artificial\_weights**<br>_optional_ | Indicate whether artificial cpu resource weights were used | boolean |\
| **cpu\_usage**<br>_optional_ | Tasks running task multiplied by cpu resource | number |\
| **duration**<br>_optional_ | Tasks running time in seconds | integer |\
| **gpu\_artificial\_weights**<br>_optional_ | Indicate whether artificial gpu resource weights were used | boolean |\
| **gpu\_usage**<br>_optional_ | Tasks running task multiplied by gpu resource | number |\
| **id**<br>_optional_ |  | string |\
| **name**<br>_optional_ |  | string |\
\
## permissions.access\_permission\_enum [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#permissionsaccess_permission_enum "Direct link to permissions.access_permission_enum")\
\
_Type_ : enum (read, read\_write)\
\
## permissions.entity\_type\_enum [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#permissionsentity_type_enum "Direct link to permissions.entity_type_enum")\
\
_Type_ : enum (task, model, project, queue, dataset, dataview, route, app, app\_category)\
\
## permissions.user [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#permissionsuser "Direct link to permissions.user")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **email**<br>_optional_ | User email | string |\
| **id**<br>_optional_ | User ID | string |\
| **name**<br>_optional_ | User name | string |\
| **role**<br>_optional_ | User role | string |\
\
## projects.metric\_variant\_result [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#projectsmetric_variant_result "Direct link to projects.metric_variant_result")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **metric**<br>_optional_ | Metric name | string |\
| **metric\_hash**<br>_optional_ | Metric name hash. Used instead of the metric name when categorizing last <br>metrics events in task objects. | string |\
| **variant**<br>_optional_ | Variant name | string |\
| **variant\_hash**<br>_optional_ | Variant name hash. Used instead of the variant name when categorizing last <br>metrics events in task objects. | string |\
\
## projects.multi\_field\_pattern\_data [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#projectsmulti_field_pattern_data "Direct link to projects.multi_field_pattern_data")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **datetime**<br>_optional_ | Date time conditions (applicable only to datetime fields). Either 'pattern' or <br>'datetime' should be specified | string |\
| **fields**<br>_optional_ | List of field names | < string > array |\
| **pattern**<br>_optional_ | Pattern string (regex). Either 'pattern' or 'datetime' should be specified | string |\
\
## projects.project [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#projectsproject "Direct link to projects.project")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **basename**<br>_optional_ | Project base name | string |\
| **company**<br>_optional_ | Company id | string |\
| **created**<br>_optional_ | Creation time | string (date-time) |\
| **default\_output\_destination**<br>_optional_ | The default output destination URL for new tasks under this project | string |\
| **description**<br>_optional_ | Project description | string |\
| **id**<br>_optional_ | Project id | string |\
| **last\_update**<br>_optional_ | Last project update time. Reflects the last time the project metadata was <br>changed or a task in this project has changed status | string (date-time) |\
| **name**<br>_optional_ | Project name | string |\
| **system\_tags**<br>_optional_ | System tags. This field is reserved for system use, please don't use it. | < string > array |\
| **tags**<br>_optional_ | User-defined tags | < string > array |\
| **user**<br>_optional_ | Associated user id | string |\
\
## projects.projects\_get\_all\_response\_single [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#projectsprojects_get_all_response_single "Direct link to projects.projects_get_all_response_single")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **basename**<br>_optional_ | Project base name | string |\
| **company**<br>_optional_ | Company id | string |\
| **created**<br>_optional_ | Creation time | string (date-time) |\
| **dataset\_stats**<br>_optional_ | Project dataset statistics | [dataset\_stats](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#projects-projects_get_all_response_single-dataset_stats) |\
| **default\_output\_destination**<br>_optional_ | The default output destination URL for new tasks under this project | string |\
| **description**<br>_optional_ | Project description | string |\
| **hidden**<br>_optional_ | Returned if the search\_hidden flag was specified in the get\_all\_ex call and the <br>project is hidden | boolean |\
| **id**<br>_optional_ | Project id | string |\
| **last\_update**<br>_optional_ | Last project update time. Reflects the last time the project metadata was <br>changed or a task in this project has changed status | string (date-time) |\
| **name**<br>_optional_ | Project name | string |\
| **own\_datasets**<br>_optional_ | The amount of datasets/hyperdatasers under this project (without children <br>projects). Returned if 'check\_own\_contents' flag is set in the request and <br>children\_type is set to 'dataset' or 'hyperdataset' | integer |\
| **own\_dataviews**<br>_optional_ | The amount of dataviews under this project (without children projects). <br>Returned if 'check\_own\_contents' flag is set in the request | integer |\
| **own\_models**<br>_optional_ | The amount of models under this project (without children projects). Returned <br>if 'check\_own\_contents' flag is set in the request | integer |\
| **own\_tasks**<br>_optional_ | The amount of tasks under this project (without children projects). Returned if <br>'check\_own\_contents' flag is set in the request | integer |\
| **stats**<br>_optional_ | Additional project stats | [projects.stats](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#projects-stats) |\
| **sub\_projects**<br>_optional_ | The list of sub projects | < [sub\_projects](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#projects-projects_get_all_response_single-sub_projects) \> array |\
| **system\_tags**<br>_optional_ | System tags. This field is reserved for system use, please don't use it. | < string > array |\
| **tags**<br>_optional_ | User-defined tags | < string > array |\
| **user**<br>_optional_ | Associated user id | string |\
\
**dataset\_stats**\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **file\_count**<br>_optional_ | The number of files stored in the dataset | integer |\
| **total\_size**<br>_optional_ | The total dataset size in bytes | integer |\
\
**sub\_projects**\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **id**<br>_optional_ | Subproject ID | string |\
| **name**<br>_optional_ | Subproject name | string |\
\
## projects.stats [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#projectsstats "Direct link to projects.stats")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **active**<br>_optional_ | Stats for active tasks | [projects.stats\_status\_count](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#projects-stats_status_count) |\
| **archived**<br>_optional_ | Stats for archived tasks | [projects.stats\_status\_count](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#projects-stats_status_count) |\
| **datasets**<br>_optional_ | Stats for childrent datasets | [projects.stats\_datasets](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#projects-stats_datasets) |\
\
## projects.stats\_datasets [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#projectsstats_datasets "Direct link to projects.stats_datasets")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **count**<br>_optional_ | Number of datasets | integer |\
| **tags**<br>_optional_ | Dataset tags | < string > array |\
\
## projects.stats\_status\_count [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#projectsstats_status_count "Direct link to projects.stats_status_count")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **completed\_tasks\_24h**<br>_optional_ | Number of tasks completed in the last 24 hours | integer |\
| **last\_task\_run**<br>_optional_ | The most recent started time of a task | integer |\
| **status\_count**<br>_optional_ | Status counts | [status\_count](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#projects-stats_status_count-status_count) |\
| **total\_runtime**<br>_optional_ | Total run time of all tasks in project (in seconds) | integer |\
| **total\_tasks**<br>_optional_ | Number of tasks | integer |\
\
**status\_count**\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **closed**<br>_optional_ | Number of 'closed' tasks in project | integer |\
| **completed**<br>_optional_ | Number of 'completed' tasks in project | integer |\
| **created**<br>_optional_ | Number of 'created' tasks in project | integer |\
| **failed**<br>_optional_ | Number of 'failed' tasks in project | integer |\
| **in\_progress**<br>_optional_ | Number of 'in\_progress' tasks in project | integer |\
| **published**<br>_optional_ | Number of 'published' tasks in project | integer |\
| **queued**<br>_optional_ | Number of 'queued' tasks in project | integer |\
| **stopped**<br>_optional_ | Number of 'stopped' tasks in project | integer |\
| **unknown**<br>_optional_ | Number of 'unknown' tasks in project | integer |\
\
## projects.urls [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#projectsurls "Direct link to projects.urls")\
\
| Name | Schema |\
| --- | --- |\
| **artifact\_urls**<br>_optional_ | < string > array |\
| **event\_urls**<br>_optional_ | < string > array |\
| **model\_urls**<br>_optional_ | < string > array |\
\
## queues.entry [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#queuesentry "Direct link to queues.entry")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **added**<br>_optional_ | Time this entry was added to the queue | string (date-time) |\
| **task**<br>_optional_ | Queued task ID | string |\
\
## queues.metadata\_item [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#queuesmetadata_item "Direct link to queues.metadata_item")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **key**<br>_optional_ | The key uniquely identifying the metadata item inside the given entity | string |\
| **type**<br>_optional_ | The type of the metadata item | string |\
| **value**<br>_optional_ | The value stored in the metadata item | string |\
\
## queues.queue [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#queuesqueue "Direct link to queues.queue")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **company**<br>_optional_ | Company id | string |\
| **created**<br>_optional_ | Queue creation time | string (date-time) |\
| **display\_name**<br>_optional_ | Display name | string |\
| **entries**<br>_optional_ | List of ordered queue entries | < [queues.entry](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#queues-entry) \> array |\
| **id**<br>_optional_ | Queue id | string |\
| **last\_update**<br>_optional_ | Queue last update | string (date-time) |\
| **metadata**<br>_optional_ | Queue metadata | < string, [queues.metadata\_item](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#queues-metadata_item) \> map |\
| **name**<br>_optional_ | Queue name | string |\
| **profile\_connection**<br>_optional_ | Profile connection for policy queues | [profile\_connection](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#queues-queue-profile_connection) |\
| **system\_tags**<br>_optional_ | System tags. This field is reserved for system use, please don't use it. | < string > array |\
| **tags**<br>_optional_ | User-defined tags | < string > array |\
| **user**<br>_optional_ | Associated user id | string |\
\
**profile\_connection**\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **policy**<br>_optional_ | Policy ID | string |\
| **policy\_name**<br>_optional_ | Policy Name. Returned only for admins or members of the corresponding policy <br>group | string |\
| **profile**<br>_optional_ | Profile ID | string |\
| **user\_group**<br>_optional_ | Policy group | string |\
\
## queues.queue\_metrics [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#queuesqueue_metrics "Direct link to queues.queue_metrics")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **avg\_waiting\_times**<br>_optional_ | List of average waiting times for tasks in the queue. The points correspond to <br>the timestamps in the dates list. If more than one value exists for the given <br>interval then the maximum value is taken. | < number > array |\
| **dates**<br>_optional_ | List of timestamps (in seconds from epoch) in the acceding order. The <br>timestamps are separated by the requested interval. Timestamps where no queue <br>status change was recorded are omitted. | < integer > array |\
| **queue**<br>_optional_ | ID of the queue | string |\
| **queue\_lengths**<br>_optional_ | List of tasks counts in the queue. The points correspond to the timestamps in <br>the dates list. If more than one value exists for the given interval then the <br>count that corresponds to the maximum average value is taken. | < integer > array |\
\
## reports.artifact [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#reportsartifact "Direct link to reports.artifact")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **content\_size**<br>_optional_ | Raw data length in bytes | integer |\
| **display\_data**<br>_optional_ | User-defined list of key/value pairs, sorted | < < string > array > array |\
| **hash**<br>_optional_ | Hash of entire raw data | string |\
| **key**<br>_required_ | Entry key | string |\
| **mode**<br>_optional_ | System defined input/output indication | [reports.artifact\_mode\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reports-artifact_mode_enum) |\
| **timestamp**<br>_optional_ | Epoch time when artifact was created | integer |\
| **type**<br>_required_ | System defined type | string |\
| **type\_data**<br>_optional_ | Additional fields defined by the system | [reports.artifact\_type\_data](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reports-artifact_type_data) |\
| **uri**<br>_optional_ | Raw data location | string |\
\
## reports.artifact\_mode\_enum [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#reportsartifact_mode_enum "Direct link to reports.artifact_mode_enum")\
\
_Type_ : enum (input, output)\
\
## reports.artifact\_type\_data [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#reportsartifact_type_data "Direct link to reports.artifact_type_data")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **content\_type**<br>_optional_ | System defined raw data content type | string |\
| **data\_hash**<br>_optional_ | Hash of raw data, without any headers or descriptive parts | string |\
| **preview**<br>_optional_ | Description or textual data | string |\
\
## reports.augmentation [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#reportsaugmentation "Direct link to reports.augmentation")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **crop\_around\_rois**<br>_optional_ | Crop image data around all frame ROIs | boolean |\
| **sets**<br>_optional_ | List of augmentation sets | < [reports.augmentation\_set](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reports-augmentation_set) \> array |\
\
## reports.augmentation\_set [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#reportsaugmentation_set "Direct link to reports.augmentation_set")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **arguments**<br>_optional_ | Arguments dictionary per custom augmentation type. | < string, object > map |\
| **cls**<br>_optional_ | Augmentation class | string |\
| **strength**<br>_optional_ | Augmentation strength. Range \[0,). <br>**Minimum value** : `0` | number |\
| **types**<br>_optional_ | Augmentation type | < string > array |\
\
## reports.configuration\_item [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#reportsconfiguration_item "Direct link to reports.configuration_item")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **description**<br>_optional_ | The parameter description. Optional | string |\
| **name**<br>_optional_ | Name of the parameter. Should be unique | string |\
| **type**<br>_optional_ | Type of the parameter. Optional | string |\
| **value**<br>_optional_ | Value of the parameter | string |\
\
## reports.debug\_images\_response\_task\_metrics [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#reportsdebug_images_response_task_metrics "Direct link to reports.debug_images_response_task_metrics")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **iterations**<br>_optional_ |  | < [iterations](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reports-debug_images_response_task_metrics-iterations) \> array |\
| **task**<br>_optional_ | Task ID | string |\
\
**iterations**\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **events**<br>_optional_ |  | < object > array |\
| **iter**<br>_optional_ | Iteration number | integer |\
\
## reports.execution [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#reportsexecution "Direct link to reports.execution")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **artifacts**<br>_optional_ | Task artifacts | < [reports.artifact](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reports-artifact) \> array |\
| **dataviews**<br>_optional_ | Additional dataviews for the task | < object > array |\
| **docker\_cmd**<br>_optional_ | Command for running docker script for the execution of the task | string |\
| **framework**<br>_optional_ | Framework related to the task. Case insensitive. Mandatory for Training tasks. | string |\
| **model**<br>_optional_ | Execution input model ID Not applicable for Register (Import) tasks | string |\
| **model\_desc**<br>_optional_ | Json object representing the Model descriptors | object |\
| **model\_labels**<br>_optional_ | Json object representing the ids of the labels in the model. The keys are the <br>layers' names and the values are the IDs. Not applicable for Register (Import) <br>tasks. Mandatory for Training tasks | < string, integer > map |\
| **parameters**<br>_optional_ | Json object containing the Task parameters | object |\
| **queue**<br>_optional_ | Queue ID where task was queued. | string |\
| **test\_split**<br>_optional_ | Percentage of frames to use for testing only | integer |\
\
## reports.filter\_by\_roi\_enum [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#reportsfilter_by_roi_enum "Direct link to reports.filter_by_roi_enum")\
\
_Type_ : enum (disabled, no\_rois, label\_rules)\
\
## reports.filter\_label\_rule [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#reportsfilter_label_rule "Direct link to reports.filter_label_rule")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **conf\_range**<br>_optional_ | Range of ROI confidence level in the frame (min, max). -1 for not applicable <br>Both min and max can be either -1 or positive. 2nd number (max) must be either <br>-1 or larger than or equal to the 1st number (min) | < number > array |\
| **count\_range**<br>_optional_ | Range of times ROI appears in the frame (min, max). -1 for not applicable. Both <br>integers must be larger than or equal to -1. 2nd integer (max) must be either <br>-1 or larger than or equal to the 1st integer (min) | < integer > array |\
| **label**<br>_required_ | Lucene format query (see lucene query syntax). Default search field is <br>label.keyword and default operator is AND, so searching for: <br>'Bus Stop' Blue <br>is equivalent to: <br>Label.keyword:'Bus Stop' AND label.keyword:'Blue' | string |\
| **must\_not**<br>_optional_ | If set then the label must not exist or lucene query must not be true. The <br>default value is false <br>**Default** : `false` | boolean |\
\
## reports.filter\_rule [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#reportsfilter_rule "Direct link to reports.filter_rule")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **dataset**<br>_required_ | Dataset ID. Must be a dataset which is in the task's view. If set to '\*' all <br>datasets in View are used. | string |\
| **filter\_by\_roi**<br>_optional_ | Type of filter. Optional, the default value is 'label\_rules' | [reports.filter\_by\_roi\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reports-filter_by_roi_enum) |\
| **frame\_query**<br>_optional_ | Frame filter, in Lucene query syntax | string |\
| **label\_rules**<br>_optional_ | List of FilterLabelRule ('AND' connection) <br>disabled - No filtering by ROIs. Select all frames, even if they don't have <br>ROIs (all frames) <br>no\_rois - Select only frames without ROIs (empty frames) <br>label\_rules - Select frames according to label rules | < [reports.filter\_label\_rule](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reports-filter_label_rule) \> array |\
| **sources\_query**<br>_optional_ | Sources filter, in Lucene query syntax. Filters sources in each frame. | string |\
| **vector\_search**<br>_optional_ | Vector search rule | [vector\_search](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reports-filter_rule-vector_search) |\
| **version**<br>_optional_ | Dataset version to apply rule to. Must belong to the dataset and be in the <br>task's view. If set to '\*' all version of the datasets in View are used. | string |\
| **weight**<br>_optional_ | Rule weight. Default is 1 | number |\
\
**vector\_search**\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **field**<br>_required_ | Vector field name | string |\
| **min\_score**<br>_optional_ | Min allowed score | number |\
| **similarity\_func**<br>_optional_ | The function for calculating distance from the search vector | [reports.similarity\_function](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reports-similarity_function) |\
| **sort**<br>_optional_ |  | enum (asc, desc) |\
| **vector**<br>_required_ | The search vector | < number > array |\
\
## reports.filtering [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#reportsfiltering "Direct link to reports.filtering")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **filtering\_rules**<br>_optional_ | List of FilterRule ('OR' connection) | < [reports.filter\_rule](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reports-filter_rule) \> array |\
| **output\_rois**<br>_optional_ | 'all\_in\_frame' - all rois for a frame are returned <br>'only\_filtered' - only rois which led this frame to be selected <br>'frame\_per\_roi' - single roi per frame. Frame can be returned multiple times <br>with a different roi each time. <br>Note: this should be used for Training tasks only <br>Note: frame\_per\_roi implies that only filtered rois will be returned | [reports.output\_rois\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reports-output_rois_enum) |\
\
## reports.input [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#reportsinput "Direct link to reports.input")\
\
Task input params. (input view must be provided).\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **augmentation**<br>_optional_ | Augmentation parameters. Only for training and testing tasks. | [reports.augmentation](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reports-augmentation) |\
| **dataviews**<br>_optional_ | Key to DataView ID Mapping | < string, string > map |\
| **frames\_filter**<br>_optional_ | Filtering params | [reports.filtering](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reports-filtering) |\
| **iteration**<br>_optional_ | Iteration parameters. Not applicable for register (import) tasks. | [reports.iteration](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reports-iteration) |\
| **mapping**<br>_optional_ | Mapping params (see common definitions section) | [reports.mapping](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reports-mapping) |\
| **view**<br>_optional_ | View params | [reports.view](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reports-view) |\
\
## reports.iteration [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#reportsiteration "Direct link to reports.iteration")\
\
Sequential Iteration API configuration\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **infinite**<br>_optional_ | Infinite iteration | boolean |\
| **jump**<br>_optional_ | Jump entry | [reports.jump](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reports-jump) |\
| **limit**<br>_optional_ | Maximum frames per task. If not passed, frames will end when no more matching <br>frames are found, unless infinite is True. | integer |\
| **min\_sequence**<br>_optional_ | Length (in ms) of video clips to return. This is used in random order, and in <br>sequential order only if jumping is provided and only for video frames | integer |\
| **order**<br>_optional_ | Input frames order. Values: 'sequential', 'random' In Sequential mode frames <br>will be returned according to the order in which the frames were added to the <br>dataset. | string |\
| **random\_seed**<br>_required_ | Random seed used during iteration | integer |\
\
## reports.jump [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#reportsjump "Direct link to reports.jump")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **time**<br>_optional_ | Max time in milliseconds between frames | integer |\
\
## reports.label\_source [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#reportslabel_source "Direct link to reports.label_source")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **dataset**<br>_optional_ | Source dataset id. '\*' for all datasets in view | string |\
| **labels**<br>_optional_ | List of source labels (AND connection). '\*' indicates any label. Labels must <br>exist in at least one of the dataset versions in the task's view | < string > array |\
| **version**<br>_optional_ | Source dataset version id. Default is '\*' (for all versions in dataset in the <br>view) Version must belong to the selected dataset, and must be in the task's <br>view\[i\] | string |\
\
## reports.last\_metrics\_event [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#reportslast_metrics_event "Direct link to reports.last_metrics_event")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **count**<br>_optional_ | The total count of reported values | integer |\
| **first\_value**<br>_optional_ | First value reported | number |\
| **first\_value\_iteration**<br>_optional_ | The iteration at which the first value was reported | integer |\
| **max\_value**<br>_optional_ | Maximum value reported | number |\
| **max\_value\_iteration**<br>_optional_ | The iteration at which the maximum value was reported | integer |\
| **mean\_value**<br>_optional_ | The mean value | number |\
| **metric**<br>_optional_ | Metric name | string |\
| **min\_value**<br>_optional_ | Minimum value reported | number |\
| **min\_value\_iteration**<br>_optional_ | The iteration at which the minimum value was reported | integer |\
| **value**<br>_optional_ | Last value reported | number |\
| **variant**<br>_optional_ | Variant name | string |\
| **x\_axis\_label**<br>_optional_ | The user defined value for the X-Axis name stored with the event | string |\
\
## reports.last\_metrics\_variants [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#reportslast_metrics_variants "Direct link to reports.last_metrics_variants")\
\
Last metric events, one for each variant hash\
\
_Type_ : < string, [reports.last\_metrics\_event](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reports-last_metrics_event) \> map\
\
## reports.mapping [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#reportsmapping "Direct link to reports.mapping")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **rules**<br>_optional_ | Rules list | < [reports.mapping\_rule](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reports-mapping_rule) \> array |\
\
## reports.mapping\_rule [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#reportsmapping_rule "Direct link to reports.mapping_rule")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **source**<br>_optional_ | Source label info | [reports.label\_source](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reports-label_source) |\
| **target**<br>_optional_ | Target label name | string |\
\
## reports.metric\_variants [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#reportsmetric_variants "Direct link to reports.metric_variants")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **metric**<br>_optional_ | The metric name | string |\
| **variants**<br>_optional_ | The names of the metric variants | < string > array |\
\
## reports.multi\_field\_pattern\_data [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#reportsmulti_field_pattern_data "Direct link to reports.multi_field_pattern_data")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **datetime**<br>_optional_ | Date time conditions (applicable only to datetime fields). Either 'pattern' or <br>'datetime' should be specified | string |\
| **fields**<br>_optional_ | List of field names | < string > array |\
| **pattern**<br>_optional_ | Pattern string (regex). Either 'pattern' or 'datetime' should be specified | string |\
\
## reports.output [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#reportsoutput "Direct link to reports.output")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **destination**<br>_optional_ | Storage id. This is where output files will be stored. | string |\
| **error**<br>_optional_ | Last error text | string |\
| **model**<br>_optional_ | Model id. | string |\
| **result**<br>_optional_ | Task result. Values: 'success', 'failure' | string |\
| **view**<br>_optional_ | View params | [reports.view](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reports-view) |\
\
## reports.output\_rois\_enum [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#reportsoutput_rois_enum "Direct link to reports.output_rois_enum")\
\
_Type_ : enum (all\_in\_frame, only\_filtered, frame\_per\_roi)\
\
## reports.params\_item [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#reportsparams_item "Direct link to reports.params_item")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **description**<br>_optional_ | The parameter description. Optional | string |\
| **name**<br>_optional_ | Name of the parameter. The combination of section and name should be unique | string |\
| **section**<br>_optional_ | Section that the parameter belongs to | string |\
| **type**<br>_optional_ | Type of the parameter. Optional | string |\
| **value**<br>_optional_ | Value of the parameter | string |\
\
## reports.report [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#reportsreport "Direct link to reports.report")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **comment**<br>_optional_ | Free text comment | string |\
| **company**<br>_optional_ | Company ID | string |\
| **created**<br>_optional_ | Report creation time (UTC) | string (date-time) |\
| **id**<br>_optional_ | Report id | string |\
| **last\_update**<br>_optional_ | Last time this report was created, edited, changed | string (date-time) |\
| **name**<br>_optional_ | Report Name | string |\
| **project**<br>_optional_ | Project ID of the project to which this report is assigned | string |\
| **published**<br>_optional_ | Report publish time | string (date-time) |\
| **report**<br>_optional_ | Report template | string |\
| **report\_assets**<br>_optional_ | List of the external report assets | < string > array |\
| **status**<br>_optional_ |  | [reports.report\_status\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reports-report_status_enum) |\
| **status\_changed**<br>_optional_ | Last status change time | string (date-time) |\
| **status\_message**<br>_optional_ | free text string representing info about the status | string |\
| **status\_reason**<br>_optional_ | Reason for last status change | string |\
| **system\_tags**<br>_optional_ | System tags list. This field is reserved for system use, please don't use it. | < string > array |\
| **tags**<br>_optional_ | User-defined tags list | < string > array |\
| **user**<br>_optional_ | Associated user id | string |\
\
## reports.report\_status\_enum [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#reportsreport_status_enum "Direct link to reports.report_status_enum")\
\
_Type_ : enum (created, published)\
\
## reports.scalar\_key\_enum [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#reportsscalar_key_enum "Direct link to reports.scalar_key_enum")\
\
_Type_ : enum (iter, timestamp, iso\_time)\
\
## reports.script [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#reportsscript "Direct link to reports.script")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **binary**<br>_optional_ | Binary to use when running the script <br>**Default** : `"python"` | string |\
| **branch**<br>_optional_ | Repository branch id If not provided and tag not provided, default repository <br>branch is used. | string |\
| **diff**<br>_optional_ | Uncommitted changes found in the repository when task was run | string |\
| **entry\_point**<br>_optional_ | Path to execute within the repository | string |\
| **repository**<br>_optional_ | Name of the repository where the script is located | string |\
| **requirements**<br>_optional_ | A JSON object containing requirements strings by key | object |\
| **tag**<br>_optional_ | Repository tag | string |\
| **version\_num**<br>_optional_ | Version (changeset) number. Optional (default is head version) Unused if tag is <br>provided. | string |\
| **working\_dir**<br>_optional_ | Path to the folder from which to run the script Default - root folder of <br>repository | string |\
\
## reports.section\_params [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#reportssection_params "Direct link to reports.section_params")\
\
Task section params\
\
_Type_ : < string, [reports.params\_item](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reports-params_item) \> map\
\
## reports.similarity\_function [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#reportssimilarity_function "Direct link to reports.similarity_function")\
\
_Type_ : enum (l2\_norm, dot\_product, cosine)\
\
## reports.single\_value\_task\_metrics [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#reportssingle_value_task_metrics "Direct link to reports.single_value_task_metrics")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **task**<br>_optional_ | Task ID | string |\
| **task\_name**<br>_optional_ | Task name | string |\
| **values**<br>_optional_ |  | < [values](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reports-single_value_task_metrics-values) \> array |\
\
**values**\
\
| Name | Schema |\
| --- | --- |\
| **metric**<br>_optional_ | string |\
| **timestamp**<br>_optional_ | number |\
| **value**<br>_optional_ | number |\
| **variant**<br>_optional_ | string |\
\
## reports.task [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#reportstask "Direct link to reports.task")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **active\_duration**<br>_optional_ | Task duration time (seconds) | integer |\
| **comment**<br>_optional_ | Free text comment | string |\
| **company**<br>_optional_ | Company ID | string |\
| **completed**<br>_optional_ | Task end time (UTC) | string (date-time) |\
| **configuration**<br>_optional_ | Task configuration params | < string, [reports.configuration\_item](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reports-configuration_item) \> map |\
| **container**<br>_optional_ | Docker container parameters | < string, string > map |\
| **created**<br>_optional_ | Task creation time (UTC) | string (date-time) |\
| **execution**<br>_optional_ | Task execution params | [reports.execution](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reports-execution) |\
| **hyperparams**<br>_optional_ | Task hyper params per section | < string, [reports.section\_params](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reports-section_params) \> map |\
| **id**<br>_optional_ | Task id | string |\
| **input**<br>_optional_ | Task input params | [reports.input](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reports-input) |\
| **last\_change**<br>_optional_ | Last time any update was done to the task | string (date-time) |\
| **last\_iteration**<br>_optional_ | Last iteration reported for this task | integer |\
| **last\_metrics**<br>_optional_ | Last metric variants (hash to events), one for each metric hash | < string, [reports.last\_metrics\_variants](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reports-last_metrics_variants) \> map |\
| **last\_update**<br>_optional_ | Last time this task was created, edited, changed or events for this task were <br>reported | string (date-time) |\
| **last\_worker**<br>_optional_ | ID of last worker that handled the task | string |\
| **last\_worker\_report**<br>_optional_ | Last time a worker reported while working on this task | string (date-time) |\
| **models**<br>_optional_ | Task models | [reports.task\_models](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reports-task_models) |\
| **name**<br>_optional_ | Task Name | string |\
| **output**<br>_optional_ | Task output params | [reports.output](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reports-output) |\
| **parent**<br>_optional_ | Parent task id | string |\
| **project**<br>_optional_ | Project ID of the project to which this task is assigned | string |\
| **published**<br>_optional_ | Task publish time | string (date-time) |\
| **runtime**<br>_optional_ | Task runtime mapping | object |\
| **script**<br>_optional_ | Script info | [reports.script](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reports-script) |\
| **started**<br>_optional_ | Task start time (UTC) | string (date-time) |\
| **status**<br>_optional_ |  | [reports.task\_status\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reports-task_status_enum) |\
| **status\_changed**<br>_optional_ | Last status change time | string (date-time) |\
| **status\_message**<br>_optional_ | free text string representing info about the status | string |\
| **status\_reason**<br>_optional_ | Reason for last status change | string |\
| **system\_tags**<br>_optional_ | System tags list. This field is reserved for system use, please don't use it. | < string > array |\
| **tags**<br>_optional_ | User-defined tags list | < string > array |\
| **type**<br>_optional_ | Type of task. Values: 'dataset\_import', 'annotation', 'training', 'testing' | [reports.task\_type\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reports-task_type_enum) |\
| **user**<br>_optional_ | Associated user id | string |\
\
## reports.task\_model\_item [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#reportstask_model_item "Direct link to reports.task_model_item")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **model**<br>_required_ | The model ID | string |\
| **name**<br>_required_ | The task model name | string |\
\
## reports.task\_models [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#reportstask_models "Direct link to reports.task_models")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **input**<br>_optional_ | The list of task input models | < [reports.task\_model\_item](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reports-task_model_item) \> array |\
| **output**<br>_optional_ | The list of task output models | < [reports.task\_model\_item](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reports-task_model_item) \> array |\
\
## reports.task\_status\_enum [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#reportstask_status_enum "Direct link to reports.task_status_enum")\
\
_Type_ : enum (created, queued, in\_progress, stopped, published, publishing, closed, failed, completed, unknown)\
\
## reports.task\_type\_enum [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#reportstask_type_enum "Direct link to reports.task_type_enum")\
\
Type of task\
\
_Type_ : enum (dataset\_import, annotation, annotation\_manual, training, testing, inference, data\_processing, application, monitor, controller, optimizer, service, qc, agent, custom)\
\
## reports.view [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#reportsview "Direct link to reports.view")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **entries**<br>_optional_ | List of view entries. All tasks must have at least one view. | < [reports.view\_entry](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reports-view_entry) \> array |\
\
## reports.view\_entry [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#reportsview_entry "Direct link to reports.view_entry")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **dataset**<br>_optional_ | Existing Dataset id | string |\
| **merge\_with**<br>_optional_ | Version ID to merge with | string |\
| **version**<br>_optional_ | Version id of a version belonging to the dataset | string |\
\
## resources.task\_status\_enum [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#resourcestask_status_enum "Direct link to resources.task_status_enum")\
\
_Type_ : enum (created, queued, in\_progress, stopped, published, publishing, closed, failed, completed, unknown)\
\
## resources.task\_type\_enum [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#resourcestask_type_enum "Direct link to resources.task_type_enum")\
\
Type of task\
\
_Type_ : enum (dataset\_import, annotation, annotation\_manual, training, testing, inference, data\_processing, application, monitor, controller, optimizer, service, qc, agent, custom)\
\
## serving.container\_info [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#servingcontainer_info "Direct link to serving.container_info")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **age\_sec**<br>_optional_ | Amount of seconds since the container registration | integer |\
| **endpoint**<br>_optional_ | Endpoint name | string |\
| **id**<br>_optional_ | Container ID | string |\
| **input\_size**<br>_optional_ | Input size | string |\
| **input\_type**<br>_optional_ | Input type | string |\
| **last\_update**<br>_optional_ | The latest time when the container instance sent update | string (date-time) |\
| **model**<br>_optional_ | Model name | string |\
| **model\_source**<br>_optional_ | Model source | string |\
| **model\_version**<br>_optional_ | Model version | string |\
| **preprocess\_artifact**<br>_optional_ | Preprocess Artifact | string |\
| **uptime\_sec**<br>_optional_ | Model instance uptime in seconds | integer |\
| **url**<br>_optional_ | Model url | string |\
\
## serving.container\_instance\_stats [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#servingcontainer_instance_stats "Direct link to serving.container_instance_stats")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **cpu\_count**<br>_optional_ | CPU Count | integer |\
| **gpu\_count**<br>_optional_ | GPU Count | integer |\
| **id**<br>_optional_ | Container ID | string |\
| **last\_update**<br>_optional_ | The latest time when the container instance sent update | string (date-time) |\
| **latency\_ms**<br>_optional_ | Average request latency in ms | integer |\
| **reference**<br>_optional_ | Array of reference items provided by the container instance. Can contain <br>multiple reference items with the same type | < [reference](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#serving-container_instance_stats-reference) \> array |\
| **requests**<br>_optional_ | Number of requests | integer |\
| **requests\_min**<br>_optional_ | Average requests per minute | number |\
| **uptime\_sec**<br>_optional_ | Uptime in seconds | integer |\
\
**reference**\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **type**<br>_required_ | The type of the reference item | enum (app\_id, app\_instance, model, task, url) |\
| **value**<br>_required_ | The reference item value | string |\
\
## serving.endpoint\_stats [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#servingendpoint_stats "Direct link to serving.endpoint_stats")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **endpoint**<br>_optional_ | Endpoint name | string |\
| **instances**<br>_optional_ | The number of model serving instances | integer |\
| **last\_update**<br>_optional_ | The latest time when one of the model instances was updated | string (date-time) |\
| **latency\_ms**<br>_optional_ | Average of latency of model instances in ms | integer |\
| **model**<br>_optional_ | Model name | string |\
| **requests**<br>_optional_ | Total requests processed by model instances | integer |\
| **requests\_min**<br>_optional_ | Average of request rate of model instances per minute | number |\
| **uptime\_sec**<br>_optional_ | Max of model instance uptime in seconds | integer |\
| **url**<br>_optional_ | Model url | string |\
\
## serving.machine\_stats [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#servingmachine_stats "Direct link to serving.machine_stats")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **cpu\_temperature**<br>_optional_ | CPU temperature | < number > array |\
| **cpu\_usage**<br>_optional_ | Average CPU usage per core | < number > array |\
| **disk\_free\_home**<br>_optional_ | Free space in % of /home drive | number |\
| **disk\_free\_temp**<br>_optional_ | Free space in % of /tmp drive | number |\
| **disk\_read**<br>_optional_ | Mbytes read per second | number |\
| **disk\_write**<br>_optional_ | Mbytes write per second | number |\
| **gpu\_fraction**<br>_optional_ | GPU fraction | < number > array |\
| **gpu\_memory\_free**<br>_optional_ | GPU free memory MBs | < number > array |\
| **gpu\_memory\_used**<br>_optional_ | GPU used memory MBs | < number > array |\
| **gpu\_temperature**<br>_optional_ | GPU temperature | < number > array |\
| **gpu\_usage**<br>_optional_ | Average GPU usage per GPU card | < number > array |\
| **memory\_free**<br>_optional_ | Free memory MBs | number |\
| **memory\_used**<br>_optional_ | Used memory MBs | number |\
| **network\_rx**<br>_optional_ | Mbytes per second | number |\
| **network\_tx**<br>_optional_ | Mbytes per second | number |\
\
## sso.configuration [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#ssoconfiguration "Direct link to sso.configuration")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **active**<br>_optional_ | Configuration status | boolean |\
| **category**<br>_optional_ | The category of the provider | [sso.provider\_category](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#sso-provider_category) |\
| **display\_name**<br>_optional_ | The display name of the configuraton | string |\
| **id**<br>_optional_ | ID of the configuration | string |\
| **last\_update**<br>_optional_ | The UTC time of the last editing | string (date-time) |\
| **provider**<br>_optional_ | ID of the provider | string |\
| **readonly**<br>_optional_ | If set then the configuration cannot be viewed or edited | boolean |\
\
## sso.provider [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#ssoprovider "Direct link to sso.provider")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **category**<br>_optional_ | The category of the provider | [sso.provider\_category](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#sso-provider_category) |\
| **display\_name**<br>_optional_ | The display name of the provider | string |\
| **icon**<br>_optional_ | The icon url | string |\
| **id**<br>_optional_ | ID of the provider | string |\
\
## sso.provider\_category [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#ssoprovider_category "Direct link to sso.provider_category")\
\
_Type_ : enum (saml, oidc)\
\
## storage.aws [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#storageaws "Direct link to storage.aws")\
\
AWS S3 storage settings\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **buckets**<br>_optional_ | Credential settings per bucket | < [storage.aws\_bucket](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#storage-aws_bucket) \> array |\
| **key**<br>_optional_ | Access key | string |\
| **region**<br>_optional_ | AWS region | string |\
| **secret**<br>_optional_ | Secret key | string |\
| **token**<br>_optional_ | Access token | string |\
| **use\_credentials\_chain**<br>_optional_ | If set then use host credentials <br>**Default** : `false` | boolean |\
\
## storage.aws\_bucket [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#storageaws_bucket "Direct link to storage.aws_bucket")\
\
Settings per S3 bucket\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **acl**<br>_optional_ | ACL | string |\
| **bucket**<br>_optional_ | The name of the bucket | string |\
| **host**<br>_optional_ | Host address (for minio servers) | string |\
| **key**<br>_optional_ | Access key | string |\
| **multipart**<br>_optional_ | Multipart upload <br>**Default** : `true` | boolean |\
| **region**<br>_optional_ | AWS Region | string |\
| **secret**<br>_optional_ | Secret key | string |\
| **secure**<br>_optional_ | Use SSL connection <br>**Default** : `true` | boolean |\
| **subdir**<br>_optional_ | The path to match | string |\
| **token**<br>_optional_ | Access token | string |\
| **use\_credentials\_chain**<br>_optional_ | Use host configured credentials <br>**Default** : `false` | boolean |\
| **verify**<br>_optional_ | Verify server certificate <br>**Default** : `true` | boolean |\
\
## storage.azure [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#storageazure "Direct link to storage.azure")\
\
Azure storage settings\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **containers**<br>_optional_ | Credentials per container | < [storage.azure\_container](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#storage-azure_container) \> array |\
\
## storage.azure\_container [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#storageazure_container "Direct link to storage.azure_container")\
\
Azure container settings\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **account\_key**<br>_optional_ | Account key | string |\
| **account\_name**<br>_optional_ | Account name | string |\
| **container\_name**<br>_optional_ | The name of the container | string |\
\
## storage.google [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#storagegoogle "Direct link to storage.google")\
\
Google storage settings\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **buckets**<br>_optional_ | Credentials per bucket | < [storage.google\_bucket](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#storage-google_bucket) \> array |\
| **credentials\_json**<br>_optional_ | The contents of the credentials json file | string |\
| **project**<br>_optional_ | Project name | string |\
\
## storage.google\_bucket [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#storagegoogle_bucket "Direct link to storage.google_bucket")\
\
Settings per Google storage bucket\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **bucket**<br>_optional_ | The name of the bucket | string |\
| **credentials\_json**<br>_optional_ | The contents of the credentials json file | string |\
| **project**<br>_optional_ | The name of the project | string |\
| **subdir**<br>_optional_ | The path to match | string |\
\
## system.basic\_company\_info [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#systembasic_company_info "Direct link to system.basic_company_info")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **active**<br>_optional_ | Company status | boolean |\
| **id**<br>_optional_ | Company ID | string |\
| **name**<br>_optional_ | Company Name | string |\
\
## system.company\_defaults [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#systemcompany_defaults "Direct link to system.company_defaults")\
\
Company configuration defaults\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **allowed\_users**<br>_optional_ | Maximum allowed number of users for this company | integer |\
| **cluster**<br>_optional_ | Cluster in which dataset indices for this company will be created | string |\
| **kibana\_space**<br>_optional_ | Link to user-hosted kibana space | string |\
| **sso**<br>_optional_ | sso config | object |\
\
## system.dataset [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#systemdataset "Direct link to system.dataset")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **comment**<br>_optional_ |  | string |\
| **company**<br>_optional_ | Company ID | string |\
| **created**<br>_optional_ | Dataset creation time (UTC) | string (date-time) |\
| **id**<br>_optional_ | Dataset ID | string |\
| **last\_update**<br>_optional_ | Time of last update (UTC). Updated on dataset update; on any version operation: <br>when version is created, modified, committed, published or deleted; and on any <br>frame operation: when frames are added, modified or deleted. | string (date-time) |\
| **metadata**<br>_optional_ | User-provided metadata | object |\
| **name**<br>_optional_ | Dataset name | string |\
| **project**<br>_optional_ | Associated project ID | string |\
| **system\_tags**<br>_optional_ | List of system tags. This field is reserved for system use, please don't use <br>it. | < string > array |\
| **tags**<br>_optional_ | List of user-defined tags | < string > array |\
| **terms\_of\_use**<br>_optional_ | Terms of use string | string |\
| **user**<br>_optional_ | Associated user ID | string |\
\
## system.features\_enum [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#systemfeatures_enum "Direct link to system.features_enum")\
\
_Type_ : enum (user\_management, user\_management\_advanced, permissions, applications, experiments, queues, queue\_management, data\_management, config\_vault, app\_management, pipelines, reports, show\_dashboard, show\_model\_view, show\_projects, resource\_dashboard, sso\_management, service\_users, resource\_policy, show\_datasets, show\_orchestration, model\_serving, show\_app\_gateways, project\_workloads, tenant\_usages)\
\
## system.match\_set [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#systemmatch_set "Direct link to system.match_set")\
\
| Name | Schema |\
| --- | --- |\
| **rules**<br>_optional_ | < [system.match\_spec](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#system-match_spec) \> array |\
\
## system.match\_spec [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#systemmatch_spec "Direct link to system.match_spec")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **field**<br>_optional_ | Match field. Denotes the object field path this spec references. | string |\
| **obj\_type**<br>_optional_ | Type of object this match spec refers to (e.g. frame) | string |\
| **regex**<br>_optional_ | Python-style regex. This spec matches the field if the field's value is matched <br>by thie regex. | string |\
\
## system.service\_info [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#systemservice_info "Direct link to system.service_info")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **match\_sets**<br>_optional_ | A list of match specs sets. Each nested set represents a set of specs - a <br>nested set is matched if all specs in this nested set match (AND relation). <br>Nested sets have an OR relation, meaning that if at least one of them is <br>matched, the service can be used. | < [system.match\_set](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#system-match_set) \> array |\
| **type**<br>_optional_ | Service type | string |\
| **url**<br>_optional_ | Service URL | string |\
| **use\_fallback**<br>_optional_ | If set and url is not responding then the original url will be contacted | boolean |\
\
## system.version [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#systemversion "Direct link to system.version")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **comment**<br>_optional_ | Version comment | string |\
| **committed**<br>_optional_ | Commit time | string (date-time) |\
| **committed\_frames\_ts**<br>_optional_ | Timestamp of last committed frame | number |\
| **committed\_rois\_ts**<br>_optional_ | Timestamp of last committed ROI | number |\
| **company**<br>_optional_ | Company ID | string |\
| **created**<br>_optional_ | Version creation time (UTC) | string (date-time) |\
| **dataset**<br>_optional_ | Datset ID | string |\
| **es\_index**<br>_optional_ | Name of elasticsearch index | string |\
| **id**<br>_optional_ | Version ID | string |\
| **last\_frames\_update**<br>_optional_ | Last time version was created, committed or frames were updated or saved | string (date-time) |\
| **metadata**<br>_optional_ | User-provided metadata | object |\
| **name**<br>_optional_ | Version name | string |\
| **parent**<br>_optional_ | Version parent ID | string |\
| **published**<br>_optional_ | Publish time | string (date-time) |\
| **status**<br>_optional_ | Version status | [system.version\_status\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#system-version_status_enum) |\
| **system\_tags**<br>_optional_ | List of system tags. This field is reserved for system use, please don't use <br>it. | < string > array |\
| **tags**<br>_optional_ | List of user-defined tags | < string > array |\
| **task**<br>_optional_ | Task ID of the task which created the version | string |\
| **user**<br>_optional_ | Associated user ID | string |\
\
## system.version\_status\_enum [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#systemversion_status_enum "Direct link to system.version_status_enum")\
\
_Type_ : enum (draft, committing, committed, published)\
\
## tasks.artifact [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#tasksartifact "Direct link to tasks.artifact")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **content\_size**<br>_optional_ | Raw data length in bytes | integer |\
| **display\_data**<br>_optional_ | User-defined list of key/value pairs, sorted | < < string > array > array |\
| **hash**<br>_optional_ | Hash of entire raw data | string |\
| **key**<br>_required_ | Entry key | string |\
| **mode**<br>_optional_ | System defined input/output indication | [tasks.artifact\_mode\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasks-artifact_mode_enum) |\
| **timestamp**<br>_optional_ | Epoch time when artifact was created | integer |\
| **type**<br>_required_ | System defined type | string |\
| **type\_data**<br>_optional_ | Additional fields defined by the system | [tasks.artifact\_type\_data](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasks-artifact_type_data) |\
| **uri**<br>_optional_ | Raw data location | string |\
\
## tasks.artifact\_id [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#tasksartifact_id "Direct link to tasks.artifact_id")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **key**<br>_required_ | Entry key | string |\
| **mode**<br>_optional_ | System defined input/output indication | [tasks.artifact\_mode\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasks-artifact_mode_enum) |\
\
## tasks.artifact\_mode\_enum [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#tasksartifact_mode_enum "Direct link to tasks.artifact_mode_enum")\
\
_Type_ : enum (input, output)\
\
## tasks.artifact\_type\_data [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#tasksartifact_type_data "Direct link to tasks.artifact_type_data")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **content\_type**<br>_optional_ | System defined raw data content type | string |\
| **data\_hash**<br>_optional_ | Hash of raw data, without any headers or descriptive parts | string |\
| **preview**<br>_optional_ | Description or textual data | string |\
\
## tasks.augmentation [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#tasksaugmentation "Direct link to tasks.augmentation")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **crop\_around\_rois**<br>_optional_ | Crop image data around all frame ROIs | boolean |\
| **sets**<br>_optional_ | List of augmentation sets | < [tasks.augmentation\_set](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasks-augmentation_set) \> array |\
\
## tasks.augmentation\_set [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#tasksaugmentation_set "Direct link to tasks.augmentation_set")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **arguments**<br>_optional_ | Arguments dictionary per custom augmentation type. | < string, object > map |\
| **cls**<br>_optional_ | Augmentation class | string |\
| **strength**<br>_optional_ | Augmentation strength. Range \[0,). <br>**Minimum value** : `0` | number |\
| **types**<br>_optional_ | Augmentation type | < string > array |\
\
## tasks.configuration\_item [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#tasksconfiguration_item "Direct link to tasks.configuration_item")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **description**<br>_optional_ | The parameter description. Optional | string |\
| **name**<br>_optional_ | Name of the parameter. Should be unique | string |\
| **type**<br>_optional_ | Type of the parameter. Optional | string |\
| **value**<br>_optional_ | Value of the parameter | string |\
\
## tasks.execution [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#tasksexecution "Direct link to tasks.execution")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **artifacts**<br>_optional_ | Task artifacts | < [tasks.artifact](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasks-artifact) \> array |\
| **dataviews**<br>_optional_ | Additional dataviews for the task | < object > array |\
| **docker\_cmd**<br>_optional_ | Command for running docker script for the execution of the task | string |\
| **framework**<br>_optional_ | Framework related to the task. Case insensitive. Mandatory for Training tasks. | string |\
| **model**<br>_optional_ | Execution input model ID Not applicable for Register (Import) tasks | string |\
| **model\_desc**<br>_optional_ | Json object representing the Model descriptors | object |\
| **model\_labels**<br>_optional_ | Json object representing the ids of the labels in the model. The keys are the <br>layers' names and the values are the IDs. Not applicable for Register (Import) <br>tasks. Mandatory for Training tasks | < string, integer > map |\
| **parameters**<br>_optional_ | Json object containing the Task parameters | object |\
| **queue**<br>_optional_ | Queue ID where task was queued. | string |\
| **test\_split**<br>_optional_ | Percentage of frames to use for testing only | integer |\
\
## tasks.execution\_15 [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#tasksexecution_15 "Direct link to tasks.execution_15")\
\
Task execution params\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **dataviews**<br>_optional_ | key to embedded Dataview mapping | object |\
| **framework**<br>_optional_ | Framework related to the task. Case insensitive. Mandatory for Training tasks. | string |\
| **model**<br>_optional_ | Execution input model ID Not applicable for Register (Import) tasks | string |\
| **model\_desc**<br>_optional_ | Json object representing the Model descriptors | object |\
| **model\_labels**<br>_optional_ | Json object representing the ids of the labels in the model. The keys are the <br>layers' names and the values are the IDs. Not applicable for Register (Import) <br>tasks. Mandatory for Training tasks | < string, integer > map |\
| **parameters**<br>_optional_ | Json object containing the Task parameters | object |\
| **queue**<br>_optional_ | Queue ID where task was queued. | string |\
| **test\_split**<br>_optional_ | Percentage of frames to use for testing only | integer |\
\
## tasks.filter\_by\_roi\_enum [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#tasksfilter_by_roi_enum "Direct link to tasks.filter_by_roi_enum")\
\
_Type_ : enum (disabled, no\_rois, label\_rules)\
\
## tasks.filter\_label\_rule [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#tasksfilter_label_rule "Direct link to tasks.filter_label_rule")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **conf\_range**<br>_optional_ | Range of ROI confidence level in the frame (min, max). -1 for not applicable <br>Both min and max can be either -1 or positive. 2nd number (max) must be either <br>-1 or larger than or equal to the 1st number (min) | < number > array |\
| **count\_range**<br>_optional_ | Range of times ROI appears in the frame (min, max). -1 for not applicable. Both <br>integers must be larger than or equal to -1. 2nd integer (max) must be either <br>-1 or larger than or equal to the 1st integer (min) | < integer > array |\
| **label**<br>_required_ | Lucene format query (see lucene query syntax). Default search field is <br>label.keyword and default operator is AND, so searching for: <br>'Bus Stop' Blue <br>is equivalent to: <br>Label.keyword:'Bus Stop' AND label.keyword:'Blue' | string |\
| **must\_not**<br>_optional_ | If set then the label must not exist or lucene query must not be true. The <br>default value is false <br>**Default** : `false` | boolean |\
\
## tasks.filter\_rule [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#tasksfilter_rule "Direct link to tasks.filter_rule")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **dataset**<br>_required_ | Dataset ID. Must be a dataset which is in the task's view. If set to '\*' all <br>datasets in View are used. | string |\
| **filter\_by\_roi**<br>_optional_ | Type of filter. Optional, the default value is 'label\_rules' | [tasks.filter\_by\_roi\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasks-filter_by_roi_enum) |\
| **frame\_query**<br>_optional_ | Frame filter, in Lucene query syntax | string |\
| **label\_rules**<br>_optional_ | List of FilterLabelRule ('AND' connection) <br>disabled - No filtering by ROIs. Select all frames, even if they don't have <br>ROIs (all frames) <br>no\_rois - Select only frames without ROIs (empty frames) <br>label\_rules - Select frames according to label rules | < [tasks.filter\_label\_rule](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasks-filter_label_rule) \> array |\
| **sources\_query**<br>_optional_ | Sources filter, in Lucene query syntax. Filters sources in each frame. | string |\
| **vector\_search**<br>_optional_ | Vector search rule | [vector\_search](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasks-filter_rule-vector_search) |\
| **version**<br>_optional_ | Dataset version to apply rule to. Must belong to the dataset and be in the <br>task's view. If set to '\*' all version of the datasets in View are used. | string |\
| **weight**<br>_optional_ | Rule weight. Default is 1 | number |\
\
**vector\_search**\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **field**<br>_required_ | Vector field name | string |\
| **min\_score**<br>_optional_ | Min allowed score | number |\
| **similarity\_func**<br>_optional_ | The function for calculating distance from the search vector | [tasks.similarity\_function](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasks-similarity_function) |\
| **sort**<br>_optional_ |  | enum (asc, desc) |\
| **vector**<br>_required_ | The search vector | < number > array |\
\
## tasks.filtering [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#tasksfiltering "Direct link to tasks.filtering")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **filtering\_rules**<br>_optional_ | List of FilterRule ('OR' connection) | < [tasks.filter\_rule](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasks-filter_rule) \> array |\
| **output\_rois**<br>_optional_ | 'all\_in\_frame' - all rois for a frame are returned <br>'only\_filtered' - only rois which led this frame to be selected <br>'frame\_per\_roi' - single roi per frame. Frame can be returned multiple times <br>with a different roi each time. <br>Note: this should be used for Training tasks only <br>Note: frame\_per\_roi implies that only filtered rois will be returned | [tasks.output\_rois\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasks-output_rois_enum) |\
\
## tasks.input [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#tasksinput "Direct link to tasks.input")\
\
Task input params. (input view must be provided).\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **augmentation**<br>_optional_ | Augmentation parameters. Only for training and testing tasks. | [tasks.augmentation](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasks-augmentation) |\
| **dataviews**<br>_optional_ | Key to DataView ID Mapping | < string, string > map |\
| **frames\_filter**<br>_optional_ | Filtering params | [tasks.filtering](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasks-filtering) |\
| **iteration**<br>_optional_ | Iteration parameters. Not applicable for register (import) tasks. | [tasks.iteration](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasks-iteration) |\
| **mapping**<br>_optional_ | Mapping params (see common definitions section) | [tasks.mapping](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasks-mapping) |\
| **view**<br>_optional_ | View params | [tasks.view](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasks-view) |\
\
## tasks.iteration [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#tasksiteration "Direct link to tasks.iteration")\
\
Sequential Iteration API configuration\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **infinite**<br>_optional_ | Infinite iteration | boolean |\
| **jump**<br>_optional_ | Jump entry | [tasks.jump](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasks-jump) |\
| **limit**<br>_optional_ | Maximum frames per task. If not passed, frames will end when no more matching <br>frames are found, unless infinite is True. | integer |\
| **min\_sequence**<br>_optional_ | Length (in ms) of video clips to return. This is used in random order, and in <br>sequential order only if jumping is provided and only for video frames | integer |\
| **order**<br>_optional_ | Input frames order. Values: 'sequential', 'random' In Sequential mode frames <br>will be returned according to the order in which the frames were added to the <br>dataset. | string |\
| **random\_seed**<br>_required_ | Random seed used during iteration | integer |\
\
## tasks.jump [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#tasksjump "Direct link to tasks.jump")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **time**<br>_optional_ | Max time in milliseconds between frames | integer |\
\
## tasks.label\_source [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#taskslabel_source "Direct link to tasks.label_source")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **dataset**<br>_optional_ | Source dataset id. '\*' for all datasets in view | string |\
| **labels**<br>_optional_ | List of source labels (AND connection). '\*' indicates any label. Labels must <br>exist in at least one of the dataset versions in the task's view | < string > array |\
| **version**<br>_optional_ | Source dataset version id. Default is '\*' (for all versions in dataset in the <br>view) Version must belong to the selected dataset, and must be in the task's <br>view\[i\] | string |\
\
## tasks.last\_metrics\_event [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#taskslast_metrics_event "Direct link to tasks.last_metrics_event")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **count**<br>_optional_ | The total count of reported values | integer |\
| **first\_value**<br>_optional_ | First value reported | number |\
| **first\_value\_iteration**<br>_optional_ | The iteration at which the first value was reported | integer |\
| **max\_value**<br>_optional_ | Maximum value reported | number |\
| **max\_value\_iteration**<br>_optional_ | The iteration at which the maximum value was reported | integer |\
| **mean\_value**<br>_optional_ | The mean value | number |\
| **metric**<br>_optional_ | Metric name | string |\
| **min\_value**<br>_optional_ | Minimum value reported | number |\
| **min\_value\_iteration**<br>_optional_ | The iteration at which the minimum value was reported | integer |\
| **value**<br>_optional_ | Last value reported | number |\
| **variant**<br>_optional_ | Variant name | string |\
| **x\_axis\_label**<br>_optional_ | The user defined value for the X-Axis name stored with the event | string |\
\
## tasks.last\_metrics\_variants [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#taskslast_metrics_variants "Direct link to tasks.last_metrics_variants")\
\
Last metric events, one for each variant hash\
\
_Type_ : < string, [tasks.last\_metrics\_event](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasks-last_metrics_event) \> map\
\
## tasks.mapping [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#tasksmapping "Direct link to tasks.mapping")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **rules**<br>_optional_ | Rules list | < [tasks.mapping\_rule](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasks-mapping_rule) \> array |\
\
## tasks.mapping\_rule [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#tasksmapping_rule "Direct link to tasks.mapping_rule")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **source**<br>_optional_ | Source label info | [tasks.label\_source](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasks-label_source) |\
| **target**<br>_optional_ | Target label name | string |\
\
## tasks.model\_type\_enum [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#tasksmodel_type_enum "Direct link to tasks.model_type_enum")\
\
_Type_ : enum (input, output)\
\
## tasks.multi\_field\_pattern\_data [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#tasksmulti_field_pattern_data "Direct link to tasks.multi_field_pattern_data")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **datetime**<br>_optional_ | Date time conditions (applicable only to datetime fields). Either 'pattern' or <br>'datetime' should be specified | string |\
| **fields**<br>_optional_ | List of field names | < string > array |\
| **pattern**<br>_optional_ | Pattern string (regex). Either 'pattern' or 'datetime' should be specified | string |\
\
## tasks.output [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#tasksoutput "Direct link to tasks.output")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **destination**<br>_optional_ | Storage id. This is where output files will be stored. | string |\
| **error**<br>_optional_ | Last error text | string |\
| **model**<br>_optional_ | Model id. | string |\
| **result**<br>_optional_ | Task result. Values: 'success', 'failure' | string |\
| **view**<br>_optional_ | View params | [tasks.view](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasks-view) |\
\
## tasks.output\_rois\_enum [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#tasksoutput_rois_enum "Direct link to tasks.output_rois_enum")\
\
_Type_ : enum (all\_in\_frame, only\_filtered, frame\_per\_roi)\
\
## tasks.param\_key [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#tasksparam_key "Direct link to tasks.param_key")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **name**<br>_optional_ | Name of the parameter. If the name is ommitted then the corresponding operation <br>is performed on the whole section | string |\
| **section**<br>_optional_ | Section that the parameter belongs to | string |\
\
## tasks.params\_item [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#tasksparams_item "Direct link to tasks.params_item")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **description**<br>_optional_ | The parameter description. Optional | string |\
| **name**<br>_optional_ | Name of the parameter. The combination of section and name should be unique | string |\
| **section**<br>_optional_ | Section that the parameter belongs to | string |\
| **type**<br>_optional_ | Type of the parameter. Optional | string |\
| **value**<br>_optional_ | Value of the parameter | string |\
\
## tasks.replace\_hyperparams\_enum [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#tasksreplace_hyperparams_enum "Direct link to tasks.replace_hyperparams_enum")\
\
_Type_ : enum (none, section, all)\
\
## tasks.script [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#tasksscript "Direct link to tasks.script")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **binary**<br>_optional_ | Binary to use when running the script <br>**Default** : `"python"` | string |\
| **branch**<br>_optional_ | Repository branch id If not provided and tag not provided, default repository <br>branch is used. | string |\
| **diff**<br>_optional_ | Uncommitted changes found in the repository when task was run | string |\
| **entry\_point**<br>_optional_ | Path to execute within the repository | string |\
| **repository**<br>_optional_ | Name of the repository where the script is located | string |\
| **requirements**<br>_optional_ | A JSON object containing requirements strings by key | object |\
| **tag**<br>_optional_ | Repository tag | string |\
| **version\_num**<br>_optional_ | Version (changeset) number. Optional (default is head version) Unused if tag is <br>provided. | string |\
| **working\_dir**<br>_optional_ | Path to the folder from which to run the script Default - root folder of <br>repository | string |\
\
## tasks.section\_params [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#taskssection_params "Direct link to tasks.section_params")\
\
Task section params\
\
_Type_ : < string, [tasks.params\_item](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasks-params_item) \> map\
\
## tasks.similarity\_function [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#taskssimilarity_function "Direct link to tasks.similarity_function")\
\
_Type_ : enum (l2\_norm, dot\_product, cosine)\
\
## tasks.task [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#taskstask "Direct link to tasks.task")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **active\_duration**<br>_optional_ | Task duration time (seconds) | integer |\
| **comment**<br>_optional_ | Free text comment | string |\
| **company**<br>_optional_ | Company ID | string |\
| **completed**<br>_optional_ | Task end time (UTC) | string (date-time) |\
| **configuration**<br>_optional_ | Task configuration params | < string, [tasks.configuration\_item](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasks-configuration_item) \> map |\
| **container**<br>_optional_ | Docker container parameters | < string, string > map |\
| **created**<br>_optional_ | Task creation time (UTC) | string (date-time) |\
| **execution**<br>_optional_ | Task execution params | [tasks.execution](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasks-execution) |\
| **hyperparams**<br>_optional_ | Task hyper params per section | < string, [tasks.section\_params](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasks-section_params) \> map |\
| **id**<br>_optional_ | Task id | string |\
| **input**<br>_optional_ | Task input params | [tasks.input](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasks-input) |\
| **last\_change**<br>_optional_ | Last time any update was done to the task | string (date-time) |\
| **last\_iteration**<br>_optional_ | Last iteration reported for this task | integer |\
| **last\_metrics**<br>_optional_ | Last metric variants (hash to events), one for each metric hash | < string, [tasks.last\_metrics\_variants](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasks-last_metrics_variants) \> map |\
| **last\_update**<br>_optional_ | Last time this task was created, edited, changed or events for this task were <br>reported | string (date-time) |\
| **last\_worker**<br>_optional_ | ID of last worker that handled the task | string |\
| **last\_worker\_report**<br>_optional_ | Last time a worker reported while working on this task | string (date-time) |\
| **models**<br>_optional_ | Task models | [tasks.task\_models](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasks-task_models) |\
| **name**<br>_optional_ | Task Name | string |\
| **output**<br>_optional_ | Task output params | [tasks.output](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasks-output) |\
| **parent**<br>_optional_ | Parent task id | string |\
| **project**<br>_optional_ | Project ID of the project to which this task is assigned | string |\
| **published**<br>_optional_ | Task publish time | string (date-time) |\
| **runtime**<br>_optional_ | Task runtime mapping | object |\
| **script**<br>_optional_ | Script info | [tasks.script](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasks-script) |\
| **started**<br>_optional_ | Task start time (UTC) | string (date-time) |\
| **status**<br>_optional_ |  | [tasks.task\_status\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasks-task_status_enum) |\
| **status\_changed**<br>_optional_ | Last status change time | string (date-time) |\
| **status\_message**<br>_optional_ | free text string representing info about the status | string |\
| **status\_reason**<br>_optional_ | Reason for last status change | string |\
| **system\_tags**<br>_optional_ | System tags list. This field is reserved for system use, please don't use it. | < string > array |\
| **tags**<br>_optional_ | User-defined tags list | < string > array |\
| **type**<br>_optional_ | Type of task. Values: 'dataset\_import', 'annotation', 'training', 'testing' | [tasks.task\_type\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasks-task_type_enum) |\
| **user**<br>_optional_ | Associated user id | string |\
\
## tasks.task\_15 [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#taskstask_15 "Direct link to tasks.task_15")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **comment**<br>_optional_ | Free text comment | string |\
| **company**<br>_optional_ | Company ID | string |\
| **completed**<br>_optional_ | Task end time (UTC) | string (date-time) |\
| **created**<br>_optional_ | Task creation time (UTC) | string (date-time) |\
| **execution**<br>_optional_ |  | [tasks.execution\_15](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasks-execution_15) |\
| **id**<br>_optional_ | Task id | string |\
| **input**<br>_optional_ |  | [tasks.input](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasks-input) |\
| **last\_change**<br>_optional_ | Last time any update was done to the task | string (date-time) |\
| **last\_iteration**<br>_optional_ | Last iteration reported for this task | integer |\
| **last\_metrics**<br>_optional_ | Last metric variants (hash to events), one for each metric hash | < string, [tasks.last\_metrics\_variants](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasks-last_metrics_variants) \> map |\
| **last\_update**<br>_optional_ | Last time this task was created, edited, changed or events for this task were <br>reported | string (date-time) |\
| **last\_worker**<br>_optional_ | ID of last worker that handled the task | string |\
| **last\_worker\_report**<br>_optional_ | Last time a worker reported while working on this task | string (date-time) |\
| **name**<br>_optional_ | Task Name | string |\
| **output**<br>_optional_ | Task output params | [tasks.output](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasks-output) |\
| **parent**<br>_optional_ | Parent task id | string |\
| **project**<br>_optional_ | Project ID of the project to which this task is assigned | string |\
| **published**<br>_optional_ | Last status change time | string (date-time) |\
| **script**<br>_optional_ |  | [tasks.script](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasks-script) |\
| **started**<br>_optional_ | Task start time (UTC) | string (date-time) |\
| **status**<br>_optional_ |  | [tasks.task\_status\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasks-task_status_enum) |\
| **status\_changed**<br>_optional_ | Last status change time | string (date-time) |\
| **status\_message**<br>_optional_ | free text string representing info about the status | string |\
| **status\_reason**<br>_optional_ | Reason for last status change | string |\
| **system\_tags**<br>_optional_ | System tags list. This field is reserved for system use, please don't use it. | < string > array |\
| **tags**<br>_optional_ | User-defined tags list | < string > array |\
| **type**<br>_optional_ | Type of task. Values: 'dataset\_import', 'annotation', 'training', 'testing' | [tasks.task\_type\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasks-task_type_enum) |\
| **user**<br>_optional_ | Associated user id | string |\
\
## tasks.task\_model\_item [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#taskstask_model_item "Direct link to tasks.task_model_item")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **model**<br>_required_ | The model ID | string |\
| **name**<br>_required_ | The task model name | string |\
\
## tasks.task\_models [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#taskstask_models "Direct link to tasks.task_models")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **input**<br>_optional_ | The list of task input models | < [tasks.task\_model\_item](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasks-task_model_item) \> array |\
| **output**<br>_optional_ | The list of task output models | < [tasks.task\_model\_item](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasks-task_model_item) \> array |\
\
## tasks.task\_status\_enum [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#taskstask_status_enum "Direct link to tasks.task_status_enum")\
\
_Type_ : enum (created, queued, in\_progress, stopped, published, publishing, closed, failed, completed, unknown)\
\
## tasks.task\_type\_enum [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#taskstask_type_enum "Direct link to tasks.task_type_enum")\
\
Type of task\
\
_Type_ : enum (dataset\_import, annotation, annotation\_manual, training, testing, inference, data\_processing, application, monitor, controller, optimizer, service, qc, agent, custom)\
\
## tasks.task\_urls [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#taskstask_urls "Direct link to tasks.task_urls")\
\
| Name | Schema |\
| --- | --- |\
| **artifact\_urls**<br>_optional_ | < string > array |\
| **event\_urls**<br>_optional_ | < string > array |\
| **model\_urls**<br>_optional_ | < string > array |\
\
## tasks.view [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#tasksview "Direct link to tasks.view")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **entries**<br>_optional_ | List of view entries. All tasks must have at least one view. | < [tasks.view\_entry](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasks-view_entry) \> array |\
\
## tasks.view\_entry [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#tasksview_entry "Direct link to tasks.view_entry")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **dataset**<br>_optional_ | Existing Dataset id | string |\
| **merge\_with**<br>_optional_ | Version ID to merge with | string |\
| **version**<br>_optional_ | Version id of a version belonging to the dataset | string |\
\
## tenants.resource\_usage\_series [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#tenantsresource_usage_series "Direct link to tenants.resource_usage_series")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **dates**<br>_optional_ | List of timestamps (in milliseconds from epoch) in ascending order, separated <br>by the requested interval. | < integer > array |\
| **title**<br>_optional_ | The title of the series | string |\
| **values**<br>_optional_ | List of values corresponding to the timestamps in the dates list. | < number > array |\
\
## users.assignable\_role [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#usersassignable_role "Direct link to users.assignable_role")\
\
Roles that can be assigned to a user via the API\
\
_Type_ : enum (admin, user, consumer)\
\
## users.features\_enum [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#usersfeatures_enum "Direct link to users.features_enum")\
\
_Type_ : enum (user\_management, user\_management\_advanced, permissions, applications, experiments, queues, queue\_management, data\_management, config\_vault, app\_management, pipelines, reports, show\_dashboard, show\_model\_view, show\_projects, resource\_dashboard, sso\_management, service\_users, resource\_policy, show\_datasets, show\_orchestration, model\_serving, show\_app\_gateways, project\_workloads, tenant\_usages)\
\
## users.get\_current\_user\_response\_user\_object [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#usersget_current_user_response_user_object "Direct link to users.get_current_user_response_user_object")\
\
like user, but returns company object instead of ID\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **avatar**<br>_optional_ |  | string |\
| **companies**<br>_optional_ |  | < [companies](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#users-get_current_user_response_user_object-companies) \> array |\
| **company**<br>_optional_ |  | [company](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#users-get_current_user_response_user_object-company) |\
| **created**<br>_optional_ | User creation time | string (date-time) |\
| **created\_in\_version**<br>_optional_ | Server version at user creation time | string |\
| **email**<br>_optional_ | User email | string |\
| **family\_name**<br>_optional_ |  | string |\
| **given\_name**<br>_optional_ |  | string |\
| **id**<br>_optional_ |  | string |\
| **name**<br>_optional_ |  | string |\
| **preferences**<br>_optional_ | User preferences | object |\
| **role**<br>_optional_ |  | string |\
| **terms\_of\_use\_ver\_accepted**<br>_optional_ |  | number |\
\
**companies**\
\
| Name | Schema |\
| --- | --- |\
| **active**<br>_optional_ | boolean |\
| **id**<br>_optional_ | string |\
| **name**<br>_optional_ | string |\
| **tier**<br>_optional_ | enum (free, paid, suspended) |\
\
**company**\
\
| Name | Schema |\
| --- | --- |\
| **id**<br>_optional_ | string |\
| **name**<br>_optional_ | string |\
| **tier**<br>_optional_ | enum (free, paid, suspended) |\
\
## users.get\_current\_user\_response\_user\_object\_v1\_5 [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#usersget_current_user_response_user_object_v1_5 "Direct link to users.get_current_user_response_user_object_v1_5")\
\
like user, but returns company object instead of ID\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **avatar**<br>_optional_ |  | string |\
| **companies**<br>_optional_ |  | < [companies](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#users-get_current_user_response_user_object_v1_5-companies) \> array |\
| **company**<br>_optional_ |  | [company](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#users-get_current_user_response_user_object_v1_5-company) |\
| **email**<br>_optional_ | User email | string |\
| **family\_name**<br>_optional_ |  | string |\
| **given\_name**<br>_optional_ |  | string |\
| **id**<br>_optional_ |  | string |\
| **name**<br>_optional_ |  | string |\
| **preferences**<br>_optional_ | User preferences | object |\
| **role**<br>_optional_ |  | string |\
| **terms\_of\_use\_ver\_accepted**<br>_optional_ |  | number |\
\
**companies**\
\
| Name | Schema |\
| --- | --- |\
| **active**<br>_optional_ | boolean |\
| **id**<br>_optional_ | string |\
| **name**<br>_optional_ | string |\
| **tier**<br>_optional_ | enum (free, paid, suspended) |\
\
**company**\
\
| Name | Schema |\
| --- | --- |\
| **id**<br>_optional_ | string |\
| **name**<br>_optional_ | string |\
| **tier**<br>_optional_ | enum (free, paid, suspended) |\
\
## users.get\_current\_user\_response\_user\_object\_v\_2\_2\_0 [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#usersget_current_user_response_user_object_v_2_2_0 "Direct link to users.get_current_user_response_user_object_v_2_2_0")\
\
like user, but returns company object instead of ID\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **avatar**<br>_optional_ |  | string |\
| **companies**<br>_optional_ |  | < [companies](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#users-get_current_user_response_user_object_v_2_2_0-companies) \> array |\
| **company**<br>_optional_ |  | [company](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#users-get_current_user_response_user_object_v_2_2_0-company) |\
| **created**<br>_optional_ | User creation time | string (date-time) |\
| **email**<br>_optional_ | User email | string |\
| **family\_name**<br>_optional_ |  | string |\
| **given\_name**<br>_optional_ |  | string |\
| **id**<br>_optional_ |  | string |\
| **name**<br>_optional_ |  | string |\
| **preferences**<br>_optional_ | User preferences | object |\
| **role**<br>_optional_ |  | string |\
| **terms\_of\_use\_ver\_accepted**<br>_optional_ |  | number |\
\
**companies**\
\
| Name | Schema |\
| --- | --- |\
| **active**<br>_optional_ | boolean |\
| **id**<br>_optional_ | string |\
| **name**<br>_optional_ | string |\
| **tier**<br>_optional_ | enum (free, paid, suspended) |\
\
**company**\
\
| Name | Schema |\
| --- | --- |\
| **id**<br>_optional_ | string |\
| **name**<br>_optional_ | string |\
| **tier**<br>_optional_ | enum (free, paid, suspended) |\
\
## users.login\_white\_list\_v1\_5 [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#userslogin_white_list_v1_5 "Direct link to users.login_white_list_v1_5")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **company**<br>_optional_ | Company | string |\
| **domain**<br>_optional_ | Email domain name (all addresses under the domain are included in this <br>whitelist entry) | string (hostname) |\
| **emails**<br>_optional_ | List of email addresses (all addresses in this list are included in this <br>whitelist entry) | < string (email) > array |\
| **group**<br>_optional_ | Group ID to be assigned to users added through this whitelist | string |\
| **id**<br>_optional_ | Whitelist entry ID | string |\
\
## users.role [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#usersrole "Direct link to users.role")\
\
_Type_ : enum (admin, superuser, user, annotator, consumer)\
\
## users.terms\_of\_use [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#usersterms_of_use "Direct link to users.terms_of_use")\
\
Terms of use for the ClearML platform\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **created**<br>_optional_ | Create time | string (date-time) |\
| **deprecated**<br>_optional_ | Indicates whether this version has been deprecated | boolean |\
| **text**<br>_optional_ | Terms of use text | string |\
| **update**<br>_optional_ | Last update time | string (date-time) |\
| **version**<br>_optional_ | Version number | number |\
\
## users.user [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#usersuser "Direct link to users.user")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **activity**<br>_optional_ |  | [activity](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#users-user-activity) |\
| **avatar**<br>_optional_ | Avatar URL | string |\
| **company**<br>_optional_ | Company ID | string |\
| **created**<br>_optional_ | User creation date | string (date-time) |\
| **email**<br>_optional_ | User email | string (email) |\
| **family\_name**<br>_optional_ | Family name | string |\
| **given\_name**<br>_optional_ | Given name | string |\
| **id**<br>_optional_ | User ID | string |\
| **name**<br>_optional_ | Full name | string |\
| **providers**<br>_optional_ | Providers uses has logged-in with | object |\
| **read\_only**<br>_optional_ | Whether the user can be deleted or his role edited | boolean |\
| **role**<br>_optional_ | User's role (admin only) | string |\
| **sec\_groups**<br>_optional_ | The list of security groups that the user is member of | < string > array |\
| **support**<br>_optional_ | Whether the user is a support user | boolean |\
| **terms\_of\_use\_ver\_accepted**<br>_optional_ | Terms of Use version number accepted by the user | number |\
\
**activity**\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **last\_credentials\_login**<br>_optional_ | The last time when user credentials were used | string (date-time) |\
| **last\_provider**<br>_optional_ | The provider that was used for the last login | string |\
| **last\_provider\_login**<br>_optional_ | The last time when provider login was used used | string (date-time) |\
| **last\_provider\_name**<br>_optional_ | The last provider name | string |\
| **last\_ui\_access**<br>_optional_ | The last time when UI was accessed by the user | string (date-time) |\
\
## users.vault [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#usersvault "Direct link to users.vault")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **data**<br>_optional_ | Vault data | string |\
| **description**<br>_optional_ | Vault description | string |\
| **enabled**<br>_optional_ | Is the vaule enabled or disabled <br>**Default** : `true` | boolean |\
| **format**<br>_optional_ | Vault data format <br>**Default** : `"hocon"` | string |\
| **id**<br>_optional_ | Vault ID | string |\
| **scope**<br>_optional_ | Vault scope | enum (organization, group, user) |\
| **type**<br>_optional_ | Vault document type <br>**Default** : `"config"` | string |\
\
## users.vault\_data [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#usersvault_data "Direct link to users.vault_data")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **data**<br>_optional_ | Vault data | string |\
| **description**<br>_optional_ | Vault description | string |\
| **editable**<br>_optional_ | Whether the vault can be edited. False when server encryption is disabled and <br>the vault contains encrypted data | boolean |\
| **enabled**<br>_optional_ | Is the vaule enabled or disabled <br>**Default** : `true` | boolean |\
| **format**<br>_optional_ | Vault data format <br>**Default** : `"hocon"` | string |\
| **group**<br>_optional_ | ID of the group that the vault belongs to | string |\
| **group\_name**<br>_optional_ | The name of the vault group. Returned only for the group vaults | string |\
| **id**<br>_optional_ | Vault ID | string |\
| **last\_update**<br>_optional_ | Last vault update time. Reflects the time when the vault was created or last <br>updated | string (date-time) |\
| **scope**<br>_optional_ | Vault scope | enum (organization, group, user) |\
| **type**<br>_optional_ | Vault document type <br>**Default** : `"config"` | string |\
| **user**<br>_optional_ | ID of the user that the vault belongs to | string |\
\
## variables.increment\_command [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#variablesincrement_command "Direct link to variables.increment_command")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **allow\_partial**<br>_optional_ | If set then incrementing by a value that is smaller then requested is allowed <br>**Default** : `true` | boolean |\
| **expiration\_sec**<br>_optional_ | Expiration period in seconds to retain the variable. If not set then the <br>variable will never expire | integer |\
| **increment**<br>_optional_ | The number to be added to the global var | string |\
| **key**<br>_optional_ | The key of the variable to increment. The variable should hold an integer value | integer |\
| **max\_allowed\_value**<br>_optional_ | The maximum allowed value for the variable after the increment. If not set then <br>the operation is not limited | integer |\
| **min\_allowed\_value**<br>_optional_ | The minimum allowed value for the variable after the increment. If not set then <br>the operation is not limited | integer |\
\
## variables.variable [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#variablesvariable "Direct link to variables.variable")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **expiration\_sec**<br>_optional_ | Expiration period in seconds to retain the variable. If not set then the <br>variable will never expire | integer |\
| **key**<br>_optional_ | Variable key | string |\
| **value**<br>_optional_ | Variable value | string |\
\
## workers.activity\_series [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#workersactivity_series "Direct link to workers.activity_series")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **counts**<br>_optional_ | List of counts corresponding to the timestamps in the dates list. | < integer > array |\
| **dates**<br>_optional_ | List of timestamps (in seconds from epoch) in the acceding order. The <br>timestamps are separated by the requested interval. | < integer > array |\
\
## workers.aggregation\_stats [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#workersaggregation_stats "Direct link to workers.aggregation_stats")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **aggregation**<br>_optional_ |  | [workers.aggregation\_type](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#workers-aggregation_type) |\
| **dates**<br>_optional_ | List of timestamps (in seconds from epoch) in the acceding order. The <br>timestamps are separated by the requested interval. Timestamps where no workers <br>activity was recorded are omitted. | < integer > array |\
| **resource\_series**<br>_optional_ | Metric data per single resource. Return only if split\_by\_resource request <br>parameter is set to True | < [workers.metric\_resource\_series](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#workers-metric_resource_series) \> array |\
| **values**<br>_optional_ | List of values corresponding to the dates in metric statistics | < number > array |\
\
## workers.aggregation\_type [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#workersaggregation_type "Direct link to workers.aggregation_type")\
\
Metric aggregation type\
\
_Type_ : enum (avg, min, max)\
\
## workers.current\_task\_entry [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#workerscurrent_task_entry "Direct link to workers.current_task_entry")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **id**<br>_optional_ | Worker ID | string |\
| **last\_iteration**<br>_optional_ | Last task iteration | integer |\
| **name**<br>_optional_ | Worker name | string |\
| **running\_time**<br>_optional_ | Task running time | integer |\
\
## workers.id\_name\_entry [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#workersid_name_entry "Direct link to workers.id_name_entry")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **id**<br>_optional_ | Worker ID | string |\
| **name**<br>_optional_ | Worker name | string |\
\
## workers.machine\_stats [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#workersmachine_stats "Direct link to workers.machine_stats")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **cpu\_temperature**<br>_optional_ | CPU temperature | < number > array |\
| **cpu\_usage**<br>_optional_ | Average CPU usage per core | < number > array |\
| **disk\_free\_home**<br>_optional_ | Free space in % of /home drive | number |\
| **disk\_free\_temp**<br>_optional_ | Free space in % of /tmp drive | number |\
| **disk\_read**<br>_optional_ | Mbytes read per second | number |\
| **disk\_write**<br>_optional_ | Mbytes write per second | number |\
| **gpu\_fraction**<br>_optional_ | GPU fraction | < number > array |\
| **gpu\_memory\_free**<br>_optional_ | GPU free memory MBs | < number > array |\
| **gpu\_memory\_used**<br>_optional_ | GPU used memory MBs | < number > array |\
| **gpu\_temperature**<br>_optional_ | GPU temperature | < number > array |\
| **gpu\_usage**<br>_optional_ | Average GPU usage per GPU card | < number > array |\
| **memory\_free**<br>_optional_ | Free memory MBs | number |\
| **memory\_used**<br>_optional_ | Used memory MBs | number |\
| **network\_rx**<br>_optional_ | Mbytes per second | number |\
| **network\_tx**<br>_optional_ | Mbytes per second | number |\
\
## workers.metric\_resource\_series [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#workersmetric_resource_series "Direct link to workers.metric_resource_series")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **name**<br>_optional_ | Resource name | string |\
| **values**<br>_optional_ | List of values corresponding to the dates in metric statistics | < number > array |\
\
## workers.metric\_stats [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#workersmetric_stats "Direct link to workers.metric_stats")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **metric**<br>_optional_ | Name of the metric (cpu\_usage, memory\_used etc.) | string |\
| **stats**<br>_optional_ | Statistics data by type | < [workers.aggregation\_stats](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#workers-aggregation_stats) \> array |\
| **variant**<br>_optional_ | Name of the metric component. Set only if 'split\_by\_variant' was set in the <br>request | string |\
\
## workers.metrics\_category [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#workersmetrics_category "Direct link to workers.metrics_category")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **metric\_keys**<br>_optional_ | The names of the metrics in the category. | < string > array |\
| **name**<br>_optional_ | Name of the metrics category. | string |\
\
## workers.queue\_entry [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#workersqueue_entry "Direct link to workers.queue_entry")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **display\_name**<br>_optional_ | Display name for the queue (if defined) | string |\
| **id**<br>_optional_ | Worker ID | string |\
| **name**<br>_optional_ | Worker name | string |\
| **next\_task**<br>_optional_ | Next task in the queue | [workers.id\_name\_entry](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#workers-id_name_entry) |\
| **num\_tasks**<br>_optional_ | Number of task entries in the queue | integer |\
\
## workers.resource\_usage\_series [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#workersresource_usage_series "Direct link to workers.resource_usage_series")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **dates**<br>_optional_ | List of timestamps (in seconds from epoch) in the acceding order. The <br>timestamps are separated by the requested interval. | < integer > array |\
| **title**<br>_optional_ | The title of the series | string |\
| **values**<br>_optional_ | List of values corresponding to the timestamps in the dates list. | < number > array |\
\
## workers.stat\_item [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#workersstat_item "Direct link to workers.stat_item")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **category**<br>_optional_ |  | [workers.aggregation\_type](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#workers-aggregation_type) |\
| **key**<br>_optional_ | Name of a metric | enum (cpu\_usage, cpu\_temperature, memory\_used, memory\_free, gpu\_usage, gpu\_temperature, gpu\_fraction, gpu\_memory\_free, gpu\_memory\_used, network\_tx, network\_rx, disk\_free\_home, disk\_free\_temp, disk\_read, disk\_write) |\
\
## workers.worker [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#workersworker "Direct link to workers.worker")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **company**<br>_optional_ | Associated company | [workers.id\_name\_entry](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#workers-id_name_entry) |\
| **id**<br>_optional_ | Worker ID | string |\
| **ip**<br>_optional_ | IP of the worker | string |\
| **key**<br>_optional_ | Worker entry key | string |\
| **last\_activity\_time**<br>_optional_ | Last activity time (even if an error occurred) | string (date-time) |\
| **last\_report\_time**<br>_optional_ | Last successful report time | string (date-time) |\
| **project**<br>_optional_ | Project in which currently executing task resides | [workers.id\_name\_entry](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#workers-id_name_entry) |\
| **queue**<br>_optional_ | Queue from which running task was taken | [workers.queue\_entry](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#workers-queue_entry) |\
| **queues**<br>_optional_ | List of queues on which the worker is listening | < [workers.queue\_entry](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#workers-queue_entry) \> array |\
| **register\_time**<br>_optional_ | Registration time | string (date-time) |\
| **system\_tags**<br>_optional_ | System tags for the worker | < string > array |\
| **tags**<br>_optional_ | User tags for the worker | < string > array |\
| **task**<br>_optional_ | Task currently being run by the worker | [workers.current\_task\_entry](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#workers-current_task_entry) |\
| **user**<br>_optional_ | Associated user (under whose credentials are used by the worker daemon) | [workers.id\_name\_entry](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#workers-id_name_entry) |\
\
## workers.worker\_stats [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#workersworker_stats "Direct link to workers.worker_stats")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **metrics**<br>_optional_ | List of the metrics statistics for the worker | < [workers.metric\_stats](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#workers-metric_stats) \> array |\
| **worker**<br>_optional_ | ID of the worker | string |\
\
## workers.worker\_v1\_5 [​](https://clear.ml/docs/latest/docs/references/enterprise/definitions/\#workersworker_v1_5 "Direct link to workers.worker_v1_5")\
\
| Name | Description | Schema |\
| --- | --- | --- |\
| **company**<br>_optional_ | Associated company | [workers.id\_name\_entry](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#workers-id_name_entry) |\
| **id**<br>_optional_ | Worker ID | string |\
| **ip**<br>_optional_ | IP of the worker | string |\
| **last\_activity\_time**<br>_optional_ | Last activity time (even if an error occurred) | string (date-time) |\
| **last\_report\_time**<br>_optional_ | Last successful report time | string (date-time) |\
| **queue**<br>_optional_ | ID of the queue from which task was received | string |\
| **queues**<br>_optional_ | List of queue IDs on which the worker is listening | < string > array |\
| **register\_time**<br>_optional_ | Registration time | string (date-time) |\
| **task**<br>_optional_ | Task currently being run by the worker | [workers.id\_name\_entry](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#workers-id_name_entry) |\
| **user**<br>_optional_ | Associated user (under whose credentials are used by the worker daemon) | [workers.id\_name\_entry](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#workers-id_name_entry) |\
\
- [Definitions](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#definitions)\
- [apps.app\_info](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#appsapp_info)\
- [apps.app\_info\_with\_usages](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#appsapp_info_with_usages)\
- [apps.application\_instance](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#appsapplication_instance)\
- [apps.application\_instance\_status\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#appsapplication_instance_status_enum)\
- [apps.application\_instance\_summary](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#appsapplication_instance_summary)\
- [apps.details\_page\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#appsdetails_page_enum)\
- [apps.task\_status\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#appstask_status_enum)\
- [auth.credential\_key](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#authcredential_key)\
- [auth.credentials](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#authcredentials)\
- [auth.role](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#authrole)\
- [billing.payment\_details](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#billingpayment_details)\
- [billing.resource\_usage](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#billingresource_usage)\
- [datasets.dataset](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#datasetsdataset)\
- [datasets.frame](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#datasetsframe)\
- [datasets.frame\_15](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#datasetsframe_15)\
- [datasets.mask](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#datasetsmask)\
- [datasets.multi\_field\_pattern\_data](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#datasetsmulti_field_pattern_data)\
- [datasets.preview](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#datasetspreview)\
- [datasets.roi](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#datasetsroi)\
- [datasets.roi\_mask](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#datasetsroi_mask)\
- [datasets.schema\_type\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#datasetsschema_type_enum)\
- [datasets.source](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#datasetssource)\
- [datasets.stat\_count](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#datasetsstat_count)\
- [datasets.statistics](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#datasetsstatistics)\
- [datasets.version](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#datasetsversion)\
- [datasets.version\_paradigm\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#datasetsversion_paradigm_enum)\
- [datasets.version\_status\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#datasetsversion_status_enum)\
- [dataviews.augmentation](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#dataviewsaugmentation)\
- [dataviews.augmentation\_set](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#dataviewsaugmentation_set)\
- [dataviews.dataview](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#dataviewsdataview)\
- [dataviews.dataview\_entry](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#dataviewsdataview_entry)\
- [dataviews.filter\_by\_roi\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#dataviewsfilter_by_roi_enum)\
- [dataviews.filter\_label\_rule](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#dataviewsfilter_label_rule)\
- [dataviews.filter\_rule](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#dataviewsfilter_rule)\
- [dataviews.iteration](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#dataviewsiteration)\
- [dataviews.iteration\_order\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#dataviewsiteration_order_enum)\
- [dataviews.jump](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#dataviewsjump)\
- [dataviews.label\_source](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#dataviewslabel_source)\
- [dataviews.mapping](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#dataviewsmapping)\
- [dataviews.mapping\_rule](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#dataviewsmapping_rule)\
- [dataviews.multi\_field\_pattern\_data](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#dataviewsmulti_field_pattern_data)\
- [dataviews.output\_rois\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#dataviewsoutput_rois_enum)\
- [dataviews.similarity\_function](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#dataviewssimilarity_function)\
- [events.debug\_image\_sample\_response](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#eventsdebug_image_sample_response)\
- [events.debug\_images\_response](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#eventsdebug_images_response)\
- [events.debug\_images\_response\_task\_metrics](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#eventsdebug_images_response_task_metrics)\
- [events.event\_type\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#eventsevent_type_enum)\
- [events.log\_level\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#eventslog_level_enum)\
- [events.metric\_variants](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#eventsmetric_variants)\
- [events.metrics\_image\_event](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#eventsmetrics_image_event)\
- [events.metrics\_plot\_event](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#eventsmetrics_plot_event)\
- [events.metrics\_scalar\_event](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#eventsmetrics_scalar_event)\
- [events.metrics\_vector\_event](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#eventsmetrics_vector_event)\
- [events.plot\_sample\_response](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#eventsplot_sample_response)\
- [events.plots\_response](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#eventsplots_response)\
- [events.plots\_response\_task\_metrics](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#eventsplots_response_task_metrics)\
- [events.scalar\_key\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#eventsscalar_key_enum)\
- [events.single\_value\_metrics\_response](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#eventssingle_value_metrics_response)\
- [events.single\_value\_task\_metrics](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#eventssingle_value_task_metrics)\
- [events.task\_log\_event](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#eventstask_log_event)\
- [events.task\_metric](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#eventstask_metric)\
- [events.task\_metric\_variants](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#eventstask_metric_variants)\
- [frames.augmentation](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#framesaugmentation)\
- [frames.dataset\_version](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#framesdataset_version)\
- [frames.dataview](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#framesdataview)\
- [frames.dv\_augmentation](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#framesdv_augmentation)\
- [frames.dv\_augmentation\_set](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#framesdv_augmentation_set)\
- [frames.filter\_by\_roi\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#framesfilter_by_roi_enum)\
- [frames.filter\_label\_rule](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#framesfilter_label_rule)\
- [frames.filter\_rule](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#framesfilter_rule)\
- [frames.flow\_control](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#framesflow_control)\
- [frames.frame](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#framesframe)\
- [frames.frame\_15](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#framesframe_15)\
- [frames.iteration](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#framesiteration)\
- [frames.iteration\_order\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#framesiteration_order_enum)\
- [frames.jump](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#framesjump)\
- [frames.label\_source](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#frameslabel_source)\
- [frames.mapping](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#framesmapping)\
- [frames.mapping\_rule](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#framesmapping_rule)\
- [frames.mask](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#framesmask)\
- [frames.output\_rois\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#framesoutput_rois_enum)\
- [frames.preview](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#framespreview)\
- [frames.roi](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#framesroi)\
- [frames.roi\_mask](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#framesroi_mask)\
- [frames.rule\_count](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#framesrule_count)\
- [frames.similarity\_function](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#framessimilarity_function)\
- [frames.snippet](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#framessnippet)\
- [frames.source](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#framessource)\
- [frames.stat\_count](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#framesstat_count)\
- [frames.view\_entry](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#framesview_entry)\
- [login.assignable\_role](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#loginassignable_role)\
- [login.choose\_company](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#loginchoose_company)\
- [login.login\_status\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#loginlogin_status_enum)\
- [login.login\_white\_list](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#loginlogin_white_list)\
- [login.login\_white\_list\_email\_entry](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#loginlogin_white_list_email_entry)\
- [login.login\_white\_list\_v1\_5](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#loginlogin_white_list_v1_5)\
- [login.role](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#loginrole)\
- [login.signup\_info](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#loginsignup_info)\
- [login.whitelist\_entry](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#loginwhitelist_entry)\
- [models.last\_metrics\_event](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#modelslast_metrics_event)\
- [models.last\_metrics\_variants](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#modelslast_metrics_variants)\
- [models.metadata\_item](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#modelsmetadata_item)\
- [models.model](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#modelsmodel)\
- [models.multi\_field\_pattern\_data](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#modelsmulti_field_pattern_data)\
- [organization.field\_mapping](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#organizationfield_mapping)\
- [organization.invite](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#organizationinvite)\
- [organization.match\_set](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#organizationmatch_set)\
- [organization.match\_spec](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#organizationmatch_spec)\
- [organization.service\_info](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#organizationservice_info)\
- [organization.ui\_action](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#organizationui_action)\
- [organization.user\_details](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#organizationuser_details)\
- [organization.value\_mapping](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#organizationvalue_mapping)\
- [organization.workloads](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#organizationworkloads)\
- [permissions.access\_permission\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#permissionsaccess_permission_enum)\
- [permissions.entity\_type\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#permissionsentity_type_enum)\
- [permissions.user](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#permissionsuser)\
- [projects.metric\_variant\_result](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#projectsmetric_variant_result)\
- [projects.multi\_field\_pattern\_data](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#projectsmulti_field_pattern_data)\
- [projects.project](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#projectsproject)\
- [projects.projects\_get\_all\_response\_single](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#projectsprojects_get_all_response_single)\
- [projects.stats](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#projectsstats)\
- [projects.stats\_datasets](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#projectsstats_datasets)\
- [projects.stats\_status\_count](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#projectsstats_status_count)\
- [projects.urls](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#projectsurls)\
- [queues.entry](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#queuesentry)\
- [queues.metadata\_item](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#queuesmetadata_item)\
- [queues.queue](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#queuesqueue)\
- [queues.queue\_metrics](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#queuesqueue_metrics)\
- [reports.artifact](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reportsartifact)\
- [reports.artifact\_mode\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reportsartifact_mode_enum)\
- [reports.artifact\_type\_data](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reportsartifact_type_data)\
- [reports.augmentation](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reportsaugmentation)\
- [reports.augmentation\_set](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reportsaugmentation_set)\
- [reports.configuration\_item](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reportsconfiguration_item)\
- [reports.debug\_images\_response\_task\_metrics](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reportsdebug_images_response_task_metrics)\
- [reports.execution](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reportsexecution)\
- [reports.filter\_by\_roi\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reportsfilter_by_roi_enum)\
- [reports.filter\_label\_rule](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reportsfilter_label_rule)\
- [reports.filter\_rule](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reportsfilter_rule)\
- [reports.filtering](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reportsfiltering)\
- [reports.input](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reportsinput)\
- [reports.iteration](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reportsiteration)\
- [reports.jump](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reportsjump)\
- [reports.label\_source](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reportslabel_source)\
- [reports.last\_metrics\_event](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reportslast_metrics_event)\
- [reports.last\_metrics\_variants](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reportslast_metrics_variants)\
- [reports.mapping](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reportsmapping)\
- [reports.mapping\_rule](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reportsmapping_rule)\
- [reports.metric\_variants](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reportsmetric_variants)\
- [reports.multi\_field\_pattern\_data](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reportsmulti_field_pattern_data)\
- [reports.output](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reportsoutput)\
- [reports.output\_rois\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reportsoutput_rois_enum)\
- [reports.params\_item](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reportsparams_item)\
- [reports.report](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reportsreport)\
- [reports.report\_status\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reportsreport_status_enum)\
- [reports.scalar\_key\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reportsscalar_key_enum)\
- [reports.script](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reportsscript)\
- [reports.section\_params](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reportssection_params)\
- [reports.similarity\_function](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reportssimilarity_function)\
- [reports.single\_value\_task\_metrics](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reportssingle_value_task_metrics)\
- [reports.task](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reportstask)\
- [reports.task\_model\_item](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reportstask_model_item)\
- [reports.task\_models](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reportstask_models)\
- [reports.task\_status\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reportstask_status_enum)\
- [reports.task\_type\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reportstask_type_enum)\
- [reports.view](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reportsview)\
- [reports.view\_entry](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#reportsview_entry)\
- [resources.task\_status\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#resourcestask_status_enum)\
- [resources.task\_type\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#resourcestask_type_enum)\
- [serving.container\_info](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#servingcontainer_info)\
- [serving.container\_instance\_stats](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#servingcontainer_instance_stats)\
- [serving.endpoint\_stats](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#servingendpoint_stats)\
- [serving.machine\_stats](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#servingmachine_stats)\
- [sso.configuration](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#ssoconfiguration)\
- [sso.provider](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#ssoprovider)\
- [sso.provider\_category](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#ssoprovider_category)\
- [storage.aws](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#storageaws)\
- [storage.aws\_bucket](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#storageaws_bucket)\
- [storage.azure](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#storageazure)\
- [storage.azure\_container](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#storageazure_container)\
- [storage.google](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#storagegoogle)\
- [storage.google\_bucket](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#storagegoogle_bucket)\
- [system.basic\_company\_info](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#systembasic_company_info)\
- [system.company\_defaults](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#systemcompany_defaults)\
- [system.dataset](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#systemdataset)\
- [system.features\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#systemfeatures_enum)\
- [system.match\_set](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#systemmatch_set)\
- [system.match\_spec](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#systemmatch_spec)\
- [system.service\_info](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#systemservice_info)\
- [system.version](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#systemversion)\
- [system.version\_status\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#systemversion_status_enum)\
- [tasks.artifact](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasksartifact)\
- [tasks.artifact\_id](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasksartifact_id)\
- [tasks.artifact\_mode\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasksartifact_mode_enum)\
- [tasks.artifact\_type\_data](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasksartifact_type_data)\
- [tasks.augmentation](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasksaugmentation)\
- [tasks.augmentation\_set](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasksaugmentation_set)\
- [tasks.configuration\_item](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasksconfiguration_item)\
- [tasks.execution](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasksexecution)\
- [tasks.execution\_15](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasksexecution_15)\
- [tasks.filter\_by\_roi\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasksfilter_by_roi_enum)\
- [tasks.filter\_label\_rule](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasksfilter_label_rule)\
- [tasks.filter\_rule](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasksfilter_rule)\
- [tasks.filtering](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasksfiltering)\
- [tasks.input](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasksinput)\
- [tasks.iteration](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasksiteration)\
- [tasks.jump](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasksjump)\
- [tasks.label\_source](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#taskslabel_source)\
- [tasks.last\_metrics\_event](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#taskslast_metrics_event)\
- [tasks.last\_metrics\_variants](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#taskslast_metrics_variants)\
- [tasks.mapping](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasksmapping)\
- [tasks.mapping\_rule](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasksmapping_rule)\
- [tasks.model\_type\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasksmodel_type_enum)\
- [tasks.multi\_field\_pattern\_data](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasksmulti_field_pattern_data)\
- [tasks.output](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasksoutput)\
- [tasks.output\_rois\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasksoutput_rois_enum)\
- [tasks.param\_key](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasksparam_key)\
- [tasks.params\_item](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasksparams_item)\
- [tasks.replace\_hyperparams\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasksreplace_hyperparams_enum)\
- [tasks.script](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasksscript)\
- [tasks.section\_params](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#taskssection_params)\
- [tasks.similarity\_function](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#taskssimilarity_function)\
- [tasks.task](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#taskstask)\
- [tasks.task\_15](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#taskstask_15)\
- [tasks.task\_model\_item](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#taskstask_model_item)\
- [tasks.task\_models](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#taskstask_models)\
- [tasks.task\_status\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#taskstask_status_enum)\
- [tasks.task\_type\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#taskstask_type_enum)\
- [tasks.task\_urls](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#taskstask_urls)\
- [tasks.view](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasksview)\
- [tasks.view\_entry](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tasksview_entry)\
- [tenants.resource\_usage\_series](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#tenantsresource_usage_series)\
- [users.assignable\_role](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#usersassignable_role)\
- [users.features\_enum](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#usersfeatures_enum)\
- [users.get\_current\_user\_response\_user\_object](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#usersget_current_user_response_user_object)\
- [users.get\_current\_user\_response\_user\_object\_v1\_5](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#usersget_current_user_response_user_object_v1_5)\
- [users.get\_current\_user\_response\_user\_object\_v\_2\_2\_0](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#usersget_current_user_response_user_object_v_2_2_0)\
- [users.login\_white\_list\_v1\_5](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#userslogin_white_list_v1_5)\
- [users.role](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#usersrole)\
- [users.terms\_of\_use](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#usersterms_of_use)\
- [users.user](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#usersuser)\
- [users.vault](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#usersvault)\
- [users.vault\_data](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#usersvault_data)\
- [variables.increment\_command](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#variablesincrement_command)\
- [variables.variable](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#variablesvariable)\
- [workers.activity\_series](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#workersactivity_series)\
- [workers.aggregation\_stats](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#workersaggregation_stats)\
- [workers.aggregation\_type](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#workersaggregation_type)\
- [workers.current\_task\_entry](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#workerscurrent_task_entry)\
- [workers.id\_name\_entry](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#workersid_name_entry)\
- [workers.machine\_stats](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#workersmachine_stats)\
- [workers.metric\_resource\_series](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#workersmetric_resource_series)\
- [workers.metric\_stats](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#workersmetric_stats)\
- [workers.metrics\_category](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#workersmetrics_category)\
- [workers.queue\_entry](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#workersqueue_entry)\
- [workers.resource\_usage\_series](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#workersresource_usage_series)\
- [workers.stat\_item](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#workersstat_item)\
- [workers.worker](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#workersworker)\
- [workers.worker\_stats](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#workersworker_stats)\
- [workers.worker\_v1\_5](https://clear.ml/docs/latest/docs/references/enterprise/definitions/#workersworker_v1_5)