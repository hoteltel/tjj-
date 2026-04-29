import urllib.request
import json
import ssl
import gzip
import sys
import os

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Origin': 'https://www.vstats.gg',
    'Referer': 'https://www.vstats.gg/agents'
}

output = []

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

def fetch_json(url):
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=30, context=ctx) as resp:
            raw = resp.read()
            try:
                return json.loads(raw.decode('utf-8'))
            except:
                try:
                    decompressed = gzip.decompress(raw)
                    return json.loads(decompressed.decode('utf-8'))
                except:
                    return None
    except Exception as e:
        return None

output.append("=== TRYING VSTATS.GG API ENDPOINTS ===")

endpoints = [
    'https://www.vstats.gg/statistics/agents/ALL/agents.json.gz',
    'https://www.vstats.gg/statistics/agents/ALL/agents.json',
    'https://www.vstats.gg/api/agents',
    'https://www.vstats.gg/api/v1/agents',
    'https://www.vstats.gg/api/agents/ALL',
]

for url in endpoints:
    output.append(f"\nTrying: {url}")
    data = fetch_json_gz(url)
    if data is None:
        data = fetch_json(url)
    if data:
        output.append(f"SUCCESS! Type: {type(data).__name__}")
        if isinstance(data, list):
            output.append(f"Entries: {len(data)}")
            if len(data) > 0:
                output.append(f"First entry keys: {list(data[0].keys()) if isinstance(data[0], dict) else 'N/A'}")
                output.append(f"First entry: {json.dumps(data[0], indent=2)[:500]}")
                output.append("\n=== ALL AGENTS DATA ===")
                for agent in sorted(data, key=lambda x: x.get('wr', x.get('win_rate', 0)), reverse=True):
                    name = agent.get('agent', agent.get('name', agent.get('a', 'Unknown')))
                    wr = agent.get('wr', agent.get('win_rate', 0))
                    if isinstance(wr, float) and wr < 1:
                        wr = wr * 100
                    pr = agent.get('pr', agent.get('pick_rate', 0))
                    kd = agent.get('kd', agent.get('k_d', 0))
                    matches = agent.get('matches', agent.get('m', 0))
                    nm_wr = agent.get('non_mirror_wr', agent.get('nm_wr', 0))
                    if isinstance(nm_wr, float) and nm_wr < 1:
                        nm_wr = nm_wr * 100
                    output.append(f"{name}|WR:{wr:.2f}|PR:{pr:.2f}|KD:{kd:.2f}|M:{matches}|NMWR:{nm_wr:.2f}")
        elif isinstance(data, dict):
            output.append(f"Keys: {list(data.keys())[:20]}")
            output.append(f"Data preview: {json.dumps(data, indent=2)[:1000]}")
    else:
        output.append("FAILED - No data returned")

output.append("\n=== TRYING MAP-SPECIFIC ENDPOINTS ===")
maps = ['Ascent', 'Bind', 'Haven', 'Split', 'Lotus', 'Sunset', 'Icebox']
for map_name in maps:
    url = f'https://www.vstats.gg/statistics/agents/{map_name}/agents.json.gz'
    output.append(f"\nTrying: {url}")
    data = fetch_json_gz(url)
    if data is None:
        data = fetch_json(url)
    if data:
        output.append(f"SUCCESS! Entries: {len(data) if isinstance(data, list) else 'dict'}")
        if isinstance(data, list) and len(data) > 0:
            output.append(f"First entry: {json.dumps(data[0], indent=2)[:500]}")
    else:
        output.append("FAILED")

output.append("\n=== TRYING RANK-SPECIFIC ENDPOINTS ===")
ranks = ['Iron', 'Bronze', 'Silver', 'Gold', 'Platinum', 'Diamond', 'Ascendant', 'Immortal', 'Radiant']
for rank in ranks:
    url = f'https://www.vstats.gg/statistics/agents/ALL/{rank}/agents.json.gz'
    output.append(f"\nTrying: {url}")
    data = fetch_json_gz(url)
    if data is None:
        data = fetch_json(url)
    if data:
        output.append(f"SUCCESS! Entries: {len(data) if isinstance(data, list) else 'dict'}")
        if isinstance(data, list) and len(data) > 0:
            output.append(f"First entry: {json.dumps(data[0], indent=2)[:500]}")
    else:
        output.append("FAILED")

result_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'vstats_api_results.txt')
with open(result_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(output))

print(f"Results saved to {result_path}")
print('\n'.join(output[:50]))
