import urllib.request, re, ssl, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

js_url = 'https://www.vstats.gg/assets/index-VdEKILD-.js'
req = urllib.request.Request(js_url, headers=headers)
with urllib.request.urlopen(req, timeout=30, context=ctx) as resp:
    js = resp.read().decode('utf-8', errors='replace')

print(f'JS length: {len(js)}')

all_urls = re.findall(r'(https?://[a-zA-Z0-9._/:-]+)', js)
if all_urls:
    print(f'\nAll URLs ({len(set(all_urls))}):')
    for u in sorted(set(all_urls)):
        print(f'  {u}')

cdn_patterns = re.findall(r'["\']([a-zA-Z0-9._-]+\.cloudfront\.net[^"\']*)["\']', js)
if cdn_patterns:
    print(f'\nCloudFront domains:')
    for c in set(cdn_patterns):
        print(f'  {c}')

domain_patterns = re.findall(r'["\']([a-zA-Z0-9._-]+\.[a-z]{2,}[^"\']*)["\']', js)
if domain_patterns:
    print(f'\nDomain-like strings ({len(set(domain_patterns))}):')
    for d in sorted(set(domain_patterns)):
        if '.' in d and not d.startswith('/') and not d.startswith('{'):
            print(f'  {d}')

base_url_patterns = re.findall(r'(base_?url|api_?url|cdn_?url|data_?url|host)\s*[:=]\s*["\']([^"\']+)["\']', js, re.IGNORECASE)
if base_url_patterns:
    print(f'\nBase URL patterns:')
    for name, val in base_url_patterns:
        print(f'  {name} = {val}')

env_patterns = re.findall(r'import\.meta\.env\.([A-Z_]+)', js)
if env_patterns:
    print(f'\nEnv variables ({len(set(env_patterns))}):')
    for e in sorted(set(env_patterns)):
        print(f'  {e}')

print('\n--- Searching for statistics-related code ---')
stat_code = re.findall(r'.{0,100}statistics.{0,100}', js)
if stat_code:
    print(f'Statistics references ({len(stat_code)}):')
    for s in stat_code[:10]:
        print(f'  {s[:300]}')

print('\n--- Searching for .json.gz references ---')
gz_code = re.findall(r'.{0,100}\.json\.gz.{0,100}', js)
if gz_code:
    print(f'.json.gz references ({len(gz_code)}):')
    for g in gz_code[:10]:
        print(f'  {g[:300]}')

print('\n--- First 3000 chars ---')
print(js[:3000])
