import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace lowercase taskflow.png with TaskFlow.png
html = html.replace('assets/taskflow.png', 'assets/TaskFlow.png')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
