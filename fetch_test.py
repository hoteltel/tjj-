import urllib.request
import ssl
import json
import gzip

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

results = []

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': 'application/json, text/plain, */*',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'https://www.vstats.gg/agents',
    'Origin': 'https://www.vstats.gg'
}

urls = [
    'https://www.vstats.gg/statistics/agents/ALL/agents.json.gz',
    'https://www.vstats.gg/statistics/agents/ALL/agents.json',
]

for url in urls:
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15, context=ctx) as resp:
            raw = resp.read()
            ct = resp.headers.get('Content-Type', '')
            is_html = b'<!DOCTYPE' in raw or b'<html' in raw
            results.append(f"URL: {url}")
            results.append(f"  Status: {resp.status}, CT: {ct}, Len: {len(raw)}, IsHTML: {is_html}")
            
            if not is_html:
                try:
                    decompressed = gzip.decompress(raw)
                    data = json.loads(decompressed.decode('utf-8'))
                    results.append(f"  SUCCESS! Type: {type(data).__name__}")
                    if isinstance(data, list):
                        results.append(f"  Count: {len(data)}")
                        if len(data) > 0:
                            results.append(f"  First: {json.dumps(data[0], ensure_ascii=True)[:300]}")
                except gzipError:
                    try:
                        data = json.loads(raw.decode('utf-8'))
                        results.append(f"  SUCCESS (no gzip)! Type: {type(data).__name__}")
                    except:
                        results.append(f"  Cannot parse as JSON")
    except Exception as e:
        results.append(f"URL: {url} - Error: {e}")

with open(r'd:\TRAE\valorant-stats-dashboard\fetch_results.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(results))

print("Done")
