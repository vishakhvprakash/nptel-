import subprocess
import json
import os

test_html = r'''<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
</body>
</html>'''

# Let's inspect index.html using python to find any min-w or fixed w
with open(r'C:\Users\pcvis\.gemini\antigravity\scratch\swayam-progress\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
fixed_w = re.findall(r'class="[^"]*\bw-\[[^\]]+\][^"]*"', text)
print('Fixed w-[...] classes:')
for w in set(fixed_w):
    print(' ', w)

min_w = re.findall(r'class="[^"]*\bmin-w-\[[^\]]+\][^"]*"', text)
print('Min w-[...] classes:')
for m in set(min_w):
    print(' ', m)
