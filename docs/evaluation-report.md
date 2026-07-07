# SignalGuard Evaluation Report

## Scope

This report evaluates whether SignalGuard is useful as a GenLayer Builder project and whether the current evidence is strong enough for reviewers to inspect.

SignalGuard is not a generic chatbot wrapper. The core behavior depends on GenLayer-specific capabilities: fetching a cited public source, asking validators to reason over natural-language evidence, and storing the accepted verdict as contract state.

## Evaluation criteria

| Criterion | Current result | Evidence |
| --- | --- | --- |
| GenLayer is central to the workflow | Pass | `contracts/signal_guard.py` uses web access and `prompt_non_comparative`. |
| Reviewer can reproduce the call shape | Pass | `app/signalguard_cli.py` and `web/index.html` prepare `review_claim` inputs. |
| CLI helper is locally testable | Pass | `scripts/test-signalguard-cli.ps1` verifies the generated payload shape. |
| Reviewer can inspect expected verdict behavior | Pass | `examples/adversarial_claims.json` lists supported, contradicted, and inconclusive cases. |
| Public status can be checked without login | Pass | `scripts/check-genlayer-status.ps1` reads public Portal and GitHub endpoints. |
| Dashboard calculations are testable | Pass | `scripts/test-portal-dashboard-calculations.ps1` checks the offline fixture. |
| Evidence is currently public on GitHub main | Partial | A prepared sync branch exists locally, but GitHub main still needs to be updated. |

## Contract behavior

The contract stores three fields:

- `claim`
- `source_url`
- `verdict_report`

The `review_claim` method fetches the cited page, asks validators to classify the claim as `supported`, `contradicted`, or `inconclusive`, and stores the compact report. The view methods expose the latest claim and verdict for a simple app or reviewer workflow.

## Dashboard behavior

The Portal dashboard is a static HTML file that reads public Portal endpoints and displays:

- Builder points for a wallet address.
- Public Builder rank when available.
- Gap to the current #1 Builder.
- Accepted public Builder contribution count.
- Top public contribution categories by current maximum display points.

The dashboard is intentionally static so it can be reviewed directly from GitHub or a simple HTTP server.

## Risk review

| Risk | Mitigation |
| --- | --- |
| Source pages change over time | Adversarial cases include expected verdicts and should be rechecked before submission. |
| Large source pages exceed prompt budget | The contract uses a compact source excerpt. Future work can add chunking. |
| Single latest verdict limits history | A future milestone can store verdicts by claim hash. |
| Dashboard depends on public API availability | Status scripts record API errors instead of fabricating values. |
| GitHub evidence may lag local work | The sync branch and patch bundle preserve the exact public update package. |

## Current conclusion

SignalGuard is a valid Builder-style project because it uses GenLayer as the decision layer, not as a decorative dependency. The strongest next step is to publish the prepared GitHub evidence so the already-submitted Project has matching code, dashboard files, benchmarks, and adversarial tests available for review.
