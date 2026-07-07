---
url: "https://clear.ml/docs/latest/docs/fundamentals/projects/"
title: "Projects | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/fundamentals/projects/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

Projects are contextual containers for [tasks](https://clear.ml/docs/latest/docs/fundamentals/task) and [models](https://clear.ml/docs/latest/docs/fundamentals/models) (as well as [dataviews](https://clear.ml/docs/latest/docs/hyperdatasets/dataviews)
when Hyper-Datasets are enabled), providing a logical structure similar to file system folders.
An often useful method is to categorize components into projects according to models or objectives.
Grouping into projects helps in identifying tasks, models, and dataviews when queried.

Projects can be divided into subprojects (and sub-subprojects, etc.) just like files and subdirectories on a
computer, making organization easier.

Projects contain a textual description field for noting relevant information. The WebApp supports markdown rendering
of the description (see [overview](https://clear.ml/docs/latest/docs/webapp/webapp_project_overview)).

In addition, the project's default output URI can be specified. When new tasks from
the project are executed, the model checkpoints (snapshots) and artifacts are stored in the default output location.

## WebApp [​](https://clear.ml/docs/latest/docs/fundamentals/projects/\#webapp "Direct link to WebApp")

Users can create and modify projects, and see project details in the [WebApp](https://clear.ml/docs/latest/docs/webapp/webapp_home).
A project's description can be edited in its [overview](https://clear.ml/docs/latest/docs/webapp/webapp_project_overview) page. Each project's tasks,
models, and dataviews, can be viewed in the project's [task table](https://clear.ml/docs/latest/docs/webapp/webapp_exp_table),
[model table](https://clear.ml/docs/latest/docs/webapp/webapp_model_table), and [dataview table](https://clear.ml/docs/latest/docs/hyperdatasets/webapp/webapp_dataviews).

## Usage [​](https://clear.ml/docs/latest/docs/fundamentals/projects/\#usage "Direct link to Usage")

### Creating Projects and Subprojects [​](https://clear.ml/docs/latest/docs/fundamentals/projects/\#creating-projects-and-subprojects "Direct link to Creating Projects and Subprojects")

When [initializing a task](https://clear.ml/docs/latest/docs/clearml_sdk/task_sdk#task-creation), its project needs to be specified. If the project entered does not exist, it will be created.
Projects can contain subprojects, just like folders can contain subfolders. Input into the `project_name`
parameter a target project path. The project path should follow the project tree hierarchy, in which the project and
subprojects are slash (`/`) delimited.

For example:

```python
from clearml import Task

Task.init(project_name='main_project/sub_project', task_name='test')
```

Nesting projects works on multiple levels. For example: `project_name=main_project/sub_project/sub_sub_project`.

Projects can also be created using the [`projects.create`](https://clear.ml/docs/latest/docs/references/api/projects#post-projectscreate) REST API call.

### View All Projects in System [​](https://clear.ml/docs/latest/docs/fundamentals/projects/\#view-all-projects-in-system "Direct link to View All Projects in System")

To view all projects in the system, use the [`Task.get_projects()`](https://clear.ml/docs/latest/docs/references/sdk/task#taskget_projects) class method:

```python
project_list = Task.get_projects()
```

This returns a list of projects sorted by last update time.

### More Actions [​](https://clear.ml/docs/latest/docs/fundamentals/projects/\#more-actions "Direct link to More Actions")

For additional ways to work with projects, use the REST API [`projects`](https://clear.ml/docs/latest/docs/references/api/projects) resource. Some
of the available actions include:

- [`projects.create`](https://clear.ml/docs/latest/docs/references/api/projects#post-projectscreate) and [`projects.delete`](https://clear.ml/docs/latest/docs/references/api/projects#post-projectsdelete) \- create and delete projects
- [`projects.get_hyper_parameters`](https://clear.ml/docs/latest/docs/references/api/projects#post-projectsget_hyper_parameters) \- get a list of all hyperparameter sections and names used in a project
- [`projects.merge_projects`](https://clear.ml/docs/latest/docs/references/api/projects#post-projectsmerge) \- merge projects into a single project

See more in the [REST API reference](https://clear.ml/docs/latest/docs/references/api/projects#projects).

- [WebApp](https://clear.ml/docs/latest/docs/fundamentals/projects/#webapp)
- [Usage](https://clear.ml/docs/latest/docs/fundamentals/projects/#usage)
  - [Creating Projects and Subprojects](https://clear.ml/docs/latest/docs/fundamentals/projects/#creating-projects-and-subprojects)
  - [View All Projects in System](https://clear.ml/docs/latest/docs/fundamentals/projects/#view-all-projects-in-system)
  - [More Actions](https://clear.ml/docs/latest/docs/fundamentals/projects/#more-actions)