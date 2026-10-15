# Let's add a tiny script at top of index.html that finds the culprit
with open(r'C:\Users\pcvis\.gemini\antigravity\scratch\swayam-progress\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect all elements with fixed width in index.html
import re
tags = re.findall(r'<[a-zA-Z0-9]+[^>]*style="[^"]*"', text)
print(f'Total elements with inline style: {len(tags)}')
for t in tags:
    if 'width' in t:
        print('Width style:', t[:120])
