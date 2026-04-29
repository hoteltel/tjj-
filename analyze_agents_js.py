import urllib.request, re, ssl, sys, json
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

js_url = 'https://www.vstats.gg/assets/AgentsRoot-L6VNZkTH.js'
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
    print(f'\nTemplate literals ({len(template_literals)}):')
    for t in template_literals[:30]:
        print(f'  {t[:300]}')

fetch_patterns = re.findall(r'.{0,80}fetch.{0,150}', js)
if fetch_patterns:
    print(f'\nFetch patterns ({len(fetch_patterns)}):')
    for p in fetch_patterns[:10]:
        print(f'  {p[:300]}')

json_gz = re.findall(r'["\']([^"\']*\.json[^"\']*)["\']', js)
if json_gz:
    print(f'\nJSON file references ({len(set(json_gz))}):')
    for j in sorted(set(json_gz)):
        print(f'  {j}')

supabase = re.findall(r'(supabase[a-zA-Z_]*)\s*[:=]\s*["\']([^"\']+)["\']', js)
if supabase:
    print(f'\nSupabase config:')
    for name, val in supabase:
        print(f'  {name} = {val}')

api_keys = re.findall(r'eyJ[a-zA-Z0-9._-]{20,}', js)
if api_keys:
    print(f'\nJWT keys ({len(set(api_keys))}):')
    for k in set(api_keys):
        print(f'  {k[:120]}...')

print('\n--- Searching for data variable names ---')
wr_patterns = re.findall(r'["\']wr["\']', js)
print(f'"wr" occurrences: {len(wr_patterns)}')
pr_patterns = re.findall(r'["\']pr["\']', js)
print(f'"pr" occurrences: {len(pr_patterns)}')
kd_patterns = re.findall(r'["\']kd["\']', js)
print(f'"kd" occurrences: {len(kd_patterns)}')
agent_patterns = re.findall(r'["\']agent["\']', js)
print(f'"agent" occurrences: {len(agent_patterns)}')
matches_patterns = re.findall(r'["\']matches["\']', js)
print(f'"matches" occurrences: {len(matches_patterns)}')

print('\n--- First 3000 chars ---')
print(js[:3000])

print('\n--- Last 2000 chars ---')
print(js[-2000:])
