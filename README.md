# GenLayer SignalGuard

SignalGuard is a working GenLayer DApp for checking whether a public claim is supported by a cited source. Its deployed Intelligent Contract fetches the source, asks GenLayer validators to classify the claim, and stores the accepted verdict on StudioNet.

## Live project

- DApp: https://jiangfeng1999.github.io/genlayer-signalguard/web/dapp.html
- Project overview: https://jiangfeng1999.github.io/genlayer-signalguard/web/project-overview.html
- Intelligent Contract review: https://jiangfeng1999.github.io/genlayer-signalguard/web/intelligent-contract.html
- Studio import: https://studio.genlayer.com/contracts?import-contract=0x1d496901d68FC02d105A14B81Ea0e67476A9891A
- Deployed address: `0x1d496901d68FC02d105A14B81Ea0e67476A9891A`
- Reviewer quickstart: https://jiangfeng1999.github.io/genlayer-signalguard/web/reviewer-quickstart.html

## Why GenLayer is required

The consensus-critical question is not calculated by the frontend or a private server. The Intelligent Contract:

1. receives a claim and an HTTPS source URL;
2. fetches the cited source inside GenVM;
3. asks validators to classify the claim as `supported`, `contradicted`, or `inconclusive`;
4. stores the accepted report as shared contract state.

A normal deterministic contract cannot interpret changing natural-language evidence. The frontend only collects user intent, connects a wallet, sends the contract call, and displays accepted state.

## Core repository layout

```text
contracts/signal_guard.py              Deployed Intelligent Contract source
web/dapp.html                          Wallet-connected SignalGuard application
web/signalguard-dapp.js                GenLayerJS read/write integration
app/signalguard_cli.py                 CLI payload helper
scripts/verify_studionet_deployment.py Live source, schema, and state verifier
tests/direct/test_signal_guard.py       GenLayer Direct Mode storage test
docs/project-submission.md              Reviewer-facing Project evidence
docs/testing.md                         Reproducible verification notes
```

Additional research, examples, and operational material remain available under `docs/`, `examples/`, and `web/`, but they are supporting evidence rather than separate Project claims.

## Use the DApp

The public page shows the latest deployment snapshot produced by the verification script. After wallet connection it performs live StudioNet reads and writes through the injected provider. To submit a review:

1. open the DApp in a browser with MetaMask;
2. connect the wallet to GenLayer StudioNet;
3. enter a claim and an HTTPS source;
4. approve the `review_claim` transaction in the wallet;
5. wait for the accepted receipt and refreshed contract state.

The page never requests or stores a private key.

## Verify the deployment

Create a Python 3.12 environment and install the pinned verification dependencies:

```bash
python -m pip install -r requirements-dev.txt
```

Verify that the public StudioNet bytecode source matches this repository and that the deployed schema and view methods are readable:

```bash
python scripts/verify_studionet_deployment.py
```

Expected checks:

```text
source_matches_deployment: true
constructor_has_no_parameters: true
expected_methods_present: true
latest_claim_readable: true
latest_verdict_readable: true
```

Run the GenLayer Direct Mode storage test on Linux:

```bash
python -m pytest tests/direct -q
```

Run the full static evidence verifier on Windows or Linux PowerShell:

```powershell
./scripts/verify-evidence-package.ps1
```

GitHub Actions runs these checks for every push to `main` and every pull request.

## Contract interface

```text
review_claim(claim: str, source_url: str) -> None
latest_claim() -> str
latest_verdict() -> str
```

The repository contract and the deployed StudioNet source currently normalize to the same SHA-256:

```text
8963b191a60722ccb27b45eb4e6c90a314e089337e0b65871ba29e7758902fac
```

## Scope and limitations

- SignalGuard stores the latest accepted review, not a complete review history.
- Source availability and content changes can affect later reviews.
- The current deployment uses GenVM `v0.2.16`; the verification dependencies are pinned for reproducibility.
- A future contract upgrade can add bounded history, URL policy controls, and structured verdict storage after the base Project is reviewed.

## References

- GenLayer DApp workflow: https://docs.genlayer.com/developers/decentralized-applications/dapp-development-workflow
- When to use GenLayer: https://docs.genlayer.com/developers/intelligent-contracts/when-to-use-genlayer
- GenLayerJS: https://docs.genlayer.com/api-references/genlayer-js
- Contract testing: https://docs.genlayer.com/developers/intelligent-contracts/testing
