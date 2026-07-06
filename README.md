# GenLayer SignalGuard

SignalGuard is a compact GenLayer project for checking whether a public claim is supported by a cited source. It uses an Intelligent Contract as the decision layer: the contract fetches source content, asks validators to reason over the claim, and stores the accepted verdict report.

## Why this uses GenLayer

Normal smart contracts cannot inspect natural-language evidence or compare source text with a claim. SignalGuard is designed for GenLayer's AI-native contract model:

- An Intelligent Contract evaluates a natural-language claim.
- The contract reads the cited source with `gl.nondet.web.get`.
- Validators independently interpret the same evidence.
- The accepted result is stored as a reusable on-chain attestation.
- A simple app can submit claims and read the latest verdict.

## What it can be used for

- Community fact checks for ecosystem announcements.
- Lightweight risk labels for project claims.
- Research notes where every conclusion links back to public evidence.
- AI-agent workflows that need a human-readable, consensus-backed answer.

## Repository layout

```text
contracts/signal_guard.py      GenLayer Intelligent Contract
app/signalguard_cli.py         Minimal CLI payload builder for contract calls
web/index.html                 Static demo UI for preparing calls
web/portal-dashboard.html      Static Portal points and leaderboard dashboard
docs/submission.md             Portal submission notes and review checklist
docs/research-analysis.md      Research notes on the source-grounded verdict pattern
docs/tooling-notes.md          Tooling and local verification notes
docs/network-dashboard-submission.md  Dashboard contribution notes
examples/sample_claims.json    Example claims and sources
```

## Contract workflow

1. Deploy `contracts/signal_guard.py` in GenLayer Studio.
2. Initialize with an optional first claim and source URL.
3. Call `review_claim(claim, source_url)`.
4. The contract fetches the URL and uses `prompt_non_comparative` to validate a compact JSON verdict report.
5. Accepted verdicts can be read with `latest_verdict()`.

The MVP intentionally keeps state small so reviewers can deploy and test it quickly in Studio.

## Demo UI

Open `web/index.html` locally and generate a `review_claim` payload for Studio. The UI is deliberately static so the contribution can be reviewed without installing a frontend toolchain.

Serve the repository over HTTP and open `web/portal-dashboard.html` to inspect public Portal points, the builder leaderboard gap, and high-value contribution categories from the public Portal API:

```bash
python -m http.server 8765
```

Then open `http://127.0.0.1:8765/web/portal-dashboard.html`.

## Example claim

```text
Claim: GenLayer uses Intelligent Contracts that can access the internet and reason over natural language.
Source: https://docs.genlayer.com/
Expected verdict: supported
```

## Portal contribution category

This is intended for the **Projects** category because GenLayer is central to the workflow and the project contains both contract logic and app-side call preparation.

## Reference docs

- GenLayer Equivalence Principle: https://docs.genlayer.com/developers/intelligent-contracts/equivalence-principle
- Calling LLMs from Intelligent Contracts: https://docs.genlayer.com/developers/intelligent-contracts/features/calling-llms
- Web access and Intelligent Contracts overview: https://docs.genlayer.com/understand-genlayer-protocol/what-is-genlayer
