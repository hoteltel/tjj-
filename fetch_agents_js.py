import urllib.request
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Accept': '*/*',
    'Referer': 'https://www.vstats.gg/agents'
}

# Fetch the AgentsRoot JS file
js_url = 'https://www.vstats.gg/assets/AgentsRoot-L6VNZkTH.js'
try:
    req = urllib.request.Request(js_url, headers=headers)
    with urllib.request.urlopen(req, timeout=30, context=ctx) as resp:
        content = resp.read().decode('utf-8', errors='ignore')
        print(f"AgentsRoot JS length: {len(content)}")
        
        # Look for Supabase URL
        sb_urls = re.findall(r'(https?://[a-zA-Z0-9_-]+\.supabase\.co[a-zA-Z0-9_/.-]*)', content)
        if sb_urls:
            print(f"Supabase URLs: {set(sb_urls)}")
        
        # Look for API keys (JWT tokens)
        api_keys = re.findall(r'(eyJ[a-zA-Z0-9_-]{50,})', content)
        if api_keys:
            for k in set(api_keys):
                print(f"API Key: {k[:80]}...")
        
        # Look for createClient
        sb_patterns = re.findall(r'(createClient\([^)]+\))', content)
        if sb_patterns:
            for p in sb_patterns:
                print(f"Supabase client: {p[:300]}")
        
        # Look for supabase keyword
        sb_idx = content.lower().find('supabase')
        if sb_idx >= 0:
            start = max(0, sb_idx - 100)
            end = min(len(content), sb_idx + 500)
            print(f"Supabase context: {content[start:end]}")
        
        # Look for .from( calls (Supabase query)
        from_calls = re.findall(r'\.from\(["\']([^"\']+)["\']\)', content)
        if from_calls:
            print(f"Supabase tables: {set(from_calls)}")
        
        # Look for select calls
        select_calls = re.findall(r'\.select\(["\']([^"\']+)["\']\)', content)
        if select_calls:
            print(f"Select fields: {set(select_calls)}")
        
        # Look for any URL patterns
        url_patterns = re.findall(r'["\'](/api/[a-zA-Z0-9_/.-]+)["\']', content)
        if url_patterns:
            print(f"API paths: {set(url_patterns)}")
        
        # Look for environment variable references
        env_patterns = re.findall(r'(VITE_[A-Z_]+|import\.meta\.env\.[A-Z_]+)', content)
        if env_patterns:
            print(f"Env vars: {set(env_patterns)}")
        
        # Look for any hardcoded URLs
        urls = re.findall(r'(https?://[a-zA-Z0-9_./:-]+)', content)
        if urls:
            print(f"All URLs: {set(urls)}")
        
        # Print first 2000 chars to understand structure
        print(f"\nFirst 2000 chars:\n{content[:2000]}")
        
except Exception as e:
    print(f"Error: {e}")
