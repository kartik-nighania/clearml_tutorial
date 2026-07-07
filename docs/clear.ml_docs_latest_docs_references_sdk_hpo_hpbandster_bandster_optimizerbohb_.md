---
url: "https://clear.ml/docs/latest/docs/references/sdk/hpo_hpbandster_bandster_optimizerbohb/"
title: "OptimizerBOHB | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/references/sdk/hpo_hpbandster_bandster_optimizerbohb/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

## _class_ automation.hpbandster.OptimizerBOHB(base\_task\_id, hyper\_parameters, objective\_metric, execution\_queue, num\_concurrent\_workers, min\_iteration\_per\_job, max\_iteration\_per\_job, total\_max\_jobs, pool\_period\_min=2.0, time\_limit\_per\_job=None, compute\_time\_limit=None, local\_port=9090, \*\*bohb\_kwargs) [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_hpbandster_bandster_optimizerbohb/\#class-automationhpbandsteroptimizerbohbbase_task_id-hyper_parameters-objective_metric-execution_queue-num_concurrent_workers-min_iteration_per_job-max_iteration_per_job-total_max_jobs-pool_period_min20-time_limit_per_jobnone-compute_time_limitnone-local_port9090-bohb_kwargs "Direct link to class-automationhpbandsteroptimizerbohbbase_task_id-hyper_parameters-objective_metric-execution_queue-num_concurrent_workers-min_iteration_per_job-max_iteration_per_job-total_max_jobs-pool_period_min20-time_limit_per_jobnone-compute_time_limitnone-local_port9090-bohb_kwargs")

Initialize a BOHB search strategy optimizer
BOHB performs robust and efficient hyperparameter optimization at scale by combining
the speed of Hyperband searches with the guidance and guarantees of convergence of Bayesian
Optimization. Instead of sampling new configurations at random,
BOHB uses kernel density estimators to select promising candidates.

```default
For reference:

@InProceedings{falkner-icml-18,

     title =        {{BOHB}: Robust and Efficient Hyperparameter Optimization at Scale},

     author =       {Falkner, Stefan and Klein, Aaron and Hutter, Frank},

     booktitle =    {Proceedings of the 35th International Conference on Machine Learning},

     pages =        {1436--1445},

     year =         {2018},

}
```

- **Parameters**
  - **base\_task\_id** ( _str_ ) – Task ID (str)

  - **hyper\_parameters** ( _list_ ) – list of Parameter objects to optimize over

  - **objective\_metric** ( _Objective_ ) – Objective metric to maximize / minimize

  - **execution\_queue** ( _str_ ) – execution queue to use for launching Tasks (experiments).

  - **num\_concurrent\_workers** ( _int_ ) – Limit number of concurrent running Tasks (machines)

  - **min\_iteration\_per\_job** ( _int_ ) – minimum number of iterations for a job to run.
    ‘iterations’ are the reported iterations for the specified objective,
    not the maximum reported iteration of the Task.

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

  - **time\_limit\_per\_job** ( _float_ ) – Optional, maximum execution time per single job in minutes,
    when time limit is exceeded job is aborted

  - **compute\_time\_limit** ( _float_ ) – The maximum compute time in minutes. When time limit is exceeded,
    all jobs aborted. (Optional)

  - **local\_port** ( _int_ ) – default port 9090 tcp, this is a must for the BOHB workers to communicate, even locally.

  - **bohb\_kwargs** (`Any`) – arguments passed directly to the BOHB object

* * *

### create\_job [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_hpbandster_bandster_optimizerbohb/\#create_job "Direct link to create_job")

**create\_job()**

Abstract helper function. Implementation is not required. Default use in process\_step default implementation
Create a new job if needed. return the newly created job. If no job needs to be created, return `None`.

- **Return type**

