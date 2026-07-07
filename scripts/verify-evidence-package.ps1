$ErrorActionPreference = "Stop"

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = Split-Path -Parent $scriptDir

function Invoke-Check {
    param(
        [Parameter(Mandatory = $true)][string]$Name,
        [Parameter(Mandatory = $true)][scriptblock]$Body
    )

    try {
        & $Body | Out-Null
        return [pscustomobject]@{
            name = $Name
            status = "pass"
            error = $null
        }
    }
    catch {
        return [pscustomobject]@{
            name = $Name
            status = "fail"
            error = $_.Exception.Message
        }
    }
}

$results = @()

Push-Location $repoRoot
try {
    $results += Invoke-Check "required files exist" {
        $required = @(
            "contracts\signal_guard.py",
            "contracts\signal_guard_history.py",
            "app\signalguard_cli.py",
            "web\index.html",
            "web\tutorial.html",
            "web\portal-dashboard.html",
            "web\research-analysis.html",
            "docs\evaluation-report.md",
            "docs\educational-content-submission.md",
            "docs\milestone-1-evidence.md",
            "docs\research-analysis-submission.md",
            "docs\history-milestone-design.md",
            "examples\milestone_evidence.json"
        )
        foreach ($path in $required) {
            if (-not (Test-Path -LiteralPath (Join-Path $repoRoot $path))) {
                throw "Missing required file: $path"
            }
        }
    }

    $results += Invoke-Check "python files compile" {
        & python -m py_compile app\signalguard_cli.py contracts\signal_guard.py contracts\signal_guard_history.py
        if ($LASTEXITCODE -ne 0) {
            throw "Python compilation failed."
        }
    }

    $results += Invoke-Check "cli payload helper" {
        & (Join-Path $scriptDir "test-signalguard-cli.ps1") | ConvertFrom-Json | Out-Null
    }

    $results += Invoke-Check "dashboard calculations" {
        & (Join-Path $scriptDir "test-portal-dashboard-calculations.ps1") | ConvertFrom-Json | Out-Null
    }

    $results += Invoke-Check "json examples parse" {
        $jsonFiles = @(
            "examples\sample_claims.json",
            "examples\adversarial_claims.json",
            "examples\portal_dashboard_checks.json",
            "examples\dashboard_calculation_fixture.json",
            "examples\milestone_evidence.json"
        )
        foreach ($path in $jsonFiles) {
            Get-Content -LiteralPath (Join-Path $repoRoot $path) -Raw | ConvertFrom-Json | Out-Null
        }
    }

    $results += Invoke-Check "static pages contain expected hooks" {
        $demo = Get-Content -LiteralPath (Join-Path $repoRoot "web\index.html") -Raw
        $tutorial = Get-Content -LiteralPath (Join-Path $repoRoot "web\tutorial.html") -Raw
        $dashboard = Get-Content -LiteralPath (Join-Path $repoRoot "web\portal-dashboard.html") -Raw
        $research = Get-Content -LiteralPath (Join-Path $repoRoot "web\research-analysis.html") -Raw
        if ($demo -notmatch "review_claim") {
            throw "web/index.html does not contain review_claim."
        }
        if ($tutorial -notmatch "Source-Grounded Claim Review Contract" -or $tutorial -notmatch "Educational Content") {
            throw "web/tutorial.html does not contain the expected tutorial markers."
        }
        if ($dashboard -notmatch "portal-admin\.genlayer\.foundation") {
            throw "web/portal-dashboard.html does not call the public Portal API."
        }
        if ($dashboard -notmatch "FALLBACK_DATA") {
            throw "web/portal-dashboard.html does not include a bundled public fallback snapshot."
        }
        if ($research -notmatch "SignalGuard Research Analysis" -or $research -notmatch "Research &amp; Analysis") {
            throw "web/research-analysis.html does not contain the expected research report markers."
        }
    }
}
finally {
    Pop-Location
}

$failed = @($results | Where-Object { $_.status -ne "pass" })
$summary = [pscustomobject]@{
    checked_at = Get-Date -Format o
    status = if ($failed.Count -eq 0) { "pass" } else { "fail" }
    passed = @($results | Where-Object { $_.status -eq "pass" }).Count
    failed = $failed.Count
    checks = $results
}

$summary | ConvertTo-Json -Depth 6

if ($failed.Count -gt 0) {
    exit 1
}
