import urllib.request, json, gzip, ssl, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36', 'Accept': 'application/json, text/plain, */*'}

urls = [
    'https://www.vstats.gg/statistics/agents/ALL/agents.json.gz',
    'https://d1s1t6g4fsu3ed.cloudfront.net/statistics/agents/ALL/agents.json.gz',
    'https://www.vstats.gg/api/agents?rank=ALL',
]

for url in urls:
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15, context=ctx) as resp:
            raw = resp.read()
            try:
                decompressed = gzip.decompress(raw)
                data = json.loads(decompressed.decode('utf-8'))
            except:
                try:
                    data = json.loads(raw.decode('utf-8'))
                except:
                    print(f'{url}: parse failed, len={len(raw)}')
                    continue
            if isinstance(data, list):
                print(f'{url}: LIST with {len(data)} entries')
                for a in sorted(data, key=lambda x: x.get('wr', 0), reverse=True):
                    name = a.get('agent', a.get('a', '?'))
                    wr = a.get('wr', 0) * 100
                    pr = a.get('pr', 0)
                    kd = a.get('kd', 0)
                    matches = a.get('matches', a.get('m', 0))
                    nm_wr = a.get('non_mirror_wr', 0) * 100
                    print(f'{name}|{wr:.2f}|{pr:.2f}|{kd:.2f}|{matches}|{nm_wr:.2f}')
            elif isinstance(data, dict):
                print(f'{url}: DICT keys={list(data.keys())[:10]}')
            else:
                print(f'{url}: type={type(data).__name__}')
    except Exception as e:
        print(f'{url}: ERROR {e}')
