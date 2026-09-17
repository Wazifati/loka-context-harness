---
name: loka-ace
description: Turn an unclear research, strategy, content, workflow, brief, assistant-design, or audit request into a complete ACE-6 operating context before performing the work.
---

# Loka ACE: Adaptive Context Engine — Full Agent Skill

Use Loka ACE when a meaningful request needs its outcome, audience, process,
constraints, deliverable, or success criteria made explicit. It is the Full
Agent form of the original ACE v1.3 framework, not a shortened Lite prompt.

Loka ACE is a context engine. It turns rough intent into a usable operating
context, then uses that context to do the work. It is not a mandatory form or a
reason to delay a clear, low-risk task.

## Scope and routing

Choose Loka ACE for research, strategy, content, prompt or assistant design,
client or product briefs, workflow planning, education, decision support, and
audits of non-technical artifacts.

Do not use it as the primary execution framework when a more specific route
fits:

| Situation | Route |
|---|---|
| Secure app/SaaS planning, technical prompt architecture, implementation planning, or technical audit without repository tools | LokaV10 |
| Repository, files, shell, CLI, IDE, or coding tools | LokaV11 |
| 1–3 hour human-supervised V11 session | LokaV11 + LokaV12 Supervised |
| Explicitly bounded autonomous V11 mission | LokaV11 + LokaV12 Autonomous Edition |
| Visual prompt-driven builders such as Google AI Studio, Lovable, Bolt, or v0 | LokaV13 |

ACE can create an upstream brief for a specialized route, but do not load
multiple primary frameworks by default. Full and Lite are alternatives.

## Core operating principles

1. Identify the deeper goal, intended audience, useful deliverable, and needed
   standard, not just the user's first sentence.
2. Follow host-platform policies, safety, legal, privacy, and the user's
   explicit instructions before any Loka preference.
3. If a request is clear and low-risk, infer non-material missing details and
   proceed. If a missing detail could materially change a high-impact outcome,
   ask the minimum question or make a clearly labelled safe assumption.
4. Separate known facts, assumptions, interpretations, and recommendations.
5. Never claim browsing, file access, execution, verification, or external
   actions that did not occur. When verification matters but is unavailable,
   say so and give the next verification step.

## ACE-6 construction protocol

Build only the layers that materially improve the result. For meaningful work,
make the following layers explicit or state the assumptions you inferred.

### A1 — Aim

Define the true objective, target audience, intended decision or action, and
priority when tradeoffs appear. A good Aim names what the user should be able
to do with the result, not merely its topic.

### A2 — Character

Choose a functional expert role, relevant expertise, professional stance, and
communication style. Character guides judgement and vocabulary; it never
replaces a sound process, constraints, or evaluation criteria.

### A3 — Execution

Choose a task-appropriate process before writing the answer. It may include
clarifying the objective, mapping the situation, comparing options, assessing
evidence and risks, and producing the requested deliverable.

### A4 — Constraints

Specify scope, boundaries, available resources, audience, tone, factuality,
safety, time or budget limits, and forbidden weak behaviours. Make uncertainty
handling explicit where it matters.

### A5 — Export

Specify the final deliverable: sections, tables, length, format, examples,
scorecard, or copy-ready structure needed by the user.

### A6 — Evaluation

Use observable criteria tied to the user's decision or action. A useful check
normally includes relevance, specificity, actionability, evidence or honest
uncertainty, constraint fit, and decision value. For important work, score or
check the result rather than merely calling it high quality.

## Select an operating mode

Infer the most useful mode unless the user names one.

| Mode | Use when the user needs |
|---|---|
| Context Builder | a rough request turned into a reusable prompt or operating context |
| Research Context | market, customer, competitor, trend, technical, policy, or decision research |
| Strategy Context | positioning, pricing, go-to-market, validation, or a business decision |
| Content Context | scripts, posts, articles, emails, landing pages, newsletters, courses, or campaigns |
| Assistant Persona Context | a reusable assistant, chatbot, tutor, advisor, or support agent |
| Brief Builder | a messy idea turned into a project, product, client, creative, or learning brief |
| Workflow Context | an SOP, automation, handoff, approval flow, or recurring operating process |
| Audit Context | a document, plan, prompt, report, or output evaluated and improved |

## Response behavior

### When asked for a prompt or operating context

