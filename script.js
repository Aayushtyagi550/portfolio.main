document.addEventListener('DOMContentLoaded', () => {
  
  /* ==========================================================================
     MOBILE NAVIGATION TOGGLE
     ========================================================================== */
  const navToggle = document.getElementById('navToggle');
  const navLinks = document.getElementById('navLinks');
  
  if (navToggle && navLinks) {
    navToggle.addEventListener('click', () => {
      const isOpen = navLinks.classList.toggle('open');
      navToggle.classList.toggle('open');
      navToggle.setAttribute('aria-expanded', isOpen);
    });
    
    // Close menu when clicking nav links
    navLinks.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        navLinks.classList.remove('open');
        navToggle.classList.remove('open');
        navToggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  /* ==========================================================================
     SCROLL LINK ACTIVE STATE HIGHLIGHT
     ========================================================================== */
  const sections = document.querySelectorAll('section');
  const navItems = document.querySelectorAll('.nav-links a');
  const header = document.querySelector('header');

  const scrollActiveHighlight = () => {
    let currentSectionId = '';
    const scrollPosition = window.scrollY + 120; // offset

    sections.forEach(section => {
      const sectionTop = section.offsetTop;
      const sectionHeight = section.offsetHeight;
      if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
        currentSectionId = section.getAttribute('id');
      }
    });

    navItems.forEach(item => {
      item.classList.remove('active');
      if (item.getAttribute('href') === `#${currentSectionId}`) {
        item.classList.add('active');
      }
    });

    // Shrink header on scroll
    if (window.scrollY > 50) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  };

  window.addEventListener('scroll', scrollActiveHighlight);
  window.addEventListener('resize', scrollActiveHighlight);

  /* ==========================================================================
     INTERSECTION OBSERVER FOR SCROLL REVEALS
     ========================================================================== */
  const observerOptions = {
    root: null,
    rootMargin: '0px 0px -15% 0px',
    threshold: 0.1
  };

  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('in');
        
        // Trigger specific animations if section has them
        const sectionId = entry.target.getAttribute('id');
        if (sectionId === 'achievements') {
          triggerAchievementsAnimation();
        } else if (sectionId === 'contact') {
          triggerContactFormAnimation();
        }
        
        // Unobserve to trigger only once
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  document.querySelectorAll('.scroll-trigger').forEach(section => {
    observer.observe(section);
  });

  /* ==========================================================================
     SKILLS SECTION ANIMATION DETAILS & CARD LOGGING
     ========================================================================== */
  // Note: Skills section staggered animations are handled natively via CSS transition-delays
  
  // Dynamic card logger diagnostics hover logic
  const skillBadges = document.querySelectorAll('.skill-badge');
  
  skillBadges.forEach(badge => {
    const card = badge.closest('.skill-category-card');
    if (!card) return;
    
    const logTextEl = card.querySelector('.card-console-log .log-text');
    if (!logTextEl) return;
    
    const defaultText = logTextEl.textContent || 'Waiting for diagnostics...';
    if (!logTextEl.hasAttribute('data-default')) {
      logTextEl.setAttribute('data-default', defaultText);
    }
    
    badge.addEventListener('mouseenter', () => {
      const logMsg = badge.getAttribute('data-log') || '';
      if (!logMsg) return;
      
      // Cancel any active typing on this card logger
      if (logTextEl.typingTimer) {
        clearInterval(logTextEl.typingTimer);
      }
      
      logTextEl.textContent = '';
      logTextEl.setAttribute('data-active-badge', badge.querySelector('.badge-name').textContent);
      
      let charIndex = 0;
      logTextEl.typingTimer = setInterval(() => {
        if (charIndex < logMsg.length) {
          logTextEl.textContent += logMsg.charAt(charIndex);
          charIndex++;
        } else {
          clearInterval(logTextEl.typingTimer);
          logTextEl.typingTimer = null;
        }
      }, 12); // Stream at high speed (12ms per char)
    });
    
    badge.addEventListener('mouseleave', () => {
      // Revert to default ONLY if this badge is still the active badge in the logger
      const activeBadgeName = logTextEl.getAttribute('data-active-badge');
      const thisBadgeName = badge.querySelector('.badge-name').textContent;
      
      if (activeBadgeName === thisBadgeName) {
        if (logTextEl.typingTimer) {
          clearInterval(logTextEl.typingTimer);
          logTextEl.typingTimer = null;
        }
        logTextEl.removeAttribute('data-active-badge');
        logTextEl.textContent = logTextEl.getAttribute('data-default') || 'Waiting for diagnostics...';
      }
    });
  });

  /* ==========================================================================
     ACHIEVEMENTS COUNTER ANIMATION
     ========================================================================== */
  let achievementsAnimated = false;
  
  const triggerAchievementsAnimation = () => {
    if (achievementsAnimated) return;
    achievementsAnimated = true;

    const certCounter = document.getElementById('certCounter');
    const projectCounter = document.getElementById('projectCounter');

    const animateCounter = (el, target) => {
      if (!el) return;
      let current = 0;
      const duration = 1000; // 1s
      const stepTime = Math.max(Math.floor(duration / target), 30);
      
      const timer = setInterval(() => {
        current++;
        el.textContent = current;
        if (current >= target) {
          clearInterval(timer);
          el.textContent = `${target}+`;
        }
      }, stepTime);
    };

    if (certCounter) {
      const targetVal = parseInt(certCounter.getAttribute('data-value') || '4', 10);
      animateCounter(certCounter, targetVal);
    }
    if (projectCounter) {
      const targetVal = parseInt(projectCounter.getAttribute('data-value') || '2', 10);
      let current = 0;
      const timer = setInterval(() => {
        current++;
        projectCounter.textContent = current;
        if (current >= targetVal) {
          clearInterval(timer);
        }
      }, 150);
    }
  };

  /* ==========================================================================
     PROJECT SCREENSHOT GALLERY SWITCHER
     ========================================================================== */
  const screenshotContainers = document.querySelectorAll('.proj-screenshot-container');
  screenshotContainers.forEach(container => {
    const img = container.querySelector('.proj-screenshot');
    const dots = container.querySelectorAll('.gallery-indicator .dot');
    const imagesStr = container.getAttribute('data-images');
    if (img && imagesStr) {
      const images = imagesStr.split(',');
      
      const cycleImage = () => {
        let currentIdx = parseInt(container.getAttribute('data-current') || '0', 10);
        currentIdx = (currentIdx + 1) % images.length;
        container.setAttribute('data-current', currentIdx);
        
        img.style.opacity = '0';
        setTimeout(() => {
          img.src = images[currentIdx];
          img.style.opacity = '1';
        }, 250);

        dots.forEach((dot, dotIdx) => {
          if (dotIdx === currentIdx) {
            dot.classList.add('active');
          } else {
            dot.classList.remove('active');
          }
        });
      };

      // Set up autoplay interval (3.5 seconds)
      let autoPlayInterval = setInterval(cycleImage, 3500);

      // Manual click override
      container.addEventListener('click', () => {
        cycleImage();
      });

      // Pause autoplay on mouse enter
      container.addEventListener('mouseenter', () => {
        clearInterval(autoPlayInterval);
      });

      // Resume autoplay on mouse leave
      container.addEventListener('mouseleave', () => {
        autoPlayInterval = setInterval(cycleImage, 3500);
      });
    }
  });

  /* ==========================================================================
     CONTACT FORM SEQUENTIAL UNDERLINE & PULSE
     ========================================================================== */
  let contactAnimated = false;

  const triggerContactFormAnimation = () => {
    if (contactAnimated) return;
    contactAnimated = true;

    const formGroups = document.querySelectorAll('.contact-form-panel .form-group');
    const sendBtn = document.getElementById('sendBtn');

    // Sequential underline drawing
    formGroups.forEach((group, index) => {
      setTimeout(() => {
        group.classList.add('drawn');
      }, index * 300); // 300ms sequential stagger
    });

    // Button pulse after draw sequence ends
    const totalDrawTime = formGroups.length * 300 + 400;
    setTimeout(() => {
      if (sendBtn) {
        sendBtn.classList.add('submit-pulse');
        // Remove after one cycle
        setTimeout(() => {
          sendBtn.classList.remove('submit-pulse');
        }, 1500);
      }
    }, totalDrawTime);
  };

  /* ==========================================================================
     3D MOUSE-FOLLOW TILT ON CERTIFICATIONS
     ========================================================================== */
  const certContainers = document.querySelectorAll('.cert-card-tilt-container');

  certContainers.forEach(container => {
    const card = container.querySelector('.cert-card-placeholder');
    if (card) {
      let rect = null;

      container.addEventListener('mouseenter', () => {
        rect = container.getBoundingClientRect();
        card.style.transition = 'none'; // Disable transition for instant mouse tracking
      });

      container.addEventListener('mousemove', (e) => {
        if (!rect) {
          rect = container.getBoundingClientRect();
        }
        const x = e.clientX - rect.left - rect.width / 2;
        const y = e.clientY - rect.top - rect.height / 2;
        
        // Calculate rotation bounds (5 degrees max)
        const rotX = -(y / (rect.height / 2)) * 5;
        const rotY = (x / (rect.width / 2)) * 5;

        card.style.transform = `rotateX(${rotX}deg) rotateY(${rotY}deg) scale3d(1.02, 1.02, 1.02)`;
      });

      container.addEventListener('mouseleave', () => {
        rect = null;
        card.style.transition = 'transform 0.5s cubic-bezier(0.25, 0.8, 0.25, 1)'; // Smooth spring-like reset transition
        card.style.transform = 'rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)';
      });
    }
  });

  /* ==========================================================================
     MISSION / VISION TAPPING FOR MOBILE DEVICES
     ========================================================================== */
  document.querySelectorAll('.mv-card').forEach(card => {
    card.addEventListener('click', (e) => {
      // Toggle flipped state
      card.classList.toggle('flipped');
    });
  });

  /* ==========================================================================
     CONTACT FORM SUBMISSION ACTION
     ========================================================================== */
  const contactForm = document.getElementById('contactForm');
  
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      
      const fullName = document.getElementById('fullName').value.trim();
      const emailAddress = document.getElementById('emailAddress').value.trim();
      const phoneNumber = document.getElementById('phoneNumber') ? document.getElementById('phoneNumber').value.trim() : '';
      const message = document.getElementById('message').value.trim();
      
      if (!fullName || !emailAddress || !message) {
        alert('Please fill out all required fields (Name, Email, Message) before sending.');
        return;
      }
      
      // Email validation regex
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegex.test(emailAddress)) {
        alert('Please enter a valid email address.');
        return;
      }
      
      // Construct mailto link
      const emailRecipient = 'aayushtyagi728@gmail.com';
      const mailtoSubject = encodeURIComponent(`[Portfolio Inquiry] Message from ${fullName}`);
      
      let emailBody = `Hello Aayush,\n\n` + 
                        `You have received a new inquiry from your portfolio website.\n\n` +
                        `Name: ${fullName}\n` +
                        `Email: ${emailAddress}\n`;
                        
      if (phoneNumber) {
        emailBody += `Phone: ${phoneNumber}\n`;
      }
      
      emailBody += `\nMessage:\n${message}\n\n` +
                   `Best regards,\n` +
                   `${fullName}`;
                         
      const mailtoBody = encodeURIComponent(emailBody);
      
      // Open mail client
      window.location.href = `mailto:aayushtyagi728@gmail.com?subject=${mailtoSubject}&body=${mailtoBody}`;
    });
  }

  /* ==========================================================================
     DARK MODE THEME TOGGLE
     ========================================================================== */
  const themeToggle = document.getElementById('themeToggle');
  const sunIcon = document.querySelector('.sun-icon');
  const moonIcon = document.querySelector('.moon-icon');
  const themeText = document.querySelector('.theme-text');

  if (themeToggle) {
    // Check local storage or system preference
    const currentTheme = localStorage.getItem('theme') || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    
    if (currentTheme === 'dark') {
      document.body.classList.add('dark-mode');
      if (sunIcon) sunIcon.style.display = 'none';
      if (moonIcon) moonIcon.style.display = 'inline-block';
      if (themeText) themeText.textContent = 'LIGHT';
    } else {
      document.body.classList.remove('dark-mode');
      if (sunIcon) sunIcon.style.display = 'inline-block';
      if (moonIcon) moonIcon.style.display = 'none';
      if (themeText) themeText.textContent = 'DARK';
    }

    themeToggle.addEventListener('click', () => {
      document.body.classList.add('theme-transition');
      document.body.classList.toggle('dark-mode');
      const isDark = document.body.classList.contains('dark-mode');
      localStorage.setItem('theme', isDark ? 'dark' : 'light');
      
      if (isDark) {
        if (sunIcon) sunIcon.style.display = 'none';
        if (moonIcon) moonIcon.style.display = 'inline-block';
        if (themeText) themeText.textContent = 'LIGHT';
      } else {
        if (sunIcon) sunIcon.style.display = 'inline-block';
        if (moonIcon) moonIcon.style.display = 'none';
        if (themeText) themeText.textContent = 'DARK';
      }

      setTimeout(() => {
        document.body.classList.remove('theme-transition');
      }, 500);
    });
  }
  
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

  /* ==========================================================================
     TERMINAL VISUAL & INTERACTIVE ENHANCEMENTS
     ========================================================================== */

  // 1. Session-Tracked Boot Screen
  const bootOverlay = document.getElementById('bootOverlay');
  const skipBootBtn = document.getElementById('skipBootBtn');

  if (bootOverlay) {
    let countInterval;
    const skipBoot = () => {
      if (countInterval) clearInterval(countInterval);
      bootOverlay.classList.add('fade-out');
      sessionStorage.setItem('vk_booted', 'true');
      setTimeout(() => {
        bootOverlay.style.display = 'none';
      }, 800); // match CSS transition duration
    };

    if (sessionStorage.getItem('vk_booted') === 'true') {
      bootOverlay.style.display = 'none';
    } else {
      // Auto-hide boot screen after 1.8s
      const bootTimer = setTimeout(skipBoot, 1850);

      // Animate progress bar percentage from 0 to 100
      const percentEl = document.getElementById('bootProgressPercent');
      if (percentEl) {
        let count = 0;
        const duration = 1800; // 1.8s
        const steps = 100;
        const stepTime = duration / steps; // 18ms per step
        
        countInterval = setInterval(() => {
          count++;
          percentEl.textContent = `${count}%`;
          if (count >= 100) {
            clearInterval(countInterval);
          }
        }, stepTime);
      }

      if (skipBootBtn) {
        skipBootBtn.addEventListener('click', () => {
          clearTimeout(bootTimer);
          skipBoot();
        });
      }

      // Allow Escape key to skip boot sequence
      const escBootHandler = (e) => {
        if (e.key === 'Escape') {
          clearTimeout(bootTimer);
          skipBoot();
          window.removeEventListener('keydown', escBootHandler);
        }
      };
      window.addEventListener('keydown', escBootHandler);
    }
  }

  // 2. Monospace Typography Toggle
  const monoToggle = document.getElementById('monoToggle');
  if (monoToggle) {
    const enableMonoMode = () => {
      document.body.classList.add('terminal-font-mode');
      localStorage.setItem('vk_mono_mode', 'true');
      const monoText = monoToggle.querySelector('.mono-text');
      if (monoText) monoText.textContent = 'STANDARD';
    };

    const disableMonoMode = () => {
      document.body.classList.remove('terminal-font-mode');
      localStorage.setItem('vk_mono_mode', 'false');
      const monoText = monoToggle.querySelector('.mono-text');
      if (monoText) monoText.textContent = 'MONO';
    };

    // Load initial preference
    if (localStorage.getItem('vk_mono_mode') === 'true') {
      enableMonoMode();
    }

    monoToggle.addEventListener('click', () => {
      if (document.body.classList.contains('terminal-font-mode')) {
        disableMonoMode();
      } else {
        enableMonoMode();
      }
    });
  }

  // 3. Card Terminal Headers Injection
  const cardHeaders = document.querySelectorAll('.terminal-card-header');
  cardHeaders.forEach(header => {
    const title = header.getAttribute('data-title') || 'config.sys';
    header.innerHTML = `
      <div class="window-dots">
        <span class="window-dot red"></span>
        <span class="window-dot yellow"></span>
        <span class="window-dot green"></span>
      </div>
      <div class="window-title">${title}</div>
    `;
  });

  // 4. Scroll-Triggered Typing Prompts
  const prompts = document.querySelectorAll('.terminal-prompt');
  
  const typePrompt = (promptEl) => {
    const cmd = promptEl.getAttribute('data-cmd') || '';
    promptEl.innerHTML = `<span style="color: var(--accent-gold-light)">aayush@tyagi:~$</span> `;
    promptEl.classList.add('typing');
    
    let i = 0;
    const typeSpeed = () => Math.random() * 40 + 30; // 30ms to 70ms per character
    
    function type() {
      if (i < cmd.length) {
        promptEl.innerHTML += cmd.charAt(i);
        i++;
        setTimeout(type, typeSpeed());
      } else {
        setTimeout(() => {
          promptEl.classList.remove('typing');
        }, 1500); // keep cursor blinking for 1.5s
      }
    }
    
    type();
  };

  const promptObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        typePrompt(entry.target);
        observer.unobserve(entry.target);
      }
    });
  }, {
    root: null,
    rootMargin: '0px 0px -10% 0px',
    threshold: 0.1
  });

  prompts.forEach(p => {
    p.innerHTML = `<span style="color: var(--accent-gold-light)">aayush@tyagi:~$</span> `;
    promptObserver.observe(p);
  });

  // 5. Floating Console Widget & Router Engine
  const terminalToggleBtn = document.getElementById('terminalToggleBtn');
  const terminalConsole = document.getElementById('terminalConsole');
  const consoleCloseBtn = document.getElementById('consoleCloseBtn');
  const consoleForm = document.getElementById('consoleForm');
  const consoleInput = document.getElementById('consoleInput');
  const consoleOutputLog = document.getElementById('consoleOutputLog');

  if (terminalToggleBtn && terminalConsole) {
    // Inject welcome banner art
    if (consoleOutputLog) {
      consoleOutputLog.innerHTML = `
<div class="console-line ascii-art"> _   _  _   ___ _   _ ___  _______     __
| | | |/_\\ / __| | | |   \\| __\\ \\ \\   / /
| |_| / _ \\\\__ \\ |_| | |) | _| \\ \\ \\ / / 
 \\___/_/ \\_\\___/\\___/|___/|___| \\_\\_/_/  </div>
<div class="console-line system-msg">Welcome to Aayush's Interactive Terminal CLI v1.0.0.</div>
<div class="console-line system-msg">Type 'help' to see all available commands.</div>
<div class="console-line system-msg">[Tip: Press keyboard hotkeys (when console is closed) to scroll: 's' skills, 'p' projects, 'c' contact, 'e' education, 'a' about]</div>
<div class="console-line system-msg">[Or type single-letter commands (a, s, p, e, c, t) directly inside this terminal!]</div>
<br>
      `;
    }

    // Quick Pills click execution binding
    const consolePills = terminalConsole.querySelectorAll('.console-pill');
    consolePills.forEach(pill => {
      pill.addEventListener('click', (e) => {
        e.stopPropagation();
        const cmd = pill.getAttribute('data-cmd');
        if (cmd && consoleInput && consoleForm) {
          consoleInput.value = cmd;
          // Dispatch submit event to trigger the router
          consoleForm.dispatchEvent(new Event('submit'));
        }
      });
    });

    // Open/Close Console Panel
    terminalToggleBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      const isOpen = terminalConsole.classList.toggle('open');
      if (isOpen) {
        setTimeout(() => {
          consoleInput.focus();
        }, 100);
        scrollToBottom();
      }
    });

    // Close Button Action
    if (consoleCloseBtn) {
      consoleCloseBtn.addEventListener('click', (e) => {
        e.stopPropagation();
        terminalConsole.classList.remove('open');
      });
    }

    // Close when clicking outside of console
    document.addEventListener('click', (e) => {
      if (terminalConsole.classList.contains('open') && 
          !terminalConsole.contains(e.target) && 
          !terminalToggleBtn.contains(e.target)) {
        terminalConsole.classList.remove('open');
      }
    });

    // Focus input when clicking anywhere inside console body
    terminalConsole.querySelector('.console-body').addEventListener('click', () => {
      consoleInput.focus();
    });

    // Handle Escape key or key shortcuts
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && terminalConsole.classList.contains('open')) {
        terminalConsole.classList.remove('open');
      }
    });

    // Global Keyboard Navigation Shortcuts
    window.addEventListener('keydown', (e) => {
      // Ignore keyboard shortcuts if typing inside input/textarea
      const activeEl = document.activeElement;
      if (activeEl && (activeEl.tagName === 'INPUT' || activeEl.tagName === 'TEXTAREA' || activeEl.isContentEditable)) {
        return;
      }

      const key = e.key.toLowerCase();
      
      // Toggle console panel on ` (backtick) or 't'
      if (e.key === '`' || key === 't') {
        e.preventDefault();
        const isOpen = terminalConsole.classList.toggle('open');
        if (isOpen) {
          setTimeout(() => {
            consoleInput.focus();
          }, 100);
          scrollToBottom();
        } else {
          consoleInput.blur();
        }
      }

      // Smooth scroll to sections on hotkeys
      if (key === 's') {
        e.preventDefault();
        document.getElementById('skills')?.scrollIntoView({ behavior: 'smooth' });
      } else if (key === 'p') {
        e.preventDefault();
        document.getElementById('projects')?.scrollIntoView({ behavior: 'smooth' });
      } else if (key === 'c') {
        e.preventDefault();
        document.getElementById('contact')?.scrollIntoView({ behavior: 'smooth' });
      } else if (key === 'e') {
        e.preventDefault();
        document.getElementById('education')?.scrollIntoView({ behavior: 'smooth' });
      } else if (key === 'a') {
        e.preventDefault();
        document.getElementById('about')?.scrollIntoView({ behavior: 'smooth' });
      }
    });

    // Scroll output to bottom helper
    const scrollToBottom = () => {
      consoleOutputLog.scrollTop = consoleOutputLog.scrollHeight;
    };

    // Print lines helper
    const printLine = (content, type = 'output-text') => {
      const line = document.createElement('div');
      line.className = `console-line ${type}`;
      line.innerHTML = content;
      consoleOutputLog.appendChild(line);
      scrollToBottom();
    };

    // Form submission processing commands
    consoleForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const rawVal = consoleInput.value;
      let cmd = rawVal.trim().toLowerCase();
      consoleInput.value = '';

      // Echo User Command
      printLine(`<span class="console-prompt">aayush@tyagi:~$</span> ${rawVal}`, 'cmd-echo');

      if (!cmd) {
        scrollToBottom();
        return;
      }

      // Handle quotes inside input: strip single and double quotes (e.g. 'c' or "c")
      cmd = cmd.replace(/['"]/g, '');

      // Router Switch Board
      switch (cmd) {
        case 'help':
        case 'h':
          printLine('Available commands:', 'system-msg');
          printLine('  <span style="color: var(--accent-gold)">about</span> (a)     - Short biography & focus areas');
          printLine('  <span style="color: var(--accent-gold)">skills</span> (s)    - Loaded system modules & technical skills config');
          printLine('  <span style="color: var(--accent-gold)">projects</span> (p)  - Featured development projects with links');
          printLine('  <span style="color: var(--accent-gold)">education</span> (e) - Academic timeline & qualifications');
          printLine('  <span style="color: var(--accent-gold)">contact</span> (c)   - Email, GitHub, and social channels');
          printLine('  <span style="color: var(--accent-gold)">exit</span> (t)      - Close console terminal');
          printLine('  <span style="color: var(--accent-gold)">clear</span>         - Clear console history');
          printLine('  <span style="color: var(--accent-gold)">help</span> (h)      - Show this help directory');
          break;

        case 'about':
        case 'a':
          printLine('Aayush Tyagi — Software Engineer', 'success-msg');
          printLine('Specializing in Java, DSA, and Full-Stack MERN stack development.');
          printLine('Passionate about building AI-integrated web platforms, refining database schemas, and solving core algorithmic puzzles.');
          printLine('<br>Current Focus: AI Healthcare Triage & Emotion-Driven Music Streaming.');
          break;

        case 'skills':
        case 's':
          printLine('System Modules Configuration Status:', 'success-msg');
          printLine('  [Languages]   - Java, JavaScript, SQL, C/C++');
          printLine('  [Frontend]    - React.js, Tailwind CSS, HTML5, CSS3, Bootstrap');
          printLine('  [Backend]     - Node.js, Express.js, REST APIs');
          printLine('  [Databases]   - MongoDB, MySQL');
          printLine('  [Core CS]     - Data Structures, OOPs, DBMS, OS, Networks');
          printLine('  [Tools]       - Git, GitHub, Postman, VS Code');
          break;

        case 'projects':
        case 'p':
          printLine('Featured Projects:', 'success-msg');
          printLine('1. <span style="font-weight: bold; color: #fff;">SymptoGenie (AI Healthcare Assistant)</span>');
          printLine('   - OCR/NLP clinical report processing & ailment triage scoring.');
          printLine('   - GitHub: <a href="https://github.com/Aayushtyagi550/SymptoGenie---AI-Health-App.git" target="_blank" rel="noopener noreferrer">SymptoGenie Repo</a>');
          printLine('   - Live: <a href="https://symptogenie-a-health-monitoring-platform.onrender.com/dashboard" target="_blank" rel="noopener noreferrer">SymptoGenie Demo</a>');
          printLine('');
          printLine('2. <span style="font-weight: bold; color: #fff;">MelodyVerse (AI-Powered Music Streaming)</span>');
          printLine('   - Voice search via Gemini 2.5 Flash & Emotion playlist mapping.');
          printLine('   - GitHub: <a href="https://github.com/Aayushtyagi550/MelodyVerse---Web-Music-Player.git" target="_blank" rel="noopener noreferrer">MelodyVerse Repo</a>');
          printLine('   - Live: <a href="https://melodyverse-web-music-player.onrender.com/" target="_blank" rel="noopener noreferrer">MelodyVerse Demo</a>');
          break;

        case 'education':
        case 'edu':
        case 'e':
          printLine('Academic Qualifications & Timeline:', 'success-msg');
          printLine('1. <span style="font-weight: bold; color: #fff;">B.Tech in Computer Science</span> (2022 – 2026)');
          printLine('   - Meerut Institute of Engineering and Technology (MIET)');
          printLine('   - Key Focus: Algorithms, OOPs, DBMS, OS, Computer Networks.');
          printLine('');
          printLine('2. <span style="font-weight: bold; color: #fff;">Class 12th</span> (2022 – 2023)');
          printLine('   - Guru Govind Singh Public School');
          printLine('');
          printLine('3. <span style="font-weight: bold; color: #fff;">Class 10th</span> (2020 – 2021)');
          printLine('   - Guru Govind Singh Public School');
          break;

        case 'contact':
        case 'c':
          printLine('Connecting sockets...', 'system-msg');
          printLine('  Email:    <a href="mailto:aayushtyagi728@gmail.com">aayushtyagi728@gmail.com</a>');
          printLine('  GitHub:   <a href="https://github.com/Aayushtyagi550" target="_blank" rel="noopener noreferrer">github.com/Aayushtyagi550</a>');
          printLine('  LinkedIn: <a href="https://www.linkedin.com/in/aayush-tyagi-39160b359/" target="_blank" rel="noopener noreferrer">linkedin.com/in/aayush-tyagi-39160b359/</a>');
          printLine('  LeetCode: <a href="https://leetcode.com/u/tyagiaayush0007/" target="_blank" rel="noopener noreferrer">leetcode.com/u/tyagiaayush0007/</a>');
          break;

        case 'exit':
        case 'quit':
        case 'q':
        case 't':
        case '`':
          terminalConsole.classList.remove('open');
          consoleInput.blur();
          break;

        case 'clear':
          consoleOutputLog.innerHTML = '';
          printLine('Console cleared. Type "help" to see available commands.', 'system-msg');
          break;

        default:
          printLine(`sh: command not found: ${cmd}. Type 'help' to see all available commands.`, 'error-msg');
      }
      scrollToBottom();
    });
  }

  /* ==========================================================================
     CUSTOM INTERACTIVE MOUSE CURSOR (Option 2: Magnetic Ring Halo)
     ========================================================================== */
  const cursorDot = document.querySelector('.custom-cursor-dot');
  const cursorOutline = document.querySelector('.custom-cursor-outline');

  if (cursorDot && cursorOutline && window.innerWidth > 768) {
    let mouseX = 0;
    let mouseY = 0;
    let dotX = 0;
    let dotY = 0;
    let outlineX = 0;
    let outlineY = 0;
    let hoveredEl = null;

    window.addEventListener('mousemove', (e) => {
      mouseX = e.clientX;
      mouseY = e.clientY;
    });

    const updateCursor = () => {
      // Precision inner dot positioning (lerp 0.25)
      dotX += (mouseX - dotX) * 0.25;
      dotY += (mouseY - dotY) * 0.25;
      cursorDot.style.left = `${dotX}px`;
      cursorDot.style.top = `${dotY}px`;

      // Magnet snap logic for outer outline
      if (hoveredEl) {
        const rect = hoveredEl.getBoundingClientRect();
        // Only snap to center for small elements (links, buttons, socials, logo)
        if (rect.width < 200 && rect.height < 100) {
          const targetX = rect.left + rect.width / 2;
          const targetY = rect.top + rect.height / 2;
          
          outlineX += (targetX - outlineX) * 0.22; // Quick snap
          outlineY += (targetY - outlineY) * 0.22;
          
          cursorOutline.style.width = `${rect.width + 12}px`;
          cursorOutline.style.height = `${rect.height + 12}px`;
          
          const computedStyle = window.getComputedStyle(hoveredEl);
          cursorOutline.style.borderRadius = computedStyle.borderRadius;
        } else {
          // Large card hover: follow mouse but expand to standard 60px circular halo
          outlineX += (mouseX - outlineX) * 0.15;
          outlineY += (mouseY - outlineY) * 0.15;
          
          cursorOutline.style.width = '60px';
          cursorOutline.style.height = '60px';
          cursorOutline.style.borderRadius = '50%';
        }
      } else {
        // Standard idle state: follow mouse, default 30px circular ring
        outlineX += (mouseX - outlineX) * 0.15;
        outlineY += (mouseY - outlineY) * 0.15;
        
        cursorOutline.style.width = '30px';
        cursorOutline.style.height = '30px';
        cursorOutline.style.borderRadius = '50%';
      }

      cursorOutline.style.left = `${outlineX}px`;
      cursorOutline.style.top = `${outlineY}px`;

      requestAnimationFrame(updateCursor);
    };
    
    // Start animation loop
    requestAnimationFrame(updateCursor);

    // Interactive Hover States
    const interactiveSelectors = 'a, button, input, textarea, select, .proj-screenshot-container, .edu-card, .mv-card, .ach-card, .cert-card-tilt-container, .cert-image-box a, .logo, .social-btn-round, .proj-btn, .counter-num';
    
    const addHoverClass = (el) => {
      document.body.classList.add('cursor-hovering');
      hoveredEl = el;
    };
    
    const removeHoverClass = () => {
      document.body.classList.remove('cursor-hovering');
      hoveredEl = null;
    };

    document.querySelectorAll(interactiveSelectors).forEach((el) => {
      el.addEventListener('mouseenter', () => addHoverClass(el));
      el.addEventListener('mouseleave', removeHoverClass);
    });

    // Delegate hover detection for dynamically updated components
    window.addEventListener('mouseover', (e) => {
      const match = e.target.closest(interactiveSelectors);
      if (match) {
        addHoverClass(match);
      } else {
        removeHoverClass();
      }
    });

    // Mouse Press Effects
    window.addEventListener('mousedown', () => {
      document.body.classList.add('cursor-clicking');
    });

    window.addEventListener('mouseup', () => {
      document.body.classList.remove('cursor-clicking');
    });
  }
});

