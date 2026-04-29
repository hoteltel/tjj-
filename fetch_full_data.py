import urllib.request, ssl, sys, re, json, gzip, os
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
h = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36', 'Accept': '*/*', 'Referer': 'https://www.vstats.gg/agents', 'Accept-Encoding': 'gzip, deflate, br'}

output = []
act = '9d85c932-4820-c060-09c3-668636d4df1b'
base = 'https://www.vstats.gg/statistics'

def fetch_data(url):
    try:
        req = urllib.request.Request(url, headers=h)
        resp = urllib.request.urlopen(req, timeout=60, context=ctx)
        raw = resp.read()
        if b'<!DOCTYPE' in raw[:20]:
            return None, 'HTML response'
        try:
            data = json.loads(gzip.decompress(raw).decode('utf-8'))
            return data, f'GZIP JSON OK, type={type(data).__name__}, len={len(data) if isinstance(data, list) else "dict"}'
        except:
            try:
                data = json.loads(raw.decode('utf-8'))
                return data, f'JSON OK, type={type(data).__name__}, len={len(data) if isinstance(data, list) else "dict"}'
            except:
                return None, f'Not JSON, first 200: {raw[:200].decode("utf-8", errors="replace")}'
    except Exception as e:
        return None, f'Error: {e}'

url = f'{base}/ALL/{act}/agent.json.gz'
output.append(f'=== Fetching ALL agents: {url} ===')
data, msg = fetch_data(url)
output.append(msg)

if data and isinstance(data, list):
    output.append(f'\nTotal agents: {len(data)}')
    if len(data) > 0:
        output.append(f'First entry keys: {list(data[0].keys())}')
        output.append(f'First entry: {json.dumps(data[0], indent=2)[:500]}')
    
    output.append('\n=== ALL AGENTS SORTED BY WIN RATE ===')
    for a in sorted(data, key=lambda x: x.get('wr', 0), reverse=True):
        name = a.get('agent', '?')
        wr = a.get('wr', 0) * 100
        pr = a.get('pr', 0)
        kd = a.get('kd', 0)
        m = a.get('matches', 0)
        nmwr = a.get('non_mirror_wr', 0) * 100
        nmm = a.get('non_mirror_matches', 0)
        output.append(f'{name}|WR:{wr:.2f}|PR:{pr:.2f}|KD:{kd:.2f}|M:{m}|NMWR:{nmwr:.2f}|NMM:{nmm}')

maps = ['Ascent', 'Bind', 'Haven', 'Split', 'Lotus', 'Sunset', 'Icebox']
for map_name in maps:
    url = f'{base}/{map_name}/{act}/agent.json.gz'
    output.append(f'\n=== Fetching {map_name} agents: {url} ===')
    data, msg = fetch_data(url)
    output.append(msg)
    if data and isinstance(data, list):
        output.append(f'Agents: {len(data)}')
        if len(data) > 0:
            output.append(f'First entry: {json.dumps(data[0], indent=2)[:500]}')
        for a in sorted(data, key=lambda x: x.get('wr', 0), reverse=True)[:5]:
            name = a.get('agent', '?')
            wr = a.get('wr', 0) * 100
            pr = a.get('pr', 0)
            kd = a.get('kd', 0)
            output.append(f'  {name}|WR:{wr:.2f}|PR:{pr:.2f}|KD:{kd:.2f}')

ranks = ['Iron', 'Bronze', 'Silver', 'Gold', 'Platinum', 'Diamond', 'Ascendant', 'Immortal', 'Radiant']
for rank in ranks:
    url = f'{base}/ALL/{act}/{rank}/agent.json.gz'
    output.append(f'\n=== Fetching {rank} agents: {url} ===')
    data, msg = fetch_data(url)
    output.append(msg)
    if data and isinstance(data, list):
        output.append(f'Agents: {len(data)}')
        if len(data) > 0:
            output.append(f'First entry: {json.dumps(data[0], indent=2)[:500]}')
        for a in sorted(data, key=lambda x: x.get('wr', 0), reverse=True)[:3]:
            name = a.get('agent', '?')
            wr = a.get('wr', 0) * 100
            pr = a.get('pr', 0)
            output.append(f'  {name}|WR:{wr:.2f}|PR:{pr:.2f}')

result_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'vstats_data.txt')
with open(result_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(output))
print('Done! Results saved.')
