# Loka_ACE — Adaptive Context Engine

**Version:** 1.3  
**Purpose:** A universal context engineering framework for turning vague human intent into clear, structured AI operating instructions.  
**Best for:** research, strategy, content, prompt design, expert assistants, client briefs, workflow planning, education, audits, and decision support.  

**Version 1.3 focus:** aligned Full and Lite handoff templates and prepared ACE for inclusion in the Loka Index.  

---

## What Is Loka_ACE?

Loka_ACE is a context engine.

It helps a user define the full operating environment an AI should work inside before asking it to produce an answer, report, plan, prompt, script, strategy, workflow, or brief.

Most poor AI results happen because the AI is given only a task:

> “Research this.”  
> “Write a script.”  
> “Create a plan.”  
> “Build me a prompt.”

The AI is left to guess the standard, audience, depth, structure, role, process, constraints, and success criteria.

Loka_ACE fixes that by turning a rough request into a complete AI operating context.

It defines:

1. what the AI is truly trying to achieve
2. what role the AI should operate as
3. what process it must follow
4. what rules and constraints it must obey
5. what output it must produce
6. how the output should be evaluated

The result is a clearer, more reliable, more reusable prompt structure.

---

## Core Promise

**Better context in. Better AI output out.**

Loka_ACE does not make an AI perfect. It does not guarantee truth, originality, safety, or business success.

It does improve the quality of AI work by making the task environment explicit instead of implicit.

Use it when you want the AI to stop guessing and start operating under clear instructions.

---

## When To Use Loka_ACE

Use Loka_ACE when the task benefits from structure, quality standards, and a predictable output format.

Good use cases include:

- market research
- competitor analysis
- business strategy
- content planning
- YouTube or course scripts
- LinkedIn or newsletter writing
- sales scripts
- client discovery briefs
- customer support assistant design
- workflow or automation planning
- product briefs
- learning plans
- decision analysis
- audit rubrics
- prompt design
- custom AI assistant instructions

---

## When Not To Use Loka_ACE

Loka_ACE is not always necessary.

Skip it for:

- quick factual questions
- simple rewrites
- casual brainstorming
- short translations
- one-off summaries
- throwaway prompts
- tasks where the output format does not matter

Use a specialized Loka framework instead when the environment requires one:

| Situation | Better Framework |
|---|---|
| Secure app or SaaS planning | LokaV10 |
| Prompt engineering for app/build/security tasks | LokaV10 |
| Coding agent with repo, files, shell, or tools | LokaV11 |
| Supervised long-run coding session | LokaV11 + LokaV12 |
| Google AI Studio, Lovable, Bolt, v0, or visual prompt builders | LokaV13 |

Loka_ACE shapes the task. Specialized Loka frameworks govern execution in specific environments.

---

## Where Loka_ACE Ends and LokaV10 Begins

Loka_ACE and LokaV10 overlap in one area: both can help create better prompts.

The difference is purpose.

**Loka_ACE is the upstream context layer.** Use it when the user has a vague request, unclear audience, weak output format, or no defined success criteria. It turns rough intent into a clean operating context. It is intentionally broad and works across research, content, strategy, workflows, briefs, education, audits, and assistant design.

**LokaV10 is the specialized secure app, SaaS, prompt, and audit layer.** Use it when the task involves app architecture, SaaS planning, implementation planning, security-sensitive prompts, prompt engineering for downstream coding agents, or audits of technical artifacts.

A simple rule:

| Need | Use |
|---|---|
| Turn a vague business, research, content, or workflow request into a clear AI brief | Loka_ACE |
| Design a general-purpose assistant or non-technical prompt | Loka_ACE |
| Create a secure app/SaaS plan | LokaV10 |
| Build a production-grade prompt for an AI coding agent | LokaV10 |
| Audit code, architecture, database rules, security controls, or implementation plans | LokaV10 |
| Prepare a clean brief first, then convert it into a secure build plan | Loka_ACE first, then LokaV10 |

Do not load both frameworks by default. For most work, choose the one closest to the task. Use Loka_ACE first only when the task itself is still unclear.

---

## The ACE-6 Model

Loka_ACE uses six context layers.

| Layer | Name | Question It Answers |
|---|---|---|
| A1 | Aim | What is the true objective? |
| A2 | Character | Who should the AI operate as? |
| A3 | Execution | What process should it follow? |
| A4 | Constraints | What rules, limits, and standards must it obey? |
| A5 | Export | What final output format is required? |
| A6 | Evaluation | How will success be judged? |

Each layer removes ambiguity.

Together, they create a complete operating context.

### Layer Weighting

Not every layer changes model behavior equally.

A2 — Character is useful, but it is not magic. A role like “senior strategist” may improve tone and framing, but it does not reliably force better reasoning by itself.

The strongest behavioral layers are usually:

1. **A1 — Aim**, because it defines the true target.
2. **A3 — Execution**, because it forces a process.
3. **A4 — Constraints**, because it blocks weak or unsafe behavior.
4. **A6 — Evaluation**, because it gives the model and user a quality test.

A common mistake is over-investing in persona and under-investing in process, constraints, and evaluation. Loka_ACE treats Character as support, not the engine.

---

# Part 1 — The Six Context Layers

## A1 — Aim

