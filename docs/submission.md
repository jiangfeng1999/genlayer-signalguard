# GenLayer Portal Submission Notes

## Suggested title

GenLayer SignalGuard: AI Consensus Claim Verification

## Short description

SignalGuard is a GenLayer Intelligent Contract project that turns public evidence into a stored consensus-backed verdict. It demonstrates a practical use case for AI-native contracts: checking whether a claim is supported, contradicted, or inconclusive based on source material.

## Why it should qualify as a Project

- GenLayer is the core decision layer, not a decorative add-on.
- The project includes an Intelligent Contract and app-side call preparation.
- The main workflow depends on validator reasoning over natural language evidence.
- It can be extended into an explorer widget, research workflow, or community fact-checking tool.

## Review checklist

- Open `contracts/signal_guard.py` in GenLayer Studio.
- Deploy it with no constructor arguments.
- Use `app/signalguard_cli.py` or `web/index.html` to prepare a `review_claim` payload.
- Call `latest_verdict()` after review to read the stored attestation.

## Example evidence

Use `examples/sample_claims.json` as a quick test dataset.
