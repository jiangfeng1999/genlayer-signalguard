# Tools & Infrastructure Submission Notes

## Suggested title

SignalGuard Builder Evidence and Status Toolchain

## Suggested category

`Tools & Infrastructure`

## Published evidence

```text
https://jiangfeng1999.github.io/genlayer-signalguard/web/tools-infrastructure.html
```

## Supporting public evidence

```text
https://github.com/jiangfeng1999/genlayer-signalguard/blob/main/scripts/check-genlayer-status.ps1
https://github.com/jiangfeng1999/genlayer-signalguard/blob/main/scripts/save-genlayer-status.ps1
https://github.com/jiangfeng1999/genlayer-signalguard/blob/main/scripts/verify-evidence-package.ps1
https://github.com/jiangfeng1999/genlayer-signalguard/blob/main/scripts/test-portal-dashboard-calculations.ps1
https://github.com/jiangfeng1999/genlayer-signalguard/blob/main/app/signalguard_cli.py
https://github.com/jiangfeng1999/genlayer-signalguard/blob/main/docs/tooling-notes.md
```

## Short description

SignalGuard Builder Evidence and Status Toolchain is a public, reproducible toolkit for GenLayer builders. It combines a read-only Portal status checker, timestamped local snapshot helper, deterministic dashboard calculation test, CLI payload generator for Studio calls, and one-command evidence package verifier. The tooling helps reviewers and builders inspect project evidence without wallet access, private Portal data, or a frontend build step.

## What reviewers can reproduce

- Read the public Portal user, leaderboard, contribution type, and GitHub evidence status.
- Save timestamped local point snapshots and compare deltas.
- Verify dashboard calculations with an offline fixture.
- Generate a `review_claim` Studio payload from a claim and source URL.
- Run the full package verifier for required files, Python compilation, JSON examples, and static page markers.

## Guardrails

- Submit once under the clearest fitting category.
- The public contribution type list currently marks the Builder `tools-infrastructure` category as not directly submittable; use this page as support evidence unless Portal exposes the category to the logged-in account.
- Do not claim this toolchain guarantees Portal acceptance or points.
- Do not use private Portal session data, wallet signatures, or hidden APIs as evidence.
- User must handle any wallet session, reCAPTCHA, and final Portal confirmation.
