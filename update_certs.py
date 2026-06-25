import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_certs = '''<div class="certifications-grid">
          <!-- Card 1: HackerRank Problem Solving -->
          <div class="cert-card-tilt-container trigger-cert">
            <div class="cert-card-placeholder">
              <div class="terminal-card-header" data-title="problem_solving.cert"></div>
              <div class="cert-image-box">
                <img src="assets/Certificate_HackerRank.jpg" alt="HackerRank Problem Solving" class="cert-img">
              </div>
              <div class="cert-info">
                <div class="cert-provider-badge">
                  <span>HackerRank</span>
                </div>
                <h3>Problem Solving (Basic)</h3>
                <p class="cert-meta">March 18, 2026</p>
              </div>
            </div>
          </div>

          <!-- Card 2: Oracle Cloud AI Foundations Associate -->
          <div class="cert-card-tilt-container trigger-cert">
            <div class="cert-card-placeholder">
              <div class="terminal-card-header" data-title="oracle_ai.cert"></div>
              <div class="cert-image-box">
                <img src="assets/Certificate_Oracle.jpg" alt="Oracle AI Foundations" class="cert-img">
              </div>
              <div class="cert-info">
                <div class="cert-provider-badge">
                  <span>Oracle</span>
                </div>
                <h3>AI Foundations Associate</h3>
                <p class="cert-meta">August 19, 2025</p>
              </div>
            </div>
          </div>

          <!-- Card 3: MongoDB -->
          <div class="cert-card-tilt-container trigger-cert">
            <div class="cert-card-placeholder">
              <div class="terminal-card-header" data-title="mongodb.cert"></div>
              <div class="cert-image-box">
                <img src="assets/Certificate_MongoDB.jpg" alt="Introduction to MongoDB" class="cert-img">
              </div>
              <div class="cert-info">
                <div class="cert-provider-badge">
                  <span>MongoDB</span>
                </div>
                <h3>Introduction to MongoDB</h3>
                <p class="cert-meta">May 8, 2025</p>
              </div>
            </div>
          </div>

          <!-- Card 4: TrendyTech SQL -->
          <div class="cert-card-tilt-container trigger-cert">
            <div class="cert-card-placeholder">
              <div class="terminal-card-header" data-title="sql_superstar.cert"></div>
              <div class="cert-image-box">
                <img src="assets/Certificate_SQL.jpg" alt="SQL Superstar Course" class="cert-img">
              </div>
              <div class="cert-info">
                <div class="cert-provider-badge">
                  <span>TrendyTech</span>
                </div>
                <h3>SQL Superstar</h3>
                <p class="cert-meta">March 12, 2026</p>
              </div>
            </div>
          </div>
        </div>'''

# Replace the existing certifications grid
# Find from <div class="certifications-grid"> to the next </section> and then reconstruct.
start_idx = content.find('<div class="certifications-grid">')
end_idx = content.find('</section>', start_idx)
if start_idx != -1 and end_idx != -1:
    # Need to keep the </div> that closes the container
    # The structure is:
    # <div class="container">
    #   ...
    #   <div class="certifications-grid">...</div>
    # </div>
    # </section>
    
    # Let's use regex
    pattern = r'<div class="certifications-grid">.*?</div>\s*</div>\s*</section>'
    replacement = new_certs + '\n      </div>\n    </section>'
    content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Certs updated")
