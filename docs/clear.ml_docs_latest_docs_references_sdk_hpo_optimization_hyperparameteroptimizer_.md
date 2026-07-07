---
url: "https://clear.ml/docs/latest/docs/references/sdk/hpo_optimization_hyperparameteroptimizer/"
title: "HyperParameterOptimizer | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/sdk/hpo_optimization_hyperparameteroptimizer/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

## _class_ automation.HyperParameterOptimizer(base\_task\_id, hyper\_parameters, objective\_metric\_title, objective\_metric\_series, objective\_metric\_sign='min', optimizer\_class=<class 'clearml.automation.optimization.RandomSearch'>, max\_number\_of\_concurrent\_tasks=10, execution\_queue='default', optimization\_time\_limit=None, compute\_time\_limit=None, auto\_connect\_task=True, always\_create\_task=False, spawn\_project=None, save\_top\_k\_tasks\_only=None, \*\*optimizer\_kwargs) [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_optimization_hyperparameteroptimizer/\#class-automationhyperparameteroptimizerbase_task_id-hyper_parameters-objective_metric_title-objective_metric_series-objective_metric_signmin-optimizer_classclass-clearmlautomationoptimizationrandomsearch-max_number_of_concurrent_tasks10-execution_queuedefault-optimization_time_limitnone-compute_time_limitnone-auto_connect_tasktrue-always_create_taskfalse-spawn_projectnone-save_top_k_tasks_onlynone-optimizer_kwargs "Direct link to class-automationhyperparameteroptimizerbase_task_id-hyper_parameters-objective_metric_title-objective_metric_series-objective_metric_signmin-optimizer_classclass-clearmlautomationoptimizationrandomsearch-max_number_of_concurrent_tasks10-execution_queuedefault-optimization_time_limitnone-compute_time_limitnone-auto_connect_tasktrue-always_create_taskfalse-spawn_projectnone-save_top_k_tasks_onlynone-optimizer_kwargs")

Hyperparameter search controller. Clones the base experiment, changes arguments and tries to maximize/minimize
the defined objective.

Create a new hyperparameter controller. The newly created object will launch and monitor the new experiments.

- **Parameters**


  - **base\_task\_id** ( _str_ ) – The Task ID to be used as template experiment to optimize.

  - **hyper\_parameters** ( _list_ ) – The list of Parameter objects to optimize over.

  - **objective\_metric\_title** (`Union`\[`str`, `Sequence`\[`str`\]\]) – The Objective metric title(s) to maximize / minimize
    (for example, `validation`, `["validation", "loss"]`). If `objective_metric_title` is a sequence
    (used to optimize multiple objectives at the same time), then `objective_metric_series` and
    `objective_metric_sign` have to be sequences of the same length. Each title will be matched
    with the respective series and sign

  - **objective\_metric\_series** ( _Union_ _\[_ _str_ \\*, \\* _Sequence_ _\[_ _str_ _\]_ _\]_ ) – The Objective metric series to maximize / minimize
    (for example, `loss_series`, `["validation_series", "loss_series"]`).

  - **objective\_metric\_sign** ( _Union_ _\[_ _str_ \\*, \\* _Sequence_ _\[_ _str_ _\]_ _\]_ ) – The objectives to maximize / minimize.

    The values are:
    - `min` \- Minimize the last reported value for the specified title/series scalar.

    - `max` \- Maximize the last reported value for the specified title/series scalar.

    - `min_global` \- Minimize the min value of _all_ reported values for the specific title/series scalar.

    - `max_global` \- Maximize the max value of _all_ reported values for the specific title/series scalar.
  - **optimizer\_class** ( _class.SearchStrategy_ ) – The SearchStrategy optimizer to use for the hyperparameter search

  - **max\_number\_of\_concurrent\_tasks** ( _int_ ) – The maximum number of concurrent Tasks (experiments) running at the
    same time.

  - **execution\_queue** ( _str_ ) – The execution queue to use for launching Tasks (experiments).

  - **optimization\_time\_limit** ( _float_ ) – The maximum time (minutes) for the entire optimization process. The
    default is `None`, indicating no time limit.

  - **compute\_time\_limit** ( _float_ ) – The maximum compute time in minutes. When time limit is exceeded,
    all jobs aborted. (Optional)

  - **auto\_connect\_task** ( _bool_ ) – Store optimization arguments and configuration in the Task.

    The values are:


    - `True` \- The optimization argument and configuration will be stored in the Task. All arguments will

