import re

# Read current index.html
with open('index.html', 'r', encoding='utf-8') as f:
    base_html = f.read()

# Make sure mobile avatar button has an ID and proper cursor
base_html = base_html.replace(
    'class="h-9 w-9 rounded-full bg-blue-600 dark:bg-blue-500 font-semibold text-white lg:hidden hover-styles">JJ</button>',
    'id="mobile-avatar-btn" class="h-9 w-9 rounded-full bg-blue-600 dark:bg-blue-500 font-semibold text-white lg:hidden hover-styles cursor-pointer">JJ</button>'
)

# Update the JS to attach event listener to both desktop and mobile avatar buttons
old_profile_js = """        // --- Profile Menu ---
        const profileBtn = document.getElementById('radix-_r_0_');
        const profileDropdown = document.getElementById('profile-dropdown');
        if (profileBtn && profileDropdown) {
          profileBtn.addEventListener('click', function(e) {
            e.stopPropagation();
            profileDropdown.classList.toggle('hidden');
          });
        }"""

new_profile_js = """        // --- Profile Menu (Desktop & Mobile) ---
        const profileBtns = [
          document.getElementById('radix-_r_0_'),
          document.getElementById('mobile-avatar-btn')
        ];
        const profileDropdown = document.getElementById('profile-dropdown');
        profileBtns.forEach(function(btn) {
          if (btn && profileDropdown) {
            btn.addEventListener('click', function(e) {
              e.stopPropagation();
              profileDropdown.classList.toggle('hidden');
            });
          }
        });"""

base_html = base_html.replace(old_profile_js, new_profile_js)

# Define the 5 users
users = [
    {
        'id': 'vishakh',
        'name': 'Vishakh V Prakash',
        'first_name': 'Vishakh',
        'email': 'vishakhvprakash@gmail.com',
        'avatar': 'VH',  # Exactly as in user's mobile screenshot media_1792094347483_ee98a267.png!
        'filename': 'vishakh.html'
    },
    {
        'id': 'vishnu',
        'name': 'Vishnu S',
        'first_name': 'Vishnu',
        'email': 'vishnus123@gmail.com',
        'avatar': 'VS',
        'filename': 'vishnu.html'
    },
    {
        'id': 'abhijith',
        'name': 'Abhijith G',
        'first_name': 'Abhijith',
        'email': 'abhijithg69@gmail.com',
        'avatar': 'AG',
        'filename': 'abhijith.html'
    },
    {
        'id': 'jijohns',
        'name': 'Jijohns Johnson',
        'first_name': 'Jijohns',
        'email': 'jijohnsjohnson178@gmail.com',
        'avatar': 'JJ',
        'filename': 'jijohns.html'
    },
    {
        'id': 'vaishnav',
        'name': 'Vaishnav Biju',
        'first_name': 'Vaishnav',
        'email': 'vaishnabiju345@gmail.com',
        'avatar': 'VB',
        'filename': 'vaishnav.html'
    }
]

# Generate each student's page
for user in users:
    html = base_html
    
    # 1. Replace emails
    html = html.replace('jijohnsjohnson178@gmail.com', user['email'])
    
    # 2. Replace names
    html = html.replace('Jijohns Johnson', user['name'])
    
    # 3. Replace avatars in buttons
    # Desktop avatar
    html = html.replace(
        'data-slot="dropdown-menu-trigger">JJ</button>',
        f'data-slot="dropdown-menu-trigger">{user["avatar"]}</button>'
    )
    # Mobile avatar
    html = html.replace(
        'id="mobile-avatar-btn" class="h-9 w-9 rounded-full bg-blue-600 dark:bg-blue-500 font-semibold text-white lg:hidden hover-styles cursor-pointer">JJ</button>',
        f'id="mobile-avatar-btn" class="h-9 w-9 rounded-full bg-blue-600 dark:bg-blue-500 font-semibold text-white lg:hidden hover-styles cursor-pointer">{user["avatar"]}</button>'
    )
    
    # 4. Replace AI greeting
    html = html.replace('Hello Jijohns!', f'Hello {user["first_name"]}!')
    
    # 5. Add a "Switch Profile" section in the dropdown menu
    switch_section = f'''        <div class="mt-2 inline-flex items-center px-2 py-0.5 rounded text-xs font-medium bg-blue-100 text-blue-800 dark:bg-blue-900/40 dark:text-blue-300">Enrolled Student</div>
      </div>
      <!-- Switch Profile Quick Access -->
      <div class="py-2 border-b border-gray-100 dark:border-gray-700 bg-gray-50/70 dark:bg-gray-800/40 px-2 rounded-lg my-1">
        <p class="px-2 pb-1.5 text-[11px] font-semibold text-gray-500 dark:text-gray-400 uppercase tracking-wider flex items-center justify-between">
          <span>Switch Student</span>
          <a href="index.html" class="text-blue-600 dark:text-blue-400 text-[10px] lowercase hover:underline font-normal">All Profiles</a>
        </p>
        <div class="space-y-1">
'''
    for other in users:
        is_active = (other['id'] == user['id'])
        active_class = "bg-blue-50 text-blue-700 font-medium dark:bg-blue-950/50 dark:text-blue-300 border-l-2 border-blue-600" if is_active else "text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700/50"
        check_icon = f'<span class="text-xs text-blue-600 font-bold">✓</span>' if is_active else f'<span class="text-[11px] text-gray-400 font-mono">{other["avatar"]}</span>'
        switch_section += f'''          <a href="{other['filename']}" class="flex items-center justify-between px-2.5 py-1.5 text-xs rounded-md {active_class} transition-colors">
            <span class="truncate pr-2">{other['name']}</span>
            {check_icon}
          </a>
'''
    switch_section += '''        </div>
      </div>
'''
    
    html = html.replace(
        '''        <div class="mt-2 inline-flex items-center px-2 py-0.5 rounded text-xs font-medium bg-blue-100 text-blue-800 dark:bg-blue-900/40 dark:text-blue-300">Enrolled Student</div>
      </div>''',
        switch_section
    )
    
    # Save student file
    with open(user['filename'], 'w', encoding='utf-8') as out_f:
        out_f.write(html)
    
    print(f"Generated {user['filename']} for {user['name']} ({user['email']}, Avatar: {user['avatar']})")

print("All 5 student files generated successfully!")