/* ==========================================================================
   VOICE GREETING (Runs on first user interaction to bypass autoplay limits)
   ========================================================================== */
let hasSpokenGreeting = false;

function playVoiceGreeting() {
    if (hasSpokenGreeting) return;
    hasSpokenGreeting = true;

    const text = "Hi! I am Aayush Tyagi, a passionate Java Full Stack Developer. Welcome to my portfolio! I specialize in building dynamic web applications using React, Spring Boot, and databases like MySQL and MongoDB. Feel free to explore my projects, certifications, and experience.";
    const utterance = new SpeechSynthesisUtterance(text);
    
    const setVoiceAndSpeak = () => {
      const voices = window.speechSynthesis.getVoices();
      
      // Strict filter for Male English voices
      let maleVoice = voices.find(v => 
        (v.name.toLowerCase().includes('male') || 
         v.name.includes('Mark') || // Windows Male
         v.name.includes('David') || // Windows Desktop Male
         v.name.includes('Alex') || // Mac Male
         v.name.includes('Daniel') || // Mac UK Male
         v.name.includes('Arthur') ||
         v.name.includes('James')) && v.lang.startsWith('en')
      );

      // If absolutely no male voice is found by name, we just pick the first voice, 
      // but pitch it down heavily so it sounds masculine
      if (maleVoice) {
        utterance.voice = maleVoice;
        utterance.pitch = 0.9; 
      } else {
        utterance.pitch = 0.5; // Deepen the voice forcefully if it defaults to female
      }
      
      utterance.rate = 0.95;
      
      // Speak the text
      window.speechSynthesis.speak(utterance);
      
      // Force stop it after 45 seconds to ensure it is less than 1 minute
      setTimeout(() => {
          window.speechSynthesis.cancel();
      }, 45000);
    };

    if (window.speechSynthesis.getVoices().length > 0) {
      setVoiceAndSpeak();
    } else {
      window.speechSynthesis.onvoiceschanged = setVoiceAndSpeak;
    }
}

document.addEventListener('click', playVoiceGreeting, { once: true });
document.addEventListener('scroll', playVoiceGreeting, { once: true });
document.addEventListener('keydown', playVoiceGreeting, { once: true });
