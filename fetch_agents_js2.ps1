try {
    $r = Invoke-WebRequest -Uri "https://www.vstats.gg/assets/AgentsRoot-L6VNZkTH.js" -TimeoutSec 15 -Headers @{"User-Agent"="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    $content = $r.Content
    Write-Output $content
} catch {
    Write-Output "Error: $($_.Exception.Message)"
}
