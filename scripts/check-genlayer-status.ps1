param(
    [string]$Wallet = "0x554406e72a76a7b90f1d2857187669af42f65b59",
    [string]$Repository = "jiangfeng1999/genlayer-signalguard"
)

$ErrorActionPreference = "Stop"
$ProgressPreference = "SilentlyContinue"

function Invoke-JsonGet {
    param(
        [Parameter(Mandatory = $true)][string]$Uri,
        [hashtable]$Headers = @{}
    )

    try {
        return @{
            ok = $true
            data = Invoke-RestMethod -Uri $Uri -Headers $Headers -TimeoutSec 20
            error = $null
        }
    }
    catch {
        return @{
            ok = $false
            data = $null
            error = $_.Exception.Message
        }
    }
}

$portalBase = "https://portal-admin.genlayer.foundation/api/v1"
$githubHeaders = @{ "User-Agent" = "Codex-GenLayer-Status" }

$userResult = Invoke-JsonGet "$portalBase/users/by-address/$Wallet/"
$leaderboardResult = Invoke-JsonGet "$portalBase/leaderboard/?type=builder&page_size=10"
$typesResult = Invoke-JsonGet "$portalBase/contribution-types/?page_size=1000"
$contractResult = Invoke-JsonGet "https://api.github.com/repos/$Repository/contents/contracts/signal_guard.py?ref=main" $githubHeaders
$mainCommitResult = Invoke-JsonGet "https://api.github.com/repos/$Repository/commits/main" $githubHeaders

$userSummary = $null
if ($userResult.ok) {
    $u = $userResult.data
    $userSummary = [pscustomobject]@{
        name = $u.name
        address = $u.address
        github = $u.github_username
        builder_points = $u.builder.total_points
        builder_rank = $u.builder.rank
        builder_contributions = $u.builder.total_contributions
        validator = ($null -ne $u.validator)
        creator = ($null -ne $u.creator)
        twitter_connected = ($null -ne $u.twitter_connection)
        discord_connected = ($null -ne $u.discord_connection)
    }
}

$leaderboardTop = @()
$leaderboardLeader = $null
if ($leaderboardResult.ok) {
    $leaderboardTop = @($leaderboardResult.data) |
        Select-Object -First 10 |
        Select-Object rank,total_points,@{n="name";e={$_.user_details.name}},@{n="address";e={$_.user_details.address}},updated_at
    $leaderboardLeader = @($leaderboardResult.data) | Where-Object { $_.rank -eq 1 } | Select-Object -First 1
}

$bestTypes = @()
if ($typesResult.ok) {
    $bestTypes = @($typesResult.data.results) |
        Where-Object { $_.is_submittable -eq $true } |
        Select-Object id,name,slug,category,min_points,max_points,current_multiplier,@{n="max_display_points";e={[math]::Round($_.max_points * $_.current_multiplier, 2)}},submission_count,is_full |
        Sort-Object @{Expression="max_display_points";Descending=$true},category,name |
        Select-Object -First 12
}

$contractEvidence = $null
if ($contractResult.ok) {
    $text = [Text.Encoding]::UTF8.GetString([Convert]::FromBase64String(($contractResult.data.content -replace "\s", "")))
    $contractEvidence = [pscustomobject]@{
        sha = $contractResult.data.sha
        has_fixed_dependency_hash = ($text -match "jqmwsfhh")
        has_old_bad_dependency_hash = ($text -match "jqmw5fhh")
        has_review_count = ($text -match "review_count")
    }
}

[pscustomobject]@{
    checked_at = (Get-Date -Format o)
    wallet = $Wallet
    user = $userSummary
    builder_gap_to_rank_1 = if ($userSummary -and $leaderboardLeader) {
        [math]::Max(0, [int]$leaderboardLeader.total_points + 1 - [int]$userSummary.builder_points)
    } else { $null }
    rank_1 = if ($leaderboardLeader) {
        [pscustomobject]@{
            name = $leaderboardLeader.user_details.name
            points = $leaderboardLeader.total_points
            address = $leaderboardLeader.user_details.address
            updated_at = $leaderboardLeader.updated_at
        }
    } else { $null }
    user_error = $userResult.error
    builder_leaderboard_top = $leaderboardTop
    leaderboard_error = $leaderboardResult.error
    top_submittable_contribution_types = $bestTypes
    contribution_types_error = $typesResult.error
    github_main = if ($mainCommitResult.ok) {
        [pscustomobject]@{
            sha = $mainCommitResult.data.sha
            message = $mainCommitResult.data.commit.message
            date = $mainCommitResult.data.commit.author.date
        }
    } else { $null }
    github_main_error = $mainCommitResult.error
    github_contract_evidence = $contractEvidence
    github_contract_needs_sync = if ($contractEvidence) {
        $contractEvidence.has_old_bad_dependency_hash -or -not $contractEvidence.has_fixed_dependency_hash
    } else { $null }
    github_contract_error = $contractResult.error
} | ConvertTo-Json -Depth 8
