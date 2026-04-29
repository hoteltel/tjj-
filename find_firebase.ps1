try {
    $r = Invoke-WebRequest -Uri "https://www.vstats.gg/assets/index-VdEKILD-.js" -TimeoutSec 15 -Headers @{"User-Agent"="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    $content = $r.Content
    
    $chunkPattern = [regex]::Matches($content, '"\./([A-Za-z0-9_-]+-[A-Za-z0-9_-]+\.js)"')
    foreach ($m in $chunkPattern) {
        Write-Output "Chunk: $($m.Groups[1].Value)"
    }
    
    $idx = $content.IndexOf("initializeApp")
    if ($idx -ge 0) {
        Write-Output "Found initializeApp at $idx"
        Write-Output $content.Substring([Math]::Max(0, $idx - 100), [Math]::Min(500, $content.Length - [Math]::Max(0, $idx - 100)))
    }
    
    $idx2 = $content.IndexOf("FIREBASE")
    if ($idx2 -ge 0) {
        Write-Output "Found FIREBASE at $idx2"
        Write-Output $content.Substring([Math]::Max(0, $idx2 - 50), [Math]::Min(500, $content.Length - [Math]::Max(0, $idx2 - 50)))
    }
    
    $idx3 = $content.IndexOf("vstats")
    if ($idx3 -ge 0) {
        Write-Output "Found vstats at $idx3"
        Write-Output $content.Substring([Math]::Max(0, $idx3 - 50), [Math]::Min(300, $content.Length - [Math]::Max(0, $idx3 - 50)))
    }
    
    $idx4 = $content.IndexOf("AIzaSy")
    if ($idx4 -ge 0) {
        Write-Output "Found Google API key at $idx4"
        Write-Output $content.Substring($idx4, [Math]::Min(100, $content.Length - $idx4))
    }
    
    $idx5 = $content.IndexOf("vstats-")
    if ($idx5 -ge 0) {
        Write-Output "Found vstats- at $idx5"
        Write-Output $content.Substring([Math]::Max(0, $idx5 - 20), [Math]::Min(200, $content.Length - [Math]::Max(0, $idx5 - 20)))
    }
    
    $idx6 = $content.IndexOf(".firebaseapp.com")
    if ($idx6 -ge 0) {
        Write-Output "Found firebaseapp.com at $idx6"
        Write-Output $content.Substring([Math]::Max(0, $idx6 - 100), [Math]::Min(200, $content.Length - [Math]::Max(0, $idx6 - 100)))
    }
} catch {
    Write-Output "Error: $($_.Exception.Message)"
}
