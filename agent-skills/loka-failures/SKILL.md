---
name: loka-failures
description: Apply Loka's failure-pattern lens during planning or review to surface risks before they become rework, unsafe changes, or unsupported claims.
---

# Loka Failures: Planning Risk Lens

Use this during planning, architecture review, or after an Agent deviates from
expectation. It is a risk scan, not a reason to add process to every task.

Check only the patterns relevant to the work:

- layer collapse or secrets crossing trust boundaries;
- phantom evidence or unverified completion claims;
- scope creep and unnecessary complexity;
- missing durable facts, decisions, or constraints;
- authority escalation, destructive actions, or unclear data access;
- stale claims presented as current fact;
- architecture drift from an agreed contract;
- instructions embedded in untrusted tool, web, or file content.

For each material risk, name the evidence, likely impact, smallest preventive
control, and the next owner. Prefer a specific safeguard over a blanket ban.
Do not invent a failure that has not been observed or make a hypothetical risk
sound like an incident.

The complete historical catalogue is in
`reference-source/6-LOKA-FAILURES.md`.