be under the hyperparameter section `opt`, and the optimization hyper\_parameters space will be
stored in the Task configuration object section.
    - `False` \- Do not store with Task.

    - `Task` \- A specific Task object to connect the optimization process with.
  - **always\_create\_task** ( _bool_ ) – Always create a new Task.

    The values are:


    - `True` \- No current Task initialized. Create a new task named `optimization` in the `base_task_id`

project.
    - `False` \- Use the `task.Task.current_task` (if exists) to report statistics.
  - **spawn\_project** ( _str_ ) – If project name is specified, create all optimization Jobs (Tasks) in the
    specified project instead of the original base\_task\_id project.

  - **save\_top\_k\_tasks\_only** ( _int_ ) – If specified and above 0, keep only the top\_k performing Tasks,
    and archive the rest of the created Tasks. Default: -1 keep everything, nothing will be archived.

  - **optimizer\_kwargs** ( _\*\*_ ) – Arguments passed directly to the optimizer constructor.


Example:

```py
:linenos:

:caption: Example

from clearml import Task

from clearml.automation import UniformParameterRange, DiscreteParameterRange

from clearml.automation import GridSearch, RandomSearch, HyperParameterOptimizer

task = Task.init('examples', 'HyperParameterOptimizer example')

an_optimizer = HyperParameterOptimizer(

    base_task_id='fa30fa45d95d4927b87c323b5b04dc44',

    hyper_parameters=[\
\
        UniformParameterRange('lr', min_value=0.01, max_value=0.3, step_size=0.05),\
\
        DiscreteParameterRange('network', values=['ResNet18', 'ResNet50', 'ResNet101']),\
\
    ],

    objective_metric_title='title',

    objective_metric_series='series',

    objective_metric_sign='min',

    max_number_of_concurrent_tasks=5,

    optimizer_class=RandomSearch,

    execution_queue='workers', time_limit_per_job=120, pool_period_min=0.2)

# This will automatically create and print the optimizer new task id

# for later use. if a Task was already created, it will use it.

an_optimizer.set_time_limit(in_minutes=10.)

an_optimizer.start()

# we can create a pooling loop if we like

while not an_optimizer.reached_time_limit():

    top_exp = an_optimizer.get_top_experiments(top_k=3)

    print(top_exp)

# wait until optimization completed or timed-out

an_optimizer.wait()

# make sure we stop all jobs

an_optimizer.stop()
```

  - **objective\_metric\_series** –

  - **objective\_metric\_sign** –

* * *

### elapsed [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_optimization_hyperparameteroptimizer/\#elapsed "Direct link to elapsed")

**elapsed()**

Return minutes elapsed from controller stating time stamp.

- **Return type**

`float`

- **Returns**

The minutes from controller start time. A negative value means the process has not started yet.


* * *

### get\_active\_experiments [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_optimization_hyperparameteroptimizer/\#get_active_experiments "Direct link to get_active_experiments")

**get\_active\_experiments()**

Return a list of Tasks of the current active experiments.

- **Return type**

