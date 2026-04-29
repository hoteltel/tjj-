import urllib.request, ssl, sys, re, json
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
h = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36', 'Accept': '*/*'}

url = 'https://www.vstats.gg/assets/index-BOShnSr_.js'
req = urllib.request.Request(url, headers=h)
resp = urllib.request.urlopen(req, timeout=60, context=ctx)
js = resp.read().decode('utf-8', errors='replace')

print(f'JS length: {len(js)}')
print('\n=== First 5000 chars ===')
print(js[:5000])

print('\n=== Searching for fetch function definitions ===')
fetch_defs = re.findall(r'(?:async\s+)?function\s+\w*[Ff]etch\w*\s*\([^)]*\)\s*\{[^}]{0,500}\}', js)
if fetch_defs:
    for d in fetch_defs:
        print(f'  {d[:300]}')

print('\n=== Searching for "fetch" in arrow functions ===')
arrow_fetch = re.findall(r'(?:const|let|var)\s+\w+\s*=\s*(?:async\s*)?\([^)]*\)\s*=>\s*\{?[^;]{0,300}fetch[^;]{0,200}', js)
if arrow_fetch:
    for a in arrow_fetch[:10]:
        print(f'  {a[:300]}')

print('\n=== Searching for URL construction patterns ===')
url_constructions = re.findall(r'["\']https?://[^"\']*["\']\s*\+[^;]{0,100}', js)
if url_constructions:
    for u in url_constructions[:10]:
        print(f'  {u[:200]}')

template_urls = re.findall(r'`[^`]*(?:https?://|/api|/statistics|/data)[^`]*`', js)
if template_urls:
    print('\nTemplate literal URLs:')
    for u in template_urls:
        print(f'  {u[:200]}')

print('\n=== Searching for ACTIVE_ACT / ACTIVE_PATCH ===')
active_patterns = re.findall(r'ACTIVE_[A-Z_]+\s*[:=]\s*["\']([^"\']+)["\']', js)
if active_patterns:
    for p in active_patterns:
        print(f'  {p}')

print('\n=== Searching for .json.gz or .json patterns ===')
json_gz = re.findall(r'["\']([^"\']*(?:\.json|\.gz)[^"\']*)["\']', js)
if json_gz:
    for p in sorted(set(json_gz)):
        print(f'  {p}')

print('\n=== Searching for supabase keyword ===')
supa = re.findall(r'.{0,100}supabase.{0,100}', js, re.IGNORECASE)
if supa:
    for s in supa[:10]:
        print(f'  {s[:200]}')

print('\n=== Searching for API base URL ===')
api_base = re.findall(r'(?:API_BASE|API_URL|BASE_URL|apiUrl|baseUrl)\s*[:=]\s*["\']([^"\']+)["\']', js)
if api_base:
    for a in api_base:
        print(f'  {a}')

print('\n=== Searching for statistics path ===')
stats_path = re.findall(r'["\'](/statistics[^"\']*)["\']', js)
if stats_path:
    for p in sorted(set(stats_path)):
        print(f'  {p}')

print('\n=== Searching for any function that takes map, act, type params ===')
func_patterns = re.findall(r'(?:function|const|let)\s+(\w+)\s*=\s*(?:async\s*)?\([^)]*(?:map|act|type)[^)]*\)\s*=>\s*[^;]{0,300}', js)
if func_patterns:
    for f in func_patterns[:10]:
        print(f'  {f[:300]}')