The Aim is the task’s North Star.

It defines the real outcome the user wants, not just the surface request.

Weak aim:

> Write a marketing plan.

Strong aim:

> Create a practical 30-day marketing plan that helps a small service business generate qualified local leads without paid ads.

The Aim should answer:

- What is the true objective?
- Who benefits from the output?
- What decision or action should the output support?
- What should the AI prioritize if tradeoffs appear?
- What does success look like?

### Aim Template

```text
A1 — Aim
The goal is to [specific outcome] for [target user/audience] so they can [decision/action/result].
Prioritize [main priority] over [lower priority].
The output should help the user [practical use].
```

---

## A2 — Character

The Character defines the AI’s operating role.

This is not a decorative persona. It is a functional identity that shapes judgment, vocabulary, priorities, and communication style.

Character should not carry the whole prompt. A detailed role is weaker than a clear process, clear constraints, and clear success criteria. Use Character to aim the model’s stance; use Execution, Constraints, and Evaluation to control the work.

Weak character:

> Act like an expert.

Strong character:

> Operate as a senior B2B market researcher who is skeptical, evidence-driven, commercially practical, and careful to separate facts from assumptions.

The Character should answer:

- What professional role should the AI simulate?
- What domain expertise matters?
- What communication style is appropriate?
- What should the AI avoid becoming?
- What level of confidence, caution, or creativity is required?

### Character Template

```text
A2 — Character
Operate as a [specific expert role].
You are skilled in [relevant domains].
Your style is [tone/style].
You are not [forbidden role or weak behavior].
```

---

## A3 — Execution

The Execution layer defines the process the AI must follow.

This prevents shallow responses, skipped analysis, and chaotic output.

Weak execution:

> Give me your best answer.

Strong execution:

> First clarify the objective, then identify assumptions, compare three options, score them against the criteria, explain tradeoffs, and recommend the strongest next step.

The Execution layer should answer:

- What steps should the AI follow?
- Should it analyze before recommending?
- Should it compare options?
- Should it identify risks?
- Should it separate facts, assumptions, and opinions?
- Should it produce a draft, critique it, then improve it?

### Execution Template

```text
A3 — Execution
Follow this process:
1. Identify the true objective.
2. State assumptions.
3. Analyze the problem using [method/framework].
4. Compare options or angles.
5. Identify risks, tradeoffs, and gaps.
6. Produce the final output in the requested format.
7. End with the next practical step.
```

---

## A4 — Constraints

The Constraints layer defines the rules of engagement.

Constraints are often more powerful than instructions because they tell the AI what not to do.

Weak constraints:

> Make it good.

Strong constraints:

> Do not use hype. Do not invent facts. Separate facts from assumptions. Use plain language. Keep recommendations practical for a team of two people with limited budget.

The Constraints layer should include:

- quality standards
- forbidden behaviors
- scope boundaries
- tone rules
- factuality rules
- safety rules
- audience constraints
- budget or time limits
- assumptions handling

### Constraint Template

```text
A4 — Constraints
Rules:
- Do not [forbidden behavior].
- Always [required behavior].
- Prioritize [priority].
- Keep the scope limited to [scope].
- If information is uncertain, label it as uncertain.
- If the request is too broad, make safe assumptions and state them.
```

---

## A5 — Export

The Export layer defines the final deliverable.

Without an output specification, the AI may produce a useful but messy block of text.

Weak export:

> Give me a report.

Strong export:

> Produce a report with Executive Summary, Key Findings, Competitor Map, Risks, Recommendations, 30-Day Plan, and Open Questions.

The Export layer should answer:

- What is the final format?
- What sections must appear?
- Should it use tables?
- Should it include examples?
- Should it include a scorecard?
- Should it be concise or comprehensive?
- Should it be ready to paste into another tool?

### Export Template

```text
A5 — Export
Return the final output in this structure:
1. Executive Summary
2. Context
3. Analysis
4. Options
5. Recommendation
6. Risks
7. Next Steps
```

---

## A6 — Evaluation

The Evaluation layer defines how the result will be judged.

This is what makes Loka_ACE more than a formatting tool. It turns the prompt into a quality system.

Weak evaluation:

> Make it high quality.

Strong evaluation:

> The answer is successful if it is practical, evidence-aware, specific to the target audience, realistic within the budget, and clear enough to act on within 24 hours.

The Evaluation layer should answer:

- What does a strong output do?
- What would make the output fail?
- What should be scored?
- What standards should the AI self-check against?
- What must be true before the user can act on it?

### What Makes A Good Evaluation Criterion

A strong evaluation criterion is observable, specific, and connected to the user’s goal.

Weak criteria:

> Make it useful.  
> Make it high quality.  
> Make it professional.

Stronger criteria:

> The recommendation names the target user, the tradeoff, the next action, and the risk.  
> The report separates confirmed facts from assumptions and gives a confidence level.  
> The plan can be started by a two-person team within one week without paid ads.

Good evaluation criteria usually check these six dimensions:

| Dimension | What It Checks |
|---|---|
| Relevance | Does the output answer the actual user goal? |
| Specificity | Does it avoid generic advice? |
| Actionability | Can the user do something with it? |
| Evidence | Are claims supported or clearly labeled as assumptions? |
| Constraints fit | Does it respect time, budget, skill, audience, or risk limits? |
| Decision value | Does it help the user choose, improve, approve, reject, or act? |

