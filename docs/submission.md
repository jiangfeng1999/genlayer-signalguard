# GenLayer Portal Submission Notes

## Suggested title

GenLayer SignalGuard: AI Consensus Claim Verification

## Short description

SignalGuard is a deployed GenLayer DApp that turns public evidence into a stored consensus-backed verdict. Its browser application reads accepted StudioNet state and uses GenLayerJS plus an injected wallet to submit `review_claim` transactions.

## Why it should qualify as a Project

- GenLayer is the core decision layer, not a decorative add-on.
- The project includes a deployed Intelligent Contract and a wallet-connected GenLayerJS application.
- The main workflow depends on validator reasoning over natural language evidence.
- It can be extended into an explorer widget, research workflow, or community fact-checking tool.

## Review checklist

- Open `contracts/signal_guard.py` in GenLayer Studio.
- Deploy it with no constructor arguments.
- Open `web/dapp.html` and confirm that it reads the deployed StudioNet state.
- Inspect `web/signalguard-dapp.js` for the GenLayerJS `readContract`, `writeContract`, and receipt flow.
- Run `python scripts/verify_studionet_deployment.py` to compare repository and deployed source.
- Call `latest_verdict()` after review to read the stored attestation.

## Example evidence

Use `examples/sample_claims.json` as a quick test dataset.
