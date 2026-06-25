import re

# Read files
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Update LinkedIn
# Old linkedin might be just the placeholder or already updated, but we ensure it matches the requested URL.
html = re.sub(r'https://www\.linkedin\.com/in/[^/"]+/?', 'https://www.linkedin.com/in/aayush-tyagi-39160b359/', html)
js = re.sub(r'https://www\.linkedin\.com/in/[^/"]+/?', 'https://www.linkedin.com/in/aayush-tyagi-39160b359/', js)

# Update Instagram
html = re.sub(r'https://instagram\.com/[^/"]+', 'https://www.instagram.com/tyagi__aayush_?igsh=djNlbnpkYmp2NTJu', html)
js = re.sub(r'https://instagram\.com/[^/"]+', 'https://www.instagram.com/tyagi__aayush_?igsh=djNlbnpkYmp2NTJu', js)

# Update Email
html = re.sub(r'mailto:[^"\' ]+', 'mailto:aayushtyagi728@gmail.com', html)
js = re.sub(r'mailto:[^"\' ]+', 'mailto:aayushtyagi728@gmail.com', js)

# Update Github (base profile, ignoring repo links which already have the correct username)
# Actually, the repo links are fine: github.com/Aayushtyagi550/RepoName
# But for the base profile:
html = re.sub(r'href="https://github\.com/[^/"]+"', 'href="https://github.com/Aayushtyagi550"', html)
js = re.sub(r'href="https://github\.com/[^/"]+"', 'href="https://github.com/Aayushtyagi550"', js)

# Let's save the files
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Socials updated")
