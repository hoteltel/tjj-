$urls = @(
    "https://www.vstats.gg/api/agents",
    "https://api.vstats.gg/agents",
    "https://www.vstats.gg/_next/data/build-id/agents.json"
)

foreach ($url in $urls) {
    try {
        $r = Invoke-WebRequest -Uri $url -TimeoutSec 10 -Headers @{"User-Agent"="Mozilla/5.0"}
        Write-Output "URL: $url"
        Write-Output "Status: $($r.StatusCode)"
        Write-Output "Content: $($r.Content.Substring(0, [Math]::Min(500, $r.Content.Length)))"
        Write-Output "---"
    } catch {
        Write-Output "URL: $url - Error: $($_.Exception.Message)"
        Write-Output "---"
    }
}
