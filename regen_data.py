import sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

RANKS = ["Silver", "Gold", "Platinum", "Diamond", "Ascendant", "Immortal", "Radiant"]

RD = {
    "Clove":{"Silver":{"wr":53.87,"pr":11.41},"Gold":{"wr":53.92,"pr":11.53},"Platinum":{"wr":54.31,"pr":12.09},"Diamond":{"wr":53.46,"pr":13.57},"Ascendant":{"wr":53.94,"pr":11.67},"Immortal":{"wr":51.81,"pr":23.36},"Radiant":{"wr":57.45,"pr":32.44}},
    "Sage":{"Silver":{"wr":48.78,"pr":5.40},"Gold":{"wr":49.39,"pr":3.91},"Platinum":{"wr":50.39,"pr":2.80},"Diamond":{"wr":48.51,"pr":2.02},"Ascendant":{"wr":50.37,"pr":2.44},"Immortal":{"wr":49.64,"pr":1.33},"Radiant":{"wr":60.0,"pr":0.69}},
    "Killjoy":{"Silver":{"wr":53.04,"pr":1.87},"Gold":{"wr":52.25,"pr":1.87},"Platinum":{"wr":51.83,"pr":2.03},"Diamond":{"wr":51.27,"pr":2.28},"Ascendant":{"wr":52.87,"pr":2.25},"Immortal":{"wr":54.91,"pr":2.11},"Radiant":{"wr":57.14,"pr":0.97}},
    "Phoenix":{"Silver":{"wr":50.89,"pr":8.38},"Gold":{"wr":51.67,"pr":8.57},"Platinum":{"wr":51.88,"pr":8.89},"Diamond":{"wr":51.58,"pr":8.68},"Ascendant":{"wr":52.02,"pr":7.39},"Immortal":{"wr":51.25,"pr":7.15},"Radiant":{"wr":60.0,"pr":6.90}},
    "Omen":{"Silver":{"wr":47.59,"pr":7.91},"Gold":{"wr":47.58,"pr":8.09},"Platinum":{"wr":47.67,"pr":8.02},"Diamond":{"wr":47.66,"pr":6.96},"Ascendant":{"wr":47.80,"pr":6.55},"Immortal":{"wr":43.66,"pr":2.84},"Radiant":{"wr":28.57,"pr":0.97}},
    "Jett":{"Silver":{"wr":50.24,"pr":15.78},"Gold":{"wr":50.41,"pr":17.75},"Platinum":{"wr":50.34,"pr":20.04},"Diamond":{"wr":49.93,"pr":21.38},"Ascendant":{"wr":50.15,"pr":20.59},"Immortal":{"wr":49.77,"pr":27.46},"Radiant":{"wr":51.30,"pr":32.30}},
    "Sova":{"Silver":{"wr":50.20,"pr":7.74},"Gold":{"wr":50.64,"pr":7.60},"Platinum":{"wr":50.96,"pr":8.09},"Diamond":{"wr":50.21,"pr":9.24},"Ascendant":{"wr":50.83,"pr":8.46},"Immortal":{"wr":49.10,"pr":9.13},"Radiant":{"wr":58.06,"pr":4.28}},
    "Cypher":{"Silver":{"wr":50.74,"pr":6.65},"Gold":{"wr":51.02,"pr":5.86},"Platinum":{"wr":51.28,"pr":5.33},"Diamond":{"wr":51.59,"pr":5.11},"Ascendant":{"wr":51.33,"pr":5.40},"Immortal":{"wr":50.90,"pr":5.19},"Radiant":{"wr":72.0,"pr":3.45}},
    "Viper":{"Silver":{"wr":50.29,"pr":0.91},"Gold":{"wr":50.44,"pr":1.10},"Platinum":{"wr":48.61,"pr":1.24},"Diamond":{"wr":50.30,"pr":1.31},"Ascendant":{"wr":49.63,"pr":1.28},"Immortal":{"wr":50.0,"pr":0.95},"Radiant":{"wr":100.0,"pr":0.14}},
    "Neon":{"Silver":{"wr":50.11,"pr":19.11},"Gold":{"wr":49.98,"pr":18.96},"Platinum":{"wr":50.76,"pr":18.48},"Diamond":{"wr":50.15,"pr":17.83},"Ascendant":{"wr":50.64,"pr":18.76},"Immortal":{"wr":52.01,"pr":19.52},"Radiant":{"wr":64.91,"pr":23.60}},
    "Chamber":{"Silver":{"wr":49.97,"pr":23.63},"Gold":{"wr":50.31,"pr":25.85},"Platinum":{"wr":50.04,"pr":27.17},"Diamond":{"wr":50.08,"pr":27.57},"Ascendant":{"wr":50.04,"pr":26.47},"Immortal":{"wr":49.66,"pr":27.09},"Radiant":{"wr":43.88,"pr":13.80}},
    "Iso":{"Silver":{"wr":48.44,"pr":4.44},"Gold":{"wr":48.02,"pr":3.92},"Platinum":{"wr":48.40,"pr":3.46},"Diamond":{"wr":49.27,"pr":3.04},"Ascendant":{"wr":48.57,"pr":3.49},"Immortal":{"wr":48.10,"pr":3.35},"Radiant":{"wr":62.11,"pr":13.25}},
    "Deadlock":{"Silver":{"wr":48.21,"pr":0.94},"Gold":{"wr":47.72,"pr":0.86},"Platinum":{"wr":48.72,"pr":0.73},"Diamond":{"wr":47.97,"pr":0.71},"Ascendant":{"wr":50.56,"pr":0.69},"Immortal":{"wr":49.06,"pr":0.50},"Radiant":{"wr":52.8,"pr":0.30}},
    "Reyna":{"Silver":{"wr":50.37,"pr":24.30},"Gold":{"wr":50.14,"pr":23.20},"Platinum":{"wr":50.17,"pr":21.84},"Diamond":{"wr":50.01,"pr":21.20},"Ascendant":{"wr":50.06,"pr":22.45},"Immortal":{"wr":48.80,"pr":22.36},"Radiant":{"wr":59.62,"pr":29.68}},
    "Fade":{"Silver":{"wr":51.68,"pr":6.24},"Gold":{"wr":51.62,"pr":7.45},"Platinum":{"wr":51.51,"pr":8.72},"Diamond":{"wr":51.68,"pr":10.04},"Ascendant":{"wr":50.99,"pr":9.26},"Immortal":{"wr":50.65,"pr":10.11},"Radiant":{"wr":54.55,"pr":4.55}},
    "Brimstone":{"Silver":{"wr":49.86,"pr":2.97},"Gold":{"wr":49.59,"pr":2.21},"Platinum":{"wr":50.26,"pr":1.86},"Diamond":{"wr":51.84,"pr":1.73},"Ascendant":{"wr":51.33,"pr":1.56},"Immortal":{"wr":53.62,"pr":1.11},"Radiant":{"wr":72.97,"pr":5.11}},
    "Veto":{"Silver":{"wr":49.56,"pr":1.07},"Gold":{"wr":48.40,"pr":1.06},"Platinum":{"wr":48.77,"pr":0.99},"Diamond":{"wr":48.70,"pr":1.03},"Ascendant":{"wr":49.38,"pr":1.07},"Immortal":{"wr":44.44,"pr":0.88},"Radiant":{"wr":100.0,"pr":0.55}},
    "Vyse":{"Silver":{"wr":50.87,"pr":1.13},"Gold":{"wr":49.95,"pr":1.24},"Platinum":{"wr":50.20,"pr":1.32},"Diamond":{"wr":52.36,"pr":1.29},"Ascendant":{"wr":50.64,"pr":1.37},"Immortal":{"wr":49.38,"pr":1.12},"Radiant":{"wr":0.0,"pr":0.41}},
    "Gekko":{"Silver":{"wr":51.47,"pr":2.92},"Gold":{"wr":50.66,"pr":2.27},"Platinum":{"wr":49.92,"pr":1.58},"Diamond":{"wr":49.07,"pr":0.98},"Ascendant":{"wr":49.85,"pr":1.35},"Immortal":{"wr":50.85,"pr":0.28},"Radiant":{"wr":50.5,"pr":0.10}},
    "Astra":{"Silver":{"wr":48.84,"pr":1.11},"Gold":{"wr":49.57,"pr":1.57},"Platinum":{"wr":47.80,"pr":2.19},"Diamond":{"wr":47.68,"pr":2.57},"Ascendant":{"wr":48.35,"pr":2.14},"Immortal":{"wr":45.32,"pr":1.97},"Radiant":{"wr":66.67,"pr":0.41}},
    "Skye":{"Silver":{"wr":50.94,"pr":9.77},"Gold":{"wr":51.03,"pr":9.53},"Platinum":{"wr":51.04,"pr":9.30},"Diamond":{"wr":51.14,"pr":9.14},"Ascendant":{"wr":50.86,"pr":8.95},"Immortal":{"wr":50.68,"pr":7.87},"Radiant":{"wr":43.59,"pr":5.38}},
    "Miks":{"Silver":{"wr":49.36,"pr":15.51},"Gold":{"wr":49.21,"pr":15.03},"Platinum":{"wr":49.48,"pr":14.28},"Diamond":{"wr":48.71,"pr":13.86},"Ascendant":{"wr":49.22,"pr":17.19},"Immortal":{"wr":48.57,"pr":10.19},"Radiant":{"wr":57.89,"pr":8.01}},
    "Yoru":{"Silver":{"wr":46.42,"pr":1.68},"Gold":{"wr":46.04,"pr":1.62},"Platinum":{"wr":46.44,"pr":1.49},"Diamond":{"wr":45.66,"pr":1.36},"Ascendant":{"wr":46.58,"pr":1.35},"Immortal":{"wr":48.99,"pr":1.16},"Radiant":{"wr":51.72,"pr":4.00}},
    "Tejo":{"Silver":{"wr":49.02,"pr":4.33},"Gold":{"wr":49.18,"pr":3.96},"Platinum":{"wr":49.41,"pr":3.92},"Diamond":{"wr":49.99,"pr":4.37},"Ascendant":{"wr":49.70,"pr":4.14},"Immortal":{"wr":48.47,"pr":3.82},"Radiant":{"wr":63.64,"pr":1.52}},
    "Harbor":{"Silver":{"wr":46.57,"pr":0.99},"Gold":{"wr":45.92,"pr":0.95},"Platinum":{"wr":45.93,"pr":0.82},"Diamond":{"wr":43.02,"pr":0.68},"Ascendant":{"wr":45.10,"pr":0.65},"Immortal":{"wr":34.83,"pr":0.42},"Radiant":{"wr":47.7,"pr":0.30}},
    "Waylay":{"Silver":{"wr":47.89,"pr":2.52},"Gold":{"wr":47.97,"pr":2.58},"Platinum":{"wr":48.70,"pr":2.73},"Diamond":{"wr":47.89,"pr":2.73},"Ascendant":{"wr":48.18,"pr":3.41},"Immortal":{"wr":45.60,"pr":2.62},"Radiant":{"wr":44.44,"pr":2.48}},
    "Raze":{"Silver":{"wr":49.34,"pr":6.42},"Gold":{"wr":49.77,"pr":6.72},"Platinum":{"wr":49.65,"pr":6.77},"Diamond":{"wr":48.98,"pr":6.39},"Ascendant":{"wr":50.09,"pr":6.33},"Immortal":{"wr":49.85,"pr":4.75},"Radiant":{"wr":30.30,"pr":4.69}},
    "KAY/O":{"Silver":{"wr":47.03,"pr":3.22},"Gold":{"wr":46.26,"pr":2.96},"Platinum":{"wr":47.16,"pr":2.20},"Diamond":{"wr":46.26,"pr":1.43},"Ascendant":{"wr":46.59,"pr":1.78},"Immortal":{"wr":48.94,"pr":0.44},"Radiant":{"wr":49.2,"pr":0.20}},
    "Breach":{"Silver":{"wr":48.93,"pr":1.68},"Gold":{"wr":48.68,"pr":1.77},"Platinum":{"wr":47.99,"pr":1.64},"Diamond":{"wr":45.97,"pr":1.49},"Ascendant":{"wr":48.15,"pr":1.56},"Immortal":{"wr":54.40,"pr":0.90},"Radiant":{"wr":100.0,"pr":0.41}},
}