`Sequence`\[ [`Task`](https://clear.ml/docs/latest/docs/references/sdk/task#clearml.Task)\]

- **Returns**

A list of Task objects, representing the current active experiments.


* * *

### get\_num\_active\_experiments [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_optimization_hyperparameteroptimizer/\#get_num_active_experiments "Direct link to get_num_active_experiments")

**get\_num\_active\_experiments()**

Return the number of current active experiments.

- **Return type**

`int`

- **Returns**

The number of active experiments.


* * *

### get\_optimizer [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_optimization_hyperparameteroptimizer/\#get_optimizer "Direct link to get_optimizer")

**get\_optimizer()**

Return the currently used optimizer object.

- **Return type**

`SearchStrategy`

- **Returns**

The SearchStrategy object used.


* * *

### HyperParameterOptimizer.get\_optimizer\_top\_experiments [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_optimization_hyperparameteroptimizer/\#hyperparameteroptimizerget_optimizer_top_experiments "Direct link to HyperParameterOptimizer.get_optimizer_top_experiments")

**_classmethod_ get\_optimizer\_top\_experiments(objective\_metric\_title, objective\_metric\_series, objective\_metric\_sign, optimizer\_task\_id, top\_k)**

Return a list of Tasks of the top performing experiments
for a specific HyperParameter Optimization session (i.e. Task ID), based on the title/series objective.

- **Parameters**
  - **objective\_metric\_title** ( _str_ ) – The Objective metric title to maximize / minimize (for example,
    `validation`).

  - **objective\_metric\_series** ( _str_ ) – The Objective metric series to maximize / minimize (for example, `loss`).

  - **objective\_metric\_sign** ( _str_ ) – The objective to maximize / minimize.

    The values are:
    - `min` \- Minimize the last reported value for the specified title/series scalar.

    - `max` \- Maximize the last reported value for the specified title/series scalar.

    - `min_global` \- Minimize the min value of _all_ reported values for the specific title/series scalar.

    - `max_global` \- Maximize the max value of _all_ reported values for the specific title/series scalar.
  - **optimizer\_task\_id** ( _str_ ) – Parent optimizer Task ID

  - **top\_k** (`int`) – The number of Tasks (experiments) to return.
- **Return type**

`Sequence`\[ [`Task`](https://clear.ml/docs/latest/docs/references/sdk/task#clearml.Task)\]

- **Returns**

A list of Task objects, ordered by performance, where index 0 is the best performing Task.


* * *

### get\_time\_limit [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_optimization_hyperparameteroptimizer/\#get_time_limit "Direct link to get_time_limit")

**get\_time\_limit()**

Return the controller optimization time limit.

- **Return type**

`datetime`

- **Returns**

The absolute datetime limit of the controller optimization process.


* * *

### get\_top\_experiments [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_optimization_hyperparameteroptimizer/\#get_top_experiments "Direct link to get_top_experiments")

**get\_top\_experiments(top\_k)**

Return a list of Tasks of the top performing experiments, based on the controller `Objective` object.

- **Parameters**

**top\_k** ( _int_ ) – The number of Tasks (experiments) to return.

- **Return type**

`Sequence`\[ [`Task`](https://clear.ml/docs/latest/docs/references/sdk/task#clearml.Task)\]

- **Returns**

A list of Task objects, ordered by performance, where index 0 is the best performing Task.


* * *

### get\_top\_experiments\_details [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_optimization_hyperparameteroptimizer/\#get_top_experiments_details "Direct link to get_top_experiments_details")

**get\_top\_experiments\_details(top\_k, all\_metrics=False, all\_hyper\_parameters=False, only\_completed=False)**

Return a list of dictionaries of the top performing experiments.
Example: `[{'task_id': Task-ID, 'metrics': scalar-metric-dict, 'hyper_parameters': Hyper-Parameters},]`

Order is based on the controller `Objective` object.

- **Parameters**
  - **top\_k** ( _int_ ) – The number of Tasks (experiments) to return.

  - **all\_metrics** (`bool`) – Default False, only return the objective metric on the metrics dictionary.
    If True, return all scalar metrics of the experiment

  - **all\_hyper\_parameters** (`bool`) – Default False. If True, return all the hyperparameters from all the sections.

  - **only\_completed** (`bool`) – return only completed Tasks. Default False.
- **Return type**

`Sequence`\[`Union`\[`str`, `dict`\]\]

- **Returns**

A list of dictionaries `({task_id: '', hyper_parameters: {}, metrics: {}})`, ordered by performance,
where index 0 is the best performing Task.
Example w/ all\_metrics=False:





```py
[\
\
      {\
\
          task_id: '0593b76dc7234c65a13a301f731958fa',\
\
          hyper_parameters: {'General/lr': '0.03', 'General/batch_size': '32'},\
\
          metrics: {\
\
              'accuracy per class/cat': {\
\
                  'metric': 'accuracy per class',\
\
                  'variant': 'cat',\
\
                  'value': 0.119,\
\
                  'min_value': 0.119,\
\
                  'max_value': 0.782\
\
              },\
\
          }\
\
      },\
\
]
```









Example w/ all\_metrics=True:





```py
[\
\
      {\
\
          task_id: '0593b76dc7234c65a13a301f731958fa',\
\
          hyper_parameters: {'General/lr': '0.03', 'General/batch_size': '32'},\
\
          metrics: {\
\
              'accuracy per class/cat': {\
\
                  'metric': 'accuracy per class',\
\
                  'variant': 'cat',\
\
                  'value': 0.119,\
\
                  'min_value': 0.119,\
\
                  'max_value': 0.782\
\
              },\
\
              'accuracy per class/deer': {\
\
                  'metric': 'accuracy per class',\
\
                  'variant': 'deer',\
\
                  'value': 0.219,\
\
                  'min_value': 0.219,\
\
                  'max_value': 0.282\
\
              },\
\
          }\
\
      },\
\
]
```


* * *

### is\_active [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_optimization_hyperparameteroptimizer/\#is_active "Direct link to is_active")

**is\_active()**

Is the optimization procedure active (still running)

The values are:

- `True` \- The optimization procedure is active (still running).

- `False` \- The optimization procedure is not active (not still running).


info

If the daemon thread has not yet started, is\_active returns True.

- **Return type**

`bool`

- **Returns**

A boolean indicating whether the optimization procedure is active (still running) or stopped.


* * *

### is\_running [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_optimization_hyperparameteroptimizer/\#is_running "Direct link to is_running")

**is\_running()**

Is the optimization controller is running

The values are:

- `True` \- The optimization procedure is running.

- `False` \- The optimization procedure is running.


- **Return type**

`bool`

- **Returns**

A boolean indicating whether the optimization procedure is active (still running) or stopped.


* * *

### reached\_time\_limit [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_optimization_hyperparameteroptimizer/\#reached_time_limit "Direct link to reached_time_limit")

**reached\_time\_limit()**

Did the optimizer reach the time limit

The values are:

- `True` \- The time limit passed.

- `False` \- The time limit did not pass.


This method returns immediately, it does not wait for the optimizer.

- **Return type**

`bool`

- **Returns**

True, if optimizer is running and we passed the time limit, otherwise returns False.


* * *

### set\_default\_job\_class [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_optimization_hyperparameteroptimizer/\#set_default_job_class "Direct link to set_default_job_class")

**set\_default\_job\_class(job\_class)**

Set the Job class to use when the optimizer spawns new Jobs.

- **Parameters**

**job\_class** ( [_ClearmlJob_](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob#clearml.automation.ClearmlJob)) – The Job Class type.

- **Return type**

`None`


* * *

### set\_report\_period [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_optimization_hyperparameteroptimizer/\#set_report_period "Direct link to set_report_period")

**set\_report\_period(report\_period\_minutes)**

Set reporting period for the accumulated objective report (minutes). This report is sent on the Optimizer Task,
and collects the Objective metric from all running jobs.

- **Parameters**

**report\_period\_minutes** ( _float_ ) – The reporting period (minutes). The default is once every 10 minutes.

- **Return type**

`None`


* * *

### set\_time\_limit [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_optimization_hyperparameteroptimizer/\#set_time_limit "Direct link to set_time_limit")

**set\_time\_limit(in\_minutes=None, specific\_time=None)**

Set a time limit for the HyperParameterOptimizer controller. If we reached the time limit, stop the optimization
process. If `specific_time` is provided, use it; otherwise, use the `in_minutes`.

- **Parameters**
  - **in\_minutes** ( _float_ ) – The maximum processing time from current time (minutes).

  - **specific\_time** ( _datetime_ ) – The specific date/time limit.
- **Return type**

`None`


* * *

### start [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_optimization_hyperparameteroptimizer/\#start "Direct link to start")

**start(job\_complete\_callback=None)**

Start the HyperParameterOptimizer controller. If the calling process is stopped, then the controller stops
as well.

- **Parameters**

**job\_complete\_callback** ( _Callable_ ) – Callback function, called when a job is completed.





```py
def job_complete_callback(

      job_id,                 # type: str

      objective_value,        # type: float

      objective_iteration,    # type: int

      job_parameters,         # type: dict

      top_performance_job_id  # type: str

):

      pass
```

- **Return type**

`bool`

- **Returns**

True, if the controller started. False, if the controller did not start.


* * *

### start\_locally [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_optimization_hyperparameteroptimizer/\#start_locally "Direct link to start_locally")

**start\_locally(job\_complete\_callback=None)**

Start the HyperParameterOptimizer controller completely locally. Both the optimizer task
and all spawned substasks are run on the local machine using the current environment.
If the calling process is stopped, then the controller stops as well.

- **Parameters**

**job\_complete\_callback** ( _Callable_ ) – Callback function, called when a job is completed.





```py
def job_complete_callback(

      job_id,                 # type: str

      objective_value,        # type: float

      objective_iteration,    # type: int

      job_parameters,         # type: dict

      top_performance_job_id  # type: str

):

      pass
```

- **Return type**

`bool`

- **Returns**

True, if the controller started. False, if the controller did not start.


* * *

### stop [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_optimization_hyperparameteroptimizer/\#stop "Direct link to stop")

**stop(timeout=None, wait\_for\_reporter=True)**

Stop the HyperParameterOptimizer controller and the optimization thread.

- **Parameters**
  - **timeout** ( _float_ ) – Wait timeout for the optimization thread to exit (minutes).
    The default is `None`, indicating do not wait to terminate immediately.

  - **wait\_for\_reporter** (`Optional`\[`bool`\]) – Wait for reporter to flush data.
- **Return type**

`None`


* * *

### wait [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_optimization_hyperparameteroptimizer/\#wait "Direct link to wait")

**wait(timeout=None)**

Wait for the optimizer to finish.

info

This method does not stop the optimizer. Call stop to terminate the optimizer.

- **Parameters**

**timeout** ( _float_ ) – The timeout to wait for the optimization to complete (minutes).
If `None`, then wait until we reached the timeout, or optimization completed.

- **Return type**

`bool`

- **Returns**

True, if the optimization finished. False, if the optimization timed out.


- [_class_ automation.HyperParameterOptimizer(base\_task\_id, hyper\_parameters, objective\_metric\_title, objective\_metric\_series, objective\_metric\_sign='min', optimizer\_class=<class 'clearml.automation.optimization.RandomSearch'>, max\_number\_of\_concurrent\_tasks=10, execution\_queue='default', optimization\_time\_limit=None, compute\_time\_limit=None, auto\_connect\_task=True, always\_create\_task=False, spawn\_project=None, save\_top\_k\_tasks\_only=None, \*\*optimizer\_kwargs)](https://clear.ml/docs/latest/docs/references/sdk/hpo_optimization_hyperparameteroptimizer/#class-automationhyperparameteroptimizerbase_task_id-hyper_parameters-objective_metric_title-objective_metric_series-objective_metric_signmin-optimizer_classclass-clearmlautomationoptimizationrandomsearch-max_number_of_concurrent_tasks10-execution_queuedefault-optimization_time_limitnone-compute_time_limitnone-auto_connect_tasktrue-always_create_taskfalse-spawn_projectnone-save_top_k_tasks_onlynone-optimizer_kwargs)
  - [elapsed](https://clear.ml/docs/latest/docs/references/sdk/hpo_optimization_hyperparameteroptimizer/#elapsed)
  - [get\_active\_experiments](https://clear.ml/docs/latest/docs/references/sdk/hpo_optimization_hyperparameteroptimizer/#get_active_experiments)
  - [get\_num\_active\_experiments](https://clear.ml/docs/latest/docs/references/sdk/hpo_optimization_hyperparameteroptimizer/#get_num_active_experiments)
  - [get\_optimizer](https://clear.ml/docs/latest/docs/references/sdk/hpo_optimization_hyperparameteroptimizer/#get_optimizer)
  - [HyperParameterOptimizer.get\_optimizer\_top\_experiments](https://clear.ml/docs/latest/docs/references/sdk/hpo_optimization_hyperparameteroptimizer/#hyperparameteroptimizerget_optimizer_top_experiments)
  - [get\_time\_limit](https://clear.ml/docs/latest/docs/references/sdk/hpo_optimization_hyperparameteroptimizer/#get_time_limit)
  - [get\_top\_experiments](https://clear.ml/docs/latest/docs/references/sdk/hpo_optimization_hyperparameteroptimizer/#get_top_experiments)
  - [get\_top\_experiments\_details](https://clear.ml/docs/latest/docs/references/sdk/hpo_optimization_hyperparameteroptimizer/#get_top_experiments_details)
  - [is\_active](https://clear.ml/docs/latest/docs/references/sdk/hpo_optimization_hyperparameteroptimizer/#is_active)
  - [is\_running](https://clear.ml/docs/latest/docs/references/sdk/hpo_optimization_hyperparameteroptimizer/#is_running)
  - [reached\_time\_limit](https://clear.ml/docs/latest/docs/references/sdk/hpo_optimization_hyperparameteroptimizer/#reached_time_limit)
  - [set\_default\_job\_class](https://clear.ml/docs/latest/docs/references/sdk/hpo_optimization_hyperparameteroptimizer/#set_default_job_class)
  - [set\_report\_period](https://clear.ml/docs/latest/docs/references/sdk/hpo_optimization_hyperparameteroptimizer/#set_report_period)
  - [set\_time\_limit](https://clear.ml/docs/latest/docs/references/sdk/hpo_optimization_hyperparameteroptimizer/#set_time_limit)
  - [start](https://clear.ml/docs/latest/docs/references/sdk/hpo_optimization_hyperparameteroptimizer/#start)
  - [start\_locally](https://clear.ml/docs/latest/docs/references/sdk/hpo_optimization_hyperparameteroptimizer/#start_locally)
  - [stop](https://clear.ml/docs/latest/docs/references/sdk/hpo_optimization_hyperparameteroptimizer/#stop)
  - [wait](https://clear.ml/docs/latest/docs/references/sdk/hpo_optimization_hyperparameteroptimizer/#wait)