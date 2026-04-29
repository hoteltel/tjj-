import urllib.request
import ssl
import json
import gzip

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'https://www.vstats.gg/agents'
}

def fetch_json_gz(url):
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=30, context=ctx) as resp:
            raw = resp.read()
            try:
                decompressed = gzip.decompress(raw)
                return json.loads(decompressed.decode('utf-8'))
            except:
                try:
                    return json.loads(raw.decode('utf-8'))
                except:
                    return None
    except Exception as e:
        return None

output = []

# Fetch all agents data
data = fetch_json_gz('https://www.vstats.gg/statistics/agents/ALL/agents.json.gz')
if data and isinstance(data, list):
    output.append(f"ALL AGENTS: {len(data)} entries")
    for agent in sorted(data, key=lambda x: x.get('wr', 0), reverse=True):
        name = agent.get('agent', agent.get('a', 'Unknown'))
        wr = agent.get('wr', 0) * 100
        pr = agent.get('pr', 0)
        kd = agent.get('kd', 0)
        matches = agent.get('matches', agent.get('m', 0))
        nm_wr = agent.get('non_mirror_wr', 0) * 100
        output.append(f"{name}|{wr:.2f}|{pr:.2f}|{kd:.2f}|{matches}|{nm_wr:.2f}")
else:
    output.append("ALL AGENTS: No data or error")

# Fetch map data
maps = ['Haven', 'Bind', 'Split', 'Pearl', 'Sunset', 'Fracture', 'Lotus']
for map_name in maps:
    data = fetch_json_gz(f'https://www.vstats.gg/statistics/agents/ALL/{map_name}/agents.json.gz')
    if data and isinstance(data, list):
        output.append(f"\nMAP_{map_name}: {len(data)} entries")
        for agent in sorted(data, key=lambda x: x.get('wr', 0), reverse=True):
            name = agent.get('agent', agent.get('a', 'Unknown'))
            wr = agent.get('wr', 0) * 100
            pr = agent.get('pr', 0)
            kd = agent.get('kd', 0)
            matches = agent.get('matches', agent.get('m', 0))
            output.append(f"{name}|{wr:.2f}|{pr:.2f}|{kd:.2f}|{matches}")
    else:
        output.append(f"\nMAP_{map_name}: No data")

# Fetch rank data
ranks = ['Radiant', 'Immortal', 'Diamond', 'Platinum', 'Gold', 'Silver']
for rank in ranks:
    data = fetch_json_gz(f'https://www.vstats.gg/statistics/agents/{rank}/agents.json.gz')
    if data and isinstance(data, list):
        output.append(f"\nRANK_{rank}: {len(data)} entries")
        for agent in sorted(data, key=lambda x: x.get('wr', 0), reverse=True):
            name = agent.get('agent', agent.get('a', 'Unknown'))
            wr = agent.get('wr', 0) * 100
            pr = agent.get('pr', 0)
            kd = agent.get('kd', 0)
            matches = agent.get('matches', agent.get('m', 0))
            output.append(f"{name}|{wr:.2f}|{pr:.2f}|{kd:.2f}|{matches}")
    else:
        output.append(f"\nRANK_{rank}: No data")

# Also fetch rank+map data for first map
for rank in ranks:
    for map_name in maps:
        data = fetch_json_gz(f'https://www.vstats.gg/statistics/agents/{rank}/{map_name}/agents.json.gz')
        if data and isinstance(data, list):
            output.append(f"\nRANK_{rank}_MAP_{map_name}: {len(data)} entries")
            for agent in sorted(data, key=lambda x: x.get('wr', 0), reverse=True)[:5]:
                name = agent.get('agent', agent.get('a', 'Unknown'))
                wr = agent.get('wr', 0) * 100
                pr = agent.get('pr', 0)
                output.append(f"{name}|{wr:.2f}|{pr:.2f}")
        else:
            output.append(f"\nRANK_{rank}_MAP_{map_name}: No data")

with open('d:\\TRAE\\valorant-stats-dashboard\\vstats_data.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(output))

print("Data saved to vstats_data.txt")