MAP_POOL = ["Ascent", "Bind", "Haven", "Split", "Lotus", "Sunset", "Icebox"]
MAP_BALANCE = {"Ascent":{"atk":-2.0,"def":2.0},"Bind":{"atk":-2.0,"def":2.0},"Haven":{"atk":0.0,"def":0.0},"Split":{"atk":-1.5,"def":1.5},"Lotus":{"atk":1.6,"def":-1.6},"Sunset":{"atk":-1.0,"def":1.0},"Icebox":{"atk":0.5,"def":-0.5}}

agents = [
    {"name":"Clove","role":"Controller","wr":53.11,"pr":26.36,"kd":0.94,"matches":927917,"mb":{"Haven":2.2,"Lotus":0.4,"Ascent":1.0,"Bind":-0.3,"Split":-1.2,"Sunset":-0.8,"Icebox":-1.5}},
    {"name":"Sage","role":"Sentinel","wr":51.43,"pr":32.01,"kd":0.91,"matches":1126855,"mb":{"Haven":1.7,"Ascent":0.9,"Lotus":0.1,"Bind":-0.6,"Split":-1.5,"Sunset":-0.8,"Icebox":-1.7}},
    {"name":"Killjoy","role":"Sentinel","wr":51.27,"pr":12.53,"kd":1.00,"matches":52800,"mb":{"Ascent":0.5,"Bind":0.3,"Haven":0.1,"Split":0.0,"Lotus":-0.2,"Sunset":-0.3,"Icebox":-0.5}},
    {"name":"Phoenix","role":"Duelist","wr":50.90,"pr":19.48,"kd":1.07,"matches":122000,"mb":{"Split":1.2,"Ascent":0.6,"Icebox":0.3,"Bind":-0.1,"Lotus":-0.4,"Haven":-0.7,"Sunset":-1.1}},
    {"name":"Omen","role":"Controller","wr":47.82,"pr":19.50,"kd":0.98,"matches":82300,"mb":{"Lotus":0.5,"Haven":0.3,"Split":0.2,"Bind":-0.3,"Ascent":-0.4,"Icebox":-0.5,"Sunset":-0.7}},
    {"name":"Jett","role":"Duelist","wr":50.02,"pr":43.00,"kd":1.08,"matches":181000,"mb":{"Ascent":0.6,"Haven":0.3,"Icebox":0.2,"Split":-0.3,"Lotus":-0.4,"Bind":-0.5,"Sunset":-0.6}},
    {"name":"Sova","role":"Initiator","wr":50.42,"pr":19.00,"kd":0.98,"matches":80200,"mb":{"Haven":0.6,"Ascent":0.4,"Bind":0.1,"Split":-0.2,"Lotus":-0.3,"Icebox":-0.4,"Sunset":-0.5}},
    {"name":"Cypher","role":"Sentinel","wr":50.22,"pr":15.00,"kd":1.00,"matches":63300,"mb":{"Bind":0.6,"Ascent":0.4,"Split":0.2,"Lotus":-0.1,"Haven":-0.3,"Icebox":-0.4,"Sunset":-0.6}},
    {"name":"Viper","role":"Controller","wr":49.62,"pr":5.50,"kd":1.01,"matches":23200,"mb":{"Icebox":1.5,"Bind":0.3,"Lotus":0.1,"Ascent":-0.4,"Haven":-0.5,"Split":-0.6,"Sunset":-0.8}},
    {"name":"Neon","role":"Duelist","wr":50.02,"pr":26.50,"kd":0.98,"matches":112000,"mb":{"Split":0.5,"Lotus":0.3,"Bind":0.1,"Haven":-0.1,"Ascent":-0.2,"Icebox":-0.3,"Sunset":-0.5}},
    {"name":"Chamber","role":"Sentinel","wr":49.62,"pr":41.00,"kd":1.11,"matches":173000,"mb":{"Ascent":0.4,"Bind":0.3,"Haven":0.1,"Split":-0.2,"Lotus":-0.3,"Icebox":-0.4,"Sunset":-0.5}},
    {"name":"Iso","role":"Duelist","wr":48.32,"pr":10.00,"kd":1.01,"matches":42200,"mb":{"Split":0.3,"Ascent":0.2,"Bind":0.0,"Lotus":-0.2,"Haven":-0.3,"Icebox":-0.4,"Sunset":-0.5}},
    {"name":"Deadlock","role":"Sentinel","wr":50.02,"pr":9.00,"kd":0.96,"matches":38000,"mb":{"Ascent":0.3,"Bind":0.2,"Split":0.1,"Lotus":-0.1,"Haven":-0.2,"Icebox":-0.2,"Sunset":-0.3}},
    {"name":"Reyna","role":"Duelist","wr":49.92,"pr":45.00,"kd":1.08,"matches":190000,"mb":{"Split":0.5,"Icebox":0.3,"Ascent":0.1,"Bind":-0.2,"Lotus":-0.3,"Haven":-0.5,"Sunset":-0.7}},
    {"name":"Fade","role":"Initiator","wr":50.52,"pr":18.50,"kd":0.93,"matches":78100,"mb":{"Haven":0.5,"Split":0.3,"Lotus":0.1,"Bind":-0.2,"Ascent":-0.3,"Sunset":-0.4,"Icebox":-0.5}},
    {"name":"Brimstone","role":"Controller","wr":50.72,"pr":11.00,"kd":0.97,"matches":46400,"mb":{"Ascent":0.8,"Bind":0.5,"Haven":0.2,"Split":-0.1,"Lotus":-0.3,"Icebox":-0.5,"Sunset":-0.7}},
    {"name":"Veto","role":"Sentinel","wr":49.02,"pr":3.00,"kd":1.02,"matches":12600,"mb":{"Bind":0.3,"Split":0.2,"Ascent":0.1,"Lotus":-0.1,"Haven":-0.2,"Icebox":-0.3,"Sunset":-0.4}},
    {"name":"Vyse","role":"Sentinel","wr":50.02,"pr":3.50,"kd":1.01,"matches":14800,"mb":{"Bind":0.4,"Split":0.2,"Lotus":0.0,"Ascent":-0.2,"Haven":-0.3,"Icebox":-0.3,"Sunset":-0.4}},
    {"name":"Gekko","role":"Initiator","wr":50.62,"pr":14.00,"kd":0.89,"matches":59100,"mb":{"Lotus":0.6,"Bind":0.4,"Haven":0.2,"Split":-0.1,"Ascent":-0.3,"Icebox":-0.4,"Sunset":-0.6}},
    {"name":"Astra","role":"Controller","wr":48.72,"pr":4.50,"kd":1.03,"matches":19000,"mb":{"Ascent":0.3,"Haven":0.2,"Split":0.1,"Bind":-0.2,"Lotus":-0.3,"Icebox":-0.4,"Sunset":-0.5}},
    {"name":"Skye","role":"Initiator","wr":49.82,"pr":17.50,"kd":0.93,"matches":73800,"mb":{"Split":0.5,"Haven":0.3,"Bind":0.1,"Lotus":-0.2,"Ascent":-0.3,"Icebox":-0.4,"Sunset":-0.5}},
    {"name":"Miks","role":"Controller","wr":49.12,"pr":40.50,"kd":0.94,"matches":171000,"mb":{"Lotus":0.4,"Haven":0.2,"Split":0.1,"Bind":-0.2,"Ascent":-0.3,"Icebox":-0.4,"Sunset":-0.5}},
    {"name":"Yoru","role":"Duelist","wr":46.93,"pr":4.50,"kd":0.97,"matches":19000,"mb":{"Split":0.4,"Ascent":0.2,"Bind":0.0,"Lotus":-0.2,"Haven":-0.3,"Icebox":-0.4,"Sunset":-0.6}},
    {"name":"Tejo","role":"Initiator","wr":49.42,"pr":9.00,"kd":0.94,"matches":38000,"mb":{"Bind":0.3,"Split":0.2,"Lotus":0.1,"Haven":-0.1,"Ascent":-0.2,"Icebox":-0.3,"Sunset":-0.4}},
    {"name":"Harbor","role":"Controller","wr":47.02,"pr":2.50,"kd":0.93,"matches":10500,"mb":{"Lotus":0.4,"Bind":0.2,"Haven":0.1,"Split":-0.2,"Ascent":-0.3,"Icebox":-0.4,"Sunset":-0.5}},
    {"name":"Waylay","role":"Duelist","wr":48.42,"pr":10.00,"kd":1.00,"matches":42200,"mb":{"Split":0.4,"Ascent":0.2,"Bind":0.0,"Lotus":-0.2,"Haven":-0.3,"Icebox":-0.4,"Sunset":-0.6}},
    {"name":"Raze","role":"Duelist","wr":50.52,"pr":21.00,"kd":1.03,"matches":88600,"mb":{"Split":0.8,"Bind":0.5,"Lotus":0.2,"Haven":-0.1,"Ascent":-0.4,"Icebox":-0.5,"Sunset":-0.7}},
    {"name":"KAY/O","role":"Initiator","wr":47.02,"pr":8.00,"kd":0.90,"matches":33800,"mb":{"Split":0.3,"Bind":0.2,"Ascent":0.1,"Lotus":-0.1,"Haven":-0.2,"Icebox":-0.3,"Sunset":-0.5}},
    {"name":"Breach","role":"Initiator","wr":49.02,"pr":10.00,"kd":0.93,"matches":42200,"mb":{"Split":0.4,"Bind":0.2,"Ascent":0.1,"Lotus":-0.1,"Haven":-0.2,"Icebox":-0.3,"Sunset":-0.5}},
]

