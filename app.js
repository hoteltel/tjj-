// VALORANT 特工数据 - 更新至 Season 26 Act 2 (2026/4/25)
// 数据来源: vstats.gg + tracker.gg 交叉验证
const agentsData = [
    { name: "Clove", role: "Controller", winRate: 53.11, pickRate: 26.36, kd: 0.94, image: "agents/Clove.png" },
    { name: "Sage", role: "Sentinel", winRate: 51.43, pickRate: 32.01, kd: 0.91, image: "agents/Sage.png" },
    { name: "Killjoy", role: "Sentinel", winRate: 51.27, pickRate: 12.53, kd: 1.00, image: "agents/Killjoy.png" },
    { name: "Phoenix", role: "Duelist", winRate: 50.90, pickRate: 19.48, kd: 1.07, image: "agents/Phoenix.png" },
    { name: "Brimstone", role: "Controller", winRate: 50.72, pickRate: 11.00, kd: 0.97, image: "agents/Brimstone.png" },
    { name: "Gekko", role: "Initiator", winRate: 50.62, pickRate: 14.00, kd: 0.89, image: "agents/Gekko.png" },
    { name: "Fade", role: "Initiator", winRate: 50.52, pickRate: 18.50, kd: 0.93, image: "agents/Fade.png" },
    { name: "Raze", role: "Duelist", winRate: 50.52, pickRate: 21.00, kd: 1.03, image: "agents/Raze.png" },
    { name: "Sova", role: "Initiator", winRate: 50.42, pickRate: 19.00, kd: 0.98, image: "agents/Sova.png" },
    { name: "Cypher", role: "Sentinel", winRate: 50.22, pickRate: 15.00, kd: 1.00, image: "agents/Cypher.png" },
    { name: "Neon", role: "Duelist", winRate: 50.02, pickRate: 26.50, kd: 0.98, image: "agents/Neon.png" },
    { name: "Vyse", role: "Sentinel", winRate: 50.02, pickRate: 3.50, kd: 1.01, image: "agents/Vyse.png" },
    { name: "Deadlock", role: "Sentinel", winRate: 50.02, pickRate: 9.00, kd: 0.96, image: "agents/Deadlock.png" },
    { name: "Jett", role: "Duelist", winRate: 50.02, pickRate: 43.00, kd: 1.08, image: "agents/Jett.png" },
    { name: "Reyna", role: "Duelist", winRate: 49.92, pickRate: 45.00, kd: 1.08, image: "agents/Reyna.png" },
    { name: "Skye", role: "Initiator", winRate: 49.82, pickRate: 17.50, kd: 0.93, image: "agents/Skye.png" },
    { name: "Chamber", role: "Sentinel", winRate: 49.62, pickRate: 41.00, kd: 1.11, image: "agents/Chamber.png" },
    { name: "Viper", role: "Controller", winRate: 49.62, pickRate: 5.50, kd: 1.01, image: "agents/Viper.png" },
    { name: "Tejo", role: "Initiator", winRate: 49.42, pickRate: 9.00, kd: 0.94, image: "agents/Tejo.png" },
    { name: "Miks", role: "Controller", winRate: 49.12, pickRate: 40.50, kd: 0.94, image: "agents/Miks.png" },
    { name: "Veto", role: "Sentinel", winRate: 49.02, pickRate: 3.00, kd: 1.02, image: "agents/Veto.png" },
    { name: "Breach", role: "Initiator", winRate: 49.02, pickRate: 10.00, kd: 0.93, image: "agents/Breach.png" },
    { name: "Astra", role: "Controller", winRate: 48.72, pickRate: 4.50, kd: 1.03, image: "agents/Astra.png" },
    { name: "Waylay", role: "Duelist", winRate: 48.42, pickRate: 10.00, kd: 1.00, image: "agents/Waylay.png" },
    { name: "Iso", role: "Duelist", winRate: 48.32, pickRate: 10.00, kd: 1.01, image: "agents/Iso.png" },
    { name: "Omen", role: "Controller", winRate: 47.82, pickRate: 19.50, kd: 0.98, image: "agents/Omen.png" },
    { name: "Harbor", role: "Controller", winRate: 47.02, pickRate: 2.50, kd: 0.93, image: "agents/Harbor.png" },
    { name: "KAY/O", role: "Initiator", winRate: 47.02, pickRate: 8.00, kd: 0.90, image: "agents/KAY-O.png" },
    { name: "Yoru", role: "Duelist", winRate: 46.93, pickRate: 4.50, kd: 0.97, image: "agents/Yoru.png" }
];