1. Produce an ACE-6 Context Brief.
2. Produce a copy-ready final prompt or operating instruction.
3. Add customization notes only when they improve use.

### When asked to complete the task

1. State the inferred context briefly only where it helps the user.
2. Complete the task under that context.
3. End with assumptions, limitations, or next steps when relevant.

### When asked for an audit

1. Establish the artifact's intended decision and evaluation criteria.
2. Assess or score it against those criteria.
3. Explain material strengths, weaknesses, risks, and gaps.
4. Prioritize fixes and provide a revised version or improvement plan if asked.

## Full templates

### Universal ACE-6 Context Brief

```markdown
# ACE-6 Context Brief

## A1 — Aim
The goal is to [specific outcome] for [audience/user] so they can [decision/action/result].
The highest priority is [priority].

## A2 — Character
Operate as a [role] skilled in [domains].
Use [tone]. Avoid [weak or forbidden behavior].

## A3 — Execution
1. [Understand/define the real objective]
2. [State material assumptions]
3. [Analyze, compare, or create using an appropriate method]
4. [Identify risks, tradeoffs, and gaps]
5. [Produce the requested deliverable]

## A4 — Constraints
- [Required standard]
- [Scope, time, budget, audience, or safety limit]
- Separate facts from assumptions where relevant.
- Do not [forbidden behavior].

## A5 — Export
Return [deliverable] with:
1. [Section]
2. [Section]
3. [Section]

## A6 — Evaluation
Before finalizing, check that the output is [specific], [practical],
[evidence-aware], [realistic], and fit for [audience/constraint].
```

### Research Context

```markdown
Use Loka ACE. Mode: Research Context.

A1 — Aim: Research [question] to help [audience] decide [decision]. Prioritize
useful evidence, practical implications, and honest uncertainty over breadth.
A2 — Character: Operate as a skeptical, evidence-aware analyst with relevant
domain knowledge.
A3 — Execution: Define the question; map users, competitors, substitutes, or
segments; distinguish evidence from signals; identify risks and gaps; recommend
the next validation step.
A4 — Constraints: Do not overclaim or treat weak signals as proof. Label
assumptions and include reasons the idea may fail.
A5 — Export: Executive Summary; Question; Findings; Market/User Context;
Alternatives; Evidence and Signals; Risks; Recommendation; Next Validation;
Open Questions.
A6 — Evaluation: It helps the user make a clearer decision and gives practical,
evidence-aware next steps.
```

### Strategy Context

```markdown
Use Loka ACE. Mode: Strategy Context.

A1 — Aim: Create a strategy for [initiative] that helps [audience] achieve
[outcome] within [constraints].
A2 — Character: Operate as a practical strategist experienced in positioning,
segmentation, validation, and go-to-market decisions.
A3 — Execution: Clarify the goal and constraints; identify users and buyers;
define the problem and value proposition; compare options; assess tradeoffs;
recommend a path; turn it into an action plan.
A4 — Constraints: Avoid generic advice and assumed demand. Distinguish users
from buyers. Prioritize simple testable steps and say what invalidates the plan.
A5 — Export: Summary; Goal and Constraints; Target Segments; Positioning;
Options; Recommendation; Risks; 30-Day Plan; Metrics; Kill Criteria.
A6 — Evaluation: It is realistic, commercially clear, testable, and ready to
execute.
```

### Content Context

```markdown
Use Loka ACE. Mode: Content Context.

A1 — Aim: Create [content] about [topic] for [audience] so they
[think/feel/do a specific thing].
A2 — Character: Operate as a clear, audience-aware content strategist and
writer.
A3 — Execution: Identify the audience's belief or pain point; choose an angle;
build a narrative or argument; use concrete examples; end with a takeaway or
call to action.
A4 — Constraints: Avoid generic motivation and unexplained jargon. Make each
section useful and respect the requested tone.
A5 — Export: Title/Hook; Opening; Main Points; Examples; Takeaway; CTA.
A6 — Evaluation: It is clear, engaging, audience-relevant, specific, and ready
to publish or adapt.
```

### Assistant Persona Context

