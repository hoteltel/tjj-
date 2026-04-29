# 下载特工头像
$agents = @(
    @{name="Clove"; id="1f10a0f5-4b0b-4e1a-9e1a-9c5c5c5c5c5c"},
    @{name="Sage"; id="569fdd95-4d10-43ab-ca70-79becc718b46"},
    @{name="Killjoy"; id="1e58de9c-4950-5125-93e9-a0aee9f98746"},
    @{name="Phoenix"; id="eb93336a-449b-9c1b-0a54-a891f7921d69"},
    @{name="Neon"; id="bb2a4828-46eb-8cd1-e765-15848195d751"},
    @{name="Sova"; id="320b2a48-4d9b-a075-30f1-1f93a9b638fa"},
    @{name="Cypher"; id="117ed9e3-49f3-6512-3ccf-0cada7e3823b"},
    @{name="Viper"; id="707eab51-4836-f488-046a-cda6bf494859"},
    @{name="Chamber"; id="22697a3d-45bf-8dd7-4fec-84a9e28c69d7"},
    @{name="Iso"; id="0e38b510-41a8-5780-5e8f-568b2a4f2d6c"},
    @{name="Jett"; id="add6443a-41bd-e414-f6ad-e58d267f4e95"},
    @{name="Deadlock"; id="cc8b64c8-4e3c-4e6e-8e6a-4e8b8c6d8e8f"},
    @{name="Reyna"; id="a3bfb853-43b2-7238-a4f1-ad90e9e46bcc"},
    @{name="Fade"; id="dade69b4-4f5a-8528-247b-219e5a1facd6"},
    @{name="Brimstone"; id="9f0d8ba9-4140-b941-57a3-7eb4f0c8c148"},
    @{name="Veto"; id="5f7d8e9f-6a8c-7d3e-4f5a-6b7c8d9e0f1a"},
    @{name="Vyse"; id="6e8f9a0b-7c9d-8e4f-5a6b-7c8d9e0f1a2b"},
    @{name="Gekko"; id="e370fa57-4757-3604-3648-499e1f642d3f"},
    @{name="Astra"; id="41fb69c1-4189-7b37-f117-bcaf1e96f1bf"},
    @{name="Skye"; id="6f2a04ca-43e0-be17-7f36-b3908627744d"},
    @{name="Miks"; id="7d9e0a1c-8b0f-9c5a-6b7c-8d9e0f1a2b3c"},
    @{name="Yoru"; id="7f94d92c-4234-0a36-9646-3a87eb8b5c89"},
    @{name="Tejo"; id="8c0f1b2d-9a1e-0d6b-7c8d-9e0f1a2b3c4d"},
    @{name="Harbor"; id="95b78ed7-4637-86d9-7e41-71ba8c293152"},
    @{name="Waylay"; id="fc3d8f85-4290-4d19-8b0c-0d14556401c0"},
    @{name="Raze"; id="f94c3b30-42be-e959-889c-5aa313dba261"},
    @{name="Omen"; id="8e253930-4c05-31dd-1b6c-968525494517"},
    @{name="KAY/O"; id="601dbbe7-43ce-be57-2a40-4abd24953621"},
    @{name="Breach"; id="5f8d3a7f-467b-97f3-062c-13acf203c006"}
)

foreach ($agent in $agents) {
    $url = "https://media.valorant-api.com/agents/$($agent.id)/displayicon.png"
    $output = "agents/$($agent.name).png"
    try {
        Invoke-WebRequest -Uri $url -OutFile $output -ErrorAction Stop
        Write-Host "✓ Downloaded $($agent.name)"
    } catch {
        Write-Host "✗ Failed $($agent.name): $($_.Exception.Message)"
    }
    Start-Sleep -Milliseconds 100
}

Write-Host "Done!"
