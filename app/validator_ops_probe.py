import argparse
import json
from dataclasses import dataclass
from typing import Dict, List


@dataclass(frozen=True)
class OpsProbe:
    endpoint: str
    purpose: str
    public: bool
    alert_rule: str


def default_probes() -> List[OpsProbe]:
    return [
        OpsProbe(
            endpoint="/health",
            purpose="Check node, database, and consensus health before treating a validator as ready.",
            public=True,
            alert_rule="Alert when status is not up or when a required check reports down.",
        ),
        OpsProbe(
            endpoint="/metrics",
            purpose="Expose Prometheus metrics for node, GenVM, and WebDriver resource tracking.",
            public=True,
            alert_rule="Alert on missing scrape data, high CPU, memory pressure, or stalled block progress.",
        ),
        OpsProbe(
            endpoint="/balance",
            purpose="Track account balance needed for operational transactions.",
            public=True,
            alert_rule="Alert when balance drops below the operator-defined threshold.",
        ),
        OpsProbe(
            endpoint="/snapshot",
            purpose="Create an operator-authorized state snapshot for maintenance and upgrades.",
            public=False,
            alert_rule="Require operator token and local or tunneled access before invocation.",
        ),
    ]


def build_probe_manifest() -> Dict[str, object]:
    return {
        "tool": "SignalGuard Validator Ops Probe",
        "purpose": "A lightweight checklist for validator operators to verify health, metrics, balance, and snapshot readiness.",
        "default_ops_port": 9153,
        "probes": [
            {
                "endpoint": probe.endpoint,
                "purpose": probe.purpose,
                "public": probe.public,
                "alert_rule": probe.alert_rule,
            }
            for probe in default_probes()
        ],
        "boundaries": [
            "This is operator tooling; it does not claim the current wallet is running a validator.",
            "The snapshot route is intentionally marked protected because it requires an operator token.",
            "Reviewers can adapt the endpoint list to a local, tunneled, or hosted validator.",
        ],
    }


def build_prometheus_notes() -> str:
    lines = [
        "# SignalGuard Validator Ops Probe",
        "",
        "- Scrape `/metrics` from the configured ops port.",
        "- Probe `/health` before trusting validator status.",
        "- Keep `/snapshot` on loopback or behind an authenticated tunnel.",
        "- Alert on missing metrics, unhealthy checks, low balance, and stale sync.",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Emit validator ops probe fixtures.")
    parser.add_argument("--notes", action="store_true", help="Emit plain Markdown notes.")
    args = parser.parse_args()

    if args.notes:
        print(build_prometheus_notes())
    else:
        print(json.dumps(build_probe_manifest(), indent=2))


if __name__ == "__main__":
    main()
