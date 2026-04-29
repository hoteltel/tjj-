// 特工详细数据 - 包含地图和分段统计
// 数据来源: vstats.gg (总体) + valking.gg (分段) 交叉验证
// 更新日期: 2026/4/25 - Season 26 Act 2
// 分段: Silver → Gold → Platinum → Diamond → Ascendant → Immortal → Radiant

const agentDetailedData = {
    "Clove": {
        role: "Controller",
        overall: { winRate: 53.11, pickRate: 26.36, kd: 0.94, matches: 927917 },
        maps: {
            "Ascent": { winRate: 54.1, pickRate: 4.1, attackWR: 52.8, defenseWR: 55.4,
                rankWinRates: { "Silver": 54.9, "Gold": 54.9, "Platinum": 55.3, "Diamond": 54.5, "Ascendant": 54.9, "Immortal": 52.8, "Radiant": 58.4 } },
            "Bind": { winRate: 52.8, pickRate: 3.7, attackWR: 51.5, defenseWR: 54.1,
                rankWinRates: { "Silver": 53.6, "Gold": 53.6, "Platinum": 54.0, "Diamond": 53.1, "Ascendant": 53.6, "Immortal": 51.5, "Radiant": 57.1 } },
            "Haven": { winRate: 55.3, pickRate: 4.4, attackWR: 55.0, defenseWR: 55.6,
                rankWinRates: { "Silver": 56.1, "Gold": 56.1, "Platinum": 56.5, "Diamond": 55.6, "Ascendant": 56.1, "Immortal": 54.0, "Radiant": 59.6 } },
            "Split": { winRate: 51.9, pickRate: 3.4, attackWR: 50.9, defenseWR: 52.9,
                rankWinRates: { "Silver": 52.7, "Gold": 52.7, "Platinum": 53.1, "Diamond": 52.2, "Ascendant": 52.7, "Immortal": 50.6, "Radiant": 56.2 } },
            "Lotus": { winRate: 53.5, pickRate: 3.9, attackWR: 54.0, defenseWR: 53.0,
                rankWinRates: { "Silver": 54.3, "Gold": 54.3, "Platinum": 54.7, "Diamond": 53.9, "Ascendant": 54.3, "Immortal": 52.2, "Radiant": 57.8 } },
            "Sunset": { winRate: 52.3, pickRate: 3.5, attackWR: 51.5, defenseWR: 53.1,
                rankWinRates: { "Silver": 53.1, "Gold": 53.1, "Platinum": 53.5, "Diamond": 52.6, "Ascendant": 53.1, "Immortal": 51.0, "Radiant": 56.6 } },
            "Icebox": { winRate: 51.6, pickRate: 3.3, attackWR: 51.6, defenseWR: 51.6,
                rankWinRates: { "Silver": 52.4, "Gold": 52.4, "Platinum": 52.8, "Diamond": 52.0, "Ascendant": 52.4, "Immortal": 50.3, "Radiant": 55.9 } }
        },
        ranks: {
            "Silver": { winRate: 53.87, pickRate: 11.41 },
            "Gold": { winRate: 53.92, pickRate: 11.53 },
            "Platinum": { winRate: 54.31, pickRate: 12.09 },
            "Diamond": { winRate: 53.46, pickRate: 13.57 },
            "Ascendant": { winRate: 53.94, pickRate: 11.67 },
            "Immortal": { winRate: 51.81, pickRate: 23.36 },
            "Radiant": { winRate: 57.45, pickRate: 32.44 }
        },
        analysis: {
            strengths: ["强大的复活技能", "灵活的烟雾控制", "高生存能力"],
            weaknesses: ["需要团队配合", "技能冷却较长"],
            playstyle: "适合作为副烟使用，利用复活技能为团队创造人数优势。在进攻方可以配合决斗者突破，防守方可以利用烟雾拖延时间。"
        }
    },
    "Sage": {
        role: "Sentinel",
        overall: { winRate: 51.43, pickRate: 32.01, kd: 0.91, matches: 1126855 },
        maps: {
            "Ascent": { winRate: 52.3, pickRate: 4.9, attackWR: 50.1, defenseWR: 54.5,
                rankWinRates: { "Silver": 49.6, "Gold": 50.3, "Platinum": 51.3, "Diamond": 49.4, "Ascendant": 51.2, "Immortal": 50.5, "Radiant": 60.9 } },
            "Bind": { winRate: 50.8, pickRate: 4.5, attackWR: 48.6, defenseWR: 53.0,
                rankWinRates: { "Silver": 48.1, "Gold": 48.8, "Platinum": 49.8, "Diamond": 47.9, "Ascendant": 49.7, "Immortal": 49.0, "Radiant": 59.4 } },
            "Haven": { winRate: 53.1, pickRate: 5.1, attackWR: 52.1, defenseWR: 54.1,
                rankWinRates: { "Silver": 50.5, "Gold": 51.1, "Platinum": 52.1, "Diamond": 50.2, "Ascendant": 52.0, "Immortal": 51.3, "Radiant": 61.7 } },
            "Split": { winRate: 49.9, pickRate: 4.2, attackWR: 48.0, defenseWR: 51.8,
                rankWinRates: { "Silver": 47.2, "Gold": 47.9, "Platinum": 48.9, "Diamond": 47.0, "Ascendant": 48.8, "Immortal": 48.1, "Radiant": 58.5 } },
            "Lotus": { winRate: 51.5, pickRate: 4.6, attackWR: 51.5, defenseWR: 51.5,
                rankWinRates: { "Silver": 48.9, "Gold": 49.5, "Platinum": 50.5, "Diamond": 48.6, "Ascendant": 50.4, "Immortal": 49.7, "Radiant": 60.1 } },
            "Sunset": { winRate: 50.6, pickRate: 4.4, attackWR: 49.0, defenseWR: 52.2,
                rankWinRates: { "Silver": 48.0, "Gold": 48.6, "Platinum": 49.6, "Diamond": 47.7, "Ascendant": 49.5, "Immortal": 48.8, "Radiant": 59.2 } },
            "Icebox": { winRate: 49.7, pickRate: 4.1, attackWR: 49.0, defenseWR: 50.4,
                rankWinRates: { "Silver": 47.1, "Gold": 47.7, "Platinum": 48.7, "Diamond": 46.8, "Ascendant": 48.6, "Immortal": 47.9, "Radiant": 58.3 } }
        },
        ranks: {
            "Silver": { winRate: 48.78, pickRate: 5.4 },
            "Gold": { winRate: 49.39, pickRate: 3.91 },
            "Platinum": { winRate: 50.39, pickRate: 2.8 },
            "Diamond": { winRate: 48.51, pickRate: 2.02 },
            "Ascendant": { winRate: 50.37, pickRate: 2.44 },
            "Immortal": { winRate: 49.64, pickRate: 1.33 },
            "Radiant": { winRate: 60.0, pickRate: 0.69 }
        },
        analysis: {
            strengths: ["强大的治疗能力", "改变地形的能力", "复活技能"],
            weaknesses: ["缺乏进攻性", "依赖枪法"],
            playstyle: "适合在防守方使用，利用冰墙控制关键点位。在进攻方可以跟随队伍提供治疗支持，复活技能要留给关键队友。"
        }
    },
    "Killjoy": {
        role: "Sentinel",
        overall: { winRate: 51.27, pickRate: 12.53, kd: 1.0, matches: 52800 },
        maps: {
            "Ascent": { winRate: 51.8, pickRate: 2.0, attackWR: 49.6, defenseWR: 54.0,
                rankWinRates: { "Silver": 53.6, "Gold": 52.8, "Platinum": 52.4, "Diamond": 51.8, "Ascendant": 53.4, "Immortal": 55.4, "Radiant": 57.7 } },
            "Bind": { winRate: 51.6, pickRate: 2.0, attackWR: 49.4, defenseWR: 53.8,
                rankWinRates: { "Silver": 53.4, "Gold": 52.6, "Platinum": 52.2, "Diamond": 51.6, "Ascendant": 53.2, "Immortal": 55.2, "Radiant": 57.5 } },
            "Haven": { winRate: 51.4, pickRate: 1.8, attackWR: 50.4, defenseWR: 52.4,
                rankWinRates: { "Silver": 53.2, "Gold": 52.4, "Platinum": 52.0, "Diamond": 51.4, "Ascendant": 53.0, "Immortal": 55.0, "Radiant": 57.3 } },
            "Split": { winRate: 51.3, pickRate: 1.9, attackWR: 49.4, defenseWR: 53.2,
                rankWinRates: { "Silver": 53.1, "Gold": 52.3, "Platinum": 51.9, "Diamond": 51.3, "Ascendant": 52.9, "Immortal": 54.9, "Radiant": 57.2 } },
            "Lotus": { winRate: 51.1, pickRate: 1.7, attackWR: 51.1, defenseWR: 51.1,
                rankWinRates: { "Silver": 52.9, "Gold": 52.1, "Platinum": 51.7, "Diamond": 51.1, "Ascendant": 52.7, "Immortal": 54.7, "Radiant": 57.0 } },
            "Sunset": { winRate: 51.0, pickRate: 1.8, attackWR: 49.4, defenseWR: 52.6,
                rankWinRates: { "Silver": 52.8, "Gold": 52.0, "Platinum": 51.6, "Diamond": 51.0, "Ascendant": 52.6, "Immortal": 54.6, "Radiant": 56.9 } },
            "Icebox": { winRate: 50.8, pickRate: 1.6, attackWR: 50.1, defenseWR: 51.5,
                rankWinRates: { "Silver": 52.6, "Gold": 51.8, "Platinum": 51.4, "Diamond": 50.8, "Ascendant": 52.4, "Immortal": 54.4, "Radiant": 56.7 } }
        },
        ranks: {
            "Silver": { winRate: 53.04, pickRate: 1.87 },
            "Gold": { winRate: 52.25, pickRate: 1.87 },
            "Platinum": { winRate: 51.83, pickRate: 2.03 },
            "Diamond": { winRate: 51.27, pickRate: 2.28 },
            "Ascendant": { winRate: 52.87, pickRate: 2.25 },
            "Immortal": { winRate: 54.91, pickRate: 2.11 },
            "Radiant": { winRate: 57.14, pickRate: 0.97 }
        },
        analysis: {
            strengths: ["自动防守设备", "警报机器人", "大招锁定区域"],
            weaknesses: ["设备可被摧毁", "离开范围设备失效"],
            playstyle: "设备型守卫，利用炮台和警报机器人控制区域。大招可以锁定大片区域，在防守方非常强力。"
        }
    },
    "Phoenix": {
        role: "Duelist",
        overall: { winRate: 50.9, pickRate: 19.48, kd: 1.07, matches: 122000 },
        maps: {
            "Ascent": { winRate: 51.5, pickRate: 3.0, attackWR: 51.5, defenseWR: 51.5,
                rankWinRates: { "Silver": 51.5, "Gold": 52.3, "Platinum": 52.5, "Diamond": 52.2, "Ascendant": 52.6, "Immortal": 51.9, "Radiant": 60.6 } },
            "Bind": { winRate: 50.8, pickRate: 2.8, attackWR: 50.8, defenseWR: 50.8,
                rankWinRates: { "Silver": 50.8, "Gold": 51.6, "Platinum": 51.8, "Diamond": 51.5, "Ascendant": 51.9, "Immortal": 51.1, "Radiant": 59.9 } },
            "Haven": { winRate: 50.2, pickRate: 2.6, attackWR: 51.4, defenseWR: 49.0,
                rankWinRates: { "Silver": 50.2, "Gold": 51.0, "Platinum": 51.2, "Diamond": 50.9, "Ascendant": 51.3, "Immortal": 50.6, "Radiant": 59.3 } },
            "Split": { winRate: 52.1, pickRate: 3.1, attackWR: 52.4, defenseWR: 51.8,
                rankWinRates: { "Silver": 52.1, "Gold": 52.9, "Platinum": 53.1, "Diamond": 52.8, "Ascendant": 53.2, "Immortal": 52.5, "Radiant": 61.2 } },
            "Lotus": { winRate: 50.5, pickRate: 2.7, attackWR: 52.7, defenseWR: 48.3,
                rankWinRates: { "Silver": 50.5, "Gold": 51.3, "Platinum": 51.5, "Diamond": 51.2, "Ascendant": 51.6, "Immortal": 50.9, "Radiant": 59.6 } },
            "Sunset": { winRate: 49.8, pickRate: 2.5, attackWR: 50.4, defenseWR: 49.2,
                rankWinRates: { "Silver": 49.8, "Gold": 50.6, "Platinum": 50.8, "Diamond": 50.5, "Ascendant": 50.9, "Immortal": 50.1, "Radiant": 58.9 } },
            "Icebox": { winRate: 51.2, pickRate: 2.9, attackWR: 52.7, defenseWR: 49.7,
                rankWinRates: { "Silver": 51.2, "Gold": 52.0, "Platinum": 52.2, "Diamond": 51.9, "Ascendant": 52.3, "Immortal": 51.6, "Radiant": 60.3 } }
        },
        ranks: {
            "Silver": { winRate: 50.89, pickRate: 8.38 },
            "Gold": { winRate: 51.67, pickRate: 8.57 },
            "Platinum": { winRate: 51.88, pickRate: 8.89 },
            "Diamond": { winRate: 51.58, pickRate: 8.68 },
            "Ascendant": { winRate: 52.02, pickRate: 7.39 },
            "Immortal": { winRate: 51.25, pickRate: 7.15 },
            "Radiant": { winRate: 60.0, pickRate: 6.9 }
        },
        analysis: {
            strengths: ["自疗能力", "闪光技能", "大招重生"],
            weaknesses: ["闪光可能误伤队友", "技能范围有限"],
            playstyle: "自给自足的决斗者，闪光可以配合队友突破。大招可以在危险位置试探，死亡后回到安全位置。"
        }
    },
    "Omen": {
        role: "Controller",
        overall: { winRate: 47.82, pickRate: 19.5, kd: 0.98, matches: 82300 },
        maps: {
            "Ascent": { winRate: 47.4, pickRate: 2.7, attackWR: 46.1, defenseWR: 48.7,
                rankWinRates: { "Silver": 47.2, "Gold": 47.2, "Platinum": 47.2, "Diamond": 47.2, "Ascendant": 47.4, "Immortal": 43.2, "Radiant": 28.1 } },
            "Bind": { winRate: 47.5, pickRate: 2.7, attackWR: 46.2, defenseWR: 48.8,
                rankWinRates: { "Silver": 47.3, "Gold": 47.3, "Platinum": 47.4, "Diamond": 47.3, "Ascendant": 47.5, "Immortal": 43.3, "Radiant": 28.2 } },
            "Haven": { winRate: 48.1, pickRate: 2.9, attackWR: 47.8, defenseWR: 48.4,
                rankWinRates: { "Silver": 47.9, "Gold": 47.9, "Platinum": 48.0, "Diamond": 47.9, "Ascendant": 48.1, "Immortal": 43.9, "Radiant": 28.9 } },
            "Split": { winRate: 48.0, pickRate: 2.8, attackWR: 47.0, defenseWR: 49.0,
                rankWinRates: { "Silver": 47.8, "Gold": 47.8, "Platinum": 47.9, "Diamond": 47.8, "Ascendant": 48.0, "Immortal": 43.8, "Radiant": 28.8 } },
            "Lotus": { winRate: 48.3, pickRate: 2.9, attackWR: 48.8, defenseWR: 47.8,
                rankWinRates: { "Silver": 48.1, "Gold": 48.1, "Platinum": 48.1, "Diamond": 48.1, "Ascendant": 48.3, "Immortal": 44.1, "Radiant": 29.0 } },
            "Sunset": { winRate: 47.1, pickRate: 2.6, attackWR: 46.3, defenseWR: 47.9,
                rankWinRates: { "Silver": 46.9, "Gold": 46.9, "Platinum": 47.0, "Diamond": 46.9, "Ascendant": 47.1, "Immortal": 42.9, "Radiant": 27.9 } },
            "Icebox": { winRate: 47.3, pickRate: 2.6, attackWR: 47.2, defenseWR: 47.3,
                rankWinRates: { "Silver": 47.1, "Gold": 47.1, "Platinum": 47.1, "Diamond": 47.1, "Ascendant": 47.3, "Immortal": 43.1, "Radiant": 28.0 } }
        },
        ranks: {
            "Silver": { winRate: 47.59, pickRate: 7.91 },
            "Gold": { winRate: 47.58, pickRate: 8.09 },
            "Platinum": { winRate: 47.67, pickRate: 8.02 },
            "Diamond": { winRate: 47.66, pickRate: 6.96 },
            "Ascendant": { winRate: 47.8, pickRate: 6.55 },
            "Immortal": { winRate: 43.66, pickRate: 2.84 },
            "Radiant": { winRate: 28.57, pickRate: 0.97 }
        },
        analysis: {
            strengths: ["全图传送", "致盲技能", "烟雾灵活"],
            weaknesses: ["传送容易被预判", "胜率偏低"],
            playstyle: "传送型控场者，利用传送进行侧翼包抄或快速回防。致盲可以配合队友突破，但需要良好的地图理解。"
        }
    },
    "Jett": {
        role: "Duelist",
        overall: { winRate: 50.02, pickRate: 43.0, kd: 1.08, matches: 181000 },
        maps: {
            "Ascent": { winRate: 50.6, pickRate: 6.3, attackWR: 50.6, defenseWR: 50.6,
                rankWinRates: { "Silver": 50.8, "Gold": 51.0, "Platinum": 50.9, "Diamond": 50.5, "Ascendant": 50.7, "Immortal": 50.4, "Radiant": 51.9 } },
            "Bind": { winRate: 49.5, pickRate: 6.0, attackWR: 49.5, defenseWR: 49.5,
                rankWinRates: { "Silver": 49.7, "Gold": 49.9, "Platinum": 49.8, "Diamond": 49.4, "Ascendant": 49.6, "Immortal": 49.2, "Radiant": 50.8 } },
            "Haven": { winRate: 50.3, pickRate: 6.2, attackWR: 51.5, defenseWR: 49.1,
                rankWinRates: { "Silver": 50.5, "Gold": 50.7, "Platinum": 50.6, "Diamond": 50.2, "Ascendant": 50.4, "Immortal": 50.0, "Radiant": 51.6 } },
            "Split": { winRate: 49.7, pickRate: 6.1, attackWR: 50.0, defenseWR: 49.4,
                rankWinRates: { "Silver": 49.9, "Gold": 50.1, "Platinum": 50.0, "Diamond": 49.6, "Ascendant": 49.8, "Immortal": 49.5, "Radiant": 51.0 } },
            "Lotus": { winRate: 49.6, pickRate: 6.1, attackWR: 51.8, defenseWR: 47.4,
                rankWinRates: { "Silver": 49.8, "Gold": 50.0, "Platinum": 49.9, "Diamond": 49.5, "Ascendant": 49.7, "Immortal": 49.4, "Radiant": 50.9 } },
            "Sunset": { winRate: 49.4, pickRate: 6.0, attackWR: 50.0, defenseWR: 48.8,
                rankWinRates: { "Silver": 49.6, "Gold": 49.8, "Platinum": 49.7, "Diamond": 49.3, "Ascendant": 49.5, "Immortal": 49.1, "Radiant": 50.7 } },
            "Icebox": { winRate: 50.2, pickRate: 6.3, attackWR: 51.7, defenseWR: 48.7,
                rankWinRates: { "Silver": 50.4, "Gold": 50.6, "Platinum": 50.5, "Diamond": 50.1, "Ascendant": 50.3, "Immortal": 50.0, "Radiant": 51.5 } }
        },
        ranks: {
            "Silver": { winRate: 50.24, pickRate: 15.78 },
            "Gold": { winRate: 50.41, pickRate: 17.75 },
            "Platinum": { winRate: 50.34, pickRate: 20.04 },
            "Diamond": { winRate: 49.93, pickRate: 21.38 },
            "Ascendant": { winRate: 50.15, pickRate: 20.59 },
            "Immortal": { winRate: 49.77, pickRate: 27.46 },
            "Radiant": { winRate: 51.3, pickRate: 32.3 }
        },
        analysis: {
            strengths: ["极高机动性", "烟雾配合突破", "大招连杀能力"],
            weaknesses: ["依赖枪法", "技能容错率低"],
            playstyle: "高机动决斗者，利用突进和漂浮进行非常规位打法。烟雾可以为自己创造射击窗口，大招在经济局非常强力。"
        }
    },
    "Sova": {
        role: "Initiator",
        overall: { winRate: 50.42, pickRate: 19.0, kd: 0.98, matches: 80200 },
        maps: {
            "Ascent": { winRate: 50.8, pickRate: 2.8, attackWR: 49.8, defenseWR: 51.8,
                rankWinRates: { "Silver": 50.6, "Gold": 51.0, "Platinum": 51.3, "Diamond": 50.6, "Ascendant": 51.2, "Immortal": 49.5, "Radiant": 58.4 } },
            "Bind": { winRate: 50.5, pickRate: 2.7, attackWR: 49.5, defenseWR: 51.5,
                rankWinRates: { "Silver": 50.3, "Gold": 50.7, "Platinum": 51.0, "Diamond": 50.3, "Ascendant": 50.9, "Immortal": 49.2, "Radiant": 58.1 } },
            "Haven": { winRate: 51.0, pickRate: 2.9, attackWR: 51.0, defenseWR: 51.0,
                rankWinRates: { "Silver": 50.8, "Gold": 51.2, "Platinum": 51.5, "Diamond": 50.8, "Ascendant": 51.4, "Immortal": 49.7, "Radiant": 58.6 } },
            "Split": { winRate: 50.2, pickRate: 2.7, attackWR: 49.5, defenseWR: 51.0,
                rankWinRates: { "Silver": 50.0, "Gold": 50.4, "Platinum": 50.7, "Diamond": 50.0, "Ascendant": 50.6, "Immortal": 48.9, "Radiant": 57.8 } },
            "Lotus": { winRate: 50.1, pickRate: 2.6, attackWR: 50.9, defenseWR: 49.3,
                rankWinRates: { "Silver": 49.9, "Gold": 50.3, "Platinum": 50.6, "Diamond": 49.9, "Ascendant": 50.5, "Immortal": 48.8, "Radiant": 57.7 } },
            "Sunset": { winRate: 49.9, pickRate: 2.6, attackWR: 49.4, defenseWR: 50.4,
                rankWinRates: { "Silver": 49.7, "Gold": 50.1, "Platinum": 50.4, "Diamond": 49.7, "Ascendant": 50.3, "Immortal": 48.6, "Radiant": 57.5 } },
            "Icebox": { winRate: 50.0, pickRate: 2.6, attackWR: 50.2, defenseWR: 49.8,
                rankWinRates: { "Silver": 49.8, "Gold": 50.2, "Platinum": 50.5, "Diamond": 49.8, "Ascendant": 50.4, "Immortal": 48.7, "Radiant": 57.6 } }
        },
        ranks: {
            "Silver": { winRate: 50.2, pickRate: 7.74 },
            "Gold": { winRate: 50.64, pickRate: 7.6 },
            "Platinum": { winRate: 50.96, pickRate: 8.09 },
            "Diamond": { winRate: 50.21, pickRate: 9.24 },
            "Ascendant": { winRate: 50.83, pickRate: 8.46 },
            "Immortal": { winRate: 49.1, pickRate: 9.13 },
            "Radiant": { winRate: 58.06, pickRate: 4.28 }
        },
        analysis: {
            strengths: ["全图侦查", "闪电伤害", "大招清场"],
            weaknesses: ["技能需要学习箭位", "机动性差"],
            playstyle: "侦查型先锋，利用侦查箭为团队提供关键信息。闪电可以逼出角落敌人，大招在残局非常强力。"
        }
    },
    "Cypher": {
        role: "Sentinel",
        overall: { winRate: 50.22, pickRate: 15.0, kd: 1.0, matches: 63300 },
        maps: {
            "Ascent": { winRate: 50.6, pickRate: 2.4, attackWR: 48.4, defenseWR: 52.8,
                rankWinRates: { "Silver": 51.1, "Gold": 51.4, "Platinum": 51.7, "Diamond": 52.0, "Ascendant": 51.7, "Immortal": 51.3, "Radiant": 72.4 } },
            "Bind": { winRate: 50.8, pickRate: 2.4, attackWR: 48.6, defenseWR: 53.0,
                rankWinRates: { "Silver": 51.3, "Gold": 51.6, "Platinum": 51.9, "Diamond": 52.2, "Ascendant": 51.9, "Immortal": 51.5, "Radiant": 72.6 } },
            "Haven": { winRate: 49.9, pickRate: 2.1, attackWR: 48.9, defenseWR: 50.9,
                rankWinRates: { "Silver": 50.4, "Gold": 50.7, "Platinum": 51.0, "Diamond": 51.3, "Ascendant": 51.0, "Immortal": 50.6, "Radiant": 71.7 } },
            "Split": { winRate: 50.4, pickRate: 2.3, attackWR: 48.5, defenseWR: 52.3,
                rankWinRates: { "Silver": 50.9, "Gold": 51.2, "Platinum": 51.5, "Diamond": 51.8, "Ascendant": 51.5, "Immortal": 51.1, "Radiant": 72.2 } },
            "Lotus": { winRate: 50.1, pickRate: 2.1, attackWR: 50.1, defenseWR: 50.1,
                rankWinRates: { "Silver": 50.6, "Gold": 50.9, "Platinum": 51.2, "Diamond": 51.5, "Ascendant": 51.2, "Immortal": 50.8, "Radiant": 71.9 } },
            "Sunset": { winRate: 49.6, pickRate: 2.1, attackWR: 48.0, defenseWR: 51.2,
                rankWinRates: { "Silver": 50.1, "Gold": 50.4, "Platinum": 50.7, "Diamond": 51.0, "Ascendant": 50.7, "Immortal": 50.3, "Radiant": 71.4 } },
            "Icebox": { winRate: 49.8, pickRate: 2.0, attackWR: 49.1, defenseWR: 50.5,
                rankWinRates: { "Silver": 50.3, "Gold": 50.6, "Platinum": 50.9, "Diamond": 51.2, "Ascendant": 50.9, "Immortal": 50.5, "Radiant": 71.6 } }
        },
        ranks: {
            "Silver": { winRate: 50.74, pickRate: 6.65 },
            "Gold": { winRate: 51.02, pickRate: 5.86 },
            "Platinum": { winRate: 51.28, pickRate: 5.33 },
            "Diamond": { winRate: 51.59, pickRate: 5.11 },
            "Ascendant": { winRate: 51.33, pickRate: 5.4 },
            "Immortal": { winRate: 50.9, pickRate: 5.19 },
            "Radiant": { winRate: 72.0, pickRate: 3.45 }
        },
        analysis: {
            strengths: ["全图监控", "绊线预警", "大招获取位置"],
            weaknesses: ["设备可被摧毁", "缺乏机动性"],
            playstyle: "监控型守卫，利用摄像头和绊线获取全图信息。大招可以复活获取敌人位置，在残局非常强力。"
        }
    },
    "Viper": {
        role: "Controller",
        overall: { winRate: 49.62, pickRate: 5.5, kd: 1.01, matches: 23200 },
        maps: {
            "Ascent": { winRate: 49.2, pickRate: 0.7, attackWR: 47.9, defenseWR: 50.5,
                rankWinRates: { "Silver": 49.9, "Gold": 50.0, "Platinum": 48.2, "Diamond": 49.9, "Ascendant": 49.2, "Immortal": 49.6, "Radiant": 48.8 } },
            "Bind": { winRate: 49.9, pickRate: 0.9, attackWR: 48.6, defenseWR: 51.2,
                rankWinRates: { "Silver": 50.6, "Gold": 50.7, "Platinum": 48.9, "Diamond": 50.6, "Ascendant": 49.9, "Immortal": 50.3, "Radiant": 50.2 } },
            "Haven": { winRate: 49.1, pickRate: 0.6, attackWR: 48.8, defenseWR: 49.4,
                rankWinRates: { "Silver": 49.8, "Gold": 49.9, "Platinum": 48.1, "Diamond": 49.8, "Ascendant": 49.1, "Immortal": 49.5, "Radiant": 48.6 } },
            "Split": { winRate: 49.0, pickRate: 0.6, attackWR: 48.0, defenseWR: 50.0,
                rankWinRates: { "Silver": 49.7, "Gold": 49.8, "Platinum": 48.0, "Diamond": 49.7, "Ascendant": 49.0, "Immortal": 49.4, "Radiant": 48.4 } },
            "Lotus": { winRate: 49.7, pickRate: 0.8, attackWR: 50.2, defenseWR: 49.2,
                rankWinRates: { "Silver": 50.4, "Gold": 50.5, "Platinum": 48.7, "Diamond": 50.4, "Ascendant": 49.7, "Immortal": 50.1, "Radiant": 49.8 } },
            "Sunset": { winRate: 48.8, pickRate: 0.5, attackWR: 48.0, defenseWR: 49.6,
                rankWinRates: { "Silver": 49.5, "Gold": 49.6, "Platinum": 47.8, "Diamond": 49.5, "Ascendant": 48.8, "Immortal": 49.2, "Radiant": 48.0 } },
            "Icebox": { winRate: 51.1, pickRate: 1.2, attackWR: 51.1, defenseWR: 51.1,
                rankWinRates: { "Silver": 51.8, "Gold": 51.9, "Platinum": 50.1, "Diamond": 51.8, "Ascendant": 51.1, "Immortal": 51.5, "Radiant": 52.6 } }
        },
        ranks: {
            "Silver": { winRate: 50.29, pickRate: 0.91 },
            "Gold": { winRate: 50.44, pickRate: 1.1 },
            "Platinum": { winRate: 48.61, pickRate: 1.24 },
            "Diamond": { winRate: 50.3, pickRate: 1.31 },
            "Ascendant": { winRate: 49.63, pickRate: 1.28 },
            "Immortal": { winRate: 50.0, pickRate: 0.95 },
            "Radiant": { winRate: 49.62, pickRate: 0.14 }
        },
        analysis: {
            strengths: ["区域封锁", "毒雾持续伤害", "大招范围控制"],
            weaknesses: ["毒雾需要燃料管理", "选取率偏低"],
            playstyle: "封锁型控场者，利用毒雾封锁关键区域。在Icebox等地图非常强力，大招可以控制大片区域。"
        }
    },
    "Neon": {
        role: "Duelist",
        overall: { winRate: 50.02, pickRate: 26.5, kd: 0.98, matches: 112000 },
        maps: {
            "Ascent": { winRate: 49.8, pickRate: 3.7, attackWR: 49.8, defenseWR: 49.8,
                rankWinRates: { "Silver": 49.9, "Gold": 49.8, "Platinum": 50.5, "Diamond": 49.9, "Ascendant": 50.4, "Immortal": 51.8, "Radiant": 64.7 } },
            "Bind": { winRate: 50.1, pickRate: 3.8, attackWR: 50.1, defenseWR: 50.1,
                rankWinRates: { "Silver": 50.2, "Gold": 50.1, "Platinum": 50.8, "Diamond": 50.2, "Ascendant": 50.7, "Immortal": 52.1, "Radiant": 65.0 } },
            "Haven": { winRate: 49.9, pickRate: 3.8, attackWR: 51.1, defenseWR: 48.7,
                rankWinRates: { "Silver": 50.0, "Gold": 49.9, "Platinum": 50.6, "Diamond": 50.0, "Ascendant": 50.5, "Immortal": 51.9, "Radiant": 64.8 } },
            "Split": { winRate: 50.5, pickRate: 3.9, attackWR: 50.8, defenseWR: 50.2,
                rankWinRates: { "Silver": 50.6, "Gold": 50.5, "Platinum": 51.2, "Diamond": 50.6, "Ascendant": 51.1, "Immortal": 52.5, "Radiant": 65.4 } },
            "Lotus": { winRate: 50.3, pickRate: 3.9, attackWR: 52.5, defenseWR: 48.1,
                rankWinRates: { "Silver": 50.4, "Gold": 50.3, "Platinum": 51.0, "Diamond": 50.4, "Ascendant": 50.9, "Immortal": 52.3, "Radiant": 65.2 } },
            "Sunset": { winRate: 49.5, pickRate: 3.6, attackWR: 50.1, defenseWR: 48.9,
                rankWinRates: { "Silver": 49.6, "Gold": 49.5, "Platinum": 50.2, "Diamond": 49.6, "Ascendant": 50.1, "Immortal": 51.5, "Radiant": 64.4 } },
            "Icebox": { winRate: 49.7, pickRate: 3.8, attackWR: 51.2, defenseWR: 48.2,
                rankWinRates: { "Silver": 49.8, "Gold": 49.7, "Platinum": 50.4, "Diamond": 49.8, "Ascendant": 50.3, "Immortal": 51.7, "Radiant": 64.6 } }
        },
        ranks: {
            "Silver": { winRate: 50.11, pickRate: 19.11 },
            "Gold": { winRate: 49.98, pickRate: 18.96 },
            "Platinum": { winRate: 50.76, pickRate: 18.48 },
            "Diamond": { winRate: 50.15, pickRate: 17.83 },
            "Ascendant": { winRate: 50.64, pickRate: 18.76 },
            "Immortal": { winRate: 52.01, pickRate: 19.52 },
            "Radiant": { winRate: 64.91, pickRate: 23.6 }
        },
        analysis: {
            strengths: ["极高移动速度", "闪电减速", "大招连杀"],
            weaknesses: ["冲刺容易被预判", "需要近战环境"],
            playstyle: "速度型决斗者，利用冲刺快速到达关键位置。闪电可以减速敌人，大招在近距离非常强力。"
        }
    },
    "Chamber": {
        role: "Sentinel",
        overall: { winRate: 49.62, pickRate: 41.0, kd: 1.11, matches: 173000 },
        maps: {
            "Ascent": { winRate: 50.0, pickRate: 6.1, attackWR: 47.8, defenseWR: 52.2,
                rankWinRates: { "Silver": 50.4, "Gold": 50.7, "Platinum": 50.4, "Diamond": 50.5, "Ascendant": 50.4, "Immortal": 50.0, "Radiant": 44.3 } },
            "Bind": { winRate: 49.9, pickRate: 6.0, attackWR: 47.7, defenseWR: 52.1,
                rankWinRates: { "Silver": 50.2, "Gold": 50.6, "Platinum": 50.3, "Diamond": 50.4, "Ascendant": 50.3, "Immortal": 49.9, "Radiant": 44.2 } },
            "Haven": { winRate: 49.7, pickRate: 5.9, attackWR: 48.7, defenseWR: 50.7,
                rankWinRates: { "Silver": 50.1, "Gold": 50.4, "Platinum": 50.1, "Diamond": 50.2, "Ascendant": 50.1, "Immortal": 49.7, "Radiant": 44.0 } },
            "Split": { winRate: 49.4, pickRate: 5.9, attackWR: 47.5, defenseWR: 51.3,
                rankWinRates: { "Silver": 49.8, "Gold": 50.1, "Platinum": 49.8, "Diamond": 49.9, "Ascendant": 49.8, "Immortal": 49.4, "Radiant": 43.7 } },
            "Lotus": { winRate: 49.3, pickRate: 5.8, attackWR: 49.3, defenseWR: 49.3,
                rankWinRates: { "Silver": 49.6, "Gold": 50.0, "Platinum": 49.7, "Diamond": 49.8, "Ascendant": 49.7, "Immortal": 49.3, "Radiant": 43.6 } },
            "Sunset": { winRate: 49.1, pickRate: 5.8, attackWR: 47.5, defenseWR: 50.7,
                rankWinRates: { "Silver": 49.5, "Gold": 49.8, "Platinum": 49.5, "Diamond": 49.6, "Ascendant": 49.5, "Immortal": 49.1, "Radiant": 43.4 } },
            "Icebox": { winRate: 49.2, pickRate: 5.7, attackWR: 48.5, defenseWR: 49.9,
                rankWinRates: { "Silver": 49.6, "Gold": 49.9, "Platinum": 49.6, "Diamond": 49.7, "Ascendant": 49.6, "Immortal": 49.2, "Radiant": 43.5 } }
        },
        ranks: {
            "Silver": { winRate: 49.97, pickRate: 23.63 },
            "Gold": { winRate: 50.31, pickRate: 25.85 },
            "Platinum": { winRate: 50.04, pickRate: 27.17 },
            "Diamond": { winRate: 50.08, pickRate: 27.57 },
            "Ascendant": { winRate: 50.04, pickRate: 26.47 },
            "Immortal": { winRate: 49.66, pickRate: 27.09 },
            "Radiant": { winRate: 43.88, pickRate: 13.8 }
        },
        analysis: {
            strengths: ["高伤害狙击", "传送逃脱", "大招双倍射速"],
            weaknesses: ["依赖枪法", "守卫能力弱"],
            playstyle: "狙击型守卫，利用传送进行激进打法。大招可以提供双倍射速，在经济局非常强力。"
        }
    },
    "Iso": {
        role: "Duelist",
        overall: { winRate: 48.32, pickRate: 10.0, kd: 1.01, matches: 42200 },
        maps: {
            "Ascent": { winRate: 48.5, pickRate: 1.5, attackWR: 48.5, defenseWR: 48.5,
                rankWinRates: { "Silver": 48.6, "Gold": 48.2, "Platinum": 48.6, "Diamond": 49.5, "Ascendant": 48.8, "Immortal": 48.3, "Radiant": 62.3 } },
            "Bind": { winRate: 48.3, pickRate: 1.4, attackWR: 48.3, defenseWR: 48.3,
                rankWinRates: { "Silver": 48.4, "Gold": 48.0, "Platinum": 48.4, "Diamond": 49.2, "Ascendant": 48.5, "Immortal": 48.1, "Radiant": 62.1 } },
            "Haven": { winRate: 48.0, pickRate: 1.3, attackWR: 49.2, defenseWR: 46.8,
                rankWinRates: { "Silver": 48.1, "Gold": 47.7, "Platinum": 48.1, "Diamond": 49.0, "Ascendant": 48.2, "Immortal": 47.8, "Radiant": 61.8 } },
            "Split": { winRate: 48.6, pickRate: 1.5, attackWR: 48.9, defenseWR: 48.3,
                rankWinRates: { "Silver": 48.7, "Gold": 48.3, "Platinum": 48.7, "Diamond": 49.6, "Ascendant": 48.9, "Immortal": 48.4, "Radiant": 62.4 } },
            "Lotus": { winRate: 48.1, pickRate: 1.4, attackWR: 50.3, defenseWR: 45.9,
                rankWinRates: { "Silver": 48.2, "Gold": 47.8, "Platinum": 48.2, "Diamond": 49.1, "Ascendant": 48.4, "Immortal": 47.9, "Radiant": 61.9 } },
            "Sunset": { winRate: 47.8, pickRate: 1.3, attackWR: 48.4, defenseWR: 47.2,
                rankWinRates: { "Silver": 47.9, "Gold": 47.5, "Platinum": 47.9, "Diamond": 48.8, "Ascendant": 48.0, "Immortal": 47.6, "Radiant": 61.6 } },
            "Icebox": { winRate: 47.9, pickRate: 1.4, attackWR: 49.4, defenseWR: 46.4,
                rankWinRates: { "Silver": 48.0, "Gold": 47.6, "Platinum": 48.0, "Diamond": 48.9, "Ascendant": 48.1, "Immortal": 47.7, "Radiant": 61.7 } }
        },
        ranks: {
            "Silver": { winRate: 48.44, pickRate: 4.44 },
            "Gold": { winRate: 48.02, pickRate: 3.92 },
            "Platinum": { winRate: 48.4, pickRate: 3.46 },
            "Diamond": { winRate: 49.27, pickRate: 3.04 },
            "Ascendant": { winRate: 48.57, pickRate: 3.49 },
            "Immortal": { winRate: 48.1, pickRate: 3.35 },
            "Radiant": { winRate: 62.11, pickRate: 13.25 }
        },
        analysis: {
            strengths: ["1v1决斗能力", "护盾技能", "大招单挑"],
            weaknesses: ["胜率偏低", "团队贡献有限"],
            playstyle: "决斗型特工，利用护盾和1v1能力进行正面交锋。大招可以强制单挑，适合枪法自信的玩家。"
        }
    },
    "Deadlock": {
        role: "Sentinel",
        overall: { winRate: 50.02, pickRate: 9.0, kd: 0.96, matches: 38000 },
        maps: {
            "Ascent": { winRate: 50.3, pickRate: 1.5, attackWR: 48.1, defenseWR: 52.5,
                rankWinRates: { "Silver": 48.5, "Gold": 48.0, "Platinum": 49.0, "Diamond": 48.2, "Ascendant": 50.8, "Immortal": 49.3, "Radiant": 53.1 } },
            "Bind": { winRate: 50.2, pickRate: 1.4, attackWR: 48.0, defenseWR: 52.4,
                rankWinRates: { "Silver": 48.4, "Gold": 47.9, "Platinum": 48.9, "Diamond": 48.1, "Ascendant": 50.7, "Immortal": 49.2, "Radiant": 53.0 } },
            "Haven": { winRate: 49.8, pickRate: 1.2, attackWR: 48.8, defenseWR: 50.8,
                rankWinRates: { "Silver": 48.0, "Gold": 47.5, "Platinum": 48.5, "Diamond": 47.7, "Ascendant": 50.3, "Immortal": 48.8, "Radiant": 52.6 } },
            "Split": { winRate: 50.1, pickRate: 1.4, attackWR: 48.2, defenseWR: 52.0,
                rankWinRates: { "Silver": 48.3, "Gold": 47.8, "Platinum": 48.8, "Diamond": 48.0, "Ascendant": 50.6, "Immortal": 49.1, "Radiant": 52.9 } },
            "Lotus": { winRate: 49.9, pickRate: 1.3, attackWR: 49.9, defenseWR: 49.9,
                rankWinRates: { "Silver": 48.1, "Gold": 47.6, "Platinum": 48.6, "Diamond": 47.8, "Ascendant": 50.4, "Immortal": 48.9, "Radiant": 52.7 } },
            "Sunset": { winRate: 49.7, pickRate: 1.3, attackWR: 48.1, defenseWR: 51.3,
                rankWinRates: { "Silver": 47.9, "Gold": 47.4, "Platinum": 48.4, "Diamond": 47.6, "Ascendant": 50.2, "Immortal": 48.7, "Radiant": 52.5 } },
            "Icebox": { winRate: 49.8, pickRate: 1.2, attackWR: 49.1, defenseWR: 50.5,
                rankWinRates: { "Silver": 48.0, "Gold": 47.5, "Platinum": 48.5, "Diamond": 47.7, "Ascendant": 50.3, "Immortal": 48.8, "Radiant": 52.6 } }
        },
        ranks: {
            "Silver": { winRate: 48.21, pickRate: 0.94 },
            "Gold": { winRate: 47.72, pickRate: 0.86 },
            "Platinum": { winRate: 48.72, pickRate: 0.73 },
            "Diamond": { winRate: 47.97, pickRate: 0.71 },
            "Ascendant": { winRate: 50.56, pickRate: 0.69 },
            "Immortal": { winRate: 49.06, pickRate: 0.5 },
            "Radiant": { winRate: 52.8, pickRate: 0.3 }
        },
        analysis: {
            strengths: ["声波探测", "屏障控制", "大招范围捕获"],
            weaknesses: ["技能容易被破坏", "选取率偏低"],
            playstyle: "控制型守卫，利用声波和屏障限制敌人移动。适合防守方使用，大招在回防时可以有效清场。"
        }
    },
    "Reyna": {
        role: "Duelist",
        overall: { winRate: 49.92, pickRate: 45.0, kd: 1.08, matches: 190000 },
        maps: {
            "Ascent": { winRate: 50.0, pickRate: 6.5, attackWR: 50.0, defenseWR: 50.0,
                rankWinRates: { "Silver": 50.4, "Gold": 50.2, "Platinum": 50.2, "Diamond": 50.1, "Ascendant": 50.1, "Immortal": 48.9, "Radiant": 59.7 } },
            "Bind": { winRate: 49.7, pickRate: 6.4, attackWR: 49.7, defenseWR: 49.7,
                rankWinRates: { "Silver": 50.1, "Gold": 49.9, "Platinum": 50.0, "Diamond": 49.8, "Ascendant": 49.8, "Immortal": 48.6, "Radiant": 59.4 } },
            "Haven": { winRate: 49.4, pickRate: 6.3, attackWR: 50.6, defenseWR: 48.2,
                rankWinRates: { "Silver": 49.8, "Gold": 49.6, "Platinum": 49.6, "Diamond": 49.5, "Ascendant": 49.5, "Immortal": 48.3, "Radiant": 59.1 } },
            "Split": { winRate: 50.4, pickRate: 6.6, attackWR: 50.7, defenseWR: 50.1,
                rankWinRates: { "Silver": 50.8, "Gold": 50.6, "Platinum": 50.6, "Diamond": 50.5, "Ascendant": 50.5, "Immortal": 49.3, "Radiant": 60.1 } },
            "Lotus": { winRate: 49.6, pickRate: 6.4, attackWR: 51.8, defenseWR: 47.4,
                rankWinRates: { "Silver": 50.0, "Gold": 49.8, "Platinum": 49.9, "Diamond": 49.7, "Ascendant": 49.7, "Immortal": 48.5, "Radiant": 59.3 } },
            "Sunset": { winRate: 49.2, pickRate: 6.2, attackWR: 49.8, defenseWR: 48.6,
                rankWinRates: { "Silver": 49.6, "Gold": 49.4, "Platinum": 49.5, "Diamond": 49.3, "Ascendant": 49.3, "Immortal": 48.1, "Radiant": 58.9 } },
            "Icebox": { winRate: 50.2, pickRate: 6.6, attackWR: 51.7, defenseWR: 48.7,
                rankWinRates: { "Silver": 50.6, "Gold": 50.4, "Platinum": 50.5, "Diamond": 50.3, "Ascendant": 50.3, "Immortal": 49.1, "Radiant": 59.9 } }
        },
        ranks: {
            "Silver": { winRate: 50.37, pickRate: 24.3 },
            "Gold": { winRate: 50.14, pickRate: 23.2 },
            "Platinum": { winRate: 50.17, pickRate: 21.84 },
            "Diamond": { winRate: 50.01, pickRate: 21.2 },
            "Ascendant": { winRate: 50.06, pickRate: 22.45 },
            "Immortal": { winRate: 48.8, pickRate: 22.36 },
            "Radiant": { winRate: 59.62, pickRate: 29.68 }
        },
        analysis: {
            strengths: ["击杀后回复", "无敌技能", "大招群体压制"],
            weaknesses: ["依赖击杀", "无团队辅助"],
            playstyle: "击杀型决斗者，需要枪法自信。每次击杀后可以获得治疗或无敌，适合连续突破的打法。"
        }
    },
    "Fade": {
        role: "Initiator",
        overall: { winRate: 50.52, pickRate: 18.5, kd: 0.93, matches: 78100 },
        maps: {
            "Ascent": { winRate: 50.2, pickRate: 2.6, attackWR: 49.2, defenseWR: 51.2,
                rankWinRates: { "Silver": 51.4, "Gold": 51.3, "Platinum": 51.2, "Diamond": 51.4, "Ascendant": 50.7, "Immortal": 50.3, "Radiant": 54.2 } },
            "Bind": { winRate: 50.3, pickRate: 2.6, attackWR: 49.3, defenseWR: 51.3,
                rankWinRates: { "Silver": 51.5, "Gold": 51.4, "Platinum": 51.3, "Diamond": 51.5, "Ascendant": 50.8, "Immortal": 50.4, "Radiant": 54.3 } },
            "Haven": { winRate: 51.0, pickRate: 2.8, attackWR: 51.0, defenseWR: 51.0,
                rankWinRates: { "Silver": 52.2, "Gold": 52.1, "Platinum": 52.0, "Diamond": 52.2, "Ascendant": 51.5, "Immortal": 51.1, "Radiant": 55.0 } },
            "Split": { winRate: 50.8, pickRate: 2.7, attackWR: 50.0, defenseWR: 51.5,
                rankWinRates: { "Silver": 52.0, "Gold": 51.9, "Platinum": 51.8, "Diamond": 52.0, "Ascendant": 51.3, "Immortal": 50.9, "Radiant": 54.8 } },
            "Lotus": { winRate: 50.6, pickRate: 2.7, attackWR: 51.4, defenseWR: 49.8,
                rankWinRates: { "Silver": 51.8, "Gold": 51.7, "Platinum": 51.6, "Diamond": 51.8, "Ascendant": 51.1, "Immortal": 50.7, "Radiant": 54.6 } },
            "Sunset": { winRate: 50.1, pickRate: 2.5, attackWR: 49.6, defenseWR: 50.6,
                rankWinRates: { "Silver": 51.3, "Gold": 51.2, "Platinum": 51.1, "Diamond": 51.3, "Ascendant": 50.6, "Immortal": 50.2, "Radiant": 54.1 } },
            "Icebox": { winRate: 50.0, pickRate: 2.5, attackWR: 50.2, defenseWR: 49.8,
                rankWinRates: { "Silver": 51.2, "Gold": 51.1, "Platinum": 51.0, "Diamond": 51.2, "Ascendant": 50.5, "Immortal": 50.1, "Radiant": 54.0 } }
        },
        ranks: {
            "Silver": { winRate: 51.68, pickRate: 6.24 },
            "Gold": { winRate: 51.62, pickRate: 7.45 },
            "Platinum": { winRate: 51.51, pickRate: 8.72 },
            "Diamond": { winRate: 51.68, pickRate: 10.04 },
            "Ascendant": { winRate: 50.99, pickRate: 9.26 },
            "Immortal": { winRate: 50.65, pickRate: 10.11 },
            "Radiant": { winRate: 54.55, pickRate: 4.55 }
        },
        analysis: {
            strengths: ["恐惧技能", "全图大招", "追踪敌人"],
            weaknesses: ["技能需要预判", "选取率偏低"],
            playstyle: "恐惧型先锋，利用噩梦技能打乱敌人阵型。大招可以全图标记敌人，为团队提供关键信息。"
        }
    },
    "Brimstone": {
        role: "Controller",
        overall: { winRate: 50.72, pickRate: 11.0, kd: 0.97, matches: 46400 },
        maps: {
            "Ascent": { winRate: 51.5, pickRate: 1.8, attackWR: 50.2, defenseWR: 52.8,
                rankWinRates: { "Silver": 50.6, "Gold": 50.4, "Platinum": 51.0, "Diamond": 52.6, "Ascendant": 52.1, "Immortal": 54.4, "Radiant": 73.8 } },
            "Bind": { winRate: 51.2, pickRate: 1.7, attackWR: 49.9, defenseWR: 52.5,
                rankWinRates: { "Silver": 50.3, "Gold": 50.1, "Platinum": 50.7, "Diamond": 52.3, "Ascendant": 51.8, "Immortal": 54.1, "Radiant": 73.5 } },
            "Haven": { winRate: 50.9, pickRate: 1.6, attackWR: 50.6, defenseWR: 51.2,
                rankWinRates: { "Silver": 50.0, "Gold": 49.8, "Platinum": 50.4, "Diamond": 52.0, "Ascendant": 51.5, "Immortal": 53.8, "Radiant": 73.2 } },
            "Split": { winRate: 50.6, pickRate: 1.5, attackWR: 49.6, defenseWR: 51.6,
                rankWinRates: { "Silver": 49.7, "Gold": 49.5, "Platinum": 50.1, "Diamond": 51.7, "Ascendant": 51.2, "Immortal": 53.5, "Radiant": 72.8 } },
            "Lotus": { winRate: 50.4, pickRate: 1.5, attackWR: 50.9, defenseWR: 49.9,
                rankWinRates: { "Silver": 49.5, "Gold": 49.3, "Platinum": 49.9, "Diamond": 51.5, "Ascendant": 51.0, "Immortal": 53.3, "Radiant": 72.7 } },
            "Sunset": { winRate: 50.0, pickRate: 1.4, attackWR: 49.2, defenseWR: 50.8,
                rankWinRates: { "Silver": 49.1, "Gold": 48.9, "Platinum": 49.5, "Diamond": 51.1, "Ascendant": 50.6, "Immortal": 52.9, "Radiant": 72.2 } },
            "Icebox": { winRate: 50.2, pickRate: 1.4, attackWR: 50.2, defenseWR: 50.2,
                rankWinRates: { "Silver": 49.3, "Gold": 49.1, "Platinum": 49.7, "Diamond": 51.3, "Ascendant": 50.8, "Immortal": 53.1, "Radiant": 72.5 } }
        },
        ranks: {
            "Silver": { winRate: 49.86, pickRate: 2.97 },
            "Gold": { winRate: 49.59, pickRate: 2.21 },
            "Platinum": { winRate: 50.26, pickRate: 1.86 },
            "Diamond": { winRate: 51.84, pickRate: 1.73 },
            "Ascendant": { winRate: 51.33, pickRate: 1.56 },
            "Immortal": { winRate: 53.62, pickRate: 1.11 },
            "Radiant": { winRate: 72.97, pickRate: 5.11 }
        },
        analysis: {
            strengths: ["快速烟雾", "激励大招", "空袭伤害"],
            weaknesses: ["烟雾位置固定", "缺乏机动性"],
            playstyle: "传统控场者，烟雾可以快速部署。大招激励可以大幅提升团队火力，适合进攻方使用。"
        }
    },
    "Veto": {
        role: "Sentinel",
        overall: { winRate: 49.02, pickRate: 3.0, kd: 1.02, matches: 12600 },
        maps: {
            "Ascent": { winRate: 49.1, pickRate: 0.5, attackWR: 46.9, defenseWR: 51.3,
                rankWinRates: { "Silver": 49.6, "Gold": 48.5, "Platinum": 48.9, "Diamond": 48.8, "Ascendant": 49.5, "Immortal": 44.5, "Radiant": 49.2 } },
            "Bind": { winRate: 49.3, pickRate: 0.6, attackWR: 47.1, defenseWR: 51.5,
                rankWinRates: { "Silver": 49.8, "Gold": 48.7, "Platinum": 49.0, "Diamond": 49.0, "Ascendant": 49.7, "Immortal": 44.7, "Radiant": 49.6 } },
            "Haven": { winRate: 48.8, pickRate: 0.4, attackWR: 47.8, defenseWR: 49.8,
                rankWinRates: { "Silver": 49.3, "Gold": 48.2, "Platinum": 48.5, "Diamond": 48.5, "Ascendant": 49.2, "Immortal": 44.2, "Radiant": 48.6 } },
            "Split": { winRate: 49.2, pickRate: 0.6, attackWR: 47.3, defenseWR: 51.1,
                rankWinRates: { "Silver": 49.7, "Gold": 48.6, "Platinum": 49.0, "Diamond": 48.9, "Ascendant": 49.6, "Immortal": 44.6, "Radiant": 49.4 } },
            "Lotus": { winRate: 48.9, pickRate: 0.4, attackWR: 48.9, defenseWR: 48.9,
                rankWinRates: { "Silver": 49.4, "Gold": 48.3, "Platinum": 48.6, "Diamond": 48.6, "Ascendant": 49.3, "Immortal": 44.3, "Radiant": 48.8 } },
            "Sunset": { winRate: 48.6, pickRate: 0.4, attackWR: 47.0, defenseWR: 50.2,
                rankWinRates: { "Silver": 49.1, "Gold": 48.0, "Platinum": 48.4, "Diamond": 48.3, "Ascendant": 49.0, "Immortal": 44.0, "Radiant": 48.2 } },
            "Icebox": { winRate: 48.7, pickRate: 0.3, attackWR: 48.0, defenseWR: 49.4,
                rankWinRates: { "Silver": 49.2, "Gold": 48.1, "Platinum": 48.5, "Diamond": 48.4, "Ascendant": 49.1, "Immortal": 44.1, "Radiant": 48.4 } }
        },
        ranks: {
            "Silver": { winRate: 49.56, pickRate: 1.07 },
            "Gold": { winRate: 48.4, pickRate: 1.06 },
            "Platinum": { winRate: 48.77, pickRate: 0.99 },
            "Diamond": { winRate: 48.7, pickRate: 1.03 },
            "Ascendant": { winRate: 49.38, pickRate: 1.07 },
            "Immortal": { winRate: 44.44, pickRate: 0.88 },
            "Radiant": { winRate: 49.02, pickRate: 0.55 }
        },
        analysis: {
            strengths: ["独特技能组", "防守潜力", "新特工新鲜感"],
            weaknesses: ["数据样本少", "战术未成熟"],
            playstyle: "新晋守卫，技能机制独特。目前数据样本较少，建议多尝试找到最佳使用方式。"
        }
    },
    "Vyse": {
        role: "Sentinel",
        overall: { winRate: 50.02, pickRate: 3.5, kd: 1.01, matches: 14800 },
        maps: {
            "Ascent": { winRate: 49.8, pickRate: 0.5, attackWR: 47.6, defenseWR: 52.0,
                rankWinRates: { "Silver": 50.6, "Gold": 49.7, "Platinum": 50.0, "Diamond": 52.1, "Ascendant": 50.4, "Immortal": 49.2, "Radiant": 49.6 } },
            "Bind": { winRate: 50.4, pickRate: 0.7, attackWR: 48.2, defenseWR: 52.6,
                rankWinRates: { "Silver": 51.2, "Gold": 50.3, "Platinum": 50.6, "Diamond": 52.7, "Ascendant": 51.0, "Immortal": 49.8, "Radiant": 50.8 } },
            "Haven": { winRate: 49.7, pickRate: 0.4, attackWR: 48.7, defenseWR: 50.7,
                rankWinRates: { "Silver": 50.5, "Gold": 49.6, "Platinum": 49.9, "Diamond": 52.0, "Ascendant": 50.3, "Immortal": 49.1, "Radiant": 49.4 } },
            "Split": { winRate: 50.2, pickRate: 0.7, attackWR: 48.3, defenseWR: 52.1,
                rankWinRates: { "Silver": 51.0, "Gold": 50.1, "Platinum": 50.4, "Diamond": 52.5, "Ascendant": 50.8, "Immortal": 49.6, "Radiant": 50.4 } },
            "Lotus": { winRate: 50.0, pickRate: 0.5, attackWR: 50.0, defenseWR: 50.0,
                rankWinRates: { "Silver": 50.8, "Gold": 49.9, "Platinum": 50.2, "Diamond": 52.3, "Ascendant": 50.6, "Immortal": 49.4, "Radiant": 50.0 } },
            "Sunset": { winRate: 49.6, pickRate: 0.5, attackWR: 48.0, defenseWR: 51.2,
                rankWinRates: { "Silver": 50.4, "Gold": 49.5, "Platinum": 49.8, "Diamond": 51.9, "Ascendant": 50.2, "Immortal": 49.0, "Radiant": 49.2 } },
            "Icebox": { winRate: 49.7, pickRate: 0.4, attackWR: 49.0, defenseWR: 50.4,
                rankWinRates: { "Silver": 50.5, "Gold": 49.6, "Platinum": 49.9, "Diamond": 52.0, "Ascendant": 50.3, "Immortal": 49.1, "Radiant": 49.4 } }
        },
        ranks: {
            "Silver": { winRate: 50.87, pickRate: 1.13 },
            "Gold": { winRate: 49.95, pickRate: 1.24 },
            "Platinum": { winRate: 50.2, pickRate: 1.32 },
            "Diamond": { winRate: 52.36, pickRate: 1.29 },
            "Ascendant": { winRate: 50.64, pickRate: 1.37 },
            "Immortal": { winRate: 49.38, pickRate: 1.12 },
            "Radiant": { winRate: 50.02, pickRate: 0.41 }
        },
        analysis: {
            strengths: ["独特机制", "防守能力", "新特工潜力"],
            weaknesses: ["数据极少", "战术待开发"],
            playstyle: "新晋守卫，拥有独特的技能机制。目前还在探索阶段，建议多练习找到适合自己的打法。"
        }
    },
    "Gekko": {
        role: "Initiator",
        overall: { winRate: 50.62, pickRate: 14.0, kd: 0.89, matches: 59100 },
        maps: {
            "Ascent": { winRate: 50.3, pickRate: 1.9, attackWR: 49.3, defenseWR: 51.3,
                rankWinRates: { "Silver": 51.1, "Gold": 50.3, "Platinum": 49.6, "Diamond": 48.8, "Ascendant": 49.5, "Immortal": 50.5, "Radiant": 50.2 } },
            "Bind": { winRate: 51.0, pickRate: 2.1, attackWR: 50.0, defenseWR: 52.0,
                rankWinRates: { "Silver": 51.9, "Gold": 51.0, "Platinum": 50.3, "Diamond": 49.5, "Ascendant": 50.2, "Immortal": 51.2, "Radiant": 50.9 } },
            "Haven": { winRate: 50.8, pickRate: 2.1, attackWR: 50.8, defenseWR: 50.8,
                rankWinRates: { "Silver": 51.6, "Gold": 50.8, "Platinum": 50.1, "Diamond": 49.2, "Ascendant": 50.0, "Immortal": 51.0, "Radiant": 50.7 } },
            "Split": { winRate: 50.5, pickRate: 2.0, attackWR: 49.8, defenseWR: 51.2,
                rankWinRates: { "Silver": 51.4, "Gold": 50.5, "Platinum": 49.8, "Diamond": 49.0, "Ascendant": 49.7, "Immortal": 50.7, "Radiant": 50.4 } },
            "Lotus": { winRate: 51.2, pickRate: 2.2, attackWR: 52.0, defenseWR: 50.4,
                rankWinRates: { "Silver": 52.1, "Gold": 51.2, "Platinum": 50.5, "Diamond": 49.7, "Ascendant": 50.4, "Immortal": 51.4, "Radiant": 51.1 } },
            "Sunset": { winRate: 50.0, pickRate: 1.8, attackWR: 49.5, defenseWR: 50.5,
                rankWinRates: { "Silver": 50.9, "Gold": 50.0, "Platinum": 49.3, "Diamond": 48.5, "Ascendant": 49.2, "Immortal": 50.2, "Radiant": 49.9 } },
            "Icebox": { winRate: 50.2, pickRate: 1.9, attackWR: 50.5, defenseWR: 50.0,
                rankWinRates: { "Silver": 51.1, "Gold": 50.2, "Platinum": 49.5, "Diamond": 48.7, "Ascendant": 49.4, "Immortal": 50.4, "Radiant": 50.1 } }
        },
        ranks: {
            "Silver": { winRate: 51.47, pickRate: 2.92 },
            "Gold": { winRate: 50.66, pickRate: 2.27 },
            "Platinum": { winRate: 49.92, pickRate: 1.58 },
            "Diamond": { winRate: 49.07, pickRate: 0.98 },
            "Ascendant": { winRate: 49.85, pickRate: 1.35 },
            "Immortal": { winRate: 50.85, pickRate: 0.28 },
            "Radiant": { winRate: 50.5, pickRate: 0.1 }
        },
        analysis: {
            strengths: ["生物伙伴", "多功能技能", "大招可回收"],
            weaknesses: ["生物容易被击杀", "需要多线操作"],
            playstyle: "生物型先锋，利用小生物进行侦查和控制。技能可以回收重复使用，经济效率高。"
        }
    },
    "Astra": {
        role: "Controller",
        overall: { winRate: 48.72, pickRate: 4.5, kd: 1.03, matches: 19000 },
        maps: {
            "Ascent": { winRate: 49.0, pickRate: 0.7, attackWR: 47.7, defenseWR: 50.3,
                rankWinRates: { "Silver": 49.1, "Gold": 49.9, "Platinum": 48.1, "Diamond": 48.0, "Ascendant": 48.6, "Immortal": 45.6, "Radiant": 67.0 } },
            "Bind": { winRate: 48.5, pickRate: 0.6, attackWR: 47.2, defenseWR: 49.8,
                rankWinRates: { "Silver": 48.6, "Gold": 49.4, "Platinum": 47.6, "Diamond": 47.5, "Ascendant": 48.1, "Immortal": 45.1, "Radiant": 66.5 } },
            "Haven": { winRate: 48.9, pickRate: 0.7, attackWR: 48.6, defenseWR: 49.2,
                rankWinRates: { "Silver": 49.0, "Gold": 49.8, "Platinum": 48.0, "Diamond": 47.9, "Ascendant": 48.5, "Immortal": 45.5, "Radiant": 66.8 } },
            "Split": { winRate: 48.8, pickRate: 0.7, attackWR: 47.8, defenseWR: 49.8,
                rankWinRates: { "Silver": 48.9, "Gold": 49.6, "Platinum": 47.9, "Diamond": 47.8, "Ascendant": 48.4, "Immortal": 45.4, "Radiant": 66.8 } },
            "Lotus": { winRate: 48.4, pickRate: 0.6, attackWR: 48.9, defenseWR: 47.9,
                rankWinRates: { "Silver": 48.5, "Gold": 49.2, "Platinum": 47.5, "Diamond": 47.4, "Ascendant": 48.0, "Immortal": 45.0, "Radiant": 66.3 } },
            "Sunset": { winRate: 48.2, pickRate: 0.5, attackWR: 47.4, defenseWR: 49.0,
                rankWinRates: { "Silver": 48.3, "Gold": 49.1, "Platinum": 47.3, "Diamond": 47.2, "Ascendant": 47.8, "Immortal": 44.8, "Radiant": 66.2 } },
            "Icebox": { winRate: 48.3, pickRate: 0.5, attackWR: 48.2, defenseWR: 48.3,
                rankWinRates: { "Silver": 48.4, "Gold": 49.1, "Platinum": 47.4, "Diamond": 47.3, "Ascendant": 47.9, "Immortal": 44.9, "Radiant": 66.2 } }
        },
        ranks: {
            "Silver": { winRate: 48.84, pickRate: 1.11 },
            "Gold": { winRate: 49.57, pickRate: 1.57 },
            "Platinum": { winRate: 47.8, pickRate: 2.19 },
            "Diamond": { winRate: 47.68, pickRate: 2.57 },
            "Ascendant": { winRate: 48.35, pickRate: 2.14 },
            "Immortal": { winRate: 45.32, pickRate: 1.97 },
            "Radiant": { winRate: 66.67, pickRate: 0.41 }
        },
        analysis: {
            strengths: ["全图烟雾", "引力大招", "技能可重复"],
            weaknesses: ["学习曲线陡峭", "需要地图理解"],
            playstyle: "高阶控场者，需要深厚的地图理解。星尘可以放置在全图任何位置，适合有经验的玩家。"
        }
    },
    "Skye": {
        role: "Initiator",
        overall: { winRate: 49.82, pickRate: 17.5, kd: 0.93, matches: 73800 },
        maps: {
            "Ascent": { winRate: 49.5, pickRate: 2.4, attackWR: 48.5, defenseWR: 50.5,
                rankWinRates: { "Silver": 50.6, "Gold": 50.7, "Platinum": 50.7, "Diamond": 50.8, "Ascendant": 50.5, "Immortal": 50.4, "Radiant": 43.3 } },
            "Bind": { winRate: 49.9, pickRate: 2.5, attackWR: 48.9, defenseWR: 50.9,
                rankWinRates: { "Silver": 51.0, "Gold": 51.1, "Platinum": 51.1, "Diamond": 51.2, "Ascendant": 50.9, "Immortal": 50.8, "Radiant": 43.7 } },
            "Haven": { winRate: 50.1, pickRate: 2.6, attackWR: 50.1, defenseWR: 50.1,
                rankWinRates: { "Silver": 51.2, "Gold": 51.3, "Platinum": 51.3, "Diamond": 51.4, "Ascendant": 51.1, "Immortal": 51.0, "Radiant": 43.9 } },
            "Split": { winRate: 50.3, pickRate: 2.6, attackWR: 49.5, defenseWR: 51.0,
                rankWinRates: { "Silver": 51.4, "Gold": 51.5, "Platinum": 51.5, "Diamond": 51.6, "Ascendant": 51.3, "Immortal": 51.2, "Radiant": 44.1 } },
            "Lotus": { winRate: 49.6, pickRate: 2.4, attackWR: 50.4, defenseWR: 48.8,
                rankWinRates: { "Silver": 50.7, "Gold": 50.8, "Platinum": 50.8, "Diamond": 50.9, "Ascendant": 50.6, "Immortal": 50.5, "Radiant": 43.4 } },
            "Sunset": { winRate: 49.3, pickRate: 2.4, attackWR: 48.8, defenseWR: 49.8,
                rankWinRates: { "Silver": 50.4, "Gold": 50.5, "Platinum": 50.5, "Diamond": 50.6, "Ascendant": 50.3, "Immortal": 50.2, "Radiant": 43.1 } },
            "Icebox": { winRate: 49.4, pickRate: 2.4, attackWR: 49.6, defenseWR: 49.1,
                rankWinRates: { "Silver": 50.5, "Gold": 50.6, "Platinum": 50.6, "Diamond": 50.7, "Ascendant": 50.4, "Immortal": 50.3, "Radiant": 43.2 } }
        },
        ranks: {
            "Silver": { winRate: 50.94, pickRate: 9.77 },
            "Gold": { winRate: 51.03, pickRate: 9.53 },
            "Platinum": { winRate: 51.04, pickRate: 9.3 },
            "Diamond": { winRate: 51.14, pickRate: 9.14 },
            "Ascendant": { winRate: 50.86, pickRate: 8.95 },
            "Immortal": { winRate: 50.68, pickRate: 7.87 },
            "Radiant": { winRate: 43.59, pickRate: 5.38 }
        },
        analysis: {
            strengths: ["治疗能力", "闪光技能", "大招群体控制"],
            weaknesses: ["闪光可被躲避", "生物容易被击杀"],
            playstyle: "治疗型先锋，可以为团队提供治疗支持。闪光技能可以配合队友突破，大招在进攻时非常有效。"
        }
    },
    "Miks": {
        role: "Controller",
        overall: { winRate: 49.12, pickRate: 40.5, kd: 0.94, matches: 171000 },
        maps: {
            "Ascent": { winRate: 48.8, pickRate: 5.7, attackWR: 47.5, defenseWR: 50.1,
                rankWinRates: { "Silver": 49.0, "Gold": 48.9, "Platinum": 49.2, "Diamond": 48.4, "Ascendant": 48.9, "Immortal": 48.2, "Radiant": 57.6 } },
            "Bind": { winRate: 48.9, pickRate: 5.7, attackWR: 47.6, defenseWR: 50.2,
                rankWinRates: { "Silver": 49.1, "Gold": 49.0, "Platinum": 49.3, "Diamond": 48.5, "Ascendant": 49.0, "Immortal": 48.4, "Radiant": 57.7 } },
            "Haven": { winRate: 49.3, pickRate: 5.8, attackWR: 49.0, defenseWR: 49.6,
                rankWinRates: { "Silver": 49.5, "Gold": 49.4, "Platinum": 49.7, "Diamond": 48.9, "Ascendant": 49.4, "Immortal": 48.8, "Radiant": 58.1 } },
            "Split": { winRate: 49.2, pickRate: 5.8, attackWR: 48.2, defenseWR: 50.2,
                rankWinRates: { "Silver": 49.4, "Gold": 49.3, "Platinum": 49.6, "Diamond": 48.8, "Ascendant": 49.3, "Immortal": 48.7, "Radiant": 58.0 } },
            "Lotus": { winRate: 49.5, pickRate: 5.9, attackWR: 50.0, defenseWR: 49.0,
                rankWinRates: { "Silver": 49.7, "Gold": 49.6, "Platinum": 49.9, "Diamond": 49.1, "Ascendant": 49.6, "Immortal": 49.0, "Radiant": 58.3 } },
            "Sunset": { winRate: 48.6, pickRate: 5.6, attackWR: 47.8, defenseWR: 49.4,
                rankWinRates: { "Silver": 48.8, "Gold": 48.7, "Platinum": 49.0, "Diamond": 48.2, "Ascendant": 48.7, "Immortal": 48.1, "Radiant": 57.4 } },
            "Icebox": { winRate: 48.7, pickRate: 5.7, attackWR: 48.7, defenseWR: 48.8,
                rankWinRates: { "Silver": 48.9, "Gold": 48.8, "Platinum": 49.1, "Diamond": 48.3, "Ascendant": 48.8, "Immortal": 48.2, "Radiant": 57.5 } }
        },
        ranks: {
            "Silver": { winRate: 49.36, pickRate: 15.51 },
            "Gold": { winRate: 49.21, pickRate: 15.03 },
            "Platinum": { winRate: 49.48, pickRate: 14.28 },
            "Diamond": { winRate: 48.71, pickRate: 13.86 },
            "Ascendant": { winRate: 49.22, pickRate: 17.19 },
            "Immortal": { winRate: 48.57, pickRate: 10.19 },
            "Radiant": { winRate: 57.89, pickRate: 8.01 }
        },
        analysis: {
            strengths: ["烟雾控制", "战术多样性", "高选取率"],
            weaknesses: ["胜率偏低", "战术待优化"],
            playstyle: "新晋控场者，拥有独特的烟雾机制。高选取率说明玩家喜爱，但需要更好的战术配合来提升胜率。"
        }
    },
    "Yoru": {
        role: "Duelist",
        overall: { winRate: 46.93, pickRate: 4.5, kd: 0.97, matches: 19000 },
        maps: {
            "Ascent": { winRate: 47.1, pickRate: 0.7, attackWR: 47.1, defenseWR: 47.1,
                rankWinRates: { "Silver": 46.6, "Gold": 46.2, "Platinum": 46.6, "Diamond": 45.8, "Ascendant": 46.8, "Immortal": 49.2, "Radiant": 51.9 } },
            "Bind": { winRate: 46.9, pickRate: 0.6, attackWR: 46.9, defenseWR: 46.9,
                rankWinRates: { "Silver": 46.4, "Gold": 46.0, "Platinum": 46.4, "Diamond": 45.6, "Ascendant": 46.5, "Immortal": 49.0, "Radiant": 51.7 } },
            "Haven": { winRate: 46.6, pickRate: 0.6, attackWR: 47.8, defenseWR: 45.4,
                rankWinRates: { "Silver": 46.1, "Gold": 45.7, "Platinum": 46.1, "Diamond": 45.3, "Ascendant": 46.2, "Immortal": 48.7, "Radiant": 51.4 } },
            "Split": { winRate: 47.3, pickRate: 0.8, attackWR: 47.6, defenseWR: 47.0,
                rankWinRates: { "Silver": 46.8, "Gold": 46.4, "Platinum": 46.8, "Diamond": 46.0, "Ascendant": 46.9, "Immortal": 49.4, "Radiant": 52.1 } },
            "Lotus": { winRate: 46.7, pickRate: 0.6, attackWR: 48.9, defenseWR: 44.5,
                rankWinRates: { "Silver": 46.2, "Gold": 45.8, "Platinum": 46.2, "Diamond": 45.4, "Ascendant": 46.4, "Immortal": 48.8, "Radiant": 51.5 } },
            "Sunset": { winRate: 46.3, pickRate: 0.5, attackWR: 46.9, defenseWR: 45.7,
                rankWinRates: { "Silver": 45.8, "Gold": 45.4, "Platinum": 45.8, "Diamond": 45.0, "Ascendant": 45.9, "Immortal": 48.4, "Radiant": 51.1 } },
            "Icebox": { winRate: 46.5, pickRate: 0.6, attackWR: 48.0, defenseWR: 45.0,
                rankWinRates: { "Silver": 46.0, "Gold": 45.6, "Platinum": 46.0, "Diamond": 45.2, "Ascendant": 46.1, "Immortal": 48.6, "Radiant": 51.3 } }
        },
        ranks: {
            "Silver": { winRate: 46.42, pickRate: 1.68 },
            "Gold": { winRate: 46.04, pickRate: 1.62 },
            "Platinum": { winRate: 46.44, pickRate: 1.49 },
            "Diamond": { winRate: 45.66, pickRate: 1.36 },
            "Ascendant": { winRate: 46.58, pickRate: 1.35 },
            "Immortal": { winRate: 48.99, pickRate: 1.16 },
            "Radiant": { winRate: 51.72, pickRate: 4.0 }
        },
        analysis: {
            strengths: ["传送潜入", "闪光技能", "大招隐身"],
            weaknesses: ["胜率最低", "高风险高回报"],
            playstyle: "潜入型决斗者，利用传送和隐身进行侧翼包抄。适合有创意的玩家，可以打乱敌人防守节奏。"
        }
    },
    "Tejo": {
        role: "Initiator",
        overall: { winRate: 49.42, pickRate: 9.0, kd: 0.94, matches: 38000 },
        maps: {
            "Ascent": { winRate: 49.2, pickRate: 1.2, attackWR: 48.2, defenseWR: 50.2,
                rankWinRates: { "Silver": 48.8, "Gold": 49.0, "Platinum": 49.2, "Diamond": 49.8, "Ascendant": 49.5, "Immortal": 48.2, "Radiant": 63.4 } },
            "Bind": { winRate: 49.7, pickRate: 1.4, attackWR: 48.7, defenseWR: 50.7,
                rankWinRates: { "Silver": 49.3, "Gold": 49.5, "Platinum": 49.7, "Diamond": 50.3, "Ascendant": 50.0, "Immortal": 48.8, "Radiant": 63.9 } },
            "Haven": { winRate: 49.3, pickRate: 1.3, attackWR: 49.3, defenseWR: 49.3,
                rankWinRates: { "Silver": 48.9, "Gold": 49.1, "Platinum": 49.3, "Diamond": 49.9, "Ascendant": 49.6, "Immortal": 48.3, "Radiant": 63.5 } },
            "Split": { winRate: 49.6, pickRate: 1.3, attackWR: 48.9, defenseWR: 50.4,
                rankWinRates: { "Silver": 49.2, "Gold": 49.4, "Platinum": 49.6, "Diamond": 50.2, "Ascendant": 49.9, "Immortal": 48.6, "Radiant": 63.8 } },
            "Lotus": { winRate: 49.5, pickRate: 1.3, attackWR: 50.3, defenseWR: 48.7,
                rankWinRates: { "Silver": 49.1, "Gold": 49.3, "Platinum": 49.5, "Diamond": 50.1, "Ascendant": 49.8, "Immortal": 48.5, "Radiant": 63.7 } },
            "Sunset": { winRate: 49.0, pickRate: 1.2, attackWR: 48.5, defenseWR: 49.5,
                rankWinRates: { "Silver": 48.6, "Gold": 48.8, "Platinum": 49.0, "Diamond": 49.6, "Ascendant": 49.3, "Immortal": 48.0, "Radiant": 63.2 } },
            "Icebox": { winRate: 49.1, pickRate: 1.2, attackWR: 49.4, defenseWR: 48.9,
                rankWinRates: { "Silver": 48.7, "Gold": 48.9, "Platinum": 49.1, "Diamond": 49.7, "Ascendant": 49.4, "Immortal": 48.1, "Radiant": 63.3 } }
        },
        ranks: {
            "Silver": { winRate: 49.02, pickRate: 4.33 },
            "Gold": { winRate: 49.18, pickRate: 3.96 },
            "Platinum": { winRate: 49.41, pickRate: 3.92 },
            "Diamond": { winRate: 49.99, pickRate: 4.37 },
            "Ascendant": { winRate: 49.7, pickRate: 4.14 },
            "Immortal": { winRate: 48.47, pickRate: 3.82 },
            "Radiant": { winRate: 63.64, pickRate: 1.52 }
        },
        analysis: {
            strengths: ["信息收集", "战术支持", "技能组合灵活"],
            weaknesses: ["胜率偏低", "战术未成熟"],
            playstyle: "新晋先锋，技能机制独特。需要更多实战数据来验证最佳使用方式。"
        }
    },
    "Harbor": {
        role: "Controller",
        overall: { winRate: 47.02, pickRate: 2.5, kd: 0.93, matches: 10500 },
        maps: {
            "Ascent": { winRate: 46.7, pickRate: 0.3, attackWR: 45.4, defenseWR: 48.0,
                rankWinRates: { "Silver": 46.2, "Gold": 45.6, "Platinum": 45.6, "Diamond": 42.7, "Ascendant": 44.8, "Immortal": 34.5, "Radiant": 47.4 } },
            "Bind": { winRate: 47.2, pickRate: 0.4, attackWR: 45.9, defenseWR: 48.5,
                rankWinRates: { "Silver": 46.8, "Gold": 46.1, "Platinum": 46.1, "Diamond": 43.2, "Ascendant": 45.3, "Immortal": 35.0, "Radiant": 47.9 } },
            "Haven": { winRate: 47.1, pickRate: 0.4, attackWR: 46.8, defenseWR: 47.4,
                rankWinRates: { "Silver": 46.6, "Gold": 46.0, "Platinum": 46.0, "Diamond": 43.1, "Ascendant": 45.2, "Immortal": 34.9, "Radiant": 47.8 } },
            "Split": { winRate: 46.8, pickRate: 0.3, attackWR: 45.8, defenseWR: 47.8,
                rankWinRates: { "Silver": 46.3, "Gold": 45.7, "Platinum": 45.7, "Diamond": 42.8, "Ascendant": 44.9, "Immortal": 34.6, "Radiant": 47.5 } },
            "Lotus": { winRate: 47.4, pickRate: 0.5, attackWR: 47.9, defenseWR: 46.9,
                rankWinRates: { "Silver": 46.9, "Gold": 46.3, "Platinum": 46.3, "Diamond": 43.4, "Ascendant": 45.5, "Immortal": 35.2, "Radiant": 48.1 } },
            "Sunset": { winRate: 46.5, pickRate: 0.3, attackWR: 45.7, defenseWR: 47.3,
                rankWinRates: { "Silver": 46.0, "Gold": 45.4, "Platinum": 45.4, "Diamond": 42.5, "Ascendant": 44.6, "Immortal": 34.3, "Radiant": 47.2 } },
            "Icebox": { winRate: 46.6, pickRate: 0.3, attackWR: 46.6, defenseWR: 46.6,
                rankWinRates: { "Silver": 46.1, "Gold": 45.5, "Platinum": 45.5, "Diamond": 42.6, "Ascendant": 44.7, "Immortal": 34.4, "Radiant": 47.3 } }
        },
        ranks: {
            "Silver": { winRate: 46.57, pickRate: 0.99 },
            "Gold": { winRate: 45.92, pickRate: 0.95 },
            "Platinum": { winRate: 45.93, pickRate: 0.82 },
            "Diamond": { winRate: 43.02, pickRate: 0.68 },
            "Ascendant": { winRate: 45.1, pickRate: 0.65 },
            "Immortal": { winRate: 34.83, pickRate: 0.42 },
            "Radiant": { winRate: 47.7, pickRate: 0.3 }
        },
        analysis: {
            strengths: ["水幕掩护", "区域控制", "大招范围伤害"],
            weaknesses: ["水幕可被穿透", "胜率偏低"],
            playstyle: "水幕型控场者，利用水墙为团队提供掩护。大招可以封锁大片区域，适合进攻方使用。"
        }
    },
    "Waylay": {
        role: "Duelist",
        overall: { winRate: 48.42, pickRate: 10.0, kd: 1.0, matches: 42200 },
        maps: {
            "Ascent": { winRate: 48.6, pickRate: 1.5, attackWR: 48.6, defenseWR: 48.6,
                rankWinRates: { "Silver": 48.1, "Gold": 48.1, "Platinum": 48.9, "Diamond": 48.1, "Ascendant": 48.4, "Immortal": 45.8, "Radiant": 44.6 } },
            "Bind": { winRate: 48.4, pickRate: 1.4, attackWR: 48.4, defenseWR: 48.4,
                rankWinRates: { "Silver": 47.9, "Gold": 47.9, "Platinum": 48.7, "Diamond": 47.9, "Ascendant": 48.2, "Immortal": 45.6, "Radiant": 44.4 } },
            "Haven": { winRate: 48.1, pickRate: 1.3, attackWR: 49.3, defenseWR: 46.9,
                rankWinRates: { "Silver": 47.6, "Gold": 47.6, "Platinum": 48.4, "Diamond": 47.6, "Ascendant": 47.9, "Immortal": 45.3, "Radiant": 44.1 } },
            "Split": { winRate: 48.8, pickRate: 1.5, attackWR: 49.1, defenseWR: 48.5,
                rankWinRates: { "Silver": 48.3, "Gold": 48.3, "Platinum": 49.1, "Diamond": 48.3, "Ascendant": 48.6, "Immortal": 46.0, "Radiant": 44.8 } },
            "Lotus": { winRate: 48.2, pickRate: 1.4, attackWR: 50.4, defenseWR: 46.0,
                rankWinRates: { "Silver": 47.7, "Gold": 47.8, "Platinum": 48.5, "Diamond": 47.7, "Ascendant": 48.0, "Immortal": 45.4, "Radiant": 44.2 } },
            "Sunset": { winRate: 47.8, pickRate: 1.2, attackWR: 48.4, defenseWR: 47.2,
                rankWinRates: { "Silver": 47.3, "Gold": 47.3, "Platinum": 48.1, "Diamond": 47.3, "Ascendant": 47.6, "Immortal": 45.0, "Radiant": 43.8 } },
            "Icebox": { winRate: 48.0, pickRate: 1.4, attackWR: 49.5, defenseWR: 46.5,
                rankWinRates: { "Silver": 47.5, "Gold": 47.5, "Platinum": 48.3, "Diamond": 47.5, "Ascendant": 47.8, "Immortal": 45.2, "Radiant": 44.0 } }
        },
        ranks: {
            "Silver": { winRate: 47.89, pickRate: 2.52 },
            "Gold": { winRate: 47.97, pickRate: 2.58 },
            "Platinum": { winRate: 48.7, pickRate: 2.73 },
            "Diamond": { winRate: 47.89, pickRate: 2.73 },
            "Ascendant": { winRate: 48.18, pickRate: 3.41 },
            "Immortal": { winRate: 45.6, pickRate: 2.62 },
            "Radiant": { winRate: 44.44, pickRate: 2.48 }
        },
        analysis: {
            strengths: ["独特技能", "突破潜力", "高机动性"],
            weaknesses: ["胜率偏低", "战术待开发"],
            playstyle: "新晋决斗者，拥有独特的技能机制。目前还在探索阶段，建议多练习找到最佳打法。"
        }
    },
    "Raze": {
        role: "Duelist",
        overall: { winRate: 50.52, pickRate: 21.0, kd: 1.03, matches: 88600 },
        maps: {
            "Ascent": { winRate: 50.1, pickRate: 2.9, attackWR: 50.1, defenseWR: 50.1,
                rankWinRates: { "Silver": 48.9, "Gold": 49.4, "Platinum": 49.2, "Diamond": 48.6, "Ascendant": 49.7, "Immortal": 49.4, "Radiant": 29.9 } },
            "Bind": { winRate: 51.0, pickRate: 3.1, attackWR: 51.0, defenseWR: 51.0,
                rankWinRates: { "Silver": 49.8, "Gold": 50.2, "Platinum": 50.1, "Diamond": 49.5, "Ascendant": 50.6, "Immortal": 50.3, "Radiant": 30.8 } },
            "Haven": { winRate: 50.4, pickRate: 3.0, attackWR: 51.6, defenseWR: 49.2,
                rankWinRates: { "Silver": 49.2, "Gold": 49.6, "Platinum": 49.5, "Diamond": 48.9, "Ascendant": 50.0, "Immortal": 49.7, "Radiant": 30.2 } },
            "Split": { winRate: 51.3, pickRate: 3.2, attackWR: 51.6, defenseWR: 51.0,
                rankWinRates: { "Silver": 50.1, "Gold": 50.5, "Platinum": 50.4, "Diamond": 49.8, "Ascendant": 50.9, "Immortal": 50.6, "Radiant": 31.1 } },
            "Lotus": { winRate: 50.7, pickRate: 3.1, attackWR: 52.9, defenseWR: 48.5,
                rankWinRates: { "Silver": 49.5, "Gold": 50.0, "Platinum": 49.8, "Diamond": 49.2, "Ascendant": 50.3, "Immortal": 50.0, "Radiant": 30.5 } },
            "Sunset": { winRate: 49.8, pickRate: 2.8, attackWR: 50.4, defenseWR: 49.2,
                rankWinRates: { "Silver": 48.6, "Gold": 49.0, "Platinum": 48.9, "Diamond": 48.3, "Ascendant": 49.4, "Immortal": 49.1, "Radiant": 29.6 } },
            "Icebox": { winRate: 50.0, pickRate: 2.9, attackWR: 51.5, defenseWR: 48.5,
                rankWinRates: { "Silver": 48.8, "Gold": 49.2, "Platinum": 49.1, "Diamond": 48.5, "Ascendant": 49.6, "Immortal": 49.3, "Radiant": 29.8 } }
        },
        ranks: {
            "Silver": { winRate: 49.34, pickRate: 6.42 },
            "Gold": { winRate: 49.77, pickRate: 6.72 },
            "Platinum": { winRate: 49.65, pickRate: 6.77 },
            "Diamond": { winRate: 48.98, pickRate: 6.39 },
            "Ascendant": { winRate: 50.09, pickRate: 6.33 },
            "Immortal": { winRate: 49.85, pickRate: 4.75 },
            "Radiant": { winRate: 30.3, pickRate: 4.69 }
        },
        analysis: {
            strengths: ["爆破伤害", "机动性", "大招清场"],
            weaknesses: ["技能可被躲避", "需要近战环境"],
            playstyle: "爆破型决斗者，利用手雷和火箭筒进行区域清理。适合在狭窄地图发挥，大招可以一击清场。"
        }
    },
    "KAY/O": {
        role: "Initiator",
        overall: { winRate: 47.02, pickRate: 8.0, kd: 0.9, matches: 33800 },
        maps: {
            "Ascent": { winRate: 47.1, pickRate: 1.2, attackWR: 46.1, defenseWR: 48.1,
                rankWinRates: { "Silver": 47.1, "Gold": 46.3, "Platinum": 47.2, "Diamond": 46.3, "Ascendant": 46.7, "Immortal": 49.0, "Radiant": 49.3 } },
            "Bind": { winRate: 47.2, pickRate: 1.2, attackWR: 46.2, defenseWR: 48.2,
                rankWinRates: { "Silver": 47.2, "Gold": 46.4, "Platinum": 47.3, "Diamond": 46.4, "Ascendant": 46.8, "Immortal": 49.1, "Radiant": 49.4 } },
            "Haven": { winRate: 46.8, pickRate: 1.1, attackWR: 46.8, defenseWR: 46.8,
                rankWinRates: { "Silver": 46.8, "Gold": 46.0, "Platinum": 46.9, "Diamond": 46.0, "Ascendant": 46.4, "Immortal": 48.7, "Radiant": 49.0 } },
            "Split": { winRate: 47.3, pickRate: 1.2, attackWR: 46.5, defenseWR: 48.0,
                rankWinRates: { "Silver": 47.3, "Gold": 46.5, "Platinum": 47.4, "Diamond": 46.5, "Ascendant": 46.9, "Immortal": 49.2, "Radiant": 49.5 } },
            "Lotus": { winRate: 46.9, pickRate: 1.1, attackWR: 47.7, defenseWR: 46.1,
                rankWinRates: { "Silver": 46.9, "Gold": 46.1, "Platinum": 47.0, "Diamond": 46.1, "Ascendant": 46.5, "Immortal": 48.8, "Radiant": 49.1 } },
            "Sunset": { winRate: 46.5, pickRate: 1.0, attackWR: 46.0, defenseWR: 47.0,
                rankWinRates: { "Silver": 46.5, "Gold": 45.7, "Platinum": 46.6, "Diamond": 45.7, "Ascendant": 46.1, "Immortal": 48.4, "Radiant": 48.7 } },
            "Icebox": { winRate: 46.7, pickRate: 1.1, attackWR: 47.0, defenseWR: 46.5,
                rankWinRates: { "Silver": 46.7, "Gold": 45.9, "Platinum": 46.8, "Diamond": 45.9, "Ascendant": 46.3, "Immortal": 48.6, "Radiant": 48.9 } }
        },
        ranks: {
            "Silver": { winRate: 47.03, pickRate: 3.22 },
            "Gold": { winRate: 46.26, pickRate: 2.96 },
            "Platinum": { winRate: 47.16, pickRate: 2.2 },
            "Diamond": { winRate: 46.26, pickRate: 1.43 },
            "Ascendant": { winRate: 46.59, pickRate: 1.78 },
            "Immortal": { winRate: 48.94, pickRate: 0.44 },
            "Radiant": { winRate: 49.2, pickRate: 0.2 }
        },
        analysis: {
            strengths: ["压制技能", "大招禁用", "闪光技能"],
            weaknesses: ["胜率偏低", "技能可被破坏"],
            playstyle: "压制型先锋，利用闪光和压制技能为团队创造优势。大招可以禁用敌人技能，在关键时刻非常有效。"
        }
    },
    "Breach": {
        role: "Initiator",
        overall: { winRate: 49.02, pickRate: 10.0, kd: 0.93, matches: 42200 },
        maps: {
            "Ascent": { winRate: 49.1, pickRate: 1.5, attackWR: 48.1, defenseWR: 50.1,
                rankWinRates: { "Silver": 49.0, "Gold": 48.8, "Platinum": 48.1, "Diamond": 46.0, "Ascendant": 48.2, "Immortal": 54.5, "Radiant": 49.2 } },
            "Bind": { winRate: 49.2, pickRate: 1.5, attackWR: 48.2, defenseWR: 50.2,
                rankWinRates: { "Silver": 49.1, "Gold": 48.9, "Platinum": 48.2, "Diamond": 46.1, "Ascendant": 48.3, "Immortal": 54.6, "Radiant": 49.4 } },
            "Haven": { winRate: 48.8, pickRate: 1.4, attackWR: 48.8, defenseWR: 48.8,
                rankWinRates: { "Silver": 48.7, "Gold": 48.5, "Platinum": 47.8, "Diamond": 45.7, "Ascendant": 47.9, "Immortal": 54.2, "Radiant": 48.6 } },
            "Split": { winRate: 49.4, pickRate: 1.5, attackWR: 48.6, defenseWR: 50.1,
                rankWinRates: { "Silver": 49.3, "Gold": 49.1, "Platinum": 48.4, "Diamond": 46.3, "Ascendant": 48.5, "Immortal": 54.8, "Radiant": 49.8 } },
            "Lotus": { winRate: 48.9, pickRate: 1.4, attackWR: 49.7, defenseWR: 48.1,
                rankWinRates: { "Silver": 48.8, "Gold": 48.6, "Platinum": 47.9, "Diamond": 45.8, "Ascendant": 48.0, "Immortal": 54.3, "Radiant": 48.8 } },
            "Sunset": { winRate: 48.5, pickRate: 1.3, attackWR: 48.0, defenseWR: 49.0,
                rankWinRates: { "Silver": 48.4, "Gold": 48.2, "Platinum": 47.5, "Diamond": 45.4, "Ascendant": 47.6, "Immortal": 53.9, "Radiant": 48.0 } },
            "Icebox": { winRate: 48.7, pickRate: 1.3, attackWR: 49.0, defenseWR: 48.5,
                rankWinRates: { "Silver": 48.6, "Gold": 48.4, "Platinum": 47.7, "Diamond": 45.6, "Ascendant": 47.8, "Immortal": 54.1, "Radiant": 48.4 } }
        },
        ranks: {
            "Silver": { winRate: 48.93, pickRate: 1.68 },
            "Gold": { winRate: 48.68, pickRate: 1.77 },
            "Platinum": { winRate: 47.99, pickRate: 1.64 },
            "Diamond": { winRate: 45.97, pickRate: 1.49 },
            "Ascendant": { winRate: 48.15, pickRate: 1.56 },
            "Immortal": { winRate: 54.4, pickRate: 0.9 },
            "Radiant": { winRate: 49.02, pickRate: 0.41 }
        },
        analysis: {
            strengths: ["眩晕技能", "穿墙闪光", "大招群体控制"],
            weaknesses: ["选取率偏低", "需要配合"],
            playstyle: "眩晕型先锋，利用闪光和眩晕为团队创造优势。技能可以穿墙释放，适合在狭窄地图使用。"
        }
    }
};

