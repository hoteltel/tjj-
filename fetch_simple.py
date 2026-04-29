import urllib.request
import ssl
import json
import gzip

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'https://www.vstats.gg/agents'
}

url = 'https://www.vstats.gg/statistics/agents/ALL/agents.json.gz'
try:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30, context=ctx) as resp:
        raw = resp.read()
        print(f"Raw response length: {len(raw)}")
        print(f"First 20 bytes: {raw[:20]}")
        
        try:
            decompressed = gzip.decompress(raw)
            print(f"Decompressed length: {len(decompressed)}")
            data = json.loads(decompressed.decode('utf-8'))
            print(f"Type: {type(data)}")
            if isinstance(data, list):
                print(f"Count: {len(data)}")
                if len(data) > 0:
                    print(f"First item keys: {list(data[0].keys())}")
                    print(f"First item: {json.dumps(data[0], ensure_ascii=True)}")
            with open(r'd:\TRAE\valorant-stats-dashboard\vstats_all_agents.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=True, indent=2)
            print("Saved to vstats_all_agents.json")
        except Exception as e:
            print(f"Decompression error: {e}")
            try:
                text = raw.decode('utf-8')
                print(f"Text length: {len(text)}")
                print(f"First 500 chars: {text[:500]}")
            except:
                print(f"Cannot decode as text")
except Exception as e:
    print(f"Request error: {e}")
