# ClearML Hands-on Lab — Plant Disease Detection (PlantVillage)

A 4-hour, browser-only workshop that teaches the **full ClearML MLOps loop** on a self-hosted
open-source server, using a tiny Vision Transformer and the PlantVillage leaf-disease dataset.

> **The goal is to learn ClearML, not to build a production model.** We deliberately use a small
> model (ViT-Tiny), a ~1000-image subset, and 1–2 epochs so runs finish in seconds and everyone can
> watch experiments, queues, comparisons, and the model registry come alive.

- **Server:** http://202.131.110.56 (open-source ClearML; plain HTTP is fine on this internal box)
- **Compute:** 2× H200 — one MIG-sliced into VRAM tiers (`gpu-18gb` ×2, `gpu-35gb`, `gpu-71gb`) plus
  one whole card (`gpu-141gb`). MIG hardware-isolation = zero cross-job OOM. Attendees pick a
  tier by queue; ViT-Tiny fits the smallest (`gpu-18gb`) easily.
- **You need:** just a browser + a Google account. Notebooks run in **Google Colab** (CPU); training
  is submitted to a GPU queue and runs on the H200 MIG agents.

---

## Files in this folder

| File | Who | What |
|---|---|---|
| `00_setup_credentials.md` | attendee | log in → create API keys → paste into your notebook |
| `hour1_first_experiment.ipynb` | attendee | first tracked experiment + auto-captured EDA plots |
| `hour1_create_dataset.py` | facilitator | register full PlantVillage + build the 1000-img demo subset |
| `hour2_finetune_vit.py` | attendee | ViT-Tiny fine-tune, submitted to the `gpu-18gb` queue |
| `hour3_pick_best_model.ipynb` | attendee | clone/compare runs + pick the winner programmatically |
| `hour4_publish_and_infer.py` | attendee | publish the winner, pull it back, classify new images |
| `facilitator/agent_setup.md` | facilitator | GPU queues/agents (MIG) + remaining VM work checklist |
| `facilitator/shared_user.md` | facilitator | one shared login + shared API key (no per-user accounts) |
| `facilitator/VM_SETUP.md` | facilitator | full "what to do on the ClearML VM" checklist (Colab route) |
| `requirements.txt` | facilitator | training deps installed into the HF container via `task.set_packages` |

---

## The 4 hours

### Hour 1 — Login & first experiment
- Connect your Colab notebook with the **shared** API key + your name (`WORKSHOP_USER`) →
  `00_setup_credentials.md`. Your runs land in your own project `PlantVillage Workshop/<your-name>`.
- Open `hour1_first_experiment.ipynb`:
  - `Task.init()` — two lines that auto-track code, packages, environment, console, params, plots.
  - EDA: class-distribution bar chart + a sample-leaf grid → **auto-captured** into ClearML PLOTS /
    DEBUG SAMPLES the moment you call `plt.show()`.
- **Look in the UI:** your task under project **`PlantVillage Workshop/<your-name>`** with PLOTS, DEBUG SAMPLES, SCALARS,
  CONFIGURATION, EXECUTION all filled in automatically.

### Hour 2 — GPU training via a shared queue
- Run `hour2_finetune_vit.py` (from a cell: `%run workshop/hour2_finetune_vit.py`):
  - pulls the versioned `plantdisease_demo` dataset with `Dataset.get(...).get_local_copy()`,
  - fine-tunes **ViT-Tiny** with HuggingFace `Trainer(report_to=['clearml'])`,
  - `task.execute_remotely(queue_name='gpu-18gb')` ships the run to a MIG-backed agent.
- **The big moment:** everyone submits at once → **Orchestration → Workers** shows many tasks
  running on the *same* H200, each in its own memory slice, while live loss/accuracy curves and GPU
  utilization stream into each task's SCALARS tab.

### Hour 3 — Compare & find the winner
- In the UI: right-click your run → **Clone** → edit `learning_rate`/`epochs` under CONFIGURATION →
  **Enqueue** to `gpu-18gb`. (HF caveat: set `_ignore_hparams_ui_overrides_ = False` first — noted in the
  notebook.)
- Select 2+ runs → **COMPARE** → scalars graphs, values table, parallel-coordinates.
- `hour3_pick_best_model.ipynb` ranks runs by validation accuracy and prints the winner's
  `output_model_id` + the exact Hour-4 publish command.

### Hour 4 — Model registry & reuse
- `python workshop/hour4_publish_and_infer.py publish --task-id <winner_id>` → publishes the winning
  model (read-only) and tags it `winner`.
- `python workshop/hour4_publish_and_infer.py infer --images <folder>` → pulls that published model
  back **by tag** (models are standalone registry entries), classifies new leaves, and reports a
  labeled grid + confusion matrix. This is the "reuse" half of the loop: a model registered by one
  run, consumed by a separate script.

---

## Facilitator quick-start (before the session, on the H200 VM)

```bash
# 0. deps
pip install clearml clearml-agent
pip install -r workshop/requirements.txt

# GPU queues + MIG agents are ALREADY set up (gpu-18gb ×2, gpu-35gb, gpu-71gb, gpu-141gb).
# Remaining VM work — see facilitator/agent_setup.md:

# 1. create ONE shared login + shared API key, then restart the apiserver   (facilitator/shared_user.md)
docker restart clearml-apiserver

# 2. the shared demo dataset is ALREADY registered (plantdisease_demo). Optionally add the full catalog:
python workshop/hour1_create_dataset.py --data-root dataset --skip-demo

# 3. confirm the MIG agents use a HuggingFace GPU image (torch+transformers+CUDA 12.x), e.g.
#    --docker huggingface/transformers-pytorch-gpu:latest

# 4. make the server reachable from Google Colab + push repo to GitHub   (facilitator/VM_SETUP.md)
```

### Acceptance test (run the whole loop once yourself)
1. `plantdisease_demo` already appears in **Datasets** (project PlantVillage). ✅
2. Workers show on `gpu-18gb` etc. (Orchestration → Workers) — already live.
3. `hour2_finetune_vit.py` → `execute_remotely('gpu-18gb')` → an agent runs it; live loss/accuracy +
   GPU utilization appear; an output model registers.
4. Submit 2–3 at once → confirm concurrent execution across the MIG slices.
5. Clone → tweak → compare two runs in the UI.
6. `hour4 publish --task-id <winner>` then `hour4 infer --images <folder>` → predictions + confusion
   matrix reported. ✅ Green end-to-end = ready.

---

## Notes & gotchas
- **HTTP, not HTTPS:** fine for this internal server. No nginx/TLS needed. (`clearml-init` warns about
  http but still works; attendees set creds in the notebook cell, not the wizard.)
- **The demo dataset is standalone** (not a child of the full dataset) on purpose — a child version
  would inherit all ~20k parent images on `get_local_copy()` instead of the ~1000 we want.
- **GPU sharing here is MIG** (hardware-partitioned instances) — works on open-source ClearML and
  gives the strongest OOM isolation: a job that over-allocates OOMs only inside its own slice.
- **On MIG queues, use a HuggingFace GPU image** (torch+transformers+CUDA 12.x, Hopper-ready), not a
  memory-capping image — MIG already caps VRAM in hardware.
- **Distributed / sharded training** (DDP, FSDP, DeepSpeed) is possible across the 2 H200s but is out
  of scope for this teaching lab (we run many small independent jobs, not one big sharded one).
- Built from this repo's local ClearML docs (`../docs/`) and examples (`../coding_examples/`); the
  `clearml-docs` skill indexes both if you want to dig deeper into any step.
