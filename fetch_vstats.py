import sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import urllib.request, ssl, re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

req = urllib.request.Request('https://www.vstats.gg/assets/index-VdEKILD-.js', headers={'User-Agent': 'Mozilla/5.0'})
resp = urllib.request.urlopen(req, context=ctx, timeout=30)
js = resp.read().decode('utf-8', errors='replace')

create_client = js.find('createClient')
if create_client > -1:
    print("Found createClient at:", create_client)
    print(js[max(0,create_client-100):create_client+300])
    print("---")

supa = js.find('supa')
if supa > -1:
    print("Found supa at:", supa)
    print(js[max(0,supa-100):supa+300])
    print("---")

anon = js.find('anon')
if anon > -1:
    print("Found anon at:", anon)
    print(js[max(0,anon-100):anon+300])
    print("---")

project = js.find('.supabase')
if project > -1:
    print("Found .supabase at:", project)
    print(js[max(0,project-200):project+200])
    print("---")

create_client2 = js.find('create_client')
if create_client2 > -1:
    print("Found create_client at:", create_client2)
    print(js[max(0,create_client2-100):create_client2+300])
    print("---")

init = js.find('initSupabase')
if init > -1:
    print("Found initSupabase at:", init)
    print(js[max(0,init-100):init+300])

url_pattern = re.findall(r'["\']https?://[a-z0-9-]+\.supabase\.co[^"\']*["\']', js)
print("\nDirect supabase.co URLs:")
for u in set(url_pattern):
    print(u)

key_pattern = re.findall(r'["\']eyJ[A-Za-z0-9_-]{30,}["\']', js)
print("\nJWT-like keys:")
for k in set(key_pattern):
    print(k[:80] + "..." if len(k) > 80 else k)

# Search for any base64-like strings that could be API keys
b64_pattern = re.findall(r'["\']([A-Za-z0-9+/=_-]{40,})["\']', js)
print(f"\nBase64-like strings (found {len(b64_pattern)}):")
for b in set(b64_pattern)[:10]:
    print(b[:80] + "..." if len(b) > 80 else b)