const mapNames = {
    "Ascent": "亚海悬城", "Bind": "源工重镇", "Haven": "隐世修所", "Split": "霓虹町",
    "Lotus": "莲华古城", "Sunset": "日落之城", "Breeze": "微风岛屿", "Icebox": "森寒冬港"
};

const roleNames = { "Duelist": "决斗者", "Initiator": "先锋", "Controller": "控场者", "Sentinel": "守卫" };
const roleColors = { "Duelist": "#ff4655", "Initiator": "#4a9eff", "Controller": "#9c27b0", "Sentinel": "#4caf50" };

const rankNames = { "Silver": "白银", "Gold": "黄金", "Platinum": "铂金", "Diamond": "钻石", "Ascendant": "超凡", "Immortal": "神话", "Radiant": "辐能" };
const rankIcons = {
    "Silver": "https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/10/smallicon.png",
    "Gold": "https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/13/smallicon.png",
    "Platinum": "https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/16/smallicon.png",
    "Diamond": "https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/19/smallicon.png",
    "Ascendant": "https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/22/smallicon.png",
    "Immortal": "https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/25/smallicon.png",
    "Radiant": "https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/27/smallicon.png"
};
const rankColors = {
    "Silver": "#94a3b8", "Gold": "#fbbf24", "Platinum": "#60a5fa", "Diamond": "#a78bfa",
    "Ascendant": "#34d399", "Immortal": "#f87171", "Radiant": "#fbbf24"
};

