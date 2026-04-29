import urllib.request
import gzip
import ssl
import re
import json
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.vstats.gg/agents',
    'Origin': 'https://www.vstats.gg',
}

def fetch_url_raw(url):
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=30, context=ctx) as resp:
            return resp.read()
    except Exception as e:
        return f"Error: {e}".encode()

results = []

with open('d:/TRAE/valorant-stats-dashboard/vstats_index_js.txt', 'r', encoding='utf-8') as f:
    js = f.read()

act_patterns = re.findall(r'ACTIVE_ACT\s*[:=]\s*["\']([^"\']+)["\']', js)
results.append(f"ACTIVE_ACT patterns: {act_patterns}")

act_patterns2 = re.findall(r'ACT[_A-Z]*\s*[:=]\s*["\']([^"\']+)["\']', js)
results.append(f"ACT patterns: {act_patterns2}")

const_patterns = re.findall(r'(ACTIVE_[A-Z_]+)\s*[:=]\s*["\']([^"\']+)["\']', js)
results.append(f"ACTIVE constants: {const_patterns}")

map_patterns = re.findall(r'(MAP_[A-Z_]+)\s*[:=]\s*["\']([^"\']+)["\']', js)
results.append(f"MAP constants: {map_patterns}")

rank_patterns = re.findall(r'(RANK_[A-Z_]+)\s*[:=]\s*["\']([^"\']+)["\']', js)
results.append(f"RANK constants: {rank_patterns}")

category_patterns = re.findall(r'(CATEGORY_[A-Z_]+)\s*[:=]\s*["\']([^"\']+)["\']', js)
results.append(f"CATEGORY constants: {category_patterns}")

table_patterns = re.findall(r'(TABLE_[A-Z_]+)\s*[:=]\s*["\']([^"\']+)["\']', js)
results.append(f"TABLE constants: {table_patterns}")

results.append("\n=== Trying API endpoints ===")

base_urls = [
    'https://www.vstats.gg/statistics/agents/ALL/agents.json.gz',
    'https://www.vstats.gg/statistics/agents/ALL/duos.json.gz',
    'https://www.vstats.gg/statistics/agents/ALL/comps.json.gz',
    'https://www.vstats.gg/statistics/agents/ALL/maps.json.gz',
    'https://www.vstats.gg/statistics/maps/ALL/maps.json.gz',
    'https://www.vstats.gg/statistics/plants/ALL/plants.json.gz',
    'https://www.vstats.gg/statistics/weapons/ALL/weapons.json.gz',
]

for url in base_urls:
    results.append(f"\n--- {url} ---")
    raw = fetch_url_raw(url)
    if isinstance(raw, bytes):
        results.append(f"Raw bytes: {len(raw)}")
        try:
            decompressed = gzip.decompress(raw)
            data = json.loads(decompressed)
            results.append(f"Success! {len(data)} entries")
            if isinstance(data, list) and len(data) > 0:
                results.append(f"First entry keys: {list(data[0].keys())}")
                for item in sorted(data, key=lambda x: x.get('wr', 0), reverse=True)[:5]:
                    results.append(f"  {item}")
        except gzip.BadGzipFile:
            try:
                data = json.loads(raw.decode('utf-8'))
                results.append(f"Success (no gzip)! {len(data)} entries")
                if isinstance(data, list) and len(data) > 0:
                    results.append(f"First entry keys: {list(data[0].keys())}")
            except:
                results.append(f"Not JSON. First 200: {raw[:200]}")
        except json.JSONDecodeError:
            results.append(f"Decompressed but not JSON. First 200: {decompressed[:200]}")
        except Exception as e:
            results.append(f"Error: {e}")
    else:
        results.append(f"Failed: {raw}")

with open('d:/TRAE/valorant-stats-dashboard/api_endpoint_results.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(results))

print('\n'.join(results))
