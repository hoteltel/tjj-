import urllib.request
import gzip
import ssl
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': '*/*',
}

def fetch_url(url):
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=30, context=ctx) as resp:
            raw = resp.read()
            try:
                return gzip.decompress(raw).decode('utf-8', errors='replace')
            except:
                try:
                    return raw.decode('utf-8', errors='replace')
                except:
                    return None
    except Exception as e:
        return f"Error: {e}"

js = fetch_url('https://www.vstats.gg/assets/index-VdEKILD-.js')
if js and not js.startswith('Error'):
    with open('d:/TRAE/valorant-stats-dashboard/vstats_index_js.txt', 'w', encoding='utf-8') as f:
        f.write(js)
    print(f"JS saved, length: {len(js)}")
    
    import re
    
    all_strings = re.findall(r'"([^"]{5,100})"', js)
    interesting = [s for s in all_strings if any(kw in s.lower() for kw in ['agent', 'stat', 'api', 'fetch', 'supabase', 'json', 'cdn', 'data', 'table', 'map', 'rank', 'win', 'pick'])]
    print(f"\nInteresting strings ({len(interesting)}):")
    for s in sorted(set(interesting))[:50]:
        print(f"  {s}")
    
    url_patterns = re.findall(r'["\']((https?://|/)[^"\']{5,})["\']', js)
    print(f"\nURL patterns ({len(url_patterns)}):")
    for url in sorted(set([u[0] for u in url_patterns]))[:50]:
        print(f"  {url}")
else:
    print(f"Failed: {js}")
