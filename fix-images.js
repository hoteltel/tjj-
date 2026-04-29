// 从本地agents.json读取正确的UUID并下载头像
const fs = require('fs');
const https = require('https');
const path = require('path');

const rawData = fs.readFileSync('agents.json');
const json = JSON.parse(rawData);

const agentMap = {};
json.data.forEach(agent => {
    agentMap[agent.displayName] = agent.uuid;
    console.log(`${agent.displayName}: ${agent.uuid}`);
});

const agentNames = ["Clove","Sage","Killjoy","Phoenix","Neon","Sova","Cypher","Viper","Chamber","Iso","Jett","Deadlock","Reyna","Fade","Brimstone","Veto","Vyse","Gekko","Astra","Skye","Miks","Yoru","Tejo","Harbor","Waylay","Raze","Omen","KAY/O","Breach"];

function downloadImage(name, uuid) {
    const url = `https://media.valorant-api.com/agents/${uuid}/displayicon.png`;
    const output = path.join('agents', `${name}.png`);
    
    const file = fs.createWriteStream(output);
    https.get(url, (response) => {
        if (response.statusCode === 200) {
            response.pipe(file);
            file.on('finish', () => {
                file.close();
                console.log(`Downloaded: ${name}`);
            });
        } else {
            console.log(`Failed: ${name} (HTTP ${response.statusCode})`);
            file.close();
            fs.unlinkSync(output);
        }
    }).on('error', (err) => {
        console.log(`Error: ${name} - ${err.message}`);
        fs.unlinkSync(output);
    });
}

agentNames.forEach((name, index) => {
    if (agentMap[name]) {
        setTimeout(() => downloadImage(name, agentMap[name]), index * 200);
    } else {
        console.log(`Not found: ${name}`);
    }
});
