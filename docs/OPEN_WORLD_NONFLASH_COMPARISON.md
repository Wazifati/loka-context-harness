# Open-world, non-Flash comparison: ACE Lite

## What this is

This is a transparent illustration of how a direct request and an ACE Lite
condition begin two rich, realistic planning tasks. It is **not** a benchmark,
a model ranking, legal advice, financial advice, or proof that Loka universally
improves an Agent.

Both scenarios are fictional so the responses can be inspected and shared
without representing a real person, company, or market claim.

## Design

- **Scenarios:** a Barcelona-based bilingual creator building an AI-assisted
  content business for EU freelancers; and a London-based B2B fintech preparing
  a private UK/EU pre-seed pitch.
- **Models:** Claude Sonnet 5, GPT-5.6 Terra, and DeepSeek V4 Pro, through
  Abacus RouteLLM.
- **Conditions:** a minimal practical-assistant system instruction (`direct`)
  versus that same instruction plus the preserved [Loka ACE Lite](../meta-prompts/LOKA_ACE_LITE.md)
  and a small adapter that shows the six applied-context layers before answering.
- **Temperature:** `0`.
- **Output cap:** none. The API request deliberately omitted a
  completion-token maximum.
- **One completion per condition:** no retries. All 12 calls completed.
- **No source packs:** models received only the rich scenario prompt and their
  applicable system context. They were not asked to browse.

The exact prompts, system conditions, metadata, and full raw outputs are in
[the evidence folder](evidence/open-world-nonflash-20260917/).

## Returned response size

Response length is descriptive only. It is not a quality score.

| Scenario | Model | Direct words | ACE Lite words |
| --- | --- | ---: | ---: |
| eu creator income plan | Claude Sonnet 5 | 1,284 | 1,286 |
| eu creator income plan | GPT-5.6 Terra | 3,990 | 3,789 |
| eu creator income plan | DeepSeek V4 Pro | 1,254 | 5,028 |
| uk fintech preseed pitch | Claude Sonnet 5 | 2,114 | 1,724 |
| uk fintech preseed pitch | GPT-5.6 Terra | 5,454 | 5,030 |
| uk fintech preseed pitch | DeepSeek V4 Pro | 3,598 | 2,897 |

## What the outputs show

1. **ACE Lite consistently externalised working context.** Every ACE response
   begins by naming an objective, audience, approach, constraints, deliverable,
   and success check. That makes the intended operating frame inspectable before
   the plan starts.
2. **Strong direct responses were already strong.** Claude’s creator and fintech
   responses cover much of the requested structure without ACE. This comparison
   does not support a blanket claim that ACE produces a better answer every time.
3. **More context can mean more output.** GPT and DeepSeek often produced far
   longer ACE responses on the creator task. Readability and decision usefulness
   must be judged separately from length.
4. **The strongest practical benefit appears to be constraint visibility.** In
   the fintech task, several ACE responses explicitly separated available facts,
   assumptions, and validation needs. That is valuable for a founder preparing
   an honest pitch.
5. **ACE is not a fact-checker or compliance layer.** Some outputs in **both**
   conditions still made unsupported regulatory or market-adjacent assertions.
   They must not be reused as legal, financial, market, or compliance guidance
   without human verification.

## How to use this evidence

Use it to decide whether explicit context framing helps a planning task you
actually have. Inspect the raw pairs—not only the headings—and test a specific
Loka route against your own success criteria.

For high-stakes or regulated work, ACE should shape the brief, then
[Loka Guard](../agent-skills/loka-guard/SKILL.md) should help define review and
escalation boundaries. It does not replace qualified review.

## Limitations

- Two scenarios and one completion per condition are too small for performance
  claims.
- The scenarios include useful user context; they do not test live research,
  tool use, coding, or autonomous execution.
- No independent judges or real-world outcomes were used.
- The models may differ in verbosity, internal routing, or product behaviour.
- The report does not rank models or claim causation beyond the visible change
  in provided operating context.
