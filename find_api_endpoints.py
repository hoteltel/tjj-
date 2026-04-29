import urllib.request
import json
import gzip
import ssl
import re
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
}

def fetch_url(url):
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=30, context=ctx) as resp:
            raw = resp.read()
            try:
                decompressed = gzip.decompress(raw)
                return decompressed.decode('utf-8', errors='replace')
            except:
                try:
                    return raw.decode('utf-8', errors='replace')
                except:
                    return None
    except Exception as e:
        return f"Error: {e}"

results = []

html = fetch_url('https://www.vstats.gg/agents')
if html and not html.startswith('Error'):
    results.append(f"HTML length: {len(html)}")
    
    js_files = re.findall(r'src="(/assets/[^"]*\.js)"', html)
    results.append(f"Found {len(js_files)} JS files:")
    for js in js_files:
        results.append(f"  {js}")
    
    for js_file in js_files[:3]:
        js_url = f'https://www.vstats.gg{js_file}'
        results.append(f"\n=== Analyzing: {js_url} ===")
        js_content = fetch_url(js_url)
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
                    results.append(f"  {key[:100]}...")
            
            statistics_patterns = re.findall(r'["\'](/statistics/[^"\']+)["\']', js_content)
            if statistics_patterns:
                results.append(f"Statistics patterns ({len(statistics_patterns)}):")
                for p in sorted(set(statistics_patterns))[:30]:
                    results.append(f"  {p}")
            
            api_patterns = re.findall(r'["\'](/api/[^"\']+)["\']', js_content)
            if api_patterns:
                results.append(f"API patterns ({len(api_patterns)}):")
                for p in sorted(set(api_patterns))[:30]:
                    results.append(f"  {p}")
            
            fetch_patterns = re.findall(r'fetch\(["\']([^"\']+)["\']', js_content)
            if fetch_patterns:
                results.append(f"Fetch URLs ({len(fetch_patterns)}):")
                for url in sorted(set(fetch_patterns))[:30]:
                    results.append(f"  {url}")
            
            cdn_patterns = re.findall(r'["\'](https?://[a-zA-Z0-9._/-]+\.json\.gz)["\']', js_content)
            if cdn_patterns:
                results.append(f"CDN JSON.gz URLs ({len(cdn_patterns)}):")
                for url in sorted(set(cdn_patterns)):
                    results.append(f"  {url}")
            
            json_gz_patterns = re.findall(r'["\']([^"\']*\.json\.gz)["\']', js_content)
            if json_gz_patterns:
                results.append(f"JSON.gz patterns ({len(json_gz_patterns)}):")
                for p in sorted(set(json_gz_patterns))[:30]:
                    results.append(f"  {p}")
            
            supabase_client = re.findall(r'createClient\(["\']([^"\']+)["\']\s*,\s*["\']([^"\']+)["\']', js_content)
            if supabase_client:
                results.append("Supabase client configs:")
                for url, key in supabase_client:
                    results.append(f"  URL: {url}")
                    results.append(f"  Key: {key[:80]}...")
            
            from_patterns = re.findall(r'\.from\(["\']([^"\']+)["\']', js_content)
            if from_patterns:
                results.append(f"Supabase table names ({len(from_patterns)}):")
                for t in sorted(set(from_patterns))[:30]:
                    results.append(f"  {t}")
        else:
            results.append(f"Failed to fetch JS: {js_content}")
else:
    results.append(f"Failed to fetch HTML: {html}")

with open('d:/TRAE/valorant-stats-dashboard/vstats_api_analysis.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(results))

print('\n'.join(results))
