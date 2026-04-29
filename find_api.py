import urllib.request, re, ssl, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

html_url = 'https://www.vstats.gg/agents'
try:
    req = urllib.request.Request(html_url, headers=headers)
    with urllib.request.urlopen(req, timeout=15, context=ctx) as resp:
        html = resp.read().decode('utf-8', errors='replace')
    
    js_files = re.findall(r'src="(/assets/[^"]*\.js)"', html)
    print(f'Found {len(js_files)} JS files:')
    for js in js_files:
        print(f'  {js}')
    
    if js_files:
        js_url = f'https://www.vstats.gg{js_files[0]}'
        print(f'\nFetching: {js_url}')
        req2 = urllib.request.Request(js_url, headers=headers)
        with urllib.request.urlopen(req2, timeout=30, context=ctx) as resp2:
            js_content = resp2.read().decode('utf-8', errors='replace')
        
        print(f'JS length: {len(js_content)}')
        
        supabase_urls = re.findall(r'(https?://[a-zA-Z0-9._-]+supabase[a-zA-Z0-9./_-]*)', js_content)
        if supabase_urls:
            print(f'\nSupabase URLs ({len(set(supabase_urls))}):')
            for u in set(supabase_urls):
                print(f'  {u}')
        
        api_keys = re.findall(r'eyJ[a-zA-Z0-9._-]{20,}', js_content)
        if api_keys:
            print(f'\nJWT API keys ({len(api_keys)}):')
            for k in set(api_keys):
                print(f'  {k[:100]}...')
        
        json_gz_patterns = re.findall(r'["\']([^"\']*\.json\.gz)["\']', js_content)
        if json_gz_patterns:
            print(f'\n.json.gz patterns ({len(set(json_gz_patterns))}):')
            for p in set(json_gz_patterns)[:20]:
                print(f'  {p}')
        
        fetch_patterns = re.findall(r'fetch\(["\']([^"\']+)["\']', js_content)
        if fetch_patterns:
            print(f'\nFetch URLs ({len(set(fetch_patterns))}):')
            for f in set(fetch_patterns)[:20]:
                print(f'  {f}')
        
        cdn_patterns = re.findall(r'(https?://[a-zA-Z0-9._-]+cloudfront[a-zA-Z0-9./_-]*)', js_content)
        if cdn_patterns:
            print(f'\nCloudFront URLs ({len(set(cdn_patterns))}):')
            for c in set(cdn_patterns):
                print(f'  {c}')
        
        stat_patterns = re.findall(r'["\'](/statistics/[^"\']+)["\']', js_content)
        if stat_patterns:
            print(f'\n/statistics/ patterns ({len(set(stat_patterns))}):')
            for s in set(stat_patterns)[:30]:
                print(f'  {s}')

except Exception as e:
    print(f'ERROR: {e}')
