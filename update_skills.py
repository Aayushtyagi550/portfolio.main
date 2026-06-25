import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace C & C++ (Basics) with Python
content = re.sub(r'<span class="badge-name">C &amp; C\+\+ \(Basics\)</span>', '<span class="badge-name">Python</span>', content)

# Profile pic replace
content = re.sub(r'assets/profile\.png', 'assets/profile_aayush.jpg', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done')
