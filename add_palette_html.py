import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add Palette Dropdown HTML
palette_html = '''
          <!-- Theme Palette Dropdown -->
          <div class="nav-palette-container" style="position: relative;">
            <button id="paletteToggle" class="nav-palette-btn" aria-label="Toggle Color Palette">
              <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M12 22a10 10 0 1 1 10-10c0 4.41-1.34 8-6 8a4 4 0 0 1-4-4c0-2 1.34-4 3-4a1 1 0 0 0-1-1H9a7 7 0 1 0 0 14z"></path>
              </svg>
              <span class="palette-text">COLOR</span>
            </button>
            <div id="paletteMenu" class="palette-menu">
              <button class="palette-option active" data-theme="default">
                <span class="color-swatch" style="background: #2a1e17;"></span> Default
              </button>
              <button class="palette-option" data-theme="ocean">
                <span class="color-swatch" style="background: #1e3a5f;"></span> Ocean
              </button>
              <button class="palette-option" data-theme="forest">
                <span class="color-swatch" style="background: #234d20;"></span> Forest
              </button>
              <button class="palette-option" data-theme="cyber">
                <span class="color-swatch" style="background: #0f0f15;"></span> Cyber
              </button>
            </div>
          </div>
'''

# Insert before Theme Toggle Button
html = html.replace('          <!-- Theme Toggle Button -->', palette_html + '\n          <!-- Theme Toggle Button -->')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
