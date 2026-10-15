import re

with open(r'C:\Users\pcvis\.gemini\antigravity\scratch\swayam-progress\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect the width of the card container
pos = text.find('radix-assignment-content')
snippet = text[pos-100:pos+1500]
print(snippet[:600])
