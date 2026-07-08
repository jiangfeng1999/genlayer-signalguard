import argparse
import json
from dataclasses import dataclass
from typing import Dict, List


@dataclass(frozen=True)
class ContractEntry:
    key: str
    title: str
    path: str
    purpose: str
    genlayer_features: List[str]
    review_command: str


def catalog_entries() -> List[ContractEntry]:
    return [
        ContractEntry(
            key="signal_guard",
            title="SignalGuard source-grounded claim review",
            path="contracts/signal_guard.py",
            purpose="Store the latest consensus-backed verdict for a claim checked against a public source URL.",
            genlayer_features=[
                "Python Intelligent Contract",
                "gl.nondet.web.get for source fetching",
                "strict_eq source agreement",
                "prompt_non_comparative verdict classification",
                "public view getter for latest_verdict",
            ],
            review_command="python app/signalguard_cli.py",
        ),
        ContractEntry(
            key="signal_guard_history",
            title="SignalGuard history milestone prototype",
            path="contracts/signal_guard_history.py",
            purpose="Extend the base review flow with append-only review history and review_count state.",
            genlayer_features=[
                "Python Intelligent Contract",
                "source-grounded verdict flow",
                "append-only history pattern",
                "public view methods for latest verdict and review count",
            ],
            review_command="python -m py_compile contracts/signal_guard_history.py",
        ),
    ]


def build_catalog() -> Dict[str, object]:
    return {
        "tool": "SignalGuard Intelligent Contract Catalog",
        "purpose": "Index the created GenLayer Intelligent Contracts and the review path for each one.",
        "entries": [
            {
                "key": entry.key,
                "title": entry.title,
                "path": entry.path,
                "purpose": entry.purpose,
                "genlayer_features": entry.genlayer_features,
                "review_command": entry.review_command,
            }
            for entry in catalog_entries()
        ],
        "boundaries": [
            "The catalog indexes created contracts and prototypes; Project submission remains the main product entry.",
            "The history contract is a milestone prototype, not the currently deployed Studio address.",
            "Reviewers should inspect the source files and published evidence hub before scoring.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Emit the SignalGuard Intelligent Contract catalog.")
    parser.add_argument("--paths", action="store_true", help="Emit only contract source paths.")
    args = parser.parse_args()

    catalog = build_catalog()
    if args.paths:
        print(json.dumps([entry["path"] for entry in catalog["entries"]], indent=2))
    else:
        print(json.dumps(catalog, indent=2))


if __name__ == "__main__":
    main()
