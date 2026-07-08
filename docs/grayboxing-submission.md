# SignalGuard Graybox Harness

## Suggested title

SignalGuard Graybox Harness for Source-Grounded Intelligent Contracts

## Portal category

Grayboxing

## Primary evidence

https://jiangfeng1999.github.io/genlayer-signalguard/web/grayboxing.html

## Supporting evidence

- https://github.com/jiangfeng1999/genlayer-signalguard/blob/main/app/graybox_harness.py
- https://github.com/jiangfeng1999/genlayer-signalguard/blob/main/examples/graybox_cases.json
- https://github.com/jiangfeng1999/genlayer-signalguard/blob/main/contracts/signal_guard.py
- https://github.com/jiangfeng1999/genlayer-signalguard/blob/main/docs/adversarial-testing.md

## Description

SignalGuard Graybox Harness documents and implements practical grayboxing controls for source-grounded GenLayer claim review. It packages prompt-control cases for prompt injection in retrieved source content, oversized source excerpts, conflicting source evidence, and ambiguous reward claims. Each case is converted into a prompt package that separates trusted instructions from untrusted source text, bounds the source excerpt, restricts verdict outputs, and records the security risk being tested.

## Why it fits Grayboxing

- It maps GenLayer grayboxing ideas into practical SignalGuard test cases.
- It implements input filtration by normalizing and bounding untrusted source text.
- It implements output restriction by pinning verdicts to supported, contradicted, or inconclusive.
- It documents model-isolation and monitoring assumptions for reviewers.
- It pairs the analysis with executable fixtures rather than only prose.

## Verification

Run from the repository root:

```powershell
python app\graybox_harness.py
python app\graybox_harness.py --compact
python -m py_compile app\graybox_harness.py
powershell -ExecutionPolicy Bypass -File scripts\verify-evidence-package.ps1
```

## Review boundaries

- This is a graybox prompt-control harness, not a claim that any single prompt defeats all prompt injection.
- The harness is designed for review and extension by GenLayer builders.
- Portal submission still requires the user to complete wallet, reCAPTCHA, and final confirmation.
