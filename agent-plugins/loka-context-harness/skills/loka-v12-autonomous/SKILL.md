---
name: loka-v12-autonomous
description: Apply the separate LokaV12 Autonomous Edition on top of LokaV11 for bounded autonomous Agent missions with explicit delegated authority and adaptive recoverability controls.
---

# LokaV12 Autonomous Edition

This is a **second V12 edition**, distinct from the original V12 Supervised
Long-Run Framework. Load it only on top of LokaV11 when the user has explicitly
delegated a bounded mission to a capable Agent.

Start with a mission contract: outcome, non-goals, capability profile, permitted
action classes, environment/scope, exclusions, stop condition, evidence needed,
and recovery route. Delegated authority may cover defined reversible work; it
does not override platform safety, secrecy, excluded actions, or an unclear
trust boundary.

Checkpoint at milestones, before a trust-boundary crossing, after a failed
assumption, before handoff/context loss, and at any agreed maximum interval.
Record the durable delta rather than generating empty report templates.

Stop and escalate when work leaves delegated authority, evidence contradicts
the mission, an irreversible/high-impact action is not explicitly covered,
recovery is unclear after risk, or repeated attempts no longer add evidence.
Report the observed evidence, recovery point, remaining risk, and next safe
action.

Use the standalone prompt at `meta-prompts/LOKA_V12_AUTONOMOUS_EDITION.md`.
