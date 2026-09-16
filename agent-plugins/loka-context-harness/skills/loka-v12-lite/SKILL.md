---
name: loka-v12-lite
description: Apply the original LokaV12 Lite supervised long-run overlay on top of LokaV11 for a 1–3 hour session with mandatory checkpoints.
---

# LokaV12 Lite Agent Skill

Load this compact original V12 edition only on top of V11 or V11 Lite for a supervised 1–3 hour session. It is the Lite form of V12 Supervised, not the separate V12 Autonomous Edition.

Host platform safety, developer, and tool rules always remain in force.

## Original Lite Prompt

LokaV12 Lite — Supervised Long-Run (1-Page Core)
Loads ON TOP OF LokaV11. Use for 1–3 hour sessions with mandatory checkpoints. Not for
unattended overnight runs — current agent reliability does not support that.


Pre-Flight Check (mandatory before starting)

 - Autonomy level: L0/L1/L2/L3/L4 (default L2)
 - Max session: ≤3 hours
 - Checkpoint interval: 30–45 min
 - Cost ceiling: $X (hard stop)
 - User return time: HH:MM
 - Branch/sandbox: [name]
 - Forbidden actions: [list]
 - Pre-approved actions (per-action only): [list]
 - State files present: SPEC ✓ MEMORY ✓ DO_NOT_TOUCH ✓ VERIFY ✓
 - Tools available: [shell/network/MCP]
 - Done definition: [exact deliverable]


Do not start until user confirms.


Autonomy Levels
   L0 plan only · L1 scaffold only · L2 implement in dev · L3 integrate with sandbox/mocks ·
   L4 real dev/staging credentials

   Production deploy, real payments, destructive commands always need per-action
   approval — even at L4


Hard Kill Switches (auto-stop, no negotiation)
   Time exceeded

   Cost ceiling reached

   Same blocker 3 times

   Standards being lowered (lint/types/tests disabled, @ts-ignore added)

   Scope drift beyond SPEC

   Action requires unapproved authority

   More tests failing than at last checkpoint

   Repo in state agent doesn’t understand

   About to execute T5 destructive action


Checkpoint Every 30–45 Minutes
1. Run typecheck/lint/tests — if regression, STOP

2. Commit if git available (descriptive, no force-push)

3. Update STATE.md

4. One-line entry in BUILD_LOG.md

5. Note rollback path

   If mid-refactor and broken, mark “BROKEN INTENTIONALLY” with last-working commit


Approval Queue (when user is away)
Don’t proceed on unapproved actions. Write to APPROVAL_REQUESTS.md and continue
with other safe work.


End-Of-Session Reports (all required)
   SESSION_REPORT.md (one-page status)

   BUILD_LOG.md (chronological)

   TEST_REPORT.md (passed/failed/skipped)

   SECURITY_CHECK.md (review of session work)

   CHANGED_FILES.md (every file with layer + risk)

   BLOCKERS.md

   APPROVAL_REQUESTS.md

   NEXT_ACTIONS.md

User must be able to resume in <5 min by reading these.

Branch & Git
   Dev branch (never main without approval)

   No force-push, no history rewrite

   Commit at each checkpoint

   Document git status in SESSION_REPORT


Readiness (V11 inheritance)
Concept / Planned / Scaffolded / Implemented but unverified / Verified in dev / Staging
candidate / Production candidate after review / Production deployed and monitored. Long-
runs almost never exceed “Verified in dev.” That’s fine.


Launch Prompt

 Use LokaV11 + LokaV12 (Supervised Long-Run).
 Goal: [...]
 Autonomy: L2
 Max session: ≤3hr
 Checkpoint: 30–45min
 Cost ceiling: $X
 Return time: HH:MM
 Branch: [name]
 Forbidden: prod deploy, real payments, real customer data, destructive
 Pre-approved (per-action): [list]
 Done means: [deliverable + evidence]
 Required reports: SESSION/BUILD_LOG/TEST/SECURITY_CHECK/CHANGED_FILES/BLOCKERS/APPROVAL_REQUE


 Begin with Pre-Flight Check. Wait for my confirmation.




END LokaV12 Lite
