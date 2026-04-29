import urllib.request
import gzip
import ssl
import re
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': '*/*',
    'Referer': 'https://www.vstats.gg/agents',
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

chunk_files = [
    'AgentsRoot-L6VNZkTH.js',
    'index-BOShnSr_.js',
    'RankFilter-DbuGoLBS.js',
    'MapFilter.vue_vue_type_script_setup_true_lang-Cj7mJLos.js',
    'AgentsSelection-BHqv_PPo.js',
    'EcoFilter-NhLvtnaJ.js',
]

for chunk in chunk_files:
    url = f'https://www.vstats.gg/assets/{chunk}'
    results.append(f"\n=== {chunk} ===")
    content = fetch_url(url)
    if content and not content.startswith('Error'):
        results.append(f"Length: {len(content)}")
        
        supabase_urls = re.findall(r'(https?://[a-zA-Z0-9._-]+supabase[a-zA-Z0-9./_-]*)', content)
        if supabase_urls:
            results.append("Supabase URLs:")
            for u in set(supabase_urls):
                results.append(f"  {u}")
        
        api_keys = re.findall(r'eyJ[a-zA-Z0-9._-]{20,}', content)
        if api_keys:
            results.append(f"JWT API keys ({len(api_keys)}):")
            for key in api_keys[:5]:
                results.append(f"  {key[:100]}...")
        
        supabase_client = re.findall(r'createClient\(["\']([^"\']+)["\']\s*,\s*["\']([^"\']+)["\']', content)
        if supabase_client:
            results.append("Supabase client configs:")
            for url, key in supabase_client:
                results.append(f"  URL: {url}")
                results.append(f"  Key: {key[:100]}...")
        
        from_patterns = re.findall(r'\.from\(["\']([^"\']+)["\']', content)
        if from_patterns:
            results.append(f"Supabase tables: {sorted(set(from_patterns))}")
        
        fetch_patterns = re.findall(r'fetch\(["\']([^"\']+)["\']', content)
        if fetch_patterns:
            results.append(f"Fetch URLs: {sorted(set(fetch_patterns))}")
        
        json_urls = re.findall(r'["\']([^"\']*(?:\.json|statistics|api)[^"\']*)["\']', content)
        if json_urls:
            results.append(f"JSON/API URLs: {sorted(set(json_urls))[:20]}")
        
        url_patterns = re.findall(r'["\']((https?://|/)[^"\']{5,})["\']', content)
        if url_patterns:
            results.append(f"All URLs: {sorted(set([u[0] for u in url_patterns]))[:20]}")
        
        if len(content) < 5000:
            results.append(f"Full content:\n{content}")
        else:
            results.append(f"First 3000 chars:\n{content[:3000]}")
    else:
        results.append(f"Failed: {content}")

with open('d:/TRAE/valorant-stats-dashboard/chunk_analysis2.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(results))

print("Done! Results saved.")
