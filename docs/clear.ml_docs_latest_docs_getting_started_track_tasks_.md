---
url: "https://clear.ml/docs/latest/docs/getting_started/track_tasks/"
title: "Tracking Tasks | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/getting_started/track_tasks/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

Every ClearML [task](https://clear.ml/docs/latest/docs/fundamentals/task) you create can be found in the **All Tasks** table and in its project's
task table.

The task table is a powerful tool for creating dashboards and views of your own projects, your team's projects, or the
entire development.

![Task table](https://clear.ml/docs/latest/assets/images/webapp_experiment_table-a577a6afe399a69e25580ff2e6cd08d8.png#light-mode-only)![Task table](https://clear.ml/docs/latest/assets/images/webapp_experiment_table_dark-febb24408feb51bfc367665fd00c4f55.png#dark-mode-only)

Customize the [task table](https://clear.ml/docs/latest/docs/webapp/webapp_exp_table) to fit your own needs by adding views of parameters, metrics, and tags.
Filter and sort based on various criteria, such as parameters and metrics, making it simple to create custom
views. This allows you to:

- Create a dashboard for a project, presenting the latest model accuracy scores, for immediate insights.
- Create a live leaderboard displaying the best-performing tasks, updated in real time
- Monitor a projects' progress and share it across the organization.

## Creating Leaderboards [​](https://clear.ml/docs/latest/docs/getting_started/track_tasks/\#creating-leaderboards "Direct link to Creating Leaderboards")

To create a leaderboard:

1. Select a project in the ClearML WebApp and go to its task table
2. Customize the column selection. Click "Settings" ![Setting Gear](https://clear.ml/docs/latest/icons/ico-settings.svg)
to view and select columns to display.
3. Filter tasks by name using the search bar to find tasks containing any search term
4. Filter by other categories by clicking "Filter" ![Filter](https://clear.ml/docs/latest/icons/ico-filter-off.svg)
on the relevant column. There are a few types of filters:

   - Value set - Choose which values to include from a list of all values in the column
   - Numerical ranges - Insert minimum and/or maximum value
   - Date ranges - Insert starting and/or ending date and time
   - Tags - Choose which tags to filter by from a list of all tags used in the column.
     - Filter by multiple tag values using the **ANY** or **ALL** options, which correspond to the logical "AND" and "OR" respectively. These
       options appear on the top of the tag list.
     - Filter by the absence of a tag (logical "NOT") by clicking its checkbox twice. An `X` will appear in the tag's checkbox.
5. Enable auto-refresh for real-time monitoring

For more detailed instructions, see the [Tracking Leaderboards Tutorial](https://clear.ml/docs/latest/docs/guides/ui/building_leader_board).

## Sharing Leaderboards [​](https://clear.ml/docs/latest/docs/getting_started/track_tasks/\#sharing-leaderboards "Direct link to Sharing Leaderboards")

Bookmark the URL of your customized leaderboard to save and share your view. The URL contains all parameters and values
for your specific leaderboard view.

- [Creating Leaderboards](https://clear.ml/docs/latest/docs/getting_started/track_tasks/#creating-leaderboards)
- [Sharing Leaderboards](https://clear.ml/docs/latest/docs/getting_started/track_tasks/#sharing-leaderboards)