---
url: "https://clear.ml/docs/latest/docs/guides/frameworks/huggingface/transformers/"
title: "Transformers | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/frameworks/huggingface/transformers/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The [Hugging Face Transformers example](https://github.com/clearml/clearml/blob/master/examples/frameworks/huggingface/transformers.ipynb)
demonstrates how to integrate ClearML into your Transformer's [Trainer](https://huggingface.co/docs/transformers/v4.34.1/en/main_classes/trainer)
code. The Hugging Face Trainer automatically uses the built-in [`ClearMLCallback`](https://huggingface.co/docs/transformers/v4.34.1/en/main_classes/callback#transformers.integrations.ClearMLCallback)
if the `clearml` package is already installed, to log Transformers models, parameters, scalars, and more.

In the example, ClearML is installed and set up in the training environment. This way ClearML can log models, parameters,
scalars, and more.

When the example runs, it creates a ClearML task called `Trainer` in the `HuggingFace Transformers` project. To change
the task's name or project, use the `CLEARML_PROJECT` and `CLEARML_TASK` environment variables respectively.

For more information about integrating ClearML into your Transformers code, see [Hugging Face Transformers](https://clear.ml/docs/latest/docs/integrations/transformers).

## WebApp [​](https://clear.ml/docs/latest/docs/guides/frameworks/huggingface/transformers/\#webapp "Direct link to WebApp")

### Hyperparameters [​](https://clear.ml/docs/latest/docs/guides/frameworks/huggingface/transformers/\#hyperparameters "Direct link to Hyperparameters")

ClearML automatically captures all the Trainer [parameters](https://huggingface.co/docs/transformers/v4.34.1/en/main_classes/trainer#transformers.TrainingArguments).
Notice in the code example that only a few of the `TrainingArguments` are explicitly set:

```python
training_args = TrainingArguments(

     output_dir="path/to/save/folder/",

     learning_rate=2e-5,

     per_device_train_batch_size=8,

     per_device_eval_batch_size=8,

     num_train_epochs=2,

)
```

ClearML captures all of the `TrainingArguments` passed to the Trainer.

View these parameters in the task's **CONFIGURATION** tab **\> Hyperparameters** section.

![Transformers params](https://clear.ml/docs/latest/assets/images/examples_transformers_params-e328163682f7469bdd9d6b4ed1e412e6.png#light-mode-only)![Transformers params](https://clear.ml/docs/latest/assets/images/examples_transformers_params_dark-0d50d32d97a3b707480708a9fcee74c1.png#dark-mode-only)

### Models [​](https://clear.ml/docs/latest/docs/guides/frameworks/huggingface/transformers/\#models "Direct link to Models")

In order for ClearML to log the models created during training in this example, the `CLEARML_LOG_MODEL` environment
variable is set to `True`.

ClearML automatically captures the model snapshots created by the Trainer, and saves them as artifacts. View the snapshots in the
task's **ARTIFACTS** tab.

![Transformers models](https://clear.ml/docs/latest/assets/images/examples_transformers_artifacts-71da1f9dba893a3d487dbbc48e63c47b.png#light-mode-only)![Transformers models](https://clear.ml/docs/latest/assets/images/examples_transformers_artifacts_dark-443e06aa80a16f3d2e5ebf7c42f4d0d4.png#dark-mode-only)

### Scalars [​](https://clear.ml/docs/latest/docs/guides/frameworks/huggingface/transformers/\#scalars "Direct link to Scalars")

ClearML automatically captures the Trainer's scalars, which can be viewed in the task's **Scalars** tab.

![Transformers scalars](https://clear.ml/docs/latest/assets/images/integrations_transformers_scalars-049963238a2f9668abce37de10a9dc77.png#light-mode-only)![Transformers scalars](https://clear.ml/docs/latest/assets/images/integrations_transformers_scalars_dark-727830990bbfa8b5ad313d596f74e100.png#dark-mode-only)

- [WebApp](https://clear.ml/docs/latest/docs/guides/frameworks/huggingface/transformers/#webapp)
  - [Hyperparameters](https://clear.ml/docs/latest/docs/guides/frameworks/huggingface/transformers/#hyperparameters)
  - [Models](https://clear.ml/docs/latest/docs/guides/frameworks/huggingface/transformers/#models)
  - [Scalars](https://clear.ml/docs/latest/docs/guides/frameworks/huggingface/transformers/#scalars)