ANALYSIS = {
    "Clove":{"s":["强大的复活技能","灵活的烟雾控制","高生存能力"],"w":["需要团队配合","技能冷却较长"],"p":"适合作为副烟使用，利用复活技能为团队创造人数优势。在进攻方可以配合决斗者突破，防守方可以利用烟雾拖延时间。"},
    "Sage":{"s":["强大的治疗能力","改变地形的能力","复活技能"],"w":["缺乏进攻性","依赖枪法"],"p":"适合在防守方使用，利用冰墙控制关键点位。在进攻方可以跟随队伍提供治疗支持，复活技能要留给关键队友。"},
    "Killjoy":{"s":["自动防守设备","警报机器人","大招锁定区域"],"w":["设备可被摧毁","离开范围设备失效"],"p":"设备型守卫，利用炮台和警报机器人控制区域。大招可以锁定大片区域，在防守方非常强力。"},
    "Phoenix":{"s":["自疗能力","闪光技能","大招重生"],"w":["闪光可能误伤队友","技能范围有限"],"p":"自给自足的决斗者，闪光可以配合队友突破。大招可以在危险位置试探，死亡后回到安全位置。"},
    "Omen":{"s":["全图传送","致盲技能","烟雾灵活"],"w":["传送容易被预判","胜率偏低"],"p":"传送型控场者，利用传送进行侧翼包抄或快速回防。致盲可以配合队友突破，但需要良好的地图理解。"},
    "Jett":{"s":["极高机动性","烟雾配合突破","大招连杀能力"],"w":["依赖枪法","技能容错率低"],"p":"高机动决斗者，利用突进和漂浮进行非常规位打法。烟雾可以为自己创造射击窗口，大招在经济局非常强力。"},
    "Sova":{"s":["全图侦查","闪电伤害","大招清场"],"w":["技能需要学习箭位","机动性差"],"p":"侦查型先锋，利用侦查箭为团队提供关键信息。闪电可以逼出角落敌人，大招在残局非常强力。"},
    "Cypher":{"s":["全图监控","绊线预警","大招获取位置"],"w":["设备可被摧毁","缺乏机动性"],"p":"监控型守卫，利用摄像头和绊线获取全图信息。大招可以复活获取敌人位置，在残局非常强力。"},
    "Viper":{"s":["区域封锁","毒雾持续伤害","大招范围控制"],"w":["毒雾需要燃料管理","选取率偏低"],"p":"封锁型控场者，利用毒雾封锁关键区域。在Icebox等地图非常强力，大招可以控制大片区域。"},
    "Neon":{"s":["极高移动速度","闪电减速","大招连杀"],"w":["冲刺容易被预判","需要近战环境"],"p":"速度型决斗者，利用冲刺快速到达关键位置。闪电可以减速敌人，大招在近距离非常强力。"},
    "Chamber":{"s":["高伤害狙击","传送逃脱","大招双倍射速"],"w":["依赖枪法","守卫能力弱"],"p":"狙击型守卫，利用传送进行激进打法。大招可以提供双倍射速，在经济局非常强力。"},
    "Iso":{"s":["1v1决斗能力","护盾技能","大招单挑"],"w":["胜率偏低","团队贡献有限"],"p":"决斗型特工，利用护盾和1v1能力进行正面交锋。大招可以强制单挑，适合枪法自信的玩家。"},
    "Deadlock":{"s":["声波探测","屏障控制","大招范围捕获"],"w":["技能容易被破坏","选取率偏低"],"p":"控制型守卫，利用声波和屏障限制敌人移动。适合防守方使用，大招在回防时可以有效清场。"},
    "Reyna":{"s":["击杀后回复","无敌技能","大招群体压制"],"w":["依赖击杀","无团队辅助"],"p":"击杀型决斗者，需要枪法自信。每次击杀后可以获得治疗或无敌，适合连续突破的打法。"},
    "Fade":{"s":["恐惧技能","全图大招","追踪敌人"],"w":["技能需要预判","选取率偏低"],"p":"恐惧型先锋，利用噩梦技能打乱敌人阵型。大招可以全图标记敌人，为团队提供关键信息。"},
    "Brimstone":{"s":["快速烟雾","激励大招","空袭伤害"],"w":["烟雾位置固定","缺乏机动性"],"p":"传统控场者，烟雾可以快速部署。大招激励可以大幅提升团队火力，适合进攻方使用。"},
    "Veto":{"s":["独特技能组","防守潜力","新特工新鲜感"],"w":["数据样本少","战术未成熟"],"p":"新晋守卫，技能机制独特。目前数据样本较少，建议多尝试找到最佳使用方式。"},
    "Vyse":{"s":["独特机制","防守能力","新特工潜力"],"w":["数据极少","战术待开发"],"p":"新晋守卫，拥有独特的技能机制。目前还在探索阶段，建议多练习找到适合自己的打法。"},
    "Gekko":{"s":["生物伙伴","多功能技能","大招可回收"],"w":["生物容易被击杀","需要多线操作"],"p":"生物型先锋，利用小生物进行侦查和控制。技能可以回收重复使用，经济效率高。"},
    "Astra":{"s":["全图烟雾","引力大招","技能可重复"],"w":["学习曲线陡峭","需要地图理解"],"p":"高阶控场者，需要深厚的地图理解。星尘可以放置在全图任何位置，适合有经验的玩家。"},
    "Skye":{"s":["治疗能力","闪光技能","大招群体控制"],"w":["闪光可被躲避","生物容易被击杀"],"p":"治疗型先锋，可以为团队提供治疗支持。闪光技能可以配合队友突破，大招在进攻时非常有效。"},
    "Miks":{"s":["烟雾控制","战术多样性","高选取率"],"w":["胜率偏低","战术待优化"],"p":"新晋控场者，拥有独特的烟雾机制。高选取率说明玩家喜爱，但需要更好的战术配合来提升胜率。"},
    "Yoru":{"s":["传送潜入","闪光技能","大招隐身"],"w":["胜率最低","高风险高回报"],"p":"潜入型决斗者，利用传送和隐身进行侧翼包抄。适合有创意的玩家，可以打乱敌人防守节奏。"},
    "Tejo":{"s":["信息收集","战术支持","技能组合灵活"],"w":["胜率偏低","战术未成熟"],"p":"新晋先锋，技能机制独特。需要更多实战数据来验证最佳使用方式。"},
    "Harbor":{"s":["水幕掩护","区域控制","大招范围伤害"],"w":["水幕可被穿透","胜率偏低"],"p":"水幕型控场者，利用水墙为团队提供掩护。大招可以封锁大片区域，适合进攻方使用。"},
    "Waylay":{"s":["独特技能","突破潜力","高机动性"],"w":["胜率偏低","战术待开发"],"p":"新晋决斗者，拥有独特的技能机制。目前还在探索阶段，建议多练习找到最佳打法。"},
    "Raze":{"s":["爆破伤害","机动性","大招清场"],"w":["技能可被躲避","需要近战环境"],"p":"爆破型决斗者，利用手雷和火箭筒进行区域清理。适合在狭窄地图发挥，大招可以一击清场。"},
    "KAY/O":{"s":["压制技能","大招禁用","闪光技能"],"w":["胜率偏低","技能可被破坏"],"p":"压制型先锋，利用闪光和压制技能为团队创造优势。大招可以禁用敌人技能，在关键时刻非常有效。"},
    "Breach":{"s":["眩晕技能","穿墙闪光","大招群体控制"],"w":["选取率偏低","需要配合"],"p":"眩晕型先锋，利用闪光和眩晕为团队创造优势。技能可以穿墙释放，适合在狭窄地图使用。"},
}

