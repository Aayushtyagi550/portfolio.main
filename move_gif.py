import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace top: 40px with top: 120px for the GIF
css = css.replace('top: 40px;\n  left: 40px;', 'top: 120px;\n  left: 40px;')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("GIF moved down")
