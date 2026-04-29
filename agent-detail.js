// 特工详情页逻辑

let currentAgent = null;
let currentMap = 'all';
let currentRank = 'all';
let currentMapRank = 'all';
let mapChart = null;
let rankWinRateChart = null;
let mapRankChart = null;

// 特工头像映射 - 使用本地图片
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
    "Vyse": "agents/Vyse.png",
    "Tejo": "agents/Tejo.png",
    "Miks": "agents/Miks.png",
    "Veto": "agents/Veto.png"
};

// 初始化页面
document.addEventListener('DOMContentLoaded', () => {
    const urlParams = new URLSearchParams(window.location.search);
    const agentName = urlParams.get('agent') || 'Clove';
    
    currentAgent = agentDetailedData[agentName];
    if (!currentAgent) {
        currentAgent = agentDetailedData['Clove'];
    }
    
    initPage();
    setupEventListeners();
});

// 初始化页面内容
function initPage() {
    const agentName = Object.keys(agentDetailedData).find(
        key => agentDetailedData[key] === currentAgent
    );
    
    document.title = `${agentName} - 特工详细分析`;
    document.getElementById('agentName').textContent = agentName;
    document.getElementById('agentRole').textContent = `角色: ${roleNames[currentAgent.role]}`;
    
    const avatar = document.getElementById('agentAvatar');
    const agentImage = agentImages[agentName];
    if (agentImage) {
        avatar.innerHTML = `<img src="${agentImage}" alt="${agentName}" onerror="this.style.display='none'; this.parentElement.textContent='${agentName.charAt(0)}'; this.parentElement.style.background='${roleColors[currentAgent.role]}'">`;
        avatar.style.background = 'transparent';
    } else {
        avatar.textContent = agentName.charAt(0);
        avatar.style.background = roleColors[currentAgent.role];
    }
    
    document.getElementById('overallWinRate').textContent = currentAgent.overall.winRate.toFixed(2) + '%';
    document.getElementById('overallPickRate').textContent = currentAgent.overall.pickRate.toFixed(2) + '%';
    document.getElementById('overallKD').textContent = currentAgent.overall.kd.toFixed(2);
    
    const tier = getTier(currentAgent.overall.winRate);
    const tierBadge = document.getElementById('tierBadge');
    tierBadge.textContent = tier.tier + '级';
    tierBadge.className = `value tier-badge ${tier.class}`;
    
    renderMapStats();
    renderSuggestions();
    initMapChart();
    initRankCharts();
    renderMapStatsGrid();
}

function setupEventListeners() {
    document.querySelectorAll('.map-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            document.querySelectorAll('.map-btn').forEach(b => b.classList.remove('active'));
            e.target.classList.add('active');
            currentMap = e.target.dataset.map;
            renderMapStatsGrid();
        });
    });
    
    document.querySelectorAll('.rank-btn').forEach(btn => {
        btn.addEventListener('click', (e) => {
            document.querySelectorAll('.rank-btn').forEach(b => b.classList.remove('active'));
            e.target.classList.add('active');
            currentRank = e.target.dataset.rank;
            updateRankCharts();
        });
    });
    
    document.getElementById('mapRankFilter').addEventListener('change', (e) => {
        currentMapRank = e.target.value;
        renderMapStatsGrid();
    });
}

function renderMapStatsGrid() {
    const grid = document.getElementById('mapStatsGrid');
    grid.innerHTML = '';
    
    let mapsToShow = currentMap === 'all' 
        ? Object.entries(currentAgent.maps)
        : [[currentMap, currentAgent.maps[currentMap]]];
    
    const allWinRates = Object.values(currentAgent.maps).map(m => m.winRate);
    const avgWinRate = allWinRates.reduce((a, b) => a + b, 0) / allWinRates.length;
    
    mapsToShow.forEach(([map, data]) => {
        const card = document.createElement('div');
        let heatClass = 'heat-average';
        
        const displayWinRate = currentMapRank === 'all' 
            ? data.winRate 
            : (data.rankWinRates && data.rankWinRates[currentMapRank] ? data.rankWinRates[currentMapRank] : data.winRate);
        
        if (displayWinRate >= avgWinRate + 2) {
            heatClass = 'heat-excellent';
        } else if (displayWinRate >= avgWinRate) {
            heatClass = 'heat-good';
        } else if (displayWinRate < avgWinRate - 2) {
            heatClass = 'heat-poor';
        }
        
        card.className = `map-stat-card ${heatClass}`;
        
        let rankInfo = '';
        if (currentMapRank !== 'all' && data.rankWinRates) {
            rankInfo = `<div class="sub-value">分段: ${getRankName(currentMapRank)}</div>`;
        }
        
        card.innerHTML = `
            <h4>${mapNames[map]}</h4>
            <div class="value">${displayWinRate.toFixed(1)}%</div>
            <div class="sub-value">选取率: ${data.pickRate.toFixed(1)}%</div>
            ${rankInfo}
        `;
        grid.appendChild(card);
    });
}

