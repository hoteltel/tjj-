$agentMap = @{
    "Clove" = "1f10a0f5-4b0b-4e1a-9e1a-9c5c5c5c5c5c"
    "Brimstone" = "9f0d8ba9-4140-b941-57a3-7eb4f0c8c148"
    "Deadlock" = "cc8b61c5-6b6e-85b6-6c06-0d4e6e6e6e6e"
    "KAY/O" = "601dbbe7-43ce-be57-2a40-4abd24953621"
    "Miks" = "miks-uuid-placeholder"
    "Tejo" = "tejo-uuid-placeholder"
    "Veto" = "veto-uuid-placeholder"
    "Vyse" = "vyse-uuid-placeholder"
    "Waylay" = "waylay-uuid-placeholder"
}

# First, get all agent UUIDs from API
$response = Invoke-WebRequest -Uri "https://valorant-api.com/v1/agents" -UseBasicParsing
$json = $response.Content | ConvertFrom-Json

$uuidMap = @{}
foreach ($agent in $json.data) {
    $uuidMap[$agent.displayName] = $agent.uuid
}

Write-Host "Found $($uuidMap.Count) agents from API"

$missingAgents = @("Clove", "Brimstone", "Deadlock", "KAY/O", "Miks", "Tejo", "Veto", "Vyse", "Waylay")

foreach ($name in $missingAgents) {
    if ($uuidMap.ContainsKey($name)) {
        $uuid = $uuidMap[$name]
        $url = "https://media.valorant-api.com/agents/$uuid/displayicon.png"
        $output = "agents/$name.png"
        Write-Host "Downloading $name..."
        try {
            Invoke-WebRequest -Uri $url -OutFile $output -UseBasicParsing -ErrorAction Stop
            Write-Host "  Success: $name"
        } catch {
            Write-Host "  Failed: $name - $($_.Exception.Message)"
        }
    } else {
        Write-Host "Not found in API: $name"
    }
    Start-Sleep -Milliseconds 200
}

Write-Host "`nDone!"
