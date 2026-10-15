import re

with open(r'C:\Users\pcvis\.gemini\antigravity\scratch\swayam-progress\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add responsive style helper in head if not already there
responsive_css = '''
<style>
  html, body {
    overflow-x: hidden !important;
    max-width: 100vw !important;
    box-sizing: border-box !important;
  }
  *, *::before, *::after {
    box-sizing: border-box;
  }
  @media (min-width: 768px) {
    .md\\:block { display: block !important; }
    .md\\:hidden { display: none !important; }
  }
  @media (max-width: 767px) {
    .md\\:hidden { display: block !important; }
    .md\\:block { display: none !important; }
  }
  [data-state=open] > button > svg,
  button[data-state=open] > svg {
    transform: rotate(180deg);
  }
</style>
'''

if '/* responsive helper */' not in html:
    html = html.replace('</head>', f'<!-- responsive helper -->\n{responsive_css}\n</head>')

# 2. Assignment items matching user screenshot
assignment_items = [
    ('Week 1: Assignment 1', '-'),
    ('Week 2 : Assignment 2', '90'),
    ('Week 3: Assignment 3', '90'),
    ('Week 4: Assignment 4', '90'),
    ('Week 5: Assignment 5', '90'),
    ('Week 6: Assignment 6', '90'),
    ('Week 7: Assignment 7', '-'),
    ('Week 8: Assignment 8', '-'),
    ('Week 9: Assignment 9', '-'),
    ('Week 10: Assignment 10', '100'),
    ('Week 11: Assignment 11', '100'),
    ('Week 12: Assignment 12', '100')
]

# Mobile cards matching screenshot exactly:
# Screenshot shows:
# Title                           Score
# Week 1: Assignment 1                -
cards = []
for title, score in assignment_items:
    c = f'''          <div class="preview-card-light border border-slate-200 dark:border-gray-700 rounded-2xl p-4 bg-white dark:bg-[#1E2535] shadow-xs w-full">
            <div class="flex items-center justify-between text-xs text-gray-500 dark:text-gray-400 mb-1">
              <span class="font-normal">Title</span>
              <span class="font-normal text-right">Score</span>
            </div>
            <div class="flex items-center justify-between">
              <span class="text-sm font-semibold text-gray-900 dark:text-gray-100">{title}</span>
              <span class="text-sm font-bold text-gray-900 dark:text-gray-100 text-right">{score}</span>
            </div>
          </div>'''
    cards.append(c)

mobile_cards_html = '\n'.join(cards)

# Desktop rows
rows = []
for title, score in assignment_items:
    r = f'''                <tr data-slot="table-row" class="hover:bg-muted/50 border-b transition-colors">
                  <td data-slot="table-cell" class="p-3 align-middle whitespace-nowrap pl-8 font-medium text-sm text-foreground">{title}</td>
                  <td data-slot="table-cell" class="p-3 align-middle whitespace-nowrap pr-8 text-right font-bold text-sm text-foreground">{score}</td>
                </tr>'''
    rows.append(r)

desktop_rows_html = '\n'.join(rows)

assignment_accordion_block = f'''<div data-state="open" data-orientation="vertical" data-slot="accordion-item" class="w-full rounded-md border">
  <h3 data-orientation="vertical" data-state="open" class="flex">
    <button type="button" aria-expanded="true" data-state="open" data-orientation="vertical" id="radix-_r_8_" data-slot="accordion-trigger" class="focus-visible:border-ring focus-visible:ring-ring/50 flex flex-1 items-start justify-between gap-4 text-left transition-all outline-none focus-visible:ring-[3px] disabled:pointer-events-none disabled:opacity-50 w-full rounded-md px-4 py-4 text-base leading-relaxed font-medium tracking-normal not-italic preview-panel-light hover-styles data-[state=open]:rounded-b-none data-[state=open]:border-b" data-radix-collection-item="">
      Assignment Scores
      <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-chevron-down text-muted-foreground pointer-events-none size-4 shrink-0 translate-y-0.5 transition-transform duration-200" aria-hidden="true">
        <path d="m6 9 6 6 6-6"></path>
      </svg>
    </button>
  </h3>
  <div data-state="open" id="radix-assignment-content" role="region" aria-labelledby="radix-_r_8_" data-orientation="vertical" data-slot="accordion-content" class="overflow-hidden text-sm w-full">
    <div class="pt-0 pb-4 w-full">
      <div class="w-full overflow-hidden">
        
        <!-- Desktop Table View -->
        <div class="hidden md:block max-h-[350px] overflow-x-auto overflow-y-auto rounded-md">
          <p class="py-2.5 pl-4 text-sm/[1.43] font-normal tracking-[0.17px] preview-link-light border-b text-blue-600">
            Note : Please scroll down to see all assignment scores
          </p>
          <div data-slot="table-container" class="relative w-full overflow-x-auto">
            <table data-slot="table" class="caption-bottom text-sm w-full">
              <colgroup>
                <col class="w-[75%]">
                <col class="w-[25%]">
              </colgroup>
              <thead data-slot="table-header" class="[&_tr]:border-b bg-background sticky top-0 z-10">
                <tr data-slot="table-row" class="hover:bg-muted/50 border-b transition-colors">
                  <th data-slot="table-head" class="h-10 px-2 text-left align-middle font-medium whitespace-nowrap text-muted-foreground pl-8">
                    Title
                  </th>
                  <th data-slot="table-head" class="h-10 px-2 text-right align-middle font-medium whitespace-nowrap text-muted-foreground pr-8">
                    Score
                  </th>
                </tr>
              </thead>
              <tbody data-slot="table-body" class="[&_tr:last-child]:border-0">
{desktop_rows_html}
              </tbody>
            </table>
          </div>
        </div>

        <!-- Mobile Card View (Matches Uploaded Screenshot Exactly) -->
        <div class="md:hidden space-y-3 px-3 pt-3 pb-2 max-h-[350px] overflow-y-auto w-full">
          <p class="text-sm font-normal tracking-[0.17px] text-blue-600 dark:text-blue-400 mb-3 pl-1">
            Note : Please scroll down to see all assignment scores
          </p>
{mobile_cards_html}
        </div>

      </div>
    </div>
  </div>
</div>'''

# Replace assignment accordion in html
pos1 = html.find('id="radix-_r_8_"')
start_item = html.rfind('<div data-state=', 0, pos1)
pos2 = html.find('id="radix-_r_a_"')
end_item = html.rfind('<div data-state=', 0, pos2)

html = html[:start_item] + assignment_accordion_block + '\n                      ' + html[end_item:]

# Fix any unescaped bracket in buttons
html = html.replace('[&[data-state=open]>svg]', '[&amp;[data-state=open]&gt;svg]')

with open(r'C:\Users\pcvis\.gemini\antigravity\scratch\swayam-progress\index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Applied card design successfully!')
