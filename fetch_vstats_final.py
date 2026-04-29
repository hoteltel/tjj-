import urllib.request, json, gzip, ssl, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

base_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.vstats.gg/agents',
    'Origin': 'https://www.vstats.gg',
}

url = 'https://www.vstats.gg/statistics/agents/ALL/agents.json.gz'
output = []
try:
    req = urllib.request.Request(url, headers=base_headers)
    with urllib.request.urlopen(req, timeout=15, context=ctx) as resp:
        raw = resp.read()
        output.append(f'Status: {resp.status}')
        output.append(f'Content-Type: {resp.headers.get("Content-Type")}')
        output.append(f'Actual length: {len(raw)}')
        
        try:
            decompressed = gzip.decompress(raw)
            data = json.loads(decompressed.decode('utf-8'))
            output.append(f'Decompressed OK! Length: {len(decompressed)}')
            if isinstance(data, list):
                output.append(f'Data entries: {len(data)}')
                for a in sorted(data, key=lambda x: x.get('wr', 0), reverse=True):
                    name = a.get('a', a.get('agent', '?'))
                    wr = a.get('wr', 0) * 100
                    pr = a.get('pr', 0)
                    kd = a.get('kd', 0)
                    matches = a.get('m', a.get('matches', 0))
                    nmwr = a.get('nmwr', a.get('non_mirror_wr', 0)) * 100
                    output.append(f'{name}|{wr:.2f}|{pr:.2f}|{kd:.2f}|{matches}|{nmwr:.2f}')
        except Exception as e:
            output.append(f'Decompress error: {e}')
            try:
                text = raw.decode('utf-8', errors='replace')
                output.append(f'As text (first 300): {text[:300]}')
            except:
                pass
except Exception as e:
    output.append(f'ERROR: {e}')

with open('d:/TRAE/valorant-stats-dashboard/vstats_data.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(output))
print('Done! Output written to vstats_data.txt')