const roleColors = {
    "Duelist": "#ff4655",
    "Initiator": "#00d4aa",
    "Controller": "#8b5cf6",
    "Sentinel": "#10b981"
};

const roleNames = {
    "Duelist": "决斗者",
    "Initiator": "先锋",
    "Controller": "控场者",
    "Sentinel": "守卫"
};

// 特工头像映射
const agentImages = {
    "Clove": "agents/Clove.png",
    "Sage": "agents/Sage.png",
    "Phoenix": "agents/Phoenix.png",
    "Omen": "agents/Omen.png",
    "Cypher": "agents/Cypher.png",
    "Sova": "agents/Sova.png",
    "Brimstone": "agents/Brimstone.png",
    "Viper": "agents/Viper.png",
    "Killjoy": "agents/Killjoy.png",
    "Breach": "agents/Breach.png",
    "Jett": "agents/Jett.png",
    "Reyna": "agents/Reyna.png",
    "Raze": "agents/Raze.png",
    "Skye": "agents/Skye.png",
    "Fade": "agents/Fade.png",
    "Gekko": "agents/Gekko.png",
    "Neon": "agents/Neon.png",
    "Chamber": "agents/Chamber.png",
    "Harbor": "agents/Harbor.png",
    "Astra": "agents/Astra.png",
    "KAY/O": "agents/KAY-O.png",
    "Yoru": "agents/Yoru.png",
    "Iso": "agents/Iso.png",
    "Waylay": "agents/Waylay.png",
    "Deadlock": "agents/Deadlock.png",
    "Veto": "agents/Veto.png",
    "Vyse": "agents/Vyse.png",
    "Miks": "agents/Miks.png",
    "Tejo": "agents/Tejo.png"
};

let currentData = [...agentsData];

function init() {
    updateStats();
    renderTable(currentData);
    renderTopAgents();
    setupEventListeners();
}

function updateStats() {
    const sortedByWinRate = [...currentData].sort((a, b) => b.winRate - a.winRate);
    const sortedByPickRate = [...currentData].sort((a, b) => b.pickRate - a.pickRate);
    
    const highestWinRate = sortedByWinRate[0];
    const highestPickRate = sortedByPickRate[0];
    
    document.getElementById('highestWinRate').textContent = highestWinRate.winRate.toFixed(1) + '%';
    document.getElementById('highestWinRateAgent').textContent = highestWinRate.name;
    setAvatar('highestWinRateAvatar', highestWinRate.name, highestWinRate.role);
    
    document.getElementById('highestPickRate').textContent = highestPickRate.pickRate.toFixed(1) + '%';
    document.getElementById('highestPickRateAgent').textContent = highestPickRate.name;
    setAvatar('highestPickRateAvatar', highestPickRate.name, highestPickRate.role);
    
    renderTopPickAgents();
    renderMapPool();
}

function setAvatar(elementId, agentName, role) {
    const container = document.getElementById(elementId);
    const agentImage = agentImages[agentName];
    if (agentImage) {
        container.innerHTML = `<img src="${agentImage}" alt="${agentName}" onerror="this.style.display='none'; this.parentElement.textContent='${agentName.charAt(0)}'; this.parentElement.style.background='${roleColors[role]}'">`;
    } else {
        container.textContent = agentName.charAt(0);
        container.style.background = roleColors[role];
    }
}

function renderTopPickAgents() {
    const top5 = [...currentData].sort((a, b) => b.pickRate - a.pickRate).slice(0, 5);
    
    const container = document.getElementById('topPickAgentsList');
    container.innerHTML = top5.map((agent, index) => {
        const agentImage = agentImages[agent.name] || '';
        return `
        <div class="top-pick-item" onclick="window.location.href='agent-detail.html?agent=${agent.name}'">
            <span class="top-pick-rank">${index + 1}</span>
            <div class="top-pick-icon" style="background: ${roleColors[agent.role]}">
                ${agentImage ? `<img src="${agentImage}" alt="${agent.name}" onerror="this.style.display='none'; this.parentElement.textContent='${agent.name.charAt(0)}'">` : agent.name.charAt(0)}
            </div>
            <div class="top-pick-info">
                <div class="top-pick-name">${agent.name}</div>
                <div class="top-pick-role">${roleNames[agent.role]}</div>
            </div>
            <span class="top-pick-rate">${agent.pickRate.toFixed(1)}%</span>
        </div>
    `}).join('');
}

