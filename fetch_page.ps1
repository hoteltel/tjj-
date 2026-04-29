try {
    $r = Invoke-WebRequest -Uri "https://www.vstats.gg/agents?table=agents" -TimeoutSec 15 -Headers @{"User-Agent"="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    $content = $r.Content
    Write-Output "Content length: $($content.Length)"
    Write-Output "First 3000 chars:"
    Write-Output $content.Substring(0, [Math]::Min(3000, $content.Length))
} catch {
    Write-Output "Error: $($_.Exception.Message)"
}
