"""
Hour 2 — GPU training via a shared queue.

Fine-tunes a tiny Vision Transformer (WinKawaks/vit-tiny-patch16-224, ~5.7M params) on the
`plantdisease_demo` ClearML dataset (~1000 images, 4 classes) for 2-3 epochs. The point is to
teach the ClearML workflow, not to build a real classifier:

  * `Task.init(...)` gives you automatic tracking with ~2 lines.
  * `task.execute_remotely(queue_name=TRAIN_QUEUE)` stops the local run and ships the SAME task to a
    GPU queue, where a clearml-agent on a MIG slice picks it up. 30 attendees submitting at once
    -> watch the scheduler share the H200(s) across everyone.
  * HuggingFace `Trainer(report_to=["clearml"])` streams loss/accuracy live into the SCALARS tab.
  * A per-epoch callback registers one clean named model each epoch ("ViT-Tiny PlantVillage -
    epoch N") to `output_uri`, so Hours 3-4 (compare + registry) have models to work with.

Run it from a notebook cell (`%run workshop/hour2_finetune_vit.py`) or the terminal. On the FIRST
call it configures the task locally then enqueues itself to the TRAIN_QUEUE (default `gpu-18gb`);
the agent re-runs the whole thing remotely.

Docs: https://clear.ml/docs/latest/docs/integrations/transformers
      https://clear.ml/docs/latest/docs/getting_started/remote_execution
Adapted from: coding_examples/frameworks/huggingface/transformers.ipynb
              coding_examples/advanced/model_finetuning/finetune.py
"""

import os

# Normalize: strip stray quotes/whitespace so a value like '""' counts as EMPTY (e.g. from a %env cell).
for _k in ("CLEARML_API_ACCESS_KEY", "CLEARML_API_SECRET_KEY", "WORKSHOP_USER"):
    _v = os.environ.get(_k)
    if _v is not None:
        os.environ[_k] = _v.strip().strip('"').strip("'").strip()

# If ClearML creds / WORKSHOP_USER aren't already in the environment (e.g. running locally, or the
# credentials were left blank), load them from a .env file — override=True replaces any empty values.
if not (os.environ.get("CLEARML_API_ACCESS_KEY") and os.environ.get("WORKSHOP_USER")):
    try:
        from dotenv import load_dotenv, find_dotenv
        load_dotenv(find_dotenv(usecwd=True), override=True)
    except Exception:
        pass

# Ask the HF integration to register the model the Trainer produces. Set before clearml/transformers
# read it. (Attendees also set their server creds in the notebook's credentials cell before running this.)
os.environ.setdefault("CLEARML_LOG_MODEL", "True")

import numpy as np
from clearml import Task, Dataset, OutputModel

# Which GPU queue attendees submit to. This server's MIG tiers are:
#   gpu-18gb  (2 slots, 18 GB each)  · gpu-35gb (1) · gpu-71gb (1) · gpu-141gb (1, whole card)
# ViT-Tiny needs only ~2-3 GB, so gpu-18gb is the right default.
TRAIN_QUEUE = "gpu-18gb"

# Everyone shares ONE ClearML login + API key. Attendees tell their runs apart by setting
# WORKSHOP_USER (their name) in the credentials cell / .env — their experiments land in their own project.
# The dataset is COMMON (one shared copy on the server), used by every attendee's project.
# `or "anonymous"` (not a .get default) so an EMPTY WORKSHOP_USER doesn't make a "/"-suffixed project.
WORKSHOP_USER = os.environ.get("WORKSHOP_USER") or "anonymous"
EXPERIMENT_PROJECT = f"PlantVillage Workshop/{WORKSHOP_USER}"


