# Tutorial: Build a Source-Grounded Claim Review Contract

This tutorial explains the SignalGuard pattern for GenLayer builders: fetch a cited source, ask validators to reason over it, and store a compact verdict that an app can reuse.

## Goal

Build an Intelligent Contract that answers one question:

> Does this source support the submitted claim?

The contract should return one of three verdicts:

- `supported`
- `contradicted`
- `inconclusive`

This is useful because many ecosystem claims are not simple numeric facts. They depend on source text, context, and careful interpretation.

## Contract shape

SignalGuard keeps four state fields:

```python
claim: str
source_url: str
verdict_report: str
review_count: u256
```

The state is intentionally small. Reviewers can deploy the contract quickly, call one write method, and read the latest stored verdict.

## Fetching the cited source

The important GenLayer feature is web access from inside the decision flow:

```python
response = gl.nondet.web.get(source_url)
page_text = response.body.decode("utf-8")
```

The contract passes a bounded excerpt into the validator prompt:

```python
page_text[:6000]
```

This keeps the prompt compact while still giving validators evidence to inspect.

## Asking validators for a verdict

The contract uses `prompt_non_comparative` because the task is not choosing the best item from a list. Validators independently assess the claim against the source:

```python
report = gl.eq_principle.prompt_non_comparative(
    source_input,
    task=(
        "Determine whether the claim is supported, contradicted, or inconclusive "
        "based only on the source content. Return compact JSON with keys "
        "verdict, confidence, and rationale."
    ),
    criteria=(
        "The verdict must be exactly one of supported, contradicted, or inconclusive. "
        "The confidence must be an integer from 0 to 100. "
        "The rationale must cite only evidence present in the source content and must "
        "not invent facts."
    ),
)
```

The criteria matter. A vague prompt can produce broad model commentary; a constrained prompt produces an auditable result.

## App-side payload

The CLI helper builds a payload that can be copied into Studio:

```bash
python app/signalguard_cli.py \
  "GenLayer can use AI validators for subjective decisions" \
  "https://docs.genlayer.com/understand-genlayer-protocol/what-is-genlayer"
```

It outputs:

```json
{
  "method": "review_claim",
  "args": {
    "claim": "GenLayer can use AI validators for subjective decisions",
    "source_url": "https://docs.genlayer.com/understand-genlayer-protocol/what-is-genlayer"
  }
}
```

The static demo in `web/index.html` does the same thing in a browser.

## Review checklist

Before submitting a contract like this, check:

- The source URL is public.
- The claim is specific enough to evaluate.
- The prompt criteria forbid invented facts.
- The output format is compact and predictable.
- The state update stores the accepted validator result.

## Extensions

Useful next steps:

- Store verdicts by claim hash instead of keeping only the latest one.
- Add a timestamp or source freshness field.
- Compare two or three independent sources.
- Add a deployed frontend that reads the latest verdict.
- Add test cases for supported, contradicted, and inconclusive claims.

