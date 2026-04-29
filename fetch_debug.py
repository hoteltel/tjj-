import urllib.request, json, gzip, ssl, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36', 'Accept': 'application/json, text/plain, */*'}

url = 'https://www.vstats.gg/statistics/agents/ALL/agents.json.gz'
try:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=15, context=ctx) as resp:
        raw = resp.read()
        print(f'Status: {resp.status}')
        print(f'Content-Type: {resp.headers.get("Content-Type")}')
        print(f'Content-Length: {len(raw)}')
        print(f'First 500 bytes: {raw[:500]}')
        try:
            decompressed = gzip.decompress(raw)
            print(f'Decompressed len: {len(decompressed)}')
            print(f'Decompressed first 1000: {decompressed[:1000].decode("utf-8", errors="replace")}')
        except Exception as e:
            print(f'Gzip decompress error: {e}')
        try:
            text = raw.decode('utf-8', errors='replace')
            print(f'As text first 1000: {text[:1000]}')
        except:
            pass
except Exception as e:
    print(f'ERROR: {e}')
