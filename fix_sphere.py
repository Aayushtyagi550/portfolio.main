import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

sphere_html = '''        </div>
        
        <!-- Interactive 3D Skill Sphere -->
        <div class="sphere-container trigger-skill-card" style="margin-top: 30px; background-color: var(--card-light); border: 1px solid var(--border-cream); border-radius: 12px; padding: 20px; text-align: center; position: relative;">
          <div class="terminal-card-header" data-title="tech_stack_3d.exe"></div>
          <canvas id="skillSphere" width="600" height="600" style="max-width: 100%; outline: none;"></canvas>
          <div id="sphereTags" style="display: none;">
            <ul>
              <li><a href="#" style="color: #ea2d2e;">Java</a></li>
              <li><a href="#" style="color: #007396;">Python</a></li>
              <li><a href="#" style="color: #f89820;">React</a></li>
              <li><a href="#" style="color: #6db33f;">Spring Boot</a></li>
              <li><a href="#" style="color: #4db33d;">MongoDB</a></li>
              <li><a href="#" style="color: #00758f;">SQL</a></li>
              <li><a href="#" style="color: #68a063;">Node.js</a></li>
              <li><a href="#" style="color: #e34c26;">HTML5</a></li>
              <li><a href="#" style="color: #264de4;">CSS3</a></li>
              <li><a href="#" style="color: #f7df1e;">JavaScript</a></li>
              <li><a href="#" style="color: #f05032;">Git</a></li>
              <li><a href="#" style="color: #2496ed;">Docker</a></li>
              <li><a href="#" style="color: #ff9900;">AWS</a></li>
              <li><a href="#" style="color: #ff6c37;">Postman</a></li>
              <li><a href="#" style="color: #000000;">Express</a></li>
            </ul>
          </div>
        </div>
'''

if 'id="skillSphere"' not in html:
    # Safely inject right before PAGE 6
    html = html.replace('      </div>\n    </section>\n\n\n    <!-- PAGE 6: CERTIFICATIONS -->', sphere_html + '      </div>\n    </section>\n\n\n    <!-- PAGE 6: CERTIFICATIONS -->')
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

print("Sphere HTML fixed")
