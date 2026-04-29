try {
    $r = Invoke-WebRequest -Uri "https://www.vstats.gg/assets/index-VdEKILD-.js" -TimeoutSec 15 -Headers @{"User-Agent"="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    $content = $r.Content
    $patterns = @(
        'supabase',
        'firebase',
        'firestore',
        '\.from\(',
        '\.select\(',
        'getAgent',
        'getMap',
        'fetchAgent',
        'agentData',
        'winRate',
        'pickRate',
        'agentsTable',
        '/api/',
        'rpc/',
        'rest/',
        'graphql'
    )
    foreach ($pattern in $patterns) {
        $matches = [regex]::Matches($content, "[$pattern[^;]{0,100}")
        foreach ($match in $matches) {
            Write-Output "Pattern '$pattern': $($match.Groups[0].Value)"
        }
    }
} catch {
    Write-Output "Error: $($_.Exception.Message)"
}
