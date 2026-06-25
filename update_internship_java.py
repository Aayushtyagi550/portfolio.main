import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the title
html = html.replace('<h3>Full Stack Developer Intern - Eduskills</h3>', '<h3>Java Full Stack Developer Intern - Eduskills</h3>')

# Replace the bullet points
old_ul = '''<ul style="color: var(--text-muted); padding-left: 20px; line-height: 1.6; margin-top: 10px;">
                <li>Actively contributed to the design and development of dynamic, full-stack web applications utilizing the MERN stack (MongoDB, Express.js, React.js, Node.js).</li>
                <li>Collaborated closely with cross-functional teams to build highly responsive user interfaces and engineer robust RESTful APIs.</li>
                <li>Optimized database queries and schemas, resulting in significantly faster data retrieval and improved overall system performance.</li>
                <li>Gained hands-on experience in debugging complex issues, writing clean, maintainable code, and deploying scalable solutions.</li>
              </ul>'''

new_ul = '''<ul style="color: var(--text-muted); padding-left: 20px; line-height: 1.6; margin-top: 10px;">
                <li>Actively contributed to the design and development of robust, full-stack web applications utilizing Java and Spring Boot for backend architecture.</li>
                <li>Collaborated closely with cross-functional teams to build highly responsive user interfaces using React.js and engineered secure RESTful APIs.</li>
                <li>Optimized relational database schemas and SQL queries, resulting in significantly faster data retrieval and improved system performance.</li>
                <li>Gained hands-on experience in debugging complex issues, writing clean, maintainable code, and deploying scalable Java-based solutions.</li>
              </ul>'''

html = html.replace(old_ul, new_ul)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
