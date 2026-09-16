---
name: loka-build
description: "Govern new implementation after a task is understood: choose the smallest sufficient solution and place it within the project's established architecture. Use with LokaV11 for new code, files, or dependencies; not for a pure refactor or narrow surgical fix."
---

# Loka Build

Use this with LokaV11 after understanding the task and the nearby code. It has
two responsibilities, in this order: decide whether new code is necessary,
then place necessary code in the correct architectural boundary.

## 1. Pre-write check

Before creating a file, adding a dependency, or writing a component, stop at
the first sufficient answer:

1. Is the work required by the task?
2. Does the repository already solve it?
3. Does the language standard library solve it?
4. Does the target platform provide it natively?
5. Is a suitable dependency already installed?
6. Is a small local implementation clearer than a new module?
7. Otherwise, write the minimum new code that satisfies the requirement.

Minimal never means incomplete. Preserve validation, error handling, security,
accessibility, and the project's existing quality constraints. If a shortcut
would remove one, choose the next sufficient option.

## 2. Architecture placement

Before writing, inspect the project's architecture contract if it has one. Use
`ARCH_CONTRACT.md`, `SPEC.md`, or established local conventions as applicable;
do not invent a new architecture during a scoped implementation task.

Keep each change at its appropriate boundary. Delivery or UI code handles the
outside interaction; business logic owns decisions and workflows; persistence
and integration adapters contain infrastructure details; shared utilities stay
dependency-light. Follow the repository's chosen architecture when it differs
from this general model.

If an architecture check is configured, run it at the project-prescribed point
and address a violation rather than moving code merely to avoid the check. If
no executable check exists, inspect imports and dependencies manually and state
that limitation in the final evidence.

Architecture placement wins over a smaller but wrong-layer shortcut. Reuse and
minimality govern how much code is added; they never justify leaking a boundary.

## Routing

Use LokaV11 Surgical Fix Mode for a narrow existing-repository correction. This
bundle does not include a dedicated refactoring skill; for behavior-preserving
structural work, agree an explicit refactoring scope before proceeding. Consult
Loka Failures when a known risk pattern is relevant.
