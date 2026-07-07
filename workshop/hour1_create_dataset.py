"""
Hour 1 (facilitator, run ONCE on the VM) — register the PlantVillage data as ClearML Datasets.

Creates two datasets in the `PlantVillage` project so attendees can see data versioning in the UI
and pull a small, fixed training set from local VM storage:

  1. plantdisease_full  — the whole dataset (15 classes, ~20.6k images). Shown in the UI as the
                          "catalog". Not used for training (too big for a 4-hour teaching lab).
  2. plantdisease_demo  — a small, balanced ~1000-image / 4-class subset that the training job
                          actually consumes. Kept as a STANDALONE dataset (NOT a child of
                          plantdisease_full) on purpose: a child version inherits ALL parent files
                          on get_local_copy(), which would pull ~20k images instead of ~1000.

This script is HOST-AGNOSTIC: it never hardcodes server URLs. Connection comes from the
environment (CLEARML_API_HOST / CLEARML_FILES_HOST / CLEARML_API_ACCESS_KEY / CLEARML_API_SECRET_KEY)
or from ~/clearml.conf. On the VM the repo `.env` already points at localhost:8008/8081.

Docs: https://clear.ml/docs/latest/docs/clearml_data/clearml_data_sdk
Pattern adapted from: coding_examples/datasets/dataset_creation.py,
                      coding_examples/datasets/single_parent_child_dataset.py

Usage (on the VM, from the repo root):
    python workshop/hour1_create_dataset.py --data-root dataset
    python workshop/hour1_create_dataset.py --data-root dataset --per-class 250 --project PlantVillage
"""

import argparse
import os
import random
import shutil
import tempfile

from clearml import Dataset

# The 4 clean, visually-distinct classes used for the training demo. All exist in the
# Kaggle PlantVillage folder with >=1000 source images each.
DEMO_CLASSES = [
    "Tomato_healthy",
    "Tomato_Early_blight",
    "Potato___Late_blight",
    "Pepper__bell___healthy",
]

IMAGE_EXTS = (".jpg", ".jpeg", ".png", ".bmp", ".gif")


def list_class_dirs(data_root):
    """Return the real per-class subfolders of `data_root`, excluding the nested duplicate."""
    dirs = []
    for name in sorted(os.listdir(data_root)):
        path = os.path.join(data_root, name)
        if os.path.isdir(path):
            dirs.append(name)
    return dirs


def list_images(folder):
    return [
        f for f in sorted(os.listdir(folder))
        if f.lower().endswith(IMAGE_EXTS) and os.path.isfile(os.path.join(folder, f))
    ]


def create_full_dataset(data_root, project):
    """Register the entire dataset, preserving class subfolders (via dataset_path) for labels."""
    classes = list_class_dirs(data_root)
    print(f"[full] registering {len(classes)} classes from '{data_root}': {classes}")

    ds = Dataset.create(dataset_project=project, dataset_name="plantdisease_full")
    for cls in classes:
        # dataset_path=cls keeps each class in its own subfolder inside the dataset, so the
        # label structure survives get_local_copy(). No wildcard -> all image extensions added.
        ds.add_files(path=os.path.join(data_root, cls), dataset_path=cls)
    ds.upload()          # uploads to the ClearML file server (localhost:8081 on the VM)
    ds.finalize()        # immutable + consumable
    print(f"[full] done. dataset id = {ds.id}")
    return ds


def create_demo_subset(data_root, project, per_class, seed):
    """Sample `per_class` images from each DEMO_CLASSES folder into a standalone ~1000-img dataset."""
    rng = random.Random(seed)

    # Stage the sampled files under class subfolders so load_dataset("imagefolder") can infer labels.
    with tempfile.TemporaryDirectory(prefix="plantdisease_demo_") as staging:
        total = 0
        for cls in DEMO_CLASSES:
            src_dir = os.path.join(data_root, cls)
            if not os.path.isdir(src_dir):
                raise SystemExit(f"[demo] missing class folder: {src_dir}")
            imgs = list_images(src_dir)
            if len(imgs) < per_class:
                print(f"[demo] warning: {cls} has only {len(imgs)} images (< {per_class}); using all")
            picked = rng.sample(imgs, min(per_class, len(imgs)))
            dst_dir = os.path.join(staging, cls)
            os.makedirs(dst_dir, exist_ok=True)
            for f in picked:
                shutil.copy2(os.path.join(src_dir, f), os.path.join(dst_dir, f))
            total += len(picked)
            print(f"[demo] {cls}: {len(picked)} images")

        print(f"[demo] staged {total} images across {len(DEMO_CLASSES)} classes")
        ds = Dataset.create(dataset_project=project, dataset_name="plantdisease_demo")
        ds.add_files(path=staging)   # staging root has the 4 class subfolders
        ds.upload()
        ds.finalize()
    print(f"[demo] done. dataset id = {ds.id}")
    print(f"[demo] fetch later with: "
          f"Dataset.get(dataset_project='{project}', dataset_name='plantdisease_demo').get_local_copy()")
    return ds


def main():
    parser = argparse.ArgumentParser(description="Register PlantVillage datasets in ClearML")
    parser.add_argument("--data-root", default="dataset", help="path to the PlantVillage folder")
    parser.add_argument("--project", default="PlantVillage", help="ClearML dataset project")
    parser.add_argument("--per-class", type=int, default=250, help="images per class in the demo subset")
    parser.add_argument("--seed", type=int, default=42, help="sampling seed for reproducibility")
    parser.add_argument("--skip-full", action="store_true", help="don't build the full catalog dataset")
    parser.add_argument("--skip-demo", action="store_true",
                        help="don't build the demo subset (e.g. it already exists — only add the full)")
    args = parser.parse_args()

    if not os.path.isdir(args.data_root):
        raise SystemExit(f"data root not found: {args.data_root}")

    if not args.skip_full:
        create_full_dataset(args.data_root, args.project)
    if not args.skip_demo:
        create_demo_subset(args.data_root, args.project, args.per_class, args.seed)

    print("\nAll set. Open the ClearML UI -> Datasets -> project 'PlantVillage'.")


if __name__ == "__main__":
    main()
