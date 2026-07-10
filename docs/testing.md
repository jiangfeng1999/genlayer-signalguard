# SignalGuard Testing and Verification

## Verification layers

SignalGuard separates local contract tests from live deployment checks.

### 1. Python and fixture checks

`scripts/verify-evidence-package.ps1` compiles repository Python files, validates JSON fixtures, exercises the CLI payload helper, and checks the static project pages.

### 2. GenLayer Direct Mode

`tests/direct/test_signal_guard.py` loads the deployed contract source with GenVM `v0.2.16` and verifies constructor state and view methods. Run it on Linux because the current `genlayer-test` Direct Mode loader keeps a temporary stdin file open in a way that Windows does not permit.

```bash
python -m pip install -r requirements-dev.txt
python -m pytest tests/direct -q
```

The old `ExecPromptTemplate` request used by GenVM `v0.2.16` is not handled by the current Direct Mode LLM mock adapter, so this repository does not claim mocked write-path coverage.

### 3. Live StudioNet deployment verification

`scripts/verify_studionet_deployment.py` uses the official Python SDK and public StudioNet RPC to:

- download the deployed contract source;
- compare it with `contracts/signal_guard.py`;
- inspect the public contract schema;
- read `latest_claim` and `latest_verdict` without sending a transaction.

The script creates an ephemeral caller address only for read simulation. It does not print a private key, fund an account, or broadcast a transaction.

### 4. Browser DApp

`web/dapp.html` shows the latest deployment snapshot without requesting wallet access. After the user connects a browser wallet, `web/signalguard-dapp.js` performs live reads and writes through the injected provider. Private keys never enter the page or repository.

## CI

`.github/workflows/quality.yml` runs the Linux Direct Mode test, live StudioNet verification, and evidence package verifier on every push to `main` and every pull request.