def main():
    # Fail early (LOCALLY only) with a clear message if the shared key wasn't pasted in. On the agent
    # this same script re-runs, but there credentials come from the agent's clearml.conf (NOT these
    # env vars), so Task.running_locally() gates the check to avoid a false "keys are EMPTY" on remote.
    if Task.running_locally() and not (
        os.environ.get("CLEARML_API_ACCESS_KEY") and os.environ.get("CLEARML_API_SECRET_KEY")
    ):
        raise SystemExit(
            "ClearML API keys are EMPTY. Paste the shared access/secret key into your credentials cell "
            "(and set WORKSHOP_USER to your name), then re-run."
        )

    # Store THIS script standalone (copy the code into the task) instead of linking to a git repo,
    # so the agent runs it WITHOUT cloning the repo — no git access/credentials needed. Must be
    # called before Task.init.
    Task.force_store_standalone_script()

    # ---- 1. Track everything (do this first, before heavy imports/work) ----
    task = Task.init(
        project_name=EXPERIMENT_PROJECT,   # your own project, from WORKSHOP_USER
        task_name="ViT-Tiny finetune",
        output_uri=True,            # upload the trained model to the ClearML file server
        # Don't auto-register every torch.save (optimizer/scheduler/rng/etc.) as a "model" — we
        # register one clean, named model PER EPOCH instead (see the callback below). Keeps it tidy.
        auto_connect_frameworks={"pytorch": False},
    )

    # Hyperparameters we want to see/edit in the UI (Hour 3 clones this task and tweaks them).
    params = {
        "model_name": "WinKawaks/vit-tiny-patch16-224",
        "dataset_project": "PlantVillage",
        "dataset_name": "plantdisease_demo",
        "num_train_epochs": 3,
        "learning_rate": 5e-4,
        "train_batch_size": 32,
        "eval_batch_size": 32,
        "val_split": 0.2,
        "seed": 42,
    }
    params = task.connect(params)   # connected params are editable from the UI on a cloned task

    # ---- 2. Tell the agent WHERE to run and WHAT to install, then move to the GPU queue ----
    # Use the HuggingFace GPU image (torch + transformers + CUDA 12.x already inside) and let the
    # clearml-agent install our extra deps from requirements.txt into it — no custom image to build.
    # Both calls configure the task here (in Colab) and are ignored on the remote side; the MIG agents
    # just need to run in docker mode. torch/transformers are already satisfied by the image (loose
    # pins), so the agent only installs the few extras (datasets, evaluate, scikit-learn, ...).
    task.set_base_docker(docker_image="huggingface/transformers-pytorch-gpu:latest")
    _reqs = os.path.join(os.path.dirname(os.path.abspath(__file__)), "requirements.txt")
    if os.path.exists(_reqs):
        task.set_packages(_reqs)

    # execute_remotely enqueues the fully-configured task; on most setups it also terminates the
    # local process. In some environments (e.g. Colab's `!python`) it does NOT hard-exit, leaving the
    # connected `params` as a non-subscriptable StubObject. So guard explicitly: once enqueued, bail
    # out locally — the heavy training below runs only on the agent (where running_locally() is False).
    task.execute_remotely(queue_name=TRAIN_QUEUE)
    if Task.running_locally():
        print(f"Task enqueued to '{TRAIN_QUEUE}'. Training runs on the agent — watch it in the UI.")
        return

    # ===== Everything below runs on the MIG-backed GPU agent =====
    import evaluate
    import torch
    from datasets import load_dataset
    from transformers import (
        AutoImageProcessor,
        AutoModelForImageClassification,
        Trainer,
        TrainerCallback,
        TrainingArguments,
    )

    # ---- 3. Pull the shared dataset (cached). alias=... BINDS it to this task, so the UI shows
    #         exactly which dataset version this run used (lineage). ----
    data_dir = Dataset.get(
        dataset_project=params["dataset_project"],
        dataset_name=params["dataset_name"],
        alias=params["dataset_name"],
    ).get_local_copy()
    print(f"dataset materialized at: {data_dir}")

    # imagefolder infers labels from the class subfolder names.
    ds = load_dataset("imagefolder", data_dir=data_dir, split="train")
    ds = ds.train_test_split(test_size=params["val_split"], seed=params["seed"])

    labels = ds["train"].features["label"].names
    id2label = {i: name for i, name in enumerate(labels)}
    label2id = {name: i for i, name in enumerate(labels)}
    print(f"classes ({len(labels)}): {labels}")

    # ---- 4. Model + image preprocessing ----
    processor = AutoImageProcessor.from_pretrained(params["model_name"])
    model = AutoModelForImageClassification.from_pretrained(
        params["model_name"],
        num_labels=len(labels),
        id2label=id2label,
        label2id=label2id,
        ignore_mismatched_sizes=True,   # swap the 1000-class ImageNet head for our 4 classes
    )

    image_mean = processor.image_mean
    image_std = processor.image_std
    size = processor.size.get("shortest_edge", processor.size.get("height", 224))

    from torchvision.transforms import (
        Compose, Normalize, RandomHorizontalFlip, RandomResizedCrop, Resize, CenterCrop, ToTensor,
    )

    train_tf = Compose([
        RandomResizedCrop(size),
        RandomHorizontalFlip(),
        ToTensor(),
        Normalize(mean=image_mean, std=image_std),
    ])
    eval_tf = Compose([
        Resize(size),
        CenterCrop(size),
        ToTensor(),
        Normalize(mean=image_mean, std=image_std),
    ])

    def apply_train(batch):
        batch["pixel_values"] = [train_tf(img.convert("RGB")) for img in batch["image"]]
        return batch

    def apply_eval(batch):
        batch["pixel_values"] = [eval_tf(img.convert("RGB")) for img in batch["image"]]
        return batch

    ds["train"].set_transform(apply_train)
    ds["test"].set_transform(apply_eval)

    def collate(examples):
        return {
            "pixel_values": torch.stack([e["pixel_values"] for e in examples]),
            "labels": torch.tensor([e["label"] for e in examples]),
        }

    accuracy = evaluate.load("accuracy")

    def compute_metrics(eval_pred):
        preds = np.argmax(eval_pred.predictions, axis=1)
        return accuracy.compute(predictions=preds, references=eval_pred.label_ids)

    # ---- 5. Train (HF Trainer streams scalars into ClearML because report_to=['clearml']) ----
    training_args = TrainingArguments(
        output_dir="./vit-tiny-plantdisease",
        num_train_epochs=params["num_train_epochs"],
        learning_rate=params["learning_rate"],
        per_device_train_batch_size=params["train_batch_size"],
        per_device_eval_batch_size=params["eval_batch_size"],
        eval_strategy="epoch",     # still eval each epoch -> loss/accuracy scalars for Hour 3
        save_strategy="no",        # no per-epoch checkpoints (we save/register one final model below)
        logging_steps=10,
        seed=params["seed"],
        remove_unused_columns=False,     # keep the 'image' column for our transform
        report_to=["clearml"],
    )

    # Save each epoch's model + image processor and record its eval accuracy. We register the models
    # AFTER training (below) so we can make the BEST epoch the task's output model.
    epoch_saves = []   # (accuracy, epoch, weights_dir)

    class SavePerEpoch(TrainerCallback):
        def on_evaluate(self, args, state, control, metrics=None, **kw):
            epoch = int(round(state.epoch))                    # 1.0 after epoch 1 -> 1
            acc = float((metrics or {}).get("eval_accuracy", 0.0))
            d = os.path.join("epoch_ckpts", f"epoch_{epoch}")
            model.save_pretrained(d)                           # config.json + model.safetensors
            processor.save_pretrained(d)                       # preprocessor_config.json (reloadable)
            epoch_saves.append((acc, epoch, d))
            print(f"epoch {epoch}: eval_accuracy={acc:.4f}")

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=ds["train"],
        eval_dataset=ds["test"],
        data_collator=collate,
        compute_metrics=compute_metrics,
        callbacks=[SavePerEpoch()],
    )
    trainer.train()

    # ---- 6. Register EVERY epoch as a model (all show in the project's MODELS table). Register in
    #         ASCENDING accuracy order so the BEST epoch is registered LAST -> it becomes the task's
    #         output model, i.e. the ARTIFACTS section shows the BEST run, not just the last one. ----
    epoch_saves.sort(key=lambda r: r[0])   # ascending by accuracy (best last)
    for acc, epoch, d in epoch_saves:
        OutputModel(task=task, name=f"ViT-Tiny PlantVillage - epoch {epoch} (acc {acc:.3f})",
                    framework="PyTorch").update_weights_package(weights_path=d)
    best_acc, best_epoch, _ = epoch_saves[-1]
    print(f"best epoch: {best_epoch} (accuracy {best_acc:.4f}) -> task output model")
    print(f"Task ID: {task.id}")


if __name__ == "__main__":
    main()
