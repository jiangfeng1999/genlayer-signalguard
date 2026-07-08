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
            "app\source_adapter_pack.py",
            "app\graybox_harness.py",
            "app\explorer_lens.py",
            "app\gas_fee_simulator_tests.py",
            "app\validator_ops_probe.py",
            "app\contract_catalog.py",
            "app\validator_failover_drill.py",
            "app\community_materials.py",
            "app\portal_deeplink_probe.py",
            "index.html",
            "web\index.html",
            "web\project-overview.html",
            "web\milestone-1.html",
            "web\third-party-integrations.html",
            "web\grayboxing.html",
            "web\explorer-lens.html",
            "web\gas-fees-simulator-tests.html",
            "web\validator-tooling.html",
            "web\create-intelligent-contracts.html",
            "web\validator-failover.html",
            "web\blog-signalguard.html",
            "web\marketing-networking.html",
            "web\community-outreach.html",
            "web\community-support.html",
            "web\meta-contributions.html",
            "web\bug-report.html",
            "web\tutorial.html",
            "web\portal-dashboard.html",
            "web\research-analysis.html",
            "web\adversarial-testing.html",
            "web\benchmarks.html",
            "web\tools-infrastructure.html",
            "web\resource-pack.html",
            "web\reviewer-quickstart.html",
            "docs\evaluation-report.md",
            "docs\project-submission.md",
            "docs\milestone-1-submission.md",
            "docs\third-party-integrations-submission.md",
            "docs\grayboxing-submission.md",
            "docs\explorer-submission.md",
            "docs\gas-fees-simulator-tests-submission.md",
            "docs\validator-tooling-submission.md",
            "docs\create-intelligent-contracts-submission.md",
            "docs\validator-failover-submission.md",
            "docs\blog-post-submission.md",
            "docs\marketing-networking-submission.md",
            "docs\community-outreach-submission.md",
            "docs\community-support-submission.md",
            "docs\meta-contributions-submission.md",
            "docs\bug-report-submission.md",
            "docs\educational-content-submission.md",
            "docs\milestone-1-evidence.md",
            "docs\research-analysis-submission.md",
            "docs\adversarial-testing-submission.md",
            "docs\benchmarks-submission.md",
            "docs\tools-infrastructure-submission.md",
            "docs\resource-creation-submission.md",
            "docs\documentation-submission.md",
            "docs\history-milestone-design.md",
            "examples\milestone_evidence.json",
            "examples\source_adapter_cases.json",
            "examples\graybox_cases.json",
            "examples\explorer_lens_manifest.json",
            "examples\gas_fee_cases.json",
            "examples\validator_ops_probe_sample.json",
            "examples\contract_catalog.json",
            "examples\validator_failover_drill.json",
            "examples\community_materials.json",
            "examples\portal_deeplink_probe.json"
        )
        foreach ($path in $required) {
            if (-not (Test-Path -LiteralPath (Join-Path $repoRoot $path))) {
                throw "Missing required file: $path"
            }
        }
    }

    $results += Invoke-Check "python files compile" {
        & python -m py_compile app\signalguard_cli.py app\source_adapter_pack.py app\graybox_harness.py app\explorer_lens.py app\gas_fee_simulator_tests.py app\validator_ops_probe.py app\contract_catalog.py app\validator_failover_drill.py app\community_materials.py app\portal_deeplink_probe.py contracts\signal_guard.py contracts\signal_guard_history.py
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
            "examples\milestone_evidence.json",
            "examples\source_adapter_cases.json",
            "examples\graybox_cases.json",
            "examples\explorer_lens_manifest.json",
            "examples\gas_fee_cases.json",
            "examples\validator_ops_probe_sample.json",
            "examples\contract_catalog.json",
            "examples\validator_failover_drill.json",
            "examples\community_materials.json",
            "examples\portal_deeplink_probe.json"
        )
        foreach ($path in $jsonFiles) {
            Get-Content -LiteralPath (Join-Path $repoRoot $path) -Raw | ConvertFrom-Json | Out-Null
        }
    }

    $results += Invoke-Check "static pages contain expected hooks" {
        $hub = Get-Content -LiteralPath (Join-Path $repoRoot "index.html") -Raw
        $demo = Get-Content -LiteralPath (Join-Path $repoRoot "web\index.html") -Raw
        $project = Get-Content -LiteralPath (Join-Path $repoRoot "web\project-overview.html") -Raw
        $milestone = Get-Content -LiteralPath (Join-Path $repoRoot "web\milestone-1.html") -Raw
        $integrations = Get-Content -LiteralPath (Join-Path $repoRoot "web\third-party-integrations.html") -Raw
        $grayboxing = Get-Content -LiteralPath (Join-Path $repoRoot "web\grayboxing.html") -Raw
        $explorer = Get-Content -LiteralPath (Join-Path $repoRoot "web\explorer-lens.html") -Raw
        $gasFees = Get-Content -LiteralPath (Join-Path $repoRoot "web\gas-fees-simulator-tests.html") -Raw
        $validatorTooling = Get-Content -LiteralPath (Join-Path $repoRoot "web\validator-tooling.html") -Raw
        $contractCatalog = Get-Content -LiteralPath (Join-Path $repoRoot "web\create-intelligent-contracts.html") -Raw
        $validatorFailover = Get-Content -LiteralPath (Join-Path $repoRoot "web\validator-failover.html") -Raw
        $blogPost = Get-Content -LiteralPath (Join-Path $repoRoot "web\blog-signalguard.html") -Raw
        $marketing = Get-Content -LiteralPath (Join-Path $repoRoot "web\marketing-networking.html") -Raw
        $outreach = Get-Content -LiteralPath (Join-Path $repoRoot "web\community-outreach.html") -Raw
        $support = Get-Content -LiteralPath (Join-Path $repoRoot "web\community-support.html") -Raw
        $meta = Get-Content -LiteralPath (Join-Path $repoRoot "web\meta-contributions.html") -Raw
        $bugReport = Get-Content -LiteralPath (Join-Path $repoRoot "web\bug-report.html") -Raw
        $tutorial = Get-Content -LiteralPath (Join-Path $repoRoot "web\tutorial.html") -Raw
        $dashboard = Get-Content -LiteralPath (Join-Path $repoRoot "web\portal-dashboard.html") -Raw
        $research = Get-Content -LiteralPath (Join-Path $repoRoot "web\research-analysis.html") -Raw
        $adversarial = Get-Content -LiteralPath (Join-Path $repoRoot "web\adversarial-testing.html") -Raw
        $benchmarks = Get-Content -LiteralPath (Join-Path $repoRoot "web\benchmarks.html") -Raw
        $toolchain = Get-Content -LiteralPath (Join-Path $repoRoot "web\tools-infrastructure.html") -Raw
        $resourcePack = Get-Content -LiteralPath (Join-Path $repoRoot "web\resource-pack.html") -Raw
        $quickstart = Get-Content -LiteralPath (Join-Path $repoRoot "web\reviewer-quickstart.html") -Raw
        if ($hub -notmatch "GenLayer SignalGuard Evidence Hub" -or $hub -notmatch "Project Overview" -or $hub -notmatch "Milestone 1") {
            throw "index.html does not contain the expected evidence hub markers."
        }
        if ($demo -notmatch "review_claim") {
            throw "web/index.html does not contain review_claim."
        }
        if ($project -notmatch "SignalGuard Project Overview" -or $project -notmatch "Projects") {
            throw "web/project-overview.html does not contain the expected project markers."
        }
        if ($milestone -notmatch "SignalGuard Milestone 1" -or $milestone -notmatch "Milestones") {
            throw "web/milestone-1.html does not contain the expected milestone markers."
        }
        if ($integrations -notmatch "SignalGuard SourceBridge Integrations" -or $integrations -notmatch "3rd party integrations") {
            throw "web/third-party-integrations.html does not contain the expected integration markers."
        }
        if ($grayboxing -notmatch "SignalGuard Graybox Harness" -or $grayboxing -notmatch "Grayboxing") {
            throw "web/grayboxing.html does not contain the expected grayboxing markers."
        }
        if ($explorer -notmatch "SignalGuard Explorer Lens" -or $explorer -notmatch "Explorer") {
            throw "web/explorer-lens.html does not contain the expected explorer markers."
        }
        if ($gasFees -notmatch "SignalGuard Gas Fee Simulator Tests" -or $gasFees -notmatch "Gas Fees Simulator Tests") {
            throw "web/gas-fees-simulator-tests.html does not contain the expected gas-fee markers."
        }
        if ($validatorTooling -notmatch "SignalGuard Validator Ops Probe" -or $validatorTooling -notmatch "Tooling for running a Validator") {
            throw "web/validator-tooling.html does not contain the expected validator tooling markers."
        }
        if ($contractCatalog -notmatch "SignalGuard Intelligent Contract Catalog" -or $contractCatalog -notmatch "Create Intelligent Contracts") {
            throw "web/create-intelligent-contracts.html does not contain the expected contract catalog markers."
        }
        if ($validatorFailover -notmatch "SignalGuard Validator Failover Drill" -or $validatorFailover -notmatch "Validator failover") {
            throw "web/validator-failover.html does not contain the expected failover markers."
        }
        if ($blogPost -notmatch "SignalGuard: A Source-Grounded GenLayer Contract Pattern" -or $blogPost -notmatch "Blog Post") {
            throw "web/blog-signalguard.html does not contain the expected blog markers."
        }
        if ($marketing -notmatch "SignalGuard Builder Networking Kit" -or $marketing -notmatch "Marketing &amp; Networking") {
            throw "web/marketing-networking.html does not contain the expected marketing markers."
        }
        if ($outreach -notmatch "SignalGuard Community Outreach FAQ" -or $outreach -notmatch "Community outreach") {
            throw "web/community-outreach.html does not contain the expected outreach markers."
        }
        if ($support -notmatch "SignalGuard Community Support Triage Guide" -or $support -notmatch "Community Support") {
            throw "web/community-support.html does not contain the expected support markers."
        }
        if ($meta -notmatch "SignalGuard Portal Evidence Workflow Retrospective" -or $meta -notmatch "Meta Contributions") {
            throw "web/meta-contributions.html does not contain the expected meta contribution markers."
        }
        if ($bugReport -notmatch "SignalGuard Portal Deeplink Bug Report" -or $bugReport -notmatch "Bug Report") {
            throw "web/bug-report.html does not contain the expected bug report markers."
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
        if ($adversarial -notmatch "SignalGuard Adversarial Testing" -or $adversarial -notmatch "contradicted-overclaim") {
            throw "web/adversarial-testing.html does not contain the expected adversarial test markers."
        }
        if ($benchmarks -notmatch "SignalGuard Benchmarks" -or $benchmarks -notmatch "Evidence package verifier") {
            throw "web/benchmarks.html does not contain the expected benchmark markers."
        }
        if ($toolchain -notmatch "SignalGuard Builder Evidence and Status Toolchain" -or $toolchain -notmatch "Tools &amp; Infrastructure") {
            throw "web/tools-infrastructure.html does not contain the expected toolchain markers."
        }
        if ($resourcePack -notmatch "SignalGuard Source-Grounded Review Resource Pack" -or $resourcePack -notmatch "Resource Creation") {
            throw "web/resource-pack.html does not contain the expected resource pack markers."
        }
        if ($quickstart -notmatch "SignalGuard Reviewer Quickstart Documentation" -or $quickstart -notmatch "review_claim") {
            throw "web/reviewer-quickstart.html does not contain the expected quickstart markers."
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
