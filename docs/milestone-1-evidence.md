# SignalGuard Milestone 1 Evidence

## Purpose

This note groups the completed SignalGuard work into a reviewable milestone package. It is intended to support a future `Milestones` submission after the base Project is accepted, and to make the existing Project easier to review.

## Completed work

| Area | Evidence | Reviewer value |
| --- | --- | --- |
| Intelligent Contract | `contracts/signal_guard.py` | Implements source-grounded claim review with GenLayer web access and validator reasoning. |
| History prototype | `contracts/signal_guard_history.py` and `docs/history-milestone-design.md` | Shows a conservative next step for retaining multiple verdicts without changing deployed evidence. |
| Deployment evidence | `docs/submission.md` | Documents the no-argument deployment flow and review checklist. |
| App helper | `app/signalguard_cli.py` and `web/index.html` | Lets reviewers prepare `review_claim` calls without a build step. |
| CLI helper test | `scripts/test-signalguard-cli.ps1` | Verifies that the payload helper emits the expected `review_claim` structure. |
| Public Portal dashboard | `web/portal-dashboard.html` | Shows public Builder points, leaderboard gap, and high-value contribution categories. |
| Read-only status tooling | `scripts/check-genlayer-status.ps1` and `scripts/save-genlayer-status.ps1` | Verifies public Portal and GitHub evidence without account access. |
| Benchmarks | `docs/benchmarks.md` and `examples/portal_dashboard_checks.json` | Records public API checks and expected dashboard behavior. |
| Offline calculation test | `scripts/test-portal-dashboard-calculations.ps1` and `examples/dashboard_calculation_fixture.json` | Verifies gap and contribution-type ranking calculations deterministically. |
| Adversarial cases | `docs/adversarial-testing.md` and `examples/adversarial_claims.json` | Gives reviewers edge cases for supported, contradicted, and inconclusive verdicts. |

## Verification commands

Run from the repository root:

```powershell
python -m py_compile app\signalguard_cli.py contracts\signal_guard.py
python -m py_compile contracts\signal_guard_history.py
powershell -ExecutionPolicy Bypass -File scripts\check-genlayer-status.ps1
powershell -ExecutionPolicy Bypass -File scripts\test-portal-dashboard-calculations.ps1
powershell -ExecutionPolicy Bypass -File scripts\test-signalguard-cli.ps1
```

Serve the static pages:

```bash
python -m http.server 8765
```

Then open:

```text
http://127.0.0.1:8765/web/index.html
http://127.0.0.1:8765/web/portal-dashboard.html
```

## Review boundaries

- This milestone package does not require private account access.
- It does not connect a wallet or submit Portal forms.
- It does not claim passive point accrual from running the files.
- It should not be submitted as a Milestone until the original Project has been accepted.

## Next milestone candidates

- Store multiple verdicts keyed by a claim hash instead of only the latest verdict.
- Add a hosted frontend that reads the deployed contract address.
- Add a public evaluation run with Studio screenshots or explorer links for each adversarial case.
- Add source freshness fields and a small result history view.
