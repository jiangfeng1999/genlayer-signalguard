# SignalGuard Project Submission

## Suggested title

GenLayer SignalGuard: AI Consensus Claim Verification

## Portal category

Projects

## Primary evidence

https://jiangfeng1999.github.io/genlayer-signalguard/web/project-overview.html

## Supporting evidence

- https://github.com/jiangfeng1999/genlayer-signalguard
- https://jiangfeng1999.github.io/genlayer-signalguard/web/index.html
- https://studio.genlayer.com/contracts?import-contract=0x1d496901d68FC02d105A14B81Ea0e67476A9891A
- https://explorer-studio.genlayer.com/address/0x1d496901d68FC02d105A14B81Ea0e67476A9891A
- https://jiangfeng1999.github.io/genlayer-signalguard/web/reviewer-quickstart.html

## Description

SignalGuard is a GenLayer Intelligent Contract project that turns public evidence into a stored consensus-backed verdict. A reviewer provides a claim and a source URL; the contract fetches the source, asks validators to decide whether the claim is supported, contradicted, or inconclusive, and stores the accepted report.

## Why it fits Projects

- GenLayer is the core decision layer.
- The repository includes contract logic, a static demo UI, a CLI payload helper, examples, and reproducible checks.
- The workflow depends on GenLayer validator reasoning over natural-language source material.
- The project has a clear extension path into dashboards, research tooling, and claim-history storage.

## Review checklist

1. Open `web/project-overview.html`.
2. Inspect `contracts/signal_guard.py`.
3. Open the Studio import URL for the deployed contract.
4. Use `web/index.html` or `app/signalguard_cli.py` to prepare a `review_claim` payload.
5. Run `scripts/verify-evidence-package.ps1` from a cloned repository.

## Boundary

This is the base project package. Milestone evidence should be submitted separately only after this Project is accepted.