`Optional`\[ [`ClearmlJob`](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob#clearml.automation.ClearmlJob)\]

- **Returns**

A Newly created ClearmlJob object, or None if no ClearmlJob created.


* * *

### get\_created\_jobs\_ids [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_hpbandster_bandster_optimizerbohb/\#get_created_jobs_ids "Direct link to get_created_jobs_ids")

**get\_created\_jobs\_ids()**

Return a Task IDs dict created by this optimizer until now, including completed and running jobs.
The values of the returned dict are the parameters used in the specific job

- **Return type**

`Mapping`\[`str`, `dict`\]

- **Returns**

dict of task IDs (str) as keys, and their parameters dict as values.


* * *

### get\_created\_jobs\_tasks [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_hpbandster_bandster_optimizerbohb/\#get_created_jobs_tasks "Direct link to get_created_jobs_tasks")

**get\_created\_jobs\_tasks()**

Return a Task IDs dict created by this optimizer until now.
The values of the returned dict are the ClearmlJob.

- **Return type**

`Mapping`\[`str`, `dict`\]

- **Returns**

dict of task IDs (str) as keys, and their ClearmlJob as values.


* * *

### get\_objective\_metric [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_hpbandster_bandster_optimizerbohb/\#get_objective_metric "Direct link to get_objective_metric")

**get\_objective\_metric()**

Return the metric title, series pair of the objective.

- **Return type**

`Union`\[`Tuple`\[`str`, `str`\], `List`\[`Tuple`\[`str`, `str`\]\]\]

- **Returns**

(title, series)


* * *

### get\_random\_seed [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_hpbandster_bandster_optimizerbohb/\#get_random_seed "Direct link to get_random_seed")

**static get\_random\_seed()**

Get the global seed for all hyperparameter strategy random number sampling.

- **Return type**

`int`

- **Returns**

The random seed.


* * *

### get\_running\_jobs [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_hpbandster_bandster_optimizerbohb/\#get_running_jobs "Direct link to get_running_jobs")

**get\_running\_jobs()**

Return the current running ClearmlJob.

- **Return type**

`Sequence`\[ [`ClearmlJob`](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob#clearml.automation.ClearmlJob)\]

- **Returns**

List of ClearmlJob objects.


* * *

### get\_top\_experiments [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_hpbandster_bandster_optimizerbohb/\#get_top_experiments "Direct link to get_top_experiments")

**get\_top\_experiments(top\_k)**

Return a list of Tasks of the top performing experiments, based on the controller `Objective` object.

- **Parameters**

**top\_k** ( _int_ ) – The number of Tasks (experiments) to return.

- **Return type**

`Sequence`\[ [`Task`](https://clear.ml/docs/latest/docs/references/sdk/task#clearml.Task)\]

- **Returns**

A list of Task objects, ordered by performance, where index 0 is the best performing Task.


* * *

### get\_top\_experiments\_details [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_hpbandster_bandster_optimizerbohb/\#get_top_experiments_details "Direct link to get_top_experiments_details")

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

### get\_top\_experiments\_id\_metrics\_pair [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_hpbandster_bandster_optimizerbohb/\#get_top_experiments_id_metrics_pair "Direct link to get_top_experiments_id_metrics_pair")

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

### helper\_create\_job [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_hpbandster_bandster_optimizerbohb/\#helper_create_job "Direct link to helper_create_job")

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

### monitor\_job [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_hpbandster_bandster_optimizerbohb/\#monitor_job "Direct link to monitor_job")

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

### process\_step [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_hpbandster_bandster_optimizerbohb/\#process_step "Direct link to process_step")

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

### set\_job\_class [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_hpbandster_bandster_optimizerbohb/\#set_job_class "Direct link to set_job_class")

**set\_job\_class(job\_class)**

Set the class to use for the `helper_create_job` function.

- **Parameters**

**job\_class** ( [_ClearmlJob_](https://clear.ml/docs/latest/docs/references/sdk/automation_job_clearmljob#clearml.automation.ClearmlJob)) – The Job Class type.

- **Return type**

`None`


* * *

### set\_job\_default\_parent [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_hpbandster_bandster_optimizerbohb/\#set_job_default_parent "Direct link to set_job_default_parent")

**set\_job\_default\_parent(job\_parent\_task\_id, project\_name=None)**

Set the default parent for all Jobs created by the `helper_create_job` method.

- **Parameters**
  - **job\_parent\_task\_id** ( _str_ ) – The parent Task ID.

  - **project\_name** ( _str_ ) – If specified, create the jobs in the specified project
- **Return type**

`None`


* * *

### set\_job\_naming\_scheme [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_hpbandster_bandster_optimizerbohb/\#set_job_naming_scheme "Direct link to set_job_naming_scheme")

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

### set\_optimization\_args [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_hpbandster_bandster_optimizerbohb/\#set_optimization_args "Direct link to set_optimization_args")

**set\_optimization\_args(eta=3, min\_budget=None, max\_budget=None, min\_points\_in\_model=None, top\_n\_percent=15, num\_samples=None, random\_fraction=0.3333333333333333, bandwidth\_factor=3, min\_bandwidth=0.001)**

Defaults copied from BOHB constructor, see details in BOHB. **init**

BOHB performs robust and efficient hyperparameter optimization
at scale by combining the speed of Hyperband searches with the
guidance and guarantees of convergence of Bayesian
Optimization. Instead of sampling new configurations at random,
BOHB uses kernel density estimators to select promising candidates.

```default
For reference:

@InProceedings{falkner-icml-18,

     title =        {{BOHB}: Robust and Efficient Hyperparameter Optimization at Scale},

     author =       {Falkner, Stefan and Klein, Aaron and Hutter, Frank},

     booktitle =    {Proceedings of the 35th International Conference on Machine Learning},

     pages =        {1436--1445},

     year =         {2018},

}
```

- **Parameters**
  - **eta** (`float`) – float (3)
    In each iteration, a complete run of sequential halving is executed. In it,
    after evaluating each configuration on the same subset size, only a fraction of
    1/eta of them ‘advances’ to the next round.
    Must be greater or equal to 2.

  - **min\_budget** (`Optional`\[`float`\]) – float (0.01)
    The smallest budget to consider. Needs to be positive!

  - **max\_budget** (`Optional`\[`float`\]) – float (1)
    The largest budget to consider. Needs to be larger than min\_budget!
    The budgets will be geometrically distributed
    $a^2 + b^2 = c^2 /sim /eta^k$ for $k/in \[0, 1, ... , num/\_subsets - 1\]$.

  - **min\_points\_in\_model** (`Optional`\[`int`\]) – int (None)
    number of observations to start building a KDE. Default ‘None’ means
    dim+1, the bare minimum.

  - **top\_n\_percent** (`Optional`\[`int`\]) – int (15)
    percentage ( between 1 and 99, default 15) of the observations that are considered good.

  - **num\_samples** (`Optional`\[`int`\]) – int (64)
    number of samples to optimize EI (default 64)

  - **random\_fraction** (`Optional`\[`float`\]) – float (1/3.)
    fraction of purely random configurations that are sampled from the
    prior without the model.

  - **bandwidth\_factor** (`Optional`\[`float`\]) – float (3.)
    to encourage diversity, the points proposed to optimize EI, are sampled
    from a ‘widened’ KDE where the bandwidth is multiplied by this factor (default: 3)

  - **min\_bandwidth** (`Optional`\[`float`\]) – float (1e-3)
    to keep diversity, even when all (good) samples have the same value for one of the parameters,
    a minimum bandwidth (Default: 1e-3) is used instead of zero.
- **Return type**

`None`


* * *

### set\_optimizer\_task [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_hpbandster_bandster_optimizerbohb/\#set_optimizer_task "Direct link to set_optimizer_task")

**set\_optimizer\_task(task)**

Set the optimizer task object to be used to store/generate reports on the optimization process.
Usually this is the current task of this process.

- **Parameters**

**task** ( [_Task_](https://clear.ml/docs/latest/docs/references/sdk/task#clearml.Task)) – The optimizer\`s current Task.

- **Return type**

`None`


* * *

### set\_random\_seed [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_hpbandster_bandster_optimizerbohb/\#set_random_seed "Direct link to set_random_seed")

**static set\_random\_seed(seed=1337)**

Set global seed for all hyperparameter strategy random number sampling.

- **Parameters**

**seed** ( _int_ ) – The random seed.

- **Return type**

`None`


* * *

### start [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_hpbandster_bandster_optimizerbohb/\#start "Direct link to start")

**start()**

Start the Optimizer controller function loop()
If the calling process is stopped, the controller will stop as well.

important

This function returns only after optimization is completed or stop was called.

- **Return type**

`None`


* * *

### stop [​](https://clear.ml/docs/latest/docs/references/sdk/hpo_hpbandster_bandster_optimizerbohb/\#stop "Direct link to stop")

**stop()**

Stop the current running optimization loop,
Called from a different thread than the `start`.

- **Return type**

`None`


- [_class_ automation.hpbandster.OptimizerBOHB(base\_task\_id, hyper\_parameters, objective\_metric, execution\_queue, num\_concurrent\_workers, min\_iteration\_per\_job, max\_iteration\_per\_job, total\_max\_jobs, pool\_period\_min=2.0, time\_limit\_per\_job=None, compute\_time\_limit=None, local\_port=9090, \*\*bohb\_kwargs)](https://clear.ml/docs/latest/docs/references/sdk/hpo_hpbandster_bandster_optimizerbohb/#class-automationhpbandsteroptimizerbohbbase_task_id-hyper_parameters-objective_metric-execution_queue-num_concurrent_workers-min_iteration_per_job-max_iteration_per_job-total_max_jobs-pool_period_min20-time_limit_per_jobnone-compute_time_limitnone-local_port9090-bohb_kwargs)
  - [create\_job](https://clear.ml/docs/latest/docs/references/sdk/hpo_hpbandster_bandster_optimizerbohb/#create_job)
  - [get\_created\_jobs\_ids](https://clear.ml/docs/latest/docs/references/sdk/hpo_hpbandster_bandster_optimizerbohb/#get_created_jobs_ids)
  - [get\_created\_jobs\_tasks](https://clear.ml/docs/latest/docs/references/sdk/hpo_hpbandster_bandster_optimizerbohb/#get_created_jobs_tasks)
  - [get\_objective\_metric](https://clear.ml/docs/latest/docs/references/sdk/hpo_hpbandster_bandster_optimizerbohb/#get_objective_metric)
  - [get\_random\_seed](https://clear.ml/docs/latest/docs/references/sdk/hpo_hpbandster_bandster_optimizerbohb/#get_random_seed)
  - [get\_running\_jobs](https://clear.ml/docs/latest/docs/references/sdk/hpo_hpbandster_bandster_optimizerbohb/#get_running_jobs)
  - [get\_top\_experiments](https://clear.ml/docs/latest/docs/references/sdk/hpo_hpbandster_bandster_optimizerbohb/#get_top_experiments)
  - [get\_top\_experiments\_details](https://clear.ml/docs/latest/docs/references/sdk/hpo_hpbandster_bandster_optimizerbohb/#get_top_experiments_details)
  - [get\_top\_experiments\_id\_metrics\_pair](https://clear.ml/docs/latest/docs/references/sdk/hpo_hpbandster_bandster_optimizerbohb/#get_top_experiments_id_metrics_pair)
  - [helper\_create\_job](https://clear.ml/docs/latest/docs/references/sdk/hpo_hpbandster_bandster_optimizerbohb/#helper_create_job)
  - [monitor\_job](https://clear.ml/docs/latest/docs/references/sdk/hpo_hpbandster_bandster_optimizerbohb/#monitor_job)
  - [process\_step](https://clear.ml/docs/latest/docs/references/sdk/hpo_hpbandster_bandster_optimizerbohb/#process_step)
  - [set\_job\_class](https://clear.ml/docs/latest/docs/references/sdk/hpo_hpbandster_bandster_optimizerbohb/#set_job_class)
  - [set\_job\_default\_parent](https://clear.ml/docs/latest/docs/references/sdk/hpo_hpbandster_bandster_optimizerbohb/#set_job_default_parent)
  - [set\_job\_naming\_scheme](https://clear.ml/docs/latest/docs/references/sdk/hpo_hpbandster_bandster_optimizerbohb/#set_job_naming_scheme)
  - [set\_optimization\_args](https://clear.ml/docs/latest/docs/references/sdk/hpo_hpbandster_bandster_optimizerbohb/#set_optimization_args)
  - [set\_optimizer\_task](https://clear.ml/docs/latest/docs/references/sdk/hpo_hpbandster_bandster_optimizerbohb/#set_optimizer_task)
  - [set\_random\_seed](https://clear.ml/docs/latest/docs/references/sdk/hpo_hpbandster_bandster_optimizerbohb/#set_random_seed)
  - [start](https://clear.ml/docs/latest/docs/references/sdk/hpo_hpbandster_bandster_optimizerbohb/#start)
  - [stop](https://clear.ml/docs/latest/docs/references/sdk/hpo_hpbandster_bandster_optimizerbohb/#stop)