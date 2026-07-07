# SignalGuard Milestone 1 Submission

## Suggested title

SignalGuard Milestone 1: Public Evidence, Dashboard, Tests, and Reviewer Tooling

## Portal category

Milestones

## Primary evidence

https://jiangfeng1999.github.io/genlayer-signalguard/web/milestone-1.html

## Supporting evidence

- https://github.com/jiangfeng1999/genlayer-signalguard/blob/main/docs/milestone-1-evidence.md
- https://github.com/jiangfeng1999/genlayer-signalguard/blob/main/docs/history-milestone-design.md
- https://jiangfeng1999.github.io/genlayer-signalguard/web/portal-dashboard.html
- https://jiangfeng1999.github.io/genlayer-signalguard/web/adversarial-testing.html
- https://jiangfeng1999.github.io/genlayer-signalguard/web/benchmarks.html
- https://jiangfeng1999.github.io/genlayer-signalguard/web/resource-pack.html
- https://jiangfeng1999.github.io/genlayer-signalguard/web/reviewer-quickstart.html

## Description

SignalGuard Milestone 1 packages the completed review infrastructure around the base SignalGuard project: a deployed contract path, static demo helper, public Portal dashboard, adversarial cases, deterministic benchmark checks, reusable resource pack, reviewer quickstart, and a conservative history prototype for future work.

## Why it fits Milestones

- It goes beyond the base project by adding reproducibility, dashboards, tests, documentation, and reusable resources.
- It gives reviewers concrete artifacts to inspect without private account access.
- It documents the boundary between the accepted project and future extensions.
- It includes a one-command evidence verifier.

## Review checklist

1. Confirm the base Project has been submitted and accepted before submitting this milestone.
2. Open `web/milestone-1.html`.
3. Inspect `docs/milestone-1-evidence.md` and `examples/milestone_evidence.json`.
4. Run `scripts/verify-evidence-package.ps1`.
5. Review the history prototype in `contracts/signal_guard_history.py`.

## Boundary

Submit this under Milestones only after the base SignalGuard Project is accepted. Do not submit it as a duplicate Project.
