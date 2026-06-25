import re

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

old_block = '''/* ==========================================================================
   VOICE GREETING (Runs on first user interaction to bypass autoplay limits)
   ========================================================================== */'''

# Let's completely replace everything after this block since I appended it at the end
split_js = js.split(old_block)
base_js = split_js[0]

new_block = '''/* ==========================================================================
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
'''

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(base_js + new_block)

print("Voice greeting updated")
