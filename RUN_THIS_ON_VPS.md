# Optional evaluation research: not required to use Loka Context Harness

Loka Context Harness is a context-engineered prompt and workflow kit. It is
usable without this directory, without a VPS, and without any API call.

The legacy evaluation materials in this repository are an exploratory research
scaffold, not a turnkey benchmark. The synthetic dry run verifies report
generation only; it does not show that Loka improves an Agent or model. These
materials must not be used as a launch gate, proof that one LLM is better than
another, or the source of a marketing claim without a separately reviewed
methodology.

## Default: do not run anything

Install the skill or copy the meta prompt from `README.md`. No evaluation,
account, key, subscription credit, or server access is needed.

## If research is deliberately resumed later

1. Obtain explicit approval for the exact account and allowed subscription
   usage. A key existing on a VPS is not approval.
2. Run only after defining a hard call cap, expected model IDs, data retention,
   and a stop condition.
3. Verify billing attribution from the provider's account records. A changed UI
   credit balance alone is not enough to establish billing semantics.
4. Treat findings as exploratory. Preserve prompts, exact configuration, raw
   results, failed calls, and human adjudications before sharing any result.

Do not run the current legacy runner as a public proof. It is not turnkey:
`eval_config.example.json` is a reference record only and is not loaded by the
runner. It needs a separately reviewed methodology and implementation pass
before it could support external quantitative claims.
