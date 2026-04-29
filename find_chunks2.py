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
}

def fetch_url(url):
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=30, context=ctx) as resp:
            raw = resp.read()
            try:
                return gzip.decompress(raw).decode('utf-8', errors='replace')
            except:
                try:
                    return raw.decode('utf-8', errors='replace')
                except:
                    return None
    except Exception as e:
        return f"Error: {e}"

results = []

with open('d:/TRAE/valorant-stats-dashboard/vstats_index_js.txt', 'r', encoding='utf-8') as f:
    js = f.read()

chunk_files = re.findall(r'/assets/([A-Za-z0-9_-]+-[A-Za-z0-9_-]+\.js)', js)
results.append(f"Chunk file references: {len(chunk_files)}")
for cf in sorted(set(chunk_files)):
    results.append(f"  {cf}")

html = fetch_url('https://www.vstats.gg/agents')
if html and not html.startswith('Error'):
    link_tags = re.findall(r'href="([^"]*)"', html)
    results.append(f"\nAll hrefs: {len(link_tags)}")
    for lt in link_tags:
        results.append(f"  {lt}")
else:
    results.append(f"HTML fetch failed: {html}")

vite_manifest = fetch_url('https://www.vstats.gg/.vite/manifest.json')
if vite_manifest and not vite_manifest.startswith('Error'):
    results.append(f"\nVite manifest found! Length: {len(vite_manifest)}")
    try:
        manifest = json.loads(vite_manifest)
        for key, val in manifest.items():
            results.append(f"  {key}: {json.dumps(val)[:200]}")
    except:
        results.append(f"  First 1000: {vite_manifest[:1000]}")
else:
    results.append(f"\nVite manifest: {vite_manifest}")

results.append("\n=== Trying chunk files ===")
chunk_pattern = re.findall(r'"([A-Za-z0-9]+-[A-Za-z0-9]+)"', js[:5000])
results.append(f"Potential chunk IDs from first 5000 chars: {chunk_pattern[:20]}")

dynamic_chunks = re.findall(r'import\(\s*["\']([^"\']+)["\']\s*\)', js)
results.append(f"\nDynamic imports: {len(dynamic_chunks)}")
for di in sorted(set(dynamic_chunks)):
    results.append(f"  {di}")

with open('d:/TRAE/valorant-stats-dashboard/chunk_analysis.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(results))

print("Done! Results saved to chunk_analysis.txt")
