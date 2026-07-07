---
url: "https://clear.ml/docs/latest/docs/integrations/optuna/"
title: "Optuna | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/integrations/optuna/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

[Optuna](https://optuna.readthedocs.io/en/latest) is a [hyperparameter optimization](https://clear.ml/docs/latest/docs/getting_started/hpo) framework,
which makes use of different samplers such as grid search, random, bayesian, and evolutionary algorithms. You can integrate
Optuna into ClearML's automated hyperparameter optimization.

The [HyperParameterOptimizer](https://clear.ml/docs/latest/docs/references/sdk/hpo_optimization_hyperparameteroptimizer) class contains ClearML's
hyperparameter optimization modules. Its modular design enables using different optimizers, including existing software
frameworks, like Optuna, enabling simple,
accurate, and fast hyperparameter optimization. The Optuna ( [`automation.optuna.OptimizerOptuna`](https://clear.ml/docs/latest/docs/references/sdk/hpo_optuna_optuna_optimizeroptuna))
optimizer lets you simultaneously optimize many hyperparameters efficiently by relying on early stopping (pruning)
and smart resource allocation.

To use Optuna in ClearML's hyperparameter optimization, you must first install it. When you instantiate `HyperParameterOptimizer`,
pass `OptimizerOptuna` as the `optimizer_class` argument:

```python
from clearml.automation import (

    DiscreteParameterRange, HyperParameterOptimizer, UniformIntegerParameterRange

)

from clearml.automation.optuna import OptimizerOptuna

an_optimizer = HyperParameterOptimizer(

    # This is the task we want to optimize

    base_task_id=args['template_task_id'],

    hyper_parameters=[\
\
        UniformIntegerParameterRange('layer_1', min_value=128, max_value=512, step_size=128),\
\
        DiscreteParameterRange('batch_size', values=[96, 128, 160]),\
\
        DiscreteParameterRange('epochs', values=[30]),\
\
        ],

    objective_metric_title='validation',

    objective_metric_series='accuracy',

    objective_metric_sign='max',

    max_number_of_concurrent_tasks=2,

    optimizer_class=OptimizerOptuna, # input optuna as search strategy

    execution_queue='1xGPU',

    total_max_jobs=10,

)
```

See the Hyperparameter Optimization [tutorial](https://clear.ml/docs/latest/docs/guides/optimization/hyper-parameter-optimization/examples_hyperparam_opt).