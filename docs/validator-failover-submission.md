# SignalGuard Validator Failover Drill

## Suggested title

SignalGuard Validator Failover Drill for Health, Metrics, Balance, and Snapshot Signals

## Portal category

Validator failover

## Primary evidence

https://jiangfeng1999.github.io/genlayer-signalguard/web/validator-failover.html

## Supporting evidence

- https://github.com/jiangfeng1999/genlayer-signalguard/blob/main/app/validator_failover_drill.py
- https://github.com/jiangfeng1999/genlayer-signalguard/blob/main/examples/validator_failover_drill.json
- https://github.com/jiangfeng1999/genlayer-signalguard/blob/main/app/validator_ops_probe.py
- https://github.com/jiangfeng1999/genlayer-signalguard/blob/main/docs/validator-tooling-submission.md
- https://docs.genlayer.com/validators/monitoring
- https://docs.genlayer.com/api-references/genlayer-node

## Description

SignalGuard Validator Failover Drill is a deterministic failover exercise for validator operators. It defines triggers, checks, actions, and rollback paths for health failures, missing metrics, low operator balance, and protected snapshot workflows. It is designed as a reusable drill and review fixture, not as a claim that this wallet is already operating a live validator.

## Why it fits Validator failover

- It focuses on failover triggers and rollback paths rather than generic monitoring.
- It uses GenLayer node operations concepts: health, metrics, balance, and snapshot readiness.
- It marks operator-token snapshot actions as protected.
- It is executable and reproducible through `app/validator_failover_drill.py`.

## Verification

Run from the repository root:

```powershell
python app\validator_failover_drill.py
python app\validator_failover_drill.py --keys
python -m py_compile app\validator_failover_drill.py
powershell -ExecutionPolicy Bypass -File scripts\verify-evidence-package.ps1
```

## Review boundaries

- This is a failover drill and review fixture, not proof of live validator uptime.
- Operators must adapt endpoint addresses and thresholds to their own deployment.
- Portal submission still requires the user to complete wallet, reCAPTCHA, and final confirmation.
