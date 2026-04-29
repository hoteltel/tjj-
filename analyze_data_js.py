import urllib.request, re, ssl, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

files = [
    'https://www.vstats.gg/assets/index-BOShnSr_.js',
    'https://www.vstats.gg/assets/AgentsTable-Boik0md2.js',
]

for file_url in files:
    print(f'\n{"="*60}')
    print(f'Fetching: {file_url}')
    try:
        req = urllib.request.Request(file_url, headers=headers)
        with urllib.request.urlopen(req, timeout=30, context=ctx) as resp:
            js = resp.read().decode('utf-8', errors='replace')
        
        print(f'Length: {len(js)}')
        
        all_urls = re.findall(r'(https?://[a-zA-Z0-9._/:-]+)', js)
        if all_urls:
            print(f'URLs ({len(set(all_urls))}):')
            for u in sorted(set(all_urls)):
                print(f'  {u}')
        
        template_literals = re.findall(r'`[^`]*\$\{[^}]*\}[^`]*`', js)
        if template_literals:
            print(f'Template literals ({len(template_literals)}):')
            for t in template_literals[:20]:
                print(f'  {t[:300]}')
        
        supabase = re.findall(r'(supabase[a-zA-Z_]*)\s*[:=]\s*["\']([^"\']+)["\']', js)
        if supabase:
            print(f'Supabase config:')
            for name, val in supabase:
                print(f'  {name} = {val}')
        
        api_keys = re.findall(r'eyJ[a-zA-Z0-9._-]{20,}', js)
        if api_keys:
            print(f'JWT keys ({len(set(api_keys))}):')
            for k in set(api_keys):
                print(f'  {k[:120]}...')
        
        json_refs = re.findall(r'["\']([^"\']*\.json[^"\']*)["\']', js)
        if json_refs:
            print(f'JSON references ({len(set(json_refs))}):')
            for j in sorted(set(json_refs)):
                print(f'  {j}')
        
        fetch_patterns = re.findall(r'.{0,60}fetch.{0,120}', js)
        if fetch_patterns:
            print(f'Fetch patterns ({len(fetch_patterns)}):')
            for p in fetch_patterns[:10]:
                print(f'  {p[:300]}')
        
        wr_count = len(re.findall(r'["\']wr["\']', js))
        pr_count = len(re.findall(r'["\']pr["\']', js))
        kd_count = len(re.findall(r'["\']kd["\']', js))
        agent_count = len(re.findall(r'["\']agent["\']', js))
        print(f'Data keys - wr:{wr_count} pr:{pr_count} kd:{kd_count} agent:{agent_count}')
        
        print(f'\nFirst 2000 chars:')
        print(js[:2000])
    except Exception as e:
        print(f'ERROR: {e}')
