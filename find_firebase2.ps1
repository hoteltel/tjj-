$chunks = @(
    "AgentsRoot-L6VNZkTH.js",
    "vendor-vue-BzpaXZV6.js",
    "vendor-vuetify-BnhdhtYA.js"
)

foreach ($chunk in $chunks) {
    try {
        $url = "https://www.vstats.gg/assets/$chunk"
        $r = Invoke-WebRequest -Uri $url -TimeoutSec 15 -Headers @{"User-Agent"="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
        $content = $r.Content
        Write-Output "=== $chunk (length: $($content.Length)) ==="
        
        $patterns = @("AIzaSy", "firebaseapp.com", "firebaseio.com", "initializeApp", "getFirestore", "getDocs", "collection(", "query(", "where(", "onSnapshot", "FIREBASE", "projectId", "vstats-", "apiKey:")
        foreach ($p in $patterns) {
            $idx = $content.IndexOf($p)
            if ($idx -ge 0) {
                Write-Output "  Found '$p' at $idx"
                $start = [Math]::Max(0, $idx - 50)
                $len = [Math]::Min(200, $content.Length - $start)
                Write-Output "  Context: $($content.Substring($start, $len))"
            }
        }
    } catch {
        Write-Output "Error fetching $chunk : $($_.Exception.Message)"
    }
}
