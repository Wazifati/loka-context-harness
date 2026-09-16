---
name: loka-v12-supervised
description: Apply the original LokaV12 Supervised Long-Run Framework on top of LokaV11 for a 1–3 hour coding session with periodic human review and recoverable checkpoints.
---

# LokaV12 Supervised Long-Run

Load this **only on top of LokaV11**. Use it when the user will be available to
review a meaningful 1–3 hour coding session and wants the original V12.1
controls: autonomy level, pre-flight, time/cost ceilings, 30–45 minute
checkpoints, kill switches, rollback discipline, and end-of-session reports.

Do not use it for trivial work, truly unattended runs, production deployment,
real payments, or destructive actions. The original framework deliberately
limits these sessions because its objective is maximum safe progress while a
human remains available.

This is the preserved supervised edition. Do not silently relax or replace its
rules. The full original source is `reference-source/8-LokaV12.pdf`.
