# FINE TUNING STRING EXTRACTION
import re
x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+@\S+',x) # All non-space char with @ in them
print(y,'\n')


print('Using Parenthesis')
# Parentheses are not part of the match - but they tell where to start and stop what string to extract

y = re.findall('^From (\S+@\S+)',x) # Line should start with from. start extracting for non-space char
#                                   with @ in it an stop extracting on the last non-space char 
print(y)
