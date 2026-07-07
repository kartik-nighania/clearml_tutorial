# Attendee setup — connect your Colab notebook

**Server:** http://202.131.110.56 · **You need:** a browser + a Google account. Notebooks run in
**Google Colab**; training is submitted to a GPU queue on the server.

## The idea: one shared key, your own project
Everyone uses the **same** ClearML login + API key (given to you by the facilitator). You tell your
work apart by setting **`WORKSHOP_USER`** to *your name* — all your experiments then land in your own
project **`PlantVillage Workshop/<your-name>`**, and the dataset is shared by everyone.

## 1. Open the notebook in Colab
Open `hour1_first_experiment.ipynb` in Google Colab (via the repo's *Open in Colab* link, or
`File → Open notebook → GitHub`).

## Packages to install in Colab
Colab already has `torch`, `numpy`, `pandas`, `matplotlib`, `seaborn`, `scikit-learn`, `pillow`. The
**training** stack (torchvision, datasets, accelerate, …) runs on the **agent**, not in your notebook.
So in each Colab session you only run:

```python
!pip install -q clearml transformers
```

- `clearml` — every hour (talk to the server).
- `transformers` — only Hour 4's local inference needs it; installing it up front is harmless.
- Do **not** `pip install -r requirements.txt` in Colab — that's the full agent/training env, overkill here.

## 2. Fill in the first cell
The first code cell already has the shared hosts. Paste the **shared** access/secret key from the
facilitator between the quotes, and set `WORKSHOP_USER` to **your name**:

```python
import os
os.environ['CLEARML_WEB_HOST']       = 'http://202.131.110.56'
os.environ['CLEARML_API_HOST']       = 'http://202.131.110.56:8008'
os.environ['CLEARML_FILES_HOST']     = 'http://202.131.110.56:8081'
os.environ['CLEARML_API_ACCESS_KEY'] = 'PASTE_SHARED_ACCESS_KEY'   # same for everyone
os.environ['CLEARML_API_SECRET_KEY'] = 'PASTE_SHARED_SECRET_KEY'   # same for everyone
os.environ['WORKSHOP_USER']          = 'alice'                     # <-- YOUR name (letters/dashes)
```

> We use plain `os.environ = '...'`, **not** `%env`, on purpose — `%env` treats `""` as a literal
> two-char value (not empty) and swallows `#` comments into the value. Colab supports `os.environ`
> exactly like any Python; it's the reliable choice.

Run it **first**, before any `from clearml import ...`. Every `Task.init()` after that reports to
your own project on the workshop server. Use the **same `WORKSHOP_USER`** in every hour's notebook so
all your runs stay together.

> **Prefer a `.env` file?** If you leave the values blank, the next cell auto-falls back to a `.env`
> file (via `python-dotenv`, `override=True`) — put the five `CLEARML_*` vars + `WORKSHOP_USER` in a
> `.env` next to the notebook. Handy for local runs. (In Colab you'd upload/create the `.env`
> yourself, since it isn't in the cloned repo — filling the cell is usually simpler there.)

## 3. Which GPU queue does training use?
Hour 2 submits training to a GPU queue (the server slices its H200s into VRAM tiers):

| Queue | VRAM | Slots | Use it for |
|---|---|---|---|
| `gpu-18gb` | 18 GB | 2 | **default** — ViT-Tiny fits easily here |
| `gpu-35gb` | 35 GB | 1 | bigger batch / model |
| `gpu-71gb` | 71 GB | 1 | large jobs |
| `gpu-141gb` | 141 GB | 1 | whole card |

`gpu-18gb` is already the default in `hour2_finetune_vit.py`. Check **Orchestration → Queues** in the
UI: if a tier has an **idle worker**, your task starts immediately; if all are busy you're in line
(runs finish in seconds) — or pick a tier with a free slot.

## Notes / troubleshooting
- **Everyone shares the key** — that's intentional. Your runs are separated by `WORKSHOP_USER`, not by
  login. Don't change the hosts or keys; only change `WORKSHOP_USER`.
- **The dataset is shared** — you don't upload anything; the notebooks `Dataset.get(...)` the common
  copy the facilitator registered.
- **HTTP is fine** — internal server, no HTTPS needed.
- **Colab install:** run the `!pip install ...` cell once per session (Colab starts fresh each time).
- **Repo:** the notebooks are opened from GitHub in Colab; the training scripts are cloned by a setup
  cell (or `!git clone <repo-url>`), ask the facilitator for the URL.