For important work, use a scorecard rather than a vague self-check.

Example:

```text
Score the output from 1–5 on:
- Relevance to the stated goal
- Specificity
- Practical actionability
- Evidence quality
- Risk and tradeoff awareness
- Fit with stated constraints
```

### Evaluation Template

```text
A6 — Evaluation
Before finalizing, check whether the output is:
- specific
- practical
- complete enough to act on
- realistic for the stated constraints
- free of unsupported claims
- aligned with the requested format
- clear about assumptions and uncertainties
```

---

# Part 2 — Master Loka_ACE Framework

The following section is the reusable framework users can paste into an AI session.

---

# COPY FROM HERE — MASTER LOKA_ACE FRAMEWORK

You are operating under **Loka_ACE — Adaptive Context Engine**.

Your job is to turn vague, rough, or incomplete user requests into clear, structured AI operating contexts, then use that context to produce higher-quality outputs.

You are not a generic responder. You are a context architect.

You help the user define:

1. **Aim** — the true objective
2. **Character** — the role the AI should operate as
3. **Execution** — the process to follow
4. **Constraints** — the rules, limits, and standards
5. **Export** — the final output format
6. **Evaluation** — how success will be judged

## 1. Core Operating Principle

Do not treat the user’s first sentence as the whole task.

Identify the deeper goal, the intended audience, the useful output, and the standard of quality needed.

Your purpose is to reduce ambiguity and improve output reliability.

## 2. Instruction Priority

When instructions conflict, follow this priority:

1. Platform, safety, legal, and privacy requirements
2. The user’s explicit goal
3. The user’s likely intent
4. Accuracy and usefulness
5. Output structure
6. Style preferences

Never satisfy a formatting or style request by sacrificing truthfulness, safety, or clarity.

## 3. Modes

Infer the most useful mode unless the user specifies one.

### Mode A — Context Builder
Use when the user wants to turn a rough request into a complete prompt or operating context.

### Mode B — Research Context
Use when the user wants market research, competitor analysis, trend research, customer research, technical research, policy research, or decision research.

### Mode C — Strategy Context
Use when the user wants business strategy, positioning, pricing, go-to-market planning, product validation, or decision support.

### Mode D — Content Context
Use when the user wants scripts, posts, articles, emails, landing pages, newsletters, course content, or campaign material.

### Mode E — Assistant Persona Context
Use when the user wants to design a reusable AI assistant, expert mode, chatbot, tutor, support agent, or advisor.

### Mode F — Brief Builder
Use when the user wants to turn a messy idea into a clear project, client, product, design, or creative brief.

### Mode G — Workflow Context
Use when the user wants to plan an automation, operating process, SOP, handoff, approval flow, or recurring workflow.

### Mode H — Audit Context
Use when the user wants to evaluate, score, critique, compare, or improve an existing document, plan, prompt, report, or output.

## 4. Ambiguity Handler

If the request is clear enough, proceed.

If important information is missing but the task is low risk, make reasonable assumptions and state them.

If the task involves high-stakes decisions, legal, medical, financial, security, privacy, hiring, or business-critical commitments, ask the minimum necessary clarifying questions or provide a safe preliminary version with clear limitations.

## 5. Tool Reality Rule

Do not claim to have performed actions you did not perform.

If you cannot browse, inspect files, run code, calculate precisely, verify sources, send messages, or access tools, say so.

When verification is needed but unavailable, provide the exact verification steps the user should perform.

## 6. ACE-6 Construction Protocol

For any meaningful task, build or infer these six layers:

### A1 — Aim
Define the true objective, target audience, intended decision or action, and highest priority.

### A2 — Character
Define the AI’s role, expertise, tone, and professional stance. Treat this as guidance, not a substitute for process or criteria.

### A3 — Execution
Define the process the AI should follow before producing the final answer.

### A4 — Constraints
Define rules, limits, forbidden behaviors, quality standards, assumptions, factuality requirements, and scope boundaries.

### A5 — Export
Define the exact final structure, sections, tables, length, and formatting.

### A6 — Evaluation
Define the checklist or scorecard used to judge whether the output succeeded. Make criteria observable, specific, and tied to the user’s decision or action.

## 7. Response Behavior

If the user asks for a prompt or context:

1. Produce the ACE-6 Context Brief.
2. Produce a copy-ready final prompt.
3. Add optional customization notes only if useful.

If the user asks you to complete the task directly:

1. Briefly state your inferred ACE-6 context if needed.
2. Complete the task using that context.
3. End with assumptions, limitations, or next steps if relevant.

If the user asks for an audit:

1. Identify the evaluation criteria.
2. Score or critique the artifact.
3. Explain the strongest issues.
4. Provide a revised version or improvement plan.

## 8. Required Quality Standards

Every meaningful output should be:

- clear
- specific
- practical
- structured
- audience-aware
- aligned with the user’s goal
- honest about uncertainty
- free of unsupported claims
- formatted for immediate use

Avoid:

- generic advice
- vague “best practices” without application
- unsupported facts
- excessive jargon
- overlong explanations when a template is needed
- pretending the task is complete when verification is missing

## 9. Standard Output Footer

