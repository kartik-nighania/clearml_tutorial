---
url: "https://clear.ml/docs/latest/docs/clearml_sdk/apiclient_sdk/"
title: "APIClient | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/clearml_sdk/apiclient_sdk/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The `APIClient` class provides a Pythonic interface to access ClearML's backend REST API. It is a convenient low-level access tool.
Through an `APIClient` instance, you can access ClearML's REST API services:

- [authentication](https://clear.ml/docs/latest/docs/references/api/login) \- Authentication management, authorization and administration for the entire system
- [debug](https://clear.ml/docs/latest/docs/references/api/debug) \- Debugging utilities
- [projects](https://clear.ml/docs/latest/docs/references/api/projects) \- Support for defining Projects containing tasks, models, datasets, and/or pipelines
- [queues](https://clear.ml/docs/latest/docs/references/api/queues) \- [Queue](https://clear.ml/docs/latest/docs/fundamentals/agents_and_queues) management API
- [workers](https://clear.ml/docs/latest/docs/references/api/workers) \- API for worker machines to report status and retrieve tasks for execution.
- [events](https://clear.ml/docs/latest/docs/references/api/events) \- Event (e.g. metrics, debug samples) reporting and retrieval API
- [models](https://clear.ml/docs/latest/docs/references/api/models) \- Model management API
- [tasks](https://clear.ml/docs/latest/docs/references/api/tasks) \- [Task](https://clear.ml/docs/latest/docs/fundamentals/task) Management API

## Using APIClient [​](https://clear.ml/docs/latest/docs/clearml_sdk/apiclient_sdk/\#using-apiclient "Direct link to Using APIClient")

`APIClient` makes the ClearML Server's REST API endpoints available as Python methods.

To use `APIClient`, create an instance of it then call the method corresponding to the desired REST API endpoint, with
its respective parameters as described in the [REST API reference page](https://clear.ml/docs/latest/docs/references/api/).

For example, the [`POST/ projects.get_all`](https://clear.ml/docs/latest/docs/references/api/projects#post-projectsget_all) call returns all projects
in your workspace. The following code uses APIClient to retrieve a list of all projects whose name starts with "example."

```python
from clearml.backend_api.session.client import APIClient

# Create an instance of APIClient

client = APIClient()

project_list = client.projects.get_all(name="example*")

print(project_list)
```

- [Using APIClient](https://clear.ml/docs/latest/docs/clearml_sdk/apiclient_sdk/#using-apiclient)