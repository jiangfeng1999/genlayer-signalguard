# SignalGuard Evaluation Report

Updated: 2026-07-10

## Result

SignalGuard now satisfies the main technical shape of the Portal Projects category: a deployed Intelligent Contract, a user-facing application that actually interacts with GenLayer, and reproducible public evidence.

| Criterion | Result | Evidence |
| --- | --- | --- |
| GenLayer is central | Pass | `review_claim` fetches evidence and uses validator consensus before state changes. |
| Real application interaction | Pass | `web/signalguard-dapp.js` uses GenLayerJS for reads, wallet connection, writes, and receipt waiting. |
| Public deployment | Pass | StudioNet contract `0x1d496901d68FC02d105A14B81Ea0e67476A9891A`. |
| Source matches deployment | Pass | `scripts/verify_studionet_deployment.py` compares normalized source hashes. |
| Public schema is reproducible | Pass | The verifier checks constructor and `review_claim`, `latest_claim`, and `latest_verdict`. |
| Direct Mode coverage | Partial | The pinned Linux test verifies deployment and initial storage; the old prompt template is not mockable by the current Direct Mode adapter. |
| CI evidence | Pass | `.github/workflows/quality.yml` runs tests, deployment verification, and package checks. |

## Verified deployment result

The repository and StudioNet deployment normalize to this SHA-256:

```text
8963b191a60722ccb27b45eb4e6c90a314e089337e0b65871ba29e7758902fac
```

The live schema exposes:

- `review_claim(claim: string, source_url: string)`
- `latest_claim() -> string`
- `latest_verdict() -> string`

## Risks and mitigations

| Risk | Current mitigation | Future work |
| --- | --- | --- |
| Source content can change | Every review stores the cited URL with the accepted report. | Add source digest and timestamp metadata. |
| Only the latest review is stored | Scope is explicit in the DApp and docs. | Deploy a bounded-history contract upgrade. |
| Arbitrary HTTPS sources may be unreliable | DApp requires HTTPS and bounded input lengths. | Add contract-level URL policy controls in a new deployment. |
| LLM report is stored as text | Prompt criteria constrain the JSON shape. | Parse and store typed verdict fields in a new deployment. |
| Old SDK prompt templates are not supported by current Direct Mode mocks | Live source/schema/state verification covers the deployed artifact. | Upgrade and redeploy on a current GenVM SDK after base review. |

## Conclusion

The strongest review evidence is now the live DApp plus the source-to-deployment verifier. Supporting dashboards, tutorials, and research remain useful context, but they should not replace these primary artifacts or be submitted as duplicate Projects.
