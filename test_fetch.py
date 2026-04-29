import urllib.request
import json
import gzip
import ssl
import sys
import os

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': '*/*',
    'Referer': 'https://www.vstats.gg/agents',
}

url = 'https://www.vstats.gg/statistics/agents/ALL/agents.json.gz'
print(f"Fetching: {url}")

try:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30, context=ctx) as resp:
        raw = resp.read()
        print(f"Status: {resp.status}")
        print(f"Content-Type: {resp.headers.get('Content-Type', 'N/A')}")
        print(f"Content-Length: {len(raw)}")
        print(f"First 100 bytes: {raw[:100]}")
        
        is_html = b'<!DOCTYPE' in raw[:200] or b'<html' in raw[:200]
        print(f"Is HTML: {is_html}")
        
        if not is_html:
            try:
                decompressed = gzip.decompress(raw)
                data = json.loads(decompressed.decode('utf-8'))
                print(f"Decompressed OK, items: {len(data) if isinstance(data, list) else type(data)}")
                if isinstance(data, list) and len(data) > 0:
                    print(f"First item keys: {list(data[0].keys()) if isinstance(data[0], dict) else data[0]}")
                    print(f"First item: {data[0]}")
            except Exception as e:
                print(f"Gzip decompress failed: {e}")
                try:
                    data = json.loads(raw.decode('utf-8'))
                    print(f"Direct JSON OK, items: {len(data) if isinstance(data, list) else type(data)}")
                except Exception as e2:
                    print(f"Direct JSON also failed: {e2}")
                    print(f"Raw first 500: {raw[:500]}")
except Exception as e:
    print(f"Request failed: {e}")

print("\nDone")
