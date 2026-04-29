try {
    $r = Invoke-WebRequest -Uri "https://www.vstats.gg/assets/index-VdEKILD-.js" -TimeoutSec 15 -Headers @{"User-Agent"="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    $content = $r.Content
    
    $idx = $content.IndexOf("TABLE_AGENTS")
    if ($idx -ge 0) {
        Write-Output "TABLE_AGENTS context:"
        Write-Output $content.Substring([Math]::Max(0, $idx - 100), [Math]::Min(500, $content.Length - [Math]::Max(0, $idx - 100)))
    }
    
    $idx2 = $content.IndexOf(".from(")
    if ($idx2 -ge 0) {
        Write-Output "First .from( context:"
        Write-Output $content.Substring([Math]::Max(0, $idx2 - 50), [Math]::Min(300, $content.Length - [Math]::Max(0, $idx2 - 50)))
    } else {
        Write-Output "'.from(' not found"
    }
    
    $idx3 = $content.IndexOf("axios")
    if ($idx3 -ge 0) {
        Write-Output "First axios context:"
        Write-Output $content.Substring([Math]::Max(0, $idx3 - 50), [Math]::Min(300, $content.Length - [Math]::Max(0, $idx3 - 50)))
    } else {
        Write-Output "'axios' not found"
    }
    
    $idx4 = $content.IndexOf("import(")
    if ($idx4 -ge 0) {
        Write-Output "First import( context:"
        Write-Output $content.Substring([Math]::Max(0, $idx4 - 50), [Math]::Min(300, $content.Length - [Math]::Max(0, $idx4 - 50)))
    } else {
        Write-Output "'import(' not found"
    }
    
    $idx5 = $content.IndexOf("database")
    if ($idx5 -ge 0) {
        Write-Output "First database context:"
        Write-Output $content.Substring([Math]::Max(0, $idx5 - 50), [Math]::Min(300, $content.Length - [Math]::Max(0, $idx5 - 50)))
    } else {
        Write-Output "'database' not found"
    }
    
    $idx6 = $content.IndexOf("firebase")
    if ($idx6 -ge 0) {
        Write-Output "First firebase context:"
        Write-Output $content.Substring([Math]::Max(0, $idx6 - 50), [Math]::Min(300, $content.Length - [Math]::Max(0, $idx6 - 50)))
    } else {
        Write-Output "'firebase' not found"
    }
    
    $idx7 = $content.IndexOf("firestore")
    if ($idx7 -ge 0) {
        Write-Output "First firestore context:"
        Write-Output $content.Substring([Math]::Max(0, $idx7 - 50), [Math]::Min(300, $content.Length - [Math]::Max(0, $idx7 - 50)))
    } else {
        Write-Output "'firestore' not found"
    }
    
    $idx8 = $content.IndexOf("onSnapshot")
    if ($idx8 -ge 0) {
        Write-Output "First onSnapshot context:"
        Write-Output $content.Substring([Math]::Max(0, $idx8 - 50), [Math]::Min(300, $content.Length - [Math]::Max(0, $idx8 - 50)))
    } else {
        Write-Output "'onSnapshot' not found"
    }
    
    $idx9 = $content.IndexOf("collection(")
    if ($idx9 -ge 0) {
        Write-Output "First collection( context:"
        Write-Output $content.Substring([Math]::Max(0, $idx9 - 50), [Math]::Min(300, $content.Length - [Math]::Max(0, $idx9 - 50)))
    } else {
        Write-Output "'collection(' not found"
    }
    
    $idx10 = $content.IndexOf("getDocs")
    if ($idx10 -ge 0) {
        Write-Output "First getDocs context:"
        Write-Output $content.Substring([Math]::Max(0, $idx10 - 50), [Math]::Min(300, $content.Length - [Math]::Max(0, $idx10 - 50)))
    } else {
        Write-Output "'getDocs' not found"
    }
} catch {
    Write-Output "Error: $($_.Exception.Message)"
}
