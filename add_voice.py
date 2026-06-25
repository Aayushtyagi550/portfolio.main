import os

js_code = '''
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
      // Try to find a good English male voice
      const maleVoice = voices.find(v => 
        (v.name.toLowerCase().includes('male') || 
         v.name.includes('David') || 
         v.name.includes('Daniel') || 
         v.name.includes('Mark') ||
         v.name.includes('James')) && v.lang.startsWith('en')
      ) || voices.find(v => v.lang.startsWith('en'));
      
      if (maleVoice) {
        utterance.voice = maleVoice;
      }
      
      // Slightly lower pitch and rate for a smoother male-sounding voice if default is used
      utterance.pitch = 0.85; 
      utterance.rate = 0.95;
      
      window.speechSynthesis.speak(utterance);
    };

    if (window.speechSynthesis.getVoices().length > 0) {
      setVoiceAndSpeak();
    } else {
      window.speechSynthesis.onvoiceschanged = setVoiceAndSpeak;
    }
}

// Browsers block audio until the user interacts with the page.
// We trigger this greeting the very first time they click or scroll anywhere.
document.addEventListener('click', playVoiceGreeting, { once: true });
document.addEventListener('scroll', playVoiceGreeting, { once: true });
document.addEventListener('keydown', playVoiceGreeting, { once: true });
'''

with open('script.js', 'a', encoding='utf-8') as f:
    f.write(js_code)

print("Voice greeting added")
