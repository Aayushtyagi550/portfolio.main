import re

# 1. Revert index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'(\s*<!-- Theme Palette Dropdown -->.*?</div>\s*</div>\s*)<!-- Theme Toggle Button -->', r'\n          <!-- Theme Toggle Button -->', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Revert style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# I appended the palette css at the end of the file. Let's find the header.
palette_index = css.find('/* ==========================================================================\n   PALETTE MENU UI')
if palette_index != -1:
    css = css[:palette_index]

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 3. Revert script.js
with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

js = re.sub(r'\s*/\* ==========================================================================\s*COLOR THEME PALETTE SWITCHER.*?(?=\/\* ==========================================================================\s*TERMINAL VISUAL & INTERACTIVE ENHANCEMENTS)', '\n  ', js, flags=re.DOTALL)

# Revert interactiveSelectors
js = re.sub(
    r"const interactiveSelectors = '.*?';",
    "const interactiveSelectors = 'a, button, input, textarea, select, .proj-screenshot-container, .edu-card, .mv-card, .ach-card, .cert-card-tilt-container, .logo, .social-btn-round, .proj-btn, .counter-num';",
    js
)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Reverted everything successfully")
