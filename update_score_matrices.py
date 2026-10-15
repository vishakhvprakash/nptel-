import re

# Base template to use
with open('vishakh.html', 'r', encoding='utf-8') as f:
    template = f.read()

# Define the 5 student profiles with custom score matrices
students = [
    {
        'id': 'vishakh',
        'name': 'Vishakh V Prakash',
        'first_name': 'Vishakh',
        'email': 'vishakhvprakash@gmail.com',
        'avatar': 'VH',
        'filename': 'vishakh.html',
        'overall_progress': '93.33%',
        'overall_dash': '293.2045947',
        'assignment_scores': {
            1: '-',
            2: '90',
            3: '90',
            4: '90',
            5: '90',
            6: '90',
            7: '-',
            8: '-',
            9: '-',
            10: '100',
            11: '100',
            12: '100',
        },
        'unit_progress': {
            1: ('100%', '100%'),
            2: ('100%', '90%'),
            3: ('100%', '90%'),
            4: ('100%', '90%'),
            5: ('100%', '90%'),
            6: ('100%', '90%'),
            7: ('100%', '0%'),
            8: ('100%', '0%'),
            9: ('100%', '0%'),
            10: ('100%', '100%'),
            11: ('100%', '100%'),
            12: ('87.5%', '100%'),
        }
    },
    {
        'id': 'vishnu',
        'name': 'Vishnu S',
        'first_name': 'Vishnu',
        'email': 'vishnus123@gmail.com',
        'avatar': 'VS',
        'filename': 'vishnu.html',
        'overall_progress': '91.67%',
        'overall_dash': '287.99',
        'assignment_scores': {
            1: '100',
            2: '85',
            3: '92',
            4: '88',
            5: '95',
            6: '90',
            7: '-',
            8: '-',
            9: '-',
            10: '95',
            11: '100',
            12: '92',
        },
        'unit_progress': {
            1: ('100%', '100%'),
            2: ('100%', '85%'),
            3: ('100%', '92%'),
            4: ('100%', '88%'),
            5: ('100%', '95%'),
            6: ('100%', '90%'),
            7: ('100%', '0%'),
            8: ('100%', '0%'),
            9: ('100%', '0%'),
            10: ('100%', '95%'),
            11: ('100%', '100%'),
            12: ('87.5%', '92%'),
        }
    },
    {
        'id': 'abhijith',
        'name': 'Abhijith G',
        'first_name': 'Abhijith',
        'email': 'abhijithg69@gmail.com',
        'avatar': 'AG',
        'filename': 'abhijith.html',
        'overall_progress': '95.00%',
        'overall_dash': '298.45',
        'assignment_scores': {
            1: '95',
            2: '94',
            3: '96',
            4: '92',
            5: '90',
            6: '98',
            7: '-',
            8: '-',
            9: '-',
            10: '100',
            11: '100',
            12: '95',
        },
        'unit_progress': {
            1: ('100%', '95%'),
            2: ('100%', '94%'),
            3: ('100%', '96%'),
            4: ('100%', '92%'),
            5: ('100%', '90%'),
            6: ('100%', '98%'),
            7: ('100%', '0%'),
            8: ('100%', '0%'),
            9: ('100%', '0%'),
            10: ('100%', '100%'),
            11: ('100%', '100%'),
            12: ('100%', '95%'),
        }
    },
    {
        'id': 'jijohns',
        'name': 'Jijohns Johnson',
        'first_name': 'Jijohns',
        'email': 'jijohnsjohnson178@gmail.com',
        'avatar': 'JJ',
        'filename': 'jijohns.html',
        'overall_progress': '89.17%',
        'overall_dash': '280.13',
        'assignment_scores': {
            1: '-',
            2: '88',
            3: '85',
            4: '92',
            5: '86',
            6: '94',
            7: '-',
            8: '-',
            9: '-',
            10: '100',
            11: '90',
            12: '90',
        },
        'unit_progress': {
            1: ('100%', '-'),
            2: ('100%', '88%'),
            3: ('100%', '85%'),
            4: ('100%', '92%'),
            5: ('100%', '86%'),
            6: ('100%', '94%'),
            7: ('100%', '0%'),
            8: ('100%', '0%'),
            9: ('100%', '0%'),
            10: ('100%', '100%'),
            11: ('100%', '90%'),
            12: ('87.5%', '90%'),
        }
    },
    {
        'id': 'vaishnav',
        'name': 'Vaishnav Biju',
        'first_name': 'Vaishnav',
        'email': 'vaishnabiju345@gmail.com',
        'avatar': 'VB',
        'filename': 'vaishnav.html',
        'overall_progress': '86.67%',
        'overall_dash': '272.27',
        'assignment_scores': {
            1: '80',
            2: '92',
            3: '88',
            4: '95',
            5: '82',
            6: '88',
            7: '-',
            8: '-',
            9: '-',
            10: '90',
            11: '95',
            12: '85',
        },
        'unit_progress': {
            1: ('100%', '80%'),
            2: ('100%', '92%'),
            3: ('100%', '88%'),
            4: ('100%', '95%'),
            5: ('100%', '82%'),
            6: ('100%', '88%'),
            7: ('100%', '0%'),
            8: ('100%', '0%'),
            9: ('100%', '0%'),
            10: ('100%', '90%'),
            11: ('100%', '95%'),
            12: ('87.5%', '85%'),
        }
    }
]

