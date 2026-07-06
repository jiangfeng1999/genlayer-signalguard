# Tooling Notes

This repository includes a minimal app-side helper for reviewers who want to test the Intelligent Contract quickly in GenLayer Studio.

## CLI helper

`app/signalguard_cli.py` builds a `review_claim` payload from a claim and a source URL:

```bash
python app/signalguard_cli.py "GenLayer can use AI validators for subjective decisions" "https://docs.genlayer.com/understand-genlayer-protocol/what-is-genlayer"
```

The output is JSON:

```json
{
  "method": "review_claim",
  "args": {
    "claim": "...",
    "source_url": "..."
  }
}
```

Reviewers can copy the method and arguments into Studio after deploying `contracts/signal_guard.py`.

## Static demo

`web/index.html` provides the same payload preparation flow without a build system. It is deliberately static so the project remains easy to inspect.

## Portal dashboard

`web/portal-dashboard.html` is a static status dashboard that reads the public Portal API for a wallet address. It shows builder points, rank, gap to the #1 builder, the top builder leaderboard, and high-value contribution categories.

Open it through a local or public HTTP server so browser `fetch` can call the Portal API:

```bash
python -m http.server 8765
```

Then visit `http://127.0.0.1:8765/web/portal-dashboard.html`.

## Read-only status scripts

`scripts/check-genlayer-status.ps1` reads public Portal and GitHub API endpoints and returns a JSON status report. It does not connect a wallet, submit forms, or require credentials.

```powershell
powershell -ExecutionPolicy Bypass -File scripts\check-genlayer-status.ps1
```

`scripts/save-genlayer-status.ps1` saves timestamped JSON snapshots under `.genlayer-status/`, which is ignored by git, and reports the point delta versus the previous snapshot.

```powershell
powershell -ExecutionPolicy Bypass -File scripts\save-genlayer-status.ps1
```

## Verification performed

The Python files compile locally with:

```bash
python -m py_compile app\signalguard_cli.py contracts\signal_guard.py
```

The helper has also been tested with a GenLayer documentation URL and produces a valid payload structure.

The dashboard uses only browser-native `fetch` and does not require a frontend build step.

The status scripts have been run locally against the public Portal API and GitHub API.

## Benchmark notes

`docs/benchmarks.md` records the public API checks used for the dashboard and status scripts. The structured cases live in `examples/portal_dashboard_checks.json`.
