# ClearML VM — everything to do before the workshop (Google Colab route)

Attendees run notebooks in **Google Colab** (Google's cloud), each holding their own ClearML API
key, and submit training to the GPU queue. So the VM that hosts ClearML must be **reachable from the
public internet** and have datasets, users, and agents ready. GPU work runs on the MIG agents;
Colab is only a CPU place to write code and call `execute_remotely('gpu-18gb')`.

Flow:
```
Colab (Google cloud) --creds--> ClearML server (202.131.110.56) --gpu-18gb queue--> MIG agent (H200)
```

---

## Already done (verified live via API)
- ✅ 2× H200, MIG-sliced. Queues + agents attached:
  `gpu-18gb` ×2 · `gpu-35gb` · `gpu-71gb` · `gpu-141gb`.

## Still to do — ordered checklist

### 0. (Off the VM) Push the workshop repo to GitHub
Colab clones the code from a public/accessible GitHub repo. Make sure `workshop/` is pushed and note
the URL (attendees will `!git clone` it). **Do not** commit `.env` or `dataset/` (already gitignored).

### 1. Make the ClearML server reachable from the internet  ← critical for Colab
Colab lives on Google's cloud, so it must reach all three ports (already bound to `0.0.0.0` per
`docker ps`):

| Service | Port | Used by Colab for |
|---|---|---|
| Web UI | 80 | attendees log in + view results |
| API | 8008 | all SDK calls (`Task.init`, enqueue, etc.) |
| File server | 8081 | download the demo dataset, upload models/artifacts |

- [ ] Open inbound `80`, `8008`, `8081` in the VM firewall / cloud security group (to the internet,
      or at least to Google's egress ranges).
- [ ] **Test from a truly external network** (or from a Colab cell):
      ```python
      import urllib.request; print(urllib.request.urlopen("http://202.131.110.56:8008/debug.ping").read())
      ```
      (The API already answers from off-VM on our side; confirm it works **from Colab specifically**.)
- ⚠️ **Security:** this exposes ClearML over **plain HTTP** to the internet. Keep it open only for the
      workshop window, and **rotate/revoke the admin API key afterwards** (see step 8). Optionally
      restrict the security group to Google IP ranges.

### 2. Confirm the server's PUBLIC hosts are configured
When a user clicks *Create new credentials → Jupyter Notebook tab*, the snippet uses the server's
configured hosts. They must be the **public IP**, not `localhost`, or the Colab snippet won't connect.
- [ ] Verify the server's web/api/files hosts are `http://202.131.110.56[:port]`.
- Safety net: the workshop notebooks already hardcode the public hosts in their credentials cell, so even a
  mis-generated snippet still works if attendees keep those host lines.

### 3. Create ONE shared login + ONE shared API key  ← not done yet
No per-attendee users. Add a single non-admin `workshop` user to `apiserver.conf`, restart, then
generate **one** API key and share it with everyone. Full steps: **`shared_user.md`**.
```bash
docker restart clearml-apiserver
```
Attendees are separated by their **project name** (`WORKSHOP_USER` = their name), not by login — so
they all use the same key. Hand out: the shared access/secret key + "set `WORKSHOP_USER` to your name".

### 4. Register the datasets  ← demo ✅ done; full catalog optional
`plantdisease_demo` (~1000 imgs, the shared training set) is **already registered** in project
**PlantVillage** — the workshop runs on it as-is. It's **one shared copy**; each training run binds to
it automatically via `Dataset.get(..., alias=...)`, so the UI shows data→experiment lineage.

Optionally add the full 15-class catalog (for the EDA "whole dataset" view). Run on the VM — the
`--skip-demo` flag avoids duplicating the demo:
```bash
pip install clearml
export CLEARML_API_HOST=http://localhost:8008 CLEARML_FILES_HOST=http://localhost:8081
export CLEARML_API_ACCESS_KEY=... CLEARML_API_SECRET_KEY=...    # admin
python workshop/hour1_create_dataset.py --data-root dataset --skip-demo
```
> Note: Colab kernels download `plantdisease_demo` (~1000 imgs) from the file server (8081) over the
> internet — small, so fine. The "data on local VM storage" benefit applies to the agents, not Colab.

### 5. Make sure the MIG agents run in Docker mode  ← verify (no custom image to build)
The task sets its own image + packages (`hour2` calls `set_base_docker("huggingface/transformers-pytorch-gpu:latest")`
+ `set_packages("requirements.txt")`), so there's **nothing to build**.
- [ ] Confirm each agent was started with `--docker` (Docker mode). If any run in venv mode,
      `set_base_docker` is ignored — restart them with `--docker`. Details: **`agent_setup.md`**.
- [ ] `docker pull huggingface/transformers-pytorch-gpu:latest` on the agent hosts (avoid a slow
      first-task image pull) and set `agent.docker_pip_cache` so the extra-package install is cached.
- [ ] Agent hosts need **outbound internet** (to pull the image + the extra pip deps).

### 6. Capacity & disk headroom
- [ ] Ensure the server has RAM/disk for 30 concurrent users (Elasticsearch + MongoDB + file server).
- [ ] File-server disk: 30 × (ViT-Tiny model ~20 MB + a little artifact data) + the datasets ≈ a few
      GB. Confirm free space on the `clearml-fileserver` volume.

### 7. Warm-up & external smoke test (do this before attendees join)
- [ ] `docker pull huggingface/transformers-pytorch-gpu:latest` on the agent hosts.
- [ ] From a **Colab notebook** (not the VM): set os.environ with an admin/test key → `Task.init` →
      `%run hour2_finetune_vit.py` → confirm it enqueues to `gpu-18gb`, a MIG agent runs it, live
      loss/accuracy + GPU utilization show, and an output model registers.
- [ ] Do one full clone → compare → publish → infer loop from Colab. Green = ready.

### 8. After the workshop
- [ ] Revoke/rotate the admin key used above **and** the shared `workshop` API key.
- [ ] Close inbound `80/8008/8081` (or re-restrict the security group).
- [ ] Optionally remove the `workshop` user from `apiserver.conf` + restart.

---

## Quick status recap
| Item | Status |
|---|---|
| MIG queues + agents | ✅ done |
| Internet reachability (80/8008/8081) | ⚠️ verify from Colab |
| Public hosts configured | ⚠️ verify |
| 1 shared user + key | ❌ create (`shared_user.md`) |
| Shared demo dataset | ✅ done (`plantdisease_demo`) |
| Full catalog (optional) | ⬜ run `hour1_create_dataset.py --skip-demo` |
| Agents in Docker mode | ⚠️ verify (`--docker`); image comes from the task |
| Repo on GitHub for Colab | ❌ push |
| Warm-up smoke test from Colab | ❌ do last |
