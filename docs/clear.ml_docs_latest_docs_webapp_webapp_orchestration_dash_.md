---
url: "https://clear.ml/docs/latest/docs/webapp/webapp_orchestration_dash/"
title: "Orchestration Dashboard | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/webapp/webapp_orchestration_dash/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

Enterprise Feature

The Orchestration Dashboard is available under the ClearML Enterprise plan.

Use the orchestration dashboard to monitor all of your available and in-use compute resources:

- Available and utilized resources global total and by category
- Resource utilization over time
- Resource history event log
- Detailed resource performance metrics

![Orchestration Dashboard](https://clear.ml/docs/latest/assets/images/webapp_orchestration_dash-0a5fcd8979c4b40a8c5198c3dd758f20.png#light-mode-only)![Orchestration Dashboard](https://clear.ml/docs/latest/assets/images/webapp_orchestration_dash_dark-6cef55ce2fa8bdae103b5c7948898f12.png#dark-mode-only)

## Resource Categories and Groups [​](https://clear.ml/docs/latest/docs/webapp/webapp_orchestration_dash/\#resource-categories-and-groups "Direct link to Resource Categories and Groups")

The orchestration dashboard shows your workers by groups and categories, specified by the following naming
policy: `<category>:<group>:<name>`.

When no category is specified, workers are assigned the `DEFAULT` category.

When no group is specified, workers are assigned the `Default Group` group.

## Current Usage Data [​](https://clear.ml/docs/latest/docs/webapp/webapp_orchestration_dash/\#current-usage-data "Direct link to Current Usage Data")

The top of the dashboard displays the current resource availability and utilization counts. This gives you an overall
picture of the resources available and in use. The **Total** section displays available and idle resource counts.
These counts are also available per worker category.

The **Total** section displays:

- GPUs - The total number of GPUs in currently running workers out of the total number of GPUs in all provisioned workers, and the number of idle GPUs. GPUs are considered idle when their average
utilization falls below 80%.
- CPUs - The total number of CPUs in currently running workers out of the total number of CPUs in all provisioned workers, and the number of idle CPUs. CPUs are considered idle when their average
utilization falls below 30%.
- Workers - The number of currently running workers out of the total number of provisioned workers (through autoscalers or K8s), and the number of idle
workers. Workers are considered idle if all of their GPUs and CPUs are idle or if they are not executing any task.

Category sections display the resource count and utilization for:

- Workers
- GPUs
- CPUs

Hover over any of this data to see the number of currently idle machines.

Use the **Event Log** to view updates of worker events: worker addition/removal, worker has become idle/busy. Hover over
the log to download (![Download](https://clear.ml/docs/latest/icons/ico-download.svg))
it or open the expanded view (![Maximize](https://clear.ml/docs/latest/icons/ico-maximize.svg)).

## Resource Graph [​](https://clear.ml/docs/latest/docs/webapp/webapp_orchestration_dash/\#resource-graph "Direct link to Resource Graph")

The Resource graph displays resource usage over time. The graph time span can be controlled through the dropdown menu
above the graph (between 3 hours and 1 month). Hover over the plot to see specific data point values.

Click on a group in the **Resource Groups** list below the graph to have the graph display usage for that specific group.

When viewing a group's usage, you can select what data to view in the dropdown menu at the top of the plot:

- Compute Units - Available/Idle CPUs/GPUs
- Compute Utilization - Average CPU/GPU utilization
- Available Memory - Total and Free RAM
- Free Home Storage
- Network Throughput - Rx/Tx

## Resource Groups [​](https://clear.ml/docs/latest/docs/webapp/webapp_orchestration_dash/\#resource-groups "Direct link to Resource Groups")

The **Resource Groups** table displays current usage numbers for each group:

- Worker count - number of workers in the group
- GPU count
- Average GPU Utilization (%)
- Average CPU Load (%)
- Available (total) RAM (GB)
- Free RAM (GB)
- Free home disk (GB)
- Network (Tx/Rx Mbps)

Click ![Expand](https://clear.ml/docs/latest/icons/ico-chevron-right.svg) to expand the resource
group and view the stats of each worker within the group. Filters can be applied by
clicking ![Filter](https://clear.ml/docs/latest/icons/ico-filter-off.svg) on a column, and the
relevant filter appears. To clear all active filters, click ![Clear filters](https://clear.ml/docs/latest/icons/ico-filter-reset.svg).

Hover over a worker and click ![Dot menu](https://clear.ml/docs/latest/icons/ico-dots-v-menu.svg)
to access the worker's information panel.

The table highlights values that cross user configured thresholds.

![Resource groups](https://clear.ml/docs/latest/assets/images/webapp_orch_dash_resource_groups-de62de850a67753409ff87cc68094cfb.png#light-mode-only)![Resource groups](https://clear.ml/docs/latest/assets/images/webapp_orch_dash_resource_groups_dark-166efacdd4712f8a3a77f3baa64505f3.png#dark-mode-only)

Click ![Tune](https://clear.ml/docs/latest/icons/ico-tune.svg) to define the threshold values.

note

The threshold values applied to the dashboard table affect all workspace users who view the page

![Threshold modal](https://clear.ml/docs/latest/assets/images/webapp_orch_dash_threshold_modal-3627f3c21792348437364a714dd09af7.png#light-mode-only)![Threshold modal](https://clear.ml/docs/latest/assets/images/webapp_orch_dash_threshold_modal_dark-685622a0b98fb1f34d343d157b949f45.png#dark-mode-only)

Clicking on a resource group opens the group's info panel and replaces the **Overview** graph with that resource's usage
history.

![Resource group info panel](https://clear.ml/docs/latest/assets/images/webapp_orch_dash_resource_group_info-35afbf926d0202574b359b01a526b952.png#light-mode-only)![Resource group info panel](https://clear.ml/docs/latest/assets/images/webapp_orch_dash_resource_group_info_dark-4d2b1a23a65de6f5036a941b3662086a.png#dark-mode-only)

The info panel displays the group's:

- Total GPU count
- Total CPU count
- Total Worker RAM
- Total GPU RAM
- Aggregate Idle time in last 30 days

- [Resource Categories and Groups](https://clear.ml/docs/latest/docs/webapp/webapp_orchestration_dash/#resource-categories-and-groups)
- [Current Usage Data](https://clear.ml/docs/latest/docs/webapp/webapp_orchestration_dash/#current-usage-data)
- [Resource Graph](https://clear.ml/docs/latest/docs/webapp/webapp_orchestration_dash/#resource-graph)
- [Resource Groups](https://clear.ml/docs/latest/docs/webapp/webapp_orchestration_dash/#resource-groups)