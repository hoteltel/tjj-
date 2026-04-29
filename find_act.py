import urllib.request, ssl, sys, re, json, gzip
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
h = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36', 'Accept': '*/*', 'Referer': 'https://www.vstats.gg/agents'}

url = 'https://www.vstats.gg/assets/index-VdEKILD-.js'
req = urllib.request.Request(url, headers=h)
resp = urllib.request.urlopen(req, timeout=60, context=ctx)
js = resp.read().decode('utf-8', errors='replace')

print(f'JS length: {len(js)}')

print('\n=== Searching for ACTIVE_ACT ===')
act_patterns = re.findall(r'ACTIVE_ACT\s*[:=]\s*["\']([^"\']+)["\']', js)
if act_patterns:
    for p in act_patterns:
        print(f'  ACTIVE_ACT = {p}')

print('\n=== Searching for act identifiers ===')
act_ids = re.findall(r'["\']([a-z0-9]+-[a-z0-9]+-[a-z0-9]+-[a-z0-9]+-[a-z0-9]+)["\']', js)
if act_ids:
    print(f'UUID-like patterns ({len(set(act_ids))}):')
    for p in sorted(set(act_ids))[:20]:
        print(f'  {p}')

print('\n=== Searching for act/season patterns ===')
season_patterns = re.findall(r'["\']([Vv]\d+[Aa]ct\d+|season_\d+|act_\d+|e\d+a\d+|e\d+p\d+)["\']', js)
if season_patterns:
    for p in sorted(set(season_patterns)):
        print(f'  {p}')

print('\n=== Searching for MAP_ALL / RANK_ALL ===')
map_all = re.findall(r'MAP_ALL\s*[:=]\s*["\']([^"\']+)["\']', js)
if map_all:
    for p in map_all:
        print(f'  MAP_ALL = {p}')

rank_all = re.findall(r'RANK_ALL\s*[:=]\s*["\']([^"\']+)["\']', js)
if rank_all:
    for p in rank_all:
        print(f'  RANK_ALL = {p}')

print('\n=== Searching for constants ===')
constants = re.findall(r'(?:ACTIVE_|MAP_|RANK_|TABLE_)[A-Z_]+\s*[:=]\s*["\']([^"\']+)["\']', js)
if constants:
    for p in sorted(set(constants)):
        print(f'  {p}')

print('\n=== Now trying to fetch data with discovered patterns ===')
base_url = 'https://www.vstats.gg/statistics'

test_urls = [
    f'{base_url}/ALL/ALL/agent.json.gz',
    f'{base_url}/ALL/V26Act2/agent.json.gz',
    f'{base_url}/ALL/v26act2/agent.json.gz',
    f'{base_url}/ALL/e9a2/agent.json.gz',
    f'{base_url}/ALL/e9p2/agent.json.gz',
]

for test_url in test_urls:
    print(f'\nTrying: {test_url}')
    try:
        req = urllib.request.Request(test_url, headers=h)
        resp = urllib.request.urlopen(req, timeout=30, context=ctx)
        raw = resp.read()
        print(f'  Status: {resp.status}, Length: {len(raw)}, Content-Type: {resp.headers.get("Content-Type")}')
        if len(raw) > 100 and not raw[:5].startswith(b'<!DOC'):
            try:
                data = json.loads(gzip.decompress(raw).decode('utf-8'))
                print(f'  GZIP JSON parsed! Type: {type(data).__name__}, Len: {len(data)}')
                if isinstance(data, list) and len(data) > 0:
                    print(f'  First entry: {json.dumps(data[0], indent=2)[:300]}')
            except:
                try:
                    data = json.loads(raw.decode('utf-8'))
                    print(f'  JSON parsed! Type: {type(data).__name__}')
                except:
                    print(f'  First 200 chars: {raw[:200].decode("utf-8", errors="replace")}')
        else:
            print(f'  First 200 chars: {raw[:200].decode("utf-8", errors="replace")}')
    except Exception as e:
        print(f'  Error: {e}')