function renderSuggestions() {
    const agentName = Object.keys(agentDetailedData).find(
        key => agentDetailedData[key] === currentAgent
    );

    const bestMaps = getBestMaps(currentAgent, 3);
    const bestMapsContainer = document.getElementById('bestMaps');
    bestMapsContainer.innerHTML = bestMaps.map(m => `
        <div class="smart-map-item">
            <span class="map-name">${mapNames[m.map]}</span>
            <span class="win-rate smart-wr-good">${m.winRate.toFixed(1)}%</span>
        </div>
    `).join('');
    
    const avoidMaps = getAvoidMaps(currentAgent, 3);
    const avoidMapsContainer = document.getElementById('avoidMaps');
    avoidMapsContainer.innerHTML = avoidMaps.map(m => `
        <div class="smart-map-item">
            <span class="map-name">${mapNames[m.map]}</span>
            <span class="win-rate smart-wr-bad">${m.winRate.toFixed(1)}%</span>
        </div>
    `).join('');
    
    const rankSuggestion = getRankSuggestion(currentAgent);
    const rankAnalysis = analyzeRankPerformance(currentAgent);
    const rankContainer = document.getElementById('rankSuggestion');
    const rankIconMap = {
        'Silver': 'https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/10/smallicon.png',
        'Gold': 'https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/13/smallicon.png',
        'Platinum': 'https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/16/smallicon.png',
        'Diamond': 'https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/19/smallicon.png',
        'Ascendant': 'https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/22/smallicon.png',
        'Immortal': 'https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/25/smallicon.png',
        'Radiant': 'https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/27/smallicon.png'
    };
    const rankColorMap2 = {
        'Silver': '#94a3b8', 'Gold': '#fbbf24', 'Platinum': '#60a5fa', 'Diamond': '#a78bfa',
        'Ascendant': '#34d399', 'Immortal': '#f87171', 'Radiant': '#fbbf24'
    };
    const bestIcon = rankIconMap[rankSuggestion.best.rank] || '';
    const worstIcon = rankIconMap[rankSuggestion.worst.rank] || '';
    const bestColor = rankColorMap2[rankSuggestion.best.rank] || '#34d399';
    const worstColor = rankColorMap2[rankSuggestion.worst.rank] || '#f87171';
    const bestIconHtml = bestIcon ? `<img class="rank-icon-sm" src="${bestIcon}" alt="" onerror="this.style.display='none'">` : '';
    const worstIconHtml = worstIcon ? `<img class="rank-icon-sm" src="${worstIcon}" alt="" onerror="this.style.display='none'">` : '';
    rankContainer.innerHTML = `
        <div class="smart-rank-row">
            <span class="smart-rank-label">最佳分段</span>
            <span class="smart-rank-value highlight" style="color: ${bestColor}">${bestIconHtml} ${rankNames[rankSuggestion.best.rank]} (${rankSuggestion.best.winRate.toFixed(1)}%)</span>
        </div>
        <div class="smart-rank-row">
            <span class="smart-rank-label">最低分段</span>
            <span class="smart-rank-value warning" style="color: ${worstColor}">${worstIconHtml} ${rankNames[rankSuggestion.worst.rank]} (${rankSuggestion.worst.winRate.toFixed(1)}%)</span>
        </div>
        <div class="smart-rank-row">
            <span class="smart-rank-label">分段差异</span>
            <span class="smart-rank-value" style="color: ${rankSuggestion.trend > 3 ? '#f87171' : rankSuggestion.trend > 1 ? '#fbbf24' : '#34d399'}">${rankSuggestion.trend.toFixed(1)}%</span>
        </div>
        <div class="smart-insight-box">
            <span class="smart-insight-icon">💡</span>
            <span class="smart-insight-text">${rankAnalysis.insight}</span>
        </div>
        <div class="smart-detail-box">${rankAnalysis.detail}</div>
    `;
    
    const playstyleAnalysis = analyzePlaystyle(currentAgent);
    const playstyleContainer = document.getElementById('playstyleSuggestion');
    playstyleContainer.innerHTML = `
        <div class="smart-section-title">🎯 玩法定位</div>
        <p class="smart-text">${currentAgent.analysis.playstyle}</p>
        <div class="smart-section-title">📋 战术策略</div>
        <p class="smart-text">${playstyleAnalysis.strategy}</p>
        <div class="smart-section-title">🔥 进阶技巧</div>
        <ul class="smart-list tips-list">
            ${playstyleAnalysis.tips.map(t => `<li>${t}</li>`).join('')}
        </ul>
    `;

    const strengthsContainer = document.getElementById('strengthsContent');
    strengthsContainer.innerHTML = `
        <ul class="smart-list">
            ${currentAgent.analysis.strengths.map(s => `<li>${s}</li>`).join('')}
        </ul>
    `;

    const weaknessesContainer = document.getElementById('weaknessesContent');
    weaknessesContainer.innerHTML = `
        <ul class="smart-list">
            ${currentAgent.analysis.weaknesses.map(w => `<li>${w}</li>`).join('')}
        </ul>
    `;

    const verdictContainer = document.getElementById('verdictContent');
    const verdict = generateVerdict(currentAgent, agentName);
    verdictContainer.innerHTML = `
        <div class="smart-verdict-grid">
            <div class="smart-verdict-item">
                <div class="smart-verdict-score" style="color: ${verdict.overallColor}">${verdict.overallScore}</div>
                <div class="smart-verdict-label">综合评分</div>
            </div>
            <div class="smart-verdict-item">
                <div class="smart-verdict-score" style="color: ${verdict.mapColor}">${verdict.mapScore}</div>
                <div class="smart-verdict-label">地图适配</div>
            </div>
            <div class="smart-verdict-item">
                <div class="smart-verdict-score" style="color: ${verdict.rankColor}">${verdict.rankScore}</div>
                <div class="smart-verdict-label">分段稳定性</div>
            </div>
            <div class="smart-verdict-item">
                <div class="smart-verdict-score" style="color: ${verdict.pickColor}">${verdict.pickScore}</div>
                <div class="smart-verdict-label">热门程度</div>
            </div>
        </div>
        <div class="smart-verdict-desc">${verdict.summary}</div>
    `;
}

