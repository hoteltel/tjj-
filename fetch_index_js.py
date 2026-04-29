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

# Fetch the index JS file that contains data fetching logic
js_url = 'https://www.vstats.gg/assets/index-BOShnSr_.js'
try:
    req = urllib.request.Request(js_url, headers=headers)
    with urllib.request.urlopen(req, timeout=30, context=ctx) as resp:
        content = resp.read().decode('utf-8', errors='ignore')
        print(f"Index JS length: {len(content)}")
        
        # Look for Supabase URL
        sb_urls = re.findall(r'(https?://[a-zA-Z0-9_-]+\.supabase\.co[a-zA-Z0-9_/.-]*)', content)
        if sb_urls:
            print(f"Supabase URLs: {set(sb_urls)}")
        
        # Look for API keys (JWT tokens)
        api_keys = re.findall(r'(eyJ[a-zA-Z0-9_-]{50,})', content)
        if api_keys:
            for k in set(api_keys):
                print(f"API Key: {k[:100]}...")
        
        # Look for createClient
        sb_patterns = re.findall(r'(createClient\([^)]{0,500}\))', content)
        if sb_patterns:
            for p in sb_patterns:
                print(f"Supabase client: {p[:500]}")
        
        # Look for .from( calls (Supabase query)
        from_calls = re.findall(r'\.from\(["\']([^"\']+)["\']\)', content)
        if from_calls:
            print(f"Supabase tables: {set(from_calls)}")
        
        # Look for any hardcoded URLs
        urls = re.findall(r'(https?://[a-zA-Z0-9_./:-]+)', content)
        if urls:
            print(f"All URLs: {set(urls)}")
        
        # Look for supabase keyword
        sb_idx = content.lower().find('supabase')
        if sb_idx >= 0:
            start = max(0, sb_idx - 200)
            end = min(len(content), sb_idx + 500)
            print(f"Supabase context: {content[start:end]}")
        
        # Look for environment variable references
        env_patterns = re.findall(r'(VITE_[A-Z_]+|import\.meta\.env\.[A-Z_]+)', content)
        if env_patterns:
            print(f"Env vars: {set(env_patterns)}")
        
        # Look for TABLE_AGENTS
        ta_idx = content.find('TABLE_AGENTS')
        if ta_idx >= 0:
            start = max(0, ta_idx - 200)
            end = min(len(content), ta_idx + 500)
            print(f"TABLE_AGENTS context: {content[start:end]}")
        
        # Look for table_agents
        ta_idx2 = content.find('table_agents')
        if ta_idx2 >= 0:
            start = max(0, ta_idx2 - 200)
            end = min(len(content), ta_idx2 + 500)
            print(f"table_agents context: {content[start:end]}")
        
        # Print first 3000 chars
        print(f"\nFirst 3000 chars:\n{content[:3000]}")
        
except Exception as e:
    print(f"Error: {e}")
