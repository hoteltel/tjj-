import json
with open('agents.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
for agent in data['data']:
    print(f"{agent['displayName']}: {agent['uuid']}")