def generate_assignment_scores_desktop(scores):
    html = '''        <!-- Desktop Table View -->
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
'''
    for w in range(1, 13):
        # Week 2 has space before colon matching NPTEL original
        title = f"Week {w} : Assignment {w}" if w == 2 else f"Week {w}: Assignment {w}"
        val = scores.get(w, '-')
        html += f'''                <tr data-slot="table-row" class="hover:bg-muted/50 border-b transition-colors">
                  <td data-slot="table-cell" class="p-3 align-middle whitespace-nowrap pl-8 font-medium text-sm text-foreground">{title}</td>
                  <td data-slot="table-cell" class="p-3 align-middle whitespace-nowrap pr-8 text-right font-bold text-sm text-foreground">{val}</td>
                </tr>
'''
    html += '''              </tbody>
            </table>
          </div>
        </div>'''
    return html

def generate_assignment_scores_mobile(scores):
    html = '''        <!-- Mobile Card View (Matches Uploaded Screenshot Exactly) -->
        <div class="md:hidden space-y-3 px-3 pt-3 pb-2 max-h-[350px] overflow-y-auto w-full">
          <p class="text-sm font-normal tracking-[0.17px] text-blue-600 dark:text-blue-400 mb-3 pl-1">
            Note : Please scroll down to see all assignment scores
          </p>
'''
    for w in range(1, 13):
        title = f"Week {w} : Assignment {w}" if w == 2 else f"Week {w}: Assignment {w}"
        val = scores.get(w, '-')
        html += f'''          <div class="preview-card-light border border-slate-200 dark:border-gray-700 rounded-2xl p-4 bg-white dark:bg-[#1E2535] shadow-xs w-full">
            <div class="flex items-center justify-between text-xs text-gray-500 dark:text-gray-400 mb-1">
              <span class="font-normal">Title</span>
              <span class="font-normal text-right">Score</span>
            </div>
            <div class="flex items-center justify-between">
              <span class="text-sm font-semibold text-gray-900 dark:text-gray-100">{title}</span>
              <span class="text-sm font-bold text-gray-900 dark:text-gray-100 text-right">{val}</span>
            </div>
          </div>
'''
    html += '        </div>'
    return html

