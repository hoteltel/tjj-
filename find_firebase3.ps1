try {
    $r = Invoke-WebRequest -Uri "https://www.vstats.gg/assets/index-VdEKILD-.js" -TimeoutSec 15 -Headers @{"User-Agent"="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    $content = $r.Content
    
    $patterns = @("AIzaSy", "firebaseapp", "firebaseio", "initializeApp", "getFirestore", "getDocs", "collection(", "projectId", "apiKey:", "authDomain", "storageBucket", "messagingSenderId", "appId:", "measurementId", "vstats-", "FIREBASE_", "firebaseConfig")
    foreach ($p in $patterns) {
        $idx = $content.IndexOf($p)
        if ($idx -ge 0) {
            Write-Output "Found '$p' at $idx"
            $start = [Math]::Max(0, $idx - 80)
            $len = [Math]::Min(300, $content.Length - $start)
            Write-Output "Context: $($content.Substring($start, $len))"
            Write-Output "---"
        }
    }
    
    $keyMatches = [regex]::Matches($content, 'AIzaSy[A-Za-z0-9_-]{30,}')
    foreach ($m in $keyMatches) {
        Write-Output "Google API Key: $($m.Groups[0].Value)"
    }
    
    $projectMatches = [regex]::Matches($content, '[a-z0-9-]+\.firebaseapp\.com')
    foreach ($m in $projectMatches) {
        Write-Output "Firebase App: $($m.Groups[0].Value)"
    }
    
    $firestoreMatches = [regex]::Matches($content, '[a-z0-9-]+\.firebasedatabase\.app')
    foreach ($m in $firestoreMatches) {
        Write-Output "Firebase DB: $($m.Groups[0].Value)"
    }
    
    $idx2 = $content.IndexOf("ACT_ID")
    if ($idx2 -ge 0) {
        Write-Output "ACT_ID at $idx2"
        Write-Output $content.Substring([Math]::Max(0, $idx2 - 20), [Math]::Min(200, $content.Length - [Math]::Max(0, $idx2 - 20)))
    }
} catch {
    Write-Output "Error: $($_.Exception.Message)"
}
