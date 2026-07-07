---
url: "https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/"
title: "PipelineController | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

## _class_ PipelineController(name, project, version=None, pool\_frequency=0.2, add\_pipeline\_tags=False, target\_project=True, auto\_version\_bump=None, abort\_on\_failure=False, add\_run\_number=True, retry\_on\_failure=None, docker=None, docker\_args=None, docker\_bash\_setup\_script=None, packages=None, repo=None, repo\_branch=None, repo\_commit=None, always\_create\_from\_code=True, artifact\_serialization\_function=None, artifact\_deserialization\_function=None, output\_uri=None, skip\_global\_imports=False, working\_dir=None, enable\_local\_imports=True) [​](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/\#class-pipelinecontrollername-project-versionnone-pool_frequency02-add_pipeline_tagsfalse-target_projecttrue-auto_version_bumpnone-abort_on_failurefalse-add_run_numbertrue-retry_on_failurenone-dockernone-docker_argsnone-docker_bash_setup_scriptnone-packagesnone-reponone-repo_branchnone-repo_commitnone-always_create_from_codetrue-artifact_serialization_functionnone-artifact_deserialization_functionnone-output_urinone-skip_global_importsfalse-working_dirnone-enable_local_importstrue "Direct link to class-pipelinecontrollername-project-versionnone-pool_frequency02-add_pipeline_tagsfalse-target_projecttrue-auto_version_bumpnone-abort_on_failurefalse-add_run_numbertrue-retry_on_failurenone-dockernone-docker_argsnone-docker_bash_setup_scriptnone-packagesnone-reponone-repo_branchnone-repo_commitnone-always_create_from_codetrue-artifact_serialization_functionnone-artifact_deserialization_functionnone-output_urinone-skip_global_importsfalse-working_dirnone-enable_local_importstrue")

Pipeline controller.
Pipeline is a DAG of base tasks, each task will be cloned (arguments changed as required), executed, and monitored.
The pipeline process (task) itself can be executed manually or by the clearml-agent services queue.
Notice: The pipeline controller lives as long as the pipeline itself is being executed.

Create a new pipeline controller. The newly created object will launch and monitor the new experiments.

- **Parameters**


  - **name** (`str`) – Provide pipeline name (if main Task exists it overrides its name)

  - **project** (`str`) – Provide project storing the pipeline (if main Task exists it overrides its project)

  - **version** (`Optional`\[`str`\]) – Pipeline version. This version allows to uniquely identify the pipeline
    template execution. Examples for semantic versions: version=’1.0.1’ , version=’23’, version=’1.2’.
    If not set, find the latest version of the pipeline and increment it. If no such version is found,
    default to ‘1.0.0’

  - **pool\_frequency** ( _float_ ) – The pooling frequency (in minutes) for monitoring experiments / states.

  - **add\_pipeline\_tags** ( _bool_ ) – (default: False) if True, add pipe: <pipeline\_task\_id> tag to all
    steps (Tasks) created by this pipeline.

  - **target\_project** ( _str_ ) – If provided, all pipeline steps are cloned into the target project.
    If True, pipeline steps are stored into the pipeline project

  - **auto\_version\_bump** ( _bool_ ) – (Deprecated) If True, if the same pipeline version already exists
    (with any difference from the current one), the current pipeline version will be bumped to a new version
    version bump examples: 1.0.0 -> 1.0.1 , 1.2 -> 1.3, 10 -> 11 etc.

  - **abort\_on\_failure** ( _bool_ ) – If False (default), failed pipeline steps will not cause the pipeline
    to stop immediately, instead any step that is not connected (or indirectly connected) to the failed step,
    will still be executed. Nonetheless the pipeline itself will be marked failed, unless the failed step
    was specifically defined with “continue\_on\_fail=True”.
    If True, any failed step will cause the pipeline to immediately abort, stop all running steps,
    and mark the pipeline as failed.

  - **add\_run\_number** (`bool`) – If True (default), add the run number of the pipeline to the pipeline name.
    Example, the second time we launch the pipeline “best pipeline”, we rename it to “best pipeline #2”

  - **retry\_on\_failure** (`Union`\[`int`, `Callable`\[\[`PipelineController`, `Node`, `int`\], `bool`\], `None`\]) – Integer (number of retries) or Callback function that returns True to allow a retry
    - Integer: In case of node failure, retry the node the number of times indicated by this parameter.

    - Callable: A function called on node failure. Takes as parameters:
      the PipelineController instance, the PipelineController.Node that failed and an int
      representing the number of previous retries for the node that failed.
      The function must return `True` if the node should be retried and `False` otherwise.
      If True, the node will be re-queued and the number of retries left will be decremented by 1.
      By default, if this callback is not specified, the function will be retried the number of
      times indicated by retry\_on\_failure.

