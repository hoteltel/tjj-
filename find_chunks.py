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

with open('d:/TRAE/valorant-stats-dashboard/vstats_index_js.txt', 'r', encoding='utf-8') as f:
    js = f.read()

chunk_map = re.findall(r'"([A-Za-z0-9_-]{6,20})":\s*\(\s*\)\s*=>\s*import\(', js)
print(f"Chunk references found: {len(chunk_map)}")

vite_map = re.findall(r'__vite__mapDeps\(\[([^\]]+)\]\)', js)
print(f"Vite map deps found: {len(vite_map)}")

manifest_match = re.search(r'\{[^}]*"file"\s*:\s*"[^"]*"[^}]*\}', js[:2000])
if manifest_match:
    print(f"Manifest pattern: {manifest_match.group()[:200]}")

chunk_files = re.findall(r'/assets/([A-Za-z0-9_-]+-[A-Za-z0-9_-]+\.js)', js)
print(f"Chunk file references: {len(chunk_files)}")
for cf in sorted(set(chunk_files)):
    print(f"  {cf}")

html = fetch_url('https://www.vstats.gg/agents')
if html and not html.startswith('Error'):
    link_tags = re.findall(r'link[^>]*href="([^"]*)"', html)
    print(f"\nLink tags: {len(link_tags)}")
    for lt in link_tags:
        print(f"  {lt}")
    
    script_tags = re.findall(r'script[^>]*src="([^"]*)"', html)
    print(f"\nScript tags: {len(script_tags)}")
    for st in script_tags:
        print(f"  {st}")

    modulepreload = re.findall(r'modulepreload[^>]*href="([^"]*)"', html)
    print(f"\nModule preloads: {len(modulepreload)}")
    for mp in modulepreload:
        print(f"  {mp}")

vite_manifest = fetch_url('https://www.vstats.gg/.vite/manifest.json')
if vite_manifest and not vite_manifest.startswith('Error'):
    print(f"\nVite manifest found! Length: {len(vite_manifest)}")
    try:
        manifest = json.loads(vite_manifest)
        for key, val in manifest.items():
            if 'agent' in key.lower() or 'stat' in key.lower():
                print(f"  {key}: {val}")
    except:
        print(f"  First 500: {vite_manifest[:500]}")
else:
    print(f"\nVite manifest: {vite_manifest}")

for chunk_id in range(0, 40):
    chunk_url = f'https://www.vstats.gg/assets/index-{chunk_id}.js'
    content = fetch_url(chunk_url)
    if content and not content.startswith('Error') and len(content) > 100:
        if 'agent' in content.lower() and ('fetch' in content.lower() or 'supabase' in content.lower() or 'json.gz' in content.lower()):
            print(f"\n=== Chunk {chunk_id} (len={len(content)}) has data fetching! ===")
            urls = re.findall(r'["\']([^"\']*(?:json|api|supabase|statistics)[^"\']*)["\']', content)
            for u in sorted(set(urls))[:20]:
                print(f"  {u}")
