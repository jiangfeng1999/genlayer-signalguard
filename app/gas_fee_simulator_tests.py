import argparse
import json
from dataclasses import dataclass
from typing import Dict, List


@dataclass(frozen=True)
class GasCase:
    key: str
    operation: str
    expected_fee_behavior: str
    studio_note: str
    live_network_note: str
    risk: str


def gas_cases() -> List[GasCase]:
    return [
        GasCase(
            key="view_latest_verdict",
            operation="Read latest_verdict from SignalGuard.",
            expected_fee_behavior="Read-only view calls should not require a write transaction.",
            studio_note="Studio can execute the getter for inspection without a wallet fee flow.",
            live_network_note="DApp reads should use readContract or equivalent free view flow.",
            risk="Accidentally treating a read as a write creates avoidable wallet prompts.",
        ),
        GasCase(
            key="write_review_claim",
            operation="Call review_claim with a claim and source URL.",
            expected_fee_behavior="State-changing writes require signing, transaction processing, and sufficient balance for fees.",
            studio_note="Studio transactions do not consume gas, so this is only a functional prototype check.",
            live_network_note="Live clients should estimate or bound fees before asking the user to sign.",
            risk="A Studio-only test can hide fee, balance, or finalization behavior.",
        ),
        GasCase(
            key="oversized_source_url",
            operation="Submit a very long source URL.",
            expected_fee_behavior="Input length should be bounded before the write transaction is attempted.",
            studio_note="Use local validation to reject malformed or oversized input before Studio execution.",
            live_network_note="Rejecting bad input client-side reduces failed transactions and fee waste.",
            risk="Bad inputs can waste user time and fees even when the contract rejects them.",
        ),
        GasCase(
            key="repeat_review_claim",
            operation="Submit multiple review_claim calls in sequence.",
            expected_fee_behavior="Each state-changing call should be treated as a separate fee-bearing transaction.",
            studio_note="Studio can demonstrate state replacement but not real fee accumulation.",
            live_network_note="Batching or user confirmation copy should make repeated write costs explicit.",
            risk="Users may assume a repeated prototype interaction is free on live networks.",
        ),
    ]


def build_report() -> Dict[str, object]:
    cases = []
    for case in gas_cases():
        cases.append(
            {
                "key": case.key,
                "operation": case.operation,
                "expected_fee_behavior": case.expected_fee_behavior,
                "studio_note": case.studio_note,
                "live_network_note": case.live_network_note,
                "risk": case.risk,
            }
        )
    return {
        "tool": "SignalGuard Gas Fee Simulator Tests",
        "scope": "Local test matrix for fee-aware SignalGuard write/read flows.",
        "boundaries": [
            "Does not claim to calculate real mainnet or testnet gas.",
            "Separates Studio prototype behavior from live-network fee behavior.",
            "Uses deterministic fixtures so reviewers can inspect the assumptions.",
        ],
        "cases": cases,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Emit SignalGuard gas-fee simulator test fixtures.")
    parser.add_argument("--keys", action="store_true", help="Emit only case keys.")
    args = parser.parse_args()

    report = build_report()
    if args.keys:
        print(json.dumps([case["key"] for case in report["cases"]], indent=2))
    else:
        print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