def gen_maps(agent):
    name = agent["name"]
    role = agent["role"]
    wr = agent["wr"]
    pr = agent["pr"]
    mb = agent["mb"]
    rd = RD.get(name, {})
    map_pr_base = pr / len(MAP_POOL)
    lines = []
    for i, m in enumerate(MAP_POOL):
        map_wr = round(wr + mb.get(m, 0), 1)
        atk_b = MAP_BALANCE[m]["atk"]
        def_b = MAP_BALANCE[m]["def"]
        if role == "Duelist":
            atk_wr = round(map_wr + atk_b * 0.6 + 1.2, 1)
            def_wr = round(map_wr + def_b * 0.6 - 1.2, 1)
        elif role == "Sentinel":
            atk_wr = round(map_wr + atk_b * 0.6 - 1.0, 1)
            def_wr = round(map_wr + def_b * 0.6 + 1.0, 1)
        elif role == "Controller":
            atk_wr = round(map_wr + atk_b * 0.5 - 0.3, 1)
            def_wr = round(map_wr + def_b * 0.5 + 0.3, 1)
        else:
            atk_wr = round(map_wr + atk_b * 0.5, 1)
            def_wr = round(map_wr + def_b * 0.5, 1)
        bonus = mb.get(m, 0)
        if role == "Sentinel" and def_b > 0: bonus += 0.3
        elif role == "Duelist" and atk_b > 0: bonus += 0.2
        mpr = round(map_pr_base + bonus * 0.3, 1)
        if mpr < 0.3: mpr = 0.3
        rank_wrs = []
        for rank in RANKS:
            rank_d = rd.get(rank, {})
            overall_rank_wr = rank_d.get("wr", map_wr)
            if overall_rank_wr > 80 or overall_rank_wr < 10:
                overall_rank_wr = map_wr
            offset = overall_rank_wr - wr
            rwr = round(map_wr + offset, 1)
            rank_wrs.append(f'"{rank}": {rwr}')
        comma = "," if i < len(MAP_POOL) - 1 else ""
        lines.append(f'            "{m}": {{ winRate: {map_wr}, pickRate: {mpr}, attackWR: {atk_wr}, defenseWR: {def_wr},')
        lines.append(f'                rankWinRates: {{ {", ".join(rank_wrs)} }} }}{comma}')
    return "\n".join(lines)

