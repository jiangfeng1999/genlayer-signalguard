param(
    [string]$Claim = "GenLayer Intelligent Contracts can reason over natural language and connect to internet data.",
    [string]$SourceUrl = "https://docs.genlayer.com/"
)

$ErrorActionPreference = "Stop"

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$repoRoot = Split-Path -Parent $scriptDir
$cli = Join-Path $repoRoot "app\signalguard_cli.py"

if (-not (Test-Path -LiteralPath $cli)) {
    throw "Missing CLI helper: $cli"
}

$payloadJson = python $cli --claim $Claim --source-url $SourceUrl
$payload = $payloadJson | ConvertFrom-Json

if ($payload.method -ne "review_claim") {
    throw "Unexpected method. Expected review_claim, got $($payload.method)."
}

if ($payload.args.claim -ne $Claim) {
    throw "Claim mismatch in generated payload."
}

if ($payload.args.source_url -ne $SourceUrl) {
    throw "Source URL mismatch in generated payload."
}

[pscustomobject]@{
    cli = $cli
    method = $payload.method
    claim_length = $Claim.Length
    source_url = $payload.args.source_url
    status = "pass"
} | ConvertTo-Json -Depth 4
