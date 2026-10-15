import re

with open(r'C:\Users\pcvis\.gemini\antigravity\scratch\swayam-progress\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

styles = re.findall(r'style="[^"]*(?:width|min-width)[^"]*"', text)
for s in styles[:20]:
    print(s)
