---
url: "https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/audio/audio_classification_UrbanSound8K/"
title: "Audio Classification - Jupyter Notebooks | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/audio/audio_classification_UrbanSound8K/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The [audio\_classification\_UrbanSound8K.ipynb](https://github.com/clearml/clearml/blob/master/examples/frameworks/pytorch/notebooks/audio/audio_classifier_UrbanSound8K.ipynb) example script demonstrates integrating ClearML into a Jupyter Notebook which uses PyTorch, TensorBoard, and TorchVision to train a neural network on the UrbanSound8K dataset for audio classification. The example calls TensorBoard methods in training and testing to report scalars, audio debug samples, and spectrogram visualizations. The spectrogram visualizations are plotted by calling Matplotlib methods. The example also demonstrates connecting parameters to a Task and logging them. When the script runs, it creates a task named `audio classification UrbanSound8K` in the `Audio Example` project.

## Scalars [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/audio/audio_classification_UrbanSound8K/\#scalars "Direct link to Scalars")

The accuracy, learning rate, and training loss scalars are automatically logged, along with the resource utilization plots (titled **:monitor: machine**), and appear in **SCALARS**.

![image](https://clear.ml/docs/latest/assets/images/examples_audio_classification_UrbanSound8K_03-db2c98788d212b71b0fd6bb7749d95ac.png)

## Debug Samples [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/audio/audio_classification_UrbanSound8K/\#debug-samples "Direct link to Debug Samples")

The audio samples and spectrogram plots are automatically logged and appear in **DEBUG SAMPLES**.

### Audio Samples [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/audio/audio_classification_UrbanSound8K/\#audio-samples "Direct link to Audio Samples")

![image](https://clear.ml/docs/latest/assets/images/examples_audio_classification_UrbanSound8K_06-c42d04d275d7906406a9f9b1d2d1afd3.png)

By doubling clicking a thumbnail, you can play an audio sample.

### Spectrogram Visualizations [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/audio/audio_classification_UrbanSound8K/\#spectrogram-visualizations "Direct link to Spectrogram Visualizations")

![image](https://clear.ml/docs/latest/assets/images/examples_audio_classification_UrbanSound8K_04-b9c87d8fa87f7d84ced1f54bddf0fc00.png)

By doubling clicking a thumbnail, you can view a spectrogram plot in the image viewer.

![image](https://clear.ml/docs/latest/assets/images/examples_audio_classification_UrbanSound8K_05-8f895c29d2fa5081ebb2eceb48bb66cb.png)

## Hyperparameters [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/audio/audio_classification_UrbanSound8K/\#hyperparameters "Direct link to Hyperparameters")

ClearML automatically logs TensorFlow Definitions. A parameter dictionary is logged by connecting it to the Task using
a call to the [`Task.connect`](https://clear.ml/docs/latest/docs/references/sdk/task#connect) method.

```python
configuration_dict = {

    'number_of_epochs': 10,

    'batch_size': 4,

    'dropout': 0.25,

    'base_lr': 0.001

}

configuration_dict = task.connect(configuration_dict)  # enabling configuration override by clearml
```

Parameter dictionaries appear in **CONFIGURATION** **>** **HYPERPARAMETERS** **>** **General**.

![image](https://clear.ml/docs/latest/assets/images/examples_audio_classification_UrbanSound8K_01-4d3b225bfe52b18ce95dccdb855b0def.png)

TensorFlow Definitions appear in the **TF\_DEFINE** subsection.

![image](https://clear.ml/docs/latest/assets/images/examples_audio_classification_UrbanSound8K_01a-0a608e4e17be789e4e0c71cbe4b2172d.png)

## Console [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/audio/audio_classification_UrbanSound8K/\#console "Direct link to Console")

Text printed to the console for training progress, as well as all other console output, appear in **CONSOLE**.

![image](https://clear.ml/docs/latest/assets/images/examples_audio_classification_UrbanSound8K_02-a23f00a8ec964ce75c99b8be250b682c.png)

- [Scalars](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/audio/audio_classification_UrbanSound8K/#scalars)
- [Debug Samples](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/audio/audio_classification_UrbanSound8K/#debug-samples)
  - [Audio Samples](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/audio/audio_classification_UrbanSound8K/#audio-samples)
  - [Spectrogram Visualizations](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/audio/audio_classification_UrbanSound8K/#spectrogram-visualizations)
- [Hyperparameters](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/audio/audio_classification_UrbanSound8K/#hyperparameters)
- [Console](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/audio/audio_classification_UrbanSound8K/#console)