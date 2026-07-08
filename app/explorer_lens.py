import argparse
import json
import re
from dataclasses import dataclass
from typing import Dict, List


ADDRESS_RE = re.compile(r"^0x[a-fA-F0-9]{40}$")


@dataclass(frozen=True)
class ExplorerTarget:
    label: str
    address: str
    studio_url: str
    explorer_url: str
    evidence_url: str


def validate_address(address: str) -> str:
    if not ADDRESS_RE.match(address):
        raise ValueError(f"Invalid GenLayer address: {address}")
    return address


def build_target() -> ExplorerTarget:
    address = validate_address("0x1d496901d68FC02d105A14B81Ea0e67476A9891A")
    return ExplorerTarget(
        label="SignalGuard Studio deployment",
        address=address,
        studio_url=f"https://studio.genlayer.com/contracts?import-contract={address}",
        explorer_url=f"https://explorer-studio.genlayer.com/address/{address}",
        evidence_url="https://jiangfeng1999.github.io/genlayer-signalguard/web/project-overview.html",
    )


def build_manifest(target: ExplorerTarget) -> Dict[str, object]:
    return {
        "tool": "SignalGuard Explorer Lens",
        "purpose": "Give reviewers a compact, reproducible explorer index for a deployed GenLayer Intelligent Contract.",
        "target": {
            "label": target.label,
            "address": target.address,
            "studio_import_url": target.studio_url,
            "studio_explorer_url": target.explorer_url,
            "public_evidence_url": target.evidence_url,
        },
        "checks": [
            {
                "name": "address_format",
                "status": "pass",
                "detail": "Address is a 20-byte 0x-prefixed hexadecimal string.",
            },
            {
                "name": "review_links",
                "status": "manual",
                "detail": "Open the Studio import URL and Studio explorer URL during review.",
            },
            {
                "name": "source_evidence",
                "status": "pass",
                "detail": "Public project overview and GitHub source are linked from the evidence hub.",
            },
        ],
    }


def build_markdown(target: ExplorerTarget) -> str:
    manifest = build_manifest(target)
    lines: List[str] = [
        "# SignalGuard Explorer Lens",
        "",
        f"- Label: {target.label}",
        f"- Contract address: `{target.address}`",
        f"- Studio import: {target.studio_url}",
        f"- Studio explorer: {target.explorer_url}",
        f"- Evidence: {target.evidence_url}",
        "",
        "## Review Checks",
    ]
    for check in manifest["checks"]:
        lines.append(f"- {check['name']}: {check['status']} - {check['detail']}")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a compact SignalGuard explorer manifest.")
    parser.add_argument("--markdown", action="store_true", help="Emit a reviewer-friendly Markdown summary.")
    args = parser.parse_args()

    target = build_target()
    if args.markdown:
        print(build_markdown(target))
    else:
        print(json.dumps(build_manifest(target), indent=2))


if __name__ == "__main__":
    main()
