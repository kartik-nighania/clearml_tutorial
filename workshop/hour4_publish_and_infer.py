"""
Hour 4 — Model registry & reuse.

Two halves:

  (A) publish  — take the winning training task (from Hour 3), publish its output model and tag it
                 `winner`, so it becomes a read-only, catalogued entry in the model registry.
  (B) infer    — pull that published model back by tag (no task/run needed — models are standalone
                 registry entries), load it into ViT, and classify new leaf images. Predictions are
                 reported back to ClearML as a labeled image grid + a confusion matrix.

This shows the "reuse" side of the MLOps loop: a model registered by one run is consumed by a
completely separate script/person.

Docs: https://clear.ml/docs/latest/docs/clearml_sdk/model_sdk
      https://clear.ml/docs/latest/docs/fundamentals/models
Model registration/reuse pattern from: coding_examples/advanced/model_finetuning/finetune.py,
      coding_examples/reporting/model_reporting.py

Usage:
    # publish the winner (by training-task id from Hour 3, or by model id directly)
    python workshop/hour4_publish_and_infer.py publish --task-id <winning_task_id>
    python workshop/hour4_publish_and_infer.py publish --model-id <model_id>

    # pull the published winner and classify a folder of new images
    python workshop/hour4_publish_and_infer.py infer --images /path/to/new_leaves
"""

import argparse
import os

from clearml import InputModel, Model, Task

# Normalize: strip stray quotes/whitespace so a value like '""' counts as EMPTY.
for _k in ("CLEARML_API_ACCESS_KEY", "CLEARML_API_SECRET_KEY", "WORKSHOP_USER"):
    _v = os.environ.get(_k)
    if _v is not None:
        os.environ[_k] = _v.strip().strip('"').strip("'").strip()

# If creds / WORKSHOP_USER aren't in the environment, load them from a .env file (override empties).
if not (
    os.environ.get("CLEARML_API_ACCESS_KEY") and os.environ.get("WORKSHOP_USER")
):
    try:
        from dotenv import load_dotenv, find_dotenv

        load_dotenv(find_dotenv(usecwd=True), override=True)
    except Exception:
        pass

# Same per-attendee project as Hours 2-3 (from WORKSHOP_USER); your winning model lives here.
# `or "anonymous"` so an EMPTY WORKSHOP_USER doesn't make a "/"-suffixed project.
WORKSHOP_USER = os.environ.get("WORKSHOP_USER") or "anonymous"
PROJECT = f"PlantVillage Workshop/{WORKSHOP_USER}"
WINNER_TAG = "winner"


# --------------------------------------------------------------------------------------------------
# (A) Publish the winning model
# --------------------------------------------------------------------------------------------------
def resolve_model_id(task_id=None, model_id=None):
    if model_id:
        return model_id
    if task_id:
        t = Task.get_task(task_id=task_id)
        out = t.output_models_id or {}  # {output-slot-name: model_id}; robust to any slot name
        if not out:
            raise SystemExit(f"task {task_id} has no output model registered")
        chosen = list(out.values())[-1]  # the task's current (last-pointed) output model
        print(f"resolved output model of task {task_id} -> {chosen}")
        return chosen
    raise SystemExit("provide --task-id or --model-id")


def publish(args):
    model_id = resolve_model_id(args.task_id, args.model_id)
    model = Model(model_id=model_id)  # existing registry model — no task needed (unlike OutputModel)
    model.tags = list(set((model.tags or []) + [WINNER_TAG]))
    model.publish()  # -> status 'published' (read-only); its creating task also becomes published
    print(f"published model {model_id} and tagged it '{WINNER_TAG}'.")
    print(
        "Open the ClearML UI -> Models to see it as read-only with full lineage."
    )


# --------------------------------------------------------------------------------------------------
# (B) Pull the published winner and run inference on new images
# --------------------------------------------------------------------------------------------------
def find_winner_model():
    """Return the id of the published model tagged `winner` in the PlantVillage project."""
    models = Model.query_models(
        project_name=PROJECT,
        tags=[WINNER_TAG],
        only_published=True,
        max_results=1,
    )
    if not models:
        raise SystemExit(
            f"no published model tagged '{WINNER_TAG}' in project '{PROJECT}'. Run `publish` first."
        )
    return models[0].id


