---
url: "https://clear.ml/docs/latest/docs/guides/frameworks/tensorflow/integration_keras_tuner/"
title: "Keras Tuner | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/frameworks/tensorflow/integration_keras_tuner/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

tip

If you are not already using ClearML, see [ClearML Setup instructions](https://clear.ml/docs/latest/docs/clearml_sdk/clearml_sdk_setup).

Integrate ClearML into code that uses [Keras Tuner](https://www.tensorflow.org/tutorials/keras/keras_tuner). By
specifying `ClearMLTunerLogger` (see [kerastuner.py](https://github.com/clearml/clearml/blob/master/clearml/external/kerastuner.py))
as the Keras Tuner logger, ClearML automatically logs scalars and hyperparameter optimization.

## ClearMLTunerLogger [​](https://clear.ml/docs/latest/docs/guides/frameworks/tensorflow/integration_keras_tuner/\#clearmltunerlogger "Direct link to ClearMLTunerLogger")

Take a look at [keras\_tuner\_cifar.py](https://github.com/clearml/clearml/blob/master/examples/frameworks/kerastuner/keras_tuner_cifar.py)
example script, which demonstrates the integration of ClearML in a code that uses Keras Tuner.

The script does the following:

1. Creates a `Hyperband` object, which uses Keras Tuner's `Hyperband` tuner. It finds the best hyperparameters to train a
network on a CIFAR-10 dataset.
2. When the `Hyperband` object is created, instantiates a `ClearMLTunerLogger` object and assigns it to the `Hyperband` logger.
The `ClearMLTunerLogger` class provides the required binding for ClearML automatic logging.

```python
tuner = kt.Hyperband(

    build_model,

    project_name='kt examples',

    logger=ClearMLTunerLogger(),

    objective='val_accuracy',

    max_epochs=10,

    hyperband_iterations=6

)
```

When the script runs, it logs:

- Tabular summary of hyperparameters tested and their metrics by trial ID
- Scalar plot showing metrics for all runs
- Summary plot
- Output model with configuration and snapshot location.

## Scalars [​](https://clear.ml/docs/latest/docs/guides/frameworks/tensorflow/integration_keras_tuner/\#scalars "Direct link to Scalars")

ClearML logs the scalars from training each network. They appear in the task's page in the **ClearML web UI**, under
**SCALARS**.

![Scalars](https://clear.ml/docs/latest/assets/images/integration_keras_tuner_06-8ca4e2c20b5b51b9a0e23c0c7ac4ef29.png#light-mode-only)![Scalars](https://clear.ml/docs/latest/assets/images/integration_keras_tuner_06_dark-e1ef64aeef29eed4e387c8f899b90f4f.png#dark-mode-only)

## Summary of Hyperparameter Optimization [​](https://clear.ml/docs/latest/docs/guides/frameworks/tensorflow/integration_keras_tuner/\#summary-of-hyperparameter-optimization "Direct link to Summary of Hyperparameter Optimization")

ClearML automatically logs the parameters of each task run in the hyperparameter search. They appear in tabular
form in **PLOTS**.

![HPO summary plot](https://clear.ml/docs/latest/assets/images/integration_keras_tuner_07-936198be54e00d4e855732ae6a903f82.png#light-mode-only)![HPO summary plot](https://clear.ml/docs/latest/assets/images/integration_keras_tuner_07_dark-fdd1e9689b2be1ebd01619717282e422.png#dark-mode-only)

## Artifacts [​](https://clear.ml/docs/latest/docs/guides/frameworks/tensorflow/integration_keras_tuner/\#artifacts "Direct link to Artifacts")

ClearML automatically stores the output model. It appears in **ARTIFACTS** **>** **Output Model**.

![Artifact](https://clear.ml/docs/latest/assets/images/integration_keras_tuner_03-7f8b47c41edaed5c2b3ca88b1fd20b95.png#light-mode-only)![Artifact](https://clear.ml/docs/latest/assets/images/integration_keras_tuner_03_dark-d260c1ffe2431a34008416865fcd517e.png#dark-mode-only)

Model details, such as snap locations, appear in the **MODELS** tab.

![Model details](https://clear.ml/docs/latest/assets/images/integration_keras_tuner_04-24fd75567a44d6175819040f967f6deb.png#light-mode-only)![Model details](https://clear.ml/docs/latest/assets/images/integration_keras_tuner_04_dark-9829c554f9ab59f170b5513ca1cd4d88.png#dark-mode-only)

The model configuration is stored with the model.

![Model configuration](https://clear.ml/docs/latest/assets/images/integration_keras_tuner_05-4f46dfe5310f85471fee85ea23310b87.png#light-mode-only)![Model configuration](https://clear.ml/docs/latest/assets/images/integration_keras_tuner_05_dark-15f297cb305cf2a6d946dba3a038efd4.png#dark-mode-only)

## Configuration Objects [​](https://clear.ml/docs/latest/docs/guides/frameworks/tensorflow/integration_keras_tuner/\#configuration-objects "Direct link to Configuration Objects")

### Hyperparameters [​](https://clear.ml/docs/latest/docs/guides/frameworks/tensorflow/integration_keras_tuner/\#hyperparameters "Direct link to Hyperparameters")

ClearML automatically logs the TensorFlow Definitions, which appear in **CONFIGURATION** **>** **HYPERPARAMETERS**.

![Hyperparameters](https://clear.ml/docs/latest/assets/images/integration_keras_tuner_01-a80785466eab49da19b3578781c741d0.png#light-mode-only)![Hyperparameters](https://clear.ml/docs/latest/assets/images/integration_keras_tuner_01_dark-6287c67e5615f5a4219db71cf073a4aa.png#dark-mode-only)

### Configuration [​](https://clear.ml/docs/latest/docs/guides/frameworks/tensorflow/integration_keras_tuner/\#configuration "Direct link to Configuration")

The Task configuration appears in **CONFIGURATION** **>** **General**.

![Configuration object](https://clear.ml/docs/latest/assets/images/integration_keras_tuner_02-7cc61026f0be10e8a70c2f737cc19829.png#light-mode-only)![Configuration object](https://clear.ml/docs/latest/assets/images/integration_keras_tuner_02_dark-3f02489f1c4a5d2fa86143930a35ab41.png#dark-mode-only)

- [ClearMLTunerLogger](https://clear.ml/docs/latest/docs/guides/frameworks/tensorflow/integration_keras_tuner/#clearmltunerlogger)
- [Scalars](https://clear.ml/docs/latest/docs/guides/frameworks/tensorflow/integration_keras_tuner/#scalars)
- [Summary of Hyperparameter Optimization](https://clear.ml/docs/latest/docs/guides/frameworks/tensorflow/integration_keras_tuner/#summary-of-hyperparameter-optimization)
- [Artifacts](https://clear.ml/docs/latest/docs/guides/frameworks/tensorflow/integration_keras_tuner/#artifacts)
- [Configuration Objects](https://clear.ml/docs/latest/docs/guides/frameworks/tensorflow/integration_keras_tuner/#configuration-objects)
  - [Hyperparameters](https://clear.ml/docs/latest/docs/guides/frameworks/tensorflow/integration_keras_tuner/#hyperparameters)
  - [Configuration](https://clear.ml/docs/latest/docs/guides/frameworks/tensorflow/integration_keras_tuner/#configuration)