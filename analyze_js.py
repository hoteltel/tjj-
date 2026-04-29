import urllib.request
import json
import ssl
import sys
import re

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Referer': 'https://www.vstats.gg/agents',
}

results = []

def fetch_url(url):
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=30, context=ctx) as resp:
            return resp.read().decode('utf-8', errors='replace')
    except Exception as e:
        return f"Error: {e}"

js_content = fetch_url('https://www.vstats.gg/assets/index-VdEKILD-.js')
if js_content and not js_content.startswith('Error'):
    results.append(f"JS length: {len(js_content)}")
    
    supabase_urls = re.findall(r'(https?://[a-zA-Z0-9._-]+supabase[a-zA-Z0-9./_-]*)', js_content)
    if supabase_urls:
        results.append("Supabase URLs:")
        for url in set(supabase_urls):
            results.append(f"  {url}")
    
    api_keys = re.findall(r'eyJ[a-zA-Z0-9._-]{20,}', js_content)
    if api_keys:
        results.append(f"Found {len(api_keys)} potential JWT API keys:")
        for key in api_keys[:5]:
            results.append(f"  {key[:80]}...")
    
    fetch_urls = re.findall(r'fetch\(["\']([^"\']+)["\']', js_content)
    if fetch_urls:
        results.append(f"Fetch URLs found ({len(fetch_urls)}):")
        for url in fetch_urls[:20]:
            results.append(f"  {url}")
    
    api_urls = re.findall(r'["\'](/api/[^"\']+)["\']', js_content)
    if api_urls:
        results.append(f"API URLs found ({len(api_urls)}):")
        for url in api_urls[:20]:
            results.append(f"  {url}")
    
    statistics_urls = re.findall(r'["\'](/statistics/[^"\']+)["\']', js_content)
    if statistics_urls:
        results.append(f"Statistics URLs found ({len(statistics_urls)}):")
        for url in statistics_urls[:20]:
            results.append(f"  {url}")
    
    json_gz_patterns = re.findall(r'["\']([^"\']*\.json\.gz)["\']', js_content)
    if json_gz_patterns:
        results.append(f"JSON.GZ patterns found ({len(json_gz_patterns)}):")
        for url in json_gz_patterns[:20]:
            results.append(f"  {url}")
    
    create_client = re.findall(r'createClient\(["\']([^"\']+)["\']', js_content)
    if create_client:
        results.append(f"Supabase createClient URLs:")
        for url in create_client:
            results.append(f"  {url}")
    
    from_patterns = re.findall(r'from\(["\']([^"\']+)["\']\)', js_content)
    if from_patterns:
        results.append(f"Supabase from() tables ({len(from_patterns)}):")
        for table in set(from_patterns):
            results.append(f"  {table}")
    
    select_patterns = re.findall(r'\.select\(["\']([^"\']+)["\']\)', js_content)
    if select_patterns:
        results.append(f"Select patterns ({len(select_patterns)}):")
        for sel in select_patterns[:10]:
            results.append(f"  {sel}")
    
    env_patterns = re.findall(r'(VITE_[A-Z_]+)\s*[:=]', js_content)
    if env_patterns:
        results.append(f"VITE env vars: {set(env_patterns)}")
    
    url_patterns = re.findall(r'["\'](https?://[^"\']{10,})["\']', js_content)
    if url_patterns:
        results.append(f"All URLs found ({len(url_patterns)}):")
        for url in sorted(set(url_patterns)):
            results.append(f"  {url}")
    
    results.append("\n=== SEARCHING FOR DATA LOADING PATTERNS ===")
    data_load = re.findall(r'(?:load|fetch|get)[A-Za-z]*[Dd]ata[^{]{0,50}\{[^}]{0,200}', js_content)
    if data_load:
        results.append(f"Data loading patterns ({len(data_load)}):")
        for dl in data_load[:5]:
            results.append(f"  {dl[:200]}")
    
    agent_table = re.findall(r'[Aa]gent[^a-z]{0,30}(?:table|data|list|stats)', js_content)
    if agent_table:
        results.append(f"Agent table patterns: {agent_table[:10]}")
    
    chunked = [js_content[i:i+500] for i in range(0, min(len(js_content), 5000), 500)]
    results.append("\n=== FIRST 5000 CHARS OF JS ===")
    for i, chunk in enumerate(chunked):
        results.append(f"\n--- Chunk {i} ---")
        results.append(chunk[:300])

with open(r'd:\TRAE\valorant-stats-dashboard\vstats_js_analysis.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(results))

print("JS analysis saved")