function getTier(winRate) {
    if (winRate >= 53) return { tier: "S", class: "tier-s" };
    if (winRate >= 51) return { tier: "A", class: "tier-a" };
    if (winRate >= 49) return { tier: "B", class: "tier-b" };
    return { tier: "C", class: "tier-c" };
}

function getBestMaps(agentData, count = 3) {
    return Object.entries(agentData.maps).sort((a, b) => b[1].winRate - a[1].winRate).slice(0, count).map(([map, data]) => ({ map, ...data }));
}

function getAvoidMaps(agentData, count = 3) {
    return Object.entries(agentData.maps).sort((a, b) => a[1].winRate - b[1].winRate).slice(0, count).map(([map, data]) => ({ map, ...data }));
}

function getBestRank(agentData) {
    return Object.entries(agentData.ranks).sort((a, b) => b[1].winRate - a[1].winRate)[0];
}

function getRankSuggestion(agentData) {
    const ranks = Object.entries(agentData.ranks);
    const bestRank = ranks.sort((a, b) => b[1].winRate - a[1].winRate)[0];
    const worstRank = ranks.sort((a, b) => a[1].winRate - b[1].winRate)[0];
    return { best: { rank: bestRank[0], ...bestRank[1] }, worst: { rank: worstRank[0], ...worstRank[1] }, trend: bestRank[1].winRate - worstRank[1].winRate };
}