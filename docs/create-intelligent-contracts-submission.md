# SignalGuard Intelligent Contract Catalog

## Suggested title

SignalGuard Intelligent Contract Pattern Catalog

## Portal category

Create Intelligent Contracts

## Primary evidence

https://jiangfeng1999.github.io/genlayer-signalguard/web/create-intelligent-contracts.html

## Supporting evidence

- https://github.com/jiangfeng1999/genlayer-signalguard/blob/main/app/contract_catalog.py
- https://github.com/jiangfeng1999/genlayer-signalguard/blob/main/examples/contract_catalog.json
- https://github.com/jiangfeng1999/genlayer-signalguard/blob/main/contracts/signal_guard.py
- https://github.com/jiangfeng1999/genlayer-signalguard/blob/main/contracts/signal_guard_history.py
- https://studio.genlayer.com/contracts?import-contract=0x1d496901d68FC02d105A14B81Ea0e67476A9891A

## Description

SignalGuard Intelligent Contract Pattern Catalog indexes the created GenLayer Intelligent Contracts in this repository. It explains the deployed SignalGuard source-grounded claim review contract and the separate history prototype, maps each contract to GenLayer features, and gives reviewers a reproducible source path and verification command for each entry.

## Why it fits Create Intelligent Contracts

- It documents created Python Intelligent Contracts rather than only app-side tooling.
- It links directly to contract source files and the deployed Studio import path.
- It separates the deployed contract from the milestone prototype.
- It includes an executable catalog generator and JSON fixture for review.

## Verification

Run from the repository root:

```powershell
python app\contract_catalog.py
python app\contract_catalog.py --paths
python -m py_compile app\contract_catalog.py contracts\signal_guard.py contracts\signal_guard_history.py
powershell -ExecutionPolicy Bypass -File scripts\verify-evidence-package.ps1
```

## Review boundaries

- The base Project submission remains the main product submission.
- The history contract is a prototype for milestone evidence, not the currently deployed Studio address.
- Portal submission still requires the user to complete wallet, reCAPTCHA, and final confirmation.