function analyzeRankPerformance(agent) {
    const ranks = Object.entries(agent.ranks);
    const winRates = ranks.map(([_, data]) => data.winRate);
    const avgWinRate = winRates.reduce((a, b) => a + b, 0) / winRates.length;
    const maxWinRate = Math.max(...winRates);
    const minWinRate = Math.min(...winRates);
    const variance = maxWinRate - minWinRate;
    
    let insight = '';
    let detail = '';
    
    if (variance > 5) {
        const highRankBetter = agent.ranks['Radiant'].winRate > agent.ranks['Silver'].winRate;
        if (highRankBetter) {
            insight = '该特工在高分段表现显著更优，技能上限高，需要精准操作和团队配合才能发挥最大价值。';
            detail = `从白银到辐能战魂，胜率提升了${(agent.ranks['Radiant'].winRate - agent.ranks['Silver'].winRate).toFixed(1)}%。这表明该特工的技能机制具有较高的天花板，随着玩家技术水平和团队配合的提升，胜率显著提高。建议在掌握基础操作后，重点练习高级技巧和团队协同。`;
        } else {
            insight = '该特工在低分段表现更好，操作相对简单，适合新手玩家快速上手。';
            detail = '数据显示低分段玩家使用该特工时胜率更高，可能是因为其技能机制直观易懂，不需要复杂的团队配合。但随着分段提升，对手针对能力增强，胜率有所下降。';
        }
    } else if (variance > 2) {
        insight = '该特工在各分段表现相对稳定，但存在一定差异，适合大多数玩家使用。';
        detail = `胜率波动在${variance.toFixed(1)}%范围内，说明该特工的平衡性较好。不同分段玩家都能找到适合自己的玩法，但想要精通仍需要针对性练习。`;
    } else {
        insight = '该特工在各分段表现非常稳定，上手难度适中，是可靠的选角。';
        detail = '极小的胜率波动表明该特工设计平衡，不依赖特定分段的环境。无论是新手还是高手都能稳定发挥其作用，是排位赛中的安全选择。';
    }
    
    return { insight, detail };
}

