import urllib.request, ssl, sys, re, json, gzip, os
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
h = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36', 'Accept': '*/*', 'Referer': 'https://www.vstats.gg/agents'}

output = []

url = 'https://www.vstats.gg/assets/index-VdEKILD-.js'
req = urllib.request.Request(url, headers=h)
resp = urllib.request.urlopen(req, timeout=60, context=ctx)
js = resp.read().decode('utf-8', errors='replace')
output.append(f'JS length: {len(js)}')

act_patterns = re.findall(r'ACTIVE_ACT\s*[:=]\s*["\']([^"\']+)["\']', js)
output.append(f'ACTIVE_ACT patterns: {act_patterns}')

map_all = re.findall(r'MAP_ALL\s*[:=]\s*["\']([^"\']+)["\']', js)
output.append(f'MAP_ALL patterns: {map_all}')

rank_all = re.findall(r'RANK_ALL\s*[:=]\s*["\']([^"\']+)["\']', js)
output.append(f'RANK_ALL patterns: {rank_all}')

constants = re.findall(r'((?:ACTIVE_|MAP_|RANK_|TABLE_)[A-Z_]+)\s*[:=]\s*["\']([^"\']+)["\']', js)
output.append(f'Constants: {constants}')

uuid_patterns = re.findall(r'["\']([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})["\']', js, re.IGNORECASE)
output.append(f'UUID patterns ({len(set(uuid_patterns))}): {sorted(set(uuid_patterns))[:20]}')

base_url = 'https://www.vstats.gg/statistics'
test_urls = [
    f'{base_url}/ALL/ALL/agent.json.gz',
    f'{base_url}/ALL/V26Act2/agent.json.gz',
]

for test_url in test_urls:
    output.append(f'\nTrying: {test_url}')
    try:
        req = urllib.request.Request(test_url, headers=h)
        resp = urllib.request.urlopen(req, timeout=30, context=ctx)
        raw = resp.read()
        ct = resp.headers.get('Content-Type', '')
        output.append(f'  Status: {resp.status}, Length: {len(raw)}, CT: {ct}')
        if b'<!DOCTYPE' not in raw[:20]:
            try:
                data = json.loads(gzip.decompress(raw).decode('utf-8'))
                output.append(f'  GZIP JSON! Type: {type(data).__name__}, Len: {len(data)}')
                if isinstance(data, list) and len(data) > 0:
                    output.append(f'  First: {json.dumps(data[0], indent=2)[:300]}')
            except:
                try:
                    data = json.loads(raw.decode('utf-8'))
                    output.append(f'  JSON! Type: {type(data).__name__}')
                except:
                    output.append(f'  Not JSON. First 200: {raw[:200].decode("utf-8", errors="replace")}')
        else:
            output.append(f'  HTML response')
    except Exception as e:
        output.append(f'  Error: {e}')

result_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'act_results.txt')
with open(result_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(output))
print('Done!')
