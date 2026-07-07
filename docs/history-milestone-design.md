# SignalGuard History Milestone Design

## Purpose

The deployed `SignalGuard` contract stores the latest verdict only. That is intentionally small for the first Project submission, but it limits reviewers who want to inspect several claims in one deployment.

`contracts/signal_guard_history.py` is a conservative next-milestone prototype that keeps the original review flow and adds a simple append-only review log.

## Why this is separate

The original deployed contract evidence should stay stable:

```text
contracts/signal_guard.py
```

The history prototype is separate so the public repository can show a credible next step without changing the already-deployed contract address or the existing Portal Project evidence.

## Added behavior

`SignalGuardHistory` adds:

- `review_count`: total number of reviewed claims.
- `review_log`: append-only text log with a bounded excerpt view.
- `total_reviews()`: view method for the review count.
- `review_log_excerpt()`: view method returning the latest part of the review log.

The verdict logic remains the same:

- Fetch the cited source with `gl.nondet.web.get`.
- Reach agreement on the fetched source with `strict_eq`.
- Ask validators for a `supported`, `contradicted`, or `inconclusive` report.
- Store the latest report for lightweight app reads.

## Review boundaries

- This prototype is not the currently deployed Studio contract.
- It uses only simple string and integer state to reduce compatibility risk.
- It should be deployed and tested separately before any Milestone submission.
- It does not claim to solve large-scale indexing or permanent archival storage.

## Suggested manual test

1. Deploy `contracts/signal_guard_history.py` in GenLayer Studio with no constructor arguments.
2. Call `review_claim` with a supported documentation claim.
3. Call `total_reviews()` and confirm it returns `1`.
4. Call `review_log_excerpt()` and confirm the source URL, claim, and report are present.
5. Call `review_claim` with a second case.
6. Confirm `total_reviews()` returns `2` and the excerpt includes the latest entry.

## Future extension

A later version can replace the text log with keyed storage by claim hash once the repository has a tested pattern for structured historical state in GenLayer Studio.
