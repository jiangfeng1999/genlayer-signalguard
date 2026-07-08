import argparse
import json
from dataclasses import dataclass
from typing import Dict, List
from urllib.parse import urlencode


@dataclass(frozen=True)
class SourceAdapter:
    key: str
    label: str
    source_url: str
    claim_template: str
    review_note: str

    def build_case(self, claim: str = "") -> Dict[str, str]:
        return {
            "adapter": self.key,
            "label": self.label,
            "claim": claim or self.claim_template,
            "source_url": self.source_url,
            "review_note": self.review_note,
        }


def coingecko_price_adapter(asset_id: str = "ethereum", currency: str = "usd") -> SourceAdapter:
    query = urlencode({"ids": asset_id, "vs_currencies": currency})
    return SourceAdapter(
        key="coingecko_price",
        label="CoinGecko simple price API",
        source_url=f"https://api.coingecko.com/api/v3/simple/price?{query}",
        claim_template=f"{asset_id} has a quoted {currency.upper()} price in the CoinGecko simple price response.",
        review_note="Use for price-source freshness and schema checks, not as investment advice.",
    )


def open_meteo_adapter(latitude: str = "37.7749", longitude: str = "-122.4194") -> SourceAdapter:
    query = urlencode(
        {
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,wind_speed_10m",
            "timezone": "UTC",
        }
    )
    return SourceAdapter(
        key="open_meteo_current_weather",
        label="Open-Meteo current weather API",
        source_url=f"https://api.open-meteo.com/v1/forecast?{query}",
        claim_template="The Open-Meteo response contains current temperature and wind speed fields.",
        review_note="Use for structured weather-data availability checks.",
    )


def github_release_adapter(owner: str = "genlayerlabs", repo: str = "genlayer-js") -> SourceAdapter:
    return SourceAdapter(
        key="github_latest_release",
        label="GitHub latest release API",
        source_url=f"https://api.github.com/repos/{owner}/{repo}/releases/latest",
        claim_template=f"The {owner}/{repo} repository exposes latest-release metadata through the GitHub API.",
        review_note="Use for release metadata checks. Reviewers can replace owner/repo with another public repository.",
    )


def documentation_adapter(url: str = "https://docs.genlayer.com/") -> SourceAdapter:
    return SourceAdapter(
        key="documentation_page",
        label="Documentation page",
        source_url=url,
        claim_template="The cited documentation page is reachable and contains project documentation text.",
        review_note="Use for generic public documentation checks.",
    )


def default_adapters() -> List[SourceAdapter]:
    return [
        coingecko_price_adapter(),
        open_meteo_adapter(),
        github_release_adapter(),
        documentation_adapter(),
    ]


def build_signalguard_payload(case: Dict[str, str]) -> Dict[str, object]:
    return {
        "method": "review_claim",
        "args": {
            "claim": case["claim"],
            "source_url": case["source_url"],
        },
        "metadata": {
            "adapter": case["adapter"],
            "label": case["label"],
            "review_note": case["review_note"],
        },
    }


def build_cases() -> List[Dict[str, str]]:
    return [adapter.build_case() for adapter in default_adapters()]


def main() -> None:
    parser = argparse.ArgumentParser(description="Build SignalGuard source-adapter cases.")
    parser.add_argument("--payloads", action="store_true", help="Emit review_claim payloads instead of adapter cases.")
    args = parser.parse_args()

    cases = build_cases()
    output = [build_signalguard_payload(case) for case in cases] if args.payloads else cases
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
