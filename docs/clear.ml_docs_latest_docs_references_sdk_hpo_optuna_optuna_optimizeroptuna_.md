---
url: "https://clear.ml/docs/latest/docs/references/sdk/hpo_optuna_optuna_optimizeroptuna/"
title: "OptimizerOptuna | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/sdk/hpo_optuna_optuna_optimizeroptuna/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

## _class_ automation.optuna.OptimizerOptuna(base\_task\_id, hyper\_parameters, objective\_metric, execution\_queue, num\_concurrent\_workers, max\_iteration\_per\_job, total\_max\_jobs, pool\_period\_min=2.0, min\_iteration\_per\_job=None, time\_limit\_per\_job=None, compute\_time\_limit=None, optuna\_sampler=None, optuna\_pruner=None, continue\_previous\_study=None, \*\*optuna\_kwargs) [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_optuna_optuna_optimizeroptuna/\#class-automationoptunaoptimizeroptunabase_task_id-hyper_parameters-objective_metric-execution_queue-num_concurrent_workers-max_iteration_per_job-total_max_jobs-pool_period_min20-min_iteration_per_jobnone-time_limit_per_jobnone-compute_time_limitnone-optuna_samplernone-optuna_prunernone-continue_previous_studynone-optuna_kwargs "Direct link to class-automationoptunaoptimizeroptunabase_task_id-hyper_parameters-objective_metric-execution_queue-num_concurrent_workers-max_iteration_per_job-total_max_jobs-pool_period_min20-min_iteration_per_jobnone-time_limit_per_jobnone-compute_time_limitnone-optuna_samplernone-optuna_prunernone-continue_previous_studynone-optuna_kwargs")

Initialize an Optuna search strategy optimizer
Optuna performs robust and efficient hyperparameter optimization at scale by combining.
Specific hyperparameter pruning strategy can be selected via sampler and pruner arguments

- **Parameters**
  - **base\_task\_id** ( _str_ ) – Task ID (str)

  - **hyper\_parameters** ( _list_ ) – list of Parameter objects to optimize over

  - **objective\_metric** ( _Objective_ ) – Objective metric to maximize / minimize

  - **execution\_queue** ( _str_ ) – execution queue to use for launching Tasks (experiments).

  - **num\_concurrent\_workers** ( _int_ ) – Limit number of concurrent running Tasks (machines)

  - **max\_iteration\_per\_job** ( _int_ ) – number of iteration per job
    ‘iterations’ are the reported iterations for the specified objective,
    not the maximum reported iteration of the Task.

  - **total\_max\_jobs** ( _int_ ) – total maximum job for the optimization process.
    Must be provided in order to calculate the total budget for the optimization process.
    The total budget is measured by “iterations” (see above)
    and will be set to max\_iteration\_per\_job \* total\_max\_jobs
    This means more than total\_max\_jobs could be created, as long as the cumulative iterations
    (summed over all created jobs) will not exceed max\_iteration\_per\_job \* total\_max\_jobs

  - **pool\_period\_min** ( _float_ ) – time in minutes between two consecutive pools

  - **min\_iteration\_per\_job** ( _int_ ) – The minimum number of iterations (of the Objective metric) per single job,
    before early stopping the Job. (Optional)

  - **time\_limit\_per\_job** ( _float_ ) – Optional, maximum execution time per single job in minutes,
    when time limit is exceeded job is aborted

  - **compute\_time\_limit** ( _float_ ) – The maximum compute time in minutes. When time limit is exceeded,
    all jobs aborted. (Optional)

  - **optuna\_kwargs** (`Any`) – arguments passed directly to the Optuna object

  - **optuna\_sampler** ( _Optional_ _\[_ _Any_ _\]_ ) –

  - **optuna\_pruner** ( _Optional_ _\[_ _Any_ _\]_ ) –

  - **continue\_previous\_study** ( _Optional_ _\[_ _Study_ _\]_ ) –

* * *

### create\_job [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_optuna_optuna_optimizeroptuna/\#create_job "Direct link to create_job")

**create\_job()**

Abstract helper function. Implementation is not required. Default use in process\_step default implementation
Create a new job if needed. return the newly created job. If no job needs to be created, return `None`.

- **Return type**

