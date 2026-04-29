import urllib.request, ssl, sys, re, json
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
h = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36', 'Accept': '*/*'}

url = 'https://www.vstats.gg/assets/AgentsRoot-L6VNZkTH.js'
print(f'Fetching {url}')
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
        print(f'  {key[:120]}...')

create_client = re.findall(r'createClient\(["\']([^"\']+)["\']\s*,\s*["\']([^"\']+)["\']', js)
if create_client:
    print('createClient calls:')
    for u, key in create_client:
        print(f'  URL: {u}')
        print(f'  Key: {key[:120]}...')

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

url_patterns = re.findall(r'["\']([^"\']*(?:statistics|api|data|\.json)[^"\']*)["\']', js)
if url_patterns:
    print(f'URL/API patterns ({len(set(url_patterns))}):')
    for u in sorted(set(url_patterns)):
        print(f'  {u}')

domain_urls = re.findall(r'https?://[a-zA-Z0-9._:/-]+', js)
if domain_urls:
    print(f'All URLs ({len(set(domain_urls))}):')
    for u in sorted(set(domain_urls)):
        print(f'  {u}')

print(f'\n=== Full JS content (first 5000 chars) ===')
print(js[:5000])
print(f'\n=== Full JS content (last 3000 chars) ===')
print(js[-3000:])
