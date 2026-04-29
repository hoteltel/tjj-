try {
    $r = Invoke-WebRequest -Uri "https://www.vstats.gg/agents?table=agents" -TimeoutSec 15 -Headers @{"User-Agent"="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    $content = $r.Content
    $scriptMatches = [regex]::Matches($content, 'src="(/_next/static/[^"]+\.js)"')
    foreach ($match in $scriptMatches) {
        Write-Output "Script: $($match.Groups[1].Value)"
    }
    $apiMatches = [regex]::Matches($content, '(api[/a-zA-Z0-9_-]+|fetch\([^)]+\)|axios[^;]+)')
    foreach ($match in $apiMatches) {
        Write-Output "API: $($match.Groups[0].Value)"
    }
    $buildId = [regex]::Match($content, '"buildId":"([^"]+)"')
    if ($buildId.Success) {
        Write-Output "BuildId: $($buildId.Groups[1].Value)"
    }
    $nextData = [regex]::Match($content, '<script id="__NEXT_DATA__"[^>]*>([^<]+)</script>')
    if ($nextData.Success) {
        Write-Output "NextData: $($nextData.Groups[1].Value.Substring(0, [Math]::Min(2000, $nextData.Groups[1].Value.Length)))"
    }
} catch {
    Write-Output "Error: $($_.Exception.Message)"
}
