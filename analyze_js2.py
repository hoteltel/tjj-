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

template_literals = re.findall(r'`[^`]*\$\{[^}]*\}[^`]*`', js)
if template_literals:
    print(f'\nTemplate literals with variables ({len(template_literals)}):')
    for t in template_literals[:30]:
        print(f'  {t[:200]}')

import_patterns = re.findall(r'import\([^)]+\)', js)
if import_patterns:
    print(f'\nDynamic imports ({len(import_patterns)}):')
    for i in import_patterns:
        print(f'  {i[:200]}')

window_patterns = re.findall(r'window\.([a-zA-Z_][a-zA-Z0-9_]*)\s*=', js)
if window_patterns:
    print(f'\nWindow variables ({len(set(window_patterns))}):')
    for w in sorted(set(window_patterns)):
        print(f'  {w}')

json_patterns = re.findall(r'\.json', js)
print(f'\n.json occurrences: {len(json_patterns)}')

gz_patterns = re.findall(r'\.gz', js)
print(f'.gz occurrences: {len(gz_patterns)}')

cdn_patterns = re.findall(r'cdn', js, re.IGNORECASE)
print(f'cdn occurrences: {len(cdn_patterns)}')

data_patterns = re.findall(r'["\']data["\']', js)
print(f'"data" occurrences: {len(data_patterns)}')

api_patterns = re.findall(r'["\']api["\']', js)
print(f'"api" occurrences: {len(api_patterns)}')

agent_patterns = re.findall(r'["\']agent[s]?["\']', js)
print(f'"agent(s)" occurrences: {len(agent_patterns)}')

print('\n--- Searching for data loading patterns ---')
load_patterns = re.findall(r'.{0,50}(fetch|axios|XMLHttpRequest|\.get|\.post).{0,100}', js)
if load_patterns:
    print(f'HTTP request patterns ({len(load_patterns)}):')
    for p in load_patterns[:20]:
        print(f'  {p[:200]}')
