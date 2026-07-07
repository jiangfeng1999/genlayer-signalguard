param(
    [string]$FixturePath = "examples/dashboard_calculation_fixture.json"
)

$ErrorActionPreference = "Stop"

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = Split-Path -Parent $scriptDir
$fixture = if ([System.IO.Path]::IsPathRooted($FixturePath)) {
    $FixturePath
} else {
    Join-Path $repoRoot $FixturePath
}

if (-not (Test-Path -LiteralPath $fixture)) {
    throw "Missing fixture: $fixture"
}

$data = Get-Content -LiteralPath $fixture -Raw | ConvertFrom-Json
$leader = @($data.leaderboard) | Where-Object { $_.rank -eq 1 } | Select-Object -First 1
if (-not $leader) {
    throw "Fixture does not contain a rank 1 leaderboard row."
}

$points = [int]$data.user.builder_points
$gap = [Math]::Max(0, [int]$leader.total_points + 1 - $points)
if ($gap -ne [int]$data.expected.gap_to_rank_1) {
    throw "Gap calculation mismatch. Expected $($data.expected.gap_to_rank_1), got $gap."
}

$rankedTypes = @($data.contribution_types) |
    Where-Object { $_.is_submittable -eq $true } |
    ForEach-Object {
        [pscustomobject]@{
            name = $_.name
            category = $_.category
            max_display_points = [int]([decimal]$_.max_points * [decimal]$_.current_multiplier)
        }
    } |
    Sort-Object @{Expression = "max_display_points"; Descending = $true}, name

$topType = $rankedTypes | Select-Object -First 1
if ($topType.name -ne $data.expected.top_contribution_type) {
    throw "Top contribution type mismatch. Expected $($data.expected.top_contribution_type), got $($topType.name)."
}

if ($topType.max_display_points -ne [int]$data.expected.top_contribution_type_points) {
    throw "Top contribution type point mismatch. Expected $($data.expected.top_contribution_type_points), got $($topType.max_display_points)."
}

[pscustomobject]@{
    fixture = $fixture
    gap_to_rank_1 = $gap
    top_contribution_type = $topType.name
    top_contribution_type_points = $topType.max_display_points
    checked_types = @($rankedTypes).Count
    status = "pass"
} | ConvertTo-Json -Depth 5
