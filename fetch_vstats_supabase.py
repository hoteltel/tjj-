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

results.append("=== FETCHING VSTATS.GG HTML ===")
html = fetch_url('https://www.vstats.gg/agents')
if html and not html.startswith('Error'):
    results.append(f"HTML length: {len(html)}")
    
    js_files = re.findall(r'src="(/assets/[^"]*\.js)"', html)
    results.append(f"Found {len(js_files)} JS files:")
    for js in js_files:
        results.append(f"  {js}")
    
    supabase_patterns = re.findall(r'(supabase[a-zA-Z]*|SUPABASE[a-zA-Z_]*)\s*[:=]\s*["\']([^"\']+)["\']', html)
    if supabase_patterns:
        results.append("Supabase patterns found:")
        for name, val in supabase_patterns:
            results.append(f"  {name} = {val}")
    
    api_patterns = re.findall(r'(https?://[a-zA-Z0-9._-]+supabase[a-zA-Z0-9./_-]*)', html)
    if api_patterns:
        results.append("Supabase URLs found:")
        for url in api_patterns:
            results.append(f"  {url}")
    
    key_patterns = re.findall(r'["\']([a-zA-Z0-9._-]{30,})["\']', html)
    if key_patterns:
        results.append(f"Found {len(key_patterns)} potential API keys (first 5):")
        for key in key_patterns[:5]:
            results.append(f"  {key[:20]}...")
    
    data_patterns = re.findall(r'window\.__[A-Z_]+\s*=\s*({[^;]+})', html)
    if data_patterns:
        results.append(f"Found {len(data_patterns)} window data patterns")
        for dp in data_patterns[:2]:
            results.append(f"  {dp[:200]}...")
else:
    results.append(f"Failed to fetch HTML: {html}")

for js_file in js_files[:3]:
    results.append(f"\n=== FETCHING JS: {js_file} ===")
    js_content = fetch_url(f'https://www.vstats.gg{js_file}')
    if js_content and not js_content.startswith('Error'):
        results.append(f"JS length: {len(js_content)}")
        
        supabase_urls = re.findall(r'(https?://[a-zA-Z0-9._-]+supabase[a-zA-Z0-9./_-]*)', js_content)
        if supabase_urls:
            results.append("Supabase URLs:")
            for url in set(supabase_urls):
                results.append(f"  {url}")
        
        api_keys = re.findall(r'["\']eyJ[a-zA-Z0-9._-]+["\']', js_content)
        if api_keys:
            results.append(f"Found {len(api_keys)} potential JWT API keys:")
            for key in api_keys[:3]:
                results.append(f"  {key[:50]}...")
        
        agent_patterns = re.findall(r'agents?[/_-]?(?:json|data|stats|table)', js_content, re.IGNORECASE)
        if agent_patterns:
            results.append(f"Agent-related patterns: {agent_patterns[:5]}")
        
        fetch_patterns = re.findall(r'fetch\(["\']([^"\']+)["\']', js_content)
        if fetch_patterns:
            results.append(f"Fetch URLs found ({len(fetch_patterns)}):")
            for url in fetch_patterns[:10]:
                results.append(f"  {url}")
        
        api_url_patterns = re.findall(r'["\'](/api/[^"\']+)["\']', js_content)
        if api_url_patterns:
            results.append(f"API URLs found ({len(api_url_patterns)}):")
            for url in api_url_patterns[:10]:
                results.append(f"  {url}")
        
        statistics_patterns = re.findall(r'["\'](/statistics/[^"\']+)["\']', js_content)
        if statistics_patterns:
            results.append(f"Statistics URLs found ({len(statistics_patterns)}):")
            for url in statistics_patterns[:10]:
                results.append(f"  {url}")
    else:
        results.append(f"Failed: {js_content[:100]}")

with open(r'd:\TRAE\valorant-stats-dashboard\vstats_analysis.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(results))

print("Analysis saved to vstats_analysis.txt")
