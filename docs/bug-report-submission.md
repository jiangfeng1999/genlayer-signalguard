# SignalGuard Portal Deeplink Bug Report

## Suggested title

GenLayer Portal Deep Links Return HTTP 404 on Direct Open

## Portal category

Bug Report

## Primary evidence

https://jiangfeng1999.github.io/genlayer-signalguard/web/bug-report.html

## Supporting evidence

- https://github.com/jiangfeng1999/genlayer-signalguard/blob/main/app/portal_deeplink_probe.py
- https://github.com/jiangfeng1999/genlayer-signalguard/blob/main/examples/portal_deeplink_probe.json
- https://portal.genlayer.foundation/builders/journey
- https://portal.genlayer.foundation/submit-contribution/?type=41
- https://portal.genlayer.foundation/my-submissions

## Description

During the SignalGuard points run, several GenLayer Portal deep links returned server-side HTTP 404 when opened directly: the builder journey route, contribution submission route, and an expected submissions-history route. These routes are part of user workflows or copied submission helper links, so direct open or refresh should ideally serve the Portal app shell and let the client route handle the page state.

## Reproduction

Run from the repository root:

```powershell
python app\portal_deeplink_probe.py --live
```

Expected behavior: important Portal workflow deep links return HTTP 200 and render the app shell.

Observed behavior during this run: root returned 200; builder journey, submit-contribution, and my-submissions style deep links returned 404.

## Review boundaries

- This is a read-only availability/routing bug report, not a security vulnerability claim.
- It does not require wallet connection, login, reCAPTCHA, or form submission.
- Portal routing may be fixed later; reviewers should rerun the live probe.
