# Portal Dashboard Benchmark Notes

## Scope

These checks verify that the dashboard and status scripts can read public GenLayer Portal data, compute a Builder leaderboard gap, and rank high-value contribution categories.

They do not test private Portal submission status, wallet balances, signatures, or account-only pages.

## Test inputs

See:

```text
examples/portal_dashboard_checks.json
```

The checks cover:

- public Builder profile lookup by wallet address
- public Builder leaderboard top 10
- public contribution type ranking

## Latest local run

Run from the repository:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\check-genlayer-status.ps1
```

Latest observed result on 2026-07-07:

```text
Builder points: 50
Gap to rank #1: 9346 BP
Rank #1: YoneCode
GitHub contract needs sync: true
```

## Pass criteria

- The status script returns valid JSON.
- `user.builder_points` is present when the wallet is known to the Portal.
- `builder_gap_to_rank_1` is numeric when the leaderboard API is available.
- `top_submittable_contribution_types` includes point caps computed from `max_points * current_multiplier`.
- The dashboard HTML is served over HTTP and contains the dashboard script, wallet input, and leaderboard table.

## Known limitations

- Browser `file://` loading can block API calls, so the dashboard should be served over HTTP.
- Portal rate limiting or temporary queue pressure can return API errors; the script records those errors instead of fabricating a result.
- This benchmark does not prove a Portal contribution is accepted. It only verifies public data access and calculations.
