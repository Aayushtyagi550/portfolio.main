import re

with open('README.md', 'r', encoding='utf-8') as f:
    md = f.read()

md = re.sub(r'Aayush_Katariya_Resume_\.pdf', 'Aayush_Tyagi_Resume.pdf', md)

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(md)

print('Done')
