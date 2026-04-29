import urllib.request
import gzip
import ssl
import json
import sys
import struct

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': '*/*',
    'Accept-Encoding': 'identity',
    'Referer': 'https://www.vstats.gg/agents',
}

def fetch_raw(url):
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=30, context=ctx) as resp:
            status = resp.status
            resp_headers = dict(resp.headers)
            raw = resp.read()
            return status, resp_headers, raw
    except Exception as e:
        return None, None, f"Error: {e}".encode()

results = []

url = 'https://www.vstats.gg/statistics/agents/ALL/agents.json.gz'
status, resp_headers, raw = fetch_raw(url)
results.append(f"URL: {url}")
results.append(f"Status: {status}")
results.append(f"Headers: {json.dumps(resp_headers, indent=2) if resp_headers else 'None'}")
results.append(f"Raw length: {len(raw)}")
results.append(f"First 20 bytes hex: {raw[:20].hex() if isinstance(raw, bytes) else 'N/A'}")

if isinstance(raw, bytes):
    if raw[:2] == b'\x1f\x8b':
        results.append("Format: GZIP")
        try:
            data = gzip.decompress(raw)
            results.append(f"Decompressed: {len(data)} bytes")
            results.append(f"First 500: {data[:500].decode('utf-8', errors='replace')}")
        except Exception as e:
            results.append(f"GZIP decompress error: {e}")
    elif raw[:2] == b'{"':
        results.append("Format: JSON")
        results.append(f"Content: {raw[:500].decode('utf-8', errors='replace')}")
    else:
        results.append(f"Format: Unknown (first bytes: {raw[:4].hex()})")
        try:
            text = raw.decode('utf-8', errors='replace')
            results.append(f"As text: {text[:500]}")
        except:
            results.append("Cannot decode as text")

results.append("\n=== Trying without .gz extension ===")
url2 = 'https://www.vstats.gg/statistics/agents/ALL/agents.json'
status2, headers2, raw2 = fetch_raw(url2)
results.append(f"Status: {status2}")
results.append(f"Headers: {json.dumps(headers2, indent=2) if headers2 else 'None'}")
results.append(f"Raw length: {len(raw2)}")
if isinstance(raw2, bytes):
    results.append(f"First 20 bytes hex: {raw2[:20].hex()}")
    try:
        text = raw2.decode('utf-8', errors='replace')
        results.append(f"As text: {text[:500]}")
    except:
        pass

results.append("\n=== Trying with act parameter ===")
url3 = 'https://www.vstats.gg/statistics/agents/9d85c932-4820-c060-09c3-668636d4df1b/agents.json.gz'
status3, headers3, raw3 = fetch_raw(url3)
results.append(f"Status: {status3}")
results.append(f"Raw length: {len(raw3)}")
if isinstance(raw3, bytes):
    results.append(f"First 20 bytes hex: {raw3[:20].hex()}")
    try:
        text = raw3.decode('utf-8', errors='replace')
        results.append(f"As text: {text[:500]}")
    except:
        pass

results.append("\n=== Trying CloudFront direct ===")
url4 = 'https://d1v2g68kq1p5ip.cloudfront.net/statistics/agents/ALL/agents.json.gz'
status4, headers4, raw4 = fetch_raw(url4)
results.append(f"Status: {status4}")
results.append(f"Raw length: {len(raw4)}")
if isinstance(raw4, bytes):
    results.append(f"First 20 bytes hex: {raw4[:20].hex()}")

with open('d:/TRAE/valorant-stats-dashboard/cdn_debug.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(results))

print('\n'.join(results))
