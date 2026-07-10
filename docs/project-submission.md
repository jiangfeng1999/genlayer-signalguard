# SignalGuard Project Submission

## Title

SignalGuard: Source-Grounded Claim Review on GenLayer

## Category

Projects

## Primary evidence

https://jiangfeng1999.github.io/genlayer-signalguard/web/project-overview.html

## Supporting evidence

- Live DApp: https://jiangfeng1999.github.io/genlayer-signalguard/web/dapp.html
- Intelligent Contract evidence: https://jiangfeng1999.github.io/genlayer-signalguard/web/intelligent-contract.html
- Repository: https://github.com/jiangfeng1999/genlayer-signalguard
- Studio deployment: https://studio.genlayer.com/contracts?import-contract=0x1d496901d68FC02d105A14B81Ea0e67476A9891A
- Contract source: https://github.com/jiangfeng1999/genlayer-signalguard/blob/main/contracts/signal_guard.py
- Reviewer quickstart: https://jiangfeng1999.github.io/genlayer-signalguard/web/reviewer-quickstart.html
- Automated verification: https://github.com/jiangfeng1999/genlayer-signalguard/actions/workflows/quality.yml

## Description

SignalGuard is a deployed GenLayer DApp that turns a public claim and an HTTPS source into a consensus-backed verdict. The Intelligent Contract fetches the source inside GenVM, asks validators to determine whether the claim is supported, contradicted, or inconclusive, and stores the accepted report. The browser application uses GenLayerJS and an injected wallet provider to read accepted state, submit `review_claim`, wait for an accepted receipt, and display the result.

## Why it fits Projects

- GenLayer owns the consensus-critical decision and state transition.
- The public DApp performs real GenLayerJS reads and wallet-signed writes.
- A deployed StudioNet contract is available for immediate inspection.
- The repository verifies that deployed source and local source are identical.
- Linux CI runs the pinned GenLayer Direct Mode storage test.
- The project has a focused use case rather than a generic LLM wrapper.

## Fast review

1. Open the Project overview.
2. Open the DApp, inspect the verified deployment snapshot, and connect a wallet to refresh live StudioNet state.
3. Inspect the deployed contract schema or Studio import.
4. Check the `Verify SignalGuard` GitHub Actions workflow.
5. Run `python scripts/verify_studionet_deployment.py` from a clone.

## Boundaries

This is one base Project submission. Supporting research and tools are evidence for SignalGuard, not duplicate Project submissions. A Milestone should be submitted only after the base Project is accepted and a separately deployed contract upgrade exists.
