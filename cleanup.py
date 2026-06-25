import re

# Clean index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()
html = re.sub(r'vasudev<span class="logo-dot">\.</span>katariya', 'aayush<span class="logo-dot">.</span>tyagi', html)
html = re.sub(r'Aayush_Katariya_Resume_\.pdf', 'Aayush_Tyagi_Resume.pdf', html)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Clean script.js
with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()
js = re.sub(r'github\.com/vasudev7891/SymptoGenie---AI-Health-App\.git', 'github.com/Aayushtyagi550/SymptoGenie---AI-Health-App.git', js)
js = re.sub(r'github\.com/vasudev7891/MelodyVerse---Web-Music-Player\.git', 'github.com/Aayushtyagi550/MelodyVerse---Web-Music-Player.git', js)
js = re.sub(r'github\.com/vasudev7891', 'github.com/Aayushtyagi550', js)
js = re.sub(r'leetcode\.com/u/vasudev7891/', 'leetcode.com/u/tyagiaayush0007/', js)
with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

# Clean README.md
with open('README.md', 'r', encoding='utf-8') as f:
    md = f.read()
md = re.sub(r'Vasudev Katariya', 'Aayush Tyagi', md)
md = re.sub(r'Vasudev', 'Aayush', md)
md = re.sub(r'vasudevkatariya', 'aayushtyagi', md)
md = re.sub(r'vasudev7891\.github\.io', 'aayushtyagi550.github.io', md)
md = re.sub(r'vasudev7891', 'Aayushtyagi550', md)
md = re.sub(r'vasudev\.katariya_', 'aayush.tyagi_', md)
md = re.sub(r'Vasudev_Katariya_Resume_', 'Aayush_Tyagi_Resume', md)
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(md)

print('Cleanup successful')
