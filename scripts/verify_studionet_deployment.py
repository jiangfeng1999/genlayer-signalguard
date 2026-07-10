import base64
import hashlib
import json
import time
from pathlib import Path

from genlayer_py import create_client
from genlayer_py.accounts import create_account
from genlayer_py.chains import studionet


CONTRACT_ADDRESS = "0x1d496901d68FC02d105A14B81Ea0e67476A9891A"
REPO_ROOT = Path(__file__).resolve().parents[1]
LOCAL_CONTRACT = REPO_ROOT / "contracts" / "signal_guard.py"


def normalized_bytes(value: bytes) -> bytes:
    return value.replace(b"\r\n", b"\n").rstrip() + b"\n"


def rpc_with_retry(client, method: str, params: list, attempts: int = 3):
    last_error = None
    for attempt in range(attempts):
        try:
            response = client.provider.make_request(method, params)
            if response.get("error"):
                raise RuntimeError(json.dumps(response["error"], sort_keys=True))
            return response["result"]
        except Exception as error:
            last_error = error
            if attempt + 1 < attempts:
                time.sleep(2**attempt)
    raise RuntimeError(f"{method} failed after {attempts} attempts: {last_error}")


def main() -> None:
    # This ephemeral account is used only as a caller address for read-only simulation.
    client = create_client(studionet, account=create_account())
    remote_code_b64 = rpc_with_retry(client, "gen_getContractCode", [CONTRACT_ADDRESS])
    schema = rpc_with_retry(client, "gen_getContractSchema", [CONTRACT_ADDRESS])
    remote_code = normalized_bytes(base64.b64decode(remote_code_b64))
    local_code = normalized_bytes(LOCAL_CONTRACT.read_bytes())

    expected_methods = {"review_claim", "latest_claim", "latest_verdict"}
    actual_methods = set(schema.get("methods", {}))
    latest_claim = client.read_contract(CONTRACT_ADDRESS, "latest_claim", [])
    latest_verdict = client.read_contract(CONTRACT_ADDRESS, "latest_verdict", [])

    checks = {
        "source_matches_deployment": remote_code == local_code,
        "constructor_has_no_parameters": schema.get("ctor", {}).get("params") == [],
        "expected_methods_present": expected_methods.issubset(actual_methods),
        "latest_claim_readable": isinstance(latest_claim, str),
        "latest_verdict_readable": isinstance(latest_verdict, str),
    }
    report = {
        "network": studionet.name,
        "rpc_url": studionet.rpc_urls["default"]["http"][0],
        "contract_address": CONTRACT_ADDRESS,
        "local_source_sha256": hashlib.sha256(local_code).hexdigest(),
        "deployed_source_sha256": hashlib.sha256(remote_code).hexdigest(),
        "methods": sorted(actual_methods),
        "latest_claim": latest_claim,
        "latest_verdict": latest_verdict,
        "checks": checks,
        "status": "pass" if all(checks.values()) else "fail",
    }
    print(json.dumps(report, indent=2))

    if report["status"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
