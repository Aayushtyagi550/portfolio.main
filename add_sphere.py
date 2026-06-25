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
    html = html.replace('        </div>\n      </div>\n    </section>\n\n\n    <!-- PAGE 6: PROJECTS -->', sphere_html + '      </div>\n    </section>\n\n\n    <!-- PAGE 6: PROJECTS -->')
    
    # Add TagCanvas script to head
    html = html.replace('</head>', '  <script src="https://www.goat1000.com/tagcanvas.min.js" defer></script>\n</head>')
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)

# 2. Update script.js
with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

sphere_js = '''
  /* ==========================================================================
     3D SKILL SPHERE
     ========================================================================== */
  setTimeout(() => {
    try {
      if(window.TagCanvas) {
        TagCanvas.Start('skillSphere', 'sphereTags', {
          textColour: null,
          outlineColour: 'transparent',
          reverse: true,
          depth: 0.8,
          maxSpeed: 0.05,
          initial: [0.03, -0.03],
          weight: true,
          weightMode: 'both',
          weightFrom: 'data-weight',
          textFont: 'Inter, sans-serif',
          textHeight: 25,
          wheelZoom: false,
          noSelect: true,
          shuffleTags: true,
          freezeActive: false,
          frontSelect: true,
          dragControl: true,
          dragThreshold: 4
        });
        
        // Update colors based on theme if needed, but we injected inline colors!
      }
    } catch(e) {
      console.log('Canvas error:', e);
    }
  }, 1000); // Slight delay to ensure script is loaded
'''

if '3D SKILL SPHERE' not in js:
    js = js.replace('/* ==========================================================================\n     TERMINAL VISUAL & INTERACTIVE ENHANCEMENTS', sphere_js + '\n  /* ==========================================================================\n     TERMINAL VISUAL & INTERACTIVE ENHANCEMENTS')
    
    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(js)

print("Sphere injected")