function analyzePlaystyle(agent) {
    const winRate = agent.overall.winRate;
    const pickRate = agent.overall.pickRate;
    const kd = agent.overall.kd;
    
    let strategy = '';
    let tips = [];
    
    if (agent.role === 'Duelist') {
        if (kd > 1.1) {
            strategy = '作为高K/D决斗者，你的首要任务是创造击杀机会。利用技能优势主动寻找对枪，为团队打开局面。在进攻方要敢于突破，防守方要积极前压获取信息。';
            tips = [
                '利用技能创造1v1优势对枪，避免同时面对多个敌人',
                '进攻时与队友保持同步，确保突破时有补枪支持',
                '学会控制节奏，不要盲目冲锋，等待最佳时机',
                '善用预瞄和身位控制，最大化你的对枪优势'
            ];
        } else {
            strategy = '你的角色更偏向团队型决斗者，注重配合而非个人英雄主义。利用技能为队友创造机会，在关键时刻发挥决定性作用。';
            tips = [
                '与队友技能形成配合，创造多重威胁',
                '学会牺牲个人数据换取团队胜利',
                '把握进点时机，不要过早暴露位置',
                '多利用技能获取信息，减少盲目对枪'
            ];
        }
    } else if (agent.role === 'Controller') {
        strategy = '作为控场者，你是团队战术的核心。合理使用烟雾和区域控制技能，决定团队的进攻节奏和防守布局。';
        tips = [
            '烟雾使用要有目的性，为特定战术服务',
            '学会单向烟和非常规烟雾点位',
            '与队友沟通烟雾时机，避免浪费',
            '保留技能应对关键时刻，不要过早交完'
        ];
    } else if (agent.role === 'Initiator') {
        strategy = '作为先锋，你的任务是为团队获取信息和创造进点条件。合理使用侦查技能和闪光，让队友能够安全地执行战术。';
        tips = [
            '侦查技能要尽量覆盖多个角度',
            '闪光时机要与队友突破同步',
            '学会用技能逼迫敌人暴露位置',
            '保持存活，持续为团队提供信息支持'
        ];
    } else if (agent.role === 'Sentinel') {
        strategy = '作为守卫，你是团队的后盾。合理布置防御设施，保护关键点位，在关键时刻使用技能扭转战局。';
        tips = [
            '防守布置要覆盖关键通道和包点',
            '学会根据敌人习惯调整防守位置',
            '技能使用要精准，不要浪费在无效时刻',
            '保持与队友的信息交流，及时报点'
        ];
    }
    
    if (pickRate > 20) {
        strategy += ' 由于该特工选取率极高，建议练习多个同类型特工，避免被ban或被选时无法发挥。';
        tips.push('准备备选特工，应对被ban或重复选角的情况');
    }
    
    if (winRate > 52) {
        strategy += ' 当前版本该特工强度较高，是上分的好选择。';
    } else if (winRate < 49) {
        strategy += ' 当前版本该特工处于弱势，需要更高熟练度才能发挥作用，建议谨慎选择或等待版本调整。';
    }
    
    return { strategy, tips };
}

