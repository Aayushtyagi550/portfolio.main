import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('Vardhman Academy', 'Guru Govind Singh Public School')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

js = js.replace('Vardhman Academy', 'Guru Govind Singh Public School')

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("School updated")