def generate_unit_wise_desktop(unit_prog):
    html = '''<div class="hidden md:block max-h-[350px] overflow-x-auto overflow-y-auto rounded-md"><p class="py-2 pl-4 text-sm/[1.43] font-normal tracking-[0.17px] preview-link-light border-b">Note : The latest Course and Unit progress will be reflected within 24 hours.</p><div data-slot="table-container" class="relative w-full overflow-x-auto"><table data-slot="table" class="caption-bottom text-sm w-full"><colgroup><col class="w-[40%]"><col class="w-[30%]"><col class="w-[30%]"></colgroup><thead data-slot="table-header" class="[&amp;_tr]:border-b bg-background sticky top-0 z-10"><tr data-slot="table-row" class="hover:bg-muted/50 data-[state=selected]:bg-muted border-b transition-colors"><th data-slot="table-head" class="h-10 px-2 text-left align-middle font-medium whitespace-nowrap [&amp;:has([role=checkbox])]:pr-0 [&amp;&gt;[role=checkbox]]:translate-y-[2px] text-muted-foreground pl-8">Unit</th><th data-slot="table-head" class="h-10 px-2 text-left align-middle font-medium whitespace-nowrap [&amp;:has([role=checkbox])]:pr-0 [&amp;&gt;[role=checkbox]]:translate-y-[2px] text-muted-foreground">Lesson Progress</th><th data-slot="table-head" class="h-10 px-2 text-left align-middle font-medium whitespace-nowrap [&amp;:has([role=checkbox])]:pr-0 [&amp;&gt;[role=checkbox]]:translate-y-[2px] text-muted-foreground">Assignments Progress</th></tr></thead><tbody data-slot="table-body" class="[&amp;_tr:last-child]:border-0">'''
    
    # Static prefix units
    html += '''<tr data-slot="table-row" class="hover:bg-muted/50 data-[state=selected]:bg-muted border-b transition-colors"><td data-slot="table-cell" class="p-2 align-middle whitespace-nowrap [&amp;:has([role=checkbox])]:pr-0 [&amp;&gt;[role=checkbox]]:translate-y-[2px] truncate pl-8">About NPTEL</td><td data-slot="table-cell" class="p-2 align-middle whitespace-nowrap [&amp;:has([role=checkbox])]:pr-0 [&amp;&gt;[role=checkbox]]:translate-y-[2px]"><div class="flex items-center gap-2"><div class="bg-muted relative h-2 w-1/2 overflow-hidden rounded-full" role="progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100" aria-label="Lesson progress"><div class="h-full rounded-full bg-gradient-to-r from-green-500 to-green-600 transition-all duration-500" style="width: 100%;"></div></div><span class="text-foreground text-xs font-medium">100%</span></div></td><td data-slot="table-cell" class="p-2 align-middle whitespace-nowrap [&amp;:has([role=checkbox])]:pr-0 [&amp;&gt;[role=checkbox]]:translate-y-[2px]"><div class="flex items-center gap-2">-</div></td></tr>'''
    html += '''<tr data-slot="table-row" class="hover:bg-muted/50 data-[state=selected]:bg-muted border-b transition-colors"><td data-slot="table-cell" class="p-2 align-middle whitespace-nowrap [&amp;:has([role=checkbox])]:pr-0 [&amp;&gt;[role=checkbox]]:translate-y-[2px] truncate pl-8">How does an NPTEL online course work?</td><td data-slot="table-cell" class="p-2 align-middle whitespace-nowrap [&amp;:has([role=checkbox])]:pr-0 [&amp;&gt;[role=checkbox]]:translate-y-[2px]"><div class="flex items-center gap-2"><div class="bg-muted relative h-2 w-1/2 overflow-hidden rounded-full" role="progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100" aria-label="Lesson progress"><div class="h-full rounded-full bg-gradient-to-r from-green-500 to-green-600 transition-all duration-500" style="width: 100%;"></div></div><span class="text-foreground text-xs font-medium">100%</span></div></td><td data-slot="table-cell" class="p-2 align-middle whitespace-nowrap [&amp;:has([role=checkbox])]:pr-0 [&amp;&gt;[role=checkbox]]:translate-y-[2px]"><div class="flex items-center gap-2">-</div></td></tr>'''

    # Weeks 1 to 12
    for w in range(1, 13):
        # Case match
        if w == 4:
            unit_name = "week 4"
        elif w == 10:
            unit_name = "week 10"
        else:
            unit_name = f"Week {w}"
        
        lesson_pct, assign_pct = unit_prog[w]
        
        # Lesson cell
        lesson_val = float(lesson_pct.replace('%', ''))
        lesson_cell = f'''<div class="flex items-center gap-2"><div class="bg-muted relative h-2 w-1/2 overflow-hidden rounded-full" role="progressbar" aria-valuenow="{lesson_val}" aria-valuemin="0" aria-valuemax="100" aria-label="Lesson progress"><div class="h-full rounded-full bg-gradient-to-r from-green-500 to-green-600 transition-all duration-500" style="width: {lesson_pct};"></div></div><span class="text-foreground text-xs font-medium">{lesson_pct}</span></div>'''
        
        # Assignment cell
        if assign_pct == '-':
            assign_cell = '<div class="flex items-center gap-2">-</div>'
        else:
            assign_val = float(assign_pct.replace('%', ''))
            assign_cell = f'''<div class="flex items-center gap-2"><div class="bg-muted relative h-2 w-1/2 overflow-hidden rounded-full" role="progressbar" aria-valuenow="{assign_val}" aria-valuemin="0" aria-valuemax="100" aria-label="Lesson progress"><div class="h-full rounded-full bg-gradient-to-r from-[#24C246] to-[#24C246] transition-all duration-500" style="width: {assign_pct};"></div></div><span class="text-foreground text-xs font-medium">{assign_pct}</span></div>'''
            
        html += f'''<tr data-slot="table-row" class="hover:bg-muted/50 data-[state=selected]:bg-muted border-b transition-colors"><td data-slot="table-cell" class="p-2 align-middle whitespace-nowrap [&amp;:has([role=checkbox])]:pr-0 [&amp;&gt;[role=checkbox]]:translate-y-[2px] truncate pl-8">{unit_name}</td><td data-slot="table-cell" class="p-2 align-middle whitespace-nowrap [&amp;:has([role=checkbox])]:pr-0 [&amp;&gt;[role=checkbox]]:translate-y-[2px]">{lesson_cell}</td><td data-slot="table-cell" class="p-2 align-middle whitespace-nowrap [&amp;:has([role=checkbox])]:pr-0 [&amp;&gt;[role=checkbox]]:translate-y-[2px]">{assign_cell}</td></tr>'''

    # Static suffix units
    html += '''<tr data-slot="table-row" class="hover:bg-muted/50 data-[state=selected]:bg-muted border-b transition-colors"><td data-slot="table-cell" class="p-2 align-middle whitespace-nowrap [&amp;:has([role=checkbox])]:pr-0 [&amp;&gt;[role=checkbox]]:translate-y-[2px] truncate pl-8">Download Videos</td><td data-slot="table-cell" class="p-2 align-middle whitespace-nowrap [&amp;:has([role=checkbox])]:pr-0 [&amp;&gt;[role=checkbox]]:translate-y-[2px]"><div class="flex items-center gap-2"><div class="bg-muted relative h-2 w-1/2 overflow-hidden rounded-full" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" aria-label="Lesson progress"><div class="h-full rounded-full bg-gradient-to-r from-green-500 to-green-600 transition-all duration-500" style="width: 0%;"></div></div><span class="text-foreground text-xs font-medium">0%</span></div></td><td data-slot="table-cell" class="p-2 align-middle whitespace-nowrap [&amp;:has([role=checkbox])]:pr-0 [&amp;&gt;[role=checkbox]]:translate-y-[2px]"><div class="flex items-center gap-2">-</div></td></tr>'''
    html += '''<tr data-slot="table-row" class="hover:bg-muted/50 data-[state=selected]:bg-muted border-b transition-colors"><td data-slot="table-cell" class="p-2 align-middle whitespace-nowrap [&amp;:has([role=checkbox])]:pr-0 [&amp;&gt;[role=checkbox]]:translate-y-[2px] truncate pl-8">Books</td><td data-slot="table-cell" class="p-2 align-middle whitespace-nowrap [&amp;:has([role=checkbox])]:pr-0 [&amp;&gt;[role=checkbox]]:translate-y-[2px]"><div class="flex items-center gap-2"><div class="bg-muted relative h-2 w-1/2 overflow-hidden rounded-full" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" aria-label="Lesson progress"><div class="h-full rounded-full bg-gradient-to-r from-green-500 to-green-600 transition-all duration-500" style="width: 0%;"></div></div><span class="text-foreground text-xs font-medium">0%</span></div></td><td data-slot="table-cell" class="p-2 align-middle whitespace-nowrap [&amp;:has([role=checkbox])]:pr-0 [&amp;&gt;[role=checkbox]]:translate-y-[2px]"><div class="flex items-center gap-2">-</div></td></tr>'''
    html += '''<tr data-slot="table-row" class="hover:bg-muted/50 data-[state=selected]:bg-muted border-b transition-colors"><td data-slot="table-cell" class="p-2 align-middle whitespace-nowrap [&amp;:has([role=checkbox])]:pr-0 [&amp;&gt;[role=checkbox]]:translate-y-[2px] truncate pl-8">Text Transcripts</td><td data-slot="table-cell" class="p-2 align-middle whitespace-nowrap [&amp;:has([role=checkbox])]:pr-0 [&amp;&gt;[role=checkbox]]:translate-y-[2px]"><div class="flex items-center gap-2"><div class="bg-muted relative h-2 w-1/2 overflow-hidden rounded-full" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" aria-label="Lesson progress"><div class="h-full rounded-full bg-gradient-to-r from-green-500 to-green-600 transition-all duration-500" style="width: 0%;"></div></div><span class="text-foreground text-xs font-medium">0%</span></div></td><td data-slot="table-cell" class="p-2 align-middle whitespace-nowrap [&amp;:has([role=checkbox])]:pr-0 [&amp;&gt;[role=checkbox]]:translate-y-[2px]"><div class="flex items-center gap-2">-</div></td></tr>'''

    html += '''</tbody></table></div></div>'''
    return html

