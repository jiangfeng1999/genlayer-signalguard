# Research Analysis: Source-Grounded Claims on GenLayer

Published report:

```text
https://jiangfeng1999.github.io/genlayer-signalguard/web/research-analysis.html
```

SignalGuard explores a narrow but useful GenLayer pattern: turning a public claim and a cited source into a stored verdict that validators can independently reason about.

## Problem

Crypto communities often circulate claims that are not purely numeric. Examples include whether a protocol supports a feature, whether a roadmap statement exists, or whether a source actually backs a summary. Traditional smart contracts cannot interpret these claims because the decision depends on natural-language context.

## GenLayer fit

GenLayer is a good match because the workflow needs three properties:

- Internet access to retrieve source material.
- AI-assisted reasoning over natural-language evidence.
- A consensus mechanism for accepting one result instead of a single model response.

SignalGuard uses `gl.nondet.web.get` to fetch the cited page and `prompt_non_comparative` to ask validators for a compact verdict. The contract stores the accepted output so the result can be reused by an app or researcher.

## Review model

The contract asks for one of three verdicts:

- `supported`: the cited source directly backs the claim.
- `contradicted`: the cited source directly conflicts with the claim.
- `inconclusive`: the source is too vague, missing, or unrelated.

The rationale is intentionally limited to evidence present in the fetched source. This keeps the result auditable and reduces the chance of an unsupported answer.

## Limitations

- The current MVP stores only the latest verdict.
- Large pages are truncated to keep the prompt compact.
- It does not yet compare multiple independent sources.
- It does not yet include a frontend deployment or explorer integration.

## Current public observations

The public Portal API snapshot on 2026-07-07 showed:

- Builder points for `jiangfeng`: 50 BP.
- Public Builder contribution count: 1.
- Current public #1 Builder: `YoneCode` at 9395 BP.
- Highest observed display caps: `Projects` and `Milestones` at 4000 BP each.
- `Research & Analysis` displayed an observed public cap of 2000 BP.
- `Network Dashboard` displayed an observed public cap of 1500 BP.

These observations do not prove future scoring. They only describe the public contribution-type data available at the time of the report.

## Research contribution fit

This material is distinct from the Project submission because it analyzes:

- why source-grounded claim review fits GenLayer,
- what evidence is needed for reviewer confidence,
- how supported, contradicted, and inconclusive cases should behave,
- what the public Portal contribution-type data implies for prioritization.

## Next milestone candidates

- Store a list of verdicts keyed by claim hash.
- Add source freshness metadata.
- Add a small web app that calls the deployed contract.
- Add tests with supported, contradicted, and inconclusive examples.

