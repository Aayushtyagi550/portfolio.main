import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

gif_html = '''
      <!-- Floating Top-Left GIF -->
      <img src="assets/gif.gif" alt="Animated element" class="landing-floating-gif">
'''

# Insert right after the landing section opening tag
html = html.replace('<section id="landing" class="landing-section">', '<section id="landing" class="landing-section">' + gif_html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

if '.landing-floating-gif' not in css:
    css += '''
/* ==========================================================================
   FLOATING GIF
   ========================================================================== */
.landing-floating-gif {
  position: absolute;
  top: 40px;
  left: 40px;
  width: clamp(100px, 15vw, 180px);
  z-index: 5;
  pointer-events: none; /* So it doesn't block clicks */
  opacity: 0.9;
  border-radius: 12px;
}
'''

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("GIF added")
