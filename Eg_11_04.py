# MATCHIING AND EXTRACTING DATA

import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x)  # means find 1 or more digit
print(y)


y = re.findall('[AEIOU]+',x)   # Finds all 'AEOIU' char in x
print(y)    # none in x so returns an empty set
