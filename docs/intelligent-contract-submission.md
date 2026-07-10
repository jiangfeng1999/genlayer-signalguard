# SignalGuard Intelligent Contract Submission

## Title

SignalGuard Source-Grounded Verdict Contract

## Category

Intelligent Contracts

## Primary evidence

https://jiangfeng1999.github.io/genlayer-signalguard/web/intelligent-contract.html

## Deployment evidence

- Studio import: https://studio.genlayer.com/contracts?import-contract=0x1d496901d68FC02d105A14B81Ea0e67476A9891A
- Source: https://github.com/jiangfeng1999/genlayer-signalguard/blob/main/contracts/signal_guard.py
- Deployment verifier: https://github.com/jiangfeng1999/genlayer-signalguard/blob/main/scripts/verify_studionet_deployment.py
- Testing notes: https://github.com/jiangfeng1999/genlayer-signalguard/blob/main/docs/testing.md

## Description

SignalGuard is a reusable Intelligent Contract primitive for source-grounded claim review. A caller supplies a natural-language claim and an HTTPS source. The contract fetches the source inside GenVM, asks validators to classify the claim as supported, contradicted, or inconclusive under explicit criteria, and stores the accepted report with the claim and source URL.

## GenLayer-specific logic

- `gl.nondet.web.get` fetches cited evidence inside the contract execution.
- `strict_eq` establishes agreement over fetched source content.
- `prompt_non_comparative` lets validators evaluate an open-ended natural-language claim under a shared rubric.
- Accepted state is exposed through `latest_claim` and `latest_verdict`.

## State design

- `claim`: latest accepted claim.
- `source_url`: source used for the latest accepted review.
- `verdict_report`: compact accepted report with verdict, confidence, and rationale.

The deployment intentionally stores only the latest review. Bounded history and typed verdict fields are reserved for a separately deployed upgrade.

## Reproducibility

`python scripts/verify_studionet_deployment.py` downloads the deployed contract source from StudioNet and confirms that it matches the repository source. It also checks the constructor, public methods, and view calls.

## Reviewer path

1. Open the Intelligent Contract evidence page.
2. Import the deployed address in Studio.
3. Inspect `contracts/signal_guard.py`.
4. Run the deployment verifier.
5. Use the DApp with an injected wallet to submit a sample `review_claim` call.
