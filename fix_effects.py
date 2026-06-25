import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Add theme-transition when changing palette colors so it's smooth!
new_apply = '''    const applyColorTheme = (themeName) => {
      // Add smooth transition class just like the Dark Mode toggle does!
      document.body.classList.add('theme-transition');
      
      // Remove any existing theme classes
      document.body.classList.remove('theme-ocean', 'theme-forest', 'theme-cyber');
      
      // Add the new theme class if it's not the default brown/cream
      if (themeName !== 'default') {
        document.body.classList.add(	heme-);
      }
      
      // Update Active State on buttons
      paletteOptions.forEach(opt => {
        if (opt.getAttribute('data-theme') === themeName) {
          opt.classList.add('active');
        } else {
          opt.classList.remove('active');
        }
      });
      
      localStorage.setItem('colorTheme', themeName);
      
      // Remove smooth transition class after animation completes
      setTimeout(() => {
        document.body.classList.remove('theme-transition');
      }, 500);
    };'''

js = re.sub(r'const applyColorTheme = \(themeName\) => \{.*?(?=\s+// Initialize saved theme)', new_apply + '\n', js, flags=re.DOTALL)

# 2. Add palette items to interactiveSelectors so the custom magnetic cursor doesn't get lost
js = js.replace(
    "const interactiveSelectors = 'a, button, input, textarea, select, .proj-screenshot-container, .edu-card, .mv-card, .ach-card, .cert-card-tilt-container, .logo, .social-btn-round, .proj-btn, .counter-num';",
    "const interactiveSelectors = 'a, button, input, textarea, select, .proj-screenshot-container, .edu-card, .mv-card, .ach-card, .cert-card-tilt-container, .logo, .social-btn-round, .proj-btn, .counter-num, .palette-menu, .nav-palette-container, .palette-option';"
)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Effects fixed")
