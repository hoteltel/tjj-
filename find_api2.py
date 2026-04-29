import urllib.request, ssl, sys, re, json
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
h = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36', 'Accept': '*/*'}

files_to_check = [
    'assets/AgentsRoot-L6VNZkTH.js',
    'assets/index-BOShnSr_.js',
    'assets/RankFilter-DbuGoLBS.js',
    'assets/AgentsSelection-BHqv_PPo.js',
]

for f in files_to_check:
    url = f'https://www.vstats.gg/{f}'
    print(f'\n=== {url} ===')
    try:
        req = urllib.request.Request(url, headers=h)
        resp = urllib.request.urlopen(req, timeout=60, context=ctx)
        js = resp.read().decode('utf-8', errors='replace')
        print(f'Length: {len(js)}')
        
        supabase_urls = re.findall(r'(https?://[a-zA-Z0-9._-]+supabase[a-zA-Z0-9./_-]*)', js)
        if supabase_urls:
            print('Supabase URLs:')
            for u in set(supabase_urls):
                print(f'  {u}')
        
        api_keys = re.findall(r'eyJ[a-zA-Z0-9._-]{20,}', js)
        if api_keys:
            print(f'JWT API keys ({len(api_keys)}):')
            for key in api_keys[:5]:
                print(f'  {key[:100]}...')
        
        create_client = re.findall(r'createClient\(["\']([^"\']+)["\']\s*,\s*["\']([^"\']+)["\']', js)
        if create_client:
            print('createClient calls:')
            for url, key in create_client:
                print(f'  URL: {url}')
                print(f'  Key: {key[:100]}...')
        
        from_tables = re.findall(r'\.from\(["\']([^"\']+)["\']', js)
        if from_tables:
            print(f'Supabase tables ({len(set(from_tables))}):')
            for table in sorted(set(from_tables)):
                print(f'  {table}')
        
        rpc_funcs = re.findall(r'\.rpc\(["\']([^"\']+)["\']', js)
        if rpc_funcs:
            print(f'RPC functions ({len(set(rpc_funcs))}):')
            for rpc in sorted(set(rpc_funcs)):
                print(f'  {rpc}')
        
        fetch_urls = re.findall(r'fetch\(["\']([^"\']+)["\']', js)
        if fetch_urls:
            print(f'Fetch URLs ({len(fetch_urls)}):')
            for u in set(fetch_urls):
                print(f'  {u}')
        
        url_patterns = re.findall(r'["\'](/(?:api|statistics|data|v1)/[^"\']*)["\']', js)
        if url_patterns:
            print(f'API URL patterns ({len(set(url_patterns))}):')
            for u in sorted(set(url_patterns)):
                print(f'  {u}')
        
        json_patterns = re.findall(r'["\']([^"\']*\.json[^"\']*)["\']', js)
        if json_patterns:
            print(f'JSON patterns ({len(set(json_patterns))}):')
            for p in sorted(set(json_patterns)):
                print(f'  {p}')
        
        domain_urls = re.findall(r'https?://[a-zA-Z0-9._:/-]+', js)
        if domain_urls:
            print(f'All URLs ({len(set(domain_urls))}):')
            for u in sorted(set(domain_urls)):
                print(f'  {u}')
        
        if not supabase_urls and not api_keys and not create_client and not from_tables and not fetch_urls and not url_patterns and not json_patterns and not domain_urls:
            print('No data patterns found. Showing first 3000 chars:')
            print(js[:3000])
    except Exception as e:
        print(f'Error: {e}')