def infer(args):
    import torch
    from PIL import Image
    from transformers import AutoImageProcessor, AutoModelForImageClassification

    # A task so the inference results (grid + confusion matrix) are tracked too.
    # Standalone: store the code in the task, no git link (consistent with the other hours).
    Task.force_store_standalone_script()
    task = Task.init(
        project_name=PROJECT,
        task_name="ViT-Tiny inference",
        task_type=Task.TaskTypes.inference,
    )

    model_id = args.model_id or find_winner_model()
    input_model = InputModel(model_id=model_id)
    task.connect(input_model)  # record which model this run used (lineage)
    weights_dir = (
        input_model.get_local_copy()
    )  # cached local path to the model folder
    print(f"pulled model {model_id} -> {weights_dir}")
    if not weights_dir or not os.path.isdir(weights_dir):
        raise SystemExit(
            f"Could not download weights for model {model_id} (get_local_copy -> {weights_dir!r}).\n"
            f"Its weights were likely saved to the training agent's LOCAL disk instead of the file "
            f"server (model uri like 'file:///tmp/...'). Re-run Hour 2 with an output destination set:\n"
            f"    clearml-task ... --output-uri http://202.131.110.56:8081\n"
            f"then re-pick the winner (Hour 3), re-publish, and run infer again."
        )

    try:
        processor = AutoImageProcessor.from_pretrained(weights_dir)
    except Exception:
        # older model packages may not bundle the image processor -> use the base ViT-Tiny's.
        processor = AutoImageProcessor.from_pretrained("WinKawaks/vit-tiny-patch16-224")
    model = AutoModelForImageClassification.from_pretrained(weights_dir)
    model.eval()
    id2label = model.config.id2label

    if args.images:
        image_paths = [
            os.path.join(args.images, f)
            for f in sorted(os.listdir(args.images))
            if f.lower().endswith((".jpg", ".jpeg", ".png"))
        ]
    else:
        # No folder given (typical in Colab) -> sample a few images from the shared demo dataset.
        from clearml import Dataset

        demo = Dataset.get(
            dataset_project="PlantVillage",
            dataset_name="plantdisease_demo",
            alias="plantdisease_demo",
        ).get_local_copy()
        image_paths = []
        for cls in sorted(os.listdir(demo)):
            cdir = os.path.join(demo, cls)
            if os.path.isdir(cdir):
                image_paths += [os.path.join(cdir, f) for f in sorted(os.listdir(cdir))[:3]]
    if not image_paths:
        raise SystemExit("no images found (pass --images <folder>, or ensure plantdisease_demo exists)")

    logger = task.get_logger()
    import matplotlib.pyplot as plt

    preds, truths = [], []
    cols = 4
    rows = (min(len(image_paths), 12) + cols - 1) // cols
    fig = plt.figure(figsize=(4 * cols, 4 * rows))

    for i, path in enumerate(image_paths[:12]):
        img = Image.open(path).convert("RGB")
        inputs = processor(images=img, return_tensors="pt")
        with torch.no_grad():
            logits = model(**inputs).logits
        pred_id = int(logits.argmax(-1))
        pred_label = id2label[pred_id]
        preds.append(pred_id)

        # If the file lives in a class-named subfolder we can compute accuracy; otherwise skip.
        parent = os.path.basename(os.path.dirname(path))
        if parent in model.config.label2id:
            truths.append(model.config.label2id[parent])

        ax = fig.add_subplot(rows, cols, i + 1)
        ax.imshow(img)
        ax.axis("off")
        ax.set_title(pred_label, fontsize=10)

    plt.tight_layout()
    # report_image=True -> send as a PNG to the DEBUG SAMPLES tab. Without it, ClearML tries to
    # convert the figure to Plotly, which can't render imshow images (shows an empty plot).
    logger.report_matplotlib_figure(
        "Predictions", "new images", iteration=0, figure=fig, report_image=True
    )
    plt.close(fig)

    # Confusion matrix only if we had ground-truth folder labels for all shown images.
    if len(truths) == len(preds) and truths:
        from sklearn.metrics import confusion_matrix

        cm = confusion_matrix(truths, preds, labels=list(range(len(id2label))))
        logger.report_confusion_matrix(
            "Confusion matrix",
            "inference",
            matrix=cm,
            xaxis="predicted",
            yaxis="true",
            xlabels=list(id2label.values()),
            ylabels=list(id2label.values()),
        )
        acc = sum(int(p == t) for p, t in zip(preds, truths)) / len(preds)
        logger.report_single_value("inference_accuracy", acc)
        print(f"inference accuracy on labeled images: {acc:.3f}")

    print(
        f"reported predictions for {len(image_paths[:12])} images. Task ID: {task.id}"
    )


def main():
    parser = argparse.ArgumentParser(
        description="Publish the winning model and run inference"
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_pub = sub.add_parser("publish", help="publish + tag the winning model")
    p_pub.add_argument(
        "--task-id", help="winning training task id (from Hour 3)"
    )
    p_pub.add_argument("--model-id", help="model id (alternative to --task-id)")
    p_pub.set_defaults(func=publish)

    p_inf = sub.add_parser(
        "infer", help="pull the published winner and classify new images"
    )
    p_inf.add_argument(
        "--images",
        help="folder of leaf images (optional; default: sample from the plantdisease_demo dataset)",
    )
    p_inf.add_argument(
        "--model-id",
        help="explicit model id (default: published model tagged 'winner')",
    )
    p_inf.set_defaults(func=infer)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
