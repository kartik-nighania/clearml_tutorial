---
url: "https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/audio/audio_preprocessing_example/"
title: "Audio Preprocessing - Jupyter Notebook | ClearML"
---

[Skip to main content](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/audio/audio_preprocessing_example/#__docusaurus_skipToContent_fallback)

If you ❤️ ️ **ClearML**, ⭐️ us on [GitHub](https://github.com/clearml/clearml)!

On this page

The example [audio\_preprocessing\_example.ipynb](https://github.com/clearml/clearml/blob/master/examples/frameworks/pytorch/notebooks/audio/audio_preprocessing_example.ipynb)
demonstrates integrating ClearML into a Jupyter Notebook which uses PyTorch and preprocesses audio samples. ClearML automatically logs spectrogram visualizations reported by calling Matplotlib methods, and audio samples reported by calling TensorBoard methods. The example also demonstrates connecting parameters to a Task and logging them. When the script runs, it creates a task named `data pre-processing` in the `Audio Example` project.

## Plots [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/audio/audio_preprocessing_example/\#plots "Direct link to Plots")

ClearML automatically logs the waveform which the example reports by calling a Matplotlib method. These appear in **PLOTS**.

![image](https://clear.ml/docs/latest/assets/images/examples_audio_preprocessing_example_08-39cde5cbdd460233228146ccf8597aec.png)

## Debug Samples [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/audio/audio_preprocessing_example/\#debug-samples "Direct link to Debug Samples")

ClearML automatically logs the audio samples which the example reports by calling TensorBoard methods, and the spectrogram visualizations reported by calling Matplotlib methods. They appear in **DEBUG SAMPLES**.

### Audio Samples [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/audio/audio_preprocessing_example/\#audio-samples "Direct link to Audio Samples")

You can play the audio samples by clicking the audio thumbnail.

![image](https://clear.ml/docs/latest/assets/images/examples_audio_preprocessing_example_03-b1c7f0eaba4b4ed15c161f61d26a3e23.png)

### Spectrogram Visualizations [​](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/audio/audio_preprocessing_example/\#spectrogram-visualizations "Direct link to Spectrogram Visualizations")

![image](https://clear.ml/docs/latest/assets/images/examples_audio_preprocessing_example_06-6f33eb1887f1f4c41c51795d9f69ac85.png)![image](https://clear.ml/docs/latest/assets/images/examples_audio_preprocessing_example_06a-ae81de323385c1e1d8a5235af8f3a6e1.png)

You can view the spectrogram visualizations in the **ClearML Web UI** image viewer.

![image](https://clear.ml/docs/latest/assets/images/examples_audio_preprocessing_example_07-6151518da0597b8a97072ca0501f1034.png)

- [Plots](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/audio/audio_preprocessing_example/#plots)
- [Debug Samples](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/audio/audio_preprocessing_example/#debug-samples)
  - [Audio Samples](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/audio/audio_preprocessing_example/#audio-samples)
  - [Spectrogram Visualizations](https://clear.ml/docs/latest/docs/guides/frameworks/pytorch/notebooks/audio/audio_preprocessing_example/#spectrogram-visualizations)