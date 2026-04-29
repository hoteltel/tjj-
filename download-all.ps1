# 从API获取正确的UUID并下载头像
$response = Invoke-WebRequest -Uri "https://valorant-api.com/v1/agents" -UseBasicParsing
$content = $response.Content
$json = $content | ConvertFrom-Json

$agentMap = @{}
foreach ($agent in $json.data) {
    $agentMap[$agent.displayName] = $agent.uuid
    Write-Host "$($agent.displayName): $($agent.uuid)"
}

# 下载所有头像
$agentNames = @("Clove","Sage","Killjoy","Phoenix","Neon","Sova","Cypher","Viper","Chamber","Iso","Jett","Deadlock","Reyna","Fade","Brimstone","Veto","Vyse","Gekko","Astra","Skye","Miks","Yoru","Tejo","Harbor","Waylay","Raze","Omen","KAY/O","Breach")

foreach ($name in $agentNames) {
    if ($agentMap.ContainsKey($name)) {
        $uuid = $agentMap[$name]
        $url = "https://media.valorant-api.com/agents/$uuid/displayicon.png"
        $output = "agents/$name.png"
        try {
            Invoke-WebRequest -Uri $url -OutFile $output -UseBasicParsing -ErrorAction Stop
            Write-Host "Downloaded $name"
        } catch {
            Write-Host "Failed $name`: $($_.Exception.Message)"
        }
    } else {
        Write-Host "Not found: $name"
    }
    Start-Sleep -Milliseconds 100
}

Write-Host "Done!"
