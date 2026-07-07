---
url: "https://clear.ml/docs/latest/docs/guides/clearml_agent/reproduce_exp/"
title: "Recreating Task Environments | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/clearml_agent/reproduce_exp/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

How to reproduce an old experiment? -- 🧠 WISDOM NUGGET - YouTube

Tap to unmute

[How to reproduce an old experiment? -- 🧠 WISDOM NUGGET](https://www.youtube.com/watch?v=WTVrchczD34) [ClearML](https://www.youtube.com/channel/UCDYdA4hjckRLRVBrCoKenCQ)

ClearML2.62K subscribers

Sometimes, you may need to recreate your task environment on a different machine, but you haven't committed your
code.

ClearML logs everything needed to reproduce your task and its environment (uncommitted changes, used packages, and
more), making it easy to reproduce your task's execution environment using ClearML.

You can reproduce the execution environment of any task you've run with ClearML on any workload:

1. Go to the task page of the task you want to reproduce in the [ClearML WebApp](https://clear.ml/docs/latest/docs/webapp/webapp_overview)



tip





Use the UI's [filtering and sorting](https://clear.ml/docs/latest/docs/webapp/webapp_exp_table#filtering-columns) to find the best performing tasks.

2. Copy the task's ID

3. Use the ClearML Agent's [`build`](https://clear.ml/docs/latest/docs/clearml_agent/clearml_agent_ref#build) command to rebuild the task's
execution environment. Input the task's ID and the target local folder, where the environment will be created:





```commandline
clearml-agent build --id <task_id> --target <target_folder>
```









After running this command, the target folder will contain that task's original code with uncommitted changes applied,
as well as a complete recreated virtual environment

4. Activate the virtual environment using the activation script. Once done, you'll find all of your environment's packages
already installed in the environment


And that's it! Your task's environment and your code has been reproduced!