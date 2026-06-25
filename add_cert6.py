import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add Cert 6 to Certifications Grid
cert6_html = '''          <!-- Card 6: UiPath -->
          <div class="cert-card-tilt-container trigger-cert">
            <div class="cert-card-placeholder">
              <div class="terminal-card-header" data-title="uipath_automation.cert"></div>
              <div class="cert-image-box">
                <a href="assets/cert6.png" target="_blank" rel="noopener noreferrer"><img src="assets/cert6.png" alt="UiPath Automation Developer" class="cert-img"></a>
              </div>
              <div class="cert-info">
                <div class="cert-provider-badge">
                  <span>UiPath</span>
                </div>
                <h3>Automation Developer Associate</h3>
              </div>
            </div>
          </div>
'''
html = html.replace('<!-- Card 5: HackerRank -->', cert6_html + '\n          <!-- Card 5: HackerRank -->')

# Update Cert counter from 5 to 6
html = re.sub(r'data-value="5">0</div>(\s*)<div class="counter-label">Certifications', r'data-value="6">0</div>\1<div class="counter-label">Certifications', html)


# 2. Add Internship Certificate to Experience section
internship_btn = '''
              <div class="proj-links" style="margin-top: 20px;">
                  <a href="assets/internship.png" target="_blank" rel="noopener noreferrer" class="proj-btn">
                    <span>View Certificate</span>
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path>
                      <polyline points="15 3 21 3 21 9"></polyline>
                      <line x1="10" y1="14" x2="21" y2="3"></line>
                    </svg>
                  </a>
              </div>
'''

# Find the end of the <ul> in the experience section and insert the button after it
html = html.replace('</ul>\n            </div>\n          </div>', '</ul>' + internship_btn + '            </div>\n          </div>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Additions complete")
