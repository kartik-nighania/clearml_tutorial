# clearml_tutorial

A local reference repo for learning/using ClearML: a full docs mirror plus the official
coding examples repo.

## Layout

- `docs/` — 582 scraped pages of the official ClearML documentation (flat `.md` files,
  each with `url:`/`title:` frontmatter linking back to the original `clear.ml/docs/latest/...` page).
- `coding_examples/` — the official ClearML examples repo (128 Python scripts, 18 notebooks),
  organized by topic: `frameworks/`, `pipeline/`, `datasets/`, `reporting/`, `hyperdatasets/`,
  `automation/`, `services/`, `router/`, `scheduler/`, `cicd/`, `distributed/`, `optimization/`,
  `advanced/`, `clearml_agent/`.
- `clearml_docs.zip` — original zip archive `docs/` was extracted from (kept as source of truth
  for re-extraction if needed).

## Answering ClearML questions

Use the **clearml-docs** skill for anything ClearML-related — SDK usage, clearml-agent,
clearml-serving, WebApp, integrations, deployment, release notes, or working code examples.
It has pre-built topic indexes (`DOCS_INDEX.md`, `CODING_EXAMPLES_INDEX.md`) so you don't
need to grep the whole tree blind. Prefer these local docs/examples over general/remembered
knowledge — ClearML ships frequently and local docs may be newer than training data.
