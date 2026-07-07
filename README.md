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
contracts/signal_guard_history.py Next-milestone history prototype
app/signalguard_cli.py         Minimal CLI payload builder for contract calls
index.html                     GitHub Pages evidence hub
web/index.html                 Static demo UI for preparing calls
web/tutorial.html              Public builder tutorial
web/portal-dashboard.html      Static Portal points and leaderboard dashboard
web/research-analysis.html     Published research analysis report
web/adversarial-testing.html   Published adversarial testing report
web/benchmarks.html            Published benchmark report
web/tools-infrastructure.html  Published builder toolchain report
scripts/check-genlayer-status.ps1  Read-only Portal and GitHub status checker
scripts/save-genlayer-status.ps1   Local ignored status snapshot helper
scripts/test-portal-dashboard-calculations.ps1 Offline dashboard calculation test
scripts/test-signalguard-cli.ps1   CLI payload helper test
scripts/verify-evidence-package.ps1 One-command evidence package verifier
docs/submission.md             Portal submission notes and review checklist
docs/educational-content-submission.md Tutorial contribution notes
docs/research-analysis.md      Research notes on the source-grounded verdict pattern
docs/tooling-notes.md          Tooling and local verification notes
docs/network-dashboard-submission.md  Dashboard contribution notes
docs/research-analysis-submission.md  Research contribution notes
docs/adversarial-testing-submission.md Adversarial testing contribution notes
docs/benchmarks-submission.md Benchmark contribution notes
docs/tools-infrastructure-submission.md Tools and infrastructure contribution notes
docs/benchmarks.md             Dashboard and status-script benchmark notes
docs/adversarial-testing.md    Source-grounding adversarial test notes
docs/evaluation-report.md      Project evaluation and risk review
docs/milestone-1-evidence.md   Prepared milestone evidence package
docs/history-milestone-design.md History prototype design notes
examples/sample_claims.json    Example claims and sources
examples/portal_dashboard_checks.json Public Portal dashboard check cases
examples/adversarial_claims.json Source-grounding adversarial claim cases
examples/dashboard_calculation_fixture.json Offline dashboard calculation fixture
examples/milestone_evidence.json Prepared milestone artifact index
```

## Contract workflow

1. Deploy `contracts/signal_guard.py` in GenLayer Studio.
2. Deploy with no constructor arguments.
3. Call `review_claim(claim, source_url)`.
4. The contract fetches the URL and uses `prompt_non_comparative` to validate a compact JSON verdict report.
5. Accepted verdicts can be read with `latest_verdict()`.

The MVP intentionally keeps state small so reviewers can deploy and test it quickly in Studio.

`contracts/signal_guard_history.py` is a separate next-milestone prototype that preserves the same source-grounded verdict flow and adds a simple review count plus append-only log. It is not the currently deployed Studio contract.

## Demo UI

Open `web/index.html` locally and generate a `review_claim` payload for Studio. The UI is deliberately static so the contribution can be reviewed without installing a frontend toolchain.

Open the published dashboard to inspect public Portal points, the builder leaderboard gap, and high-value contribution categories from the public Portal API:

```text
https://jiangfeng1999.github.io/genlayer-signalguard/web/portal-dashboard.html
```

For local inspection, serve the repository over HTTP:

```bash
python -m http.server 8765
```

Then open `http://127.0.0.1:8765/web/portal-dashboard.html`.

## Status scripts

Run a read-only public status check:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\check-genlayer-status.ps1
```

Save timestamped local snapshots under `.genlayer-status/`:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\save-genlayer-status.ps1
```

Run the offline dashboard calculation test:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\test-portal-dashboard-calculations.ps1
```

Run the CLI payload helper test:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\test-signalguard-cli.ps1
```

Run the full evidence package verifier:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\verify-evidence-package.ps1
```

## Example claim

```text
Claim: GenLayer uses Intelligent Contracts that can access the internet and reason over natural language.
Source: https://docs.genlayer.com/
Expected verdict: supported
```

## Portal contribution category

This is intended for the **Projects** category because GenLayer is central to the workflow and the project contains both contract logic and app-side call preparation.

`docs/milestone-1-evidence.md` is prepared as a future milestone package, but it should be submitted only after the base Project is accepted.

## Reference docs

- GenLayer Equivalence Principle: https://docs.genlayer.com/developers/intelligent-contracts/equivalence-principle
- Calling LLMs from Intelligent Contracts: https://docs.genlayer.com/developers/intelligent-contracts/features/calling-llms
- Web access and Intelligent Contracts overview: https://docs.genlayer.com/understand-genlayer-protocol/what-is-genlayer
