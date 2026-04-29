# 下载缺失的特工头像
$agents = @(
    @{name="Clove"; id="1f10a0f5-4b0b-4e1a-9e1a-9c5c5c5c5c5c"}
    @{name="Deadlock"; id="cc8b64c8-4e3c-4e6e-8e6a-4e8b8c6d8e8f"}
    @{name="Brimstone"; id="9f0d8ba9-4140-b941-57a3-7eb4f0c8c148"}
    @{name="Veto"; id="5f7d8e9f-6a8c-7d3e-4f5a-6b7c8d9e0f1a"}
    @{name="Vyse"; id="6e8f9a0b-7c9d-8e4f-5a6b-7c8d9e0f1a2b"}
    @{name="Miks"; id="7d9e0a1c-8b0f-9c5a-6b7c-8d9e0f1a2b3c"}
    @{name="Tejo"; id="8c0f1b2d-9a1e-0d6b-7c8d-9e0f1a2b3c4d"}
    @{name="Waylay"; id="fc3d8f85-4290-4d19-8b0c-0d14556401c0"}
    @{name="KAY-O"; id="601dbbe7-43ce-be57-2a40-4abd24953621"}
)

foreach ($agent in $agents) {
    $url = "https://media.valorant-api.com/agents/$($agent.id)/displayicon.png"
    $output = "agents/$($agent.name).png"
    try {
        Invoke-WebRequest -Uri $url -OutFile $output -ErrorAction Stop
        Write-Host "Downloaded $($agent.name)"
    } catch {
        Write-Host "Failed $($agent.name): $($_.Exception.Message)"
    }
    Start-Sleep -Milliseconds 100
}

Write-Host "Done!"
