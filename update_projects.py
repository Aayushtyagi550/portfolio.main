import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

taskflow_project = '''
          <!-- Project 3: TaskFlow -->
          <article class="project-split-card trigger-project">
            <div class="project-visual-column">
              <div class="browser-mockup">
                <div class="browser-top-bar">
                  <div class="browser-dots">
                    <span class="dot-red"></span>
                    <span class="dot-yellow"></span>
                    <span class="dot-green"></span>
                  </div>
                  <div class="browser-address-bar">taskflow-app.onrender.com/</div>
                </div>
                <div class="browser-content">
                  <div class="proj-screenshot-container" data-current="0" data-images="assets/profile.png">
                    <img src="assets/profile.png" alt="TaskFlow Screenshot" class="proj-screenshot" style="background:#000;">
                  </div>
                </div>
              </div>
            </div>
            
            <div class="project-info-column">
              <div class="proj-info-left">
                <div class="proj-meta">
                  <span class="proj-type">Task Manager App</span>
                </div>
                <h3 class="proj-title"><span class="proj-cli-prompt">aayush@portfolio:~$</span> <span class="proj-cli-exec">./03_</span><span class="proj-name">taskflow</span><span class="title-cursor">?</span></h3>
                <p class="proj-desc-short">Task manager with CRUD operations and localStorage.</p>
                
                <div class="tech-tags-container">
                  <span class="tech-tag">React.js</span>
                  <span class="tech-tag">JavaScript</span>
                  <span class="tech-tag">CSS</span>
                  <span class="tech-tag">localStorage</span>
                </div>
              </div>
            </div>
          </article>
'''

# Find the end of project 2
pattern = r'(</article>\s*)\s*</div>\s*</div>\s*</section>\s*<!-- EXPERIENCE SECTION -->'
# Just insert before the end of the projects container
def replacer(match):
    return match.group(1) + taskflow_project + '\n        </div>\n      </div>\n    </section>\n\n    <!-- EXPERIENCE SECTION -->'

content = re.sub(pattern, replacer, content)

# Update Counters
content = re.sub(r'data-value="4">0</div>\s*<div class="counter-label">Certifications', 'data-value="4">0</div>\n            <div class="counter-label">Certifications', content)
content = re.sub(r'data-value="2">0</div>\s*<div class="counter-label">Projects', 'data-value="3">0</div>\n            <div class="counter-label">Projects', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Projects updated")
