---
url: "https://clear.ml/docs/latest/docs/webapp/pipelines/webapp_pipeline_page/"
title: "Pipelines Page | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/webapp/pipelines/webapp_pipeline_page/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

Use the **Pipelines** Page to navigate between and manage pipelines. The page shows execution summaries for all
[ClearML Pipelines](https://clear.ml/docs/latest/docs/pipelines/).

You can view the Pipelines page in Project view ![Project view](https://clear.ml/docs/latest/icons/ico-project-view.svg)
or in List view ![List view](https://clear.ml/docs/latest/icons/ico-flat-view.svg). In List
view, all pipelines are shown side-by-side. In Project view, pipelines are organized according to their projects, and
top-level projects are displayed. Click on a project card to view the project's pipelines.

Click on a pipeline card to navigate to its [Pipeline Runs Table](https://clear.ml/docs/latest/docs/webapp/pipelines/webapp_pipeline_table), where you can view the
pipeline structure, configuration, and outputs of all the pipeline's runs, as well as create new runs.

Filter page contents by specific fields ![Filter](https://clear.ml/docs/latest/icons/ico-filter-off.svg)
or through free form search ![Magnifying glass](https://clear.ml/docs/latest/icons/ico-search.svg):

- My Work - Show only pipelines that you created
- Tags - Choose which tags to filter by from a list of tags used in the pipelines.
  - Filter by multiple tag values using the **ANY** or **ALL** options, which correspond to the logical "AND" and "OR"
    respectively. These options appear on the top of the tag list.
  - Filter by the absence of a tag (logical "NOT") by clicking its checkbox twice. An X will appear in the tag's checkbox.
- User - Filter pipelines by the user who created them.

Free form search queries pipeline name and ID. To search using regex, click the `.*`
icon on the search bar.

![Pipelines page](https://clear.ml/docs/latest/assets/images/webapp_pipeline_page-e63ddbc72add715e86a3d17d6e829d12.png#light-mode-only)![Pipelines page](https://clear.ml/docs/latest/assets/images/webapp_pipeline_page_dark-1218617cbf0e232404e5826576b7b3e3.png#dark-mode-only)

## Project Cards [​](https://clear.ml/docs/latest/docs/webapp/pipelines/webapp_pipeline_page/\#project-cards "Direct link to Project Cards")

In Project view, project cards display a project's summarized pipeline information:

![Pipeline project card](https://clear.ml/docs/latest/assets/images/webapp_pipeline_project_card-f214d66778161662570c779a7ffe4334.png#light-mode-only)![Pipeline project card](https://clear.ml/docs/latest/assets/images/webapp_pipeline_project_card_dark-8772dfa1d5cf6871536e8fead2647dc4.png#dark-mode-only)

Click on a project card to view its pipelines.

## Pipeline Cards [​](https://clear.ml/docs/latest/docs/webapp/pipelines/webapp_pipeline_page/\#pipeline-cards "Direct link to Pipeline Cards")

In List view, the pipeline cards display summarized pipeline information:

![Pipeline card](https://clear.ml/docs/latest/assets/images/webapp_pipeline_card-e233f0dcba73be03f81e09298d7a7a1c.png#light-mode-only)![Pipeline card](https://clear.ml/docs/latest/assets/images/webapp_pipeline_card_dark-95454a2f85d3bb011da4c676b8acecc1.png#dark-mode-only)

- Pipeline name
- Time since the pipeline's most recent run
- Run summary - Number of _Running_/ _Pending_/ _Completed_/ _Failed_ runs
- Tags

### Pipeline Actions [​](https://clear.ml/docs/latest/docs/webapp/pipelines/webapp_pipeline_page/\#pipeline-actions "Direct link to Pipeline Actions")

Click ![Menu](https://clear.ml/docs/latest/icons/ico-bars-menu.svg) on the top right
of a pipeline card to open its context menu and access pipeline actions.

![Project context menu](https://clear.ml/docs/latest/assets/images/webapp_pipeline_context_menu-3c6cef11cb0739d6860ad27234f0bdf4.png#light-mode-only)![Project context menu](https://clear.ml/docs/latest/assets/images/webapp_pipeline_context_menu_dark-61910867e4a35959503eb81f90984478.png#dark-mode-only)

- **Rename** \- Change the pipeline's name
- **Add Tag** \- Add label to the pipeline to help easily classify groups of pipelines.
- **Delete** \- Delete the pipeline: delete all its runs and any models/artifacts produced (a list of remaining artifacts
is returned). To delete a pipeline, all its runs must first be archived.
- **Clone**\- Create a new pipeline based on the pipeline's last run. Add the following details:

  - New Pipeline Details
    - Pipeline name - Name for the new pipeline (required).
    - Initial version - The version number of the first run in the new pipeline
    - Project - ClearML project where the new pipeline will be stored. By default, this is the same project as the original pipeline.
  - Parameters - If the pipeline includes custom parameters, specify their values. The cloned run’s values are pre-filled.
  - Configuration
    - Pipeline controller queue - Queue to which the new pipeline run will be enqueued (make sure an agent is assigned to that queue).

- [Project Cards](https://clear.ml/docs/latest/docs/webapp/pipelines/webapp_pipeline_page/#project-cards)
- [Pipeline Cards](https://clear.ml/docs/latest/docs/webapp/pipelines/webapp_pipeline_page/#pipeline-cards)
  - [Pipeline Actions](https://clear.ml/docs/latest/docs/webapp/pipelines/webapp_pipeline_page/#pipeline-actions)