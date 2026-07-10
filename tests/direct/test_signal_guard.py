CONTRACT_PATH = "contracts/signal_guard.py"
SDK_VERSION = "v0.2.16"


def test_initial_state(direct_deploy):
    contract = direct_deploy(CONTRACT_PATH, sdk_version=SDK_VERSION)

    assert contract.latest_claim() == ""
    assert contract.latest_verdict() == "No review has been stored yet."