```py
def example_retry_on_failure_callback(pipeline, node, retries):

    print(f"{node.name} failed")

    # allow up to 5 retries (total of 6 runs)

    return retries &lt; 5
```

  - **docker** (`Optional`\[`str`\]) – Select the docker image to be executed in by the remote session

  - **docker\_args** (`Optional`\[`str`\]) – Add docker arguments, pass a single string

  - **docker\_bash\_setup\_script** (`Optional`\[`str`\]) – Add bash script to be executed
    inside the docker before setting up the Task’s environment

  - **packages** (`Union`\[`bool`, `str`, `Sequence`\[`str`\], `None`\]) – Manually specify a list of required packages or a local requirements.txt file.
    Example: \[“tqdm>=2.1”, “scikit-learn”\] or “./requirements.txt”
    If not provided, packages are automatically added.
    Use False to install requirements from “requirements.txt” inside your git repository

  - **repo** (`Optional`\[`str`\]) – Optional, specify a repository to attach to the pipeline controller, when remotely executing.
    Allow users to execute the controller inside the specified repository, enabling them to load modules/script
    from the repository. Notice the execution work directory will be the repository root folder.
    Supports both git repo url link, and local repository path (automatically converted into the remote
    git/commit as is currently checkout).
    Example remote url: ‘ [https://github.com/user/repo.git](https://github.com/user/repo.git)’
    Example local repo copy: ‘./repo’ -> will automatically store the remote
    repo url and commit ID based on the locally cloned copy
    Use empty string (“”) to disable any repository auto-detection

  - **repo\_branch** (`Optional`\[`str`\]) – Optional, specify the remote repository branch (Ignored, if local repo path is used)

  - **repo\_commit** (`Optional`\[`str`\]) – Optional, specify the repository commit ID (Ignored, if local repo path is used)

  - **always\_create\_from\_code** (`bool`) – If True (default) the pipeline is always constructed from code,
    if False, pipeline is generated from pipeline configuration section on the pipeline Task itsef.
    this allows to edit (also add/remove) pipeline steps without changing the original codebase

  - **artifact\_serialization\_function** (`Optional`\[`Callable`\[\[`Any`\], `Union`\[`bytes`, `bytearray`\]\]\]) – A serialization function that takes one
    parameter of any type which is the object to be serialized. The function should return
    a bytes or bytearray object, which represents the serialized object. All parameter/return
    artifacts uploaded by the pipeline will be serialized using this function.
    All relevant imports must be done in this function. For example:


```py
def serialize(obj):

    import dill

    return dill.dumps(obj)
```

  - **artifact\_deserialization\_function** (`Optional`\[`Callable`\[\[`bytes`\], `Any`\]\]) – A deserialization function that takes one parameter of type bytes,
    which represents the serialized object. This function should return the deserialized object.
    All parameter/return artifacts fetched by the pipeline will be deserialized using this function.
    All relevant imports must be done in this function. For example:

```py
def deserialize(bytes_):

    import dill

    return dill.loads(bytes_)
```

  - **output\_uri** (`Union`\[`str`, `bool`, `None`\]) – The storage / output url for this pipeline. This is the default location for output
    models and other artifacts. Check Task.init reference docs for more info (output\_uri is a parameter).
    The output\_uri of this pipeline’s steps will default to this value.

  - **skip\_global\_imports** (`bool`) – If True, global imports will not be included in the steps’ execution when creating
    the steps from a functions, otherwise all global imports will be automatically imported in a safe manner at
    the beginning of each step’s execution. Default is False

  - **working\_dir** (`Optional`\[`str`\]) – Working directory to launch the pipeline from.

  - **enable\_local\_imports** (`bool`) – If True, allow pipeline steps to import from local files
    by appending to the PYTHONPATH of each step the directory the pipeline controller
    script resides in (sys.path\[0\]).
    If False, the directory won’t be appended to PYTHONPATH. Default is True.
    Ignored while running remotely.

* * *

### add\_function\_step [​](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/\#add_function_step "Direct link to add_function_step")

**add\_function\_step(name, function, function\_kwargs=None, function\_return=None, project\_name=None, task\_name=None, task\_type=None, auto\_connect\_frameworks=None, auto\_connect\_arg\_parser=None, packages=None, repo=None, repo\_branch=None, repo\_commit=None, helper\_functions=None, docker=None, docker\_args=None, docker\_bash\_setup\_script=None, parents=None, execution\_queue=None, monitor\_metrics=None, monitor\_artifacts=None, monitor\_models=None, time\_limit=None, continue\_on\_fail=False, pre\_execute\_callback=None, post\_execute\_callback=None, cache\_executed\_step=False, retry\_on\_failure=None, status\_change\_callback=None, tags=None, output\_uri=None, draft=False, working\_dir=None, continue\_behaviour=None, stage=None)**

Create a Task from a function, including wrapping the function input arguments
into the hyper-parameter section as kwargs, and storing function results as named artifacts

Example:

```py
def mock_func(a=6, b=9):

    c = a*b

    print(a, b, c)

    return c, c**2

create_task_from_function(mock_func, function_return=['mul', 'square'])
```

Example arguments from other Tasks (artifact):

```py
def mock_func(matrix_np):

    c = matrix_np*matrix_np

    print(matrix_np, c)

    return c

create_task_from_function(

    mock_func,

    function_kwargs={'matrix_np': 'aabb1122.previous_matrix'},

    function_return=['square_matrix']

)
```

- **Parameters**


  - **name** (`str`) – Unique of the step. For example stage1

  - **function** (`Callable`) – A global function to convert into a standalone Task

  - **function\_kwargs** (`Optional`\[`Dict`\[`str`, `Any`\]\]) – Optional, provide subset of function arguments and default values to expose.
    If not provided automatically take all function arguments & defaults
    Optional, pass input arguments to the function from other Tasks’ output artifact.
    Example argument named numpy\_matrix from Task ID aabbcc artifact name answer:
    `{'numpy_matrix': 'aabbcc.answer'}`

  - **function\_return** (`Optional`\[`List`\[`str`\]\]) – Provide a list of names for all the results.
    If not provided, no results will be stored as artifacts.

  - **project\_name** (`Optional`\[`str`\]) – Set the project name for the task. Required if base\_task\_id is None.

  - **task\_name** (`Optional`\[`str`\]) – Set the name of the remote task, if not provided use name argument.

  - **task\_type** (`Optional`\[`str`\]) – Optional, The task type to be created. Supported values: ‘training’, ‘testing’, ‘inference’,
    ‘data\_processing’, ‘application’, ‘monitor’, ‘controller’, ‘optimizer’, ‘service’, ‘qc’, ‘custom’

  - **auto\_connect\_frameworks** (`Optional`\[`dict`\]) – Control the frameworks auto connect, see Task.init auto\_connect\_frameworks

  - **auto\_connect\_arg\_parser** (`Optional`\[`dict`\]) – Control the ArgParser auto connect, see Task.init auto\_connect\_arg\_parser

  - **packages** (`Union`\[`bool`, `str`, `Sequence`\[`str`\], `None`\]) – Manually specify a list of required packages or a local requirements.txt file.
    Example: \[“tqdm>=2.1”, “scikit-learn”\] or “./requirements.txt”
    If not provided, packages are automatically added based on the imports used in the function.
    Use False to install requirements from “requirements.txt” inside your git repository

  - **repo** (`Optional`\[`str`\]) – Optional, specify a repository to attach to the function, when remotely executing.
    Allow users to execute the function inside the specified repository, enabling to load modules/script
    from a repository Notice the execution work directory will be the repository root folder.
    Supports both git repo url link, and local repository path.
    Example remote url: ‘ [https://github.com/user/repo.git](https://github.com/user/repo.git)’
    Example local repo copy: ‘./repo’ -> will automatically store the remote
    repo url and commit ID based on the locally cloned copy

  - **repo\_branch** (`Optional`\[`str`\]) – Optional, specify the remote repository branch (Ignored, if local repo path is used)

  - **repo\_commit** (`Optional`\[`str`\]) – Optional, specify the repository commit ID (Ignored, if local repo path is used)

  - **helper\_functions** (`Optional`\[`Sequence`\[`Callable`\]\]) – Optional, a list of helper functions to make available
    for the standalone function Task.

  - **docker** (`Optional`\[`str`\]) – Select the docker image to be executed in by the remote session

  - **docker\_args** (`Optional`\[`str`\]) – Add docker arguments, pass a single string

  - **docker\_bash\_setup\_script** (`Optional`\[`str`\]) – Add bash script to be executed
    inside the docker before setting up the Task’s environment

  - **parents** (`Optional`\[`Sequence`\[`str`\]\]) – Optional list of parent nodes in the DAG.
    The current step in the pipeline will be sent for execution only after all the parent nodes
    have been executed successfully.

  - **execution\_queue** (`Optional`\[`str`\]) – Optional, the queue to use for executing this specific step.
    If not provided, the task will be sent to the default execution queue, as defined on the class

  - **monitor\_metrics** (`Optional`\[`List`\[`Tuple`\]\]) – Optional, log the step’s metrics on the pipeline Task.
    Format is a list of pairs metric (title, series) to log: `[(step_metric_title, step_metric_series), ]`.
    For example: `[('test', 'accuracy'), ]`.
    Or a list of tuple pairs, to specify a different target metric for to use on the pipeline Task:
    `[((step_metric_title, step_metric_series), (target_metric_title, target_metric_series)), ]`.
    For example: `[[('test', 'accuracy'), ('model', 'accuracy')], ]`

  - **monitor\_artifacts** (`Optional`\[`List`\[`Union`\[`str`, `Tuple`\]\]\]) – Optional, log the step’s artifacts on the pipeline Task.
    Provided a list of artifact names existing on the step’s Task, they will also appear on the Pipeline itself.
    Example: `[('processed_data', 'final_processed_data'), ]`.
    Alternatively user can also provide a list of artifacts to monitor
    (target artifact name will be the same as original artifact name).
    Example: `['processed_data', ]`

  - **monitor\_models** (`Optional`\[`List`\[`Union`\[`str`, `Tuple`\]\]\]) – Optional, log the step’s output models on the pipeline Task.
    Provided a list of model names existing on the step’s Task, they will also appear on the Pipeline itself.
    Example: `[('model_weights', 'final_model_weights'), ]`.
    Alternatively user can also provide a list of models to monitor
    (target models name will be the same as original model).
    Example: `['model_weights', ]`.
    To select the latest (lexicographic) model use “model\_\*”, or the last created model with just “\*”.
    Example: `['model_weights_\*', ]`

  - **time\_limit** (`Optional`\[`float`\]) – Default None, no time limit.
    Step execution time limit, if exceeded the Task is aborted and the pipeline is stopped and marked failed.

  - **continue\_on\_fail** (`bool`) – (Deprecated, use continue\_behaviour instead).
    If True, failed step will not cause the pipeline to stop
    (or marked as failed). Notice, that steps that are connected (or indirectly connected)
    to the failed step will be skipped. Defaults to False

  - **pre\_execute\_callback** (`Optional`\[`Callable`\[\[`PipelineController`, `Node`, `dict`\], `bool`\]\]) – Callback function, called when the step (Task) is created
    and before it is sent for execution. Allows a user to modify the Task before launch.
    Use node.job to access the ClearmlJob object, or node.job.task to directly access the Task object.
    `parameters` are the configuration arguments passed to the ClearmlJob.


If the callback returned value is False,
the Node is skipped and so is any node in the DAG that relies on this node.

Notice the parameters are already parsed,
e.g. `${step1.parameters.Args/param}` is replaced with relevant value.

```py
def step_created_callback(

    pipeline,             # type: PipelineController,

    node,                 # type: PipelineController.Node,

    parameters,           # type: dict

):

    pass
```

  - **post\_execute\_callback** (`Optional`\[`Callable`\[\[`PipelineController`, `Node`\], `None`\]\]) – Callback function, called when a step (Task) is completed
    and other jobs are executed. Allows a user to modify the Task status after completion.

```py
def step_completed_callback(

    pipeline,             # type: PipelineController,

    node,                 # type: PipelineController.Node,

):

    pass
```

  - **cache\_executed\_step** (`bool`) – If True, before launching the new step,
    after updating with the latest configuration, check if an exact Task with the same parameter/code
    was already executed. If it was found, use it instead of launching a new Task.
    Default: False, a new cloned copy of base\_task is always used.
    Notice: If the git repo reference does not have a specific commit ID, the Task will never be used.

  - **retry\_on\_failure** (`Union`\[`int`, `Callable`\[\[`PipelineController`, `Node`, `int`\], `bool`\], `None`\]) – Integer (number of retries) or Callback function that returns True to allow a retry
    - Integer: In case of node failure, retry the node the number of times indicated by this parameter.

    - Callable: A function called on node failure. Takes as parameters:
      the PipelineController instance, the PipelineController.Node that failed and an int
      representing the number of previous retries for the node that failed.
      The function must return `True` if the node should be retried and `False` otherwise.
      If True, the node will be re-queued and the number of retries left will be decremented by 1.
      By default, if this callback is not specified, the function will be retried the number of
      times indicated by retry\_on\_failure.

```py
def example_retry_on_failure_callback(pipeline, node, retries):

    print(node.name, ' failed')

    # allow up to 5 retries (total of 6 runs)

    return retries &lt; 5
```

  - **status\_change\_callback** (`Optional`\[`Callable`\[\[`PipelineController`, `Node`, `str`\], `None`\]\]) – Callback function, called when the status of a step (Task) changes.
    Use node.job to access the ClearmlJob object, or node.job.task to directly access the Task object.
    The signature of the function must look the following way:

```py
def status_change_callback(

    pipeline,             # type: PipelineController,

    node,                 # type: PipelineController.Node,

    previous_status       # type: str

):

    pass
```

  - **tags** (`Union`\[`Sequence`\[`str`\], `str`, `None`\]) – A list of tags for the specific pipeline step.
    When executing a Pipeline remotely
    (i.e. launching the pipeline from the UI/enqueuing it), this method has no effect.

  - **output\_uri** (`Union`\[`str`, `bool`, `None`\]) – The storage / output url for this step. This is the default location for output
    models and other artifacts. Check Task.init reference docs for more info (output\_uri is a parameter).

  - **draft** (`Optional`\[`bool`\]) – (default False). If True, the Task will be created as a draft task.

  - **working\_dir** (`Optional`\[`str`\]) – Working directory to launch the script from.

  - **continue\_behaviour** (`Optional`\[`dict`\]) – Controls whether the pipeline will continue running after a step failed/was aborted.

    Different behaviours can be set using a dictionary of boolean options. Supported options are:
    - continue\_on\_fail - If True, the pipeline will continue even if the step failed.
      If False, the pipeline will stop

    - continue\_on\_abort - If True, the pipeline will continue even if the step was aborted.
      If False, the pipeline will stop

    - skip\_children\_on\_fail - If True, the children of this step will be skipped if it failed.
      If False, the children will run even if this step failed. Any parameters passed from the failed step to its
      children will default to None

    - skip\_children\_on\_abort - If True, the children of this step will be skipped if it was aborted.
      If False, the children will run even if this step was aborted.
      Any parameters passed from the failed step to its children will default to None

    - If the keys are not present in the dictionary, their values will default to True
  - **stage** (`Optional`\[`str`\]) – Name of the stage. This parameter enables pipeline step grouping into stages
- **Return type**

`bool`

- **Returns**

True if successful


* * *

### add\_parameter [​](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/\#add_parameter "Direct link to add_parameter")

**add\_parameter(name, default=None, description=None, param\_type=None)**

Add a parameter to the pipeline Task.
The parameter can be used as input parameter for any step in the pipeline.
Notice all parameters will appear under the PipelineController Task’s Hyper-parameters -> Pipeline section
Example: pipeline.add\_parameter(name=’dataset’, description=’dataset ID to process the pipeline’)
Then in one of the steps we can refer to the value of the parameter with `'${pipeline.dataset}'`

- **Parameters**
  - **name** (`str`) – String name of the parameter.

  - **default** (`Optional`\[`Any`\]) – Default value to be put as the default value (can be later changed in the UI)

  - **description** (`Optional`\[`str`\]) – String description of the parameter and its usage in the pipeline

  - **param\_type** (`Optional`\[`str`\]) – Optional, parameter type information (to be used as hint for casting and description)
- **Return type**

`None`


* * *

### add\_step [​](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/\#add_step "Direct link to add_step")

**add\_step(name, base\_task\_id=None, parents=None, parameter\_override=None, configuration\_overrides=None, task\_overrides=None, execution\_queue=None, monitor\_metrics=None, monitor\_artifacts=None, monitor\_models=None, time\_limit=None, base\_task\_project=None, base\_task\_name=None, clone\_base\_task=True, continue\_on\_fail=False, pre\_execute\_callback=None, post\_execute\_callback=None, cache\_executed\_step=False, base\_task\_factory=None, retry\_on\_failure=None, status\_change\_callback=None, recursively\_parse\_parameters=False, output\_uri=None, continue\_behaviour=None, stage=None)**

Add a step to the pipeline execution DAG.
Each step must have a unique name (this name will later be used to address the step)

- **Parameters**


  - **name** (`str`) – Unique of the step. For example stage1

  - **base\_task\_id** (`Optional`\[`str`\]) – The Task ID to use for the step. Each time the step is executed,
    the base Task is cloned, then the cloned task will be sent for execution.

  - **parents** (`Optional`\[`Sequence`\[`str`\]\]) – Optional list of parent nodes in the DAG.
    The current step in the pipeline will be sent for execution only after all the parent nodes
    have been executed successfully.

  - **parameter\_override** (`Optional`\[`Mapping`\[`str`, `Any`\]\]) – Optional parameter overriding dictionary.

    The dict values can reference a previously executed step using the following form `'${step_name}'`. Examples:
    - Artifact access `parameter_override={'Args/input_file': '${&lt;step_name&gt;.artifacts.&lt;artifact_name&gt;.url}' }`

    - Model access (last model used) `parameter_override={'Args/input_file': '${&lt;step_name&gt;.models.output.-1.url}' }`

    - Parameter access `parameter_override={'Args/input_file': '${&lt;step_name&gt;.parameters.Args/input_file}' }`

    - Pipeline Task argument (see Pipeline.add\_parameter) `parameter_override={'Args/input_file': '${pipeline.&lt;pipeline_parameter&gt;}' }`

    - Task ID `parameter_override={'Args/input_file': '${stage3.id}' }`
  - **recursively\_parse\_parameters** (`bool`) – If True, recursively parse parameters from parameter\_override in lists, dicts, or tuples.

    Example:
    - `parameter_override={'Args/input_file': ['${&lt;step_name&gt;.artifacts.&lt;artifact_name&gt;.url}', 'file2.txt']}` will be correctly parsed.

    - `parameter_override={'Args/input_file': ('${&lt;step_name_1&gt;.parameters.Args/input_file}', '${&lt;step_name_2&gt;.parameters.Args/input_file}')}` will be correctly parsed.
  - **configuration\_overrides** (`Optional`\[`Mapping`\[`str`, `Union`\[`str`, `Mapping`\]\]\]) – Optional, override Task configuration objects.

    Expected dictionary of configuration object name and configuration object content.
    Examples:
    - `{'General': dict(key='value')}`

    - `{'General': 'configuration file content'}`

    - `{'OmegaConf': YAML.dumps(full_hydra_dict)}`
  - **task\_overrides** (`Optional`\[`Mapping`\[`str`, `Any`\]\]) – Optional task section overriding dictionary.

    The dict values can reference a previously executed step using the following form `'${step_name}'`. Examples:
    - Get the latest commit from a specific branch `task_overrides={'script.version_num': '', 'script.branch': 'main'}`

    - Match git repository branch to a previous step `task_overrides={'script.branch': '${stage1.script.branch}', 'script.version_num': ''}`

    - Change container image `task_overrides={'container.image': 'nvidia/cuda:11.6.0-devel-ubuntu20.04', 'container.arguments': '--ipc=host'}`

    - Match container image to a previous step `task_overrides={'container.image': '${stage1.container.image}'}`

    - Reset requirements (the agent will use the “requirements.txt” inside the repo) `task_overrides={'script.requirements.pip': ""}`
  - **execution\_queue** (`Optional`\[`str`\]) – Optional, the queue to use for executing this specific step.
    If not provided, the task will be sent to the default execution queue, as defined on the class

  - **monitor\_metrics** (`Optional`\[`List`\[`Union`\[`Tuple`\[`str`, `str`\], `Tuple`\]\]\]) – Optional, log the step’s metrics on the pipeline Task.
    Format is a list of pairs metric (title, series) to log: `[(step_metric_title, step_metric_series), ]`.
    For example: `[('test', 'accuracy'), ]`.
    Or a list of tuple pairs, to specify a different target metric for to use on the pipeline Task:
    `[((step_metric_title, step_metric_series), (target_metric_title, target_metric_series)), ]`.
    For example: `[[('test', 'accuracy'), ('model', 'accuracy')], ]`

  - **monitor\_artifacts** (`Optional`\[`List`\[`Union`\[`str`, `Tuple`\[`str`, `str`\]\]\]\]) – Optional, log the step’s artifacts on the pipeline Task.
    Provided a list of artifact names existing on the step’s Task, they will also appear on the Pipeline itself.
    Example: `[('processed_data', 'final_processed_data'), ]`.
    Alternatively user can also provide a list of artifacts to monitor
    (target artifact name will be the same as original artifact name).
    Example: `['processed_data', ]`

  - **monitor\_models** (`Optional`\[`List`\[`Union`\[`str`, `Tuple`\[`str`, `str`\]\]\]\]) – Optional, log the step’s output models on the pipeline Task.
    Provided a list of model names existing on the step’s Task, they will also appear on the Pipeline itself.
    Example: `[('model_weights', 'final_model_weights'), ]`.
    Alternatively user can also provide a list of models to monitor
    (target models name will be the same as original model).
    Example: `['model_weights', ]`.
    To select the latest (lexicographic) model use “model\_\*”, or the last created model with just “\*”.
    Example: `['model_weights_\*', ]`

  - **time\_limit** (`Optional`\[`float`\]) – Default None, no time limit.
    Step execution time limit, if exceeded the Task is aborted and the pipeline is stopped and marked failed.

  - **base\_task\_project** (`Optional`\[`str`\]) – If base\_task\_id is not given,
    use the base\_task\_project and base\_task\_name combination to retrieve the base\_task\_id to use for the step.

  - **base\_task\_name** (`Optional`\[`str`\]) – If base\_task\_id is not given,
    use the base\_task\_project and base\_task\_name combination to retrieve the base\_task\_id to use for the step.

  - **clone\_base\_task** (`bool`) – If True (default), the pipeline will clone the base task, and modify/enqueue
    the cloned Task. If False, the base-task is used directly, notice it has to be in draft-mode (created).

  - **continue\_on\_fail** (`bool`) – (Deprecated, use continue\_behaviour instead).
    If True, failed step will not cause the pipeline to stop
    (or marked as failed). Notice, that steps that are connected (or indirectly connected)
    to the failed step will be skipped. Defaults to False

  - **pre\_execute\_callback** (`Optional`\[`Callable`\[\[`PipelineController`, `Node`, `dict`\], `bool`\]\]) – Callback function, called when the step (Task) is created
    and before it is sent for execution. Allows a user to modify the Task before launch.
    Use node.job to access the ClearmlJob object, or node.job.task to directly access the Task object.
    `parameters` are the configuration arguments passed to the ClearmlJob.


If the callback returned value is False,
the Node is skipped and so is any node in the DAG that relies on this node.

Notice the parameters are already parsed,
e.g. `${step1.parameters.Args/param}` is replaced with relevant value.

```py
def step_created_callback(

    pipeline,             # type: PipelineController,

    node,                 # type: PipelineController.Node,

    parameters,           # type: dict

):

    pass
```

  - **post\_execute\_callback** (`Optional`\[`Callable`\[\[`PipelineController`, `Node`\], `None`\]\]) – Callback function, called when a step (Task) is completed
    and other jobs are executed. Allows a user to modify the Task status after completion.

```py
def step_completed_callback(

    pipeline,             # type: PipelineController,

    node,                 # type: PipelineController.Node,

):

    pass
```

  - **cache\_executed\_step** (`bool`) – If True, before launching the new step,
    after updating with the latest configuration, check if an exact Task with the same parameter/code
    was already executed. If it was found, use it instead of launching a new Task.
    Default: False, a new cloned copy of base\_task is always used.
    Notice: If the git repo reference does not have a specific commit ID, the Task will never be used.
    If clone\_base\_task is False there is no cloning, hence the base\_task is used.

  - **base\_task\_factory** (`Optional`\[`Callable`\[\[`Node`\], [`Task`](https://clear.ml/docs/latest/docs/references/sdk/task#clearml.Task)\]\]) – Optional, instead of providing a pre-existing Task,
    provide a Callable function to create the Task (returns Task object)

  - **retry\_on\_failure** (`Union`\[`int`, `Callable`\[\[`PipelineController`, `Node`, `int`\], `bool`\], `None`\]) – Integer (number of retries) or Callback function that returns True to allow a retry
    - Integer: In case of node failure, retry the node the number of times indicated by this parameter.

    - Callable: A function called on node failure. Takes as parameters:
      the PipelineController instance, the PipelineController.Node that failed and an int
      representing the number of previous retries for the node that failed.
      The function must return `True` if the node should be retried and `False` otherwise.
      If True, the node will be re-queued and the number of retries left will be decremented by 1.
      By default, if this callback is not specified, the function will be retried the number of
      times indicated by retry\_on\_failure.

```py
def example_retry_on_failure_callback(pipeline, node, retries):

    print(f"{node.name} failed")

    # allow up to 5 retries (total of 6 runs)

    return retries &lt; 5
```

  - **status\_change\_callback** (`Optional`\[`Callable`\[\[`PipelineController`, `Node`, `str`\], `None`\]\]) – Callback function, called when the status of a step (Task) changes.
    Use node.job to access the ClearmlJob object, or node.job.task to directly access the Task object.
    The signature of the function must look the following way:

```py
def status_change_callback(

    pipeline,             # type: PipelineController,

    node,                 # type: PipelineController.Node,

    previous_status       # type: str

):

    pass
```

  - **output\_uri** (`Union`\[`str`, `bool`, `None`\]) – The storage / output url for this step. This is the default location for output
    models and other artifacts. Check Task.init reference docs for more info (output\_uri is a parameter).

  - **continue\_behaviour** (`Optional`\[`dict`\]) – Controls whether the pipeline will continue running after a step failed/was aborted.

    Different behaviours can be set using a dictionary of boolean options. Supported options are:
    - continue\_on\_fail - If True, the pipeline will continue even if the step failed.
      If False, the pipeline will stop

    - continue\_on\_abort - If True, the pipeline will continue even if the step was aborted.
      If False, the pipeline will stop

    - skip\_children\_on\_fail - If True, the children of this step will be skipped if it failed.
      If False, the children will run even if this step failed.
      Any parameters passed from the failed step to its children will default to None

    - skip\_children\_on\_abort - If True, the children of this step will be skipped if it was aborted.
      If False, the children will run even if this step was aborted.
      Any parameters passed from the failed step to its children will default to None

    - If the keys are not present in the dictionary, their values will default to True
  - **stage** (`Optional`\[`str`\]) – Name of the stage. This parameter enables pipeline step grouping into stages
- **Return type**

`bool`

- **Returns**

True if successful


* * *

### add\_tags [​](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/\#add_tags "Direct link to add_tags")

**add\_tags(tags)**

Add tags to this pipeline. Old tags are not deleted.
When executing a Pipeline remotely
(i.e. launching the pipeline from the UI/enqueuing it), this method has no effect.

- **Parameters**

**tags** (`Union`\[`Sequence`\[`str`\], `str`\]) – A list of tags for this pipeline.

- **Return type**

`None`


* * *

### PipelineController.clone [​](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/\#pipelinecontrollerclone "Direct link to PipelineController.clone")

**_classmethod_ clone(pipeline\_controller, name=None, comment=None, parent=None, project=None, version=None)**

Create a duplicate (a clone) of a pipeline (experiment). The status of the cloned pipeline is `Draft`
and modifiable.

- **Parameters**


  - **pipeline\_controller** ( _str_ ) – The pipeline to clone. Specify a PipelineController object or an ID.

  - **name** ( _str_ ) – The name of the new cloned pipeline.

  - **comment** ( _str_ ) – A comment / description for the new cloned pipeline.

  - **parent** ( _str_ ) – The ID of the parent Task of the new pipeline.
    - If `parent` is not specified, then `parent` is set to `source_task.parent`.

    - If `parent` is not specified and `source_task.parent` is not available,

then `parent` set to `source_task`.
  - **project** ( _str_ ) – The project name in which to create the new pipeline.
    If `None`, the clone inherits the original pipeline’s project

  - **version** ( _str_ ) – The version of the new cloned pipeline. If `None`, the clone
    inherits the original pipeline’s version
- **Return type**

`PipelineController`

- **Returns**

The new cloned PipelineController


* * *

### connect\_configuration [​](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/\#connect_configuration "Direct link to connect_configuration")

**connect\_configuration(configuration, name=None, description=None)**

Connect a configuration dictionary or configuration file (pathlib.Path / str) to the PipelineController object.
This method should be called before reading the configuration file.

For example, a local file:

```py
config_file = pipe.connect_configuration(config_file)

my_params = json.load(open(config_file,'rt'))
```

A parameter dictionary/list:

```py
my_params = pipe.connect_configuration(my_params)
```

- **Parameters**
  - **configuration** (`Union`\[`Mapping`, `list`, `Path`, `str`\]) – The configuration. This is usually the configuration used in the model training process.

    Specify one of the following:
    - A dictionary/list - A dictionary containing the configuration. ClearML stores the configuration in
      the **ClearML Server** (backend), in a HOCON format (JSON-like format) which is editable.

    - A `pathlib2.Path` string - A path to the configuration file. ClearML stores the content of the file.
      A local path must be relative path. When executing a pipeline remotely in a worker, the contents brought
      from the **ClearML Server** (backend) overwrites the contents of the file.
  - **name** ( _str_ ) – Configuration section name. default: ‘General’
    Allowing users to store multiple configuration dicts/files

  - **description** ( _str_ ) – Configuration section description (text). default: None
- **Return type**

`Union`\[`dict`, `Path`, `str`\]

- **Returns**

If a dictionary is specified, then a dictionary is returned. If pathlib2.Path / string is
specified, then a path to a local configuration file is returned. Configuration object.


* * *

### PipelineController.create [​](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/\#pipelinecontrollercreate "Direct link to PipelineController.create")

**_classmethod_ create(project\_name, task\_name, repo=None, branch=None, commit=None, script=None, working\_directory=None, packages=None, requirements\_file=None, docker=None, docker\_args=None, docker\_bash\_setup\_script=None, argparse\_args=None, force\_single\_script\_file=False, version=None, add\_run\_number=True, binary=None, module=None, detect\_repository=True)**

Manually create and populate a new Pipeline in the system.
Supports pipelines from functions, decorators and tasks.

- **Parameters**
  - **project\_name** (`str`) – Set the project name for the pipeline.

  - **task\_name** (`str`) – Set the name of the remote pipeline..

  - **repo** (`Optional`\[`str`\]) – Remote URL for the repository to use, or path to local copy of the git repository.
    Example: ‘ [https://github.com/allegroai/clearml.git](https://github.com/allegroai/clearml.git)’ or ‘~/project/repo’. If `repo` is specified, then
    the `script` parameter must also be specified

  - **branch** (`Optional`\[`str`\]) – Select specific repository branch/tag (implies the latest commit from the branch)

  - **commit** (`Optional`\[`str`\]) – Select specific commit ID to use (default: latest commit,
    or when used with local repository matching the local commit ID)

  - **script** (`Optional`\[`str`\]) – Specify the entry point script for the remote execution. When used in tandem with
    remote git repository the script should be a relative path inside the repository,
    for example: ‘./source/train.py’ . When used with local repository path it supports a
    direct path to a file inside the local repository itself, for example: ‘~/project/source/train.py’

  - **working\_directory** (`Optional`\[`str`\]) – Working directory to launch the script from. Default: repository root folder.
    Relative to repo root or local folder.

  - **packages** (`Union`\[`bool`, `Sequence`\[`str`\], `None`\]) – Manually specify a list of required packages. Example: `["tqdm&gt;=2.1", "scikit-learn"]`
    or True to automatically create requirements
    based on locally installed packages (repository must be local).
    Pass an empty string to not install any packages (not even from the repository)

  - **requirements\_file** (`Union`\[`str`, `Path`, `None`\]) – Specify requirements.txt file to install when setting the session.
    If not provided, the requirements.txt from the repository will be used.

  - **docker** (`Optional`\[`str`\]) – Select the docker image to be executed in by the remote session

  - **docker\_args** (`Optional`\[`str`\]) – Add docker arguments, pass a single string

  - **docker\_bash\_setup\_script** (`Optional`\[`str`\]) – Add bash script to be executed
    inside the docker before setting up the Task’s environment

  - **argparse\_args** (`Optional`\[`Sequence`\[`Tuple`\[`str`, `str`\]\]\]) – Arguments to pass to the remote execution, list of string pairs (argument, value)
    Notice, only supported if the codebase itself uses argparse.ArgumentParser

  - **force\_single\_script\_file** (`bool`) – If True, do not auto-detect local repository

  - **binary** (`Optional`\[`str`\]) – Binary used to launch the pipeline

  - **module** (`Optional`\[`str`\]) – If specified instead of executing script, a module named module is executed.
    Implies script is empty. Module can contain multiple argument for execution,
    for example: module=”my.module arg1 arg2”

  - **detect\_repository** (`bool`) – If True, detect the repository if no repository has been specified.
    If False, don’t detect repository under any circumstance. Ignored if repo is specified

  - **version** ( _Optional_ _\[_ _str_ _\]_ ) –

  - **add\_run\_number** ( _bool_ ) –
- **Return type**

`PipelineController`

- **Returns**

The newly created PipelineController


* * *

### create\_draft [​](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/\#create_draft "Direct link to create_draft")

**create\_draft()**

Optional, manually create & serialize the Pipeline Task (use with care for manual multi pipeline creation).

**Notice** The recommended flow would be to call pipeline.start(queue=None)
which would have a similar effect and will allow you to clone/enqueue later on.

After calling Pipeline.create(), users can edit the pipeline in the UI and enqueue it for execution.

Notice: this function should be used to programmatically create pipeline for later usage.
To automatically create and launch pipelines, call the start() method.

- **Return type**

`None`


* * *

### elapsed [​](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/\#elapsed "Direct link to elapsed")

**elapsed()**

Return minutes elapsed from controller stating time stamp.

- **Return type**

`float`

- **Returns**

The minutes from controller start time. A negative value means the process has not started yet.


* * *

### PipelineController.enqueue [​](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/\#pipelinecontrollerenqueue "Direct link to PipelineController.enqueue")

**_classmethod_ enqueue(pipeline\_controller, queue\_name=None, queue\_id=None, force=False)**

Enqueue a PipelineController for execution, by adding it to an execution queue.

info

A worker daemon must be listening at the queue for the worker to fetch the Task and execute it,
see “ClearML Agent” in the ClearML Documentation.

- **Parameters**
  - **pipeline\_controller** (`Union`\[`PipelineController`, `str`\]) – The PipelineController to enqueue. Specify a PipelineController object or PipelineController ID

  - **queue\_name** (`Optional`\[`str`\]) – The name of the queue. If not specified, then `queue_id` must be specified.

  - **queue\_id** (`Optional`\[`str`\]) – The ID of the queue. If not specified, then `queue_name` must be specified.

  - **force** ( _bool_ ) – If True, reset the PipelineController if necessary before enqueuing it
- **Return type**

`Any`

- **Returns**

An enqueue JSON response.





```javascript
{

       "queued": 1,

       "updated": 1,

       "fields": {

           "status": "queued",

           "status_reason": "",

           "status_message": "",

           "status_changed": "2020-02-24T15:05:35.426770+00:00",

           "last_update": "2020-02-24T15:05:35.426770+00:00",

           "execution.queue": "2bd96ab2d9e54b578cc2fb195e52c7cf"

           }

}
```








  - `queued` \- The number of Tasks enqueued (an integer or `null`).

  - `updated` \- The number of Tasks updated (an integer or `null`).

  - `fields`
    - `status` \- The status of the experiment.

    - `status_reason` \- The reason for the last status change.

    - `status_message` \- Information about the status.

    - `status_changed` \- The last status change date and time (ISO 8601 format).

    - `last_update` \- The last Task update time, including Task creation, update, change, or events for this task (ISO 8601 format).

    - `execution.queue` \- The ID of the queue where the Task is enqueued. `null` indicates not enqueued.

* * *

### PipelineController.get [​](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/\#pipelinecontrollerget "Direct link to PipelineController.get")

**_classmethod_ get(pipeline\_id=None, pipeline\_project=None, pipeline\_name=None, pipeline\_version=None, pipeline\_tags=None, shallow\_search=False)**

Get a specific PipelineController. If multiple pipeline controllers are found, the pipeline controller
with the highest semantic version is returned. If no semantic version is found, the most recently
updated pipeline controller is returned. This function raises aan Exception if no pipeline controller
was found

Note: In order to run the pipeline controller returned by this function, use PipelineController.enqueue

- **Parameters**
  - **pipeline\_id** (`Optional`\[`str`\]) – Requested PipelineController ID

  - **pipeline\_project** (`Optional`\[`str`\]) – Requested PipelineController project

  - **pipeline\_name** (`Optional`\[`str`\]) – Requested PipelineController name

  - **pipeline\_tags** (`Optional`\[`Sequence`\[`str`\]\]) – Requested PipelineController tags (list of tag strings)

  - **shallow\_search** (`bool`) – If True, search only the first 500 results (first page)

  - **pipeline\_version** ( _Optional_ _\[_ _str_ _\]_ ) –
- **Return type**

`PipelineController`


* * *

### PipelineController.get\_logger [​](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/\#pipelinecontrollerget_logger "Direct link to PipelineController.get_logger")

**_classmethod_ get\_logger()**

Return a logger connected to the Pipeline Task.
The logger can be used by any function/tasks executed by the pipeline, in order to report
directly to the pipeline Task itself. It can also be called from the main pipeline control Task.

Raise ValueError if main Pipeline task could not be located.

- **Return type**

[`Logger`](https://clear.ml/docs/latest/docs/references/sdk/logger#clearml.Logger)

- **Returns**

Logger object for reporting metrics (scalars, plots, debug samples etc.)


* * *

### get\_parameters [​](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/\#get_parameters "Direct link to get_parameters")

**get\_parameters()**

Return the pipeline parameters dictionary

- **Return type**

`dict`

- **Returns**

Dictionary str -> str


* * *

### get\_pipeline\_dag [​](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/\#get_pipeline_dag "Direct link to get_pipeline_dag")

**get\_pipeline\_dag()**

Return the pipeline execution graph, each node in the DAG is PipelineController.Node object.
Graph itself is a dictionary of Nodes (key based on the Node name),
each node holds links to its parent Nodes (identified by their unique names)

- **Return type**

`Mapping`\[`str`, `Node`\]

- **Returns**

execution tree, as a nested dictionary. Example:


```py
{

    'stage1' : Node() {

        name: 'stage1'

        job: ClearmlJob

        ...

    },

}
```

* * *

### get\_processed\_nodes [​](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/\#get_processed_nodes "Direct link to get_processed_nodes")

**get\_processed\_nodes()**

Return a list of the processed pipeline nodes, each entry in the list is PipelineController.Node object.

- **Return type**

`Sequence`\[`Node`\]

- **Returns**

executed (excluding currently executing) nodes list


* * *

### get\_running\_nodes [​](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/\#get_running_nodes "Direct link to get_running_nodes")

**get\_running\_nodes()**

Return a list of the currently running pipeline nodes,
each entry in the list is PipelineController.Node object.

- **Return type**

`Sequence`\[`Node`\]

- **Returns**

Currently running nodes list


* * *

### is\_running [​](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/\#is_running "Direct link to is_running")

**is\_running()**

return True if the pipeline controller is running.

- **Return type**

`bool`

- **Returns**

A boolean indicating whether the pipeline controller is active (still running) or stopped.


* * *

### is\_successful [​](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/\#is_successful "Direct link to is_successful")

**is\_successful(fail\_on\_step\_fail=True, fail\_condition='all')**

Evaluate whether the pipeline is successful.

- **Parameters**
  - **fail\_on\_step\_fail** (`bool`) – If True (default), evaluate the pipeline steps’ status to assess if the pipeline
    is successful. If False, only evaluate the controller

  - **fail\_condition** (`str`) – Must be one of the following: ‘all’ (default), ‘failed’ or ‘aborted’. If ‘failed’, this
    function will return False if the pipeline failed and True if the pipeline was aborted. If ‘aborted’,
    this function will return False if the pipeline was aborted and True if the pipeline failed. If ‘all’,
    this function will return False in both cases.
- **Return type**

`bool`

- **Returns**

A boolean indicating whether the pipeline was successful or not. Note that if the pipeline is in a
running/pending state, this function will return False


* * *

### set\_default\_execution\_queue [​](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/\#set_default_execution_queue "Direct link to set_default_execution_queue")

**set\_default\_execution\_queue(default\_execution\_queue)**

Set the default execution queue if pipeline step does not specify an execution queue

- **Parameters**

**default\_execution\_queue** (`Optional`\[`str`\]) – The execution queue to use if no execution queue is provided

- **Return type**

`None`


* * *

### set\_pipeline\_execution\_time\_limit [​](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/\#set_pipeline_execution_time_limit "Direct link to set_pipeline_execution_time_limit")

**set\_pipeline\_execution\_time\_limit(max\_execution\_minutes)**

Set maximum execution time (minutes) for the entire pipeline. Pass None or 0 to disable execution time limit.

- **Parameters**

**max\_execution\_minutes** ( _float_ ) – The maximum time (minutes) for the entire pipeline process. The
default is `None`, indicating no time limit.

- **Return type**

`None`


* * *

### start [​](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/\#start "Direct link to start")

**start(queue='services', step\_task\_created\_callback=None, step\_task\_completed\_callback=None, wait=True)**

Start the current pipeline remotely (on the selected services queue).
The current process will be stopped and launched remotely.

- **Parameters**


  - **queue** (`str`) – queue name to launch the pipeline on

  - **step\_task\_created\_callback** ( _Callable_ ) – Callback function, called when a step (Task) is created
    and before it is sent for execution. Allows a user to modify the Task before launch.
    Use node.job to access the ClearmlJob object, or node.job.task to directly access the Task object.
    parameters are the configuration arguments passed to the ClearmlJob.


If the callback returned value is False,
the Node is skipped and so is any node in the DAG that relies on this node.

Notice the parameters are already parsed,
e.g. `${step1.parameters.Args/param}` is replaced with relevant value.

```py
def step_created_callback(

    pipeline,             # type: PipelineController,

    node,                 # type: PipelineController.Node,

    parameters,           # type: dict

):

    pass
```

  - **step\_task\_completed\_callback** ( _Callable_ ) – Callback function, called when a step (Task) is completed
    and other jobs are executed. Allows a user to modify the Task status after completion.

```py
def step_completed_callback(

    pipeline,             # type: PipelineController,

    node,                 # type: PipelineController.Node,

):

    pass
```

  - **wait** (`bool`) – If True (default), start the pipeline controller, return only
    after the pipeline is done (completed/aborted/failed)
- **Return type**

`bool`

- **Returns**

True, if the controller started. False, if the controller did not start.


* * *

### start\_locally [​](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/\#start_locally "Direct link to start_locally")

**start\_locally(run\_pipeline\_steps\_locally=False)**

Start the current pipeline locally, meaning the pipeline logic is running on the current machine,
instead of on the services queue.

Using run\_pipeline\_steps\_locally=True you can run all the pipeline steps locally as sub-processes.
Notice: when running pipeline steps locally, it assumes local code execution
(i.e. it is running the local code as is, regardless of the git commit/diff on the pipeline steps Task)

- **Parameters**

**run\_pipeline\_steps\_locally** (`bool`) – (default False) If True, run the pipeline steps themselves locally as a
subprocess (use for debugging the pipeline locally, notice the pipeline code is expected to be available
on the local machine)

- **Return type**

`None`


* * *

### stop [​](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/\#stop "Direct link to stop")

**stop(timeout=None, mark\_failed=False, mark\_aborted=False)**

Stop the pipeline controller and the optimization thread.
If mark\_failed and mark\_aborted are False (default) mark the pipeline as completed,
unless one of the steps failed, then mark the pipeline as failed.

- **Parameters**
  - **timeout** (`Optional`\[`float`\]) – Wait timeout for the optimization thread to exit (minutes).
    The default is `None`, indicating do not wait to terminate immediately.

  - **mark\_failed** (`bool`) – If True, mark the pipeline task as failed. (default False)

  - **mark\_aborted** (`bool`) – If True, mark the pipeline task as aborted. (default False)
- **Return type**

`None`


* * *

### update\_execution\_plot [​](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/\#update_execution_plot "Direct link to update_execution_plot")

**update\_execution\_plot()**

Update sankey diagram of the current pipeline

- **Return type**

`None`


* * *

### PipelineController.upload\_artifact [​](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/\#pipelinecontrollerupload_artifact "Direct link to PipelineController.upload_artifact")

**_classmethod_ upload\_artifact(name, artifact\_object, metadata=None, delete\_after\_upload=False, auto\_pickle=None, preview=None, wait\_on\_upload=False, serialization\_function=None, sort\_keys=True)**

Upload (add) an artifact to the main Pipeline Task object.
This function can be called from any pipeline component to directly add artifacts into the main pipeline Task.

The artifact can be uploaded by any function/tasks executed by the pipeline, in order to report
directly to the pipeline Task itself. It can also be called from the main pipeline control Task.

Raise ValueError if main Pipeline task could not be located.

The currently supported upload artifact types include:

- string / Path - A path to artifact file. If a wildcard or a folder is specified, then ClearML
creates and uploads a ZIP file.

- dict - ClearML stores a dictionary as `.json` file and uploads it.

- pandas.DataFrame - ClearML stores a pandas.DataFrame as `.csv.gz` (compressed CSV) file and uploads it.

- numpy.ndarray - ClearML stores a numpy.ndarray as `.npz` file and uploads it.

- PIL.Image - ClearML stores a PIL.Image as `.png` file and uploads it.

- Any - If called with auto\_pickle=True, the object will be pickled and uploaded.

- **Parameters**


  - **name** (`str`) – The artifact name.

warning

If an artifact with the same name was previously uploaded, then it is overwritten.

  - **artifact\_object** (`Any`) – The artifact object.

  - **metadata** (`Optional`\[`Mapping`\]) – A dictionary of key-value pairs for any metadata. This dictionary appears with the
    experiment in the **ClearML Web-App (UI)**, **ARTIFACTS** tab.

  - **delete\_after\_upload** (`bool`) – After the upload, delete the local copy of the artifact
    - `True` \- Delete the local copy of the artifact.

    - `False` \- Do not delete. (default)
  - **auto\_pickle** (`Optional`\[`bool`\]) – If True, and the artifact\_object is not one of the following types:
    pathlib2.Path, dict, pandas.DataFrame, numpy.ndarray, PIL.Image, url (string), local\_file (string)
    the artifact\_object will be pickled and uploaded as pickle file artifact (with file extension .pkl)
    If set to None (default) the sdk.development.artifacts.auto\_pickle configuration value will be used.

  - **preview** (`Optional`\[`Any`\]) – The artifact preview

  - **wait\_on\_upload** (`bool`) – Whether the upload should be synchronous, forcing the upload to complete
    before continuing.

  - **serialization\_function** (`Optional`\[`Callable`\[\[`Any`\], `Union`\[`bytes`, `bytearray`\]\]\]) – A serialization function that takes one
    parameter of any type which is the object to be serialized. The function should return
    a bytes or bytearray object, which represents the serialized object. Note that the object will be
    immediately serialized using this function, thus other serialization methods will not be used
    (e.g. pandas.DataFrame.to\_csv), even if possible. To deserialize this artifact when getting
    it using the Artifact.get method, use its deserialization\_function argument.

  - **sort\_keys** (`bool`) – If True (default), sort the keys of the artifact if it is yaml/json serializable.
    Otherwise, don’t sort the keys. Ignored if the artifact is not yaml/json serializable.
- **Return type**

`bool`

- **Returns**

The status of the upload.
  - `True` \- Upload succeeded.

  - `False` \- Upload failed.
- **Raise**

If the artifact object type is not supported, raise a `ValueError`.


* * *

### PipelineController.upload\_model [​](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/\#pipelinecontrollerupload_model "Direct link to PipelineController.upload_model")

**_classmethod_ upload\_model(model\_name, model\_local\_path, upload\_uri=None)**

Upload (add) a model to the main Pipeline Task object.
This function can be called from any pipeline component to directly add models into the main pipeline Task

The model file/path will be uploaded to the Pipeline Task and registered on the model repository.

Raise ValueError if main Pipeline task could not be located.

- **Parameters**
  - **model\_name** (`str`) – Model name as will appear in the model registry (in the pipeline’s project)

  - **model\_local\_path** (`str`) – Path to the local model file or directory to be uploaded.
    If a local directory is provided the content of the folder (recursively) will be
    packaged into a zip file and uploaded

  - **upload\_uri** (`Optional`\[`str`\]) – The URI of the storage destination for model weights upload. The default value
    is the previously used URI.
- **Return type**

[`OutputModel`](https://clear.ml/docs/latest/docs/references/sdk/model_outputmodel#clearml.OutputModel)

- **Returns**

The uploaded OutputModel


* * *

### wait [​](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/\#wait "Direct link to wait")

**wait(timeout=None)**

Wait for the pipeline to finish.

info

This method does not stop the pipeline. Call stop to terminate the pipeline.

- **Parameters**

**timeout** ( _float_ ) – The timeout to wait for the pipeline to complete (minutes).
If `None`, then wait until we reached the timeout, or pipeline completed.

- **Return type**

`bool`

- **Returns**

True, if the pipeline finished. False, if the pipeline timed out.


- [_class_ PipelineController(name, project, version=None, pool\_frequency=0.2, add\_pipeline\_tags=False, target\_project=True, auto\_version\_bump=None, abort\_on\_failure=False, add\_run\_number=True, retry\_on\_failure=None, docker=None, docker\_args=None, docker\_bash\_setup\_script=None, packages=None, repo=None, repo\_branch=None, repo\_commit=None, always\_create\_from\_code=True, artifact\_serialization\_function=None, artifact\_deserialization\_function=None, output\_uri=None, skip\_global\_imports=False, working\_dir=None, enable\_local\_imports=True)](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/#class-pipelinecontrollername-project-versionnone-pool_frequency02-add_pipeline_tagsfalse-target_projecttrue-auto_version_bumpnone-abort_on_failurefalse-add_run_numbertrue-retry_on_failurenone-dockernone-docker_argsnone-docker_bash_setup_scriptnone-packagesnone-reponone-repo_branchnone-repo_commitnone-always_create_from_codetrue-artifact_serialization_functionnone-artifact_deserialization_functionnone-output_urinone-skip_global_importsfalse-working_dirnone-enable_local_importstrue)
  - [add\_function\_step](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/#add_function_step)
  - [add\_parameter](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/#add_parameter)
  - [add\_step](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/#add_step)
  - [add\_tags](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/#add_tags)
  - [PipelineController.clone](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/#pipelinecontrollerclone)
  - [connect\_configuration](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/#connect_configuration)
  - [PipelineController.create](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/#pipelinecontrollercreate)
  - [create\_draft](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/#create_draft)
  - [elapsed](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/#elapsed)
  - [PipelineController.enqueue](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/#pipelinecontrollerenqueue)
  - [PipelineController.get](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/#pipelinecontrollerget)
  - [PipelineController.get\_logger](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/#pipelinecontrollerget_logger)
  - [get\_parameters](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/#get_parameters)
  - [get\_pipeline\_dag](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/#get_pipeline_dag)
  - [get\_processed\_nodes](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/#get_processed_nodes)
  - [get\_running\_nodes](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/#get_running_nodes)
  - [is\_running](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/#is_running)
  - [is\_successful](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/#is_successful)
  - [set\_default\_execution\_queue](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/#set_default_execution_queue)
  - [set\_pipeline\_execution\_time\_limit](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/#set_pipeline_execution_time_limit)
  - [start](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/#start)
  - [start\_locally](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/#start_locally)
  - [stop](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/#stop)
  - [update\_execution\_plot](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/#update_execution_plot)
  - [PipelineController.upload\_artifact](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/#pipelinecontrollerupload_artifact)
  - [PipelineController.upload\_model](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/#pipelinecontrollerupload_model)
  - [wait](https://clear.ml/docs/latest/docs/references/sdk/automation_controller_pipelinecontroller/#wait)