def generate_unit_wise_mobile(unit_prog):
    html = '''<div class="md:hidden space-y-4 px-4 pt-4 pb-2 max-h-[350px] overflow-y-auto"><p class="text-sm/[1.43] font-normal tracking-[0.17px] preview-link-light">Note : The latest Course and Unit progress will be reflected within 24 hours.</p>'''
    
    # Static prefix
    html += '''<div class="preview-card-light border rounded-lg p-4 shadow-sm"><h4 class="font-medium text-base mb-3 break-words whitespace-normal preview-text-primary-light">About NPTEL</h4><div class="space-y-3"><div><p class="text-xs preview-text-muted-light mb-1.5">Lesson Progress</p><div class="flex items-center gap-2 w-full"><div class="bg-muted relative h-2 flex-1 overflow-hidden rounded-full" role="progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100" aria-label="Lesson progress"><div class="h-full rounded-full bg-gradient-to-r from-green-500 to-green-600 transition-all duration-500" style="width: 100%;"></div></div><span class="text-foreground text-xs font-medium whitespace-nowrap">100%</span></div></div><div><p class="text-xs preview-text-muted-light mb-1.5">Assignments Progress</p><span class="text-sm preview-text-muted-light">-</span></div></div></div>'''
    html += '''<div class="preview-card-light border rounded-lg p-4 shadow-sm"><h4 class="font-medium text-base mb-3 break-words whitespace-normal preview-text-primary-light">How does an NPTEL online course work?</h4><div class="space-y-3"><div><p class="text-xs preview-text-muted-light mb-1.5">Lesson Progress</p><div class="flex items-center gap-2 w-full"><div class="bg-muted relative h-2 flex-1 overflow-hidden rounded-full" role="progressbar" aria-valuenow="100" aria-valuemin="0" aria-valuemax="100" aria-label="Lesson progress"><div class="h-full rounded-full bg-gradient-to-r from-green-500 to-green-600 transition-all duration-500" style="width: 100%;"></div></div><span class="text-foreground text-xs font-medium whitespace-nowrap">100%</span></div></div><div><p class="text-xs preview-text-muted-light mb-1.5">Assignments Progress</p><span class="text-sm preview-text-muted-light">-</span></div></div></div>'''

    for w in range(1, 13):
        unit_name = "week 4" if w == 4 else ("week 10" if w == 10 else f"Week {w}")
        lesson_pct, assign_pct = unit_prog[w]
        lesson_val = float(lesson_pct.replace('%', ''))
        
        if assign_pct == '-':
            assign_block = '<span class="text-sm preview-text-muted-light">-</span>'
        else:
            assign_val = float(assign_pct.replace('%', ''))
            assign_block = f'''<div class="flex items-center gap-2 w-full"><div class="bg-muted relative h-2 flex-1 overflow-hidden rounded-full" role="progressbar" aria-valuenow="{assign_val}" aria-valuemin="0" aria-valuemax="100" aria-label="Assessment progress"><div class="h-full rounded-full bg-gradient-to-r from-[#24C246] to-[#24C246] transition-all duration-500" style="width: {assign_pct};"></div></div><span class="text-foreground text-xs font-medium whitespace-nowrap">{assign_pct}</span></div>'''
            
        html += f'''<div class="preview-card-light border rounded-lg p-4 shadow-sm"><h4 class="font-medium text-base mb-3 break-words whitespace-normal preview-text-primary-light">{unit_name}</h4><div class="space-y-3"><div><p class="text-xs preview-text-muted-light mb-1.5">Lesson Progress</p><div class="flex items-center gap-2 w-full"><div class="bg-muted relative h-2 flex-1 overflow-hidden rounded-full" role="progressbar" aria-valuenow="{lesson_val}" aria-valuemin="0" aria-valuemax="100" aria-label="Lesson progress"><div class="h-full rounded-full bg-gradient-to-r from-green-500 to-green-600 transition-all duration-500" style="width: {lesson_pct};"></div></div><span class="text-foreground text-xs font-medium whitespace-nowrap">{lesson_pct}</span></div></div><div><p class="text-xs preview-text-muted-light mb-1.5">Assignments Progress</p>{assign_block}</div></div></div>'''

    # Static suffix
    html += '''<div class="preview-card-light border rounded-lg p-4 shadow-sm"><h4 class="font-medium text-base mb-3 break-words whitespace-normal preview-text-primary-light">Download Videos</h4><div class="space-y-3"><div><p class="text-xs preview-text-muted-light mb-1.5">Lesson Progress</p><div class="flex items-center gap-2 w-full"><div class="bg-muted relative h-2 flex-1 overflow-hidden rounded-full" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" aria-label="Lesson progress"><div class="h-full rounded-full bg-gradient-to-r from-green-500 to-green-600 transition-all duration-500" style="width: 0%;"></div></div><span class="text-foreground text-xs font-medium whitespace-nowrap">0%</span></div></div><div><p class="text-xs preview-text-muted-light mb-1.5">Assignments Progress</p><span class="text-sm preview-text-muted-light">-</span></div></div></div>'''
    html += '''<div class="preview-card-light border rounded-lg p-4 shadow-sm"><h4 class="font-medium text-base mb-3 break-words whitespace-normal preview-text-primary-light">Books</h4><div class="space-y-3"><div><p class="text-xs preview-text-muted-light mb-1.5">Lesson Progress</p><div class="flex items-center gap-2 w-full"><div class="bg-muted relative h-2 flex-1 overflow-hidden rounded-full" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" aria-label="Lesson progress"><div class="h-full rounded-full bg-gradient-to-r from-green-500 to-green-600 transition-all duration-500" style="width: 0%;"></div></div><span class="text-foreground text-xs font-medium whitespace-nowrap">0%</span></div></div><div><p class="text-xs preview-text-muted-light mb-1.5">Assignments Progress</p><span class="text-sm preview-text-muted-light">-</span></div></div></div>'''
    html += '''<div class="preview-card-light border rounded-lg p-4 shadow-sm"><h4 class="font-medium text-base mb-3 break-words whitespace-normal preview-text-primary-light">Text Transcripts</h4><div class="space-y-3"><div><p class="text-xs preview-text-muted-light mb-1.5">Lesson Progress</p><div class="flex items-center gap-2 w-full"><div class="bg-muted relative h-2 flex-1 overflow-hidden rounded-full" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" aria-label="Lesson progress"><div class="h-full rounded-full bg-gradient-to-r from-green-500 to-green-600 transition-all duration-500" style="width: 0%;"></div></div><span class="text-foreground text-xs font-medium whitespace-nowrap">0%</span></div></div><div><p class="text-xs preview-text-muted-light mb-1.5">Assignments Progress</p><span class="text-sm preview-text-muted-light">-</span></div></div></div>'''
    html += '</div>'
    return html