function initMapChart() {
    const ctx = document.getElementById('mapWinRateChart').getContext('2d');
    const maps = Object.keys(currentAgent.maps);
    const winRates = maps.map(m => currentAgent.maps[m].winRate);
    const pickRates = maps.map(m => currentAgent.maps[m].pickRate);
    
    const minWR = Math.min(...winRates);
    const maxWR = Math.max(...winRates);
    const yMin = Math.floor(minWR - 2);
    const yMax = Math.ceil(maxWR + 2);
    
    if (mapChart) mapChart.destroy();
    
    mapChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: maps.map(m => mapNames[m]),
            datasets: [
                {
                    label: '胜率 (%)',
                    data: winRates,
                    backgroundColor: winRates.map(wr => {
                        if (wr >= 52) return 'rgba(16, 185, 129, 0.8)';
                        if (wr >= 50) return 'rgba(74, 158, 255, 0.8)';
                        if (wr >= 48) return 'rgba(245, 158, 11, 0.8)';
                        return 'rgba(239, 68, 68, 0.8)';
                    }),
                    borderColor: winRates.map(wr => {
                        if (wr >= 52) return '#10b981';
                        if (wr >= 50) return '#4a9eff';
                        if (wr >= 48) return '#f59e0b';
                        return '#ef4444';
                    }),
                    borderWidth: 2,
                    borderRadius: 6,
                    yAxisID: 'y'
                },
                {
                    label: '选取率 (%)',
                    data: pickRates,
                    backgroundColor: 'rgba(139, 92, 246, 0.6)',
                    borderColor: '#8b5cf6',
                    borderWidth: 2,
                    type: 'line',
                    tension: 0.4,
                    pointBackgroundColor: '#8b5cf6',
                    pointBorderColor: '#fff',
                    pointBorderWidth: 2,
                    pointRadius: 4,
                    yAxisID: 'y1'
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            interaction: {
                mode: 'index',
                intersect: false
            },
            plugins: {
                legend: {
                    labels: { color: '#1a1a1a', font: { size: 11 } }
                },
                tooltip: {
                    backgroundColor: 'rgba(255, 255, 255, 0.95)',
                    titleColor: '#1a1a1a',
                    bodyColor: '#1a1a1a',
                    borderColor: 'rgba(0, 0, 0, 0.1)',
                    borderWidth: 1,
                    padding: 12,
                    cornerRadius: 8
                }
            },
            scales: {
                y: {
                    type: 'linear',
                    display: true,
                    position: 'left',
                    grid: { color: 'rgba(0, 0, 0, 0.05)' },
                    ticks: { 
                        color: 'rgba(0, 0, 0, 0.5)',
                        font: { size: 10 },
                        stepSize: 2
                    },
                    min: yMin,
                    max: yMax
                },
                y1: {
                    type: 'linear',
                    display: true,
                    position: 'right',
                    grid: { drawOnChartArea: false },
                    ticks: { 
                        color: '#8b5cf6',
                        font: { size: 10 }
                    },
                    min: 0
                },
                x: {
                    grid: { display: false },
                    ticks: { 
                        color: 'rgba(0, 0, 0, 0.5)',
                        font: { size: 10 }
                    }
                }
            }
        }
    });
}