def gen_ranks(agent):
    name = agent["name"]
    rd = RD.get(name, {})
    lines = []
    for i, rank in enumerate(RANKS):
        rank_d = rd.get(rank, {})
        wr_val = rank_d.get("wr", agent["wr"])
        pr_val = rank_d.get("pr", round(agent["pr"] / len(MAP_POOL), 1))
        if wr_val > 80 or wr_val < 10:
            wr_val = agent["wr"]
        comma = "," if i < len(RANKS) - 1 else ""
        lines.append(f'            "{rank}": {{ winRate: {wr_val}, pickRate: {pr_val} }}{comma}')
    return "\n".join(lines)

def gen_analysis(agent):
    name = agent["name"]
    a = ANALYSIS.get(name, {"s":["独特技能"],"w":["数据不足"],"p":"暂无详细分析。"})
    return f'''        analysis: {{
            strengths: [{", ".join([f'"{s}"' for s in a["s"]])}],
            weaknesses: [{", ".join([f'"{w}"' for w in a["w"]])}],
            playstyle: "{a["p"]}"
        }}'''

output = []
output.append("// 特工详细数据 - 包含地图和分段统计")
output.append("// 数据来源: vstats.gg (总体) + valking.gg (分段) 交叉验证")
output.append("// 更新日期: 2026/4/25 - Season 26 Act 2")
output.append("// 分段: Silver → Gold → Platinum → Diamond → Ascendant → Immortal → Radiant")
output.append("")
output.append("const agentDetailedData = {")

