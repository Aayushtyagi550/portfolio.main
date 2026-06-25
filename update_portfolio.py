import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replacements
content = re.sub(r'Vasudev Katariya', 'Aayush Tyagi', content)
content = re.sub(r'Vasudev', 'Aayush', content)
content = re.sub(r'vasudevkatariya75668@gmail\.com', 'aayushtyagi728@gmail.com', content)
content = re.sub(r'vasudev\.katariya_', 'aayush.tyagi_', content)
content = re.sub(r'vasudev7891', 'AayushTyagi', content) # Github placeholder
content = re.sub(r'vasudevwx', 'AayushTyagi', content) # Insta placeholder
content = re.sub(r'vasudev-katariya-cse', 'aayush-tyagi-39160b359', content)
content = re.sub(r'vasudev@portfolio', 'aayush@portfolio', content)
content = re.sub(r'vasudev@katariya', 'aayush@tyagi', content)

# Landing text
content = re.sub(r'Java &amp; DSA', 'Python &amp; SQL', content)
content = re.sub(r'I craft high-performance full-stack systems and solve complex algorithmic problems\.', 'Full Stack Developer with experience in building scalable web applications. Skilled in frontend and backend technologies, APIs, and databases. Interested in AI-based solutions.', content)

# About section text
about_text_old = r'"I\'m a Computer Science undergraduate at Meerut Institute of Engineering and Technology.*?"'
about_text_new = r'"I\'m a Full Stack Developer with experience in building scalable web applications. My foundation is in Python, Java, JavaScript, and SQL. On the applied side, I work across the MERN stack (React.js, Node.js, Express.js, MongoDB) to design REST APIs, model databases, and ship interfaces that hold up under real use. My recent projects lean into AI integration, including platforms for disease prediction using ML, OCR, and NLP."'
content = re.sub(about_text_old, about_text_new, content, flags=re.DOTALL)

# Education
content = re.sub(r'8\.35 / 10\.0 through the 5th semester', '8.91 / 10.0', content)
content = re.sub(r'Scored 94%', 'Scored 92%', content)
content = re.sub(r'Scored 94\.6%', 'Scored 81%', content)

# Achievements
content = re.sub(r'Solved 400\+ problems on LeetCode', 'Solved 100+ problems on LeetCode', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

with open('script.js', 'r', encoding='utf-8') as f:
    script_content = f.read()

script_content = re.sub(r'Vasudev Katariya', 'Aayush Tyagi', script_content)
script_content = re.sub(r'Vasudev', 'Aayush', script_content)
script_content = re.sub(r'vasudevkatariya75668@gmail\.com', 'aayushtyagi728@gmail.com', script_content)
script_content = re.sub(r'vasudev@katariya', 'aayush@tyagi', script_content)
script_content = re.sub(r'vasudev-katariya-cse', 'aayush-tyagi-39160b359', script_content)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(script_content)

print("Replacement successful")
