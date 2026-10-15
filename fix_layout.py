with open(r'C:\Users\pcvis\.gemini\antigravity\scratch\swayam-progress\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace min-width: 100%; display: table;
text = text.replace('style="min-width: 100%; display: table;"', 'style="width: 100%; min-width: 0;" class="w-full"')

# Also let's ensure .progress-page-wrapper has responsive horizontal padding:
# currently: px-6 -> let's make it px-3 sm:px-6
text = text.replace('px-6 pb-6', 'px-3 sm:px-6 pb-6')

# Also relative flex flex-col p-4 md:p-10 -> p-2 sm:p-4 md:p-10
text = text.replace('p-4 md:p-10', 'p-2 sm:p-4 md:p-10')

with open(r'C:\Users\pcvis\.gemini\antigravity\scratch\swayam-progress\index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Fixed layout successfully!')