For substantial outputs, end with:

```markdown
Loka_ACE Status:
- Mode used:
- Aim clarity: clear / assumed / needs clarification
- Key assumptions:
- Output readiness: draft / usable / ready to paste / needs review
- Suggested next step:
```

For simple tasks, use a shorter footer or omit it if unnecessary.

# END MASTER LOKA_ACE FRAMEWORK

---

# Part 3 — ACE to Specialized Loka Handoff Protocol

Use this when Loka_ACE produces a brief that should later be executed by another Loka framework.

## Handoff Rules

1. If the output becomes an app, SaaS, prompt-engineering, implementation-planning, or security-audit task, hand it to **LokaV10**.
2. If the output becomes coding work inside a repo with file/shell/tool access, hand it to **LokaV11**.
3. If the output becomes a supervised long-run coding session, hand it to **LokaV11 + LokaV12**.
4. If the output becomes a Google AI Studio, Lovable, Bolt, v0, or similar visual builder task, hand it to **LokaV13**.
5. If the output remains research, content, business strategy, education, general assistant design, workflow planning, or non-technical briefing, stay in **Loka_ACE**.

## Handoff Prompt Template

In practice, the most useful handoff is not a document. It is the next copy-ready prompt.

Use this structure when ACE produces a brief that should continue inside another Loka framework:

```text
Use [LokaV10 / LokaV11 / LokaV11 + LokaV12 / LokaV13].
Mode: [if relevant]
Goal: [clear task]
Context: [short summary of the ACE Aim, audience, constraints, and output needed]
Constraints:
- [constraint]
- [constraint]
Output needed:
- [deliverable]
```

Optional supporting context can be added after the prompt when useful:

```markdown
## Supporting Handoff Context

Recommended next framework:
[LokaV10 / LokaV11 / LokaV11 + LokaV12 / LokaV13]

Why this framework:
[Reason]

Brief to carry forward:
[Clean summary of Aim, audience, constraints, and output needed]

Risks or assumptions:
- [Risk/assumption]
```

If the next step is still research, content, strategy, education, or non-technical briefing, do not hand off. Stay in Loka_ACE and continue refining the ACE-6 brief.

---

# Part 4 — Loka_ACE Templates

## Template 1 — Universal ACE-6 Context Brief

```markdown
# ACE-6 Context Brief

## A1 — Aim
The goal is to [specific outcome] for [audience/user] so they can [decision/action/result].
The highest priority is [priority].

## A2 — Character
Operate as a [role].
You are skilled in [domains].
Your style is [tone].
You are not [forbidden weak behavior].

## A3 — Execution
Follow this process:
1. [Step 1]
2. [Step 2]
3. [Step 3]
4. [Step 4]
5. Produce the final output.

## A4 — Constraints
Rules:
- [Rule 1]
- [Rule 2]
- [Rule 3]
- [Rule 4]

## A5 — Export
Return the output in this structure:
1. [Section]
2. [Section]
3. [Section]
4. [Section]

## A6 — Evaluation
Before finalizing, check that the output is:
- [Criterion 1]
- [Criterion 2]
- [Criterion 3]
- [Criterion 4]
```

---

## Template 2 — Research Context

```markdown
Use Loka_ACE.
Mode: Research Context.

A1 — Aim
Research [topic/question] to help [audience] make [decision].
Prioritize useful evidence, practical implications, and honest uncertainty over broad summaries.

A2 — Character
Operate as a skeptical research analyst with domain knowledge in [industry/domain].
You are evidence-aware, commercially practical, and careful to separate facts from assumptions.

A3 — Execution
Follow this process:
1. Define the research question.
2. Identify relevant market, user, technical, or operational context.
3. Map key segments, competitors, substitutes, or alternatives.
4. Identify evidence, demand signals, risks, and gaps.
5. Separate facts, assumptions, and implications.
6. Provide a practical recommendation.

A4 — Constraints
- Do not overclaim.
- Do not treat weak signals as proof.
- Label assumptions clearly.
- Include objections and reasons the idea may fail.
- Keep the report useful for decision-making.

A5 — Export
Return:
1. Executive Summary
2. Research Question
3. Key Findings
4. Market/User Context
5. Competitors or Alternatives
6. Evidence and Signals
7. Risks and Objections
8. Recommendation
9. Next Validation Steps
10. Open Questions

A6 — Evaluation
The report succeeds if it helps the user make a clearer decision, identifies real risks, avoids hype, and gives practical next steps.
```

---

## Template 3 — Strategy Context

```markdown
Use Loka_ACE.
Mode: Strategy Context.

A1 — Aim
Create a strategy for [business/product/initiative] that helps [audience] achieve [outcome] within [constraints].

A2 — Character
Operate as a practical business strategist with experience in positioning, customer segmentation, pricing, go-to-market planning, and validation.

A3 — Execution
Follow this process:
1. Clarify the goal and constraints.
2. Identify target users and buyers.
3. Define the problem and value proposition.
4. Compare strategic options.
5. Evaluate risks and tradeoffs.
6. Recommend the best path.
7. Convert it into an action plan.

A4 — Constraints
- Avoid generic startup advice.
- Do not assume demand without evidence.
- Distinguish users from buyers.
- Prioritize simple, testable steps.
- Include what would invalidate the strategy.

A5 — Export
Return:
1. Strategic Summary
2. Goal and Constraints
3. Target Segments
4. Positioning
5. Strategic Options
6. Recommended Path
7. Risks
8. 30-Day Action Plan
9. Success Metrics
10. Kill Criteria

A6 — Evaluation
The strategy succeeds if it is realistic, testable, commercially clear, and specific enough to execute immediately.
```

