try {
    $r = Invoke-WebRequest -Uri "https://www.vstats.gg/assets/AgentsRoot-L6VNZkTH.js" -TimeoutSec 15 -Headers @{"User-Agent"="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    $content = $r.Content
    Write-Output "Content length: $($content.Length)"
    
    $patterns = @("supabase", "firebase", "firestore", "createClient", ".from(", ".select(", "getDocs", "collection(", "onSnapshot", "apiKey", "projectId", "authDomain", "storageBucket", "messagingSenderId", "appId")
    foreach ($p in $patterns) {
        $idx = $content.IndexOf($p)
        if ($idx -ge 0) {
            Write-Output "Found '$p' at index $idx"
            Write-Output $content.Substring([Math]::Max(0, $idx - 50), [Math]::Min(300, $content.Length - [Math]::Max(0, $idx - 50)))
        }
    }
    
    $firebaseConfig = [regex]::Match($content, 'apiKey:\s*"([^"]+)"')
    if ($firebaseConfig.Success) { Write-Output "Firebase API Key: $($firebaseConfig.Groups[1].Value)" }
    
    $projectId = [regex]::Match($content, 'projectId:\s*"([^"]+)"')
    if ($projectId.Success) { Write-Output "Project ID: $($projectId.Groups[1].Value)" }
    
    $sbUrl = [regex]::Match($content, 'https://[a-z0-9]+\.supabase\.co')
    if ($sbUrl.Success) { Write-Output "Supabase URL: $($sbUrl.Groups[0].Value)" }
    
    $sbKey = [regex]::Match($content, 'eyJ[a-zA-Z0-9_-]{20,}')
    if ($sbKey.Success) { Write-Output "Supabase/Token key: $($sbKey.Groups[0].Value.Substring(0, 40))..." }
} catch {
    Write-Output "Error: $($_.Exception.Message)"
}
