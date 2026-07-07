---
url: "https://clear.ml/docs/latest/docs/clearml_sdk/hpo_sdk/"
title: "Hyperparameter Optimization | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/clearml_sdk/hpo_sdk/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

You can automate and boost hyperparameter optimization (HPO) with ClearML's
[**`HyperParameterOptimizer`**](https://clear.ml/docs/latest/docs/references/sdk/hpo_optimization_hyperparameteroptimizer) class, which takes care of the entire optimization process
with a simple interface.

ClearML's approach to hyperparameter optimization is scalable, easy to set up and to manage, and it makes it easy to
compare results.

### Workflow [​](https://clear.ml/docs/latest/docs/clearml_sdk/hpo_sdk/\#workflow "Direct link to Workflow")

![Hyperparameter optimization diagram](https://clear.ml/docs/latest/assets/images/hpo_diagram-7548a76a2d64872924972399e7ddc526.png)

The preceding diagram demonstrates the typical flow of hyperparameter optimization where the parameters of a base task are optimized:

1. Configure an Optimization Task with a base task whose parameters will be optimized, optimization targets, and a set of parameter values to
test
2. Clone the base task. Each clone's parameter is overridden with a value from the optimization task
3. Enqueue each clone for execution by a ClearML Agent
4. The Optimization Task records and monitors the cloned tasks' configuration and execution details, and returns a
summary of the optimization results in tabular and parallel coordinate formats, and in a scalar plot.

![Optimization results summary chart](https://clear.ml/docs/latest/assets/images/fundamentals_hpo_summary-e270f1e2afce71008e1acfe05800a16f.png#light-mode-only)![Optimization results summary chart](https://clear.ml/docs/latest/assets/images/fundamentals_hpo_summary_dark-3ebd93131c9f54a2caf3f91b402d8d98.png#dark-mode-only)

Parallel coordinate and scalar plots

![Parallel Coordinates](https://clear.ml/docs/latest/assets/images/fundamentals_hpo_parallel_coordinates-53dd9fd8b3c40f162c938667117b35a4.png#light-mode-only)![Parallel Coordinates](https://clear.ml/docs/latest/assets/images/fundamentals_hpo_parallel_coordinates_dark-6f72b7c4df7c2ce576d1bfdbf79a53d0.png#dark-mode-only)

![Scalars](https://clear.ml/docs/latest/assets/images/fundamentals_hpo_scalars-de9a6c1340ddb00b01cfc163cc6489e0.png#light-mode-only)![Scalars](https://clear.ml/docs/latest/assets/images/fundamentals_hpo_scalars_dark-ab224668f5972c70fd991aa0d4a7ba6a.png#dark-mode-only)

### Supported Optimizers [​](https://clear.ml/docs/latest/docs/clearml_sdk/hpo_sdk/\#supported-optimizers "Direct link to Supported Optimizers")

The `HyperParameterOptimizer` class contains ClearML's hyperparameter optimization modules. Its modular design enables
using different optimizers, including existing software frameworks, enabling simple, accurate, and fast hyperparameter
optimization.

- **Optuna** \- [`automation.optuna.OptimizerOptuna`](https://clear.ml/docs/latest/docs/references/sdk/hpo_optuna_optuna_optimizeroptuna). Optuna is the default optimizer in ClearML. It makes use of
different samplers such as grid search, random, bayesian, and evolutionary algorithms.
For more information, see the [Optuna](https://optuna.readthedocs.io/en/latest/)
documentation.
- **BOHB** \- [`automation.hpbandster.OptimizerBOHB`](https://clear.ml/docs/latest/docs/references/sdk/hpo_hpbandster_bandster_optimizerbohb). BOHB performs robust and efficient hyperparameter optimization
at scale by combining the speed of Hyperband searches with the guidance and guarantees of convergence of Bayesian Optimization.
For more information about HpBandSter BOHB, see the [HpBandSter](https://automl.github.io/HpBandSter/build/html/index.html)
documentation and a [code example](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/image/hyperparameter_search).
- **Random** uniform sampling of hyperparameters - [`automation.RandomSearch`](https://clear.ml/docs/latest/docs/references/sdk/hpo_optimization_randomsearch).
- **Full grid** sampling strategy of every hyperparameter combination - [`automation.GridSearch`](https://clear.ml/docs/latest/docs/references/sdk/hpo_optimization_gridsearch).
- **Custom** \- [`automation.optimization.SearchStrategy`](https://github.com/clearml/clearml/blob/master/clearml/automation/optimization.py#L295) \- Use a custom class and inherit from the ClearML automation base strategy class.

## Defining a Hyperparameter Optimization Search Example [​](https://clear.ml/docs/latest/docs/clearml_sdk/hpo_sdk/\#defining-a-hyperparameter-optimization-search-example "Direct link to Defining a Hyperparameter Optimization Search Example")

1. Import ClearML's automation modules:





```python
from clearml.automation import UniformParameterRange, UniformIntegerParameterRange

from clearml.automation import HyperParameterOptimizer

from clearml.automation.optuna import OptimizerOptuna
```

2. Initialize the Task, which will be stored in ClearML Server when the code runs. After the code runs at least once,
it can be reproduced, and the parameters can be tuned:





```python
from clearml import Task



task = Task.init(

       project_name='Hyperparameter Optimization',

       task_name='Automatic Hyperparameter Optimization',

       task_type=Task.TaskTypes.optimizer,

       reuse_last_task_id=False

)
```

3. Define the optimization configuration and resources budget:





```python
optimizer = HyperParameterOptimizer(

         # specifying the task to be optimized, task must be in system already so it can be cloned

         base_task_id=TEMPLATE_TASK_ID,

         # setting the hyperparameters to optimize

         hyper_parameters=[\
\
             UniformIntegerParameterRange('number_of_epochs', min_value=2, max_value=12, step_size=2),\
\
             UniformIntegerParameterRange('batch_size', min_value=2, max_value=16, step_size=2),\
\
             UniformParameterRange('dropout', min_value=0, max_value=0.5, step_size=0.05),\
\
             UniformParameterRange('base_lr', min_value=0.00025, max_value=0.01, step_size=0.00025),\
\
             ],

         # setting the objective metric we want to maximize/minimize

         objective_metric_title='accuracy',

         objective_metric_series='total',

         objective_metric_sign='max',



         # setting optimizer

         optimizer_class=OptimizerOptuna,



         # configuring optimization parameters

         execution_queue='default',

         max_number_of_concurrent_tasks=2,

         optimization_time_limit=60.,

         compute_time_limit=120,

         total_max_jobs=20,

         min_iteration_per_job=15000,

         max_iteration_per_job=150000,

         )
```











Locating Task ID





To locate the base task's ID, go to the task's info panel in the [WebApp](https://clear.ml/docs/latest/docs/webapp/webapp_overview). The ID appears
in the task header.







Multi-objective Optimization





If you are using the Optuna framework (see [Supported Optimizers](https://clear.ml/docs/latest/docs/clearml_sdk/hpo_sdk/#supported-optimizers)), you can list multiple optimization objectives.
When doing so, make sure the `objective_metric_title`, `objective_metric_series`, and `objective_metric_sign` lists
are the same length. Each title will be matched to its respective series and sign.



For example, the code below sets two objectives: to minimize the `validation/loss` metric and to maximize the `validation/accuracy` metric.







```python
objective_metric_title=["validation", "validation"]

objective_metric_series=["loss", "accuracy"]

objective_metric_sign=["min", "max"]
```


## Optimizer Execution Options [​](https://clear.ml/docs/latest/docs/clearml_sdk/hpo_sdk/\#optimizer-execution-options "Direct link to Optimizer Execution Options")

The `HyperParameterOptimizer` provides options to launch the optimization tasks locally or through a ClearML [queue](https://clear.ml/docs/latest/docs/fundamentals/agents_and_queues#what-is-a-queue).
Start a `HyperParameterOptimizer` instance using either [`HyperParameterOptimizer.start()`](https://clear.ml/docs/latest/docs/references/sdk/hpo_optimization_hyperparameteroptimizer#start)
or [`HyperParameterOptimizer.start_locally()`](https://clear.ml/docs/latest/docs/references/sdk/hpo_optimization_hyperparameteroptimizer#start_locally).
Both methods run the optimizer controller locally. `start()` launches the base task clones through a queue
specified when instantiating the controller, while `start_locally()` runs the tasks locally.

Remote Execution

You can also launch the optimizer controller through a queue by using [`Task.execute_remotely()`](https://clear.ml/docs/latest/docs/references/sdk/task#execute_remotely)
before starting the optimizer.

## Tutorial [​](https://clear.ml/docs/latest/docs/clearml_sdk/hpo_sdk/\#tutorial "Direct link to Tutorial")

Check out the [Hyperparameter Optimization tutorial](https://clear.ml/docs/latest/docs/guides/optimization/hyper-parameter-optimization/examples_hyperparam_opt) for a step-by-step guide.

## SDK Reference [​](https://clear.ml/docs/latest/docs/clearml_sdk/hpo_sdk/\#sdk-reference "Direct link to SDK Reference")

For detailed information, see the complete [HyperParameterOptimizer SDK reference page](https://clear.ml/docs/latest/docs/references/sdk/hpo_optimization_hyperparameteroptimizer).

- [Workflow](https://clear.ml/docs/latest/docs/clearml_sdk/hpo_sdk/#workflow)
- [Supported Optimizers](https://clear.ml/docs/latest/docs/clearml_sdk/hpo_sdk/#supported-optimizers)
- [Defining a Hyperparameter Optimization Search Example](https://clear.ml/docs/latest/docs/clearml_sdk/hpo_sdk/#defining-a-hyperparameter-optimization-search-example)
- [Optimizer Execution Options](https://clear.ml/docs/latest/docs/clearml_sdk/hpo_sdk/#optimizer-execution-options)
- [Tutorial](https://clear.ml/docs/latest/docs/clearml_sdk/hpo_sdk/#tutorial)
- [SDK Reference](https://clear.ml/docs/latest/docs/clearml_sdk/hpo_sdk/#sdk-reference)