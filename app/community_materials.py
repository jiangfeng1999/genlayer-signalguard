import argparse
import json
from dataclasses import dataclass
from typing import Dict, List


@dataclass(frozen=True)
class Material:
    key: str
    category: str
    title: str
    audience: str
    purpose: str
    artifacts: List[str]
    boundary: str


def materials() -> List[Material]:
    return [
        Material(
            key="marketing_networking",
            category="Marketing & Networking",
            title="SignalGuard Builder Networking Kit",
            audience="GenLayer builders, reviewers, and ecosystem partners",
            purpose="Provide a concise one-page explanation, review links, and conversation prompts for introducing SignalGuard.",
            artifacts=[
                "Project one-liner and value proposition",
                "Evidence hub links",
                "Builder conversation prompts",
                "Reviewer call-to-action",
            ],
            boundary="This is a public networking kit, not a claim of attendee counts or social engagement.",
        ),
        Material(
            key="community_outreach",
            category="Community outreach",
            title="SignalGuard Community Outreach FAQ Pack",
            audience="Builders asking how to inspect or adapt a source-grounded contract",
            purpose="Give short answers and links that can be reused when explaining SignalGuard to the community.",
            artifacts=[
                "FAQ entries",
                "Public demo links",
                "Contribution category map",
                "Safety notes about rewards and review",
            ],
            boundary="This is outreach material, not evidence of fake engagement or mass posting.",
        ),
        Material(
            key="community_support",
            category="Community Support",
            title="SignalGuard Community Support Triage Guide",
            audience="Builders debugging Portal submissions or SignalGuard review flows",
            purpose="Help users route common support questions to project evidence, Portal status checks, or manual wallet actions.",
            artifacts=[
                "Triage table",
                "Portal status commands",
                "Wallet and reCAPTCHA boundary reminders",
                "Reviewer evidence links",
            ],
            boundary="This is support documentation, not a promise to operate official GenLayer support.",
        ),
        Material(
            key="meta_contributions",
            category="Meta Contributions",
            title="SignalGuard Portal Evidence Workflow Retrospective",
            audience="Portal reviewers and builders planning contribution evidence",
            purpose="Summarize the evidence workflow, guardrails, and lessons learned from packaging SignalGuard submissions.",
            artifacts=[
                "Submission queue model",
                "Verifier pattern",
                "Risk controls for duplicate evidence",
                "Manual-confirmation boundary",
            ],
            boundary="This is a process contribution about improving submission quality, not a request to bypass review.",
        ),
    ]


def build_pack() -> Dict[str, object]:
    return {
        "tool": "SignalGuard Community Materials Pack",
        "purpose": "Publish reusable community, support, and meta-contribution materials around SignalGuard.",
        "materials": [
            {
                "key": item.key,
                "category": item.category,
                "title": item.title,
                "audience": item.audience,
                "purpose": item.purpose,
                "artifacts": item.artifacts,
                "boundary": item.boundary,
            }
            for item in materials()
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Emit SignalGuard community material fixtures.")
    parser.add_argument("--keys", action="store_true", help="Emit only material keys.")
    args = parser.parse_args()

    pack = build_pack()
    if args.keys:
        print(json.dumps([item["key"] for item in pack["materials"]], indent=2))
    else:
        print(json.dumps(pack, indent=2))


if __name__ == "__main__":
    main()
