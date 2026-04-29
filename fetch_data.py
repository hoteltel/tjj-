import urllib.request
import json
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

urls = [
    "https://www.vstats.gg/api/agents",
    "https://www.vstats.gg/api/agents?table=agents",
    "https://api.vstats.gg/agents",
    "https://api.vstats.gg/v1/agents",
    "https://www.vstats.gg/_next/data/build-id/agents.json",
]

for url in urls:
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'application/json'
        })
        resp = urllib.request.urlopen(req, timeout=10, context=ctx)
        data = resp.read().decode('utf-8')
        print(f"URL: {url}")
        print(f"Status: {resp.status}")
        print(f"Data: {data[:500]}")
        print("---")
    except Exception as e:
        print(f"URL: {url} - Error: {e}")
        print("---")