function renderMapPool() {
    const maps = [
        { name: 'Ascent', cn: '亚海悬城', icon: '🏔️' },
        { name: 'Bind', cn: '源工重镇', icon: '🏜️' },
        { name: 'Haven', cn: '隐世修所', icon: '🏛️' },
        { name: 'Split', cn: '霓虹町', icon: '🏯' },
        { name: 'Lotus', cn: '莲华古城', icon: '🌸' },
        { name: 'Sunset', cn: '日落之城', icon: '🌅' },
        { name: 'Icebox', cn: '森寒冬港', icon: '❄️' }
    ];
    
    const container = document.getElementById('mapPool');
    container.innerHTML = maps.map(map => `
        <div class="map-item">
            <div class="map-info">
                <span class="map-icon">${map.icon}</span>
                <span class="map-name">${map.cn}</span>
            </div>
            <span class="map-code">${map.name}</span>
        </div>
    `).join('');
}

function renderTable(data) {
    const tbody = document.getElementById('agentsTableBody');
    tbody.innerHTML = '';
    
    data.forEach((agent, index) => {
        const row = document.createElement('tr');
        const winRateClass = agent.winRate >= 51 ? 'win-rate-high' : agent.winRate >= 49 ? 'win-rate-mid' : 'win-rate-low';
        const agentImage = agentImages[agent.name] || '';
        
        row.innerHTML = `
            <td>${index + 1}</td>
            <td>
                <div class="agent-cell">
                    <div class="agent-icon" style="background: ${roleColors[agent.role]}">
                        ${agentImage ? `<img src="${agentImage}" alt="${agent.name}" onerror="this.style.display='none'; this.parentElement.textContent='${agent.name.charAt(0)}'">` : agent.name.charAt(0)}
                    </div>
                    <div class="agent-info">
                        <span class="agent-name">${agent.name}</span>
                        <span class="agent-role">${roleNames[agent.role]}</span>
                    </div>
                </div>
            </td>
            <td><span class="role-badge">${roleNames[agent.role]}</span></td>
            <td class="win-rate ${winRateClass}">${agent.winRate.toFixed(1)}%</td>
            <td>
                <div class="pick-rate-bar">
                    <div class="pick-bar">
                        <div class="pick-bar-fill" style="width: ${Math.min(agent.pickRate * 2, 100)}%"></div>
                    </div>
                    <span class="pick-rate-value">${agent.pickRate.toFixed(1)}%</span>
                </div>
            </td>
            <td class="kd-value">${agent.kd.toFixed(2)}</td>
        `;
        
        row.style.cursor = 'pointer';
        row.addEventListener('click', () => {
            window.location.href = `agent-detail.html?agent=${agent.name}`;
        });
        
        tbody.appendChild(row);
    });
}

function renderTopAgents() {
    const top5 = [...currentData].sort((a, b) => b.winRate - a.winRate).slice(0, 5);
    
    const container = document.getElementById('topAgentsList');
    container.innerHTML = top5.map((agent, index) => {
        const agentImage = agentImages[agent.name] || '';
        return `
        <div class="top-agent-item" onclick="window.location.href='agent-detail.html?agent=${agent.name}'">
            <span class="top-rank">${index + 1}</span>
            <div class="top-agent-icon" style="background: ${roleColors[agent.role]}">
                ${agentImage ? `<img src="${agentImage}" alt="${agent.name}" onerror="this.style.display='none'; this.parentElement.textContent='${agent.name.charAt(0)}'">` : agent.name.charAt(0)}
            </div>
            <div class="top-agent-info">
                <div class="top-agent-name">${agent.name}</div>
                <div class="top-agent-role">${roleNames[agent.role]}</div>
            </div>
            <span class="top-agent-winrate">${agent.winRate.toFixed(1)}%</span>
        </div>
    `}).join('');
}

function setupEventListeners() {
    document.getElementById('roleFilter').addEventListener('change', filterData);
    document.getElementById('sortBy').addEventListener('change', filterData);
}

function filterData() {
    const role = document.getElementById('roleFilter').value;
    const sortBy = document.getElementById('sortBy').value;
    
    let filtered = [...agentsData];
    
    if (role !== 'all') {
        filtered = filtered.filter(agent => agent.role === role);
    }
    
    filtered.sort((a, b) => {
        switch(sortBy) {
            case 'winRate': return b.winRate - a.winRate;
            case 'pickRate': return b.pickRate - a.pickRate;
            case 'kd': return b.kd - a.kd;
            default: return b.winRate - a.winRate;
        }
    });
    
    currentData = filtered;
    updateStats();
    renderTable(currentData);
    renderTopAgents();
}

document.addEventListener('DOMContentLoaded', init);
