try {
    $r = Invoke-WebRequest -Uri "https://www.vstats.gg/assets/index-VdEKILD-.js" -TimeoutSec 15 -Headers @{"User-Agent"="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    $content = $r.Content
    Write-Output "Content length: $($content.Length)"
    $apiPatterns = [regex]::Matches($content, '["'']([a-zA-Z0-9_/]+api[a-zA-Z0-9_/]*)["'']')
    foreach ($match in $apiPatterns) {
        Write-Output "API pattern: $($match.Groups[1].Value)"
    }
    $fetchPatterns = [regex]::Matches($content, 'fetch\(["'']([^"'']+)["'']')
    foreach ($match in $fetchPatterns) {
        Write-Output "Fetch: $($match.Groups[1].Value)"
    }
    $urlPatterns = [regex]::Matches($content, '["'']https?://[^"'']+["'']')
    foreach ($match in $urlPatterns) {
        Write-Output "URL: $($match.Groups[0].Value)"
    }
    $supabasePatterns = [regex]::Matches($content, 'supabase[a-zA-Z0-9_.]*')
    foreach ($match in $supabasePatterns) {
        Write-Output "Supabase: $($match.Groups[0].Value)"
    }
    $firebasePatterns = [regex]::Matches($content, 'firebase[a-zA-Z0-9_.]*')
    foreach ($match in $firebasePatterns) {
        Write-Output "Firebase: $($match.Groups[0].Value)"
    }
} catch {
    Write-Output "Error: $($_.Exception.Message)"
}
