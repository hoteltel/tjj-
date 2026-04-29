import urllib.request
import ssl
import json
import gzip

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Try different header combinations
headers_combos = [
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'application/json',
        'Referer': 'https://www.vstats.gg/agents'
    },
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': '*/*',
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'https://www.vstats.gg/agents'
    },
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Referer': 'https://www.vstats.gg/agents',
        'Origin': 'https://www.vstats.gg'
    }
]

urls = [
    'https://www.vstats.gg/statistics/agents/ALL/agents.json.gz',
    'https://www.vstats.gg/statistics/agents/ALL/agents.json',
    'https://cdn.vstats.gg/statistics/agents/ALL/agents.json.gz',
    'https://data.vstats.gg/statistics/agents/ALL/agents.json.gz',
]

for url in urls:
    for i, headers in enumerate(headers_combos):
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=10, context=ctx) as resp:
                raw = resp.read()
                content_type = resp.headers.get('Content-Type', '')
                is_html = b'<!DOCTYPE' in raw or b'<html' in raw
                
                if not is_html:
                    try:
                        decompressed = gzip.decompress(raw)
                        data = json.loads(decompressed.decode('utf-8'))
                        print(f"SUCCESS! URL: {url}, Headers: {i}")
                        print(f"Type: {type(data)}, Count: {len(data) if isinstance(data, list) else 'N/A'}")
                        if isinstance(data, list) and len(data) > 0:
                            print(f"First item: {json.dumps(data[0], ensure_ascii=True)}")
                        break
                    except:
                        try:
                            data = json.loads(raw.decode('utf-8'))
                            print(f"SUCCESS (no gzip)! URL: {url}, Headers: {i}")
                            print(f"Type: {type(data)}, Count: {len(data) if isinstance(data, list) else 'N/A'}")
                            break
                        except:
                            pass
                
                if is_html:
                    print(f"HTML response - URL: {url}, Headers: {i}, CT: {content_type}")
                else:
                    print(f"Non-HTML - URL: {url}, Headers: {i}, Len: {len(raw)}, CT: {content_type}")
        except Exception as e:
            print(f"Error - URL: {url}, Headers: {i}: {e}")
