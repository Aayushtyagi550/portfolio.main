import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the black background style I had put in earlier for the placeholder
html = html.replace('style="background:#000;"', '')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
