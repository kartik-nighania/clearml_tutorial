---
url: "https://clear.ml/docs/latest/docs/webapp/webapp_reports/"
title: "Reports | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/webapp/webapp_reports/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

11 - Reports - YouTube

Tap to unmute

[11 - Reports](https://www.youtube.com/watch?v=D6fCvpmV8eo) [ClearML](https://www.youtube.com/channel/UCDYdA4hjckRLRVBrCoKenCQ)

![thumbnail-image](https://yt3.ggpht.com/ytc/AIdro_kEljxxvNzLP5hB1Bv03O_F-CooCUhLk76T2A-B2sM9_w=s68-c-k-c0x00ffffff-no-rj)

ClearML2.62K subscribers

With ClearML's Reports you can write up notes, task findings, or really anything you want. You can create reports
in any of your ClearML projects.

In addition to its main document, a report also contains a description field, which will appear in the report's card in
the [Reports Page](https://clear.ml/docs/latest/docs/webapp/webapp_reports/#reports-page). Reports are searchable based on their description, so adding a description
can make it easier to find the report later.

Reports are editable Markdown documents, supporting:

- Multi-level headings
- Text formatting: Italics, bold, and strikethrough
- Bulleted and numbered lists
- Tables
- Code blocks
- Text and image hyperlinks
- Embedded images uploaded from your computer
- Embedded ClearML task, model, and [app](https://clear.ml/docs/latest/docs/webapp/applications/apps_overview) content

![Report](https://clear.ml/docs/latest/assets/images/webapp_report-9fab64a47a8e9583194e70b723168290.png#light-mode-only)![Report](https://clear.ml/docs/latest/assets/images/webapp_report_dark-b9c365359a1a593ea11764b7fcd09c25.png#dark-mode-only)

Publishing a report locks it for future editing, so you can preserve its contents. You can also share your reports,
download a PDF copy, or simply copy the MarkDown content and reuse in your editor of choice.

Access ClearML reports through the [Reports Page](https://clear.ml/docs/latest/docs/webapp/webapp_reports/#reports-page).

## Embedding ClearML Visualizations [​](https://clear.ml/docs/latest/docs/webapp/webapp_reports/\#embedding-clearml-visualizations "Direct link to Embedding ClearML Visualizations")

You can embed plots and images from your ClearML objects (tasks, models, and apps) into your reports: scalar
graphs and other plots, and debug samples
from an individual object or from an object comparison page. These visualizations are updated live as the
object(s) updates.

To add a graphic resource:

1. Go to the resource you want to embed in your report (a plot or debug sample from an individual object or
object comparison)

2. Hover over the resource and click ![Generate embed code](https://clear.ml/docs/latest/icons/ico-plotly-embed-code.svg).

![Reports step 2](https://clear.ml/docs/latest/assets/images/reports_step_2-eb2deb6cc439972b4533ccbd5adcc361.png#light-mode-only)![Reports step 2](https://clear.ml/docs/latest/assets/images/reports_step_2_dark-c6fc4d66bce01510de34df7d89d0c96f.png#dark-mode-only)

Click `Embed in ClearML report`. This generates the embed code for accessing the resource, and copies
it to your clipboard.

![Reports step 2a](https://clear.ml/docs/latest/assets/images/reports_step_2a-b07bbe136eb91fa948922510b92e9831.png#light-mode-only)![Reports step 2a](https://clear.ml/docs/latest/assets/images/reports_step_2a_dark-f22619bd1ccd0a3fee1c4b8bbc6363f6.png#dark-mode-only)

3. Return to your report page and paste the code snippet

![Reports step 3](https://clear.ml/docs/latest/assets/images/reports_step_3-0a8198f2d97ad8e006ce51504ea52fec.png#light-mode-only)![Reports step 3](https://clear.ml/docs/latest/assets/images/reports_step_3_dark-62142653e4925bd39a9fc44958969105.png#dark-mode-only)


Once embedded in the report, you can return to the resource's original location (e.g. comparison page, task/model/app page)
by clicking ![Return to resource](https://clear.ml/docs/latest/icons/ico-resource-return.svg).

### Customizing Embed Code [​](https://clear.ml/docs/latest/docs/webapp/webapp_reports/\#customizing-embed-code "Direct link to Customizing Embed Code")

You can customize embed codes to make more elaborate queries for what you want to display in your reports.
A standard embed code is formatted like this:

```text
<iframe

  src="<web_server>/widgets/?type=sample&objectType=task&objects=<object_id>&xaxis=iter&metrics=<metric_name>&variants=Plot%20as%20an%20image&company=<company/workspace_id>"

  width="100%" height="400"

></iframe>
```

The `src` parameter is made up of the following components:

- Your web server's URL (e.g. `app.clear.ml`)
- `/widget/` \- The endpoint that serves the embedded data.
- The query parameters for your visualization (the path and query are separated by a question mark `?`)

The query is formatted like a standard query string: `<parameter>=<parameter_value>`. Multiple parameter-value pairs are
delimited with a `&`: `<parameter_1>=<parameter_value_1>&<parameter_2>=<parameter_value_2>`.

The query string usually includes the following parameters:

- `objectType` \- The type of object to fetch. The options are `task` or `model` (`task` also includes ClearML app instances).
- `objects` \- Object IDs (i.e. task or model IDs depending on specified ObjectType). Specify multiple IDs like this:
`objects=<id>&objects=<id>&objects=<id>`. Alternatively, you can input a query, and the matching objects' specified
resources will be displayed. See [Dynamic Queries](https://clear.ml/docs/latest/docs/webapp/webapp_reports/#dynamic-queries) below.
- `type`\- The type of resource to fetch. The options are:

  - `plot`
  - `scalar`
  - `single` (single-scalar values table)
  - `sample` (debug sample)
  - `parcoords`(hyperparameter comparison plots) - for this option, you need to also specify the following parameters:

    - `metrics` \- Unique metric/variant ID formatted like `metric_id.variant_id` (see note [below](https://clear.ml/docs/latest/docs/webapp/webapp_reports/#event_id))
    - `variants` \- Parameters to include in the plot (write in following format `<section_name>.<parameter_1>&<section_name>.<parameter_2>`)
    - `value_type`\- Specify which metric values to use. The options are:

      - `min_value`
      - `max_value`
      - `value` (last value)
- `xaxis`\- Set the x-axis units for plots. The options are:

  - `iter` \- Iteration (default)
  - `timestamp` \- Time from start
  - `iso_time` \- Wall time
- `metrics` \- Metric name
- `variants` \- Variant's name
- `company` \- Workspace ID. Applicable to the ClearML hosted service, for embedding content from a different workspace
- `light` \- add parameter to switch visualization to light theme

URL encoding

For strings, make sure to use the appropriate URL encoding. For example, if the metric name is "Metric Name",
write `Metric%20Name`

### Dynamic Queries [​](https://clear.ml/docs/latest/docs/webapp/webapp_reports/\#dynamic-queries "Direct link to Dynamic Queries")

You can create more complex queries by specifying object criteria (e.g. tags, statuses, projects, etc.) instead of
specific task IDs, with parameters from the [`tasks.get_all`](https://clear.ml/docs/latest/docs/references/api/tasks#post-tasksget_all) or
[`models.get_all`](https://clear.ml/docs/latest/docs/references/api/models#post-modelsget_all) API calls.

For these parameters, use the following syntax:

- `key=value` for non-array fields
- `key[]=<value1>,<value2>` for array fields.

Delimit the fields with `&`s.

#### Examples: [​](https://clear.ml/docs/latest/docs/webapp/webapp_reports/\#examples "Direct link to Examples:")

The following are examples of dynamic queries. All the examples use `objectType=task`, but `objectType=model` can also be
used.

- Request the scalars plot of a specific metric variant for the latest task in a project:





```text
src="<web_server>/widgets/?objectType=task&xaxis=iter&type=scalar&metrics=<metric_name>&variants=<variant>&project=<project_id>&page_size=1&page=0&order_by[]=-last_update
```









Notice that the `project` parameter is specified. To get the most recent single task,
`page_size=1&page=0&order_by[]=-last_update` is added. `page_size` specifies how many results are returned in each
page, and `page` specifies which page to return (in this case the first page)--this way you can specify how many
tasks you want in your graph. `order_by[]=-last_update` orders the results by update time in descending order
(most recent first).

- Request the scalars plot of a specific metric variant for the tasks with a specific tag:





```text
src="<web_server>/widgets/?objectType=task&xaxis=iter&type=scalar&metrics=<metric_name>&variants=<variant>&tags[]=__$or,<tag>
```









A list of tags that the task should contain is specified in the `tags` argument. You can also specify tags that
exclude tasks. See tag filter syntax examples [here](https://clear.ml/docs/latest/docs/clearml_sdk/task_sdk#tag-filters).

- Request the `training/accuracy` scalar plot of the 5 tasks with the best accuracy scores (see Metric/Variant IDs note [below](https://clear.ml/docs/latest/docs/webapp/webapp_reports/#event_id)):





```text
src="<web_server>/widgets/?objectType=task&xaxis=iter&type=scalar&metrics=training&variants=accuracy&project=4043a1657f374e9298649c6ba72ad233&page_size=5&page=0&order_by[]=-last_metrics.<metric_id>.<variant_id>.value"
```


Metric/Variant IDs

Metric names need to be MD5 encoded for parallel coordinate plots and for ordering query results by metric
performance. You can encode the strings in Python with `hashlib.md5(str("<metric_string>").encode("utf-8")).hexdigest()`,
and use the returned MD5 hash in your query.

## Reports Page [​](https://clear.ml/docs/latest/docs/webapp/webapp_reports/\#reports-page "Direct link to Reports Page")

Use the Reports Page to navigate between and manage reports.

You can view the reports page in Project view ![Project view](https://clear.ml/docs/latest/icons/ico-project-view.svg)
or in List view ![List view](https://clear.ml/docs/latest/icons/ico-flat-view.svg). In List
view, all reports are shown side-by-side. In Project view, reports are organized according to their projects, and
top-level projects are displayed. Click on a project card to view the project's reports.

Filter page contents by specific fields ![Filter](https://clear.ml/docs/latest/icons/ico-filter-off.svg)
or through free form search ![Magnifying glass](https://clear.ml/docs/latest/icons/ico-search.svg).

Field filters support:

- My Work - Show only reports that you created
- Tags - Choose which tags to filter by from a list of tags used in the reports.
  - Filter by multiple tag values using the **ANY** or **ALL** options, which correspond to the logical "AND" and "OR"
    respectively. These options appear on the top of the tag list.
  - Filter by the absence of a tag (logical "NOT") by clicking its checkbox twice. An X will appear in the tag's checkbox.
- User – Filter reports by the user who created them.
- Status (available in List view only) – Filter reports by their status (Published or Draft).

Free form search queries report name, ID, tags, project, description, and report content.
To search using regex, click the `.*` icon on the search bar.

![Report page](https://clear.ml/docs/latest/assets/images/webapp_report_page-b3134eade5afac2233230d2406f5d061.png#light-mode-only)![Report page](https://clear.ml/docs/latest/assets/images/webapp_report_page_dark-02d4130b77548c8a9db2d3d78e1ce9c1.png#dark-mode-only)

## Project Cards [​](https://clear.ml/docs/latest/docs/webapp/webapp_reports/\#project-cards "Direct link to Project Cards")

In Project view, project cards display a project's summarized report information:

![Report project card](https://clear.ml/docs/latest/assets/images/webapp_report_project_card-613acf6d222dc57f608fd488320bdf69.png#light-mode-only)![Report project card](https://clear.ml/docs/latest/assets/images/webapp_report_project_card_dark-8f5b3230a965c62d896bf7b0fe4ed350.png#dark-mode-only)

Click on a project card to view its reports.

### Report Cards [​](https://clear.ml/docs/latest/docs/webapp/webapp_reports/\#report-cards "Direct link to Report Cards")

In List view, the report cards display summarized report information:

![report card](https://clear.ml/docs/latest/assets/images/webapp_report_card-0feb337ab89d99f5e0848acffb6f554a.png#light-mode-only)![report card](https://clear.ml/docs/latest/assets/images/webapp_report_card_dark-582cbdeadfd7f543904b0e2e9f035caf.png#dark-mode-only)

- Report name
- Report's project
- Creating user
- Last update time
- Status
- Description
- Tags

#### Report Actions [​](https://clear.ml/docs/latest/docs/webapp/webapp_reports/\#report-actions "Direct link to Report Actions")

Click ![Menu](https://clear.ml/docs/latest/icons/ico-bars-menu.svg) on the top right
of a report card to open its context menu and access report actions:

![Report card context menu](https://clear.ml/docs/latest/assets/images/webapp_report_card_context_menu-4ce971cf28ed1470f002d5eaa75be2ab.png#light-mode-only)![Report card context menu](https://clear.ml/docs/latest/assets/images/webapp_report_card_context_menu_dark-d4e973c8b37003d24ac9e373358283fa.png#dark-mode-only)

- **Rename** \- Change the report's name
- **Share** \- Copy URL to share report
- **Add Tag** \- Add labels to the report to help easily classify groups of reports.
- **Move to** \- Move the report into another project. If the target project does not exist, it is created on-the-fly.
- **Archive** \- Move report from active reports page to archive
- **Delete** \- Delete the report. To delete a report, it must first be archived.

### Create Reports [​](https://clear.ml/docs/latest/docs/webapp/webapp_reports/\#create-reports "Direct link to Create Reports")

To create a report, click the **\+ NEW REPORT** button in the top right of the page,
which will open a **New Report** modal.

![New project modal](https://clear.ml/docs/latest/assets/images/webapp_report_new_report-1f1be0eb00664e6423a07ebfda6d5b30.png#light-mode-only)![New project modal](https://clear.ml/docs/latest/assets/images/webapp_report_new_report_dark-63e948dc8493d9d6cd430777f47a322d.png#dark-mode-only)

## MarkDown Formatting Quick Guide [​](https://clear.ml/docs/latest/docs/webapp/webapp_reports/\#markdown-formatting-quick-guide "Direct link to MarkDown Formatting Quick Guide")

The following is a quick reference for the MarkDown syntax that can be used in ClearML Reports.

### Heading Levels [​](https://clear.ml/docs/latest/docs/webapp/webapp_reports/\#heading-levels "Direct link to Heading Levels")

To create headings, add `#` in front of the phrases that you want to turn into
headings. The number of `#` signs correspond to the heading level (i.e. `#` for level-1 heading, `##` for level-2, etc.):

| MarkDown | Rendered Output |
| --- | --- |
| `# H1`<br>`## H2`<br>`### H3`<br>`#### H4`<br>`##### H5`<br>`###### H6` | ![Report headings](<Base64-Image-Removed>)![Report headings](<Base64-Image-Removed>) |

### Text Emphasis [​](https://clear.ml/docs/latest/docs/webapp/webapp_reports/\#text-emphasis "Direct link to Text Emphasis")

The following table presents the text format options:

| Format Option | MarkDown | Rendered Output |
| --- | --- | --- |
| Bold | \*\*This is bold text\*\* and \_\_so is this\_\_ | **This is bold text** and **so is this** |
| Italics | \*This is italic text\* and \_so is this\_ | _This is italic text_ and _so is this_ |
| Strikethrough | ~~Strikethrough~~ | ~~Strikethrough~~ |
| Inline Code | \`this is code\` | `this is code` |

### Blockquotes [​](https://clear.ml/docs/latest/docs/webapp/webapp_reports/\#blockquotes "Direct link to Blockquotes")

To create a blockquote, add a `>` before each line of the quote. Nest blockquotes by adding additional
`>` signs before each line of the nested blockquote.

| MarkDown | Rendered Output |
| --- | --- |
| ```<br>> Blockquote<br>>> Nested quote 1<br>>>> Nested quote 2<br>``` | ![Report Blockquotes](<Base64-Image-Removed>)![Report Blockquotes](<Base64-Image-Removed>) |

### Lists [​](https://clear.ml/docs/latest/docs/webapp/webapp_reports/\#lists "Direct link to Lists")

#### Ordered List [​](https://clear.ml/docs/latest/docs/webapp/webapp_reports/\#ordered-list "Direct link to Ordered List")

Create an ordered list by numbering the list items with numbers followed by periods. The list items do not have to be numbered
correctly, but the list will be rendered numerically starting with `1.`.

| MarkDown | Rendered Output |
| --- | --- |
| ```<br>1. Item 1<br>2. Item 2<br>1. Item 3<br>1. Item 4<br>``` | ![Report ordered list](<Base64-Image-Removed>)![Report ordered list](<Base64-Image-Removed>) |

#### Unordered List [​](https://clear.ml/docs/latest/docs/webapp/webapp_reports/\#unordered-list "Direct link to Unordered List")

Create an unordered list by starting each line with the `+`, `-`, or `*` signs. Different
signs can be used to create the bullets in the same list, but they are all rendered uniformly.

You can also use checkmarks (`* [x]`), following any of the bullet signs.

To nest lists, indent nested items 2 spaces more than their parent list item.

| MarkDown | Rendered Output |
| --- | --- |
| ```<br>+ Item 1<br>+ Item 2<br>  - Sub-item a:<br>    * Sub-sub-item x<br>    + Sub-sub-item y<br>    - Sub-sub-item z<br>* [x] A checkmark <br>``` | ![Report unordered list](<Base64-Image-Removed>)![Report unordered list](<Base64-Image-Removed>) |

### Tables [​](https://clear.ml/docs/latest/docs/webapp/webapp_reports/\#tables "Direct link to Tables")

MarkDown code for a table looks like this:

```markdown
|          | Align Right | Align Left | Align Center |

| -------- | -----------:|:---------- |:------------:|

| 1        |           1 | 1          |      1       |

| 11       |          11 | 11         |      11      |
```

The rendered output should look like this:

![Report table](<Base64-Image-Removed>)![Report table](<Base64-Image-Removed>)

Add the table column names in the first row; each name is preceded and followed by a pipe (`|`).
In the second row, add sets of at least three hyphens (`---`) for each column, and add a pipe before and after each set
of hyphens. In the second row, you can specify each table column's contents alignment. To align the contents to the
left, place a colon (`:`) to the left of the hyphens. To align right, place a colon to the right of the hyphens. To
center align, place colons on both sides of the hyphens.

### Code [​](https://clear.ml/docs/latest/docs/webapp/webapp_reports/\#code "Direct link to Code")

To render inline code, surround the code with single backticks (`````). For example \`code\` will be rendered `code`.

To create block code, use one of the following options:

- Indent the code





```text
      from clearml import Task



      t = Task.init(project_name='My project', task_name='Base')
```

- Surround code with "fences"--three backticks (`````````):





````text
```

from clearml import Task



t = Task.init(project_name='My project', task_name='Base')

```
````


Both of these options will be rendered as:

```text
from clearml import Task

t = Task.init(project_name='My project', task_name='Base')
```

#### Syntax Highlighting [​](https://clear.ml/docs/latest/docs/webapp/webapp_reports/\#syntax-highlighting "Direct link to Syntax Highlighting")

To display syntax highlighting, specify the coding language after the first fence (e.g. ``````python```, ``````json```, ``````js```, etc.):

````text
```python

from clearml import Task

t = Task.init(project_name='My project', task_name='Base')

```
````

The rendered output should look like this:

```py
from clearml import Task

t = Task.init(project_name='My project', task_name='Base')
```

### Links [​](https://clear.ml/docs/latest/docs/webapp/webapp_reports/\#links "Direct link to Links")

To create a link, enclose link text inside brackets, followed by the URL link enclosed in parentheses:

```text
[link text](https://clear.ml)
```

The rendered output should look like this:
[link text](https://clear.ml/)

To add a title to the link, which you can see in a tooltip when hovering over the link, add the title after the URL
link in the parentheses:

```text
[link with title](https://clear.ml "ClearML Documentation")
```

The rendered output should look like this: [link with title](https://clear.ml/ "ClearML Documentation"). Hover over the
link to see the link's title.

### Collapsible Sections [​](https://clear.ml/docs/latest/docs/webapp/webapp_reports/\#collapsible-sections "Direct link to Collapsible Sections")

The MarkDown code for a collapsible panel looks like this:

```text
<details><summary>Section title</summary>Collapsible Section Contents</details>
```

The collapsible panel is surrounded by `<details>` tags. Within the `<details>` tag, add the section's title between
the `<summary>` tags. This title can be seen when the panel is collapsed. After the `</summary>` tag, add the panel
contents.

It is rendered like this:

Section title

Collapsible Section Contents

### Horizontal Rules [​](https://clear.ml/docs/latest/docs/webapp/webapp_reports/\#horizontal-rules "Direct link to Horizontal Rules")

Create horizontal lines using three hyphens (`---`), underscores (`___`), or asterisks (`***`):

| MarkDown | Rendered Output |
| --- | --- |
| ```<br>---<br>___<br>***<br>``` | ![Reports horizontal rules](<Base64-Image-Removed>)![Reports horizontal rules](<Base64-Image-Removed>) |

### Images [​](https://clear.ml/docs/latest/docs/webapp/webapp_reports/\#images "Direct link to Images")

To add an image, add an exclamation point, followed by the alt text enclosed by brackets, followed by the link to the
image enclosed in parentheses:

```text
![Logo](https://raw.githubusercontent.com/clearml/clearml/master/docs/clearml-logo.svg)
```

The rendered output should look like this:

![Logo](https://raw.githubusercontent.com/clearml/clearml/master/docs/clearml-logo.svg)![Logo](https://raw.githubusercontent.com/clearml/clearml/master/docs/clearml-logo-dark.svg)

To add a title to the image, which you can see in a tooltip when hovering over the image, add the title after the image's
link:

```text
![With title](https://raw.githubusercontent.com/clearml/clearml/master/docs/clearml-logo.svg "ClearML logo")
```

The rendered output should look like this:

![](https://raw.githubusercontent.com/clearml/clearml/master/docs/clearml-logo.svg)![](https://raw.githubusercontent.com/clearml/clearml/master/docs/clearml-logo-dark.svg)

Hover over the image to see its title.

- [Embedding ClearML Visualizations](https://clear.ml/docs/latest/docs/webapp/webapp_reports/#embedding-clearml-visualizations)
  - [Customizing Embed Code](https://clear.ml/docs/latest/docs/webapp/webapp_reports/#customizing-embed-code)
  - [Dynamic Queries](https://clear.ml/docs/latest/docs/webapp/webapp_reports/#dynamic-queries)
- [Reports Page](https://clear.ml/docs/latest/docs/webapp/webapp_reports/#reports-page)
- [Project Cards](https://clear.ml/docs/latest/docs/webapp/webapp_reports/#project-cards)
  - [Report Cards](https://clear.ml/docs/latest/docs/webapp/webapp_reports/#report-cards)
  - [Create Reports](https://clear.ml/docs/latest/docs/webapp/webapp_reports/#create-reports)
- [MarkDown Formatting Quick Guide](https://clear.ml/docs/latest/docs/webapp/webapp_reports/#markdown-formatting-quick-guide)
  - [Heading Levels](https://clear.ml/docs/latest/docs/webapp/webapp_reports/#heading-levels)
  - [Text Emphasis](https://clear.ml/docs/latest/docs/webapp/webapp_reports/#text-emphasis)
  - [Blockquotes](https://clear.ml/docs/latest/docs/webapp/webapp_reports/#blockquotes)
  - [Lists](https://clear.ml/docs/latest/docs/webapp/webapp_reports/#lists)
  - [Tables](https://clear.ml/docs/latest/docs/webapp/webapp_reports/#tables)
  - [Code](https://clear.ml/docs/latest/docs/webapp/webapp_reports/#code)
  - [Links](https://clear.ml/docs/latest/docs/webapp/webapp_reports/#links)
  - [Collapsible Sections](https://clear.ml/docs/latest/docs/webapp/webapp_reports/#collapsible-sections)
  - [Horizontal Rules](https://clear.ml/docs/latest/docs/webapp/webapp_reports/#horizontal-rules)
  - [Images](https://clear.ml/docs/latest/docs/webapp/webapp_reports/#images)