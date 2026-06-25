import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Add Dropdown UI styles
dropdown_css = '''
/* ==========================================================================
   PALETTE MENU UI
   ========================================================================== */
.nav-palette-btn {
  display: flex;
  align-items: center;
  gap: 6px;
  background: none;
  border: 1px solid var(--border-cream);
  color: var(--brown-dark);
  font-family: var(--font-mono);
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.1em;
  padding: 6px 12px;
  border-radius: 4px;
  cursor: pointer;
  transition: var(--transition-smooth);
}

.nav-palette-btn:hover {
  background-color: var(--brown-dark);
  color: var(--bg-cream);
}

.palette-menu {
  position: absolute;
  top: 120%;
  right: 0;
  background-color: var(--card-light);
  border: 1px solid var(--border-cream);
  border-radius: 8px;
  padding: 8px;
  display: flex;
  flex-direction: column;
  gap: 4px;
  min-width: 130px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.1);
  opacity: 0;
  visibility: hidden;
  transform: translateY(-10px);
  transition: var(--transition-smooth);
  z-index: 100;
}

.palette-menu.show {
  opacity: 1;
  visibility: visible;
  transform: translateY(0);
}

.palette-option {
  display: flex;
  align-items: center;
  gap: 10px;
  background: none;
  border: none;
  padding: 8px 12px;
  font-family: var(--font-mono);
  font-size: 12px;
  color: var(--brown-dark);
  cursor: pointer;
  border-radius: 4px;
  transition: var(--transition-smooth);
  text-align: left;
}

.palette-option:hover, .palette-option.active {
  background-color: var(--bg-soft);
  font-weight: 700;
}

.color-swatch {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  border: 1px solid var(--border-cream);
  display: inline-block;
}

/* ==========================================================================
   COLOR THEMES (LIGHT & DARK MODES)
   ========================================================================== */

/* --- THEME: OCEAN BLUE --- */
body.theme-ocean {
  --bg-cream: #f0f4f8;
  --bg-soft: #e1e8f0;
  --card-light: #ffffff;
  --card-dark: #102a43;
  --brown-dark: #102a43;
  --brown-medium: #243b53;
  --brown-light: #486581;
  --brown-muted: #9fb3c8;
  --border-cream: #d9e2ec;
  --accent-gold: #008eb0;
  --accent-gold-light: #48b5c2;
  --accent-glow: rgba(0, 142, 176, 0.15);
}
body.dark-mode.theme-ocean {
  --bg-cream: #09131a;
  --bg-soft: #11202b;
  --card-light: #162a3a;
  --border-cream: #243b53;
  --brown-dark: #f0f4f8;
  --brown-medium: #d9e2ec;
  --brown-light: #829ab1;
  --accent-gold-light: #4bdcf0;
  --accent-glow: rgba(75, 220, 240, 0.12);
}

/* --- THEME: FOREST GREEN --- */
body.theme-forest {
  --bg-cream: #f4f7f4;
  --bg-soft: #e7ece7;
  --card-light: #ffffff;
  --card-dark: #1b3320;
  --brown-dark: #1b3320;
  --brown-medium: #2d4c34;
  --brown-light: #52795a;
  --brown-muted: #a3b8a8;
  --border-cream: #d5e0d7;
  --accent-gold: #388e3c;
  --accent-gold-light: #66bb6a;
  --accent-glow: rgba(56, 142, 60, 0.15);
}
body.dark-mode.theme-forest {
  --bg-cream: #0c140e;
  --bg-soft: #121e15;
  --card-light: #1a2a1d;
  --border-cream: #2d4c34;
  --brown-dark: #f4f7f4;
  --brown-medium: #d5e0d7;
  --brown-light: #8ba892;
  --accent-gold-light: #81c784;
  --accent-glow: rgba(129, 199, 132, 0.12);
}

/* --- THEME: CYBER PURPLE --- */
body.theme-cyber {
  --bg-cream: #fbf9fb;
  --bg-soft: #f2edf4;
  --card-light: #ffffff;
  --card-dark: #2a113a;
  --brown-dark: #2a113a;
  --brown-medium: #472061;
  --brown-light: #7b4ea3;
  --brown-muted: #c9b1d9;
  --border-cream: #e6d8ed;
  --accent-gold: #9d4edd;
  --accent-gold-light: #c77dff;
  --accent-glow: rgba(157, 78, 221, 0.15);
}
body.dark-mode.theme-cyber {
  --bg-cream: #09050d;
  --bg-soft: #140b1e;
  --card-light: #1e112d;
  --border-cream: #3a2253;
  --brown-dark: #fbf9fb;
  --brown-medium: #e6d8ed;
  --brown-light: #a88cb8;
  --accent-gold-light: #e0aaff;
  --accent-glow: rgba(224, 170, 255, 0.12);
}
'''

if '.theme-ocean' not in css:
    css += dropdown_css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("CSS added")
