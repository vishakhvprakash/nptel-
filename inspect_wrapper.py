import re

with open(r'C:\Users\pcvis\.gemini\antigravity\scratch\swayam-progress\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's inspect line by line from progress-page-wrapper
pos = html.find('progress-page-wrapper')
print('progress-page-wrapper start:', pos)
print(html[pos:pos+500])
