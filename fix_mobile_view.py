with open(r'C:\Users\pcvis\.gemini\antigravity\scratch\swayam-progress\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Close Unit Wise Progress accordion by default so Assignment Scores is the main open one as in the screenshot
# Find radix-_r_a_ parent item
pos = html.find('id="radix-_r_a_"')
item_start = html.rfind('<div data-state=', 0, pos)
# change data-state="open" to data-state="closed" in this accordion item
html = html[:item_start] + html[item_start:pos].replace('data-state="open"', 'data-state="closed"') + html[pos:]
# Also on the button
btn_start = html.rfind('<button', 0, pos)
btn_end = html.find('>', pos)
html = html[:btn_start] + html[btn_start:btn_end].replace('data-state="open"', 'data-state="closed"').replace('aria-expanded="true"', 'aria-expanded="false"') + html[btn_end:]

# And the content radix-_r_b_
pos_b = html.find('id="radix-_r_b_"')
if pos_b != -1:
    div_start = html.rfind('<div', 0, pos_b)
    div_end = html.find('>', pos_b)
    # add hidden and style="display: none;"
    old_tag = html[div_start:div_end+1]
    new_tag = old_tag.replace('data-state="open"', 'data-state="closed"').replace('class="', 'class="hidden ')
    if 'style="' in new_tag:
        new_tag = new_tag.replace('style="', 'style="display: none; ')
    else:
        new_tag = new_tag.replace('>', ' style="display: none;">')
    html = html[:div_start] + new_tag + html[div_end+1:]

# 2. Add overflow-x-hidden to body and html
html = html.replace('<html lang="en"', '<html lang="en" class="overflow-x-hidden"')
html = html.replace('<body class="antialiased"', '<body class="antialiased overflow-x-hidden"')

with open(r'C:\Users\pcvis\.gemini\antigravity\scratch\swayam-progress\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Updated successfully!')
