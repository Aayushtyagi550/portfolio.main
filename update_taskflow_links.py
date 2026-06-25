import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the address bar
html = html.replace('<div class="browser-address-bar">taskflow-app.onrender.com/</div>', '<div class="browser-address-bar">my-task-manager-taupe.vercel.app/</div>')

# 2. Add the proj-links inside the tech-tags-container's parent (proj-info-left)
proj_links = '''                <div class="proj-links">
                  <a href="https://github.com/Aayushtyagi550/my-task-manager" target="_blank" rel="noopener noreferrer" class="proj-btn">
                    <span>GitHub</span>
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path>
                    </svg>
                  </a>
                  <a href="https://my-task-manager-taupe.vercel.app/" target="_blank" rel="noopener noreferrer" class="proj-btn">
                    <span>Live Demo</span>
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>
                      <polyline points="15 3 21 3 21 9"></polyline>
                      <line x1="10" y1="14" x2="21" y2="3"></line>
                    </svg>
                  </a>
                </div>
'''

# Find the end of tech-tags-container in TaskFlow
# To ensure we only target TaskFlow, we use regex carefully.
taskflow_pattern = r'(<span class="proj-name">taskflow</span>.*?<div class="tech-tags-container">.*?</div>)(\s*</div>\s*</div>\s*</article>)'
html = re.sub(taskflow_pattern, r'\1\n' + proj_links + r'\2', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("TaskFlow updated")