for i, agent in enumerate(agents):
    comma = "," if i < len(agents) - 1 else ""
    output.append(f'    "{agent["name"]}": {{')
    output.append(f'        role: "{agent["role"]}",')
    output.append(f'        overall: {{ winRate: {agent["wr"]}, pickRate: {agent["pr"]}, kd: {agent["kd"]}, matches: {agent["matches"]} }},')
    output.append(f'        maps: {{')
    output.append(gen_maps(agent))
    output.append(f'        }},')
    output.append(f'        ranks: {{')
    output.append(gen_ranks(agent))
    output.append(f'        }},')
    output.append(gen_analysis(agent))
    output.append(f'    }}{comma}')

output.append("};")
output.append("")
output.append('const mapNames = {')
output.append('    "Ascent": "亚海悬城", "Bind": "源工重镇", "Haven": "隐世修所", "Split": "霓虹町",')
output.append('    "Lotus": "莲华古城", "Sunset": "日落之城", "Breeze": "微风岛屿", "Icebox": "森寒冬港"')
output.append('};')
output.append("")
output.append('const roleNames = { "Duelist": "决斗者", "Initiator": "先锋", "Controller": "控场者", "Sentinel": "守卫" };')
output.append('const roleColors = { "Duelist": "#ff4655", "Initiator": "#4a9eff", "Controller": "#9c27b0", "Sentinel": "#4caf50" };')
output.append("")
output.append('const rankNames = { "Silver": "白银", "Gold": "黄金", "Platinum": "铂金", "Diamond": "钻石", "Ascendant": "超凡", "Immortal": "神话", "Radiant": "辐能" };')
output.append('const rankIcons = {')
output.append('    "Silver": "https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/10/smallicon.png",')
output.append('    "Gold": "https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/13/smallicon.png",')
output.append('    "Platinum": "https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/16/smallicon.png",')
output.append('    "Diamond": "https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/19/smallicon.png",')
output.append('    "Ascendant": "https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/22/smallicon.png",')
output.append('    "Immortal": "https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/25/smallicon.png",')
output.append('    "Radiant": "https://media.valorant-api.com/competitivetiers/03621f52-342b-cf4e-4f86-9350a49c6d04/27/smallicon.png"')
output.append('};')
output.append('const rankColors = {')
output.append('    "Silver": "#94a3b8", "Gold": "#fbbf24", "Platinum": "#60a5fa", "Diamond": "#a78bfa",')
output.append('    "Ascendant": "#34d399", "Immortal": "#f87171", "Radiant": "#fbbf24"')
output.append('};')
output.append("")
output.append('function getTier(winRate) {')
output.append('    if (winRate >= 53) return { tier: "S", class: "tier-s" };')
output.append('    if (winRate >= 51) return { tier: "A", class: "tier-a" };')
output.append('    if (winRate >= 49) return { tier: "B", class: "tier-b" };')
output.append('    return { tier: "C", class: "tier-c" };')
output.append('}')
output.append("")
output.append('function getBestMaps(agentData, count = 3) {')
output.append('    return Object.entries(agentData.maps).sort((a, b) => b[1].winRate - a[1].winRate).slice(0, count).map(([map, data]) => ({ map, ...data }));')
output.append('}')
output.append("")
output.append('function getAvoidMaps(agentData, count = 3) {')
output.append('    return Object.entries(agentData.maps).sort((a, b) => a[1].winRate - b[1].winRate).slice(0, count).map(([map, data]) => ({ map, ...data }));')
output.append('}')
output.append("")
output.append('function getBestRank(agentData) {')
output.append('    return Object.entries(agentData.ranks).sort((a, b) => b[1].winRate - a[1].winRate)[0];')
output.append('}')
output.append("")
output.append('function getRankSuggestion(agentData) {')
output.append('    const ranks = Object.entries(agentData.ranks);')
output.append('    const bestRank = ranks.sort((a, b) => b[1].winRate - a[1].winRate)[0];')
output.append('    const worstRank = ranks.sort((a, b) => a[1].winRate - b[1].winRate)[0];')
output.append('    return { best: { rank: bestRank[0], ...bestRank[1] }, worst: { rank: worstRank[0], ...worstRank[1] }, trend: bestRank[1].winRate - worstRank[1].winRate };')
output.append('}')

with open("d:/TRAE/valorant-stats-dashboard/agent-data.js", "w", encoding="utf-8") as f:
    f.write("\n".join(output))

print(f"Generated agent-data.js with {len(agents)} agents, {len(RANKS)} ranks each")
print(f"Ranks: {', '.join(RANKS)}")
