import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Remove the media query I added
css = re.sub(r'@media \(min-width: 900px\) \{\s*\.certifications-grid \{\s*grid-template-columns: repeat\(2, 1fr\);\s*\}\s*\}', '', css)

# Fix the 'a' tag rendering
if '.cert-image-box a {' not in css:
    css += '''
.cert-image-box a {
  display: block;
  width: 100%;
  height: 100%;
}
'''

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print('CSS fixed')
