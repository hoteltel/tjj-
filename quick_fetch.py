import urllib.request, json, ssl, gzip, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
h = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36', 'Accept': '*/*', 'Referer': 'https://www.vstats.gg/agents', 'Accept-Encoding': 'identity'}

urls = [
    'https://www.vstats.gg/statistics/agents/ALL/agents.json.gz',
    'https://www.vstats.gg/statistics/agents/ALL/agents.json',
    'https://www.vstats.gg/api/agents',
]

for url in urls:
    print(f'\n=== {url} ===')
    try:
        req = urllib.request.Request(url, headers=h)
        resp = urllib.request.urlopen(req, timeout=30, context=ctx)
        raw = resp.read()
        print(f'Status: {resp.status}')
        print(f'Headers: {dict(resp.headers)}')
        print(f'Raw len: {len(raw)}')
        print(f'First 500 chars: {raw[:500].decode("utf-8", errors="replace")}')
        
        try:
            data = json.loads(gzip.decompress(raw).decode('utf-8'))
            print(f'GZIP JSON parsed! Type: {type(data).__name__}')
        except:
            pass
        
        try:
            data = json.loads(raw.decode('utf-8'))
            print(f'JSON parsed! Type: {type(data).__name__}')
            if isinstance(data, list):
                print(f'Entries: {len(data)}')
                if len(data) > 0:
                    print(f'First entry: {json.dumps(data[0], indent=2)[:300]}')
        except:
            print('Not valid JSON')
    except Exception as e:
        print(f'Error: {e}')
