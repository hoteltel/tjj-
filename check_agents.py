import re

with open('agent-data.js', 'r', encoding='utf-8') as f:
    content = f.read()

agents = re.findall(r'"([A-Za-z/]+)":\s*\{', content)
print(f'特工数量: {len(agents)}')
print('特工列表:')
for agent in agents:
    print(f'  - {agent}')