function initRankCharts() {
    const ctx = document.getElementById('rankWinRateChart').getContext('2d');
    const rankOrder = ['Silver', 'Gold', 'Platinum', 'Diamond', 'Ascendant', 'Immortal', 'Radiant'];
    const rankLabelMap = {
        'Silver': '白银', 'Gold': '黄金', 'Platinum': '铂金',
        'Diamond': '钻石', 'Ascendant': '超凡', 'Immortal': '神话', 'Radiant': '辐能'
    };
    const rankColorMap = {
        'Silver': '#94a3b8', 'Gold': '#fbbf24', 'Platinum': '#60a5fa',
        'Diamond': '#a78bfa', 'Ascendant': '#34d399', 'Immortal': '#f87171', 'Radiant': '#fbbf24'
    };
    const ranks = rankOrder.filter(r => currentAgent.ranks[r]);
    const labels = ranks.map(r => rankLabelMap[r]);
    const winRates = ranks.map(r => currentAgent.ranks[r].winRate);
    const pointColors = ranks.map(r => rankColorMap[r]);
    
    const minWR = Math.min(...winRates);
    const maxWR = Math.max(...winRates);
    const range = maxWR - minWR;
    const padding = Math.max(range * 0.5, 1);
    const yMin = Math.floor(minWR - padding);
    const yMax = Math.ceil(maxWR + padding);
    
    if (rankWinRateChart) rankWinRateChart.destroy();
    
    rankWinRateChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: '胜率 (%)',
                data: winRates,
                backgroundColor: (context) => {
                    const chart = context.chart;
                    const {ctx: chartCtx, chartArea} = chart;
                    if (!chartArea) return 'rgba(255, 70, 85, 0.1)';
                    const gradient = chartCtx.createLinearGradient(0, chartArea.top, 0, chartArea.bottom);
                    gradient.addColorStop(0, 'rgba(255, 70, 85, 0.3)');
                    gradient.addColorStop(1, 'rgba(255, 70, 85, 0.02)');
                    return gradient;
                },
                borderColor: '#ff4655',
                borderWidth: 3,
                fill: true,
                tension: 0.4,
                pointBackgroundColor: pointColors,
                pointBorderColor: '#fff',
                pointBorderWidth: 3,
                pointRadius: 7,
                pointHoverRadius: 9
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { display: false },
                tooltip: {
                    backgroundColor: 'rgba(255, 255, 255, 0.95)',
                    titleColor: '#1a1a1a',
                    bodyColor: '#1a1a1a',
                    borderColor: 'rgba(0, 0, 0, 0.1)',
                    borderWidth: 1,
                    padding: 12,
                    cornerRadius: 8,
                    callbacks: {
                        label: (context) => `胜率: ${context.parsed.y.toFixed(1)}%`
                    }
                }
            },
            scales: {
                y: {
                    grid: { color: 'rgba(0, 0, 0, 0.05)' },
                    ticks: { 
                        color: 'rgba(0, 0, 0, 0.5)',
                        font: { size: 10 },
                        stepSize: Math.max(1, Math.ceil((yMax - yMin) / 6))
                    },
                    min: yMin,
                    max: yMax
                },
                x: {
                    grid: { display: false },
                    ticks: { 
                        color: 'rgba(0, 0, 0, 0.5)',
                        font: { size: 10 }
                    }
                }
            }
        }
    });
    
    renderRankPerformanceBars();
}

function renderRankPerformanceBars() {
    const ranks = Object.entries(currentAgent.ranks);
    const winRates = ranks.map(([_, data]) => data.winRate);
    const minWR = Math.min(...winRates);
    const maxWR = Math.max(...winRates);
    const range = maxWR - minWR || 1;
    
    const rankNames = {
        'Radiant': '辐能',
        'Immortal': '神话',
        'Ascendant': '超凡',
        'Diamond': '钻石',
        'Platinum': '铂金',
        'Gold': '黄金',
        'Silver': '白银'
    };
    
    const container = document.createElement('div');
    container.className = 'rank-performance-container';
    
    ranks.forEach(([rank, data]) => {
        const normalizedWidth = ((data.winRate - minWR) / range) * 80 + 20;
        let barColor = '#f59e0b';
        if (data.winRate >= 52) barColor = '#10b981';
        else if (data.winRate >= 50) barColor = '#4a9eff';
        else if (data.winRate < 48) barColor = '#ef4444';
        
        const rankColorMap = {
            'Radiant': '#fbbf24',
            'Immortal': '#f87171',
            'Ascendant': '#34d399',
            'Diamond': '#a78bfa',
            'Platinum': '#60a5fa',
            'Gold': '#fbbf24',
            'Silver': '#94a3b8'
        };
        
        const card = document.createElement('div');
        card.className = 'rank-stat-card';
        card.innerHTML = `
            <span class="rank-name" style="color: ${rankColorMap[rank] || '#ccc'}"><img class="rank-icon-img" src="${rankIcons[rank]}" alt="${rank}" onerror="this.style.display='none'">${rankNames[rank]}</span>
            <div class="rank-bar-container">
                <div class="rank-bar-fill" style="width: ${normalizedWidth}%; background: ${barColor}"></div>
            </div>
            <span class="rank-winrate" style="color: ${barColor}">${data.winRate.toFixed(1)}%</span>
            <span class="rank-pickrate">${data.pickRate.toFixed(1)}%</span>
        `;
        container.appendChild(card);
    });
    
    const chartWrapper = document.getElementById('rankWinRateChart').parentElement;
    const existingContainer = chartWrapper.querySelector('.rank-performance-container');
    if (existingContainer) existingContainer.remove();
    chartWrapper.appendChild(container);
    
    initMapRankChart();
}

