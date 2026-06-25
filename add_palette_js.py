import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

palette_js = '''
  /* ==========================================================================
     COLOR THEME PALETTE SWITCHER
     ========================================================================== */
  const paletteToggle = document.getElementById('paletteToggle');
  const paletteMenu = document.getElementById('paletteMenu');
  const paletteOptions = document.querySelectorAll('.palette-option');
  
  if (paletteToggle && paletteMenu) {
    // Toggle menu
    paletteToggle.addEventListener('click', (e) => {
      e.stopPropagation();
      paletteMenu.classList.toggle('show');
    });
    
    // Close menu when clicking outside
    document.addEventListener('click', (e) => {
      if (!paletteMenu.contains(e.target) && !paletteToggle.contains(e.target)) {
        paletteMenu.classList.remove('show');
      }
    });

    // Handle theme switching
    const currentTheme = localStorage.getItem('colorTheme') || 'default';
    
    const applyColorTheme = (themeName) => {
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
    };

    // Initialize saved theme
    applyColorTheme(currentTheme);

    // Add click listeners to buttons
    paletteOptions.forEach(btn => {
      btn.addEventListener('click', () => {
        const theme = btn.getAttribute('data-theme');
        applyColorTheme(theme);
        paletteMenu.classList.remove('show');
      });
    });
  }
'''

# Find a good place to inject this logic. Inside the DOMContentLoaded event listener.
# We will insert it just after the Dark Mode toggle logic.
insert_marker = "/* ==========================================================================\n     TERMINAL VISUAL & INTERACTIVE ENHANCEMENTS"
js = js.replace(insert_marker, palette_js + '\n  ' + insert_marker)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("JS added")
