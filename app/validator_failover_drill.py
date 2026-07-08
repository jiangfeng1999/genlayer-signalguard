import argparse
import json
from dataclasses import dataclass
from typing import Dict, List


@dataclass(frozen=True)
class FailoverStep:
    key: str
    trigger: str
    check: str
    action: str
    rollback: str


def drill_steps() -> List[FailoverStep]:
    return [
        FailoverStep(
            key="health_gate",
            trigger="The validator health endpoint reports a down status or a required check fails.",
            check="GET /health on the active node and standby endpoint.",
            action="Freeze non-urgent maintenance and confirm whether the standby node is healthy.",
            rollback="Keep the active node serving if the standby health check is incomplete.",
        ),
        FailoverStep(
            key="metrics_gap",
            trigger="Prometheus scrape data is missing or stale for the active node.",
            check="GET /metrics and compare scrape age against the alert threshold.",
            action="Switch monitoring target to standby and verify node, GenVM, and WebDriver collectors.",
            rollback="Restore the previous scrape target when active metrics recover.",
        ),
        FailoverStep(
            key="balance_guard",
            trigger="The active operator balance falls below the configured minimum.",
            check="GET /balance and confirm the operator account threshold.",
            action="Route writes away from the low-balance operator until replenished.",
            rollback="Return to the original operator after balance and nonce state are verified.",
        ),
        FailoverStep(
            key="snapshot_boundary",
            trigger="A state snapshot is needed before maintenance or upgrade.",
            check="POST /snapshot only from loopback or an authenticated tunnel with an operator token.",
            action="Create the snapshot and record the artifact location before failover.",
            rollback="Do not switch if the snapshot fails and the maintenance is not urgent.",
        ),
    ]


def build_drill() -> Dict[str, object]:
    return {
        "tool": "SignalGuard Validator Failover Drill",
        "purpose": "A deterministic failover drill for validator operators using health, metrics, balance, and snapshot signals.",
        "steps": [
            {
                "key": step.key,
                "trigger": step.trigger,
                "check": step.check,
                "action": step.action,
                "rollback": step.rollback,
            }
            for step in drill_steps()
        ],
        "boundaries": [
            "This is a failover drill and review fixture, not proof that this wallet runs a live validator.",
            "Operator-token actions are documented as protected operations.",
            "The drill is intended to be adapted to the operator's actual deployment topology.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Emit the SignalGuard validator failover drill.")
    parser.add_argument("--keys", action="store_true", help="Emit only drill step keys.")
    args = parser.parse_args()

    drill = build_drill()
    if args.keys:
        print(json.dumps([step["key"] for step in drill["steps"]], indent=2))
    else:
        print(json.dumps(drill, indent=2))


if __name__ == "__main__":
    main()
