# Network Dashboard Submission Notes

## Suggested title

GenLayer Portal Public Points Dashboard

## Suggested category

`Network Dashboard`

## Short description

This static dashboard reads the public GenLayer Portal API and turns it into a reviewer-friendly view of a wallet's Builder points, the current gap to the #1 Builder, the Builder leaderboard, and the highest-value public contribution categories.

## Evidence

Use a public URL for:

```text
web/portal-dashboard.html
```

Supporting public files:

```text
scripts/check-genlayer-status.ps1
scripts/save-genlayer-status.ps1
scripts/test-portal-dashboard-calculations.ps1
docs/benchmarks.md
examples/portal_dashboard_checks.json
examples/dashboard_calculation_fixture.json
```

The file must be available from GitHub or another public URL before submitting it to the Portal.

## Why it qualifies

- It uses public GenLayer Portal data instead of private account state.
- It helps builders track rank, points, and the practical gap to the top leaderboard position.
- It surfaces high-value contribution categories and their current point caps.
- It is static, inspectable, and does not require a wallet connection, account login, or API key.

## Local verification

Serve the repository over HTTP:

```powershell
python -m http.server 8765
```

Open:

```text
http://127.0.0.1:8765/web/portal-dashboard.html
```

Expected behavior:

- The wallet input is prefilled with `0x554406e72a76a7b90f1d2857187669af42f65b59`.
- The dashboard fetches public Portal user, leaderboard, and contribution type data.
- It displays Builder points, rank if present, gap to #1, and contribution count.
- It displays the Builder leaderboard top 10.
- It displays the highest-value submittable contribution categories.

## Portal submission notes

```text
GenLayer Portal Public Points Dashboard is a static, public-data dashboard for builders. It reads the public Portal API to show a wallet's Builder points, the live gap to the #1 Builder, the top Builder leaderboard, and high-value contribution categories. It requires no wallet connection, no login, and no API key, so reviewers can inspect it directly from the published HTML file.
```

## Guardrails

- Do not claim that the dashboard grants points automatically.
- Do not claim private submission status unless the Portal exposes it publicly.
- Do not submit this until it is published at a public URL.
- Do not resubmit it under multiple categories with the same evidence.