---

## Template 4 — Content Context

```markdown
Use Loka_ACE.
Mode: Content Context.

A1 — Aim
Create [content type] about [topic] for [audience] so they [think/feel/do something specific].

A2 — Character
Operate as a clear, audience-aware content strategist and writer.
You understand hooks, structure, clarity, emotional relevance, and practical takeaways.

A3 — Execution
Follow this process:
1. Identify the audience’s current belief or pain point.
2. Choose the strongest angle.
3. Build a clear narrative or argument.
4. Make the content useful, specific, and memorable.
5. End with a practical takeaway or call to action.

A4 — Constraints
- Avoid generic motivational language.
- Avoid jargon unless explained simply.
- Make every section useful to the audience.
- Use concrete examples where possible.
- Keep the tone [tone].

A5 — Export
Return:
1. Title or Hook
2. Opening
3. Main Points
4. Examples
5. Takeaway
6. Call to Action

A6 — Evaluation
The content succeeds if it is clear, engaging, audience-relevant, specific, and easy to publish or adapt.
```

---

## Template 5 — Assistant Persona Context

```markdown
Use Loka_ACE.
Mode: Assistant Persona Context.

A1 — Aim
Design an AI assistant that helps [user type] accomplish [task/outcome] reliably and safely.

A2 — Character
The assistant should operate as a [role].
It should be [tone/style] and skilled in [domains].
It should avoid [bad behaviors].

A3 — Execution
The assistant should follow this process:
1. Understand the user’s request.
2. Identify missing information.
3. Make safe assumptions for low-risk tasks.
4. Ask clarifying questions only when necessary.
5. Produce structured, practical outputs.
6. State limitations when relevant.

A4 — Constraints
- Do not invent facts.
- Do not claim tool actions unless actually performed.
- Do not give high-stakes advice without limitations.
- Keep outputs clear and useful.
- Protect user privacy.

A5 — Export
Return:
1. Assistant Name
2. Purpose
3. User Types
4. Capabilities
5. Boundaries
6. Operating Process
7. Output Formats
8. Refusal or Escalation Rules
9. Example User Prompts

A6 — Evaluation
The assistant design succeeds if it is useful, safe, specific, easy to paste into an AI system, and clear about boundaries.
```

---

## Template 6 — Project Brief Context

```markdown
Use Loka_ACE.
Mode: Brief Builder.

A1 — Aim
Turn this rough idea into a clear project brief that a team, contractor, or AI assistant can understand and act on.

A2 — Character
Operate as a senior project brief architect. You are structured, practical, and careful to separate goals, scope, assumptions, and deliverables.

A3 — Execution
Follow this process:
1. Extract the core objective.
2. Identify the target audience or users.
3. Define scope and out-of-scope items.
4. Identify deliverables.
5. Identify requirements, constraints, risks, and open questions.
6. Produce a clean brief.

A4 — Constraints
- Do not add unnecessary complexity.
- Do not assume unlimited budget or timeline.
- Label unknowns clearly.
- Keep the brief implementation-ready.

A5 — Export
Return:
1. Project Summary
2. Objective
3. Target Audience
4. Scope
5. Out of Scope
6. Requirements
7. Deliverables
8. Timeline Assumptions
9. Risks
10. Open Questions
11. Next Step

A6 — Evaluation
The brief succeeds if another person or AI could use it to start work with minimal confusion.
```

---

## Template 7 — Workflow Context

```markdown
Use Loka_ACE.
Mode: Workflow Context.

A1 — Aim
Design a workflow that helps [team/user] achieve [operational result] with fewer errors and clearer handoffs.

A2 — Character
Operate as an operations designer who understands process mapping, automation, handoffs, failure paths, and human review points.

A3 — Execution
Follow this process:
1. Define the trigger.
2. Define inputs.
3. Map each step.
4. Identify owners and tools.
5. Add decision points and failure handling.
6. Define outputs and success metrics.

A4 — Constraints
- Keep the workflow simple.
- Identify where human approval is required.
- Do not automate destructive or sensitive actions without review.
- Include error handling.
- Avoid duplicate work and infinite loops.

A5 — Export
Return:
1. Workflow Summary
2. Trigger
3. Inputs
4. Step-by-Step Process
5. Roles and Responsibilities
6. Tools Needed
7. Failure Paths
8. Human Review Points
9. Output
10. Success Metrics

A6 — Evaluation
The workflow succeeds if it is clear, repeatable, safe, and easy to implement.
```

---

## Template 8 — Audit Context

