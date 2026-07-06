# Tooling Notes

This repository includes a minimal app-side helper for reviewers who want to test the Intelligent Contract quickly in GenLayer Studio.

## CLI helper

`app/signalguard_cli.py` builds a `review_claim` payload from a claim and a source URL:

```bash
python app/signalguard_cli.py "GenLayer can use AI validators for subjective decisions" "https://docs.genlayer.com/understand-genlayer-protocol/what-is-genlayer"
```

The output is JSON:

```json
{
  "method": "review_claim",
  "args": {
    "claim": "...",
    "source_url": "..."
  }
}
```

Reviewers can copy the method and arguments into Studio after deploying `contracts/signal_guard.py`.

## Static demo

`web/index.html` provides the same payload preparation flow without a build system. It is deliberately static so the project remains easy to inspect.

## Verification performed

The Python files compile locally with:

```bash
python -m py_compile app\signalguard_cli.py contracts\signal_guard.py
```

The helper has also been tested with a GenLayer documentation URL and produces a valid payload structure.

