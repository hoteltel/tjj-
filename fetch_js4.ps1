try {
    $r = Invoke-WebRequest -Uri "https://www.vstats.gg/assets/index-VdEKILD-.js" -TimeoutSec 15 -Headers @{"User-Agent"="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    $content = $r.Content
    $idx = $content.IndexOf("supabase")
    if ($idx -ge 0) {
        Write-Output "Found 'supabase' at index $idx"
        Write-Output $content.Substring([Math]::Max(0, $idx - 50), [Math]::Min(200, $content.Length - [Math]::Max(0, $idx - 50)))
    } else {
        Write-Output "'supabase' not found"
    }
    $idx2 = $content.IndexOf("createClient")
    if ($idx2 -ge 0) {
        Write-Output "Found 'createClient' at index $idx2"
        Write-Output $content.Substring([Math]::Max(0, $idx2 - 50), [Math]::Min(200, $content.Length - [Math]::Max(0, $idx2 - 50)))
    } else {
        Write-Output "'createClient' not found"
    }
    $idx3 = $content.IndexOf("agents")
    if ($idx3 -ge 0) {
        Write-Output "First 'agents' at index $idx3"
        Write-Output $content.Substring([Math]::Max(0, $idx3 - 30), [Math]::Min(200, $content.Length - [Math]::Max(0, $idx3 - 30)))
    } else {
        Write-Output "'agents' not found"
    }
    $idx4 = $content.IndexOf("getAgent")
    if ($idx4 -ge 0) {
        Write-Output "Found 'getAgent' at index $idx4"
        Write-Output $content.Substring([Math]::Max(0, $idx4 - 50), [Math]::Min(200, $content.Length - [Math]::Max(0, $idx4 - 50)))
    } else {
        Write-Output "'getAgent' not found"
    }
    $idx5 = $content.IndexOf("fetchData")
    if ($idx5 -ge 0) {
        Write-Output "Found 'fetchData' at index $idx5"
        Write-Output $content.Substring([Math]::Max(0, $idx5 - 50), [Math]::Min(200, $content.Length - [Math]::Max(0, $idx5 - 50)))
    } else {
        Write-Output "'fetchData' not found"
    }
    $idx6 = $content.IndexOf("loadData")
    if ($idx6 -ge 0) {
        Write-Output "Found 'loadData' at index $idx6"
        Write-Output $content.Substring([Math]::Max(0, $idx6 - 50), [Math]::Min(200, $content.Length - [Math]::Max(0, $idx6 - 50)))
    } else {
        Write-Output "'loadData' not found"
    }
} catch {
    Write-Output "Error: $($_.Exception.Message)"
}