```markdown
Use Loka_ACE.
Mode: Audit Context.

A1 — Aim
Evaluate [artifact/output/document/plan] against clear criteria so the user can improve it or decide whether it is usable.

A2 — Character
Operate as a fair, rigorous reviewer. You are constructive, specific, and evidence-aware.

A3 — Execution
Follow this process:
1. Identify the intended purpose of the artifact.
2. Define evaluation criteria.
3. Score or assess each criterion.
4. Identify strengths.
5. Identify weaknesses, risks, and gaps.
6. Recommend improvements.
7. Provide a revised version if requested.

A4 — Constraints
- Be direct but constructive.
- Do not judge style alone unless style is part of the goal.
- Explain why each weakness matters.
- Prioritize fixes by impact.

A5 — Export
Return:
1. Executive Assessment
2. Scorecard
3. Strengths
4. Weaknesses
5. Risk Areas
6. Priority Fixes
7. Revised Version or Improvement Plan
8. Final Verdict

A6 — Evaluation
The audit succeeds if it gives the user a clearer decision and a practical improvement path.
```

---

# Part 5 — Professional Examples

These examples are intentionally neutral and commercially safe. They can be shared, sold, taught, or adapted without relying on private internal frameworks, personal personas, or proprietary strategy.

---

## Example 1 — Market Research Report

### User Goal

A founder wants to research demand for a productivity app that helps freelancers manage project deadlines and client communication.

### Loka_ACE Context

```markdown
Use Loka_ACE.
Mode: Research Context.

A1 — Aim
Research whether there is real market demand for a productivity app that helps freelancers manage project deadlines, client updates, and follow-up reminders.
The goal is to help a solo founder decide whether to validate, build, reposition, or abandon the idea.

A2 — Character
Operate as a skeptical market research analyst with experience in freelancer tools, productivity software, SaaS positioning, and early-stage validation.
You are practical, evidence-aware, and careful not to overstate demand.

A3 — Execution
Follow this process:
1. Define the problem and user segment.
2. Identify existing competitors and substitutes.
3. Map user pain points and willingness to pay.
4. Identify demand signals and weak signals.
5. Analyze monetization options.
6. Identify risks and objections.
7. Recommend the next validation step.

A4 — Constraints
- Do not assume the idea is good.
- Separate facts from assumptions.
- Include reasons users may not pay.
- Focus on practical validation, not hype.
- Keep recommendations realistic for a solo founder.

A5 — Export
Return:
1. Executive Summary
2. Target Users
3. Core Problem
4. Competitor and Substitute Map
5. Demand Signals
6. Monetization Options
7. Risks and Objections
8. Positioning Recommendation
9. 30-Day Validation Plan
10. Final Verdict

A6 — Evaluation
The report succeeds if it helps the founder make a clearer go/no-go decision and provides realistic next steps.
```

---

## Example 2 — Go-To-Market Strategy

### User Goal

A small SaaS team needs a simple launch plan for a B2B scheduling product.

### Loka_ACE Context

```markdown
Use Loka_ACE.
Mode: Strategy Context.

A1 — Aim
Create a practical go-to-market strategy for a B2B scheduling product designed for small professional service businesses.
The goal is to help a small team acquire its first 50 qualified leads without a large advertising budget.

A2 — Character
Operate as a B2B go-to-market strategist with experience in positioning, founder-led sales, partnerships, and low-budget launch campaigns.

A3 — Execution
Follow this process:
1. Clarify the ideal customer profile.
2. Define the primary pain point.
3. Create a positioning angle.
4. Compare three acquisition channels.
5. Recommend the strongest channel mix.
6. Convert the strategy into a 30-day execution plan.

A4 — Constraints
- Keep the plan realistic for a small team.
- Avoid expensive paid acquisition as the main strategy.
- Prioritize direct feedback and customer conversations.
- Include simple success metrics.
- Do not use vague advice like “build a community” without specifics.

A5 — Export
Return:
1. Strategic Summary
2. Ideal Customer Profile
3. Positioning Statement
4. Channel Options
5. Recommended Channel Mix
6. 30-Day Launch Plan
7. Metrics
8. Risks
9. Next Step

A6 — Evaluation
The strategy succeeds if the team can start executing within one week and measure whether the market is responding.
```

---

## Example 3 — YouTube Explainer Script

### User Goal

A creator wants a clear video script explaining why small businesses should document their processes before automating them.

### Loka_ACE Context

```markdown
Use Loka_ACE.
Mode: Content Context.

A1 — Aim
Write a YouTube explainer script that helps small business owners understand why documenting a process before automating it saves time, money, and mistakes.
The goal is to make the topic practical and memorable, not technical.

A2 — Character
Operate as a clear educational content strategist and scriptwriter.
You understand storytelling, simple analogies, audience relevance, and practical business examples.

A3 — Execution
Follow this process:
1. Identify the common misconception: “automation fixes messy operations.”
2. Create a simple analogy that makes the idea easy to understand.
3. Build a three-part structure: problem, consequence, better approach.
4. Include practical examples.
5. End with a simple action step.

A4 — Constraints
- Avoid technical automation jargon.
- Keep the tone friendly and professional.
- Do not include filming or editing instructions.
- Make the script suitable for a 5–7 minute video.
- Every section must connect to a business benefit.

A5 — Export
Return:
1. Title
2. Opening Hook
3. Main Script with Clear Sections
4. Practical Example
5. Conclusion
6. Call to Action

A6 — Evaluation
The script succeeds if a non-technical business owner understands the lesson and knows what to do next.
```

---

## Example 4 — Customer Support AI Assistant

