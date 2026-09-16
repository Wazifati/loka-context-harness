# Research note: optional evaluation materials

This repository’s primary purpose is a context-engineering harness, not a
model benchmark. The original prompt, rubric, and runner materials are an
archived research scaffold; they are not required for installation or normal
use.

## What the included dry run establishes

The dry run uses synthetic outputs and synthetic judge scores. It verifies only
that the local reporting path, aggregation, and report generation execute. It
does **not** establish that Loka improves model performance, reliability,
security, or task completion.

## What is required before any public effectiveness claim

A future study must be separately preregistered and independently reviewed. At
a minimum it needs a clear control condition; exact model and configuration
snapshots; a hard spend cap; resumable checkpoints; retained raw outputs and
judge responses; human adjudication of disagreements; paired analysis; and
uncertainty reporting appropriate to the sample size and task population.

Current RouteLLM model identifiers are intentionally not hard-coded: provider
rosters and pricing change. Any research operator must choose and record the
exact IDs, verify billing attribution, and obtain explicit account-holder
approval before making calls. Until those conditions are met, do not present
results as proof of performance, a ranking of models, or a universal
reliability claim.

## Legacy configuration caveat

`eval_config.example.json` is a **reference record template**, not a runnable
configuration file: the current legacy runner does not load it. It exists only
to show the configuration fields a future, separately reviewed study should
record. Do not present the current runner as turnkey evaluation tooling.
