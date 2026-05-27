#!/usr/bin/env python3
"""
Assembles rachel-jordan-portfolio.html from sections/ and styles.css.
Run with: python3 build.py
"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
SECTIONS = ['hero', 'impact', 'experience', 'philosophy', 'recognition', 'education', 'contact']

def read(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

header = """<!DOCTYPE html>
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
    <li><a href="#contact">Contact</a></li>
  </ul>
</nav>
"""

footer = """
<footer>
  &copy; 2026 Rachel Jordan · All rights reserved.
</footer>

</body>
</html>"""

parts = [header]
for name in SECTIONS:
    parts.append(read(os.path.join(BASE, 'sections', f'{name}.html')))
parts.append(footer)

output_path = os.path.join(BASE, 'rachel-jordan-portfolio.html')
with open(output_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(parts))

print(f'Built {output_path}')
