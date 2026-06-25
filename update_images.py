import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Profile picture (occurs twice, once in about section and maybe once in boot screen or landing, let's just replace all occurrences of the old placeholder)
html = html.replace('assets/profile_aayush.jpg', 'assets/picture.jpeg')
# Just in case some were left as profile.png:
html = html.replace('assets/profile.png', 'assets/picture.jpeg')

# Certificates
html = html.replace('assets/Certificate_HackerRank.jpg', 'assets/cert1.jpg')
html = html.replace('assets/Certificate_Oracle.jpg', 'assets/cert2.jpg')
html = html.replace('assets/Certificate_MongoDB.jpg', 'assets/cert3.jpg')
html = html.replace('assets/Certificate_SQL.jpg', 'assets/cert4.jpg')

# Taskflow project image
# In update_projects.py I used: <img src="assets/profile.png" alt="TaskFlow Screenshot"
# So if it was already changed by the profile replacement above, it's now picture.jpeg.
# Let's fix that specifically for TaskFlow:
html = re.sub(r'<img src="[^"]+" alt="TaskFlow Screenshot"', '<img src="assets/taskflow.png" alt="TaskFlow Screenshot"', html)
html = re.sub(r'data-images="assets/picture\.jpeg"(.*?)alt="TaskFlow Screenshot"', r'data-images="assets/taskflow.png"\1alt="TaskFlow Screenshot"', html, flags=re.DOTALL)

# Achievements LeetCode image
html = html.replace('assets/Leetcode.png', 'assets/leetcode (1).png')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Images mapped")
