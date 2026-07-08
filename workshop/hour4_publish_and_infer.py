"""
Hour 4 — Model registry & reuse.

Two halves:

  (A) publish  — take the winning training task (from Hour 3), publish its output model and tag it
                 `winner`, so it becomes a read-only, catalogued entry in the model registry.
  (B) infer    — pull that published model back by tag (no task/run needed — models are standalone
                 registry entries), load it into ViT, and classify new leaf images LOCALLY. Results
                 (a predictions grid + a confusion matrix) are saved as PNGs and the accuracy printed;
                 nothing is reported back to ClearML. The workshop notebook displays the PNGs inline.

This shows the "reuse" side of the MLOps loop: a model registered by one run is consumed by a
completely separate script/person, on any machine, with no ClearML task needed.

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
    import matplotlib

    matplotlib.use("Agg")  # headless: we SAVE figures to PNGs (the notebook displays them inline)
    import matplotlib.pyplot as plt

    # Inference runs LOCALLY. ClearML is used only as a registry here (find + download the model);
    # NO ClearML task is created and nothing is reported back. Results are saved as PNGs + printed.
    model_id = args.model_id or find_winner_model()
    weights_dir = InputModel(model_id=model_id).get_local_copy()  # download weights to local cache
    print(f"downloaded model {model_id} -> {weights_dir}")
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

    # ---- classify + build the predictions grid (predicted label as each image's title) ----
    preds, truths = [], []
    cols = 4
    rows = (min(len(image_paths), 12) + cols - 1) // cols
    fig = plt.figure(figsize=(4 * cols, 4 * rows))
    for i, path in enumerate(image_paths[:12]):
        img = Image.open(path).convert("RGB")
        with torch.no_grad():
            logits = model(**processor(images=img, return_tensors="pt")).logits
        pred_id = int(logits.argmax(-1))
        preds.append(pred_id)
        parent = os.path.basename(os.path.dirname(path))  # class folder = ground truth (if present)
        if parent in model.config.label2id:
            truths.append(model.config.label2id[parent])
        ax = fig.add_subplot(rows, cols, i + 1)
        ax.imshow(img)
        ax.axis("off")
        ax.set_title(id2label[pred_id], fontsize=10)
    plt.tight_layout()
    pred_png = os.path.abspath("hour4_predictions.png")
    fig.savefig(pred_png, dpi=110, bbox_inches="tight")
    plt.close(fig)
    print(f"saved predictions grid -> {pred_png}")

    # ---- confusion matrix + accuracy (only if the images came from class-named folders) ----
    if len(truths) == len(preds) and truths:
        from sklearn.metrics import confusion_matrix

        cm = confusion_matrix(truths, preds, labels=list(range(len(id2label))))
        labels = list(id2label.values())
        fig2, ax = plt.subplots(figsize=(1.1 * len(labels) + 3, 1.1 * len(labels) + 2))
        im = ax.imshow(cm, cmap="Blues")
        ax.set_xticks(range(len(labels)))
        ax.set_xticklabels(labels, rotation=45, ha="right", fontsize=8)
        ax.set_yticks(range(len(labels)))
        ax.set_yticklabels(labels, fontsize=8)
        ax.set_xlabel("predicted")
        ax.set_ylabel("true")
        ax.set_title("Confusion matrix")
        for r in range(len(labels)):
            for c in range(len(labels)):
                ax.text(c, r, cm[r, c], ha="center", va="center",
                        color="white" if cm[r, c] > cm.max() / 2 else "black", fontsize=9)
        fig2.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
        plt.tight_layout()
        cm_png = os.path.abspath("hour4_confusion_matrix.png")
        fig2.savefig(cm_png, dpi=110, bbox_inches="tight")
        plt.close(fig2)
        acc = sum(int(p == t) for p, t in zip(preds, truths)) / len(preds)
        print(f"saved confusion matrix -> {cm_png}")
        print(f"inference accuracy on {len(preds)} labeled images: {acc:.3f}")

    print(f"done — classified {len(image_paths[:12])} images locally (no ClearML task created).")


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
