---
url: "https://clear.ml/docs/latest/docs/webapp/webapp_model_endpoints/"
title: "Model Endpoints | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/webapp/webapp_model_endpoints/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The Model Endpoint table lists all currently live (active, and being brought up) model endpoints, allowing you to view
endpoint details and monitor status over time. Whenever you deploy a model through the [ClearML Deploy UI applications](https://clear.ml/docs/latest/docs/webapp/applications/apps_overview#deploy),
it will be listed in the table.

View the model endpoints in table view ![Table view](https://clear.ml/docs/latest/icons/ico-table-view.svg)
or in details view ![Details view](https://clear.ml/docs/latest/icons/ico-split-view.svg)
using the buttons on the top left of the page. Use the table view for a comparative view of your endpoints according to
columns of interest. Use the details view to access a selected endpoint's details. Details view can also be accessed by
double-clicking a specific endpoint in the table view to open its details view.

Download the model endpoint table as a CSV file by clicking **Download**![Download](https://clear.ml/docs/latest/icons/ico-download.svg).

## Endpoint Tables [​](https://clear.ml/docs/latest/docs/webapp/webapp_model_endpoints/\#endpoint-tables "Direct link to Endpoint Tables")

Active Endpoints are displayed in the **Active** tab. The table provides the following information:

- Endpoint - Endpoint name
- Model - Model Name
- URL - Endpoint URL
- \# Instances - Number of model instances
- Uptime - Longest duration that any of the model instances has been running
- \# Requests - Total number of requests to the endpoint
- Requests / MIN (avg) - Average request rate in the last minute
- Latency (avg) - Average endpoint response latency

![Active endpoints](https://clear.ml/docs/latest/assets/images/webapp_model_endpoints_active_table-0db2a63a3d683188ee041d0638bd72a4.png#light-mode-only)![Active endpoints](https://clear.ml/docs/latest/assets/images/webapp_model_endpoints_active_table_dark-1aa67a347a42fa5123456eb14172513f.png#dark-mode-only)

The **Loading** tab shows endpoints that are being set up, but are not yet active. The table provides the following
information:

- Instance ID - The model deployment application instance ID
- Model - Model Name
- Uptime - Time since this endpoint has started setting up
- Preprocess artifact - Preprocessing code used for the endpoint
- Input type - Model matrix input type (e.g. uint8, float32, int16, float16)
- Input size - Model matrix input size

![Loading endpoints](https://clear.ml/docs/latest/assets/images/webapp_model_endpoints_loading_table-45f965ed310ac7149fe9d4c1e5132cce.png#light-mode-only)![Loading endpoints](https://clear.ml/docs/latest/assets/images/webapp_model_endpoints_loading_table_dark-57cf651aad665abc7e5e7d14272d7c1a.png#dark-mode-only)

You can apply column filters by clicking ![Filter](https://clear.ml/docs/latest/icons/ico-filter-off.svg),
and sort endpoints by clicking ![Sort order](https://clear.ml/docs/latest/icons/ico-sort-off.svg) on the relevant column.
Use the page's search bar ![Magnifying glass](https://clear.ml/docs/latest/icons/ico-search.svg) to search by endpoint name, ID, and model fields.

## Active Endpoint Details [​](https://clear.ml/docs/latest/docs/webapp/webapp_model_endpoints/\#active-endpoint-details "Direct link to Active Endpoint Details")

Clicking on a model endpoint opens it in detailed view.

### Details [​](https://clear.ml/docs/latest/docs/webapp/webapp_model_endpoints/\#details "Direct link to Details")

The **Details** tab displays the model endpoint information:

- Endpoint Name
- Endpoint URL
- Model name (click to go to ClearML or HuggingFace model page)
- Uptime - Duration of longest running endpoint instance
- Preprocess artifact - Preprocessing code used for the endpoint
- Input type - Model matrix input type (e.g. uint8, float32, int16, float16)
- Input size - Model matrix input size
- Model instances list - Model instances servicing the endpoint. The following information is displayed for each instance:
  - Instance ID - Click instance ID to go to the model endpoint's ClearML Application instance dashboard .
  - Uptime
  - Number of requests - Total count
  - Request rate - Average requests per minute
  - CPU Count
  - GPU Count
  - Latency - Average request latency in the last minute

![Endpoints details](https://clear.ml/docs/latest/assets/images/webapp_model_endpoints_details-8257ad7c8f6fb21560ca37c071fd7643.png#light-mode-only)![Endpoints details](https://clear.ml/docs/latest/assets/images/webapp_model_endpoints_details_dark-e2c128e67b42eda3a2d70f60229703ba.png#dark-mode-only)

### Monitor [​](https://clear.ml/docs/latest/docs/webapp/webapp_model_endpoints/\#monitor "Direct link to Monitor")

The Monitor tab displays the endpoint's operational metrics and resource usage over time graphs:

- Total number of requests
- Average requests/min
- Average latency
- Machine utilization metrics:
  - CPU and GPU Usage
  - Memory Usage
  - Video Memory Usage
  - Network Usage

![Endpoints monitor](https://clear.ml/docs/latest/assets/images/webapp_model_endpoints_monitor-7d3546f94f0a75e0a16771f78f2dc5a9.png#light-mode-only)![Endpoints monitor](https://clear.ml/docs/latest/assets/images/webapp_model_endpoints_monitor_dark-d80b49745b836e6d6b810d476b2f4471.png#dark-mode-only)

The graphs' time span can be controlled through the menu at its top right corner.
Click ![Eye Show](https://clear.ml/docs/latest/icons/ico-show.svg) to control which
plots to display.

For example, to display specific plots, click **HIDE ALL**, and then click ![Eye Show](https://clear.ml/docs/latest/icons/ico-show.svg)
on each plot you want to view.

- [Endpoint Tables](https://clear.ml/docs/latest/docs/webapp/webapp_model_endpoints/#endpoint-tables)
- [Active Endpoint Details](https://clear.ml/docs/latest/docs/webapp/webapp_model_endpoints/#active-endpoint-details)
  - [Details](https://clear.ml/docs/latest/docs/webapp/webapp_model_endpoints/#details)
  - [Monitor](https://clear.ml/docs/latest/docs/webapp/webapp_model_endpoints/#monitor)