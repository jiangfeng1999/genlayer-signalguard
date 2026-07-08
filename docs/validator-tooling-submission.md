# SignalGuard Validator Ops Probe

## Suggested title

SignalGuard Validator Ops Probe for Health, Metrics, Balance, and Snapshot Readiness

## Portal category

Tooling for running a Validator

## Primary evidence

https://jiangfeng1999.github.io/genlayer-signalguard/web/validator-tooling.html

## Supporting evidence

- https://github.com/jiangfeng1999/genlayer-signalguard/blob/main/app/validator_ops_probe.py
- https://github.com/jiangfeng1999/genlayer-signalguard/blob/main/examples/validator_ops_probe_sample.json
- https://github.com/jiangfeng1999/genlayer-signalguard/blob/main/scripts/check-genlayer-status.ps1
- https://github.com/jiangfeng1999/genlayer-signalguard/blob/main/scripts/save-genlayer-status.ps1
- https://docs.genlayer.com/validators/monitoring
- https://docs.genlayer.com/api-references/genlayer-node

## Description

SignalGuard Validator Ops Probe is a lightweight operator checklist and fixture generator for GenLayer validator operations. It covers the public operations endpoints a validator operator should monitor, including health, metrics, and balance, and marks snapshot handling as protected because it requires an operator token. It is intended to help operators and reviewers reason about validator readiness without exposing credentials.

## Why it fits Tooling for running a Validator

- It maps validator monitoring and node API concepts into a compact, reusable probe manifest.
- It separates public probes from protected snapshot operations.
- It includes concrete alert-rule guidance for health, metrics, balance, and snapshot readiness.
- It does not claim that the current Portal wallet is already running a validator.

## Verification

Run from the repository root:

```powershell
python app\validator_ops_probe.py
python app\validator_ops_probe.py --notes
python -m py_compile app\validator_ops_probe.py
powershell -ExecutionPolicy Bypass -File scripts\verify-evidence-package.ps1
```

## Review boundaries

- This is operator tooling and documentation, not proof of live validator uptime.
- Snapshot calls require a valid operator token and should be kept on loopback or behind a tunnel.
- Portal submission still requires the user to complete wallet, reCAPTCHA, and final confirmation.
