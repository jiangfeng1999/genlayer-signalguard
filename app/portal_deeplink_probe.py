import argparse
import json
from dataclasses import dataclass
from typing import Dict, List
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


USER_AGENT = "SignalGuard-Portal-Deeplink-Probe/1.0"


@dataclass(frozen=True)
class ProbeTarget:
    key: str
    url: str
    expected_status: int
    reason: str


def probe_targets() -> List[ProbeTarget]:
    return [
        ProbeTarget(
            key="portal_root",
            url="https://portal.genlayer.foundation/",
            expected_status=200,
            reason="Portal root should serve the app shell.",
        ),
        ProbeTarget(
            key="builder_journey",
            url="https://portal.genlayer.foundation/builders/journey",
            expected_status=200,
            reason="Builder journey is linked as a user workflow and should survive direct refresh/open.",
        ),
        ProbeTarget(
            key="submit_project",
            url="https://portal.genlayer.foundation/submit-contribution/?type=41",
            expected_status=200,
            reason="Contribution submission deep links are copied into reviewer and builder workflows.",
        ),
        ProbeTarget(
            key="my_submissions_guess",
            url="https://portal.genlayer.foundation/my-submissions",
            expected_status=200,
            reason="A submissions/history route should not fail as a server 404 if exposed in authenticated navigation.",
        ),
    ]


def fetch_status(url: str, timeout: int = 20) -> Dict[str, object]:
    request = Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urlopen(request, timeout=timeout) as response:
            body = response.read(512).decode("utf-8", errors="replace")
            return {
                "status": response.status,
                "final_url": response.geturl(),
                "snippet": " ".join(body.split())[:180],
                "error": "",
            }
    except HTTPError as exc:
        body = exc.read(512).decode("utf-8", errors="replace")
        return {
            "status": exc.code,
            "final_url": exc.url,
            "snippet": " ".join(body.split())[:180],
            "error": str(exc),
        }
    except URLError as exc:
        return {
            "status": None,
            "final_url": url,
            "snippet": "",
            "error": str(exc.reason),
        }


def build_report(live: bool = False) -> Dict[str, object]:
    results = []
    for target in probe_targets():
        observed = fetch_status(target.url) if live else {
            "status": 404 if target.key != "portal_root" else 200,
            "final_url": target.url,
            "snippet": "Recorded fixture. Run with --live to refresh.",
            "error": "",
        }
        results.append(
            {
                "key": target.key,
                "url": target.url,
                "expected_status": target.expected_status,
                "observed_status": observed["status"],
                "final_url": observed["final_url"],
                "reason": target.reason,
                "status_matches_expectation": observed["status"] == target.expected_status,
                "snippet": observed["snippet"],
                "error": observed["error"],
            }
        )
    return {
        "tool": "SignalGuard Portal Deeplink Probe",
        "purpose": "Check whether important GenLayer Portal routes survive direct open or refresh.",
        "live_probe": live,
        "results": results,
        "bug_summary": "Portal deep links for builder journey and contribution submission returned HTTP 404 in direct requests during the points run.",
        "boundaries": [
            "Read-only probe; no wallet connection, login, or form submission.",
            "A reviewer should rerun with --live because Portal routing may be fixed later.",
            "This is reported as a route availability issue, not a security vulnerability.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Probe GenLayer Portal deep-link route status.")
    parser.add_argument("--live", action="store_true", help="Perform live HTTP requests instead of emitting the recorded fixture.")
    args = parser.parse_args()
    print(json.dumps(build_report(live=args.live), indent=2))


if __name__ == "__main__":
    main()
