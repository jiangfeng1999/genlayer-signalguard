# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmw5fhh8jpz09h6" }

from genlayer import *


class SignalGuard(gl.Contract):
    claim: str
    source_url: str
    verdict_report: str
    review_count: u256

    def __init__(self, initial_claim: str, initial_source_url: str):
        self.claim = initial_claim
        self.source_url = initial_source_url
        self.verdict_report = "No review has been stored yet."
        self.review_count = 0

    @gl.public.write
    def review_claim(self, claim: str, source_url: str) -> None:
        def source_input() -> str:
            response = gl.nondet.web.get(source_url)
            page_text = response.body.decode("utf-8")
            return (
                "Claim:\n"
                + claim
                + "\n\nSource URL:\n"
                + source_url
                + "\n\nSource content excerpt:\n"
                + page_text[:6000]
            )

        report = gl.eq_principle.prompt_non_comparative(
            source_input,
            task=(
                "Determine whether the claim is supported, contradicted, or inconclusive "
                "based only on the source content. Return compact JSON with keys "
                "verdict, confidence, and rationale."
            ),
            criteria=(
                "The verdict must be exactly one of supported, contradicted, or inconclusive. "
                "The confidence must be an integer from 0 to 100. "
                "The rationale must cite only evidence present in the source content and must "
                "not invent facts."
            ),
        )

        self.claim = claim
        self.source_url = source_url
        self.verdict_report = report
        self.review_count = self.review_count + 1

    @gl.public.view
    def latest_verdict(self) -> str:
        return (
            "claim="
            + self.claim
            + " | source="
            + self.source_url
            + " | reviews="
            + str(self.review_count)
            + " | report="
            + self.verdict_report
        )
