import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = re.sub(r'https://github\.com/AayushTyagi', 'https://github.com/Aayushtyagi550', content)
content = re.sub(r'https://leetcode\.com/u/[^/]+/', 'https://leetcode.com/u/tyagiaayush0007/', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

with open('script.js', 'r', encoding='utf-8') as f:
    script = f.read()
script = re.sub(r'https://github\.com/AayushTyagi', 'https://github.com/Aayushtyagi550', script)
script = re.sub(r'https://leetcode\.com/u/[^/]+/', 'https://leetcode.com/u/tyagiaayush0007/', script)
with open('script.js', 'w', encoding='utf-8') as f:
    f.write(script)
