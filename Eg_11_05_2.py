# Escape Character
'''
If you want a special regular expression character to just behave normally 
(most of the time) you prefix it with '\'
'''

import re
x = 'We just received $10.00 for cookies.'  
y = re.findall('\$[0-9.]+',x) # without \, code will move to the end of the line
print(y)
