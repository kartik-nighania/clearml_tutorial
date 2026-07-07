---
url: "https://clear.ml/docs/latest/docs/guides/ide/google_colab/"
title: "ClearML Agent on Google Colab | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/ide/google_colab/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

[Google Colab](https://colab.research.google.com/) is a common development environment for data scientists. It supports a convenient IDE as well as
compute provided by Google.

Users can transform a Google Colab instance into an available resource in ClearML using [ClearML Agent](https://clear.ml/docs/latest/docs/clearml_agent).

This tutorial goes over how to create a ClearML worker node in a Google Colab notebook. Once the worker is up
and running, users can send Tasks to be executed on Google Colab's hardware.

## Prerequisites [​](https://clear.ml/docs/latest/docs/guides/ide/google_colab/\#prerequisites "Direct link to Prerequisites")

- Be signed up for ClearML (or have a server deployed).
- Have a Google account to access Google Colab.

## Steps [​](https://clear.ml/docs/latest/docs/guides/ide/google_colab/\#steps "Direct link to Steps")

1. Open up [this Google Colab notebook](https://colab.research.google.com/github/clearml/clearml/blob/master/examples/clearml_agent/clearml_colab_agent.ipynb).

2. Run the first cell, which installs all the necessary packages:





```text
!pip install git+https://github.com/clearml/clearml

!pip install clearml-agent
```

3. Run the second cell, which exports this environment variable:





```text
! export MPLBACKEND=TkAg
```









This environment variable makes Matplotlib work in headless mode, so it won't output graphs to the screen.

4. Create new credentials. Go to your [**Settings**](https://app.clear.ml/settings/workspace-configuration) page > **WORKSPACE** section.
Under **API Credentials**, click **\+ Create new credentials**, and copy the information that pops up.

5. Set the credentials. In the third cell, enter your own credentials:





```python
from clearml import Task



Task.set_credentials(

        api_host="https://api.clear.ml",

        web_host="https://app.clear.ml",

        files_host="https://files.clear.ml",

        key='<generated_key>',

        secret='<generated_secret>'

)
```

6. In the fourth cell, launch a `clearml-agent` that will listen to the `default` queue:





```text
!clearml-agent daemon --queue default
```









For additional options for running `clearml-agent`, see the [clearml-agent reference](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_ref).

After executing cell 4, the worker appears in the [**Orchestration**](https://clear.ml/docs/latest/docs/webapp/webapp_workers_queues)
page of your server. Clone tasks and enqueue them to your hearts content! The `clearml-agent` will fetch
tasks and execute them using the Google Colab hardware.


- [Prerequisites](https://clear.ml/docs/latest/docs/guides/ide/google_colab/#prerequisites)
- [Steps](https://clear.ml/docs/latest/docs/guides/ide/google_colab/#steps)