import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_certs = '''<div class="certifications-grid">
          <!-- Card 1: Oracle -->
          <div class="cert-card-tilt-container trigger-cert">
            <div class="cert-card-placeholder">
              <div class="terminal-card-header" data-title="oracle_ai.cert"></div>
              <div class="cert-image-box">
                <a href="assets/cert1.jpg" target="_blank" rel="noopener noreferrer"><img src="assets/cert1.jpg" alt="Oracle AI Foundations" class="cert-img"></a>
              </div>
              <div class="cert-info">
                <div class="cert-provider-badge">
                  <span>Oracle</span>
                </div>
                <h3>AI Foundations Associate</h3>
              </div>
            </div>
          </div>

          <!-- Card 2: AWS -->
          <div class="cert-card-tilt-container trigger-cert">
            <div class="cert-card-placeholder">
              <div class="terminal-card-header" data-title="aws_architect.cert"></div>
              <div class="cert-image-box">
                <a href="assets/cert2.jpg" target="_blank" rel="noopener noreferrer"><img src="assets/cert2.jpg" alt="AWS Cloud Architecting" class="cert-img"></a>
              </div>
              <div class="cert-info">
                <div class="cert-provider-badge">
                  <span>AWS Academy</span>
                </div>
                <h3>Cloud Architecting</h3>
              </div>
            </div>
          </div>

          <!-- Card 3: TrendyTech SQL -->
          <div class="cert-card-tilt-container trigger-cert">
            <div class="cert-card-placeholder">
              <div class="terminal-card-header" data-title="sql_superstar.cert"></div>
              <div class="cert-image-box">
                <a href="assets/cert3.jpg" target="_blank" rel="noopener noreferrer"><img src="assets/cert3.jpg" alt="SQL Superstar Course" class="cert-img"></a>
              </div>
              <div class="cert-info">
                <div class="cert-provider-badge">
                  <span>TrendyTech</span>
                </div>
                <h3>SQL Superstar</h3>
              </div>
            </div>
          </div>

          <!-- Card 4: MongoDB -->
          <div class="cert-card-tilt-container trigger-cert">
            <div class="cert-card-placeholder">
              <div class="terminal-card-header" data-title="mongodb.cert"></div>
              <div class="cert-image-box">
                <a href="assets/cert4.jpg" target="_blank" rel="noopener noreferrer"><img src="assets/cert4.jpg" alt="Introduction to MongoDB" class="cert-img"></a>
              </div>
              <div class="cert-info">
                <div class="cert-provider-badge">
                  <span>MongoDB</span>
                </div>
                <h3>Introduction to MongoDB</h3>
              </div>
            </div>
          </div>

          <!-- Card 5: HackerRank -->
          <div class="cert-card-tilt-container trigger-cert">
            <div class="cert-card-placeholder">
              <div class="terminal-card-header" data-title="problem_solving.cert"></div>
              <div class="cert-image-box">
                <a href="assets/cert5.jpg" target="_blank" rel="noopener noreferrer"><img src="assets/cert5.jpg" alt="HackerRank Problem Solving" class="cert-img"></a>
              </div>
              <div class="cert-info">
                <div class="cert-provider-badge">
                  <span>HackerRank</span>
                </div>
                <h3>Problem Solving (Basic)</h3>
              </div>
            </div>
          </div>
        </div>'''

# Replace the existing certifications grid
pattern = r'<div class="certifications-grid">.*?</div>\s*</div>\s*</section>'
replacement = new_certs + '\n      </div>\n    </section>'
html = re.sub(pattern, replacement, html, flags=re.DOTALL)

# Update Counter from 4 to 5
html = re.sub(r'data-value="4">0</div>(\s*)<div class="counter-label">Certifications', r'data-value="5">0</div>\1<div class="counter-label">Certifications', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Certs remapped")
