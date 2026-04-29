import urllib.request, json, gzip, ssl, sys, zlib, brotli
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

base_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'Accept': '*/*',
    'Referer': 'https://www.vstats.gg/agents',
}

url = 'https://www.vstats.gg/statistics/agents/ALL/agents.json.gz'
output = []
try:
    req = urllib.request.Request(url, headers=base_headers)
    with urllib.request.urlopen(req, timeout=15, context=ctx) as resp:
        raw = resp.read()
        output.append(f'Status: {resp.status}')
        output.append(f'Content-Type: {resp.headers.get("Content-Type")}')
        output.append(f'Content-Encoding: {resp.headers.get("Content-Encoding")}')
        output.append(f'Actual length: {len(raw)}')
        output.append(f'First 20 bytes hex: {raw[:20].hex()}')
        
        decompressed = None
        
        try:
            decompressed = gzip.decompress(raw)
            output.append('Gzip decompress OK!')
        except:
            pass
        
        if decompressed is None:
            try:
                decompressed = brotli.decompress(raw)
                output.append('Brotli decompress OK!')
            except:
                pass
        
        if decompressed is None:
            try:
                decompressed = zlib.decompress(raw)
                output.append('Zlib decompress OK!')
            except:
                pass
        
        if decompressed is None:
            try:
                decompressed = zlib.decompress(raw, -zlib.MAX_WBITS)
                output.append('Raw deflate decompress OK!')
            except:
                pass
        
        if decompressed is None:
            try:
                decompressed = zlib.decompress(raw, 16 + zlib.MAX_WBITS)
                output.append('Gzip via zlib decompress OK!')
            except:
                pass
        
        if decompressed is not None:
            output.append(f'Decompressed length: {len(decompressed)}')
            try:
                text = decompressed.decode('utf-8')
                data = json.loads(text)
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
                else:
                    output.append(f'Type: {type(data).__name__}')
                    output.append(f'First 500: {text[:500]}')
            except Exception as e:
                output.append(f'JSON parse error: {e}')
                output.append(f'First 500: {decompressed[:500].decode("utf-8", errors="replace")}')
        else:
            output.append('All decompress methods failed')
            output.append(f'Raw first 200: {raw[:200]}')

except Exception as e:
    output.append(f'ERROR: {e}')

with open('d:/TRAE/valorant-stats-dashboard/vstats_data2.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(output))
print('Done!')