# Now generate each student's page
for s in students:
    html = template
    
    # 1. Update User info
    html = html.replace('Vishakh V Prakash', s['name'])
    html = html.replace('vishakhvprakash@gmail.com', s['email'])
    html = html.replace('>VH<', f'>{s["avatar"]}<')
    html = html.replace('Hello Vishakh!', f'Hello {s["first_name"]}!')
    
    # 2. Update Overall Course Progress
    html = re.sub(
        r'<circle cx="60" cy="60" r="50" fill="none" stroke="#4CAF50" stroke-width="9" stroke-dasharray="[^"]*" stroke-linecap="round"></circle>',
        f'<circle cx="60" cy="60" r="50" fill="none" stroke="#4CAF50" stroke-width="9" stroke-dasharray="{s["overall_dash"]} 314.159" stroke-linecap="round"></circle>',
        html
    )
    # Desktop gauge percentage
    html = re.sub(
        r'<span class="absolute text-2xl font-semibold">[^<]*</span>',
        f'<span class="absolute text-2xl font-semibold">{s["overall_progress"]}</span>',
        html
    )
    # Mobile gauge percentage
    html = re.sub(
        r'<span class="absolute text-lg font-semibold">[^<]*</span>',
        f'<span class="absolute text-lg font-semibold">{s["overall_progress"]}</span>',
        html
    )
    # AI drawer greeting percentage
    html = re.sub(
        r'completed <strong>[^<]*</strong> of Deep Learning',
        f'completed <strong>{s["overall_progress"]}</strong> of Deep Learning',
        html
    )

    # 3. Replace Assignment Scores Desktop Table
    old_desktop_as_start = html.find('<!-- Desktop Table View -->')
    old_desktop_as_end = html.find('<!-- Mobile Card View', old_desktop_as_start)
    new_desktop_as = generate_assignment_scores_desktop(s['assignment_scores']) + '\n\n        '
    html = html[:old_desktop_as_start] + new_desktop_as + html[old_desktop_as_end:]

    # 4. Replace Assignment Scores Mobile Cards
    old_mobile_as_start = html.find('<!-- Mobile Card View (Matches Uploaded Screenshot Exactly) -->')
    # End is before radix-_r_a_ accordion trigger or closing div of radix-assignment-content
    old_mobile_as_end = html.find('</div>\n\n      </div>\n    </div>\n  </div>', old_mobile_as_start)
    new_mobile_as = generate_assignment_scores_mobile(s['assignment_scores']) + '\n\n'
    html = html[:old_mobile_as_start] + new_mobile_as + html[old_mobile_as_end:]

    # 5. Replace Unit Wise Progress Desktop Table
    u_idx = html.find('id="radix-_r_b_"')
    table_start = html.find('<div class="hidden md:block max-h-[350px]', u_idx)
    table_end = html.find('</table></div></div>', table_start) + len('</table></div></div>')
    new_unit_table = generate_unit_wise_desktop(s['unit_progress'])
    html = html[:table_start] + new_unit_table + html[table_end:]

    # 6. Replace Unit Wise Progress Mobile Cards
    u_idx2 = html.find('id="radix-_r_b_"')
    m_start = html.find('<div class="md:hidden space-y-4', u_idx2)
    m_end = html.find('</div></div></div></div><div data-state="closed"', m_start)
    if m_end == -1:
        # alternative pattern
        m_end = html.find('Text Transcripts</h4>', m_start)
        m_end = html.find('</div></div></div>', m_end) + len('</div></div></div>')
    else:
        m_end = m_end # matched
    new_unit_mobile = generate_unit_wise_mobile(s['unit_progress'])
    html = html[:m_start] + new_unit_mobile + html[m_end:]

    # Write out student file
    with open(s['filename'], 'w', encoding='utf-8') as out_f:
        out_f.write(html)
    
    print(f"Updated {s['filename']} -> Progress: {s['overall_progress']}, Scores: {s['assignment_scores']}")

print("All 5 files updated with unique course score matrices!")
