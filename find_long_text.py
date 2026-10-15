from html.parser import HTMLParser

with open(r'C:\Users\pcvis\.gemini\antigravity\scratch\swayam-progress\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's inspect all tables, inputs, text, divs inside the scroll area
pos_scroll = html.find('data-slot="scroll-area"')
end_scroll = html.find('</nav>', pos_scroll) # or end of scroll area
scroll_html = html[pos_scroll:]

import re
# check any text that has long strings without spaces
words = re.findall(r'>([^<]+)<', scroll_html)
for w in words:
    w_strip = w.strip()
    if len(w_strip) > 35:
        print('Long text:', w_strip[:60])
