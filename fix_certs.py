import re

# Update HTML
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove cert-meta
html = re.sub(r'<p class="cert-meta">.*?</p>', '', html)

# 2. Wrap cert-img with 'a' tag to open in new tab
# We find: <img src="(assets/certX.jpg)" alt=".*?" class="cert-img">
def replacer(match):
    src = match.group(1)
    img_tag = match.group(0)
    return f'<a href="{src}" target="_blank" rel="noopener noreferrer">{img_tag}</a>'

html = re.sub(r'<img src="(assets/[^"]+)" alt="[^"]+" class="cert-img">', replacer, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Update CSS
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Make the grid 2x2 on desktop
css_addition = '''
@media (min-width: 900px) {
  .certifications-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
'''
if '@media (min-width: 900px) {\n  .certifications-grid' not in css:
    css += css_addition

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Certs fixed")
