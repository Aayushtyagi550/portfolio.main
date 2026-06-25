import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add a third button to landing-ctas
new_button = '''          <a href="assets/Aayush_Tyagi_Resume.pdf" target="_blank" rel="noopener noreferrer" class="btn btn-secondary" style="border-color: var(--accent-gold); color: var(--accent-gold);" download>
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-right: 6px; vertical-align: text-bottom;">
              <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"></path>
              <polyline points="7 10 12 15 17 10"></polyline>
              <line x1="12" y1="15" x2="12" y2="3"></line>
            </svg>
            Download Resume
          </a>'''

html = html.replace(
    '<div class="landing-ctas animate-ctas">\n          <a href="#projects" class="btn btn-primary">View Selected Work <span class="btn-arrow">?</span></a>\n          <a href="#about" class="btn btn-secondary">Explore Profile <span class="btn-arrow">?</span></a>\n        </div>',
    '<div class="landing-ctas animate-ctas">\n          <a href="#projects" class="btn btn-primary">View Selected Work <span class="btn-arrow">?</span></a>\n          <a href="#about" class="btn btn-secondary">Explore Profile <span class="btn-arrow">?</span></a>\n' + new_button + '\n        </div>'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Added resume button")
