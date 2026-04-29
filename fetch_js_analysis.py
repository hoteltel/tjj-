import urllib.request
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': '*/*',
    'Referer': 'https://www.vstats.gg/agents'
}

# Fetch the main JS file
js_url = 'https://www.vstats.gg/assets/index-VdEKILD-.js'
try:
    req = urllib.request.Request(js_url, headers=headers)
    with urllib.request.urlopen(req, timeout=30, context=ctx) as resp:
        content = resp.read().decode('utf-8', errors='ignore')
        print(f"JS file length: {len(content)}")
        
        # Look for Supabase URL
        sb_urls = re.findall(r'(https?://[a-zA-Z0-9_-]+\.supabase\.co[a-zA-Z0-9_/.-]*)', content)
        if sb_urls:
            print(f"Supabase URLs: {set(sb_urls)}")
        
        # Look for API keys
        api_keys = re.findall(r'(eyJ[a-zA-Z0-9_-]{50,})', content)
        if api_keys:
            for k in set(api_keys):
                print(f"API Key: {k[:50]}...")
        
        # Look for fetch/axios calls
        fetch_calls = re.findall(r'(fetch\([^)]+\))', content)
        if fetch_calls:
            print(f"Fetch calls: {len(fetch_calls)}")
            for f in fetch_calls[:10]:
                print(f"  {f[:100]}")
        
        # Look for table names
        table_names = re.findall(r'(?:from|table)["\s:=]+["\']([a-zA-Z_]+)["\']', content, re.IGNORECASE)
        if table_names:
            print(f"Table names: {set(table_names)}")
        
        # Look for any URL patterns
        url_patterns = re.findall(r'["\'](/api/[a-zA-Z0-9_/.-]+)["\']', content)
        if url_patterns:
            print(f"API paths: {set(url_patterns)}")
        
        # Look for chunk references
        chunks = re.findall(r'["\']\./([a-zA-Z0-9_-]+-[a-zA-Z0-9_-]+\.js)["\']', content)
        if chunks:
            print(f"Chunk files: {chunks}")
        
        # Look for supabase client creation
        sb_patterns = re.findall(r'(createClient\([^)]+\))', content)
        if sb_patterns:
            for p in sb_patterns:
                print(f"Supabase client: {p[:200]}")
        
        # Look for any data-related patterns
        data_patterns = re.findall(r'(TABLE_AGENTS|agents_table|v_stats|agent_stats)', content, re.IGNORECASE)
        if data_patterns:
            print(f"Data patterns: {set(data_patterns)}")
            
        # Search around "supabase" keyword
        sb_idx = content.lower().find('supabase')
        if sb_idx >= 0:
            start = max(0, sb_idx - 100)
            end = min(len(content), sb_idx + 300)
            print(f"Supabase context: {content[start:end]}")
        
        # Search for "apiKey" or "anon" key
        key_idx = content.lower().find('apikey')
        if key_idx >= 0:
            start = max(0, key_idx - 50)
            end = min(len(content), key_idx + 200)
            print(f"API key context: {content[start:end]}")
            
except Exception as e:
    print(f"Error: {e}")
