try {
    $r = Invoke-WebRequest -Uri "https://www.vstats.gg/assets/index-VdEKILD-.js" -TimeoutSec 15 -Headers @{"User-Agent"="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    $content = $r.Content
    $sbMatch = [regex]::Match($content, 'supabase[a-zA-Z0-9_./:-]*')
    if ($sbMatch.Success) { Write-Output "Supabase: $($sbMatch.Groups[0].Value)" }
    
    $sbUrl = [regex]::Match($content, 'https://[a-z0-9]+\.supabase\.co')
    if ($sbUrl.Success) { Write-Output "Supabase URL: $($sbUrl.Groups[0].Value)" }
    
    $fromMatches = [regex]::Matches($content, '\.from\("([^"]+)"\)')
    foreach ($m in $fromMatches) { Write-Output "From table: $($m.Groups[1].Value)" }
    
    $rpcMatches = [regex]::Matches($content, '\.rpc\("([^"]+)"')
    foreach ($m in $rpcMatches) { Write-Output "RPC: $($m.Groups[1].Value)" }
    
    $keyMatch = [regex]::Match($content, 'eyJ[a-zA-Z0-9_-]{20,}')
    if ($keyMatch.Success) { Write-Output "Key: $($keyMatch.Groups[0].Value.Substring(0, 30))..." }
    
    $envMatches = [regex]::Matches($content, 'VITE_[A-Z_]+')
    foreach ($m in $envMatches) { Write-Output "Env: $($m.Groups[0].Value)" }
} catch {
    Write-Output "Error: $($_.Exception.Message)"
}

try {
    $r2 = Invoke-WebRequest -Uri "https://www.vstats.gg/assets/vendor-vue-BzpaXZV6.js" -TimeoutSec 15 -Headers @{"User-Agent"="Mozilla/5.0"}
    $content2 = $r2.Content
    $sbUrl2 = [regex]::Match($content2, 'https://[a-z0-9]+\.supabase\.co')
    if ($sbUrl2.Success) { Write-Output "Supabase URL (vendor): $($sbUrl2.Groups[0].Value)" }
    $keyMatch2 = [regex]::Match($content2, 'eyJ[a-zA-Z0-9_-]{20,}')
    if ($keyMatch2.Success) { Write-Output "Key (vendor): $($keyMatch2.Groups[0].Value.Substring(0, 30))..." }
} catch {
    Write-Output "Error vendor: $($_.Exception.Message)"
}
