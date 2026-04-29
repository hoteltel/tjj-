import urllib.request
import json
import gzip
import ssl
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://www.vstats.gg/agents',
    'Origin': 'https://www.vstats.gg'
}

def fetch_url(url):
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=30, context=ctx) as resp:
            raw = resp.read()
            try:
                decompressed = gzip.decompress(raw)
                return decompressed.decode('utf-8')
            except:
                try:
                    return raw.decode('utf-8')
                except:
                    return None
    except Exception as e:
        return f"Error: {e}"

results = []

urls_to_try = [
    'https://www.vstats.gg/statistics/agents/ALL/agents.json.gz',
    'https://www.vstats.gg/statistics/agents/ALL/agents.json',
    'https://www.vstats.gg/api/agents',
    'https://www.vstats.gg/api/v1/agents',
]

for url in urls_to_try:
    results.append(f"\n=== Trying: {url} ===")
    content = fetch_url(url)
    if content and not content.startswith('Error'):
        results.append(f"Success! Length: {len(content)}")
        try:
            data = json.loads(content)
            if isinstance(data, list):
                results.append(f"Got {len(data)} agents")
                for agent in sorted(data, key=lambda x: x.get('wr', x.get('win_rate', 0)), reverse=True):
                    name = agent.get('agent', agent.get('a', agent.get('name', 'Unknown')))
                    wr = agent.get('wr', agent.get('win_rate', 0))
                    if isinstance(wr, float) and wr < 1:
                        wr = wr * 100
                    pr = agent.get('pr', agent.get('pick_rate', 0))
                    kd = agent.get('kd', agent.get('k_d', 0))
                    matches = agent.get('matches', agent.get('m', 0))
                    nm_wr = agent.get('non_mirror_wr', agent.get('nmwr', 0))
                    if isinstance(nm_wr, float) and nm_wr < 1:
                        nm_wr = nm_wr * 100
                    results.append(f"{name}|{wr:.2f}|{pr:.2f}|{kd:.2f}|{matches}|{nm_wr:.2f}")
            elif isinstance(data, dict):
                results.append(f"Got dict with keys: {list(data.keys())[:10]}")
                results.append(json.dumps(data, indent=2)[:2000])
        except json.JSONDecodeError:
            results.append(f"Not JSON, first 500 chars: {content[:500]}")
    else:
        results.append(f"Failed: {content}")

with open('d:/TRAE/valorant-stats-dashboard/vstats_fetch_results.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(results))

print('\n'.join(results))
