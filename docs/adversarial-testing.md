# SignalGuard Adversarial Testing Notes

## Purpose

SignalGuard should avoid rewarding unsupported summaries, broad claims, and future-looking speculation. These checks are designed to make reviewers inspect whether the contract prompt keeps verdicts grounded in the cited source.

## Test cases

See:

```text
examples/adversarial_claims.json
```

The set covers:

- direct supported documentation claims
- overclaims that should be contradicted
- unrelated or insufficient sources
- time-sensitive claims that should be inconclusive
- absolute language that should be rejected when point ranges differ
- vague subjective claims without a source-grounded criterion

## How to run manually

1. Deploy `contracts/signal_guard.py` in GenLayer Studio.
2. Pick a case from `examples/adversarial_claims.json`.
3. Call `review_claim(claim, source_url)`.
4. Read `latest_verdict()`.
5. Compare the returned `verdict` field with `expected_verdict`.

## Pass criteria

- Supported claims cite source text that directly backs the claim.
- Contradicted claims identify the conflicting source evidence.
- Inconclusive claims avoid inventing facts or making future predictions.
- The rationale does not cite facts that are absent from the fetched source.

## Current limitations

- These are manual review cases, not an automated GenLayer Studio test runner.
- Web pages may change, so time-sensitive cases should be rechecked before submission.
- A source that blocks automated fetching can make a case inconclusive even when a browser can display it.

## Portal contribution fit

This material can support:

- `Adversarial Testing`
- `Benchmarks`
- a future `Milestones` submission after the base Project is accepted
