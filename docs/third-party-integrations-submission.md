# SignalGuard SourceBridge Integration Pack

## Suggested title

SignalGuard SourceBridge: External API Adapter Pack for GenLayer Claim Review

## Portal category

3rd party integrations

## Primary evidence

https://jiangfeng1999.github.io/genlayer-signalguard/web/third-party-integrations.html

## Supporting evidence

- https://github.com/jiangfeng1999/genlayer-signalguard/blob/main/app/source_adapter_pack.py
- https://github.com/jiangfeng1999/genlayer-signalguard/blob/main/examples/source_adapter_cases.json
- https://github.com/jiangfeng1999/genlayer-signalguard/blob/main/contracts/signal_guard.py
- https://github.com/jiangfeng1999/genlayer-signalguard/blob/main/app/signalguard_cli.py

## Description

SignalGuard SourceBridge is a small integration toolkit for turning public third-party data sources into reviewable GenLayer contract inputs. It includes adapters for price data, weather data, GitHub release metadata, and documentation pages. Each adapter emits a claim, source URL, and review note that can be converted into a `review_claim` payload for the SignalGuard Intelligent Contract.

## Why it fits 3rd party integrations

- It gives builders reusable patterns for external API and data-source evidence.
- It keeps the contract interface simple: every adapter resolves to a public source URL and a bounded claim.
- It includes a machine-readable fixture file for reviewers.
- It does not require secrets, private APIs, wallet access, or a frontend build.

## Verification

Run from the repository root:

```powershell
python app\source_adapter_pack.py
python app\source_adapter_pack.py --payloads
python -m py_compile app\source_adapter_pack.py
powershell -ExecutionPolicy Bypass -File scripts\verify-evidence-package.ps1
```

## Review boundaries

- The adapters prepare source-grounded review inputs; they do not guarantee API accuracy.
- The price adapter is not financial advice.
- Reviewers can replace the example API parameters with their own public endpoints.
