import argparse
import json


def build_payload(claim: str, source_url: str) -> dict:
    return {
        "method": "review_claim",
        "args": {
            "claim": claim,
            "source_url": source_url,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a SignalGuard contract-call payload.")
    parser.add_argument("--claim", required=True)
    parser.add_argument("--source-url", required=True)
    args = parser.parse_args()
    print(json.dumps(build_payload(args.claim, args.source_url), indent=2))


if __name__ == "__main__":
    main()