function initMapRankChart() {
    const ctx = document.getElementById('mapRankChart').getContext('2d');
    const maps = Object.keys(currentAgent.maps);
    const rankNames = ['Radiant', 'Immortal', 'Ascendant', 'Diamond', 'Platinum', 'Gold', 'Silver'];
    const rankLabels = ['辐能', '神话', '超凡', '钻石', '铂金', '黄金', '白银'];
    const rankColors = ['#fbbf24', '#f87171', '#34d399', '#a78bfa', '#60a5fa', '#fbbf24', '#94a3b8'];
    
    if (mapRankChart) mapRankChart.destroy();
    
    const datasets = rankNames.map((rank, idx) => {
        const data = maps.map(map => {
            const mapData = currentAgent.maps[map];
            return mapData.rankWinRates && mapData.rankWinRates[rank] ? mapData.rankWinRates[rank] : null;
        });
        
        return {
            label: rankLabels[idx],
            data: data,
            borderColor: rankColors[idx],
            backgroundColor: rankColors[idx] + '20',
            borderWidth: 2,
            tension: 0.4,
            pointBackgroundColor: rankColors[idx],
            pointBorderColor: '#fff',
            pointBorderWidth: 2,
            pointRadius: 5,
            pointHoverRadius: 7
        };
    });
    
    mapRankChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: maps.map(m => mapNames[m]),
            datasets: datasets
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            interaction: {
                mode: 'index',
                intersect: false
            },
            plugins: {
                legend: {
                    position: 'top',
                    labels: { 
                        color: '#1a1a1a', 
                        font: { size: 11 },
                        usePointStyle: true,
                        pointStyle: 'circle'
                    }
                },
                tooltip: {
                    backgroundColor: 'rgba(255, 255, 255, 0.95)',
                    titleColor: '#1a1a1a',
                    bodyColor: '#1a1a1a',
                    borderColor: 'rgba(0, 0, 0, 0.1)',
                    borderWidth: 1,
                    padding: 12,
                    cornerRadius: 8,
                    callbacks: {
                        label: (context) => `${context.dataset.label}: ${context.parsed.y.toFixed(1)}%`
                    }
                }
            },
            scales: {
                y: {
                    grid: { color: 'rgba(0, 0, 0, 0.05)' },
                    ticks: { 
                        color: 'rgba(0, 0, 0, 0.5)',
                        font: { size: 10 },
                        callback: (value) => value.toFixed(1) + '%'
                    },
                    title: {
                        display: true,
                        text: '胜率 (%)',
                        color: 'rgba(0, 0, 0, 0.6)',
                        font: { size: 12 }
                    }
                },
                x: {
                    grid: { display: false },
                    ticks: { 
                        color: 'rgba(0, 0, 0, 0.5)',
                        font: { size: 10 }
                    }
                }
            }
        }
    });
}

function updateRankCharts() {
}

function getRankName(rank) {
    const rankNames = {
        'Radiant': '辐能',
        'Immortal': '神话',
        'Ascendant': '超凡',
        'Diamond': '钻石',
        'Platinum': '铂金',
        'Gold': '黄金',
        'Silver': '白银'
    };
    return rankNames[rank] || rank;
}

