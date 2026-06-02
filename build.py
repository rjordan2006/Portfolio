#!/usr/bin/env python3
"""
Assembles rachel-jordan-portfolio.html and contact.html from sections/ and styles.css.
Run with: python3 build.py
"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
SECTIONS = ['hero', 'impact', 'experience', 'philosophy', 'recognition', 'education']

def read(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

main_nav = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Rachel Jordan — Product Executive</title>
  <link rel="stylesheet" href="styles.css" />
</head>
<body>

<!-- NAV -->
<nav>
  <a class="nav-brand" href="#hero">Rachel Jordan</a>
  <ul class="nav-links">
    <li><a href="#impact">Impact</a></li>
    <li><a href="#experience">Experience</a></li>
    <li><a href="#philosophy">Philosophy</a></li>
    <li><a href="#recognition">Recognition</a></li>
    <li><a href="contact.html">Contact</a></li>
  </ul>
</nav>
"""

contact_nav = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Contact — Rachel Jordan</title>
  <link rel="stylesheet" href="styles.css" />
</head>
<body>

<!-- NAV -->
<nav>
  <a class="nav-brand" href="rachel-jordan-portfolio.html">Rachel Jordan</a>
  <ul class="nav-links">
    <li><a href="rachel-jordan-portfolio.html#impact">Impact</a></li>
    <li><a href="rachel-jordan-portfolio.html#experience">Experience</a></li>
    <li><a href="rachel-jordan-portfolio.html#philosophy">Philosophy</a></li>
    <li><a href="rachel-jordan-portfolio.html#recognition">Recognition</a></li>
    <li><a href="contact.html">Contact</a></li>
  </ul>
</nav>
"""

footer = """
<footer>
  &copy; 2026 Rachel Jordan · All rights reserved.
</footer>

</body>
</html>"""

# Build main portfolio page
parts = [main_nav]
for name in SECTIONS:
    parts.append(read(os.path.join(BASE, 'sections', f'{name}.html')))
parts.append(footer)

main_path = os.path.join(BASE, 'index.html')
with open(main_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(parts))
print(f'Built {main_path}')

# Build contact page
contact_parts = [contact_nav, read(os.path.join(BASE, 'sections', 'contact.html')), footer]

contact_path = os.path.join(BASE, 'contact.html')
with open(contact_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(contact_parts))
print(f'Built {contact_path}')
