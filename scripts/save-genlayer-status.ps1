param(
    [string]$OutputDirectory = ".genlayer-status"
)

$ErrorActionPreference = "Stop"

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = Split-Path -Parent $scriptDir
$checkScript = Join-Path $scriptDir "check-genlayer-status.ps1"
$outDir = if ([System.IO.Path]::IsPathRooted($OutputDirectory)) {
    $OutputDirectory
} else {
    Join-Path $repoRoot $OutputDirectory
}

if (-not (Test-Path -LiteralPath $checkScript)) {
    throw "Missing status check script: $checkScript"
}

New-Item -ItemType Directory -Force -Path $outDir | Out-Null

$previous = Get-ChildItem -LiteralPath $outDir -Filter "*.json" -File -ErrorAction SilentlyContinue |
    Sort-Object LastWriteTime -Descending |
    Select-Object -First 1

$statusJson = & $checkScript
$status = $statusJson | ConvertFrom-Json
$stamp = Get-Date -Format "yyyyMMdd-HHmmss"
$snapshotPath = Join-Path $outDir "genlayer-status-$stamp.json"
$statusJson | Set-Content -LiteralPath $snapshotPath -Encoding UTF8

$previousStatus = $null
if ($previous) {
    try {
        $previousStatus = Get-Content -LiteralPath $previous.FullName -Raw | ConvertFrom-Json
    }
    catch {
        $previousStatus = $null
    }
}

$currentPoints = if ($status.user) { [int]$status.user.builder_points } else { $null }
$previousPoints = if ($previousStatus -and $previousStatus.user) { [int]$previousStatus.user.builder_points } else { $null }

[pscustomobject]@{
    snapshot = $snapshotPath
    checked_at = $status.checked_at
    builder_points = $currentPoints
    previous_points = $previousPoints
    points_delta = if ($null -ne $currentPoints -and $null -ne $previousPoints) { $currentPoints - $previousPoints } else { $null }
    builder_gap_to_rank_1 = $status.builder_gap_to_rank_1
    rank_1 = if ($status.rank_1) { $status.rank_1.name } else { $null }
    github_contract_needs_sync = $status.github_contract_needs_sync
    user_error = $status.user_error
    leaderboard_error = $status.leaderboard_error
    github_contract_error = $status.github_contract_error
} | ConvertTo-Json -Depth 5
