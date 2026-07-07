---
name: clearml-docs
description: Deep-indexed local search over the ClearML documentation (docs/, 582 pages) and the ClearML coding_examples/ sample repo (128 Python scripts + 18 notebooks). Use this whenever the user asks anything about ClearML — SDK usage (Task, Dataset, Model, Logger, PipelineController, HyperDatasets), clearml-agent, clearml-server, the WebApp UI, clearml.conf configuration, integrations (PyTorch, Keras, TensorFlow, XGBoost, Hugging Face, Hydra, etc.), deployment (clearml-serving, clearml-session, autoscalers, enterprise install), release notes / changelogs, or wants a working code example for a ClearML feature. Trigger on phrases like "how do I ... in ClearML", "clearml example for X", "does ClearML support Y", "what changed in ClearML version Z".
---

# ClearML Docs & Examples Search

This repo contains a full local mirror of the ClearML documentation and its official
coding examples. This skill tells you how to search them fast instead of grepping
blindly or guessing from training-data knowledge (which is often stale — ClearML ships
frequent releases).

Always prefer these local sources over remembered/general knowledge: docs here can be
newer than your training cutoff, and answers should cite the actual local file.

## What's indexed

- `docs/` — 582 scraped ClearML documentation pages (flat `.md` files, each with a
  `url:`/`title:` frontmatter header pointing at the original `clear.ml/docs/latest/...` page).
- `coding_examples/` — the official ClearML examples repo: 128 Python scripts, 18 Jupyter
  notebooks, organized by topic (`frameworks/`, `pipeline/`, `datasets/`, `reporting/`,
  `hyperdatasets/`, `automation/`, `services/`, `router/`, `scheduler/`, `cicd/`,
  `distributed/`, `optimization/`, `advanced/`, `clearml_agent/`).

Two pre-built indexes live alongside this skill so you don't have to re-scan the tree
every time:

- `DOCS_INDEX.md` — every doc page grouped by topic (release_notes, guides, references,
  deploying, webapp, clearml, integrations, getting_started, hyperdatasets, fundamentals,
  etc.), with its real doc path (e.g. `references/sdk/task`), title, and the actual
  filename under `docs/`.
- `CODING_EXAMPLES_INDEX.md` — every example script grouped by directory, with a
  one-line description pulled from its docstring, `task_name=`, or leading comment.
- `docs_index.json` — same data as DOCS_INDEX.md in machine-readable form (fields:
  `file`, `title`, `url`, `path`), useful if you want to grep/filter programmatically.

## How to answer a ClearML question

1. **Identify the topic** and check `DOCS_INDEX.md` for the matching category/path
   first (e.g. a question about Datasets → `clearml_data/*`, `getting_started/data_management`,
   `references/sdk/dataset`; a question about pipelines → `guides/pipeline/*`,
   `references/sdk/automation_controller_pipelinecontroller`).
2. **Grep for the real content** across `docs/` when the index title isn't enough:
   `grep -ril "keyword" docs/` — filenames are long/ugly but `grep -l` handles it fine.
   Filenames encode the doc's URL path (`clear.ml_docs_latest_docs_<path>_.md`), so you
   can reconstruct the original URL from a filename if the user wants a link.
3. **Read the matching file(s) in full** before answering — doc pages are short (usually
   under 300 lines) so read the whole thing, don't guess from a snippet.
4. **For "how do I do X" / "show me an example" questions**, check `CODING_EXAMPLES_INDEX.md`
   for a real script that already does it, then read that script directly — these are
   working, maintained examples straight from ClearML, more reliable than writing code
   from memory. Prefer pointing to / adapting an existing example over inventing new code.
5. **For version/changelog questions** ("what's new in X", "when was Y added"), search
   `release_notes/*` in `DOCS_INDEX.md` — it's organized by component
   (`clearml_agent`, `sdk_open_source`, `appgw`, `apps`, `autoscalers`, etc.) and version.
6. Cite the specific file path(s) you used in your answer (e.g. `docs/clear.ml_docs_latest_docs_clearml_data_.md`
   or `coding_examples/pipeline/pipeline_from_decorator.py`) so the user can open them directly.

## Quick reference: category → where to look

| Topic | docs/ category (see DOCS_INDEX.md) | example dir |
|---|---|---|
| Task / experiment tracking basics | `getting_started/*`, `references/sdk/task` | `reporting/`, `advanced/` |
| Datasets / data versioning | `clearml_data/*`, `getting_started/data_management` | `datasets/` |
| Hyper-Datasets (enterprise) | `hyperdatasets/*`, `references/hyperdataset/*` | `hyperdatasets/` |
| Pipelines | `guides/pipeline/*`, `pipelines/*` | `pipeline/` |
| Hyperparameter optimization | `guides/optimization/*`, `references/sdk/hpo*` | `optimization/hyper-parameter-optimization/` |
| clearml-agent / remote execution | `clearml_agent/*` | `advanced/execute_remotely_example.py`, `automation/` |
| Framework integrations (PyTorch, Keras, TF, XGBoost, sklearn, Hugging Face, Hydra, Fire, Click, ...) | `integrations/*` | `frameworks/<name>/` |
| Reporting (scalars, plots, media, artifacts, models) | `guides/reporting/*` | `reporting/` |
| Distributed training | `guides/distributed/*` | `distributed/` |
| Scheduling / triggers / cron | — | `scheduler/` |
| Services (autoscalers, cleanup, Slack monitoring) | `guides/services/*` | `services/` |
| CI/CD integration | — | `cicd/` |
| Model serving | `clearml_serving/*` | — |
| WebApp UI usage | `webapp/*` | — |
| Deployment / self-hosting / enterprise install | `deploying_clearml/*`, `references/enterprise/*` | — |
| User/project management, roles | `user_management/*` | — |
| Release notes / changelog | `release_notes/<component>/ver_X_Y` | — |

## Regenerating the indexes

If `docs/` or `coding_examples/` change (new pages/examples added), rebuild both index
files — don't hand-edit them. The generation logic is:

- `DOCS_INDEX.md` / `docs_index.json`: for each `docs/*.md`, parse the `url:` and `title:`
  frontmatter fields, derive the doc path from the URL (`/docs/latest/docs/<path>/`),
  group by the first path segment, sort within group.
- `CODING_EXAMPLES_INDEX.md`: walk `coding_examples/` for `*.py` files, extract a
  one-line description from (in order of preference) the module docstring, a
  `task_name="..."` literal, or the first leading `#` comment; group by directory.

Ask the user before doing a full regeneration if it's been a while — a quick `find docs
-newer .claude/skills/clearml-docs/DOCS_INDEX.md` check tells you if anything changed.
