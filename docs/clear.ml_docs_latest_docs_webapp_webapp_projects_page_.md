---
url: "https://clear.ml/docs/latest/docs/webapp/webapp_projects_page/"
title: "Projects Page | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/webapp/webapp_projects_page/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

Use the Projects Page for project navigation and management.

Your projects are displayed like folders: click a folder to access its contents. The Projects Page shows the top-level
projects in your workspace. Projects that contain nested subprojects are identified by an extra nested project tab.
An exception is the **All Tasks** folder, which shows all projects' and subprojects' contents in a single, flat
list.

![Projects page](https://clear.ml/docs/latest/assets/images/webapp_project_page-a2bc045522fe7953e4c2bc9c7e42b2de.png#light-mode-only)![Projects page](https://clear.ml/docs/latest/assets/images/webapp_project_page_dark-a061acb5ed74bcf62ab7f640db7ba65f.png#dark-mode-only)

If a project has any subprojects, clicking its folder will open its own project page. Access the projects' top-level
contents (i.e. tasks, models etc.) via the folder with the bracketed (`[ ]`) project name.

If a project does not contain any subprojects, clicking on its folder will open its task table (or [Project Overview](https://clear.ml/docs/latest/docs/webapp/webapp_project_overview)
page when relevant).

Filter page contents by specific fields ![Filter](https://clear.ml/docs/latest/icons/ico-filter-off.svg)
or through free form search ![Magnifying glass](https://clear.ml/docs/latest/icons/ico-search.svg):

- My Work - Show only projects that you created
- Tags - Choose which tags to filter by from a list of tags used in the projects.
  - Filter by multiple tag values using the **ANY** or **ALL** options, which correspond to the logical "AND" and "OR"
    respectively. These options appear on the top of the tag list.
  - Filter by the absence of a tag (logical "NOT") by clicking its checkbox twice. An X will appear in the tag's checkbox.
- User - Filter projects by the user who created them.

Free form search queries project name and ID. To search using regex, click the `.*`
icon on the search bar.

## Project Folders [​](https://clear.ml/docs/latest/docs/webapp/webapp_projects_page/\#project-folders "Direct link to Project Folders")

Project folders display summarized project information:

![Project card](https://clear.ml/docs/latest/assets/images/webapp_project_card-91ce92d1de13696792517cacb62889bb.png#light-mode-only)![Project card](https://clear.ml/docs/latest/assets/images/webapp_project_card_dark-5f7c4d052d8a2028b4f02c7ff29def72.png#dark-mode-only)

- When the project contains subprojects, the folder shows the number of subprojects within the project as an additional
tab. Click the tab to view a list of subprojects, and click on a subproject's name to navigate to it.



![Subproject tab](https://clear.ml/docs/latest/assets/images/webapp_sub_project_card-b8b050f66da25f82cb65678ccaa46941.png#light-mode-only)![Subproject tab](https://clear.ml/docs/latest/assets/images/webapp_sub_project_card_dark-22fcb348e748a416add4d33ce5f1a0c4.png#dark-mode-only)

- When a project's `default_output_destination` is set, the folder displays the ![Info](https://clear.ml/docs/latest/icons/ico-info.svg)
indicator. Hover over the indicator to view the default output destination.


Hidden Projects

By default, ClearML infrastructure projects (i.e. dataset, pipeline, reports, application projects) are not shown in the
projects page. You can enable viewing them in **Settings > Configuration > User Preferences**. When enabled, all infrastructure projects
are labeled with ![Hidden project](https://clear.ml/docs/latest/icons/ico-ghost.svg)

![Hidden project configuration](https://clear.ml/docs/latest/assets/images/settings_hidden_projects-5df1bec1d4595dc2338debd76f2bb97a.png#light-mode-only)![Hidden project configuration](https://clear.ml/docs/latest/assets/images/settings_hidden_projects_dark-27bb3d0904a19682926f32e7e3cc07a5.png#dark-mode-only)

### Project Actions [​](https://clear.ml/docs/latest/docs/webapp/webapp_projects_page/\#project-actions "Direct link to Project Actions")

Click ![Menu](https://clear.ml/docs/latest/icons/ico-bars-menu.svg) on the top right
of a project folder to open its context menu and access the following project actions:

![Project context menu](https://clear.ml/docs/latest/assets/images/webapp_projects_context_menu-fcd98816ccde83470a17211ae5474c1b.png#light-mode-only)![Project context menu](https://clear.ml/docs/latest/assets/images/webapp_projects_context_menu_dark-2f2850332905617dc3fbb553bc0fc6bc.png#dark-mode-only)

- **Project Settings**
  - **General** \- Set the project’s name, project path and default output destination
  - **Scalar View Defaults**\- Configure the default scalar view configuration for tasks and models

    - **Scalar view setting** \- Grouping, X-axis units and plot smoothing (see [Scalar Plot Tools](https://clear.ml/docs/latest/docs/webapp/webapp_exp_track_visual#scalar-plot-tools))
    - **Default scalars** \- Choose which metrics are visible by default when viewing task/model scalars.
  - **Storage Mounts (Enterprise Only)**\- Specify storage configuration the ClearML Agent will apply when running tasks
    in this project. To add a mountpoint:

    1. Click **Add Mountpoint**
    2. Input the following information:
       - Volume - Select storage volume. Available volumes are predefined by administrators.

       - Volume Configuration - Additional configuration can be specified based on the volume template specified by the
         admin, such as the container mount point.

         Click **Available System Variables** in the Project Settings window for built-in variables that can be used in volume configuration.

         ![Mountpoint settings](https://clear.ml/docs/latest/assets/images/webapp_project_setting_mounts-3977fad4e7312df6f0550375f0d82237.png#light-mode-only)![Mountpoint settings](https://clear.ml/docs/latest/assets/images/webapp_project_setting_mounts_dark-af7cde19e7961ab5e5d32abfb528df72.png#dark-mode-only)
- **New Project** \- Create a new project (by default a subproject).
- **Move to** \- Move the project into another project. If the target project does not exist, it is created on-the-fly.
- **Delete** \- Delete the project. To delete a project, all of its contents (i.e. any pipelines/reports/datasets) must
first be archived or removed.

Enterprise Feature

The ClearML Enterprise Server provides a mechanism to define your own custom actions, which will
appear in the context menu. Create a custom action by defining an HTTP request to issue when clicking on the context menu
action. For more information see [Custom UI Context Menu Actions](https://clear.ml/docs/latest/docs/deploying_clearml/clearml_server_config#custom-ui-context-menu-actions).

## Create Projects [​](https://clear.ml/docs/latest/docs/webapp/webapp_projects_page/\#create-projects "Direct link to Create Projects")

To create a project, click the **\+ NEW PROJECT** button in the top right of the page or in a project's context menu,
which will open a **New Project** modal.

![New project modal](https://clear.ml/docs/latest/assets/images/webapp_projects_new_project-c4848a43f5eabb4b411228f23c116c0a.png#light-mode-only)![New project modal](https://clear.ml/docs/latest/assets/images/webapp_projects_new_project_dark-437711071de05c8a810874fb83cee024.png#dark-mode-only)

- Project name
- Create in - Where the project should be created, either as a top-level project (create in `Projects root`) or as a
subproject of another project
- Description
- Default output destination - The storage location where model checkpoints (snapshots) and artifacts will be uploaded
when tasks in this project that do not have an explicit output destination specified are executed

- [Project Folders](https://clear.ml/docs/latest/docs/webapp/webapp_projects_page/#project-folders)
  - [Project Actions](https://clear.ml/docs/latest/docs/webapp/webapp_projects_page/#project-actions)
- [Create Projects](https://clear.ml/docs/latest/docs/webapp/webapp_projects_page/#create-projects)