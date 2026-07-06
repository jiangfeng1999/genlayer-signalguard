# Research Analysis: Source-Grounded Claims on GenLayer

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

## Next milestone candidates

- Store a list of verdicts keyed by claim hash.
- Add source freshness metadata.
- Add a small web app that calls the deployed contract.
- Add tests with supported, contradicted, and inconclusive examples.