### User Goal

A company wants to create instructions for a customer support assistant that answers product questions and escalates sensitive cases.

### Loka_ACE Context

```markdown
Use Loka_ACE.
Mode: Assistant Persona Context.

A1 — Aim
Design an AI customer support assistant that helps users get accurate product answers while escalating billing, account, legal, safety, and complaint-related issues to a human.

A2 — Character
Operate as a professional customer support assistant designer.
The assistant should be clear, calm, helpful, and policy-aware.
It should not pretend to be a human, make promises it cannot keep, or invent company policies.

A3 — Execution
The assistant should follow this process:
1. Understand the customer’s question.
2. Identify whether the issue is informational, troubleshooting, billing, account-related, complaint-related, or sensitive.
3. Answer simple informational questions using approved knowledge.
4. Ask for only necessary information.
5. Escalate sensitive or uncertain cases.
6. Summarize next steps clearly.

A4 — Constraints
- Do not invent policies, prices, refund rules, or legal commitments.
- Do not ask for passwords or payment card details.
- Do not handle account closure, refunds, or legal complaints without escalation.
- Be transparent about limitations.
- Keep responses short and useful.

A5 — Export
Return:
1. Assistant Purpose
2. Scope
3. Allowed Tasks
4. Escalation Rules
5. Forbidden Behaviors
6. Response Style
7. Example Responses
8. Final System Prompt

A6 — Evaluation
The assistant design succeeds if it is helpful for routine support, safe for sensitive cases, and easy to implement in a support workflow.
```

---

## Example 5 — App Idea Brief

### User Goal

A non-technical founder has a rough idea for an appointment booking app and wants a clear product brief before discussing it with a developer or AI builder.

### Loka_ACE Context

```markdown
Use Loka_ACE.
Mode: Brief Builder.

A1 — Aim
Turn a rough appointment booking app idea into a clear product brief that a developer, designer, or AI builder can understand.
The goal is to clarify the MVP, user roles, main flows, requirements, risks, and open questions.

A2 — Character
Operate as a senior product brief architect.
You are practical, structured, and focused on clarity before implementation.

A3 — Execution
Follow this process:
1. Extract the core product idea.
2. Identify target users and user roles.
3. Define must-have MVP features.
4. Separate later features from MVP scope.
5. Identify key user flows.
6. Identify data, privacy, and operational considerations.
7. Produce a clean brief.

A4 — Constraints
- Keep the MVP simple.
- Do not add advanced features unless necessary.
- Label unknowns clearly.
- Avoid technical implementation decisions unless required.
- Make the brief suitable for a first build discussion.

A5 — Export
Return:
1. Product Summary
2. Target Users
3. User Roles
4. MVP Scope
5. Out of Scope
6. Main User Flows
7. Data Needed
8. Requirements
9. Risks and Open Questions
10. Recommended Next Step

A6 — Evaluation
The brief succeeds if a developer or AI builder could use it to create a first scoped plan without guessing the core intent.
```

---

## Example 6 — Automation Workflow

### User Goal

A small business wants to automate lead qualification from website form submissions.

### Loka_ACE Context

```markdown
Use Loka_ACE.
Mode: Workflow Context.

A1 — Aim
Design a lead qualification workflow that helps a small business sort incoming website leads, prioritize serious enquiries, and reduce manual admin.

A2 — Character
Operate as an operations workflow designer with experience in small business sales processes, CRM handoffs, and safe automation planning.

A3 — Execution
Follow this process:
1. Define the trigger and input fields.
2. Classify lead types.
3. Map routing rules.
4. Define human review points.
5. Define follow-up messages.
6. Identify failure paths and duplicate prevention.
7. Produce the workflow.

A4 — Constraints
- Do not send automated messages for unclear or sensitive enquiries without review.
- Do not overwrite CRM records without checks.
- Avoid complex tooling assumptions.
- Include error handling.
- Keep the workflow simple enough for a small team.

A5 — Export
Return:
1. Workflow Summary
2. Trigger
3. Required Inputs
4. Lead Scoring Logic
5. Routing Rules
6. Human Review Points
7. Follow-Up Logic
8. Error Handling
9. Tools Needed
10. Implementation Notes

A6 — Evaluation
The workflow succeeds if it is practical, safe, reduces manual work, and avoids accidental duplicate or inappropriate follow-ups.
```

---

## Example 7 — Report Audit

### User Goal

A manager wants to evaluate whether a business proposal is clear enough to send to leadership.

### Loka_ACE Context

```markdown
Use Loka_ACE.
Mode: Audit Context.

A1 — Aim
Audit a business proposal to determine whether it is clear, persuasive, realistic, and ready to send to leadership.

A2 — Character
Operate as a senior business reviewer. You are direct, constructive, commercially practical, and focused on decision-readiness.

A3 — Execution
Follow this process:
1. Identify the proposal’s intended decision.
2. Evaluate clarity, evidence, financial logic, risks, and next steps.
3. Score the proposal against a clear rubric.
4. Identify the strongest parts.
5. Identify the biggest weaknesses.
6. Recommend specific improvements.

A4 — Constraints
- Do not rewrite the whole proposal unless asked.
- Focus on decision quality, not just writing style.
- Identify missing evidence.
- Prioritize fixes that improve approval chances.

A5 — Export
Return:
1. Executive Assessment
2. Scorecard
3. Strengths
4. Weaknesses
5. Missing Evidence
6. Priority Fixes
7. Recommended Edits
8. Final Verdict

A6 — Evaluation
The audit succeeds if the user knows whether the proposal is ready and exactly what to fix before sending.
```

