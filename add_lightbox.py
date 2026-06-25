import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

lightbox_html = '''
  <!-- Lightbox Modal for Certificates -->
  <div id="imageLightbox" class="lightbox-modal">
    <span class="lightbox-close">&times;</span>
    <img class="lightbox-content" id="lightboxImage">
  </div>
'''

if 'id="imageLightbox"' not in html:
    html = html.replace('</body>', lightbox_html + '\n</body>')
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)


# 2. Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

lightbox_css = '''
/* ==========================================================================
   LIGHTBOX MODAL
   ========================================================================== */
.lightbox-modal {
  display: none; /* Hidden by default */
  position: fixed;
  z-index: 99999; /* Sit on top */
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: hidden;
  background-color: rgba(10, 5, 2, 0.95);
  backdrop-filter: blur(5px);
  opacity: 0;
  transition: opacity 0.3s ease;
  align-items: center;
  justify-content: center;
  cursor: zoom-out; /* Indicate click to close */
}

.lightbox-modal.active {
  display: flex;
  opacity: 1;
}

.lightbox-content {
  margin: auto;
  display: block;
  max-width: 90vw;
  max-height: 90vh;
  border-radius: 8px;
  box-shadow: 0 15px 50px rgba(0,0,0,0.5);
  transform: scale(0.95);
  transition: transform 0.3s cubic-bezier(0.25, 1, 0.5, 1);
  border: 1px solid rgba(179, 133, 92, 0.3);
}

.lightbox-modal.active .lightbox-content {
  transform: scale(1);
}

.lightbox-close {
  position: absolute;
  top: 25px;
  right: 35px;
  color: #eaddd3;
  font-size: 40px;
  font-weight: 300;
  transition: 0.2s;
  cursor: pointer;
  z-index: 100000;
}

.lightbox-close:hover,
.lightbox-close:focus {
  color: var(--accent-gold-light);
  text-decoration: none;
  cursor: pointer;
}
'''

if 'lightbox-modal' not in css:
    css += lightbox_css
    with open('style.css', 'w', encoding='utf-8') as f:
        f.write(css)


# 3. Update script.js
with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

lightbox_js = '''
  /* ==========================================================================
     IMAGE LIGHTBOX (Certificates)
     ========================================================================== */
  const lightbox = document.getElementById('imageLightbox');
  const lightboxImg = document.getElementById('lightboxImage');
  const certLinks = document.querySelectorAll('.cert-image-box a');
  
  if (lightbox && lightboxImg) {
    certLinks.forEach(link => {
      link.addEventListener('click', (e) => {
        e.preventDefault(); // Stop it from opening a new tab
        
        // Grab the high-res image source from the href attribute
        const imgSrc = link.getAttribute('href');
        lightboxImg.src = imgSrc;
        
        // Show the lightbox
        lightbox.classList.add('active');
        document.body.style.overflow = 'hidden'; // Stop background scrolling
      });
    });
    
    // Close lightbox on click anywhere
    lightbox.addEventListener('click', () => {
      lightbox.classList.remove('active');
      document.body.style.overflow = '';
      
      // Remove src after animation completes so it doesn't flash old image next time
      setTimeout(() => {
        if (!lightbox.classList.contains('active')) {
          lightboxImg.src = '';
        }
      }, 300);
    });
  }
'''

# Inject right before the terminal visual enhancements
if 'IMAGE LIGHTBOX (Certificates)' not in js:
    insert_marker = "/* ==========================================================================\n     TERMINAL VISUAL & INTERACTIVE ENHANCEMENTS"
    js = js.replace(insert_marker, lightbox_js + '\n  ' + insert_marker)
    
    # We must also add the cert image boxes to interactiveSelectors so the custom magnetic cursor doesn't steal clicks
    js = js.replace(".cert-card-tilt-container, .logo", ".cert-card-tilt-container, .cert-image-box a, .logo")
    
    with open('script.js', 'w', encoding='utf-8') as f:
        f.write(js)

print("Lightbox added")
