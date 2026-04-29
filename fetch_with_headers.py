import urllib.request, json, gzip, ssl, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

base_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://www.vstats.gg/agents',
    'Origin': 'https://www.vstats.gg',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}

url = 'https://www.vstats.gg/statistics/agents/ALL/agents.json.gz'
try:
    req = urllib.request.Request(url, headers=base_headers)
    with urllib.request.urlopen(req, timeout=15, context=ctx) as resp:
        raw = resp.read()
        print(f'Status: {resp.status}')
        print(f'Content-Type: {resp.headers.get("Content-Type")}')
        print(f'Content-Encoding: {resp.headers.get("Content-Encoding")}')
        print(f'Content-Length header: {resp.headers.get("Content-Length")}')
        print(f'Actual length: {len(raw)}')
        
        try:
            decompressed = gzip.decompress(raw)
            data = json.loads(decompressed.decode('utf-8'))
            print(f'Decompressed OK! Length: {len(decompressed)}')
            if isinstance(data, list):
                print(f'Data entries: {len(data)}')
                for a in sorted(data, key=lambda x: x.get('wr', 0), reverse=True)[:5]:
                    name = a.get('a', a.get('agent', '?'))
                    wr = a.get('wr', 0) * 100
                    pr = a.get('pr', 0)
                    kd = a.get('kd', 0)
                    matches = a.get('m', a.get('matches', 0))
                    print(f'  {name}: WR={wr:.2f}% PR={pr:.2f}% KD={kd:.2f} M={matches}')
        except Exception as e:
            print(f'Decompress error: {e}')
            try:
                text = raw.decode('utf-8', errors='replace')
                print(f'As text (first 500): {text[:500]}')
            except:
                pass
except Exception as e:
    print(f'ERROR: {e}')

print('\n\n--- Trying with different URL patterns ---')
alt_urls = [
    'https://www.vstats.gg/statistics/agents/ALL/agents.json',
    'https://www.vstats.gg/api/v1/agents',
    'https://www.vstats.gg/api/agents/ALL',
]

for alt_url in alt_urls:
    try:
        req = urllib.request.Request(alt_url, headers=base_headers)
        with urllib.request.urlopen(req, timeout=10, context=ctx) as resp:
            raw = resp.read()
            ct = resp.headers.get('Content-Type', '')
            print(f'{alt_url}: Status={resp.status} CT={ct} Len={len(raw)}')
            if 'json' in ct or 'text/plain' in ct:
                try:
                    data = json.loads(raw.decode('utf-8'))
                    if isinstance(data, list):
                        print(f'  LIST with {len(data)} entries!')
                    else:
                        print(f'  Type: {type(data).__name__}')
                except:
                    print(f'  Not valid JSON, first 200: {raw[:200].decode("utf-8", errors="replace")}')
            else:
                print(f'  First 200: {raw[:200].decode("utf-8", errors="replace")}')
    except Exception as e:
        print(f'{alt_url}: ERROR {e}')