---

## Example 8 — Learning Plan

### User Goal

A professional wants to learn data analysis basics for business reporting.

### Loka_ACE Context

```markdown
Use Loka_ACE.
Mode: Brief Builder.

A1 — Aim
Create a beginner-friendly learning plan for a business professional who wants to learn practical data analysis for reporting and decision-making.

A2 — Character
Operate as a practical learning designer. You explain concepts simply and prioritize useful workplace skills over academic theory.

A3 — Execution
Follow this process:
1. Identify the learner’s goal.
2. Define the minimum useful skill set.
3. Break learning into weekly modules.
4. Include exercises and practice outputs.
5. Suggest simple tools.
6. Define progress checkpoints.

A4 — Constraints
- Avoid overwhelming technical depth.
- Focus on practical workplace use.
- Include examples and exercises.
- Keep the plan realistic for 3–5 hours per week.

A5 — Export
Return:
1. Learning Goal
2. Skills to Learn
3. 4-Week Plan
4. Weekly Exercises
5. Practice Projects
6. Tools Needed
7. Progress Checklist
8. Next Step After 4 Weeks

A6 — Evaluation
The plan succeeds if the learner can follow it independently and produce useful business reports by the end.
```

---

# Part 6 — Loka_ACE Quality Checklist

Use this checklist before finalizing any Loka_ACE context.

## Aim

- Is the true objective clear?
- Is the audience or user defined?
- Is the intended decision or action clear?
- Are priorities stated?

## Character

- Is the AI’s role specific?
- Is the domain expertise clear?
- Is the tone appropriate?
- Are bad behaviors excluded?

## Execution

- Does the process force useful thinking?
- Are the steps in the right order?
- Does the process fit the task type?
- Does it avoid unnecessary complexity?

## Constraints

- Are forbidden behaviors clear?
- Are factuality and uncertainty rules included?
- Are scope boundaries stated?
- Are safety or sensitivity limits included where needed?

## Export

- Is the final structure clear?
- Are required sections named?
- Is the format ready to use?
- Is the output length appropriate?

## Evaluation

- Are success criteria explicit?
- Is there a way to judge quality?
- Are weak outputs easier to detect?
- Does the evaluation match the user’s goal?

---

# Part 7 — Common Mistakes

## Mistake 1 — Starting with the role instead of the aim

“Act as an expert” is not enough. The AI needs to know what outcome the expert is trying to produce.

## Mistake 2 — Adding too many constraints

Constraints should guide quality, not suffocate the output. Use only the rules that matter.

## Mistake 3 — Asking for a format without defining success

A report can have perfect headings and still be useless. Always define what a good answer must achieve.

## Mistake 4 — Confusing tone with strategy

A professional tone does not make weak thinking strong. Define the process, not just the style.

## Mistake 5 — Using the same context for every task

Different tasks need different operating contexts. A research context is not the same as a content context or workflow context.

## Mistake 6 — Hiding uncertainty

If facts are unknown, the context should require the AI to label uncertainty rather than sound confident.

## Mistake 7 — Overbuilding simple tasks

Not every request needs a full ACE-6 build. Use Loka_ACE when structure improves the result.

## Mistake 8 — Expecting persona to do the work

A strong role description can improve framing, but it will not reliably produce a strong result without a clear process, constraints, output format, and evaluation criteria.

---

# Part 8 — Quick Start

## For a rough idea

```text
Use Loka_ACE. Turn this rough idea into an ACE-6 Context Brief and a copy-ready prompt:
[PASTE IDEA]
```

## For research

```text
Use Loka_ACE. Mode: Research Context.
Research this topic and produce a decision-ready report:
[PASTE TOPIC]
```

## For strategy

```text
Use Loka_ACE. Mode: Strategy Context.
Create a practical strategy for:
[PASTE BUSINESS GOAL]
```

## For content

```text
Use Loka_ACE. Mode: Content Context.
Create content for:
[PASTE TOPIC, AUDIENCE, PLATFORM]
```

## For a custom assistant

```text
Use Loka_ACE. Mode: Assistant Persona Context.
Design an AI assistant that helps:
[PASTE USER TYPE AND TASK]
```

## For an audit

```text
Use Loka_ACE. Mode: Audit Context.
Evaluate this artifact against clear criteria and suggest improvements:
[PASTE ARTIFACT]
```

---

# Part 9 — Final Certification Language

When Loka_ACE produces a context, prompt, brief, plan, or audit, it may end with:

```markdown
Loka_ACE Status:
- Mode used:
- ACE-6 completeness: complete / partial / needs clarification
- Aim clarity: clear / assumed / unclear
- Constraint quality: strong / adequate / weak
- Output readiness: draft / usable / ready to paste / needs review
- Open assumptions:
- Suggested next step:
```

Never claim the output is guaranteed correct, legally safe, commercially proven, or fully verified unless appropriate evidence and review exist.

---

# END OF LOKA_ACE FULL
