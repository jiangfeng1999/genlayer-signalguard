# SignalGuard Gas Fee Simulator Tests

## Suggested title

SignalGuard Gas Fee Simulator Tests for Read and Write Flows

## Portal category

Gas Fees Simulator Tests

## Primary evidence

https://jiangfeng1999.github.io/genlayer-signalguard/web/gas-fees-simulator-tests.html

## Supporting evidence

- https://github.com/jiangfeng1999/genlayer-signalguard/blob/main/app/gas_fee_simulator_tests.py
- https://github.com/jiangfeng1999/genlayer-signalguard/blob/main/examples/gas_fee_cases.json
- https://github.com/jiangfeng1999/genlayer-signalguard/blob/main/contracts/signal_guard.py
- https://github.com/jiangfeng1999/genlayer-signalguard/blob/main/app/signalguard_cli.py
- https://docs.genlayer.com/developers/intelligent-contracts/tools/genlayer-studio/limitations

## Description

SignalGuard Gas Fee Simulator Tests is a deterministic test matrix for fee-aware SignalGuard usage. It separates read-only getter calls, write calls, malformed inputs, and repeated writes. Each case records expected fee behavior, Studio-specific limitations, live-network considerations, and the user-facing risk.

## Why it fits Gas Fees Simulator Tests

- It focuses specifically on fee-aware testing rather than generic contract documentation.
- It makes the Studio limitation explicit: Studio prototype transactions do not consume gas.
- It helps builders avoid turning reads into fee-bearing writes.
- It documents where live clients should estimate or bound costs before a wallet prompt.

## Verification

Run from the repository root:

```powershell
python app\gas_fee_simulator_tests.py
python app\gas_fee_simulator_tests.py --keys
python -m py_compile app\gas_fee_simulator_tests.py
powershell -ExecutionPolicy Bypass -File scripts\verify-evidence-package.ps1
```

## Review boundaries

- The package does not claim to calculate real mainnet or testnet gas.
- It is a simulator-test fixture for reviewer and builder reasoning.
- Portal submission still requires the user to complete wallet, reCAPTCHA, and final confirmation.
