import urllib.request, json, ssl, sys, re
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
h = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36', 'Accept': '*/*'}

print('=== Fetching vstats.gg HTML ===')
req = urllib.request.Request('https://www.vstats.gg/agents', headers=h)
resp = urllib.request.urlopen(req, timeout=30, context=ctx)
html = resp.read().decode('utf-8', errors='replace')
print(f'HTML length: {len(html)}')

js_files = re.findall(r'src="(/assets/[^"]*\.js)"', html)
print(f'Found {len(js_files)} JS files:')
for js in js_files:
    print(f'  {js}')

if js_files:
    for js_file in js_files[:2]:
        url = f'https://www.vstats.gg{js_file}'
        print(f'\n=== Fetching {url} ===')
        try:
            req = urllib.request.Request(url, headers=h)
            resp = urllib.request.urlopen(req, timeout=60, context=ctx)
            js_content = resp.read().decode('utf-8', errors='replace')
            print(f'JS length: {len(js_content)}')
            
            supabase_urls = re.findall(r'(https?://[a-zA-Z0-9._-]+supabase[a-zA-Z0-9./_-]*)', js_content)
            if supabase_urls:
                print('Supabase URLs:')
                for u in set(supabase_urls):
                    print(f'  {u}')
            
            api_keys = re.findall(r'eyJ[a-zA-Z0-9._-]{20,}', js_content)
            if api_keys:
                print(f'Found {len(api_keys)} potential JWT API keys:')
                for key in api_keys[:5]:
                    print(f'  {key[:80]}...')
            
            supabase_config = re.findall(r'(supabase[A-Za-z]*\s*[:=]\s*["\']([^"\']+)["\'])', js_content)
            if supabase_config:
                print('Supabase config:')
                for name, val in supabase_config:
                    print(f'  {name} = {val}')
            
            create_client = re.findall(r'createClient\(["\']([^"\']+)["\']\s*,\s*["\']([^"\']+)["\']', js_content)
            if create_client:
                print('createClient calls:')
                for url, key in create_client:
                    print(f'  URL: {url}')
                    print(f'  Key: {key[:80]}...')
            
            from_pattern = re.findall(r'\.from\(["\']([^"\']+)["\']', js_content)
            if from_pattern:
                print(f'Supabase table names ({len(set(from_pattern))}):')
                for table in sorted(set(from_pattern)):
                    print(f'  {table}')
            
            rpc_pattern = re.findall(r'\.rpc\(["\']([^"\']+)["\']', js_content)
            if rpc_pattern:
                print(f'RPC function names ({len(set(rpc_pattern))}):')
                for rpc in sorted(set(rpc_pattern)):
                    print(f'  {rpc}')
                    
        except Exception as e:
            print(f'Error: {e}')
