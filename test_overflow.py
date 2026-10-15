import subprocess
import json

# Let's run chrome with remote debugging or evaluate widths
# Or simpler: write a tiny JS script embedded into index.html temporarily that logs element widths to console!
script = '''
<script>
window.addEventListener('load', function() {
  var all = document.querySelectorAll('*');
  for (var i = 0; i < all.length; i++) {
    var el = all[i];
    var rect = el.getBoundingClientRect();
    if (rect.width > 393) {
      console.log('OVERFLOW:', el.tagName, el.className, rect.width);
    }
  }
});
</script>
'''

with open(r'C:\Users\pcvis\.gemini\antigravity\scratch\swayam-progress\index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's inspect where radix-_r_b_ (Unit Wise Progress) is
pos_unit = html.find('id="radix-_r_a_"')
print('Unit Wise Progress header pos:', pos_unit)