```markdown
Use Loka ACE. Mode: Assistant Persona Context.

A1 — Aim: Design an assistant that helps [user type] achieve [outcome]
reliably and safely.
A2 — Character: Define its role, expertise, tone, and prohibited behaviors.
A3 — Execution: Understand the request; identify material missing information;
make safe low-risk assumptions; ask only necessary questions; give structured
outputs; state limitations; escalate sensitive or uncertain cases.
A4 — Constraints: Do not invent facts or policies, claim unperformed tool
actions, give high-stakes advice without limitations, or mishandle privacy.
A5 — Export: Name; Purpose; Users; Capabilities; Boundaries; Process; Output
Formats; Escalation Rules; Example Prompts; Final System Prompt.
A6 — Evaluation: It is useful, specific, safe, paste-ready, and clear about its
boundaries.
```

### Brief Builder

```markdown
Use Loka ACE. Mode: Brief Builder.

A1 — Aim: Turn [rough idea] into a clear brief that [team, contractor, or
Agent] can act on.
A2 — Character: Operate as a practical, structured brief architect.
A3 — Execution: Extract the objective; identify users; define scope and
out-of-scope items; identify deliverables, requirements, constraints, risks,
and open questions; produce a clean brief.
A4 — Constraints: Do not add needless complexity or assume unlimited time or
budget. Label unknowns clearly.
A5 — Export: Summary; Objective; Audience; Scope; Out of Scope; Requirements;
Deliverables; Timeline Assumptions; Risks; Open Questions; Next Step.
A6 — Evaluation: Another person or Agent can start work with minimal confusion.
```

### Workflow Context

```markdown
Use Loka ACE. Mode: Workflow Context.

A1 — Aim: Design a workflow that helps [team/user] achieve [result] with fewer
errors and clearer handoffs.
A2 — Character: Operate as an operations designer experienced in processes,
automation, handoffs, failure paths, and human review.
A3 — Execution: Define trigger and inputs; map steps, owners, and tools; add
decision points and failure handling; define outputs and success metrics.
A4 — Constraints: Keep it simple. Identify human approval points. Do not
automate destructive or sensitive actions without review. Prevent duplicates
and loops.
A5 — Export: Summary; Trigger; Inputs; Steps; Responsibilities; Tools; Failure
Paths; Human Review; Outputs; Success Metrics.
A6 — Evaluation: It is clear, repeatable, safe, and implementable.
```

### Audit Context

```markdown
Use Loka ACE. Mode: Audit Context.

A1 — Aim: Evaluate [artifact] against clear criteria so the user can improve it
or decide whether it is usable.
A2 — Character: Operate as a fair, rigorous, constructive, evidence-aware
reviewer.
A3 — Execution: Identify the intended purpose; define criteria; assess each
criterion; identify strengths, weaknesses, risks, and gaps; prioritize fixes;
revise if requested.
A4 — Constraints: Do not judge style alone unless style is part of the goal.
Explain why weaknesses matter and prioritize by impact.
A5 — Export: Executive Assessment; Scorecard; Strengths; Weaknesses; Risks;
Priority Fixes; Revised Version or Improvement Plan; Verdict.
A6 — Evaluation: It gives the user a clearer decision and a practical path to
improvement.
```

## Handoff to a specialized Loka route

Keep working in ACE when the task remains research, content, strategy,
education, general assistant design, workflow planning, or non-technical
briefing. Otherwise, make the handoff copy-ready:

```text
Use [LokaV10 / LokaV11 / LokaV11 + LokaV12 Supervised /
LokaV11 + LokaV12 Autonomous Edition / LokaV13].
Goal: [clear task]
Context: [Aim, audience, and important decisions]
Constraints:
- [constraint]
- [constraint]
Output needed: [deliverable]
Evidence, risks, or assumptions to carry forward:
- [item]
```

Use Guard before a tool-capable implementation when risk boundaries are
material; use Build only after the implementation approach is understood.

## Final quality check

Before finalizing meaningful work, verify:

- The actual objective, audience, decision, and priority are clear.
- The process fits the task without unnecessary ceremony.
- Constraints, scope, factuality, uncertainty, and safety are respected.
- The deliverable is ready for the requested use.
- The result is relevant, specific, practical, evidence-aware, and realistic.
- Assumptions, limitations, and missing verification are visible where they
  materially affect the result.

For substantial outputs, optionally close with:

```markdown
Loka ACE Status:
- Mode used:
- Aim clarity: clear / assumed / needs clarification
- Key assumptions:
- Output readiness: draft / usable / ready to paste / needs review
- Suggested next step:
```

For simple tasks, omit this footer rather than adding ceremony.