`Optional`\[ [`ClearmlJob`](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob#clearml.automation.ClearmlJob)\]

- **Returns**

A Newly created ClearmlJob object, or None if no ClearmlJob created.


* * *

### get\_created\_jobs\_ids [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_optuna_optuna_optimizeroptuna/\#get_created_jobs_ids "Direct link to get_created_jobs_ids")

**get\_created\_jobs\_ids()**

Return a Task IDs dict created by this optimizer until now, including completed and running jobs.
The values of the returned dict are the parameters used in the specific job

- **Return type**

`Mapping`\[`str`, `dict`\]

- **Returns**

dict of task IDs (str) as keys, and their parameters dict as values.


* * *

### get\_created\_jobs\_tasks [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_optuna_optuna_optimizeroptuna/\#get_created_jobs_tasks "Direct link to get_created_jobs_tasks")

**get\_created\_jobs\_tasks()**

Return a Task IDs dict created by this optimizer until now.
The values of the returned dict are the ClearmlJob.

- **Return type**

`Mapping`\[`str`, `dict`\]

- **Returns**

dict of task IDs (str) as keys, and their ClearmlJob as values.


* * *

### get\_objective\_metric [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_optuna_optuna_optimizeroptuna/\#get_objective_metric "Direct link to get_objective_metric")

**get\_objective\_metric()**

Return the metric title, series pair of the objective.

- **Return type**

`Union`\[`Tuple`\[`str`, `str`\], `List`\[`Tuple`\[`str`, `str`\]\]\]

- **Returns**

(title, series)


* * *

### get\_running\_jobs [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_optuna_optuna_optimizeroptuna/\#get_running_jobs "Direct link to get_running_jobs")

**get\_running\_jobs()**

Return the current running ClearmlJob.

- **Return type**

`Sequence`\[ [`ClearmlJob`](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob#clearml.automation.ClearmlJob)\]

- **Returns**

List of ClearmlJob objects.


* * *

### get\_top\_experiments [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_optuna_optuna_optimizeroptuna/\#get_top_experiments "Direct link to get_top_experiments")

**get\_top\_experiments(top\_k)**

Return a list of Tasks of the top performing experiments, based on the controller `Objective` object.

- **Parameters**

**top\_k** ( _int_ ) – The number of Tasks (experiments) to return.

- **Return type**

`Sequence`\[ [`Task`](https://clear.ml/docs/latest/docs/references/sdk/task#clearml.Task)\]

- **Returns**

A list of Task objects, ordered by performance, where index 0 is the best performing Task.


* * *

### get\_top\_experiments\_details [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_optuna_optuna_optimizeroptuna/\#get_top_experiments_details "Direct link to get_top_experiments_details")

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

### get\_top\_experiments\_id\_metrics\_pair [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_optuna_optuna_optimizeroptuna/\#get_top_experiments_id_metrics_pair "Direct link to get_top_experiments_id_metrics_pair")

**get\_top\_experiments\_id\_metrics\_pair(top\_k, all\_metrics=False, only\_completed=False)**

Return a list of pairs (Task ID, scalar metric dict) of the top performing experiments.
Order is based on the controller `Objective` object.

- **Parameters**
  - **top\_k** ( _int_ ) – The number of Tasks (experiments) to return.

  - **all\_metrics** (`bool`) – Default False, only return the objective metric on the metrics dictionary.
    If True, return all scalar metrics of the experiment

  - **only\_completed** (`bool`) – return only completed Tasks. Default False.
- **Return type**

`Sequence`\[`Union`\[`str`, `dict`\]\]

- **Returns**

A list of pairs (Task ID, metric values dict), ordered by performance,


where index 0 is the best performing Task.
Example w/ all\_metrics=False:

```py
[\
\
    ('0593b76dc7234c65a13a301f731958fa',\
\
        {\
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
    ),\
\
]
```

Example w/ all\_metrics=True:

```py
[\
\
    ('0593b76dc7234c65a13a301f731958fa',\
\
        {\
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
    ),\
\
]
```

* * *

### helper\_create\_job [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_optuna_optuna_optimizeroptuna/\#helper_create_job "Direct link to helper_create_job")

**helper\_create\_job(base\_task\_id, parameter\_override=None, task\_overrides=None, tags=None, parent=None, \*\*kwargs)**

Create a Job using the specified arguments, `ClearmlJob` for details.

- **Return type**

[`ClearmlJob`](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob#clearml.automation.ClearmlJob)

- **Returns**

A newly created Job instance.

- **Parameters**
  - **base\_task\_id** ( _str_ ) –

  - **parameter\_override** ( _Optional_ _\[_ _Mapping_ _\[_ _str_ \\*, \\* _str_ _\]_ _\]_ ) –

  - **task\_overrides** ( _Optional_ _\[_ _Mapping_ _\[_ _str_ \\*, \\* _str_ _\]_ _\]_ ) –

  - **tags** ( _Optional_ _\[_ _Sequence_ _\[_ _str_ _\]_ _\]_ ) –

  - **parent** ( _Optional_ _\[_ _str_ _\]_ ) –

  - **kwargs** ( _Any_ ) –

* * *

### monitor\_job [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_optuna_optuna_optimizeroptuna/\#monitor_job "Direct link to monitor_job")

**monitor\_job(job)**

Helper function, Implementation is not required. Default use in process\_step default implementation.
Check if the job needs to be aborted or already completed.

If returns `False`, the job was aborted / completed, and should be taken off the current job list.

If there is a budget limitation, this call should update
`self.budget.compute_time.update` / `self.budget.iterations.update`

- **Parameters**

**job** ( [_ClearmlJob_](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob#clearml.automation.ClearmlJob)) – A `ClearmlJob` object to monitor.

- **Return type**

`bool`

- **Returns**

False, if the job is no longer relevant.


* * *

### process\_step [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_optuna_optuna_optimizeroptuna/\#process_step "Direct link to process_step")

**process\_step()**

Abstract helper function. Implementation is not required. Default use in start default implementation
Main optimization loop, called from the daemon thread created by `start`.

- Call monitor job on every `ClearmlJob` in jobs:
  - Check the performance or elapsed time, and then decide whether to kill the jobs.
- Call create\_job:
  - Check if spare job slots exist, and if they do call create a new job based on previous tested experiments.

- **Return type**

`bool`

- **Returns**

True, if continue the optimization. False, if immediately stop.


* * *

### set\_job\_class [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_optuna_optuna_optimizeroptuna/\#set_job_class "Direct link to set_job_class")

**set\_job\_class(job\_class)**

Set the class to use for the `helper_create_job` function.

- **Parameters**

**job\_class** ( [_ClearmlJob_](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob#clearml.automation.ClearmlJob)) – The Job Class type.

- **Return type**

`None`


* * *

### set\_job\_default\_parent [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_optuna_optuna_optimizeroptuna/\#set_job_default_parent "Direct link to set_job_default_parent")

**set\_job\_default\_parent(job\_parent\_task\_id, project\_name=None)**

Set the default parent for all Jobs created by the `helper_create_job` method.

- **Parameters**
  - **job\_parent\_task\_id** ( _str_ ) – The parent Task ID.

  - **project\_name** ( _str_ ) – If specified, create the jobs in the specified project
- **Return type**

`None`


* * *

### set\_job\_naming\_scheme [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_optuna_optuna_optimizeroptuna/\#set_job_naming_scheme "Direct link to set_job_naming_scheme")

**set\_job\_naming\_scheme(naming\_function)**

Set the function used to name a newly created job.

- **Parameters**

**naming\_function** ( _callable_ ) – Callable function for naming a newly created job.
Use the following format:





```py
naming_functor(base_task_name, argument_dict) -&gt; str
```

- **Return type**

`None`


* * *

### set\_optimizer\_task [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_optuna_optuna_optimizeroptuna/\#set_optimizer_task "Direct link to set_optimizer_task")

**set\_optimizer\_task(task)**

Set the optimizer task object to be used to store/generate reports on the optimization process.
Usually this is the current task of this process.

- **Parameters**

**task** ( [_Task_](https://clear.ml/docs/latest/docs/references/sdk/task#clearml.Task)) – The optimizer\`s current Task.

- **Return type**

`None`


* * *

### start [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_optuna_optuna_optimizeroptuna/\#start "Direct link to start")

**start()**

Start the Optimizer controller function loop()
If the calling process is stopped, the controller will stop as well.

important

This function returns only after optimization is completed or stop was called.

- **Return type**

`None`


* * *

### stop [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_optuna_optuna_optimizeroptuna/\#stop "Direct link to stop")

**stop()**

Stop the current running optimization loop,
Called from a different thread than the `start`.

- **Return type**

`None`


- [_class_ automation.optuna.OptimizerOptuna(base\_task\_id, hyper\_parameters, objective\_metric, execution\_queue, num\_concurrent\_workers, max\_iteration\_per\_job, total\_max\_jobs, pool\_period\_min=2.0, min\_iteration\_per\_job=None, time\_limit\_per\_job=None, compute\_time\_limit=None, optuna\_sampler=None, optuna\_pruner=None, continue\_previous\_study=None, \*\*optuna\_kwargs)](https://clear.ml/docs/latest/docs/references/sdk/hpo_optuna_optuna_optimizeroptuna/#class-automationoptunaoptimizeroptunabase_task_id-hyper_parameters-objective_metric-execution_queue-num_concurrent_workers-max_iteration_per_job-total_max_jobs-pool_period_min20-min_iteration_per_jobnone-time_limit_per_jobnone-compute_time_limitnone-optuna_samplernone-optuna_prunernone-continue_previous_studynone-optuna_kwargs)
  - [create\_job](https://clear.ml/docs/latest/docs/references/sdk/hpo_optuna_optuna_optimizeroptuna/#create_job)
  - [get\_created\_jobs\_ids](https://clear.ml/docs/latest/docs/references/sdk/hpo_optuna_optuna_optimizeroptuna/#get_created_jobs_ids)
  - [get\_created\_jobs\_tasks](https://clear.ml/docs/latest/docs/references/sdk/hpo_optuna_optuna_optimizeroptuna/#get_created_jobs_tasks)
  - [get\_objective\_metric](https://clear.ml/docs/latest/docs/references/sdk/hpo_optuna_optuna_optimizeroptuna/#get_objective_metric)
  - [get\_running\_jobs](https://clear.ml/docs/latest/docs/references/sdk/hpo_optuna_optuna_optimizeroptuna/#get_running_jobs)
  - [get\_top\_experiments](https://clear.ml/docs/latest/docs/references/sdk/hpo_optuna_optuna_optimizeroptuna/#get_top_experiments)
  - [get\_top\_experiments\_details](https://clear.ml/docs/latest/docs/references/sdk/hpo_optuna_optuna_optimizeroptuna/#get_top_experiments_details)
  - [get\_top\_experiments\_id\_metrics\_pair](https://clear.ml/docs/latest/docs/references/sdk/hpo_optuna_optuna_optimizeroptuna/#get_top_experiments_id_metrics_pair)
  - [helper\_create\_job](https://clear.ml/docs/latest/docs/references/sdk/hpo_optuna_optuna_optimizeroptuna/#helper_create_job)
  - [monitor\_job](https://clear.ml/docs/latest/docs/references/sdk/hpo_optuna_optuna_optimizeroptuna/#monitor_job)
  - [process\_step](https://clear.ml/docs/latest/docs/references/sdk/hpo_optuna_optuna_optimizeroptuna/#process_step)
  - [set\_job\_class](https://clear.ml/docs/latest/docs/references/sdk/hpo_optuna_optuna_optimizeroptuna/#set_job_class)
  - [set\_job\_default\_parent](https://clear.ml/docs/latest/docs/references/sdk/hpo_optuna_optuna_optimizeroptuna/#set_job_default_parent)
  - [set\_job\_naming\_scheme](https://clear.ml/docs/latest/docs/references/sdk/hpo_optuna_optuna_optimizeroptuna/#set_job_naming_scheme)
  - [set\_optimizer\_task](https://clear.ml/docs/latest/docs/references/sdk/hpo_optuna_optuna_optimizeroptuna/#set_optimizer_task)
  - [start](https://clear.ml/docs/latest/docs/references/sdk/hpo_optuna_optuna_optimizeroptuna/#start)
  - [stop](https://clear.ml/docs/latest/docs/references/sdk/hpo_optuna_optuna_optimizeroptuna/#stop)