function generateVerdict(agent, agentName) {
    const wr = agent.overall.winRate;
    const pr = agent.overall.pickRate;
    const rankSuggestion = getRankSuggestion(agent);
    const bestMaps = getBestMaps(agent, 3);
    const worstMaps = getAvoidMaps(agent, 3);

    let overallScore, overallColor;
    if (wr >= 53) { overallScore = 'S'; overallColor = '#ffd700'; }
    else if (wr >= 51) { overallScore = 'A'; overallColor = '#34d399'; }
    else if (wr >= 49) { overallScore = 'B'; overallColor = '#60a5fa'; }
    else { overallScore = 'C'; overallColor = '#9ca3af'; }

    const mapVariance = bestMaps[0].winRate - worstMaps[0].winRate;
    let mapScore, mapColor;
    if (mapVariance <= 2) { mapScore = 'S'; mapColor = '#ffd700'; }
    else if (mapVariance <= 4) { mapScore = 'A'; mapColor = '#34d399'; }
    else if (mapVariance <= 6) { mapScore = 'B'; mapColor = '#60a5fa'; }
    else { mapScore = 'C'; mapColor = '#9ca3af'; }

    const rankVariance = rankSuggestion.trend;
    let rankScore, rankColor;
    if (rankVariance <= 2) { rankScore = 'S'; rankColor = '#ffd700'; }
    else if (rankVariance <= 5) { rankScore = 'A'; rankColor = '#34d399'; }
    else if (rankVariance <= 8) { rankScore = 'B'; rankColor = '#60a5fa'; }
    else { rankScore = 'C'; rankColor = '#9ca3af'; }

    let pickScore, pickColor;
    if (pr >= 20) { pickScore = 'S'; pickColor = '#ffd700'; }
    else if (pr >= 10) { pickScore = 'A'; pickColor = '#34d399'; }
    else if (pr >= 5) { pickScore = 'B'; pickColor = '#60a5fa'; }
    else { pickScore = 'C'; pickColor = '#9ca3af'; }

    const roleLabel = roleNames[agent.role];
    let summary = '';
    if (overallScore === 'S') {
        summary = `${agentName} 是当前版本强势${roleLabel}，总体胜率 ${wr.toFixed(1)}% 表现优异。`;
    } else if (overallScore === 'A') {
        summary = `${agentName} 作为${roleLabel}表现良好，胜率 ${wr.toFixed(1)}% 处于健康水平。`;
    } else if (overallScore === 'B') {
        summary = `${agentName} 作为${roleLabel}表现中规中矩，胜率 ${wr.toFixed(1)}% 需要一定熟练度才能发挥。`;
    } else {
        summary = `${agentName} 当前版本处于弱势，胜率 ${wr.toFixed(1)}% 偏低，建议谨慎选择。`;
    }

    summary += ` 最佳地图为${mapNames[bestMaps[0].map]}（${bestMaps[0].winRate.toFixed(1)}%），`;
    const bestRankIconUrl = rankIcons[rankSuggestion.best.rank] || '';
    const bestRankIconHtml = bestRankIconUrl ? `<img class="rank-icon-sm" src="${bestRankIconUrl}" alt="" onerror="this.style.display='none'">` : '';
    summary += `在${bestRankIconHtml} ${rankNames[rankSuggestion.best.rank]}分段表现最佳（${rankSuggestion.best.winRate.toFixed(1)}%）。`;

    if (rankVariance > 5) {
        summary += `注意：该特工分段差异较大（${rankVariance.toFixed(1)}%），在不同分段的表现差异明显，建议根据自身分段谨慎选择。`;
    } else {
        summary += `该特工在各分段表现稳定，是可靠的选择。`;
    }

    return { overallScore, overallColor, mapScore, mapColor, rankScore, rankColor, pickScore, pickColor, summary };
}

function getTier(winRate) {
    if (winRate >= 52) return { tier: 'S', class: 'tier-s' };
    if (winRate >= 50) return { tier: 'A', class: 'tier-a' };
    if (winRate >= 48) return { tier: 'B', class: 'tier-b' };
    return { tier: 'C', class: 'tier-c' };
}

function getBestMaps(agent, count) {
    return Object.entries(agent.maps)
        .map(([map, data]) => ({ map, winRate: data.winRate }))
        .sort((a, b) => b.winRate - a.winRate)
        .slice(0, count);
}

function getAvoidMaps(agent, count) {
    return Object.entries(agent.maps)
        .map(([map, data]) => ({ map, winRate: data.winRate }))
        .sort((a, b) => a.winRate - b.winRate)
        .slice(0, count);
}

function getRankSuggestion(agent) {
    const ranks = Object.entries(agent.ranks);
    const best = ranks.reduce((max, [rank, data]) => 
        data.winRate > max.winRate ? { rank, winRate: data.winRate } : max,
        { rank: ranks[0][0], winRate: ranks[0][1].winRate }
    );
    const worst = ranks.reduce((min, [rank, data]) => 
        data.winRate < min.winRate ? { rank, winRate: data.winRate } : min,
        { rank: ranks[0][0], winRate: ranks[0][1].winRate }
    );
    return { best, worst, trend: best.winRate - worst.winRate };
}

function renderMapStats() {
}
