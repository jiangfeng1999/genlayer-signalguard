# v0.2.16
# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *


class SignalGuard(gl.Contract):
    claim: str
    source_url: str
    verdict_report: str

    def __init__(self):
        self.claim = ""
        self.source_url = ""
        self.verdict_report = "No review has been stored yet."

    @gl.public.write
    def review_claim(self, claim: str, source_url: str) -> None:
        def fetch_source() -> str:
            response = gl.nondet.web.get(source_url)
            return response.body.decode("utf-8")

        page_text = gl.eq_principle.strict_eq(fetch_source)
        prompt_input = (
            "Claim:\n"
            + claim
            + "\n\nSource URL:\n"
            + source_url
            + "\n\nSource content excerpt:\n"
            + page_text[:4000]
        )

        report = gl.eq_principle.prompt_non_comparative(
            lambda: prompt_input,
            task=(
                "Determine whether the claim is supported, contradicted, or inconclusive "
                "based only on the source content. Return compact JSON with keys "
                "verdict, confidence, and rationale."
            ),
            criteria=(
                "The verdict must be exactly one of supported, contradicted, or inconclusive. "
                "The confidence must be an integer from 0 to 100. "
                "The rationale must cite only evidence present in the source content and must not invent facts."
            ),
        )
        self.claim = claim
        self.source_url = source_url
        self.verdict_report = report

    @gl.public.view
    def latest_verdict(self) -> str:
        return self.verdict_report

    @gl.public.view
    def latest_claim(self) -> str:
        return self.claim
